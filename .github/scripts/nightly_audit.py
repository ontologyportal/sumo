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


def engine_identity(root):
    """Match the source fingerprint stamped into the browser's WASM package."""
    paths = subprocess.check_output(
        ["git", "ls-files", "-z", "--", "Cargo.toml", "Cargo.lock", ".cargo", "crates"],
        cwd=root).decode().split("\0")
    digest = hashlib.sha256()
    for name in sorted(filter(None, paths)):
        digest.update(name.encode() + b"\0")
        digest.update(hashlib.sha256((root / name).read_bytes()).digest())
    return {
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root).decode().strip(),
        "fingerprint": digest.hexdigest(),
    }


def replay_metadata(root, names, fingerprint, timeout):
    return {
        "version": 1,
        "complete": False,
        "sumo_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root).decode().strip(),
        "run_id": os.environ.get("GITHUB_RUN_ID", ""),
        "run_attempt": int(os.environ.get("GITHUB_RUN_ATTEMPT", "1")),
        "engine": engine_identity(Path(os.environ.get("SIGMA_SOURCE_DIR", root.parent / "sigma-rs"))),
        "fingerprint": fingerprint,
        "constituents": [{"name": name, "sha256": hashlib.sha256((root / name).read_bytes()).hexdigest()}
                         for name in names],
        "config": {"backend": "native", "timeLimitSecs": timeout,
                   "maxSteps": 500000, "maxLits": 12, "forwardClose": True,
                   "wantProof": True, "profile": False, "selectionTolerancePct": 0},
        "request": {"count": 1, "batch": 1, "limit": 64},
    }


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


def checkpoint(path, fingerprint, engine_fingerprint):
    state = json.loads(path.read_text()) if path.exists() else {}
    if (state.get("fingerprint") != fingerprint
            or state.get("engine_fingerprint") != engine_fingerprint):
        state = {"version": 1, "fingerprint": fingerprint,
                 "engine_fingerprint": engine_fingerprint, "seed": 0, "next_step": 0,
                 "findings": []}
    if state.get("version") != 1:
        raise ValueError("Unsupported checkpoint version")
    for key in ("seed", "next_step"):
        if type(state.get(key)) is not int or state[key] < 0:
            raise ValueError(f"Invalid checkpoint {key}")
    if state["seed"] > 0xffffffff:
        raise ValueError("Seed exceeds the CLI's u32 range")
    state.setdefault("findings", [])
    if not valid_findings(state["findings"]):
        raise ValueError("Invalid checkpoint findings")
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
    axioms = [
        [a.get("file"), a.get("line"), a.get("kif")]
        for a in contradiction.get("axioms", [])
    ]
    return json.dumps(sorted(axioms, key=lambda axiom: json.dumps(axiom)),
                      separators=(",", ":"))


def valid_findings(findings):
    if not isinstance(findings, list):
        return False
    for finding in findings:
        if not isinstance(finding, dict):
            return False
        if any(type(finding.get(key)) is not int or finding[key] < 0
               or (key in ("seed", "step") and finding[key] > 0xffffffff)
               for key in ("seed", "step", "proof_steps")):
            return False
        axioms = finding.get("axioms")
        if not isinstance(axioms, list) or not axioms:
            return False
        for axiom in axioms:
            if not isinstance(axiom, dict) or not isinstance(axiom.get("kif"), str):
                return False
            if axiom.get("file") is not None and not isinstance(axiom.get("file"), str):
                return False
            if axiom.get("line") is not None and (
                    type(axiom.get("line")) is not int or axiom["line"] < 1):
                return False
    return True


def contradiction_report(findings, replay):
    """Build the versioned JSON replay report."""
    if not valid_findings(findings):
        raise ValueError("Invalid contradiction findings")
    return {**replay, "findings": findings}


def run(args):
    if args.chunk_size != 1:
        raise ValueError("Replay reports require --chunk-size 1 for exact contradiction coordinates")
    root = Path.cwd()
    output = Path(args.output).resolve()
    output.mkdir(parents=True, exist_ok=True)
    names, fingerprint = constituents(root)
    replay = replay_metadata(root, names, fingerprint, args.timeout)
    state_path = output / "checkpoint.json"
    state = checkpoint(state_path, fingerprint, replay["engine"]["fingerprint"])
    initial = dict(state)
    atomic_json(state_path, state)
    sumo = str(Path(args.sumo).resolve())
    completed = contradictions = 0
    interrupted = False
    findings = list(state["findings"])
    seen_findings = {contradiction_key(finding) for finding in findings}
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
                    finding = {
                        "seed": result["seed"],
                        "step": result["step"],
                        "proof_steps": contradiction.get("steps", 0),
                        "axioms": contradiction.get("axioms", []),
                    }
                    if not valid_findings([finding]):
                        raise RuntimeError("Invalid contradiction in audit result")
                    key = contradiction_key(contradiction)
                    if key not in seen_findings:
                        seen_findings.add(key)
                        findings.append(finding)
                with (output / "results.jsonl").open("a") as reports:
                    reports.write(json.dumps(result) + "\n")
                contradictions += len(result.get("contradictions", []))
                completed += result["next_step"] - result["step"]
                state = updated
                state["findings"] = findings
                atomic_json(state_path, state)
            replay["complete"] = True
    finally:
        report = contradiction_report(findings, replay)
        atomic_json(output / "contradictions.json", report)
        positions = "\n".join(
            f"- Seed `{f['seed']}`, step `{f['step']}`"
            for f in findings[:20]
        )
        if len(findings) > 20:
            positions += f"\n- ...and {len(findings) - 20} more in `contradictions.json`"
        if not positions:
            positions = "- None"
        summary = (
            "# Full SUMO nightly audit\n\n"
            f"- Started: seed {initial['seed']}, step {initial['next_step']}\n"
            f"- Resume: seed {state['seed']}, step {state['next_step']}\n"
            f"- Completed formula checks: {completed}\n"
            f"- Contradictions reported (may repeat across chunks): {contradictions}\n"
            f"- Cumulative distinct cited axiom sets: {len(findings)}\n"
            f"- Deadline interrupted a chunk: {interrupted}\n"
            f"- Full SUMO fingerprint: {fingerprint}\n\n"
            "## Reproduction positions\n\n"
            f"{positions}\n\n"
            "At https://sigmakee.dev/audit open Latest master contradiction report "
            "to verify and replay the findings. The complete formatted "
            "report is in `contradictions.json` in the workflow artifact.\n\n"
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
