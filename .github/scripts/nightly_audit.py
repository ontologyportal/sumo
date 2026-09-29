#!/usr/bin/env python3
"""Run resumable Full SUMO audit chunks within a wall-clock budget."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import tempfile
import time
import xml.etree.ElementTree as ET

MANIFEST = Path(__file__).resolve().parents[1] / "full-sumo.txt"


def constituents(root, manifest=MANIFEST):
    names = [s.strip() for s in manifest.read_text().splitlines()
             if s.strip() and not s.lstrip().startswith("#")]
    if not names or len(names) != len(set(names)):
        raise ValueError("Full SUMO manifest must be nonempty and contain no duplicates")
    digest = hashlib.sha256()
    for name in names:
        path = root / name
        if Path(name).is_absolute() or ".." in Path(name).parts:
            raise ValueError(f"Invalid constituent: {name}")
        digest.update(name.encode() + b"\0")
        digest.update(hashlib.sha256(path.read_bytes()).digest())
    return names, digest.hexdigest()


def atomic_json(path, value):
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, indent=2) + "\n")
    temporary.replace(path)


def checkpoint(path, fingerprint):
    state = json.loads(path.read_text()) if path.exists() else {}
    if state.get("fingerprint") != fingerprint:
        state = {"version": 1, "fingerprint": fingerprint, "seed": 0, "next_step": 0}
    if state.get("version") != 1:
        raise ValueError("Unsupported checkpoint version")
    for key in ("seed", "next_step"):
        if type(state.get(key)) is not int or state[key] < 0:
            raise ValueError(f"Invalid checkpoint {key}")
    if state["seed"] > 0xffffffff:
        raise ValueError("Seed exceeds the CLI's u32 range")
    return state


def advance(state, result, count):
    start = state["next_step"]
    if result.get("seed") != state["seed"] or result.get("step") != start:
        raise ValueError("Audit result does not match the requested checkpoint")
    end, total = result.get("next_step"), result.get("total")
    if type(end) is not int or type(total) is not int or not (
        0 <= start <= end <= total and end <= start + count
    ):
        raise ValueError("Invalid audit progress")
    if total == 0 or end == start:
        raise ValueError("Audit made no progress; refusing to skip formulas")
    updated = dict(state)
    updated["next_step"] = end
    if end == total:
        if state["seed"] == 0xffffffff:
            raise ValueError("All supported seeds exhausted")
        updated["seed"] += 1
        updated["next_step"] = 0
    return updated


def execute(command, stdout, stderr, seconds, cwd):
    """Kill the entire process group on deadline; unfinished chunks are retried."""
    with subprocess.Popen(command, cwd=cwd, stdout=stdout, stderr=stderr,
                          start_new_session=True) as process:
        try:
            return process.wait(timeout=seconds)
        except subprocess.TimeoutExpired:
            os.killpg(process.pid, signal.SIGKILL)
            process.wait()
            return None


def contradiction_key(contradiction):
    """Stable identity for deduplicating the same cited axiom set."""
    return tuple(sorted(
        (a.get("file"), a.get("line"), a.get("kif"))
        for a in contradiction.get("axioms", [])
    ))


def contradiction_report(findings):
    """Render exact reproduction coordinates and cited axioms as Markdown."""
    lines = [
        "# Full SUMO contradiction report",
        "",
        "Open https://sigmakee.dev/audit, select the SUPr backend, and use",
        "the seed and start step shown for a contradiction below. Set both audit count fields to 1.",
        "",
    ]
    for number, finding in enumerate(findings, 1):
        lines.extend([
            f"## Contradiction {number}",
            "",
            f"- Seed: `{finding['seed']}`",
            f"- Start step: `{finding['step']}`",
            "- Axioms to check: `1`",
            "- Axioms per subproblem: `1`",
            "- Backend: `SUPr`",
            f"- Proof steps reported by Sigma: `{finding['proof_steps']}`",
            "",
            "### Cited source axioms",
            "",
        ])
        for axiom in finding["axioms"]:
            lines.extend([
                f"#### {axiom.get('file') or '?'}:{axiom.get('line') or '?'}",
                "",
                "```lisp",
                axiom.get("kif", ""),
                "```",
                "",
            ])
    if not findings:
        lines.extend(["No contradictions were reported in this run.", ""])
    return "\n".join(lines)


def run(args):
    root = Path.cwd()
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    names, fingerprint = constituents(root)
    state_path = output / "checkpoint.json"
    state = checkpoint(state_path, fingerprint)
    initial = dict(state)
    atomic_json(state_path, state)
    sumo = str(Path(args.sumo).resolve())
    completed = contradictions = 0
    interrupted = False
    findings = []
    seen_findings = set()
    try:
        with tempfile.TemporaryDirectory(prefix="sumo-audit-") as scratch:
            config = ET.Element("configuration")
            ET.SubElement(config, "preference", name="sumokbname", value="SUMO")
            ET.SubElement(config, "preference", name="editDir", value=scratch)
            ET.SubElement(config, "kb", name="SUMO").text = "\n"
            config_path = Path(scratch) / "config.xml"
            ET.ElementTree(config).write(config_path)
            base = [sumo, "--config", str(config_path), "--ugly"]
            load = base + [arg for name in names for arg in ("-f", name)] + ["load"]
            with (output / "load.log").open("w") as log:
                code = execute(load, log, subprocess.STDOUT, 1800, root)
            if code != 0 or not (Path(scratch) / "SUMO.lmdb").is_dir():
                raise RuntimeError("Full SUMO database load failed; see load.log")
            deadline = time.monotonic() + args.seconds
            while time.monotonic() < deadline:
                command = base + [
                    "audit", "--backend", "native", "--json",
                    "--seed", str(state["seed"]), "--step", str(state["next_step"]),
                    "--count", str(args.chunk_size), "--batch", "1",
                    "--timeout", str(args.timeout),
                ]
                print(f"Auditing seed {state['seed']}, step {state['next_step']}", flush=True)
                with (output / "chunk.log").open("w+") as result_file, (
                    output / "progress.log"
                ).open("a") as progress:
                    code = execute(command, result_file, progress,
                                   max(0.001, deadline - time.monotonic()), root)
                    if code is None:
                        interrupted = True
                        break
                    result_file.seek(0)
                    # Refuse malformed output or unexpected CLI failures, even if
                    # stdout contains something resembling a progress report.
                    result = json.load(result_file)
                if type(result.get("inconsistent")) is not bool or code != int(result["inconsistent"]):
                    raise RuntimeError(f"Unexpected audit exit status: {code}")
                updated = advance(state, result, args.chunk_size)
                for contradiction in result.get("contradictions", []):
                    # One formula per invocation makes this the exact sweep
                    # position whose selected neighborhood produced the proof.
                    contradiction["audit_seed"] = result["seed"]
                    contradiction["audit_step"] = result["step"]
                    key = contradiction_key(contradiction)
                    if key not in seen_findings:
                        seen_findings.add(key)
                        findings.append({
                            "seed": result["seed"],
                            "step": result["step"],
                            "proof_steps": contradiction.get("steps", 0),
                            "axioms": contradiction.get("axioms", []),
                        })
                with (output / "results.jsonl").open("a") as reports:
                    reports.write(json.dumps(result) + "\n")
                contradictions += len(result.get("contradictions", []))
                completed += result["next_step"] - result["step"]
                state = updated
                atomic_json(state_path, state)
    finally:
        report = contradiction_report(findings)
        (output / "contradictions.md").write_text(report)
        positions = "\n".join(
            f"- Seed `{f['seed']}`, step `{f['step']}`"
            for f in findings[:20]
        )
        if len(findings) > 20:
            positions += f"\n- ...and {len(findings) - 20} more in `contradictions.md`"
        if not positions:
            positions = "- None"
        summary = (
            "# Full SUMO nightly audit\n\n"
            f"- Started: seed {initial['seed']}, step {initial['next_step']}\n"
            f"- Resume: seed {state['seed']}, step {state['next_step']}\n"
            f"- Completed formula checks: {completed}\n"
            f"- Contradictions reported (may repeat across chunks): {contradictions}\n"
            f"- Distinct cited axiom sets: {len(findings)}\n"
            f"- Deadline interrupted a chunk: {interrupted}\n"
            f"- Full SUMO fingerprint: {fingerprint}\n\n"
            "## Reproduction positions\n\n"
            f"{positions}\n\n"
            "At https://sigmakee.dev/audit select SUPr, enter the seed and "
            "start step, and set both count fields to 1. The complete formatted "
            "report is in `contradictions.md` in the workflow artifact.\n\n"
            "An unfinished chunk is retried next night. Finding no contradiction "
            "does not certify consistency. See the job status for execution errors.\n"
        )
        (output / "summary.md").write_text(summary)
        if os.environ.get("GITHUB_STEP_SUMMARY"):
            with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as destination:
                destination.write(summary)
    # Findings fail the job for visibility, after all progress has been saved.
    return 1 if contradictions else 0


def positive(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return number


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sumo", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--seconds", type=positive, default=7200)
    parser.add_argument("--chunk-size", type=positive, default=1)
    parser.add_argument("--timeout", type=positive, default=10)
    raise SystemExit(run(parser.parse_args()))
