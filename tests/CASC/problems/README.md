# Source and generated problems

ARI is TFF only; GEO, PUZ, NUM, and CSR may have FOF, TFF, and THF formulations.

Source files use stable SUMO IDs with a form/version suffix, such as `kif/ARI/SMO_ARI_0001_1.kif.tq`. Generated problems use `DDDNNNFV[.SSS].p` when assigned a TPTP number (`-` CNF, `+` FOF, `_` TFF, `^` THF). Included axiom files use the `.ax` extension.

Source tests declare their KIF background with include metadata. GEO tests select tests/CASC/axiom-sets/full.sources, which mirrors the repository full-SUMO constituent list. The TQ runners and exporter still need to resolve includes before these tests can be executed or translated; see INCLUDE-PLAN.md.
