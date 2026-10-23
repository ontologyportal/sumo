# Pull request CI

`sumo-dev-cycle.yml` calls `sumo-ci.yml` for pull requests and pushes to
master/main. Manual and scheduled runs reuse the same workflow with longer
Vampire time budgets.

The workflow builds a pinned sigma-rs CLI and:

* Runs `validate --parse` on every `.kif` file recursively, retaining the
  legacy parser suite's `Useful-terms_2023.kif` exclusion. Each file gets a
  JUnit testcase in the `test-results` artifact, consumed by `test-report.yml`.
* Translates the constituents in `.github/full-sumo.txt` in memory to both
  `SUMO.fof` and `SUMO.tff`. No cached database or machine-local config is used.
* Checks both translations with standalone Vampire 5.0.1. A contradiction
  fails CI; a search timeout means only that no contradiction was found in
  the allotted time. Invalid input, crashes, and unrecognized results fail.

The separate `sigma-validation.yml` workflow performs semantic validation.
Both workflows currently pin the same sigma-rs revision and apply the same
guarded validation exit-status fix. Update the pin and remove the fix together
once the upstream correction is available.
The CI build also applies a guarded logging patch to show the source line and
formula for ingest errors. Remove it once sigma-rs renders source context itself.
The syntax runner also rejects logged ingest errors: this pinned CLI can
return zero after logging a malformed constituent and loading only part of it.
Translation also rejects logged errors and uploads diagnostics separately.

The `fof-logs-and-graphs` and `tff-logs-and-graphs` artifact names are retained
for compatibility. They contain the raw Vampire log, including any TPTP
proof. The Java-generated HTML/Graphviz proof files are no longer produced.
TFF input is no longer stripped of arithmetic formulas before checking.
The manually dispatched `tqsp-ci.yml` is separate from this PR pipeline. It
builds the same pinned sigma-rs CLI, translates `Merge.kif` as top SUMO to
FOF and TFF, and runs the existing SP/TQG TPTP templates with Vampire.
It uploads each generated problem and raw proof log. Java proof graphs are
not generated.

Local helper tests: `python3 -m unittest discover -s .github/scripts -p test_pr_ci.py -v`.
