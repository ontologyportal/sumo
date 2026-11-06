# Source and generated problems

Source tests use official TPTP domain directories and local TPTP-style stems: `DDDNNNFV.kif.tq`. KIF fixtures use version 0 with `.kif`. [The directory guide](../README.md) defines the domain mapping and language markers; [naming-map.csv](naming-map.csv) records every previous source/fixture path.

Use explicit `minLang` to request FOF, TFF or THF. A missing directive defaults to FOF for naming. Preserve required background KIF in per-test `include` or legacy `file` metadata. Geographic sources use `(include tests/axiom-sets/full.sources)`. Free variables in queries are implicitly universally quantified; write explicit `exists` for existential witnesses.

Translated problems use `.p`; translated background axioms use `.ax`. KIF files retain their KIF extensions. Existing legacy translations and CI templates keep their filenames; future exports go under `tests/TPTP/Generated/`.

The runners and exporter still need include resolution before include-dependent tests can be executed or translated reliably. See [INCLUDE-PLAN.md](INCLUDE-PLAN.md).

The ROE suite is an exception: its 25 tests retain their original `tests/ROE/ROE*.kif.tq` filenames, identifiers and category metadata.
