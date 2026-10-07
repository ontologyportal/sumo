#!/usr/bin/env python3
"""
auto_vampire.py

CF: Iterates over category/scenario/option/system and runs vampire 
on each combination
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path
from typing import List, Sequence, Tuple

# Error codes:
CMD_NOT_FOUND = 127
OTHER_ERR = 2
DEFAULT_TIME_LIMIT_SECONDS = 10

def discover_main_folders(base_dir: Path) -> List[Path]:
    """Returns folders that contain SCENARIOS, OPTIONS, and SYSTEMS subfolders."""
    folders: List[Path] = []
    for child in sorted(base_dir.iterdir()):
        if child.is_dir() and (child / "SCENARIOS").is_dir() and (child / "OPTIONS").is_dir() and (child / "SYSTEMS").is_dir():
            folders.append(child)
    return folders

# Return sorted THF files from a folder. 
# Files are sorted in alphabetical order all in lower case.
def discover_thf_files(folder: Path) -> List[Path]:
    thf_files = sorted(folder.glob("*.thf"), key=lambda path: path.name.lower())
    if not thf_files:
        raise FileNotFoundError(f"No THF files found in {folder}")
    return thf_files

# Build the run plan for all combinations
def build_run_plan(base_dir: Path) -> List[Tuple[Path, Path, Path, Path, Path, Path, Path]]:
    plan: List[Tuple[Path, Path, Path, Path, Path, Path, Path]] = []
    for main_folder in discover_main_folders(base_dir):
        examples = discover_thf_files(main_folder / "SCENARIOS")
        options = discover_thf_files(main_folder / "OPTIONS")
        systems = discover_thf_files(main_folder / "SYSTEMS")

        thf_output_dir = base_dir / "results" / "thf" / main_folder.name
        full_output_dir = base_dir / "results" / "full_output" / main_folder.name
        input_axioms_dir = base_dir / "results" / "input_axioms" / main_folder.name
        thf_output_dir.mkdir(parents=True, exist_ok=True)
        full_output_dir.mkdir(parents=True, exist_ok=True)
        input_axioms_dir.mkdir(parents=True, exist_ok=True)

        for example in examples:
            for option in options:
                for system in systems:
                    stem = f"{example.stem}__{option.stem}__{system.stem}"
                    problem_file = thf_output_dir / f"{stem}.thf"
                    output_log = full_output_dir / f"{stem}.out"
                    input_axioms_file = input_axioms_dir / f"{stem}.txt"
                    plan.append((main_folder, example, option, system, problem_file, output_log, input_axioms_file))
    return plan

# Compose the problem file from the given input THF files
def compose_problem_file(output_path: Path, input_files: Sequence[Path]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    chunks: List[str] = []
    for input_file in input_files:
        chunks.append(f"% ===== {input_file.name} =====\n")
        chunks.append(input_file.read_text(encoding="utf-8"))
        if not input_file.read_text(encoding="utf-8").endswith("\n"):
            chunks.append("\n")
    output_path.write_text("".join(chunks), encoding="utf-8")

# Find correct path to the vampire on user system 
def find_vampire_binary(explicit_path: str | None) -> str | None:
    if explicit_path:
        return explicit_path
    if shutil.which("vampire"):
        return "vampire"
    return None


# Runs vampire on the combined THF file and emit stdout only for nonzero exits
def run_vampire(problem_file: Path, vampire_binary: str, output_log: Path, input_axioms_path: Path, time_limit_seconds: int) -> int:
    output_log.parent.mkdir(parents=True, exist_ok=True)
    input_axioms_path.parent.mkdir(parents=True, exist_ok=True)
    command = [vampire_binary, "--time_limit", str(time_limit_seconds), str(problem_file)]
    try:
        completed = subprocess.run(command, capture_output=True, text=True)
    except FileNotFoundError as exc:
        output_log.write_text(str(exc), encoding="utf-8")
        return CMD_NOT_FOUND

    combined_output = completed.stdout + completed.stderr
    input_axiom_lines = [line.rstrip() for line in combined_output.splitlines() if line.rstrip().endswith("[input(axiom)]")]
    if input_axiom_lines:
        input_axioms_path.write_text("\n".join(input_axiom_lines) + "\n", encoding="utf-8")

    if completed.returncode != 0:
        return completed.returncode

    output_log.write_text(combined_output, encoding="utf-8")
    return completed.returncode


def main() -> int:

    # Parse command line arguments 
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent, help="Directory containing the THF test folders")
    parser.add_argument("--vampire", default=os.environ.get("VAMPIRE_BIN"), help="Path to the Vampire executable")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIME_LIMIT_SECONDS, help="Time limit to pass to Vampire in seconds")
    parser.add_argument("--dry-run", action="store_true", help="Show the planned combinations without running Vampire")

    if len(sys.argv) == 1:
        parser.print_help()
        return 0

    args = parser.parse_args()

    # Error checking
    base_dir = args.root.resolve()
    if not base_dir.exists():
        print(f"Root directory does not exist: {base_dir}", file=sys.stderr)
        return OTHER_ERR
    plan = build_run_plan(base_dir)
    if not plan:
        print("No runnable THF folders were found.", file=sys.stderr)
        return OTHER_ERR

    # Dry run mode 
    if args.dry_run:
        print(f"Planned {len(plan)} combinations:")
        # First level '_' is example family (like "1_Obligation")
        for _, example, option, system, problem_file, output_log, input_axioms_path in plan:
            print(f"- {example.name} + {option.name} + {system.name} -> THF: {problem_file.relative_to(base_dir)} ; LOG: {output_log.relative_to(base_dir)} ; INPUT_AXIOMS: {input_axioms_path.relative_to(base_dir)}")
        return 0

    # MAIN SECTION 
    vampire_binary = find_vampire_binary(args.vampire)
    if not vampire_binary:
        print("Vampire executable was not found. Install Vampire or set --vampire / VAMPIRE_BIN.", file=sys.stderr)
        return OTHER_ERR
    print(f"Running {len(plan)} combinations with {vampire_binary} using a {args.timeout}s Vampire time limit")
    # First level '_' is example category (like "1_Obligation")
    total_runtime = 0.0
    for _, example, option, system, problem_file, output_log, input_axioms_path in plan:
        start_time = time.perf_counter()
        compose_problem_file(problem_file, [system, example, option])
        return_code = run_vampire(problem_file, vampire_binary, output_log, input_axioms_path, args.timeout)
        elapsed_time = time.perf_counter() - start_time
        status = "ok" if return_code == 0 else f"failed ({return_code})"
        print(f"- {problem_file.name}: {status} ({elapsed_time:.2f}s)")
        total_runtime += elapsed_time

    print(f"Total runtime: {total_runtime:.2f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

                    