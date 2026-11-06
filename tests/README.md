# SUMO tests

Except for the ROE suite, KIF source tests use TPTP domain codes and the naming pattern `DDDNNNFV.kif.tq`: three-letter domain, three-digit local problem number, language marker and version. For example, `BIO001+1.kif.tq` is FOF, `ARI001_1.kif.tq` is TFF, and `KRS001^1.kif.tq` is THF. Markers follow the [TPTP naming scheme](https://tptp-manual.tptp.org/): `+` FOF, `_` TFF, `^` THF, `-` CNF. The `.kif.tq` extension identifies runnable KIF source; it is not a translated `.p` file.

Numbers are local to this SUMO collection and do not claim official TPTP problem assignments. Versions distinguish formulations of one abstract problem. Language comes from `minLang`, with FOF as the default for sources that omit it. The filename records the requested formulation; translation and prover validation remain separate steps.

| Domain | Contents | KIF tests |
| --- | --- | ---: |
| [AGT/](AGT/) | Agents: communications. | 3 |
| [ARI/](ARI/) | Arithmetic, numeric classes, units, capacity and measurements. | 55 |
| [BIO/](BIO/) | Biology and food. | 30 |
| [CSR/](CSR/) | Commonsense reasoning: astronomy, transportation and weather. | 58 |
| [DAT/](DAT/) | Data structures: lists and list functions. | 3 |
| [GEG/](GEG/) | Geography: named places and geographic features; diagnostics in diagnostics/. | 17 |
| [GEO/](GEO/) | Geometry and qualitative spatial reasoning. | 8 |
| [GRA/](GRA/) | Graph theory. | 1 |
| [KRS/](KRS/) | Knowledge representation: ontology reasoning, knowledge, belief and modalities. | 31 |
| [MED/](MED/) | Medicine. | 15 |
| [MGT/](MGT/) | Management: banking and finance. | 16 |
| [NUM/](NUM/) | Number theory (reserved). | 0 |
| [PRD/](PRD/) | Products: gym equipment. | 3 |
| [PUZ/](PUZ/) | Puzzles (reserved). | 0 |
| [ROE/](ROE/) | Rules of engagement; original filenames and metadata retained. | 25 |
| [SYN/](SYN/) | Syntactic: predicate arity, valence, row variables and partitions. | 18 |
| [TIM/](TIM/) | Time: intervals, ordering, duration and temporal reasoning. | 15 |

Domains follow the [TPTP classification](https://tptp.org/Seminars/TPTP/Domains.html) and the installed TPTP 9.3.0 library. Subjects without a dedicated TPTP domain use a broader domain: astronomy, transportation and weather are CSR; finance is MGT; food is BIO. TIM is the time domain in TPTP 9.3.0.

Standalone KIF fixtures use the same domain/number/language structure with version `0` and `.kif`; a fixture paired with a test shares its abstract problem number. They remain KIF fixtures, not translated `.ax` files. Documentation and captured diagnostic reproducers retain descriptive filenames.

[naming-map.csv](docs/naming-map.csv) records the 282 source/fixture moves, original notes and before/after SHA-256 hashes. Migrated test `note` identifiers and `category` metadata match the new names and domain codes. Original SMO names in benchmark provenance headers are retained as aliases.

Discover source tests recursively (`find tests -name '*.kif.tq'`). Shared background manifests are in [axiom-sets/](axiom-sets/). See [benchmark conventions](docs/Benchmarks.md), [source conventions](docs/SourceProblems.md), and the [include implementation plan](docs/INCLUDE-PLAN.md).

The existing [TPTP/](TPTP/) translations, prover scripts, captured examples, and [TQSP/](TQSP/) CI templates retain their existing names. The source migration does not change those compatibility artifacts. Future exports go in `TPTP/Generated/Problems/<domain>/DDDNNNFV.p`, with translated background files under `TPTP/Generated/Axioms/`.

The 25 ROE tests are restored to `ROE/ROE*.kif.tq` with their original contents and identifiers. They are excluded from the naming migration map.
