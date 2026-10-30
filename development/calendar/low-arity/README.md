# Calendar variant with lower arity

Load this DateTime.kif after Merge.kif, instead of the parent version.
Use this directory's DateTime-benchmarks.kif as individual queries.
The interfaces differ, so callers must migrate with the axioms.

| Previous expression | Replacement |
| --- | --- |
| DateTimeFromYMDHMFn(Y,M,D,H,Min) | DateTimeOnDateFn(DateFromYMDFn(Y,M,D),H,Min) |
| DateTimeMinuteIntervalFn(Y,M,D,H,Min) | MinuteIntervalFn(DateTimeOnDateFn(DateFromYMDFn(Y,M,D),H,Min)) |
| nthWeekdayDate(N,W,M,Y,R) | nthWeekdayInMonth(N,W,MonthFn(MonthNumberFn(M),YearFn(Y)),R) |

The package's predicates now have at most four arguments, and its functions
have at most three inputs (four-place relation graphs). dateCalculation stays
quaternary; daysInMonth and validCalendarDate stay ternary. The grouped date
and month arguments are SUMO classes, constrained using domainSubclass.
No variadic ListFn, row variables, or new tuple constructors are introduced.

The supplied timeNormalization/7 and dateTimeCalculation/9 signatures had no
rules or uses, and did not document their coordinate order. This variant omits
them; it does not implement normalization or migrate any external callers.
Their real definitions are needed before choosing a replacement. A likely
approach is separate date normalization and time normalization with a day
carry between them, or a binary relation between structured input/output
states. Those designs need explicit semantics and supporting axioms.

Validation against the locally built sigma-rs engine and Merge.kif:

- Zero semantic errors and zero warnings; 24 natural-language formatting hints.
- All active non-metadata formulas and all nine queries round-trip to their
  parent versions when these interface replacements are reversed.
- Both FOF and TFF export completed for Merge.kif plus this variant.

Run `node development/calendar/low-arity/validate.mjs` to repeat semantic
validation. Set SIGMA_RS_ROOT if sigma-rs is not beside the SUMO repository.
validation.json records the diagnostics. The parent README explains the
integer wrappers, date-validity rule, and remaining modeling gaps.

Performance is not established by these checks. An explicit nine-argument
atom translates directly to a nine-argument TPTP atom; its arity alone does
not multiply formulas. Row variables expand combinatorially with the number
of independent row variables, and clausification may expand formulas.
Grouping coordinates trades lower arity for deeper function terms. It can
help proof search, but is not guaranteed to do so. Compare actual prover
runs before making a performance claim. No conjecture proofs were run here.
