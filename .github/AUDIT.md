# Nightly contradiction audit

Full SUMO in this workflow is the constituent list in `full-sumo.txt`.

`workflows/contradiction-audit.yml` schedules Full SUMO's native Sigma audit
at 00:10 America/Los_Angeles, including daylight-saving changes. GitHub may
delay scheduled starts. Merge the workflow onto the default branch to enable
it; **Actions > Nightly contradiction audit > Run workflow** also runs it.
Manual runs may target any branch containing this workflow:

```sh
gh workflow run contradiction-audit.yml --ref contradiction-detection-workflow
gh run list --workflow contradiction-audit.yml
gh run watch
```

Scheduled runs are allowed only on `master`. GitHub schedules originate on the
default branch, so keep `master` as the default branch for nightly runs.
Manual and scheduled runs share the `audit-state` checkpoint and are serialized.
A manual run with different Full SUMO contents resets the checkpoint; the next
run on `master` resets it again if its contents differ.

One runner checks out the latest commit on sigma-rs's `main` branch, builds
that Sigma CLI, restores its checkpoint, loads a fresh
Full SUMO database, and then audits for 7,200 seconds. Build and initial load
time are additional. The job has a 210-minute safety limit.
The checkout stays fixed for the entire run, even if `main` advances meanwhile.
Each replay report records that exact commit and its engine source fingerprint.
The app must have a matching engine fingerprint; following `main` does not
bypass compatibility checks or automatically update an already deployed app.

## Progress

The workflow creates an `audit-state` branch on its first run and writes
`.github/audit-checkpoint.json` there. This is durable repository data; the
branch does not need an active runner. Repository rules must allow the
workflow's `GITHUB_TOKEN` to create/update that branch (`contents: write`).
Do not merge the state branch into the default branch.

The checkpoint contains constituent and engine fingerprints, seed, next step,
and the cumulative distinct contradiction findings:

- Initially seed 0, step 0.
- The seed determines the formula order; the step advances through it.
- On completing a sweep, increment the seed and start at step 0.
- A change to any file named in `full-sumo.txt`, or to the list of names/order,
  resets the seed and step to 0 and clears the cumulative findings. Files outside
  that list do not reset it.
- A change to the engine source fingerprint also resets both seed and step.
  It also clears cumulative findings because their replay coordinates may no
  longer be valid. Legacy checkpoints without that fingerprint restart once.
  Frontend-only commits that leave the engine fingerprint unchanged preserve
  progress and findings.
- Each CLI invocation checks one formula, so every contradiction has an exact
  seed and step that can be reproduced in sigmakee.dev. Completed formula
  checks and their newly discovered contradictions update the checkpoint
  atomically.
  At the deadline, the unfinished chunk is killed and retried next night.
  No position from a partially completed chunk is committed.
- Runs are serialized. Saving uses the restored GitHub file SHA so an
  unexpected concurrent state edit fails instead of silently overwriting it.

`sigma-validation.yml` uses the same `full-sumo.txt` manifest. Keep the list
aligned with the intended Full SUMO definition. Sigma's `main` branch must
support `audit --seed --step --count --json`; incompatible upstream changes
fail the run rather than silently falling back to an older engine.

## Results and failures

Each completed chunk's JSON (including contradiction axioms) is retained in
the run's `full-sumo-audit-...` artifact for 30 days, alongside logs, checkpoint,
and a summary. `contradictions.json` is a versioned replay document containing
metadata and every distinct cited axiom set accumulated since the SUMO or
engine inputs last changed. It gives each finding's exact seed, step, proof-step
count, and source axioms. The Actions job summary lists the first 20
reproduction positions.

The same complete JSON document is published as
`.github/latest-contradictions.json` on the `audit-state` branch after each
complete master run. Daily runs merge newly discovered cited axiom sets into
the checkpoint, so loading the latest report includes the entire unchanged-input
period rather than only the most recent two-hour window.

To reproduce one in sigmakee.dev, load the same SUMO revision, open Audit,
select the SUPr backend, enter the reported seed and start step, and set both
`axioms to check` and `axioms per subproblem` to 1. Prover settings must also
match for the closest reproduction; the workflow currently uses a 10-second
time limit.

Finding contradictions makes the audit step fail **after** the audit window;
the checkpoint and reports are still saved. Counts can include duplicate
contradictions across chunks. No contradictions found is not a proof of
consistency.

Unexpected CLI errors or malformed results fail the job without advancing
the affected chunk. Ordinary failures still run the save/upload steps. A
runner crash or forced cancellation can prevent final persistence; the next
run then resumes the prior saved checkpoint and repeats work safely.

## Local checks

From the repository root:

```sh
python3 -m unittest discover -s .github/scripts -p 'test_*.py' -v
python3 .github/scripts/nightly_audit.py --sumo /path/to/sumo \
  --output /tmp/sumo-audit-results --seconds 60 --chunk-size 1 --timeout 1
```

The local command performs a real Full SUMO load and short audit. It uses the
native prover and never writes to GitHub. No GitHub schedule has been activated
merely by creating these files locally.
