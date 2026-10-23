# Source and generated problems

`kif/<domain-code>/` contains editable SUO-KIF TQ tests. Generated `tptp/Problems/<domain-code>/` files follow TPTP's domain layout; shared translated axioms go in `tptp/Axioms/`. There are no axiom-set, language, or per-problem directories. `ARI` is TFF only; `PUZ`, `NUM`, and `CSR` may have FOF, TFF, and THF formulations.

Source files use stable SUMO IDs with a form/version suffix, such as `kif/ARI/SMO_ARI_0001_1.kif.tq`. Generated problems use `DDDNNNFV[.SSS].p` when assigned a TPTP number (`-` CNF, `+` FOF, `_` TFF, `^` THF). Included axiom files use the `.ax` extension.

The current arithmetic test identifies `Merge.kif` in its header. Once the TQ runners and exporter support `(include ...)` metadata, declare its KIF source in the test itself. The reusable source presets remain in `../axiom-sets/`. See [INCLUDE-PLAN.md](../INCLUDE-PLAN.md).
