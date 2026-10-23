# KIF includes and CASC TPTP translation plan

## Source contract

`(include Merge.kif)` is TQ metadata: it names required background KIF, not a SUMO formula. Allow repeated `include` directives in source order. `(minLang fof)`, `(minLang tff)`, or `(minLang thf)` selects the language for the query and all included axioms. The existing arithmetic test should eventually contain:

```lisp
(include Merge.kif)
(minLang tff)
```

The `merge-mid` preset means both `Merge.kif` and `Mid-level-ontology.kif`. For full SUMO, support `(include axiom-sets/full.sources)` as a source-list include that expands to its KIF entries. Resolve both kinds of path relative to the SUMO root. Reject missing or out-of-root files, empty lists, and circular lists. Deduplicate repeated files while preserving first occurrence and order. Do not silently add axioms beyond those requested.

## Implementation sequence

1. Add `include` to the sigma-rs TQ directive parser and test model. Keep `(file ...)` as a compatibility alias during migration. Teach the Java SigmaKEE/TQ runner to load or check these dependencies. Neither runner should submit `include` as a logical assertion.
2. Build a common source resolver for test execution and export. Expand `.sources` manifests, validate paths, and record the ordered KIF closure with file hashes. Select axioms from metadata rather than a directory name.
3. Translate selected KIF to language-specific `.ax` artifacts in `problems/tptp/Axioms/`. Cache by source contents, SUMO revision, language, and translator options. Record a KIF-to-artifact map. For release, assign TPTP-style axiom names with a language marker and `.ax` extension; the extension itself does not encode FOF/TFF/THF.
4. Export local facts, translated conjecture, and header to one `problems/tptp/Problems/<domain-code>/*.p`. Emit `include('Axioms/<assigned-axiom-id>.ax').` directives before the conjecture. Keep included formulas in the problem's language. Ensure that multiple axiom files have compatible symbols, complete TFF/THF types, and distinct formula identifiers. CNF would need a separate clausification path.
5. Parse all exported `.p` and `.ax` files, resolve every TPTP include from the package root, check language and declarations, and run representative provers. Report translated, instantiated, and dropped KIF formulas; verify each claimed problem status.

## FOF limitation

Some `Merge.kif` formulas use higher-order features. A reusable FOF `.ax` cannot contain THF formulas, and conjecture-dependent instantiation may yield different FOF axioms per problem. Export a reusable FOF core plus a separately included problem-specific FOF axiom artifact when needed, with provenance for every transformation. If a sound FOF translation is unavailable, fail that export instead of silently publishing an incomplete benchmark. Validate TFF and THF paths independently.

## Migration check

The current arithmetic test names `Merge.kif` in its header. When both TQ runners and the exporter understand `include`, add `(include Merge.kif)` to the test. Keep `axiom-sets/*.sources` as reusable presets; no separate per-test source mapping is needed. The first end-to-end check is a TFF `.p` for the arithmetic test whose include resolves to a translated Merge `.ax`, with the SUO-KIF runner and TPTP parser both accepting the same source selection. Follow with a Merge + Mid-level case; add a full-SUMO case after finalizing `full.sources`.
