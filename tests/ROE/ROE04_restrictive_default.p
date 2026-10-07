fof(example_1, axiom, ( s__instance(s__measureInSeries__m,s__BinaryPredicate) )).
fof(example_2, axiom, ( s__domain(s__measureInSeries__m,n__1,s__ROEMeasure) )).
fof(example_3, axiom, ( s__domain(s__measureInSeries__m,n__2,s__ROESeries) )).
fof(example_4, axiom, ( s__instance(s__measureAuthorizes__m,s__BinaryPredicate) )).
fof(example_5, axiom, ( s__domain(s__measureAuthorizes__m,n__1,s__ROEMeasure) )).
fof(example_6, axiom, ( s__domainSubclass(s__measureAuthorizes__m,n__2,s__Process) )).
fof(example_7, axiom, ( s__instance(s__measureProhibits__m,s__BinaryPredicate) )).
fof(example_8, axiom, ( s__domain(s__measureProhibits__m,n__1,s__ROEMeasure) )).
fof(example_9, axiom, ( s__domainSubclass(s__measureProhibits__m,n__2,s__Process) )).
fof(example_10, axiom, ( s__instance(s__seriesAddresses__m,s__BinaryPredicate) )).
fof(example_11, axiom, ( s__domain(s__seriesAddresses__m,n__1,s__ROESeries) )).
fof(example_12, axiom, ( s__domainSubclass(s__seriesAddresses__m,n__2,s__Process) )).
fof(example_13, axiom, ( s__instance(s__seriesNotAddressed__m,s__BinaryPredicate) )).
fof(example_14, axiom, ( s__domain(s__seriesNotAddressed__m,n__1,s__ROESeries) )).
fof(example_15, axiom, ( s__domain(s__seriesNotAddressed__m,n__2,s__MilitaryOperation) )).
fof(example_16, axiom, ( s__instance(s__actionUnauthorized__m,s__BinaryPredicate) )).
fof(example_17, axiom, ( s__domain(s__actionUnauthorized__m,n__1,s__Process) )).
fof(example_18, axiom, ( s__domain(s__actionUnauthorized__m,n__2,s__MilitaryOperation) )).
fof(example_19, axiom, ( s__subclass(s__ROESeries,s__Proposition) )).
fof(example_20, axiom, ( s__subclass(s__ROEMeasure,s__Proposition) )).
fof(example_21, axiom, ( s__subclass(s__CompleteROEMeasure,s__ROEMeasure) )).
fof(example_22, axiom, ( s__subclass(s__TemplateROEMeasure,s__ROEMeasure) )).
fof(example_23, axiom, ( s__instance(s__ROESeries23,s__ROESeries) )).
fof(example_24, axiom, ( s__instance(s__ROE23E,s__ROEMeasure) )).
fof(example_25, axiom, ( s__instance(s__ROE23E,s__CompleteROEMeasure) )).
fof(example_26, axiom, ( s__measureInSeries(s__ROE23E,s__ROESeries23) )).
fof(example_27, axiom, ( s__measureAuthorizes(s__ROE23E,s__WarningShot) )).
fof(example_28, axiom, ( s__instance(s__ROE23A,s__ROEMeasure) )).
fof(example_29, axiom, ( s__instance(s__ROE23A,s__CompleteROEMeasure) )).
fof(example_30, axiom, ( s__measureInSeries(s__ROE23A,s__ROESeries23) )).
fof(example_31, axiom, ( s__measureProhibits(s__ROE23A,s__WarningShot) )).
fof(example_32, axiom, ( s__subclass(s__WarningShot,s__Shooting) )).
fof(example_33, axiom, ( ( ! [V__C,V__M,V__S] : (((s__measureInSeries(V__M,V__S) & s__measureAuthorizes(V__M,V__C)) => s__seriesAddresses(V__S,V__C)) ) ) )).
fof(example_34, axiom, ( ( ! [V__C,V__M,V__S] : (((s__measureInSeries(V__M,V__S) & s__measureProhibits(V__M,V__C)) => s__seriesAddresses(V__S,V__C)) ) ) )).
fof(example_35, axiom, ( ( ! [V__ACT,V__C,V__OP,V__S] : (((s__seriesNotAddressed(V__S,V__OP) & s__seriesAddresses(V__S,V__C) & s__instance(V__ACT,V__C)) => s__actionUnauthorized(V__ACT,V__OP)) ) ) )).
fof(example_36, axiom, ( ( ! [V__C1,V__C2,V__X] : (((s__instance(V__X,V__C1) & s__subclass(V__C1,V__C2)) => s__instance(V__X,V__C2)) ) ) )).
fof(example_37, axiom, ( s__instance(s__OpBravo,s__MilitaryOperation) )).
fof(example_38, axiom, ( s__seriesNotAddressed(s__ROESeries23,s__OpBravo) )).
fof(example_39, axiom, ( s__instance(s__Shot303,s__WarningShot) )).
fof(conjecture, conjecture, ( s__actionUnauthorized(s__Shot303,s__OpBravo) )).
