# Nightly contradiction audit

`workflows/contradiction-audit.yml` schedules Full SUMO's native Sigma audit
at 00:10 America/Los_Angeles, including daylight-saving changes. GitHub may
delay scheduled starts. Merge the workflow onto the default branch to enable
it; **Actions > Nightly contradiction audit > Run workflow** also runs it.
Manual runs are restricted to the default branch so they cannot overwrite
production progress with a different ontology.

One runner builds the pinned Sigma CLI, restores its checkpoint, loads a fresh
Full SUMO database, and then audits for 7,200 seconds. Build and initial load
time are additional. The job has a 210-minute safety limit.

## Progress

The workflow creates an `audit-state` branch on its first run and writes
`.github/audit-checkpoint.json` there. This is durable repository data; the
branch does not need an active runner. Repository rules must allow the
workflow's `GITHUB_TOKEN` to create/update that branch (`contents: write`).
Do not merge the state branch into the default branch.

The checkpoint contains a constituent fingerprint, seed, and next step:

- Initially seed 0, step 0.
- The seed determines the formula order; the step advances through it.
- On completing a sweep, increment the seed and start at step 0.
- A change to any file named in `full-sumo.txt`, or to the list of names/order,
  resets both seed and step to 0. Files outside that list do not reset it.
- Completed chunks (100 formulas by default) update the checkpoint atomically.
  At the deadline, the unfinished chunk is killed and retried next night.
  No position from a partially completed chunk is committed.
- Runs are serialized. Saving uses the restored GitHub file SHA so an
  unexpected concurrent state edit fails instead of silently overwriting it.

The Full SUMO manifest is also used by `sigma-validation.yml`. Keep the list
aligned with the intended Full SUMO definition. Sigma is pinned to a commit
supporting `audit --seed --step --count --json`; when upgrading Sigma, reset
the saved checkpoint if its sweep ordering or eligibility rules change.

## Results and failures

Each completed chunk's JSON (including contradiction axioms) is retained in
the run's `full-sumo-audit-...` artifact for 30 days, alongside logs, checkpoint,
and a summary. The Actions job summary shows progress and finding counts.
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
  --output /tmp/sumo-audit-results --seconds 60 --chunk-size 5 --timeout 1
```

The local command performs a real Full SUMO load and short audit. It uses the
native prover and never writes to GitHub. No GitHub schedule has been activated
merely by creating these files locally.
