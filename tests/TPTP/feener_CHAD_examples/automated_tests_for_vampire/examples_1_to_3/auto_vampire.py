#!/usr/bin/env python3
"""
CF
Script written by Copilot to spec, then manually tested and verified
Run Vampire over all category/example/option/system combinations in the THF test folders.
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

def discover_main_folders(base_dir: Path) -> List[Path]:
    """Return folders that contain EXAMPLES, OPTIONS, and SYSTEMS subfolders."""
    folders: List[Path] = []
    for child in sorted(base_dir.iterdir()):
        if child.is_dir() and (child / "EXAMPLES").is_dir() and (child / "OPTIONS").is_dir() and (child / "SYSTEMS").is_dir():
            folders.append(child)
    return folders


def discover_thf_files(folder: Path) -> List[Path]:
    """
    Return sorted THF files from a folder.
    CF: Files are sorted in alphabetical order all in lower case.
    """
    thf_files = sorted(folder.glob("*.thf"), key=lambda path: path.name.lower())
    if not thf_files:
        raise FileNotFoundError(f"No THF files found in {folder}")
    return thf_files


def build_run_plan(base_dir: Path) -> List[Tuple[Path, Path, Path, Path, Path]]:
    """
    Create a plan of (main_folder, example, option, system, output_problem_file).
    CF: Takes the input files and turns it into an object that the next 
    method is able to use as a guide
    """
    plan: List[Tuple[Path, Path, Path, Path, Path]] = []
    for main_folder in discover_main_folders(base_dir):
        examples = discover_thf_files(main_folder / "EXAMPLES")
        options = discover_thf_files(main_folder / "OPTIONS")
        systems = discover_thf_files(main_folder / "SYSTEMS")

        output_dir = base_dir / "results" / main_folder.name
        output_dir.mkdir(parents=True, exist_ok=True)

        for example in examples:
            for option in options:
                for system in systems:
                    stem = f"{example.stem}__{option.stem}__{system.stem}"
                    problem_file = output_dir / f"{stem}.thf"
                    plan.append((main_folder, example, option, system, problem_file))
    return plan


def compose_problem_file(output_path: Path, input_files: Sequence[Path]) -> None:
    """
    Concatenate the given THF files into a single input file.
    Based on Path object, composes the problem file from 
    system, example, and option to be run by vampire 
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)
    chunks: List[str] = []
    for input_file in input_files:
        chunks.append(f"% ===== {input_file.name} =====\n")
        chunks.append(input_file.read_text(encoding="utf-8"))
        if not input_file.read_text(encoding="utf-8").endswith("\n"):
            chunks.append("\n")
    output_path.write_text("".join(chunks), encoding="utf-8")


def find_vampire_binary(explicit_path: str | None) -> str | None:
    """Resolve the Vampire executable path."""
    if explicit_path:
        return explicit_path
    if shutil.which("vampire"):
        return "vampire"
    return None


def run_vampire(problem_file: Path, vampire_binary: str, output_dir: Path) -> int:
    """Run Vampire on the combined THF file and save its output log."""
    output_log = output_dir / f"{problem_file.stem}.out"
    command = [vampire_binary, str(problem_file)]
    try:
        completed = subprocess.run(command, capture_output=True, text=True)
    except FileNotFoundError as exc:
        output_log.write_text(str(exc), encoding="utf-8")
        return CMD_NOT_FOUND

    output_log.write_text(completed.stdout + completed.stderr, encoding="utf-8")
    return completed.returncode


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parent, help="Directory containing the THF test folders")
    parser.add_argument("--vampire", default=os.environ.get("VAMPIRE_BIN"), help="Path to the Vampire executable")
    parser.add_argument("--dry-run", action="store_true", help="Show the planned combinations without running Vampire")
    args = parser.parse_args()

    # Error checking:
    base_dir = args.root.resolve()
    if not base_dir.exists():
        print(f"Root directory does not exist: {base_dir}", file=sys.stderr)
        return OTHER_ERR
    plan = build_run_plan(base_dir)
    if not plan:
        print("No runnable THF folders were found.", file=sys.stderr)
        return OTHER_ERR

    # CF: Shorter, skeleton run if command line args require
    if args.dry_run:
        print(f"Planned {len(plan)} combinations:")
        # First level '_' is example category (like '1_Obligation')
        for _, example, option, system, problem_file in plan:
            print(f"- {example.name} + {option.name} + {system.name} -> {problem_file.relative_to(base_dir)}")
        return 0

    # This is the start of the main section, where it verifies vampire is installed before running 
    vampire_binary = find_vampire_binary(args.vampire)
    if not vampire_binary:
        print("Vampire executable was not found. Install Vampire or set --vampire / VAMPIRE_BIN.", file=sys.stderr)
        return OTHER_ERR
    print(f"Running {len(plan)} combinations with {vampire_binary}")
    # First level '_' is example category (like '1_Obligation')
    total_runtime = 0.0
    for _, example, option, system, problem_file in plan:
        start_time = time.perf_counter()
        output_dir = problem_file.parent
        compose_problem_file(problem_file, [system, example, option])
        return_code = run_vampire(problem_file, vampire_binary, output_dir)
        elapsed_time = time.perf_counter() - start_time
        status = "ok" if return_code == 0 else f"failed ({return_code})"
        print(f"- {problem_file.name}: {status} ({elapsed_time:.2f}s)")
        total_runtime += elapsed_time

    print(f"Total runtime: {total_runtime:.2f}s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

                    