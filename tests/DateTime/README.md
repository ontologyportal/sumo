# DateTime integration tests

Load the repository-root Merge.kif followed by the repository-root DateTime.kif.
These tests target the integrated root file, not the older copies under
development/calendar. Each .kif.tq file supplies its own premises and expects
(answer yes). No test query is added as a background axiom.

Run with a built sigma-rs repository alongside SUMO:

    node tests/DateTime/validate.mjs

Or set SIGMA_RS_ROOT to the sigma-rs checkout. To run one proof:

    node tests/DateTime/validate.mjs ordinary_leap.kif.tq

The runner uses the locally built packages/sigmakee/dist engine, isolates
premises in named sessions, checks semantic diagnostics for DateTime.kif,
checks CNF clause length against the default maxLits=8, proves each query,
and checks FOF/TFF export. A complete run writes validation.json. It does not
require a Rust rebuild and does not change sigma-rs.

Changes in the root DateTime.kif:

- validCalendarMonth and validClockTime centralize coordinate guards. Invalid
  months, nonpositive dates and out-of-range times do not acquire calendar
  realization through the old unrestricted constructor rules.
- DateFromYMDFn is equated to SUMO DayFn only for validCalendarDate coordinates.
  dateCalculation still accepts Integer days, including zero/negative/overflow,
  and only the valid base case realizes a date class. Recursive month inputs
  must be within 1-12. Successor-day interval rules also check the output date.
- DateTimeOnDateFn now covers any Day subclass with valid clock coordinates.
  MinuteIntervalFn realizes validated concrete dates/times and can also select
  an instance of an already-inhabited Minute subclass. It does not instantiate
  every arbitrary (possibly empty) minute class.
- daysInYear is now defined by the Gregorian divisibility rules. February's
  length uses that shared count. All associated SUMO year instances are
  classified as LeapYear for 366 days or explicitly non-LeapYear for 365.
- Dated MonthFn classes specialize their existing named month class.
  MonthIntervalFn lengths are connected to SUMO TimeDuration values equal to
  MeasureFn(L,DayDuration), following SUMO's typed-duration pattern.
- Functions with restricted meaningful inputs are marked PartialValuedRelation.
  Numeric signatures remain Integer so declared arithmetic result types remain
  compatible; the defining/realization rules enforce the narrower valid ranges.
- Repeated guards are factored so no DateTime CNF clause exceeds eight literals.
  The native prover can otherwise drop KIF/SUMO clauses longer than maxLits,
  which can leave even a correct recurrence query unproved.

Coverage includes January length; ordinary and century leap/common years;
SUMO LeapYear membership and nonmembership; valid/invalid dates and clocks;
date aliases; valid day/minute instances; generic date and inhabited-minute
interfaces; named-month specialization; duration; January's year boundary;
and base, overflow, December rollover, underflow and January rollover steps.
Divisibility and recursive-normalization arithmetic premises are explicit:
these are rule tests, not tests that the native prover calculates remainders
or FloorFn expressions. Proof success is not a consistency proof.

Deferred work:

- Weather.kif's NumberOfDaysInMonthFn is not equated with daysInMonth. Its
  argument types differ and its existing February rule needs independent review.
- No 366-day duration conversion is added: Merge.kif currently equates
  YearDuration with 365 DayDuration. daysInYear is a calendar count only.
- Existing adjacency/boundary axioms are retained. Removing them requires
  equivalence proofs with the relevant SUMO rules; a full-background month
  adjacency search was inconclusive within the bounded local proof run.
- nthWeekdayInMonth remains a declaration, not a weekday calculation algorithm.
- Earlier generated development/calendar copies are historical and were not
  synchronized. Use the root DateTime.kif for these integration changes.
