# Calendar KIF cleanup

Load `Merge.kif`, then `DateTime.kif`. Submit formulas in
`DateTime-benchmarks.kif` individually as queries; do not add them as axioms.
For Java Sigma installations that require a separately loaded signature file,
split the Signatures section from the rules and load it first.

Changes from the supplied text:

- Declare dateCalculation as QuaternaryPredicate and nthWeekdayDate as
  QuintaryPredicate.
- Retain the existing function and predicate interfaces, adding explicit
  valence facts for the five-input functions and seven/nine-place predicates.
- Wrap 16 integer sums/differences in FloorFn. SUMO declares AdditionFn and
  SubtractionFn to return RealNumber, whereas FloorFn returns Integer.
  All operands here are constrained to integers, so these wrappers preserve
  their arithmetic values without changing SUMO's global function ranges.
- Add the sufficient-condition rule for validCalendarDate. The supplied file
  had only the necessary-condition implication, so valid coordinates could
  not establish validity from the provided month-length axioms alone.
- Move the nine conjectures into a separate file and clarify the single-file
  organization. Add documentation for the four interval functions.

Validation:

Run `node development/calendar/validate.mjs` from the SUMO repository with a
built sigma-rs repository beside it, or set SIGMA_RS_ROOT to that repository.
The script loads Merge.kif and the two files solely for semantic validation;
it does not attempt proofs. Results are saved in validation.json.

The local engine reports zero errors, 13 missing-arity warning occurrences,
and 28 natural-language formatting hints for the calendar files. Merge.kif
also emits its own existing duplicate-formula notice and background diagnostics.
The warnings concern DateTimeFromYMDHMFn and DateTimeMinuteIntervalFn. Both
have five inputs, hence six-place function graphs. Core SUMO's fixed-arity
classes and this validator's arity table stop at QuintaryRelation (which
supports four-input functions). The explicit valence 5 facts are accurate,
but this validator does not use them to determine arity. Resolving those
warnings requires extending the ontology and validator's fixed-arity support,
or changing the function interfaces. VariableArityRelation would misstate
these fixed signatures, so it is not used as a workaround.

Remaining modeling scope:

- nthWeekdayDate has a signature but no weekday-calculation rules here.
  The weekday benchmarks assume an nthWeekdayDate premise; they do not
  demonstrate that its date can be calculated.
- daysInYear, timeNormalization, and dateTimeCalculation have signatures
  but no defining rules in the supplied material.
- Constructors retain the supplied behavior outside valid calendar ranges.
  This cleanup does not establish consistency or prove the conjectures.
