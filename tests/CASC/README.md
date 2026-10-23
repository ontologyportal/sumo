# SUMO problems for CASC-style TPTP benchmarks

Edit SUO-KIF tests under `problems/kif/` and generate TPTP editions under `problems/tptp/`. The filename form marker indicates the target language.

```text
axiom-sets/
  merge.sources                 Merge.kif
  merge-mid.sources             Merge.kif + Mid-level-ontology.kif
  full.sources                  Full SUMO list (not yet finalized)
problems/
  kif/<domain-code>/            Source tests (*.kif.tq)
  tptp/
    Axioms/                     Translated background axioms (*.ax)
    Problems/<domain-code>/     Generated problems (*.p)
```

Axiom-set manifests are reusable source-file presets; they do not create parallel problem trees. Each test will eventually declare its required KIF files through `(include ...)` metadata. The current arithmetic test names `Merge.kif` in its header; its live directive can be added when the TQ runners support it. See [INCLUDE-PLAN.md](INCLUDE-PLAN.md).

`PUZ` is puzzles, `NUM` is number theory, `CSR` is commonsense reasoning, and `ARI` is arithmetic. Use `ARI` only for TFF. Other domains may have FOF, TFF, and THF formulations. Put each source test directly in its domain directory, without language or per-problem subdirectories.

`problems/kif/ARI/SMO_ARI_0001_1.kif.tq` has a `(query ...)`, `(answer ...)`, and a TPTP-style comment header. Its source ID is `SMO_ARI_0001`; `_1` identifies TFF formulation 1. Generated problems use TPTP's `DDDNNNFV[.SSS].p` naming once numbers are assigned: `-` CNF, `+` FOF, `_` TFF, `^` THF. The example's generated name will be `ARI###_1.p`. Its `.p` file includes matching-language `.ax` files from `Axioms/` using TPTP `include('Axioms/<assigned-axiom-id>.ax').` directives.

`*.sources` lists KIF paths relative to the SUMO repository root, one per line, with `#` comments allowed. Finalize `full.sources` before exporting a full-SUMO edition. Pin SUMO and translator revisions and the exact source list for each release. Publish THF editions only after a suitable translation path and validation are in place.
