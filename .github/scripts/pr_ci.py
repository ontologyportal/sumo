"""Sigma-rs syntax checks and Vampire consistency-result grading for CI."""

import argparse
from pathlib import Path
import re
import subprocess
import time
import xml.etree.ElementTree as ET


def parse_kif(sumo, root, config, output):
    output.mkdir(parents=True, exist_ok=True)
    suite = ET.Element("testsuite", name="sigma-rs syntax")
    failures = 0
    files = sorted(p for p in root.rglob("*.kif") if p.stem != "Useful-terms_2023")
    if not files:
        raise ValueError("No KIF files found")
    for path in files:
        name = str(path.relative_to(root))
        print(f"Parsing: {name}", flush=True)
        start = time.monotonic()
        case = ET.SubElement(suite, "testcase", classname="sigma-rs.parse", name=name)
        try:
            result = subprocess.run(
                [str(sumo), "--config", str(config), "--no-db", "-f", str(path),
                 "validate", "--parse"],
                stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
                errors="replace", timeout=120,
            )
            log = result.stdout
            # This pinned CLI logs constituent ingest errors without propagating
            # them to its exit status. Do not let a partial parse pass CI.
            failed = result.returncode != 0 or bool(re.search(r"\bERROR\]", log))
        except (OSError, subprocess.TimeoutExpired) as error:
            log = str(error)
            failed = True
        # XML 1.0 cannot represent terminal escape/control characters.
        log = re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f]", "", log)
        case.set("time", f"{time.monotonic() - start:.3f}")
        if failed:
            failures += 1
            ET.SubElement(case, "failure", message="KIF parse failed").text = log
            print(log, flush=True)
        ET.SubElement(case, "system-out").text = log
    suite.set("tests", str(len(files)))
    suite.set("failures", str(failures))
    ET.ElementTree(suite).write(output / "TEST-sigma-parse.xml", encoding="utf-8",
                                xml_declaration=True)
    return bool(failures)


def check_vampire(log, returncode):
    statuses = set(re.findall(r"SZS status (\w+)", log))
    if statuses & {"Unsatisfiable", "Theorem", "ContradictoryAxioms"} or "Refutation found" in log:
        raise ValueError("Vampire found a contradiction in SUMO")
    if returncode == 0 and "Satisfiable" in statuses:
        return "Vampire reported satisfiable"
    # Vampire returns nonzero when its search budget expires.
    if returncode in (0, 1) and ("Timeout" in statuses or "Time limit reached" in log):
        return "Time limit reached; no contradiction found (not a consistency proof)"
    raise ValueError(f"Vampire failed or returned an unexpected result (exit {returncode})")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    parse = commands.add_parser("parse")
    parse.add_argument("--sumo", type=Path, required=True)
    parse.add_argument("--root", type=Path, required=True)
    parse.add_argument("--config", type=Path, required=True)
    parse.add_argument("--output", type=Path, required=True)
    check = commands.add_parser("check-vampire")
    check.add_argument("--log", type=Path, required=True)
    check.add_argument("--exit-code", type=int, required=True)
    args = parser.parse_args()
    if args.command == "parse":
        return parse_kif(args.sumo.resolve(), args.root.resolve(), args.config.resolve(), args.output)
    print(check_vampire(args.log.read_text(errors="replace"), args.exit_code))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
