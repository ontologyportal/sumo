fof(example_1, axiom, ( s__instance(s__measureInSeries__m,s__BinaryPredicate) )).
fof(example_2, axiom, ( s__domain(s__measureInSeries__m,n__1,s__ROEMeasure) )).
fof(example_3, axiom, ( s__domain(s__measureInSeries__m,n__2,s__ROESeries) )).
fof(example_4, axiom, ( s__instance(s__measureAuthorizes__m,s__BinaryPredicate) )).
fof(example_5, axiom, ( s__domain(s__measureAuthorizes__m,n__1,s__ROEMeasure) )).
fof(example_6, axiom, ( s__domainSubclass(s__measureAuthorizes__m,n__2,s__Process) )).
fof(example_7, axiom, ( s__instance(s__measureSubsumes__m,s__BinaryPredicate) )).
fof(example_8, axiom, ( s__domain(s__measureSubsumes__m,n__1,s__ROEMeasure) )).
fof(example_9, axiom, ( s__domain(s__measureSubsumes__m,n__2,s__ROEMeasure) )).
fof(example_10, axiom, ( s__subclass(s__ROESeries,s__Proposition) )).
fof(example_11, axiom, ( s__subclass(s__ROEMeasure,s__Proposition) )).
fof(example_12, axiom, ( s__subclass(s__CompleteROEMeasure,s__ROEMeasure) )).
fof(example_13, axiom, ( s__instance(s__ROESeries21,s__ROESeries) )).
fof(example_14, axiom, ( s__instance(s__ROE21B,s__ROEMeasure) )).
fof(example_15, axiom, ( s__instance(s__ROE21B,s__CompleteROEMeasure) )).
fof(example_16, axiom, ( s__measureInSeries(s__ROE21B,s__ROESeries21) )).
fof(example_17, axiom, ( s__measureAuthorizes(s__ROE21B,s__NonDeadlyForceMovementProtection) )).
fof(example_18, axiom, ( s__instance(s__ROE21C,s__ROEMeasure) )).
fof(example_19, axiom, ( s__instance(s__ROE21C,s__CompleteROEMeasure) )).
fof(example_20, axiom, ( s__measureInSeries(s__ROE21C,s__ROESeries21) )).
fof(example_21, axiom, ( s__measureAuthorizes(s__ROE21C,s__ForceMovementProtection) )).
fof(example_22, axiom, ( s__subclass(s__UseOfForce,s__IntentionalProcess) )).
fof(example_23, axiom, ( s__subclass(s__ForceMovementProtection,s__UseOfForce) )).
fof(example_24, axiom, ( s__subclass(s__NonDeadlyForceMovementProtection,s__ForceMovementProtection) )).
fof(example_25, axiom, ( ( ! [V__C1,V__C2,V__C3] : (((s__subclass(V__C1,V__C2) & s__subclass(V__C2,V__C3)) => s__subclass(V__C1,V__C3)) ) ) )).
fof(example_26, axiom, ( ( ! [V__C1,V__C2,V__M1,V__M2] : (((s__measureAuthorizes(V__M1,V__C1) & s__measureAuthorizes(V__M2,V__C2) & s__subclass(V__C2,V__C1)) => s__measureSubsumes(V__M1,V__M2)) ) ) )).
fof(conjecture, conjecture, ( s__measureSubsumes(s__ROE21C,s__ROE21B) )).
