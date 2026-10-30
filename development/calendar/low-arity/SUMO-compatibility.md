# SUMO compatibility review

Reviewed the user attachment 475d5f0f-8644-4563-9bb3-6a30bf772a73 against
this checkout of Merge.kif, Weather.kif, and repository-wide symbol searches.
The attachment matches development/calendar/low-arity/DateTime.kif.
No ontology axioms were changed by this review.

## Integration that is present

| DateTime symbol | Relationship to SUMO |
| --- | --- |
| MonthNumberFn | Numeric adapter: 1 = January through 12 = December. |
| DateFromYMDFn | Alias for DayFn(D, MonthFn(MonthNumberFn(M), YearFn(Y))). |
| DateTimeOnDateFn | For DateFromYMDFn dates, aliases MinuteFn(Min, HourFn(H, date)). |
| YearIntervalFn | Its result is asserted to be an instance of YearFn(Y). |
| MonthIntervalFn | Its result is asserted to be an instance of MonthFn(monthClass, YearFn(Y)). |
| DayIntervalFn | Its result is asserted to be an instance of DateFromYMDFn(Y,M,D). |
| MinuteIntervalFn | For constructed dates/times, its result is asserted to be an instance of the minute class. |

Merge.kif:8918-9029 defines the native class-valued calendar functions.
YearFn, MonthFn, DayFn, HourFn and MinuteFn return classes (rangeSubclass),
not individual TimeIntervals. The interval wrappers return individuals
(range TimeInterval). They must not simply be equated to the native classes.
The file uses SUMO's existing starts, finishes, during and meetsTemporally.
Their endpoint semantics match the intended strict interval relations here.

MonthDuration, YearDuration and DayDuration are measurement units, not
calendar constructors. DayDuration is 24 hours; MonthDuration is constrained
to a 28-31 day range; YearDuration is explicitly 365 DayDuration in this
checkout (Merge.kif:7296-7357). They do not replace MonthFn or YearFn.

## Duplication and missing connections

1. Month lengths and leap arithmetic overlap with SUMO. Merge.kif:9442-9460
   already describes LeapYear and its divisibility condition. The formal
   implication is from LeapYear membership to that condition, not its
   converse. DateTime computes daysInMonth but never asserts LeapYear or
   non-LeapYear membership for the associated YearIntervalFn result.
2. Merge.kif:9504-9772 already supplies month durations and consecutive-month
   adjacency. Merge.kif:8963-9029 supplies within-month day, within-day hour,
   and within-hour minute adjacency. Several DateTime bridge rules restate
   or specialize this existing knowledge. Boundary and normalization rules
   still add useful material.
3. Weather.kif:629-672 already has NumberOfDaysInMonthFn. Its first argument
   is a Month subclass, and its second is a Year instance. daysInMonth uses
   numeric month and year coordinates, so a signature-aware bridge is needed
   before identifying them. Do not substitute YearFn(Y), which is a class,
   for the required Year instance. Also review Weather.kif:651-661 before
   adding a bridge: its 28-day condition says the year differs from some
   LeapYear instance, rather than asserting that the year is not a LeapYear.
4. There is no explicit rule from daysInMonth(M,Y,L) to
   duration(MonthIntervalFn(Y,M), MeasureFn(L,DayDuration)). In particular,
   the supplied leap calculation does not by itself classify a year as a
   LeapYear for SUMO's February-duration rules. Membership in a constructed
   MonthFn class is also not explicitly declared to imply membership in its
   named January/February/etc. class by this file.
5. YearIntervalFn membership already brings in SUMO's generic Year-duration
   axiom (Merge.kif:9156-9163). A future 366-day leap-year duration bridge
   must account for the existing 365-day YearDuration equality; do not claim
   the current SUMO units already distinguish leap-year durations.

## Compatibility defects in the supplied file

### Unrestricted construction of invalid dates and times

DateFromYMDFn's defining equality (DateTime.kif:126-134) accepts any Integer
day, including 0 and 32. DayFn requires PositiveInteger (Merge.kif:8954),
and any DayFn instance must have a day number <=31 (Merge.kif:8963-8966).
DayIntervalFn's membership rule (DateTime.kif:399-406) also accepts every
integer day. Thus, with integer year/month and day 32, these rules assert an
instance of DayFn(32, monthClass); SUMO then entails 32 <= 31. This is an
out-of-range conflict derived from the explicit rules, not merely a missing
validator annotation. The current validation passes do not detect it.

DateTimeOnDateFn's equality and the minute-interval membership rule likewise
accept any Integer hour/minute. SUMO's HourFn and MinuteFn require
NonnegativeInteger, and instantiated hours/minutes must be <24 and <60
(Merge.kif:8983-9029). The constructor and instance bridges need validity and
range guards; guarding only the later adjacency rules is insufficient.
MonthIntervalFn also needs a 1-12 month guard. Keep dateCalculation's day
coordinate as Integer, since zero/negative/overflow coordinates are intentional
normalization inputs; guard the realized output, not that input coordinate.

### Partial generic minute interface

DateTimeOnDateFn is declared for any Day subclass, but its defining equation
covers only DateFromYMDFn terms. MinuteIntervalFn is declared for any Minute
subclass, but its membership bridge covers only the package's constructed
minute terms. The advertised generic behavior needs matching guarded rules
or narrower documentation/interfaces.

### Signature-only placeholders

daysInYear and nthWeekdayInMonth still have no defining computation rules.
The weekday benchmarks assume nthWeekdayInMonth as a premise; they do not
calculate weekdays.

## Verification performed

- Loaded the exact attachment after Merge.kif in the locally built sigma-rs
  WASM engine: no parse errors, semantic errors, or warnings for DateTime.
- Proved the YearIntervalFn -> YearFn membership bridge in one inference.
- Proved the DateFromYMDFn -> nested DayFn/MonthFn/YearFn equality in one inference.
- Proved the constructed MinuteIntervalFn membership bridge in one inference.
- Existing leap and interval tests exercise selected positive cases only.

These are integration checks, not a consistency proof. The out-of-range
construction issue must be fixed before calling the extension fully compatible.
Recommended order: guard constructors and realization bridges, make the minute
interfaces consistent, then add explicit LeapYear/duration integration and
review overlap with Weather.kif. Keep SUMO's existing calendar ontology as
the base rather than introducing replacement Month/Year/Day classes or units.
