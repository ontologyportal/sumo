fof(example_1, axiom, ( s__instance(s__activationMeasure__m,s__BinaryPredicate) )).
fof(example_2, axiom, ( s__domain(s__activationMeasure__m,n__1,s__ROEActivation) )).
fof(example_3, axiom, ( s__domain(s__activationMeasure__m,n__2,s__ROEMeasure) )).
fof(example_4, axiom, ( s__instance(s__activationOperation__m,s__BinaryPredicate) )).
fof(example_5, axiom, ( s__domain(s__activationOperation__m,n__1,s__ROEActivation) )).
fof(example_6, axiom, ( s__domain(s__activationOperation__m,n__2,s__MilitaryOperation) )).
fof(example_7, axiom, ( s__instance(s__actionAuthorized__m,s__BinaryPredicate) )).
fof(example_8, axiom, ( s__domain(s__actionAuthorized__m,n__1,s__Process) )).
fof(example_9, axiom, ( s__domain(s__actionAuthorized__m,n__2,s__MilitaryOperation) )).
fof(example_10, axiom, ( s__instance(s__actionPermissible__m,s__BinaryPredicate) )).
fof(example_11, axiom, ( s__domain(s__actionPermissible__m,n__1,s__Process) )).
fof(example_12, axiom, ( s__domain(s__actionPermissible__m,n__2,s__MilitaryOperation) )).
fof(example_13, axiom, ( s__instance(s__noProhibitionReaches__m,s__BinaryPredicate) )).
fof(example_14, axiom, ( s__domain(s__noProhibitionReaches__m,n__1,s__Process) )).
fof(example_15, axiom, ( s__domain(s__noProhibitionReaches__m,n__2,s__MilitaryOperation) )).
fof(example_16, axiom, ( s__instance(s__measureAuthorizes__m,s__BinaryPredicate) )).
fof(example_17, axiom, ( s__domain(s__measureAuthorizes__m,n__1,s__ROEMeasure) )).
fof(example_18, axiom, ( s__domainSubclass(s__measureAuthorizes__m,n__2,s__Process) )).
fof(example_19, axiom, ( s__subclass(s__ROEActivation,s__Proposition) )).
fof(example_20, axiom, ( s__subclass(s__ROEMeasure,s__Proposition) )).
fof(example_21, axiom, ( s__subclass(s__CompleteROEMeasure,s__ROEMeasure) )).
fof(example_22, axiom, ( s__instance(s__ROE23E,s__ROEMeasure) )).
fof(example_23, axiom, ( s__instance(s__ROE23E,s__CompleteROEMeasure) )).
fof(example_24, axiom, ( s__measureAuthorizes(s__ROE23E,s__WarningShot) )).
fof(example_25, axiom, ( s__subclass(s__WarningShot,s__Shooting) )).
fof(example_26, axiom, ( ( ! [V__ACT,V__ACTV,V__C,V__M,V__OP] : (((s__activationMeasure(V__ACTV,V__M) & s__activationOperation(V__ACTV,V__OP) & s__instance(V__M,s__CompleteROEMeasure) & s__measureAuthorizes(V__M,V__C) & s__instance(V__ACT,V__C)) => s__actionAuthorized(V__ACT,V__OP)) ) ) )).
fof(example_27, axiom, ( ( ! [V__ACT,V__OP] : (((s__actionAuthorized(V__ACT,V__OP) & s__noProhibitionReaches(V__ACT,V__OP)) => s__actionPermissible(V__ACT,V__OP)) ) ) )).
fof(example_28, axiom, ( ( ! [V__C1,V__C2,V__X] : (((s__instance(V__X,V__C1) & s__subclass(V__C1,V__C2)) => s__instance(V__X,V__C2)) ) ) )).
fof(example_29, axiom, ( s__instance(s__OpAlpha,s__MilitaryOperation) )).
fof(example_30, axiom, ( s__instance(s__Shot202,s__WarningShot) )).
fof(example_31, axiom, ( s__noProhibitionReaches(s__Shot202,s__OpAlpha) )).
fof(example_32, axiom, ( s__instance(s__Act1,s__ROEActivation) )).
fof(example_33, axiom, ( s__activationMeasure(s__Act1,s__ROE23E) )).
fof(example_34, axiom, ( s__activationOperation(s__Act1,s__OpAlpha) )).
fof(conjecture, conjecture, ( s__actionPermissible(s__Shot202,s__OpAlpha) )).
