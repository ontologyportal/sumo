"""Grade a TQSP Vampire run without mistaking a crash for a timeout."""

import argparse
from pathlib import Path
import re


def grade(log, exit_code):
    statuses = set(re.findall(r"SZS status (\w+)", log))
    has_refutation = "Refutation found" in log
    if has_refutation:
        if exit_code == 0 and "Theorem" in statuses and "negated_conjecture" in log:
            return "Theorem proved from the TQSP conjecture"
        raise ValueError("Refutation did not establish the test conjecture")
    if exit_code in (0, 1) and statuses & {"Timeout", "GaveUp", "CounterSatisfiable"}:
        return "No proof found within the search budget"
    raise ValueError(f"Vampire failed or returned an unexpected result (exit {exit_code})")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--log", required=True, type=Path)
    parser.add_argument("--exit-code", required=True, type=int)
    args = parser.parse_args()
    print(grade(args.log.read_text(errors="replace"), args.exit_code))


if __name__ == "__main__":
    main()
