fof(example_1, axiom, ( s__instance(s__activationMeasure__m,s__BinaryPredicate) )).
fof(example_2, axiom, ( s__domain(s__activationMeasure__m,n__1,s__ROEActivation) )).
fof(example_3, axiom, ( s__domain(s__activationMeasure__m,n__2,s__ROEMeasure) )).
fof(example_4, axiom, ( s__instance(s__activationOperation__m,s__BinaryPredicate) )).
fof(example_5, axiom, ( s__domain(s__activationOperation__m,n__1,s__ROEActivation) )).
fof(example_6, axiom, ( s__domain(s__activationOperation__m,n__2,s__MilitaryOperation) )).
fof(example_7, axiom, ( s__instance(s__measureInSeries__m,s__BinaryPredicate) )).
fof(example_8, axiom, ( s__domain(s__measureInSeries__m,n__1,s__ROEMeasure) )).
fof(example_9, axiom, ( s__domain(s__measureInSeries__m,n__2,s__ROESeries) )).
fof(example_10, axiom, ( s__instance(s__measureAuthorizes__m,s__BinaryPredicate) )).
fof(example_11, axiom, ( s__domain(s__measureAuthorizes__m,n__1,s__ROEMeasure) )).
fof(example_12, axiom, ( s__domainSubclass(s__measureAuthorizes__m,n__2,s__Process) )).
fof(example_13, axiom, ( s__instance(s__actionAuthorized__m,s__BinaryPredicate) )).
fof(example_14, axiom, ( s__domain(s__actionAuthorized__m,n__1,s__Process) )).
fof(example_15, axiom, ( s__domain(s__actionAuthorized__m,n__2,s__MilitaryOperation) )).
fof(example_16, axiom, ( s__subclass(s__ROESeries,s__Proposition) )).
fof(example_17, axiom, ( s__subclass(s__ROEActivation,s__Proposition) )).
fof(example_18, axiom, ( s__subclass(s__ROEMeasure,s__Proposition) )).
fof(example_19, axiom, ( s__subclass(s__CompleteROEMeasure,s__ROEMeasure) )).
fof(example_20, axiom, ( s__instance(s__ROESeries21,s__ROESeries) )).
fof(example_21, axiom, ( s__instance(s__ROE21B,s__ROEMeasure) )).
fof(example_22, axiom, ( s__instance(s__ROE21B,s__CompleteROEMeasure) )).
fof(example_23, axiom, ( s__measureInSeries(s__ROE21B,s__ROESeries21) )).
fof(example_24, axiom, ( s__measureAuthorizes(s__ROE21B,s__NonDeadlyForceMovementProtection) )).
fof(example_25, axiom, ( s__subclass(s__MovementInterference,s__Process) )).
fof(example_26, axiom, ( ( ! [V__I] : (((s__instance(V__I,s__Process) & s__hinders(V__I,s__Translocation)) => s__instance(V__I,s__MovementInterference)) ) ) )).
fof(example_27, axiom, ( s__subclass(s__ForceMovementInterference,s__MovementInterference) )).
fof(example_28, axiom, ( ( ! [V__I,V__P] : (((s__instance(V__I,s__MovementInterference) & s__instance(V__P,s__Human) & s__attribute(V__P,s__MilitaryPerson) & s__patient(V__I,V__P)) => s__instance(V__I,s__ForceMovementInterference)) ) ) )).
fof(example_29, axiom, ( s__subclass(s__UseOfForce,s__IntentionalProcess) )).
fof(example_30, axiom, ( s__subclass(s__ForceMovementProtection,s__UseOfForce) )).
fof(example_31, axiom, ( ( ! [V__A] : (((s__instance(V__A,s__UseOfForce) & s__prevents(V__A,s__ForceMovementInterference)) => s__instance(V__A,s__ForceMovementProtection)) ) ) )).
fof(example_32, axiom, ( s__subclass(s__NonDeadlyForceMovementProtection,s__ForceMovementProtection) )).
fof(example_33, axiom, ( ( ! [V__A] : (((s__instance(V__A,s__ForceMovementProtection) & s__property(V__A,s__NonDeadlyForce)) => s__instance(V__A,s__NonDeadlyForceMovementProtection)) ) ) )).
fof(example_34, axiom, ( s__subclass(s__ForceCharacter,s__Attribute) )).
fof(example_35, axiom, ( s__instance(s__NonDeadlyForce,s__ForceCharacter) )).
fof(example_36, axiom, ( s__instance(s__DeadlyForce,s__ForceCharacter) )).
fof(example_37, axiom, ( ( ! [V__ACT,V__ACTV,V__C,V__M,V__OP] : (((s__activationMeasure(V__ACTV,V__M) & s__activationOperation(V__ACTV,V__OP) & s__instance(V__M,s__CompleteROEMeasure) & s__measureAuthorizes(V__M,V__C) & s__instance(V__ACT,V__C)) => s__actionAuthorized(V__ACT,V__OP)) ) ) )).
fof(example_38, axiom, ( ( ! [V__C1,V__C2,V__X] : (((s__instance(V__X,V__C1) & s__subclass(V__C1,V__C2)) => s__instance(V__X,V__C2)) ) ) )).
fof(example_39, axiom, ( s__instance(s__OpFreedom,s__MilitaryOperation) )).
fof(example_40, axiom, ( s__instance(s__Sailor1,s__Human) )).
fof(example_41, axiom, ( s__attribute(s__Sailor1,s__MilitaryPerson) )).
fof(example_42, axiom, ( s__instance(s__Blockade1,s__Process) )).
fof(example_43, axiom, ( s__hinders(s__Blockade1,s__Translocation) )).
fof(example_44, axiom, ( s__patient(s__Blockade1,s__Sailor1) )).
fof(example_45, axiom, ( s__instance(s__ResponseForce,s__UseOfForce) )).
fof(example_46, axiom, ( s__prevents(s__ResponseForce,s__ForceMovementInterference) )).
fof(example_47, axiom, ( s__property(s__ResponseForce,s__NonDeadlyForce) )).
fof(example_48, axiom, ( s__instance(s__Act3,s__ROEActivation) )).
fof(example_49, axiom, ( s__activationMeasure(s__Act3,s__ROE21B) )).
fof(example_50, axiom, ( s__activationOperation(s__Act3,s__OpFreedom) )).
fof(conjecture, conjecture, ( s__actionAuthorized(s__ResponseForce,s__OpFreedom) )).
