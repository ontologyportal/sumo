# SUMO benchmark conventions

Source tests live in `tests/<TPTP-domain>/DDDNNNFV.kif.tq`. See [the test directory guide](../README.md) for domains, language markers, local numbering and fixture conventions. [naming-map.csv](naming-map.csv) preserves previous paths and identifiers.

Keep queries, answers and background dependency declarations in the KIF sources. TPTP-shaped filenames identify the intended formulation; they do not translate KIF or establish a theorem status. Original `SMO_*` names in provenance headers are aliases. Numbers in this collection are local SUMO numbers, not official TPTP assignments.

Shared axiom manifests are `tests/axiom-sets/merge.sources`, `merge-mid.sources` and `full.sources`. The full manifest mirrors the 51 constituents in `.github/full-sumo.txt`; verify synchronization before export. Pin SUMO and translator revisions and the exact source list for each release.

Future exports use `tests/TPTP/Generated/Problems/<domain>/DDDNNNFV.p`. Translate backgrounds into matching-language `.ax` files under `tests/TPTP/Generated/Axioms/`; exported includes resolve from that generated package root. Source KIF includes resolve from the SUMO repository root.

Include metadata handling and export implementation remain pending as described in [INCLUDE-PLAN.md](INCLUDE-PLAN.md). Validate translation, include resolution, language declarations and prover results before release. Publish THF editions only after a suitable translation path and validation are in place.

The ROE suite is an exception: its 25 tests retain their original `tests/ROE/ROE*.kif.tq` filenames, identifiers and category metadata.
