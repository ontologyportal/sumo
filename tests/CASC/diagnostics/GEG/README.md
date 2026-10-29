# GEG / Vampire diagnosis (2026-10-26)

Investigation only: no translator or prover behavior was changed.

## Reproduction

Built sigma-rs revision 7c410cb and explicitly loaded the 51 constituents in
`tests/CASC/axiom-sets/full.sources`, in memory, without an LMDB cache.
Captured the TPTP for SMO_GEG_0002+1 and replayed it with standalone Vampire
5.0.1 and the web app's actual Vampire WASM assets in headless Chromium.
The browser replay used COOP/COEP headers, as required by the WASM build.

Both backends reproduced these two separate failures:

| Input | Standalone Vampire | Browser Vampire WASM |
| --- | --- | --- |
| Generated input | parse error, line 2014: Bad character | parse error, line 2014: Bad character; exit 4 |
| Same input with only the leaked include assertion removed | ContradictoryAxioms | ContradictoryAxioms; exit 0 |

The CLI Vampire suite repeated the parser failure for the first eight tests;
the repetitive run was stopped. This was not a completed Vampire suite.
A separate native SUPr run completed at the short diagnostic timeout of 3s:
11/17 passed; 0001, 0002, 0004, 0010, 0012, 0016 timed out. These results
are not directly comparable to the user's longer/default web-app runs.
Ingest also logged a domain-mismatch diagnostic for `domain` argument 2;
that is separate from the independently reproduced TPTP parse failure.

## 1. Include metadata leaks into logic

Every GEG source has:

```lisp
(include tests/CASC/axiom-sets/full.sources)
```

`crates/core/src/parse/tq/parser.rs` does not list `include` in DIRECTIVES.
It therefore becomes a hypothesis, not a dependency declaration. No runner
currently consumes TestCase.extra_files to resolve the manifest either.
This is also explicitly documented as pending in CASC/INCLUDE-PLAN.md.

The TPTP contains:

```tptp
tff(kb_10137846432917837095, axiom, s__include(s__tests/CASC/axiom_sets/full_sources)).
```

`crates/core/src/trans/symbol.rs` replaces dots and hyphens but leaves slashes
in unquoted symbols. Vampire rejects `/` in this position. See
`leaked-include.p` for a tiny syntax reproducer. Native SUPr does not parse
this serialized TPTP and therefore avoids this failure.

The correct repair is to recognize and resolve the dependency metadata, not
merely rename the invalid symbol. The manifest must not become an axiom.

There is an additional reporting issue: `is_input_error` in
`crates/core/src/prover/vampire_proof.rs` recognizes `Parse error`, but
Vampire emits lowercase `parse error`. The CLI consequently reports a vague
GaveUp instead of InputError for this failure. The web bridge uses the same
transcript classifier.

## 2. A three-axiom background contradiction remains

`background-contradiction.p` contains six type declarations and only three
translated axioms, with no conjecture. Standalone Vampire reports
Unsatisfiable; its proof is in `background-contradiction.log`.

The axioms come from:

- Economy.kif:6041: an OrganicObjectFn result classified under Object implies
  an instance of its input class exists.
- Merge.kif:10878: an instance of DayFn(N, M) implies N <= 31.
- A generated rangeSubclass specialization for OrganicObjectFn, derived from
  Economy.kif:6023 and the rangeSubclass schema at Merge.kif:362.

Reasoning:

1. The emitted range axiom makes OrganicObjectFn(C) a subclass of Object
   for every individual C, with no restriction on its input.
2. The Economy existential rule then gives an instance of every C.
3. Choose C = DayFn(32, M). The day constraint implies 32 <= 31.

This proof never uses the geography conjecture. It is not a countermodel to
BadwaterBasin being a subregion of MojaveDesert.

`OrganicObjectFn` declares `domainSubclass ... OrganicObject`, but neither
of the implicated emitted axioms enforces that condition. The next semantic
repair needs to audit domainSubclass guards and function definedness in
signature specialization and preprocessing. The reproducer establishes the
inconsistency of the current encoding; it does not by itself establish that
the intended SUMO semantics are inconsistent, or that one local guard edit
would fix all full-SUMO contradictions.

`minLang` is currently parsed as metadata but does not select the prover's
language. Auto mode chose TFF because selected background axioms contain
numbers, including the day constraint, even for the FOF-marked GEG query.

## Recommended repair order

1. Implement include metadata/dependency resolution using the existing source
   machinery and the contract in INCLUDE-PLAN.md. Never assert includes.
2. Recognize Vampire's lowercase parse errors so input failures are visible.
3. Repair and regression-test domain/definedness handling against the minimal
   contradiction, then rerun GEG with the intended language and timeout.

Do not count a proof from contradictory axioms as a passing geography test.
SUPr proving the query via a useful subset of axioms is compatible with
Vampire discovering a contradiction elsewhere in the selected background.
