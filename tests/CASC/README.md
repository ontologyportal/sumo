# SUMO problems for CASC-style TPTP benchmarks

Edit SUO-KIF tests under `problems/kif/` and generate TPTP editions under `problems/tptp/`. The filename form marker indicates the target language.

```text
axiom-sets/
  merge.sources                 Merge.kif
  merge-mid.sources             Merge.kif + Mid-level-ontology.kif
  full.sources                  Full SUMO list mirrored from .github/full-sumo.txt
problems/
  kif/<topic-code>/             Source tests (*.kif.tq)
  tptp/
    Axioms/                     Translated background axioms (*.ax)
    Problems/<domain-code>/     Generated problems (*.p)
```

Axiom-set manifests are reusable source-file presets; they do not create parallel problem trees. Source tests declare the required KIF with include metadata. The TQ runners and exporter still need to resolve those directives; see INCLUDE-PLAN.md.

BIO is biology, TIM is time, TRN is transportation, GEG is geography, GEO is geometry (including qualitative spatial reasoning), PUZ is puzzles, NUM is number theory, CSR is commonsense reasoning, and ARI is arithmetic. Use ARI only for TFF. Other domains may have FOF, TFF, and THF formulations. BIO groups problems by biological subject, including organisms, anatomy, diet, habitat, and reproduction; individual tests name only the KIF sources needed for their conjectures. Use GEG for named places and geographic features, including spatial relations between them; reserve GEO for geometry problems. Source topic codes may overlap TPTP domains, but need not; select the TPTP domain when exporting each problem.

`problems/kif/ARI/SMO_ARI_0001_1.kif.tq` has a `(query ...)`, `(answer ...)`, and a TPTP-style comment header. Its source ID is `SMO_ARI_0001`; `_1` identifies TFF formulation 1. Generated problems use TPTP's `DDDNNNFV[.SSS].p` naming once numbers are assigned: `-` CNF, `+` FOF, `_` TFF, `^` THF. The example's generated name will be `ARI###_1.p`. Its `.p` file includes matching-language `.ax` files from `Axioms/` using TPTP `include('Axioms/<assigned-axiom-id>.ax').` directives.

The full.sources manifest mirrors the 51 constituents of .github/full-sumo.txt; verify they still match before each export. Pin SUMO and translator revisions and the exact source list for each release. Publish THF editions only after a suitable translation path and validation are in place.
