# Full SUMO contradiction report

Open https://sigmakee.dev/audit and choose Latest master contradiction report.
Save any work you want to keep before confirming replacement and replay.
The app verifies master, constituents, and engine inputs before replaying only the steps below.

## Contradiction 1

- Seed: `0`
- Start step: `1214`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `5`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### Merge.kif:13076

```lisp
(subclass Breathing AutonomicProcess)
```

## Contradiction 2

- Seed: `0`
- Start step: `1214`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `5`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### Merge.kif:13075

```lisp
(subclass Breathing OrganismProcess)
```

## Contradiction 3

- Seed: `0`
- Start step: `1214`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `8`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

## Contradiction 4

- Seed: `0`
- Start step: `1214`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `39`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:3118

```lisp
(subclass CaseRole BinaryPredicate)
```

#### Merge.kif:3290

```lisp
(instance result CaseRole)
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:83

```lisp
(instance instance BinaryPredicate)
```

#### Merge.kif:85

```lisp
(domain instance 2 Class)
```

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### Merge.kif:135

```lisp
(instance subclass BinaryPredicate)
```

#### Merge.kif:138

```lisp
(domain subclass 2 Class)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
```

#### Merge.kif:13075

```lisp
(subclass Breathing OrganismProcess)
```

#### Merge.kif:13012

```lisp
(subclass OrganismProcess PhysiologicProcess)
```

#### Merge.kif:12977

```lisp
(subclass PhysiologicProcess BiologicalProcess)
```

#### Merge.kif:12953

```lisp
(subclass BiologicalProcess InternalChange)
```

#### Merge.kif:16162

```lisp
(subclass InternalChange Process)
```

## Contradiction 5

- Seed: `0`
- Start step: `1214`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `41`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:3118

```lisp
(subclass CaseRole BinaryPredicate)
```

#### Merge.kif:3290

```lisp
(instance result CaseRole)
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:83

```lisp
(instance instance BinaryPredicate)
```

#### Merge.kif:85

```lisp
(domain instance 2 Class)
```

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### Merge.kif:135

```lisp
(instance subclass BinaryPredicate)
```

#### Merge.kif:138

```lisp
(domain subclass 2 Class)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:13076

```lisp
(subclass Breathing AutonomicProcess)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
```

#### Merge.kif:12985

```lisp
(subclass AutonomicProcess PhysiologicProcess)
```

#### Merge.kif:12977

```lisp
(subclass PhysiologicProcess BiologicalProcess)
```

#### Merge.kif:12953

```lisp
(subclass BiologicalProcess InternalChange)
```

#### Merge.kif:16162

```lisp
(subclass InternalChange Process)
```

## Contradiction 6

- Seed: `0`
- Start step: `1224`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### Merge.kif:355

```lisp
(domainSubclass rangeSubclass 2 Class)
```

#### Merge.kif:353

```lisp
(instance rangeSubclass BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6970

```lisp
(subclass BodyOfWater SelfConnectedObject)
```

#### Geography.kif:7032

```lisp
(subclass Ocean BodyOfWater)
```

#### Geography.kif:7085

```lisp
(instance PacificOcean Ocean)
```

#### Merge.kif:961

```lisp
(subclass SelfConnectedObject Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2814

```lisp
(subclass Class SetOrClass)
```

#### Merge.kif:2803

```lisp
(subclass SetOrClass Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 7

- Seed: `0`
- Start step: `1224`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### Merge.kif:355

```lisp
(domainSubclass rangeSubclass 2 Class)
```

#### Merge.kif:353

```lisp
(instance rangeSubclass BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6970

```lisp
(subclass BodyOfWater SelfConnectedObject)
```

#### Geography.kif:7032

```lisp
(subclass Ocean BodyOfWater)
```

#### Geography.kif:7180

```lisp
(instance SouthernOcean Ocean)
```

#### Merge.kif:961

```lisp
(subclass SelfConnectedObject Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2814

```lisp
(subclass Class SetOrClass)
```

#### Merge.kif:2803

```lisp
(subclass SetOrClass Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 8

- Seed: `0`
- Start step: `1224`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `27`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### Merge.kif:355

```lisp
(domainSubclass rangeSubclass 2 Class)
```

#### Merge.kif:353

```lisp
(instance rangeSubclass BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Geography.kif:7032

```lisp
(subclass Ocean BodyOfWater)
```

#### Geography.kif:6970

```lisp
(subclass BodyOfWater SelfConnectedObject)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Geography.kif:7085

```lisp
(instance PacificOcean Ocean)
```

#### Merge.kif:961

```lisp
(subclass SelfConnectedObject Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2814

```lisp
(subclass Class SetOrClass)
```

#### Merge.kif:2803

```lisp
(subclass SetOrClass Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 9

- Seed: `0`
- Start step: `1224`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `27`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### Merge.kif:355

```lisp
(domainSubclass rangeSubclass 2 Class)
```

#### Merge.kif:353

```lisp
(instance rangeSubclass BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Geography.kif:7032

```lisp
(subclass Ocean BodyOfWater)
```

#### Geography.kif:6970

```lisp
(subclass BodyOfWater SelfConnectedObject)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Geography.kif:7180

```lisp
(instance SouthernOcean Ocean)
```

#### Merge.kif:961

```lisp
(subclass SelfConnectedObject Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2814

```lisp
(subclass Class SetOrClass)
```

#### Merge.kif:2803

```lisp
(subclass SetOrClass Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 10

- Seed: `0`
- Start step: `1227`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `5`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### Merge.kif:14696

```lisp
(subclass Touching Transfer)
```

## Contradiction 11

- Seed: `0`
- Start step: `1227`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `14`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### WMD.kif:757

```lisp
(domainSubclass biochemicalAgentDelivery 2 Process)
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### WMD.kif:755

```lisp
(instance biochemicalAgentDelivery BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

## Contradiction 12

- Seed: `0`
- Start step: `1227`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `14`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### WMD.kif:757

```lisp
(domainSubclass biochemicalAgentDelivery 2 Process)
```

#### WMD.kif:755

```lisp
(instance biochemicalAgentDelivery BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

## Contradiction 13

- Seed: `0`
- Start step: `1238`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3813

```lisp
(range ListOrderFn Entity)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
```

#### Merge.kif:13075

```lisp
(subclass Breathing OrganismProcess)
```

#### Merge.kif:13012

```lisp
(subclass OrganismProcess PhysiologicProcess)
```

#### Merge.kif:12977

```lisp
(subclass PhysiologicProcess BiologicalProcess)
```

#### Merge.kif:12953

```lisp
(subclass BiologicalProcess InternalChange)
```

#### Merge.kif:16162

```lisp
(subclass InternalChange Process)
```

## Contradiction 14

- Seed: `0`
- Start step: `1238`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `12`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### WMD.kif:757

```lisp
(domainSubclass biochemicalAgentDelivery 2 Process)
```

#### WMD.kif:755

```lisp
(instance biochemicalAgentDelivery BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

## Contradiction 15

- Seed: `0`
- Start step: `1270`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `18`

### Cited source axioms

#### Merge.kif:786

```lisp
(=> (and (subAttribute ?ATTR1 ?ATTR2) (instance ?ATTR2 ?CLASS)) (instance ?ATTR1 ?CLASS))
```

#### Military.kif:846

```lisp
(subAttribute USMilitaryRankWO4 Soldier)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Military.kif:845

```lisp
(instance USMilitaryRankWO4 CommissionedOfficerRank)
```

#### Military.kif:508

```lisp
(subclass CommissionedOfficerRank MilitaryRank)
```

#### Military.kif:484

```lisp
(subclass MilitaryRank SkilledOccupation)
```

#### Mid-level-ontology.kif:12121

```lisp
(subclass SkilledOccupation OccupationalRole)
```

#### Mid-level-ontology.kif:31597

```lisp
(subclass OccupationalRole SocialRole)
```

#### Merge.kif:22288

```lisp
(subclass SocialRole RelationalAttribute)
```

#### Merge.kif:2393

```lisp
(subclass RelationalAttribute Attribute)
```

#### Merge.kif:2239

```lisp
(subclass Attribute Abstract)
```

#### Mid-level-ontology.kif:35137

```lisp
(subclass MobileCellPhone Telephone)
```

#### Mid-level-ontology.kif:34555

```lisp
(subclass Telephone TelephonyDevice)
```

#### Mid-level-ontology.kif:34539

```lisp
(subclass TelephonyDevice ContactSite)
```

#### Merge.kif:20310

```lisp
(subclass ContactSite Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 16

- Seed: `0`
- Start step: `1270`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:786

```lisp
(=> (and (subAttribute ?ATTR1 ?ATTR2) (instance ?ATTR2 ?CLASS)) (instance ?ATTR1 ?CLASS))
```

#### Military.kif:824

```lisp
(subAttribute USMilitaryRankWO2 Soldier)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Military.kif:821

```lisp
(instance USMilitaryRankWO2 USWarrantOfficerRank)
```

#### Military.kif:807

```lisp
(subclass USWarrantOfficerRank CommissionedOfficerRank)
```

#### Military.kif:508

```lisp
(subclass CommissionedOfficerRank MilitaryRank)
```

#### Military.kif:484

```lisp
(subclass MilitaryRank SkilledOccupation)
```

#### Mid-level-ontology.kif:12121

```lisp
(subclass SkilledOccupation OccupationalRole)
```

#### Mid-level-ontology.kif:31597

```lisp
(subclass OccupationalRole SocialRole)
```

#### Merge.kif:22288

```lisp
(subclass SocialRole RelationalAttribute)
```

#### Merge.kif:2393

```lisp
(subclass RelationalAttribute Attribute)
```

#### Merge.kif:2239

```lisp
(subclass Attribute Abstract)
```

#### Mid-level-ontology.kif:35137

```lisp
(subclass MobileCellPhone Telephone)
```

#### Mid-level-ontology.kif:34555

```lisp
(subclass Telephone TelephonyDevice)
```

#### Mid-level-ontology.kif:34539

```lisp
(subclass TelephonyDevice ContactSite)
```

#### Merge.kif:20310

```lisp
(subclass ContactSite Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 17

- Seed: `0`
- Start step: `1270`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:786

```lisp
(=> (and (subAttribute ?ATTR1 ?ATTR2) (instance ?ATTR2 ?CLASS)) (instance ?ATTR1 ?CLASS))
```

#### Military.kif:835

```lisp
(subAttribute USMilitaryRankWO3 Soldier)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Military.kif:832

```lisp
(instance USMilitaryRankWO3 USWarrantOfficerRank)
```

#### Military.kif:807

```lisp
(subclass USWarrantOfficerRank CommissionedOfficerRank)
```

#### Military.kif:508

```lisp
(subclass CommissionedOfficerRank MilitaryRank)
```

#### Military.kif:484

```lisp
(subclass MilitaryRank SkilledOccupation)
```

#### Mid-level-ontology.kif:12121

```lisp
(subclass SkilledOccupation OccupationalRole)
```

#### Mid-level-ontology.kif:31597

```lisp
(subclass OccupationalRole SocialRole)
```

#### Merge.kif:22288

```lisp
(subclass SocialRole RelationalAttribute)
```

#### Merge.kif:2393

```lisp
(subclass RelationalAttribute Attribute)
```

#### Merge.kif:2239

```lisp
(subclass Attribute Abstract)
```

#### Mid-level-ontology.kif:35137

```lisp
(subclass MobileCellPhone Telephone)
```

#### Mid-level-ontology.kif:34555

```lisp
(subclass Telephone TelephonyDevice)
```

#### Mid-level-ontology.kif:34539

```lisp
(subclass TelephonyDevice ContactSite)
```

#### Merge.kif:20310

```lisp
(subclass ContactSite Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 18

- Seed: `0`
- Start step: `1270`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `16`

### Cited source axioms

#### Merge.kif:786

```lisp
(=> (and (subAttribute ?ATTR1 ?ATTR2) (instance ?ATTR2 ?CLASS)) (instance ?ATTR1 ?CLASS))
```

#### Mid-level-ontology.kif:26748

```lisp
(subAttribute MilitaryOfficer Soldier)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Mid-level-ontology.kif:26749

```lisp
(instance MilitaryOfficer GovernmentPosition)
```

#### Mid-level-ontology.kif:26652

```lisp
(subclass GovernmentPosition Position)
```

#### Merge.kif:22320

```lisp
(subclass Position SocialRole)
```

#### Merge.kif:22288

```lisp
(subclass SocialRole RelationalAttribute)
```

#### Merge.kif:2393

```lisp
(subclass RelationalAttribute Attribute)
```

#### Merge.kif:2239

```lisp
(subclass Attribute Abstract)
```

#### Mid-level-ontology.kif:35137

```lisp
(subclass MobileCellPhone Telephone)
```

#### Mid-level-ontology.kif:34555

```lisp
(subclass Telephone TelephonyDevice)
```

#### Mid-level-ontology.kif:34539

```lisp
(subclass TelephonyDevice ContactSite)
```

#### Merge.kif:20310

```lisp
(subclass ContactSite Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 19

- Seed: `0`
- Start step: `1270`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `5`

### Cited source axioms

#### Media.kif:1299

```lisp
(=> (instance ?SITE WebSite) (exists (?PAGE) (and (instance ?PAGE WebPage) (component ?PAGE ?SITE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### ComputingBrands.kif:2667

```lisp
(instance IBookstore WebSite)
```

## Contradiction 20

- Seed: `0`
- Start step: `1290`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3813

```lisp
(range ListOrderFn Entity)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
```

#### Merge.kif:13076

```lisp
(subclass Breathing AutonomicProcess)
```

#### Merge.kif:12985

```lisp
(subclass AutonomicProcess PhysiologicProcess)
```

#### Merge.kif:12977

```lisp
(subclass PhysiologicProcess BiologicalProcess)
```

#### Merge.kif:12953

```lisp
(subclass BiologicalProcess InternalChange)
```

#### Merge.kif:16162

```lisp
(subclass InternalChange Process)
```

## Contradiction 21

- Seed: `0`
- Start step: `1315`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `12`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Mid-level-ontology.kif:4558

```lisp
(subclass CommunicationDevice EngineeringComponent)
```

#### Mid-level-ontology.kif:4571

```lisp
(subclass Telephone CommunicationDevice)
```

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Mid-level-ontology.kif:35137

```lisp
(subclass MobileCellPhone Telephone)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

## Contradiction 22

- Seed: `0`
- Start step: `1340`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `8`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:343

```lisp
(instance RockyMountains MountainRange)
```

#### Geography.kif:3774

```lisp
(=> (attribute ?AREA MountainousTerrain) (exists (?MTN) (and (instance ?MTN Mountain) (part ?MTN ?AREA))))
```

#### Geography.kif:3788

```lisp
(=> (instance ?AREA MountainRange) (attribute ?AREA MountainousTerrain))
```

## Contradiction 23

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `49`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

## Contradiction 24

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `56`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### CountriesAndRegions.kif:25

```lisp
(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))
```

#### Merge.kif:5075

```lisp
(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

## Contradiction 25

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `57`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### CountriesAndRegions.kif:25

```lisp
(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))
```

#### Merge.kif:5075

```lisp
(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

## Contradiction 26

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `85`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

## Contradiction 27

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `59`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:5075

```lisp
(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Geography.kif:3149

```lisp
(=> (climateTypeInArea ?AREA ?CLASS) (exists (?REGION ?TYPE) (and (instance ?REGION GeographicArea) (instance ?TYPE ?CLASS) (attribute ?REGION ?TYPE) (part ?REGION ?AREA))))
```

#### Geography.kif:516

```lisp
(climateTypeInArea GreatBasin AridClimateZone)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

## Contradiction 28

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `103`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:2947

```lisp
(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))
```

#### Merge.kif:12338

```lisp
(instance meetsSpatially IrreflexiveRelation)
```

## Contradiction 29

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `57`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### Merge.kif:2947

```lisp
(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))
```

#### Merge.kif:12338

```lisp
(instance meetsSpatially IrreflexiveRelation)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

## Contradiction 30

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `116`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

#### CountriesAndRegions.kif:25

```lisp
(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))
```

#### Merge.kif:5075

```lisp
(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

## Contradiction 31

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `107`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Geography.kif:5692

```lisp
(geographicSubregion NorthAmerica NorthernHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

## Contradiction 32

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `107`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Geography.kif:5693

```lisp
(geographicSubregion NorthAmerica WesternHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

## Contradiction 33

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `118`

### Cited source axioms

#### Geography.kif:8040

```lisp
(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Geography.kif:2311

```lisp
(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:2947

```lisp
(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))
```

#### Merge.kif:12338

```lisp
(instance meetsSpatially IrreflexiveRelation)
```

#### CountriesAndRegions.kif:3215

```lisp
(geographicSubregion LosAngelesCalifornia UnitedStates)
```

#### CountriesAndRegions.kif:35

```lisp
(subclass AmericanCity City)
```

#### Merge.kif:18387

```lisp
(subclass City LandArea)
```

## Contradiction 34

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `127`

### Cited source axioms

#### Geography.kif:8040

```lisp
(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Geography.kif:2311

```lisp
(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:2947

```lisp
(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))
```

#### Merge.kif:12338

```lisp
(instance meetsSpatially IrreflexiveRelation)
```

#### CountriesAndRegions.kif:3215

```lisp
(geographicSubregion LosAngelesCalifornia UnitedStates)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Merge.kif:18359

```lisp
(subclass Nation GeopoliticalArea)
```

#### Merge.kif:18164

```lisp
(subclass GeopoliticalArea GeographicArea)
```

#### CountriesAndRegions.kif:35

```lisp
(subclass AmericanCity City)
```

#### Merge.kif:18386

```lisp
(subclass City GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

## Contradiction 35

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `130`

### Cited source axioms

#### Geography.kif:8040

```lisp
(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Geography.kif:2311

```lisp
(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:2947

```lisp
(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))
```

#### Merge.kif:12338

```lisp
(instance meetsSpatially IrreflexiveRelation)
```

#### CountriesAndRegions.kif:35

```lisp
(subclass AmericanCity City)
```

#### Merge.kif:18386

```lisp
(subclass City GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### CountriesAndRegions.kif:3215

```lisp
(geographicSubregion LosAngelesCalifornia UnitedStates)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Merge.kif:18359

```lisp
(subclass Nation GeopoliticalArea)
```

#### Merge.kif:18164

```lisp
(subclass GeopoliticalArea GeographicArea)
```

#### Geography.kif:5693

```lisp
(geographicSubregion NorthAmerica WesternHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

## Contradiction 36

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `130`

### Cited source axioms

#### Geography.kif:8040

```lisp
(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Geography.kif:2311

```lisp
(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:2947

```lisp
(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))
```

#### Merge.kif:12338

```lisp
(instance meetsSpatially IrreflexiveRelation)
```

#### CountriesAndRegions.kif:35

```lisp
(subclass AmericanCity City)
```

#### Merge.kif:18386

```lisp
(subclass City GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### CountriesAndRegions.kif:3215

```lisp
(geographicSubregion LosAngelesCalifornia UnitedStates)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Merge.kif:18359

```lisp
(subclass Nation GeopoliticalArea)
```

#### Merge.kif:18164

```lisp
(subclass GeopoliticalArea GeographicArea)
```

#### Geography.kif:5692

```lisp
(geographicSubregion NorthAmerica NorthernHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

## Contradiction 37

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `125`

### Cited source axioms

#### Geography.kif:8040

```lisp
(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Geography.kif:2311

```lisp
(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:2947

```lisp
(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))
```

#### Merge.kif:12338

```lisp
(instance meetsSpatially IrreflexiveRelation)
```

#### CountriesAndRegions.kif:35

```lisp
(subclass AmericanCity City)
```

#### Merge.kif:18386

```lisp
(subclass City GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### CountriesAndRegions.kif:3215

```lisp
(geographicSubregion LosAngelesCalifornia UnitedStates)
```

## Contradiction 38

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `52`

### Cited source axioms

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:1074

```lisp
(meetsSpatially Nevada California)
```

#### Merge.kif:12339

```lisp
(instance meetsSpatially SymmetricRelation)
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

## Contradiction 39

- Seed: `0`
- Start step: `1349`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `150`

### Cited source axioms

#### Geography.kif:8040

```lisp
(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Geography.kif:2311

```lisp
(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18370

```lisp
(subclass StateOrProvince LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:2947

```lisp
(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))
```

#### Merge.kif:12338

```lisp
(instance meetsSpatially IrreflexiveRelation)
```

#### CountriesAndRegions.kif:86

```lisp
(=> (instance ?N EuropeanNation) (part ?N Europe))
```

#### CountriesAndRegions.kif:377

```lisp
(instance UnitedKingdom EuropeanNation)
```

#### Merge.kif:5075

```lisp
(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Geography.kif:5723

```lisp
(geographicSubregion Europe NorthernHemisphere)
```

#### CountriesAndRegions.kif:83

```lisp
(subclass EuropeanNation Nation)
```

#### Merge.kif:18359

```lisp
(subclass Nation GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### CountriesAndRegions.kif:35

```lisp
(subclass AmericanCity City)
```

#### Merge.kif:18386

```lisp
(subclass City GeopoliticalArea)
```

#### CountriesAndRegions.kif:3215

```lisp
(geographicSubregion LosAngelesCalifornia UnitedStates)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Merge.kif:18164

```lisp
(subclass GeopoliticalArea GeographicArea)
```

#### Geography.kif:5692

```lisp
(geographicSubregion NorthAmerica NorthernHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

## Contradiction 40

- Seed: `0`
- Start step: `1350`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### Merge.kif:355

```lisp
(domainSubclass rangeSubclass 2 Class)
```

#### Merge.kif:353

```lisp
(instance rangeSubclass BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6970

```lisp
(subclass BodyOfWater SelfConnectedObject)
```

#### Geography.kif:8230

```lisp
(subclass River BodyOfWater)
```

#### CountriesAndRegions.kif:764

```lisp
(instance MississippiRiver River)
```

#### Merge.kif:961

```lisp
(subclass SelfConnectedObject Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2814

```lisp
(subclass Class SetOrClass)
```

#### Merge.kif:2803

```lisp
(subclass SetOrClass Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 41

- Seed: `0`
- Start step: `1350`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### Merge.kif:355

```lisp
(domainSubclass rangeSubclass 2 Class)
```

#### Merge.kif:353

```lisp
(instance rangeSubclass BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6970

```lisp
(subclass BodyOfWater SelfConnectedObject)
```

#### Geography.kif:7057

```lisp
(instance NorthAtlanticOcean BodyOfWater)
```

#### Merge.kif:961

```lisp
(subclass SelfConnectedObject Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2814

```lisp
(subclass Class SetOrClass)
```

#### Merge.kif:2803

```lisp
(subclass SetOrClass Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 42

- Seed: `0`
- Start step: `1350`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `27`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### Merge.kif:355

```lisp
(domainSubclass rangeSubclass 2 Class)
```

#### Merge.kif:353

```lisp
(instance rangeSubclass BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Geography.kif:8230

```lisp
(subclass River BodyOfWater)
```

#### Geography.kif:6970

```lisp
(subclass BodyOfWater SelfConnectedObject)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### CountriesAndRegions.kif:764

```lisp
(instance MississippiRiver River)
```

#### Merge.kif:961

```lisp
(subclass SelfConnectedObject Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2814

```lisp
(subclass Class SetOrClass)
```

#### Merge.kif:2803

```lisp
(subclass SetOrClass Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 43

- Seed: `0`
- Start step: `1374`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `8`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1522

```lisp
(instance AndesMountains MountainRange)
```

#### Geography.kif:3774

```lisp
(=> (attribute ?AREA MountainousTerrain) (exists (?MTN) (and (instance ?MTN Mountain) (part ?MTN ?AREA))))
```

#### Geography.kif:3788

```lisp
(=> (instance ?AREA MountainRange) (attribute ?AREA MountainousTerrain))
```

## Contradiction 44

- Seed: `0`
- Start step: `1380`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `8`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1447

```lisp
(biochemicalAgentDelivery ClostridiumTetani Injecting)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

## Contradiction 45

- Seed: `0`
- Start step: `1380`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `11`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:3118

```lisp
(subclass CaseRole BinaryPredicate)
```

#### Merge.kif:3290

```lisp
(instance result CaseRole)
```

#### Merge.kif:12109

```lisp
(=> (equal (TemporalCompositionFn ?INTERVAL ?INTERVALTYPE) ?CLASS) (forall (?TIME1 ?TIME2) (=> (and (instance ?TIME1 ?INTERVALTYPE) (instance ?TIME2 ?CLASS)) (exists (?DURATION) (and (duration ?TIME1 ?DURATION) (duration ?TIME2 ?DURATION))))))
```

#### Merge.kif:12139

```lisp
(=> (equal (TemporalCompositionFn ?INTERVAL ?INTERVALTYPE) ?CLASS) (exists (?TIME) (and (instance ?TIME ?CLASS) (starts ?TIME ?INTERVAL))))
```

## Contradiction 46

- Seed: `0`
- Start step: `1380`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `42`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:3118

```lisp
(subclass CaseRole BinaryPredicate)
```

#### Merge.kif:3290

```lisp
(instance result CaseRole)
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:83

```lisp
(instance instance BinaryPredicate)
```

#### Merge.kif:85

```lisp
(domain instance 2 Class)
```

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### Merge.kif:135

```lisp
(instance subclass BinaryPredicate)
```

#### Merge.kif:138

```lisp
(domain subclass 2 Class)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1447

```lisp
(biochemicalAgentDelivery ClostridiumTetani Injecting)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

#### Merge.kif:14063

```lisp
(subclass Motion Process)
```

#### Merge.kif:14637

```lisp
(subclass Injecting Inserting)
```

#### Merge.kif:14615

```lisp
(subclass Inserting Putting)
```

#### Merge.kif:14582

```lisp
(subclass Putting Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

## Contradiction 47

- Seed: `0`
- Start step: `1387`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `38`

### Cited source axioms

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:135

```lisp
(instance subclass BinaryPredicate)
```

#### Merge.kif:138

```lisp
(domain subclass 2 Class)
```

#### Merge.kif:376

```lisp
(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
```

#### Merge.kif:137

```lisp
(domain subclass 1 Class)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
```

#### Merge.kif:13076

```lisp
(subclass Breathing AutonomicProcess)
```

#### Merge.kif:12985

```lisp
(subclass AutonomicProcess PhysiologicProcess)
```

#### Merge.kif:12977

```lisp
(subclass PhysiologicProcess BiologicalProcess)
```

#### Merge.kif:12953

```lisp
(subclass BiologicalProcess InternalChange)
```

#### Merge.kif:16162

```lisp
(subclass InternalChange Process)
```

## Contradiction 48

- Seed: `0`
- Start step: `1387`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `40`

### Cited source axioms

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### WMD.kif:757

```lisp
(domainSubclass biochemicalAgentDelivery 2 Process)
```

#### WMD.kif:755

```lisp
(instance biochemicalAgentDelivery BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:135

```lisp
(instance subclass BinaryPredicate)
```

#### Merge.kif:138

```lisp
(domain subclass 2 Class)
```

#### Merge.kif:376

```lisp
(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
```

#### Merge.kif:137

```lisp
(domain subclass 1 Class)
```

## Contradiction 49

- Seed: `0`
- Start step: `1387`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `45`

### Cited source axioms

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### WMD.kif:757

```lisp
(domainSubclass biochemicalAgentDelivery 2 Process)
```

#### WMD.kif:755

```lisp
(instance biochemicalAgentDelivery BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:135

```lisp
(instance subclass BinaryPredicate)
```

#### Merge.kif:138

```lisp
(domain subclass 2 Class)
```

#### Merge.kif:376

```lisp
(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
```

#### Merge.kif:137

```lisp
(domain subclass 1 Class)
```

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3813

```lisp
(range ListOrderFn Entity)
```

## Contradiction 50

- Seed: `0`
- Start step: `1387`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `49`

### Cited source axioms

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### WMD.kif:757

```lisp
(domainSubclass biochemicalAgentDelivery 2 Process)
```

#### WMD.kif:755

```lisp
(instance biochemicalAgentDelivery BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:135

```lisp
(instance subclass BinaryPredicate)
```

#### Merge.kif:138

```lisp
(domain subclass 2 Class)
```

#### Merge.kif:376

```lisp
(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
```

#### Merge.kif:137

```lisp
(domain subclass 1 Class)
```

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:6864

```lisp
(range KappaFn Class)
```

## Contradiction 51

- Seed: `0`
- Start step: `1428`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `5`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

## Contradiction 52

- Seed: `0`
- Start step: `1428`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `17`

### Cited source axioms

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3813

```lisp
(range ListOrderFn Entity)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### Merge.kif:13075

```lisp
(subclass Breathing OrganismProcess)
```

#### Merge.kif:13012

```lisp
(subclass OrganismProcess PhysiologicProcess)
```

#### Merge.kif:12977

```lisp
(subclass PhysiologicProcess BiologicalProcess)
```

#### Merge.kif:12953

```lisp
(subclass BiologicalProcess InternalChange)
```

#### Merge.kif:16162

```lisp
(subclass InternalChange Process)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
```

## Contradiction 53

- Seed: `0`
- Start step: `1452`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `5`

### Cited source axioms

#### WMD.kif:930

```lisp
(=> (and (biologicalAgentCarrier ?AGENT ?SUB) (subclass ?SUB ?ORGANISM)) (biologicalAgentCarrier ?AGENT ?ORGANISM))
```

#### WMD.kif:1560

```lisp
(biologicalAgentCarrier MalarialPlasmodium Mosquito)
```

#### Mid-level-ontology.kif:18056

```lisp
(subclass Mosquito Insect)
```

## Contradiction 54

- Seed: `0`
- Start step: `1456`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `10`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14696

```lisp
(subclass Touching Transfer)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

## Contradiction 55

- Seed: `0`
- Start step: `1456`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `12`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:14696

```lisp
(subclass Touching Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

## Contradiction 56

- Seed: `0`
- Start step: `1456`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `14`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:14063

```lisp
(subclass Motion Process)
```

#### Merge.kif:14696

```lisp
(subclass Touching Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

## Contradiction 57

- Seed: `0`
- Start step: `1456`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `16`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14696

```lisp
(subclass Touching Transfer)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
```

#### Merge.kif:14063

```lisp
(subclass Motion Process)
```

## Contradiction 58

- Seed: `0`
- Start step: `1456`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `18`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:14696

```lisp
(subclass Touching Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:14063

```lisp
(subclass Motion Process)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
```

## Contradiction 59

- Seed: `0`
- Start step: `1456`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3813

```lisp
(range ListOrderFn Entity)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:14696

```lisp
(subclass Touching Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

#### Merge.kif:14063

```lisp
(subclass Motion Process)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
```

## Contradiction 60

- Seed: `0`
- Start step: `1456`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:259

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### WMD.kif:757

```lisp
(domainSubclass biochemicalAgentDelivery 2 Process)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:14063

```lisp
(subclass Motion Process)
```

#### Merge.kif:14696

```lisp
(subclass Touching Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

## Contradiction 61

- Seed: `0`
- Start step: `1456`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Merge.kif:259

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Mid-level-ontology.kif:33371

```lisp
(domainSubclass typicalPart 2 Physical)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14696

```lisp
(subclass Touching Transfer)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
```

#### Merge.kif:14063

```lisp
(subclass Motion Process)
```

## Contradiction 62

- Seed: `0`
- Start step: `1456`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:259

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### capabilities.kif:140

```lisp
(domainSubclass requiredRole 1 Process)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:14063

```lisp
(subclass Motion Process)
```

#### Merge.kif:14696

```lisp
(subclass Touching Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

## Contradiction 63

- Seed: `0`
- Start step: `1456`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Merge.kif:259

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Mid-level-ontology.kif:33370

```lisp
(domainSubclass typicalPart 1 Physical)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14696

```lisp
(subclass Touching Transfer)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
```

#### Merge.kif:14063

```lisp
(subclass Motion Process)
```

## Contradiction 64

- Seed: `0`
- Start step: `1456`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:259

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:4851

```lisp
(domainSubclass capability 1 Process)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:14063

```lisp
(subclass Motion Process)
```

#### Merge.kif:14696

```lisp
(subclass Touching Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

## Contradiction 65

- Seed: `0`
- Start step: `1456`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:259

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### capabilities.kif:142

```lisp
(domainSubclass requiredRole 3 Entity)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:14696

```lisp
(subclass Touching Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

#### Merge.kif:14063

```lisp
(subclass Motion Process)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
```

## Contradiction 66

- Seed: `0`
- Start step: `1456`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:259

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### WMD.kif:891

```lisp
(domainSubclass diseaseMedicine 3 Process)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:14063

```lisp
(subclass Motion Process)
```

#### Merge.kif:14696

```lisp
(subclass Touching Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

## Contradiction 67

- Seed: `0`
- Start step: `1488`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `7`

### Cited source axioms

#### ComputerInput.kif:280

```lisp
(=> (instance ?KEYBOARD ComputerKeyboard_Generic) (exists (?KEY) (and (instance ?KEY ComputerKeyboardKey) (component ?KEY ?KEYBOARD))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### ComputerInput.kif:265

```lisp
(typicalPart ComputerKeyboardKey ComputerKeyboard_Generic)
```

## Contradiction 68

- Seed: `0`
- Start step: `1488`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `16`

### Cited source axioms

#### ComputerInput.kif:280

```lisp
(=> (instance ?KEYBOARD ComputerKeyboard_Generic) (exists (?KEY) (and (instance ?KEY ComputerKeyboardKey) (component ?KEY ?KEYBOARD))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### Merge.kif:201

```lisp
(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))
```

#### Mid-level-ontology.kif:33526

```lisp
(subrelation partTypes typicalPart)
```

#### ComputerInput.kif:392

```lisp
(partTypes ComputerKeyboard ComputerKeyboardKey)
```

#### Mid-level-ontology.kif:33523

```lisp
(instance partTypes BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Mid-level-ontology.kif:33359

```lisp
(instance typicalPart BinaryPredicate)
```

#### ComputerInput.kif:387

```lisp
(subclass ComputerKeyboard ComputerKeyboard_Generic)
```

## Contradiction 69

- Seed: `0`
- Start step: `1488`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `14`

### Cited source axioms

#### ComputerInput.kif:280

```lisp
(=> (instance ?KEYBOARD ComputerKeyboard_Generic) (exists (?KEY) (and (instance ?KEY ComputerKeyboardKey) (component ?KEY ?KEYBOARD))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### ComputerInput.kif:387

```lisp
(subclass ComputerKeyboard ComputerKeyboard_Generic)
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### Mid-level-ontology.kif:33526

```lisp
(subrelation partTypes typicalPart)
```

#### ComputerInput.kif:392

```lisp
(partTypes ComputerKeyboard ComputerKeyboardKey)
```

## Contradiction 70

- Seed: `0`
- Start step: `1492`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `12`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### WMD.kif:757

```lisp
(domainSubclass biochemicalAgentDelivery 2 Process)
```

#### WMD.kif:755

```lisp
(instance biochemicalAgentDelivery BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### WMD.kif:178

```lisp
(biochemicalAgentDelivery BacterialAgent Touching)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

## Contradiction 71

- Seed: `0`
- Start step: `1493`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `15`

### Cited source axioms

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Cars.kif:251

```lisp
(subclass Crankshaft Shaft)
```

#### engineering.kif:868

```lisp
(subclass Shaft EngineeringComponent)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Mid-level-ontology.kif:33422

```lisp
(=> (typicallyContainsPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### Cars.kif:254

```lisp
(typicallyContainsPart Crankshaft IntermittentCombustionEngine)
```

## Contradiction 72

- Seed: `0`
- Start step: `1493`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `15`

### Cited source axioms

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Cars.kif:251

```lisp
(subclass Crankshaft Shaft)
```

#### engineering.kif:868

```lisp
(subclass Shaft EngineeringComponent)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### Cars.kif:253

```lisp
(typicalPart Crankshaft IntermittentCombustionEngine)
```

## Contradiction 73

- Seed: `0`
- Start step: `1493`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `13`

### Cited source axioms

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### engineering.kif:868

```lisp
(subclass Shaft EngineeringComponent)
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### Cars.kif:253

```lisp
(typicalPart Crankshaft IntermittentCombustionEngine)
```

#### Cars.kif:251

```lisp
(subclass Crankshaft Shaft)
```

## Contradiction 74

- Seed: `0`
- Start step: `1493`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `13`

### Cited source axioms

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### engineering.kif:868

```lisp
(subclass Shaft EngineeringComponent)
```

#### Mid-level-ontology.kif:33422

```lisp
(=> (typicallyContainsPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### Cars.kif:254

```lisp
(typicallyContainsPart Crankshaft IntermittentCombustionEngine)
```

#### Cars.kif:251

```lisp
(subclass Crankshaft Shaft)
```

## Contradiction 75

- Seed: `0`
- Start step: `1522`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `13`

### Cited source axioms

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### Mid-level-ontology.kif:33526

```lisp
(subrelation partTypes typicalPart)
```

#### engineering.kif:1182

```lisp
(partTypes Valve Tube)
```

#### engineering.kif:1163

```lisp
(subclass Valve EngineeringComponent)
```

## Contradiction 76

- Seed: `0`
- Start step: `1541`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `5`

### Cited source axioms

#### WMD.kif:749

```lisp
(=> (and (biochemicalAgentSyndrome ?AGENT ?SYNDROME) (diseaseSymptom ?SYNDROME ?SYMPTOM)) (biochemicalAgentSyndrome ?AGENT ?SYMPTOM))
```

#### WMD.kif:1877

```lisp
(biochemicalAgentSyndrome CrimeanCongoHemorrhagicFeverVirus CrimeanCongoHemorrhagicFever)
```

#### WMD.kif:1871

```lisp
(diseaseSymptom CrimeanCongoHemorrhagicFever Fever)
```

## Contradiction 77

- Seed: `0`
- Start step: `1541`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `5`

### Cited source axioms

#### WMD.kif:930

```lisp
(=> (and (biologicalAgentCarrier ?AGENT ?SUB) (subclass ?SUB ?ORGANISM)) (biologicalAgentCarrier ?AGENT ?ORGANISM))
```

#### WMD.kif:1876

```lisp
(biologicalAgentCarrier CrimeanCongoHemorrhagicFeverVirus Arachnid)
```

#### Merge.kif:18776

```lisp
(subclass Arachnid Arthropod)
```

## Contradiction 78

- Seed: `0`
- Start step: `1541`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `5`

### Cited source axioms

#### WMD.kif:930

```lisp
(=> (and (biologicalAgentCarrier ?AGENT ?SUB) (subclass ?SUB ?ORGANISM)) (biologicalAgentCarrier ?AGENT ?ORGANISM))
```

#### WMD.kif:1162

```lisp
(biologicalAgentCarrier FrancisellaTularensis Rodent)
```

#### Merge.kif:18906

```lisp
(subclass Rodent Mammal)
```

## Contradiction 79

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `50`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

## Contradiction 80

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `57`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### CountriesAndRegions.kif:25

```lisp
(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))
```

#### Merge.kif:5075

```lisp
(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

## Contradiction 81

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `58`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### CountriesAndRegions.kif:25

```lisp
(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))
```

#### Merge.kif:5075

```lisp
(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

## Contradiction 82

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `86`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

## Contradiction 83

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `60`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:5075

```lisp
(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Geography.kif:3149

```lisp
(=> (climateTypeInArea ?AREA ?CLASS) (exists (?REGION ?TYPE) (and (instance ?REGION GeographicArea) (instance ?TYPE ?CLASS) (attribute ?REGION ?TYPE) (part ?REGION ?AREA))))
```

#### Geography.kif:516

```lisp
(climateTypeInArea GreatBasin AridClimateZone)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

## Contradiction 84

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `105`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:2947

```lisp
(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))
```

#### Merge.kif:12338

```lisp
(instance meetsSpatially IrreflexiveRelation)
```

## Contradiction 85

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `58`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### Merge.kif:2947

```lisp
(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))
```

#### Merge.kif:12338

```lisp
(instance meetsSpatially IrreflexiveRelation)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

## Contradiction 86

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `118`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

#### CountriesAndRegions.kif:25

```lisp
(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))
```

#### Merge.kif:5075

```lisp
(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

## Contradiction 87

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `109`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Geography.kif:5692

```lisp
(geographicSubregion NorthAmerica NorthernHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

## Contradiction 88

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `109`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Geography.kif:5693

```lisp
(geographicSubregion NorthAmerica WesternHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

## Contradiction 89

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `120`

### Cited source axioms

#### Geography.kif:8040

```lisp
(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Geography.kif:2311

```lisp
(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:2947

```lisp
(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))
```

#### Merge.kif:12338

```lisp
(instance meetsSpatially IrreflexiveRelation)
```

#### CountriesAndRegions.kif:3215

```lisp
(geographicSubregion LosAngelesCalifornia UnitedStates)
```

#### CountriesAndRegions.kif:35

```lisp
(subclass AmericanCity City)
```

#### Merge.kif:18386

```lisp
(subclass City GeopoliticalArea)
```

## Contradiction 90

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `125`

### Cited source axioms

#### Geography.kif:8040

```lisp
(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Geography.kif:2311

```lisp
(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:2947

```lisp
(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))
```

#### Merge.kif:12338

```lisp
(instance meetsSpatially IrreflexiveRelation)
```

#### CountriesAndRegions.kif:3215

```lisp
(geographicSubregion LosAngelesCalifornia UnitedStates)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### CountriesAndRegions.kif:35

```lisp
(subclass AmericanCity City)
```

#### Merge.kif:18386

```lisp
(subclass City GeopoliticalArea)
```

## Contradiction 91

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `128`

### Cited source axioms

#### Geography.kif:8040

```lisp
(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Geography.kif:2311

```lisp
(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:2947

```lisp
(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))
```

#### Merge.kif:12338

```lisp
(instance meetsSpatially IrreflexiveRelation)
```

#### CountriesAndRegions.kif:35

```lisp
(subclass AmericanCity City)
```

#### Merge.kif:18386

```lisp
(subclass City GeopoliticalArea)
```

#### CountriesAndRegions.kif:3215

```lisp
(geographicSubregion LosAngelesCalifornia UnitedStates)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Geography.kif:5693

```lisp
(geographicSubregion NorthAmerica WesternHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

## Contradiction 92

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `128`

### Cited source axioms

#### Geography.kif:8040

```lisp
(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Geography.kif:2311

```lisp
(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:2947

```lisp
(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))
```

#### Merge.kif:12338

```lisp
(instance meetsSpatially IrreflexiveRelation)
```

#### CountriesAndRegions.kif:35

```lisp
(subclass AmericanCity City)
```

#### Merge.kif:18386

```lisp
(subclass City GeopoliticalArea)
```

#### CountriesAndRegions.kif:3215

```lisp
(geographicSubregion LosAngelesCalifornia UnitedStates)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Geography.kif:5692

```lisp
(geographicSubregion NorthAmerica NorthernHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

## Contradiction 93

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `53`

### Cited source axioms

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:1074

```lisp
(meetsSpatially Nevada California)
```

#### Merge.kif:12339

```lisp
(instance meetsSpatially SymmetricRelation)
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

## Contradiction 94

- Seed: `0`
- Start step: `1559`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `149`

### Cited source axioms

#### Geography.kif:8040

```lisp
(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))
```

#### Merge.kif:12321

```lisp
(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Geography.kif:2311

```lisp
(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Geography.kif:2546

```lisp
(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))
```

#### CountriesAndRegions.kif:986

```lisp
(meetsSpatially Idaho Nevada)
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:982

```lisp
(instance Idaho AmericanState)
```

#### CountriesAndRegions.kif:21

```lisp
(subclass AmericanState StateOrProvince)
```

#### Merge.kif:18369

```lisp
(subclass StateOrProvince GeopoliticalArea)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:509

```lisp
(geographicSubregion GreatBasin Nevada)
```

#### Geography.kif:503

```lisp
(instance GreatBasin EndorheicBasin)
```

#### Geography.kif:486

```lisp
(subclass EndorheicBasin Basin)
```

#### Geography.kif:6711

```lisp
(subclass Basin LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:513

```lisp
(geographicSubregion GreatBasin Idaho)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### CountriesAndRegions.kif:1073

```lisp
(meetsSpatially Nevada Oregon)
```

#### CountriesAndRegions.kif:1072

```lisp
(instance Nevada AmericanState)
```

#### Geography.kif:511

```lisp
(geographicSubregion GreatBasin Oregon)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:947

```lisp
(meetsSpatially California Mexico)
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:515

```lisp
(geographicSubregion GreatBasin Mexico)
```

#### Geography.kif:512

```lisp
(geographicSubregion GreatBasin California)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

#### Merge.kif:12314

```lisp
(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))
```

#### Merge.kif:12328

```lisp
(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:2947

```lisp
(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))
```

#### Merge.kif:12338

```lisp
(instance meetsSpatially IrreflexiveRelation)
```

#### CountriesAndRegions.kif:86

```lisp
(=> (instance ?N EuropeanNation) (part ?N Europe))
```

#### CountriesAndRegions.kif:377

```lisp
(instance UnitedKingdom EuropeanNation)
```

#### Merge.kif:5075

```lisp
(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Geography.kif:5723

```lisp
(geographicSubregion Europe NorthernHemisphere)
```

#### CountriesAndRegions.kif:83

```lisp
(subclass EuropeanNation Nation)
```

#### Merge.kif:18359

```lisp
(subclass Nation GeopoliticalArea)
```

#### CountriesAndRegions.kif:35

```lisp
(subclass AmericanCity City)
```

#### Merge.kif:18386

```lisp
(subclass City GeopoliticalArea)
```

#### CountriesAndRegions.kif:3215

```lisp
(geographicSubregion LosAngelesCalifornia UnitedStates)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Geography.kif:5692

```lisp
(geographicSubregion NorthAmerica NorthernHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

## Contradiction 95

- Seed: `0`
- Start step: `1570`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `10`

### Cited source axioms

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### Mid-level-ontology.kif:1819

```lisp
(typicalPart GunChamber GunBarrel)
```

#### Mid-level-ontology.kif:1777

```lisp
(subclass GunBarrel EngineeringComponent)
```

## Contradiction 96

- Seed: `0`
- Start step: `1570`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `16`

### Cited source axioms

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### Merge.kif:201

```lisp
(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))
```

#### Mid-level-ontology.kif:33526

```lisp
(subrelation partTypes typicalPart)
```

#### Mid-level-ontology.kif:1891

```lisp
(partTypes GunBore GunBarrel)
```

#### Mid-level-ontology.kif:33523

```lisp
(instance partTypes BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Mid-level-ontology.kif:33359

```lisp
(instance typicalPart BinaryPredicate)
```

#### Mid-level-ontology.kif:1777

```lisp
(subclass GunBarrel EngineeringComponent)
```

## Contradiction 97

- Seed: `0`
- Start step: `1570`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `13`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Mid-level-ontology.kif:1777

```lisp
(subclass GunBarrel EngineeringComponent)
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### Mid-level-ontology.kif:33526

```lisp
(subrelation partTypes typicalPart)
```

#### Mid-level-ontology.kif:1891

```lisp
(partTypes GunBore GunBarrel)
```

## Contradiction 98

- Seed: `0`
- Start step: `1570`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Mid-level-ontology.kif:1777

```lisp
(subclass GunBarrel EngineeringComponent)
```

#### Mid-level-ontology.kif:33534

```lisp
(=> (and (partTypes ?PARTTYPE ?WHOLETYPE) (instance ?PART ?PARTTYPE)) (exists (?WHOLE) (and (instance ?WHOLE ?WHOLETYPE) (part ?PART ?WHOLE))))
```

#### Mid-level-ontology.kif:1891

```lisp
(partTypes GunBore GunBarrel)
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### Merge.kif:201

```lisp
(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))
```

#### Mid-level-ontology.kif:33526

```lisp
(subrelation partTypes typicalPart)
```

#### Mid-level-ontology.kif:33523

```lisp
(instance partTypes BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Mid-level-ontology.kif:33359

```lisp
(instance typicalPart BinaryPredicate)
```

## Contradiction 99

- Seed: `0`
- Start step: `1570`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `16`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Mid-level-ontology.kif:1777

```lisp
(subclass GunBarrel EngineeringComponent)
```

#### Mid-level-ontology.kif:33534

```lisp
(=> (and (partTypes ?PARTTYPE ?WHOLETYPE) (instance ?PART ?PARTTYPE)) (exists (?WHOLE) (and (instance ?WHOLE ?WHOLETYPE) (part ?PART ?WHOLE))))
```

#### Mid-level-ontology.kif:1891

```lisp
(partTypes GunBore GunBarrel)
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### Mid-level-ontology.kif:33526

```lisp
(subrelation partTypes typicalPart)
```

## Contradiction 100

- Seed: `0`
- Start step: `1575`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `40`

### Cited source axioms

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:135

```lisp
(instance subclass BinaryPredicate)
```

#### Merge.kif:138

```lisp
(domain subclass 2 Class)
```

#### Merge.kif:376

```lisp
(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Food.kif:4672

```lisp
(rangeSubclass PlantFn Plant)
```

#### Merge.kif:137

```lisp
(domain subclass 1 Class)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:16162

```lisp
(subclass InternalChange Process)
```

#### Merge.kif:12953

```lisp
(subclass BiologicalProcess InternalChange)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
```

#### Merge.kif:13075

```lisp
(subclass Breathing OrganismProcess)
```

#### Merge.kif:13012

```lisp
(subclass OrganismProcess PhysiologicProcess)
```

#### Merge.kif:12977

```lisp
(subclass PhysiologicProcess BiologicalProcess)
```

## Contradiction 101

- Seed: `0`
- Start step: `1575`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `42`

### Cited source axioms

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:135

```lisp
(instance subclass BinaryPredicate)
```

#### Merge.kif:138

```lisp
(domain subclass 2 Class)
```

#### Merge.kif:376

```lisp
(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Food.kif:4672

```lisp
(rangeSubclass PlantFn Plant)
```

#### Merge.kif:137

```lisp
(domain subclass 1 Class)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:13076

```lisp
(subclass Breathing AutonomicProcess)
```

#### Merge.kif:16162

```lisp
(subclass InternalChange Process)
```

#### Merge.kif:12953

```lisp
(subclass BiologicalProcess InternalChange)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
```

#### Merge.kif:12985

```lisp
(subclass AutonomicProcess PhysiologicProcess)
```

#### Merge.kif:12977

```lisp
(subclass PhysiologicProcess BiologicalProcess)
```

## Contradiction 102

- Seed: `0`
- Start step: `1575`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `40`

### Cited source axioms

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### WMD.kif:757

```lisp
(domainSubclass biochemicalAgentDelivery 2 Process)
```

#### WMD.kif:755

```lisp
(instance biochemicalAgentDelivery BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:135

```lisp
(instance subclass BinaryPredicate)
```

#### Merge.kif:138

```lisp
(domain subclass 2 Class)
```

#### Merge.kif:376

```lisp
(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Food.kif:4672

```lisp
(rangeSubclass PlantFn Plant)
```

#### Merge.kif:137

```lisp
(domain subclass 1 Class)
```

## Contradiction 103

- Seed: `0`
- Start step: `1575`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `45`

### Cited source axioms

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### WMD.kif:757

```lisp
(domainSubclass biochemicalAgentDelivery 2 Process)
```

#### WMD.kif:755

```lisp
(instance biochemicalAgentDelivery BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:135

```lisp
(instance subclass BinaryPredicate)
```

#### Merge.kif:138

```lisp
(domain subclass 2 Class)
```

#### Merge.kif:376

```lisp
(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Food.kif:4672

```lisp
(rangeSubclass PlantFn Plant)
```

#### Merge.kif:137

```lisp
(domain subclass 1 Class)
```

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3813

```lisp
(range ListOrderFn Entity)
```

## Contradiction 104

- Seed: `0`
- Start step: `1575`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `49`

### Cited source axioms

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### WMD.kif:757

```lisp
(domainSubclass biochemicalAgentDelivery 2 Process)
```

#### WMD.kif:755

```lisp
(instance biochemicalAgentDelivery BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:135

```lisp
(instance subclass BinaryPredicate)
```

#### Merge.kif:138

```lisp
(domain subclass 2 Class)
```

#### Merge.kif:376

```lisp
(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Food.kif:4672

```lisp
(rangeSubclass PlantFn Plant)
```

#### Merge.kif:137

```lisp
(domain subclass 1 Class)
```

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:6864

```lisp
(range KappaFn Class)
```

## Contradiction 105

- Seed: `0`
- Start step: `1577`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `5`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:366

```lisp
(biochemicalAgentDelivery BurkholderiaPseudomallei Ingesting)
```

#### Merge.kif:13109

```lisp
(subclass Ingesting Transfer)
```

## Contradiction 106

- Seed: `0`
- Start step: `1577`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `14`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### WMD.kif:365

```lisp
(biochemicalAgentDelivery BurkholderiaPseudomallei Breathing)
```

#### WMD.kif:757

```lisp
(domainSubclass biochemicalAgentDelivery 2 Process)
```

#### WMD.kif:755

```lisp
(instance biochemicalAgentDelivery BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

## Contradiction 107

- Seed: `0`
- Start step: `1577`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `15`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### WMD.kif:757

```lisp
(domainSubclass biochemicalAgentDelivery 2 Process)
```

#### WMD.kif:755

```lisp
(instance biochemicalAgentDelivery BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:365

```lisp
(biochemicalAgentDelivery BurkholderiaPseudomallei Breathing)
```

## Contradiction 108

- Seed: `0`
- Start step: `1577`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `14`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### WMD.kif:757

```lisp
(domainSubclass biochemicalAgentDelivery 2 Process)
```

#### WMD.kif:755

```lisp
(instance biochemicalAgentDelivery BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### WMD.kif:364

```lisp
(biochemicalAgentDelivery BurkholderiaPseudomallei Injecting)
```

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

## Contradiction 109

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `29`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:343

```lisp
(instance RockyMountains MountainRange)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:201

```lisp
(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:176

```lisp
(instance subrelation PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Merge.kif:18142

```lisp
(instance geographicSubregion BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:5030

```lisp
(instance partlyLocated BinaryPredicate)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

## Contradiction 110

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `33`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:343

```lisp
(instance RockyMountains MountainRange)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Merge.kif:201

```lisp
(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:176

```lisp
(instance subrelation PartialOrderingRelation)
```

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Merge.kif:18142

```lisp
(instance geographicSubregion BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:5030

```lisp
(instance partlyLocated BinaryPredicate)
```

#### Geography.kif:5693

```lisp
(geographicSubregion NorthAmerica WesternHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

## Contradiction 111

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `33`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:343

```lisp
(instance RockyMountains MountainRange)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Merge.kif:201

```lisp
(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:176

```lisp
(instance subrelation PartialOrderingRelation)
```

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Merge.kif:18142

```lisp
(instance geographicSubregion BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:5030

```lisp
(instance partlyLocated BinaryPredicate)
```

#### Geography.kif:5692

```lisp
(geographicSubregion NorthAmerica NorthernHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

## Contradiction 112

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `32`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:343

```lisp
(instance RockyMountains MountainRange)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Merge.kif:201

```lisp
(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:176

```lisp
(instance subrelation PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Merge.kif:18142

```lisp
(instance geographicSubregion BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:5030

```lisp
(instance partlyLocated BinaryPredicate)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

## Contradiction 113

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `35`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:343

```lisp
(instance RockyMountains MountainRange)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Merge.kif:201

```lisp
(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:176

```lisp
(instance subrelation PartialOrderingRelation)
```

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Merge.kif:18142

```lisp
(instance geographicSubregion BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:5030

```lisp
(instance partlyLocated BinaryPredicate)
```

#### Geography.kif:5693

```lisp
(geographicSubregion NorthAmerica WesternHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

## Contradiction 114

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `36`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:343

```lisp
(instance RockyMountains MountainRange)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Merge.kif:201

```lisp
(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:176

```lisp
(instance subrelation PartialOrderingRelation)
```

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Merge.kif:18142

```lisp
(instance geographicSubregion BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:5030

```lisp
(instance partlyLocated BinaryPredicate)
```

#### Geography.kif:5692

```lisp
(geographicSubregion NorthAmerica NorthernHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

## Contradiction 115

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `33`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:343

```lisp
(instance RockyMountains MountainRange)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:201

```lisp
(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:176

```lisp
(instance subrelation PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Merge.kif:18142

```lisp
(instance geographicSubregion BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:5030

```lisp
(instance partlyLocated BinaryPredicate)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

## Contradiction 116

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `26`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1522

```lisp
(instance AndesMountains MountainRange)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:1529

```lisp
(geographicSubregion AndesMountains SouthAmerica)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

## Contradiction 117

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `29`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1522

```lisp
(instance AndesMountains MountainRange)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:5708

```lisp
(geographicSubregion SouthAmerica WesternHemisphere)
```

#### Geography.kif:1529

```lisp
(geographicSubregion AndesMountains SouthAmerica)
```

#### Merge.kif:18143

```lisp
(instance geographicSubregion TransitiveRelation)
```

## Contradiction 118

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `28`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1522

```lisp
(instance AndesMountains MountainRange)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:1529

```lisp
(geographicSubregion AndesMountains SouthAmerica)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

## Contradiction 119

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `31`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1522

```lisp
(instance AndesMountains MountainRange)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:5708

```lisp
(geographicSubregion SouthAmerica WesternHemisphere)
```

#### Geography.kif:1529

```lisp
(geographicSubregion AndesMountains SouthAmerica)
```

#### Merge.kif:18143

```lisp
(instance geographicSubregion TransitiveRelation)
```

## Contradiction 120

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `30`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1522

```lisp
(instance AndesMountains MountainRange)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:1529

```lisp
(geographicSubregion AndesMountains SouthAmerica)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

## Contradiction 121

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `26`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:443

```lisp
(instance CaliforniaCoastRanges MountainRange)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:452

```lisp
(geographicSubregion CaliforniaCoastRanges California)
```

## Contradiction 122

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `29`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:443

```lisp
(instance CaliforniaCoastRanges MountainRange)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:452

```lisp
(geographicSubregion CaliforniaCoastRanges California)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

## Contradiction 123

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `30`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:443

```lisp
(instance CaliforniaCoastRanges MountainRange)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:452

```lisp
(geographicSubregion CaliforniaCoastRanges California)
```

## Contradiction 124

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `9`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:443

```lisp
(instance CaliforniaCoastRanges MountainRange)
```

#### Geography.kif:3774

```lisp
(=> (attribute ?AREA MountainousTerrain) (exists (?MTN) (and (instance ?MTN Mountain) (part ?MTN ?AREA))))
```

#### Geography.kif:3788

```lisp
(=> (instance ?AREA MountainRange) (attribute ?AREA MountainousTerrain))
```

## Contradiction 125

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `36`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:343

```lisp
(instance RockyMountains MountainRange)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Merge.kif:201

```lisp
(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:176

```lisp
(instance subrelation PartialOrderingRelation)
```

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Merge.kif:18142

```lisp
(instance geographicSubregion BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:5030

```lisp
(instance partlyLocated BinaryPredicate)
```

#### Geography.kif:5693

```lisp
(geographicSubregion NorthAmerica WesternHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

## Contradiction 126

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `29`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1522

```lisp
(instance AndesMountains MountainRange)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:1529

```lisp
(geographicSubregion AndesMountains SouthAmerica)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

## Contradiction 127

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `32`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1522

```lisp
(instance AndesMountains MountainRange)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:5708

```lisp
(geographicSubregion SouthAmerica WesternHemisphere)
```

#### Geography.kif:1529

```lisp
(geographicSubregion AndesMountains SouthAmerica)
```

#### Merge.kif:18143

```lisp
(instance geographicSubregion TransitiveRelation)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

## Contradiction 128

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `26`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:343

```lisp
(instance RockyMountains MountainRange)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

## Contradiction 129

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `29`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:343

```lisp
(instance RockyMountains MountainRange)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Geography.kif:5692

```lisp
(geographicSubregion NorthAmerica NorthernHemisphere)
```

#### Merge.kif:18143

```lisp
(instance geographicSubregion TransitiveRelation)
```

## Contradiction 130

- Seed: `0`
- Start step: `1601`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `29`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:343

```lisp
(instance RockyMountains MountainRange)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Geography.kif:5693

```lisp
(geographicSubregion NorthAmerica WesternHemisphere)
```

#### Merge.kif:18143

```lisp
(instance geographicSubregion TransitiveRelation)
```

## Contradiction 131

- Seed: `0`
- Start step: `1636`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `15`

### Cited source axioms

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Mid-level-ontology.kif:4558

```lisp
(subclass CommunicationDevice EngineeringComponent)
```

#### Mid-level-ontology.kif:4571

```lisp
(subclass Telephone CommunicationDevice)
```

#### Mid-level-ontology.kif:35137

```lisp
(subclass MobileCellPhone Telephone)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

## Contradiction 132

- Seed: `0`
- Start step: `1636`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `17`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Communications.kif:31

```lisp
(=> (instance ?SYSTEM TelephoneSystem) (exists (?PHONE) (and (instance ?PHONE Telephone) (engineeringSubcomponent ?PHONE ?SYSTEM))))
```

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Mid-level-ontology.kif:4571

```lisp
(subclass Telephone CommunicationDevice)
```

#### Mid-level-ontology.kif:4558

```lisp
(subclass CommunicationDevice EngineeringComponent)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Cellular&TelephoneArchitecture.kif:1137

```lisp
(subclass PublicSwitchedTelephoneNetwork TelephoneSystem)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

## Contradiction 133

- Seed: `0`
- Start step: `1636`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `15`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Communications.kif:31

```lisp
(=> (instance ?SYSTEM TelephoneSystem) (exists (?PHONE) (and (instance ?PHONE Telephone) (engineeringSubcomponent ?PHONE ?SYSTEM))))
```

#### Cellular&TelephoneArchitecture.kif:1137

```lisp
(subclass PublicSwitchedTelephoneNetwork TelephoneSystem)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:20794

```lisp
(domain engineeringSubcomponent 2 EngineeringComponent)
```

#### Merge.kif:20792

```lisp
(instance engineeringSubcomponent BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

## Contradiction 134

- Seed: `0`
- Start step: `1636`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `27`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Cellular&TelephoneArchitecture.kif:1137

```lisp
(subclass PublicSwitchedTelephoneNetwork TelephoneSystem)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Communications.kif:26

```lisp
(subclass TelephoneSystem CommunicationSystem)
```

#### Mid-level-ontology.kif:11288

```lisp
(subclass CommunicationSystem CollectionOfObjects)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Mid-level-ontology.kif:32155

```lisp
(=> (instance ?COLL CollectionOfObjects) (memberType ?COLL Object))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Mid-level-ontology.kif:32145

```lisp
(instance memberType BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Mid-level-ontology.kif:32146

```lisp
(domain memberType 1 Collection)
```

#### Merge.kif:83

```lisp
(instance instance BinaryPredicate)
```

#### Merge.kif:4214

```lisp
(subclass Predicate Relation)
```

#### Merge.kif:2843

```lisp
(subclass Relation Abstract)
```

#### Merge.kif:1545

```lisp
(subclass Collection Physical)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 135

- Seed: `0`
- Start step: `1636`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `28`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Cellular&TelephoneArchitecture.kif:1137

```lisp
(subclass PublicSwitchedTelephoneNetwork TelephoneSystem)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Communications.kif:26

```lisp
(subclass TelephoneSystem CommunicationSystem)
```

#### Mid-level-ontology.kif:11288

```lisp
(subclass CommunicationSystem CollectionOfObjects)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Mid-level-ontology.kif:32155

```lisp
(=> (instance ?COLL CollectionOfObjects) (memberType ?COLL Object))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Mid-level-ontology.kif:32145

```lisp
(instance memberType BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Mid-level-ontology.kif:32146

```lisp
(domain memberType 1 Collection)
```

#### Merge.kif:768

```lisp
(instance subAttribute PartialOrderingRelation)
```

#### Merge.kif:3077

```lisp
(subclass PartialOrderingRelation TotalValuedRelation)
```

#### Merge.kif:2884

```lisp
(subclass TotalValuedRelation Relation)
```

#### Merge.kif:2843

```lisp
(subclass Relation Abstract)
```

#### Merge.kif:1545

```lisp
(subclass Collection Physical)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 136

- Seed: `0`
- Start step: `1644`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `15`

### Cited source axioms

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Mid-level-ontology.kif:4558

```lisp
(subclass CommunicationDevice EngineeringComponent)
```

#### Mid-level-ontology.kif:3017

```lisp
(subclass ReceiverDevice CommunicationDevice)
```

#### Mid-level-ontology.kif:35136

```lisp
(subclass MobileCellPhone ReceiverDevice)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

## Contradiction 137

- Seed: `0`
- Start step: `1644`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `13`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Mid-level-ontology.kif:35136

```lisp
(subclass MobileCellPhone ReceiverDevice)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Mid-level-ontology.kif:3017

```lisp
(subclass ReceiverDevice CommunicationDevice)
```

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Mid-level-ontology.kif:4558

```lisp
(subclass CommunicationDevice EngineeringComponent)
```

## Contradiction 138

- Seed: `0`
- Start step: `1674`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `5`

### Cited source axioms

#### WMD.kif:930

```lisp
(=> (and (biologicalAgentCarrier ?AGENT ?SUB) (subclass ?SUB ?ORGANISM)) (biologicalAgentCarrier ?AGENT ?ORGANISM))
```

#### WMD.kif:264

```lisp
(biologicalAgentCarrier BacillusAnthracis HoofedMammal)
```

#### Merge.kif:18876

```lisp
(subclass HoofedMammal Mammal)
```

## Contradiction 139

- Seed: `0`
- Start step: `1684`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `18`

### Cited source axioms

#### Merge.kif:209

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (instance ?PRED2 ?CLASS) (subclass ?CLASS InheritableRelation)) (instance ?PRED1 ?CLASS))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Media.kif:3041

```lisp
(subrelation keyName subString)
```

#### Mid-level-ontology.kif:34327

```lisp
(subrelation subString part)
```

#### Merge.kif:176

```lisp
(instance subrelation PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:1047

```lisp
(instance part PartialOrderingRelation)
```

#### Merge.kif:3075

```lisp
(subclass PartialOrderingRelation AntisymmetricRelation)
```

#### Merge.kif:2919

```lisp
(subclass BinaryRelation InheritableRelation)
```

#### Merge.kif:2990

```lisp
(subclass AntisymmetricRelation BinaryRelation)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Media.kif:3038

```lisp
(instance keyName PartialValuedRelation)
```

#### Merge.kif:3077

```lisp
(subclass PartialOrderingRelation TotalValuedRelation)
```

#### Merge.kif:2852

```lisp
(disjoint TotalValuedRelation PartialValuedRelation)
```

## Contradiction 140

- Seed: `0`
- Start step: `1684`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `17`

### Cited source axioms

#### Merge.kif:209

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (instance ?PRED2 ?CLASS) (subclass ?CLASS InheritableRelation)) (instance ?PRED1 ?CLASS))
```

#### Mid-level-ontology.kif:34327

```lisp
(subrelation subString part)
```

#### Merge.kif:1047

```lisp
(instance part PartialOrderingRelation)
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:3075

```lisp
(subclass PartialOrderingRelation AntisymmetricRelation)
```

#### Merge.kif:2919

```lisp
(subclass BinaryRelation InheritableRelation)
```

#### Merge.kif:2990

```lisp
(subclass AntisymmetricRelation BinaryRelation)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Media.kif:3041

```lisp
(subrelation keyName subString)
```

#### Media.kif:3038

```lisp
(instance keyName PartialValuedRelation)
```

#### Merge.kif:3077

```lisp
(subclass PartialOrderingRelation TotalValuedRelation)
```

#### Merge.kif:2852

```lisp
(disjoint TotalValuedRelation PartialValuedRelation)
```

## Contradiction 141

- Seed: `0`
- Start step: `1776`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### Merge.kif:355

```lisp
(domainSubclass rangeSubclass 2 Class)
```

#### Merge.kif:353

```lisp
(instance rangeSubclass BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6970

```lisp
(subclass BodyOfWater SelfConnectedObject)
```

#### Geography.kif:7032

```lisp
(subclass Ocean BodyOfWater)
```

#### Geography.kif:7049

```lisp
(instance AtlanticOcean Ocean)
```

#### Merge.kif:961

```lisp
(subclass SelfConnectedObject Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2814

```lisp
(subclass Class SetOrClass)
```

#### Merge.kif:2803

```lisp
(subclass SetOrClass Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 142

- Seed: `0`
- Start step: `1776`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `25`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### Merge.kif:355

```lisp
(domainSubclass rangeSubclass 2 Class)
```

#### Merge.kif:353

```lisp
(instance rangeSubclass BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6970

```lisp
(subclass BodyOfWater SelfConnectedObject)
```

#### Geography.kif:7057

```lisp
(instance NorthAtlanticOcean BodyOfWater)
```

#### Geography.kif:7056

```lisp
(instance NorthAtlanticOcean SaltWaterArea)
```

#### Merge.kif:18254

```lisp
(subclass SaltWaterArea WaterArea)
```

#### Merge.kif:18234

```lisp
(subclass WaterArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2814

```lisp
(subclass Class SetOrClass)
```

#### Merge.kif:2803

```lisp
(subclass SetOrClass Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 143

- Seed: `0`
- Start step: `1776`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `25`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### Merge.kif:355

```lisp
(domainSubclass rangeSubclass 2 Class)
```

#### Merge.kif:353

```lisp
(instance rangeSubclass BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6970

```lisp
(subclass BodyOfWater SelfConnectedObject)
```

#### Geography.kif:7071

```lisp
(instance SouthAtlanticOcean BodyOfWater)
```

#### Geography.kif:7070

```lisp
(instance SouthAtlanticOcean SaltWaterArea)
```

#### Merge.kif:18254

```lisp
(subclass SaltWaterArea WaterArea)
```

#### Merge.kif:18234

```lisp
(subclass WaterArea GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2814

```lisp
(subclass Class SetOrClass)
```

#### Merge.kif:2803

```lisp
(subclass SetOrClass Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 144

- Seed: `0`
- Start step: `1776`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `27`

### Cited source axioms

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### Merge.kif:355

```lisp
(domainSubclass rangeSubclass 2 Class)
```

#### Merge.kif:353

```lisp
(instance rangeSubclass BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Geography.kif:7032

```lisp
(subclass Ocean BodyOfWater)
```

#### Geography.kif:6970

```lisp
(subclass BodyOfWater SelfConnectedObject)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Geography.kif:7049

```lisp
(instance AtlanticOcean Ocean)
```

#### Merge.kif:961

```lisp
(subclass SelfConnectedObject Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2814

```lisp
(subclass Class SetOrClass)
```

#### Merge.kif:2803

```lisp
(subclass SetOrClass Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Replay metadata

```sigma-audit-replay
{
  "version": 1,
  "complete": true,
  "sumo_commit": "85f1b3e678e3008c5db398730317440176ac8ac0",
  "run_id": "37337029890",
  "run_attempt": 1,
  "engine": {
    "commit": "6011d8da5c237d29d68b528f9a8ebcf94b89aa3d",
    "fingerprint": "82b958b3104df4cb7576711153b2e3ddb631e9f2094df084f7f2d9b343e352ac"
  },
  "fingerprint": "76fef8c8b329d8665e3b4ecebe5f6e2eb12b5eba0574447cc1877ce8cb777f66",
  "constituents": [
    {
      "name": "Astronomy.kif",
      "sha256": "842bee559ce31f13238f539e819c19850d2220f8e8367e42d56887cdfb0f0df3"
    },
    {
      "name": "english_format.kif",
      "sha256": "c3757a26cffe4c2c71400d3d812e70199ffd17dfb3bf875244d881ff788d014e"
    },
    {
      "name": "domainEnglishFormat.kif",
      "sha256": "697de5a5d18e5cd082703776377a12b8b15637b440fc9e43d80f3e7f4871f2c9"
    },
    {
      "name": "ArabicCulture.kif",
      "sha256": "9b64e17b78e718350d20c7d1e6461df2f824ad17a1c5f4af9ba9098456666ce2"
    },
    {
      "name": "Anatomy.kif",
      "sha256": "fbe005e3824a051036b4b0a25010836612e2a8840c51292a2a7a225071e02c9e"
    },
    {
      "name": "arteries.kif",
      "sha256": "65e2b849571db9a444b664b7d5a55a0bdc51b67df0e83bde9cd470efd850b5df"
    },
    {
      "name": "Biography.kif",
      "sha256": "586d287bb6688139b459c7fcfe4f85cee4609d1e07b06af928d8282893880907"
    },
    {
      "name": "Cars.kif",
      "sha256": "92bc3b6c60dec9496a3f04e86b69ac8841cbe07033a7d0e0dcac991716051d07"
    },
    {
      "name": "Catalog.kif",
      "sha256": "508f6cbb29476f1283e325214bb70a4b88d93c3aede1d48859d9916b171708e9"
    },
    {
      "name": "Communications.kif",
      "sha256": "6376815627034acafcfe28f17c2dcbc41b79217bebd647e6b9788cf03141c868"
    },
    {
      "name": "ComputerInput.kif",
      "sha256": "4ab99849578a4f5c1d4ae4e317a6e04fa62f0ac931347d2f408e30532f770eca"
    },
    {
      "name": "ComputingBrands.kif",
      "sha256": "95d394e92ccdc25901fe3043a29025a37cc56c0e6f9a3dfa9c43e102f238cc69"
    },
    {
      "name": "CountriesAndRegions.kif",
      "sha256": "5774c8a75f7ff95919fd7b56a9083eb4bf67472cc802f3b7bd775c6f0fb1d890"
    },
    {
      "name": "Cellular&TelephoneArchitecture.kif",
      "sha256": "f1fc28a276fd6f2a9005ee760eb4b236eba062de02bdd6b1058d1c889d45a7df"
    },
    {
      "name": "Dining.kif",
      "sha256": "46e831331592f7e8531b0049c6889edf3f8036d0fdad2f5931fb8871fe4442b5"
    },
    {
      "name": "Economy.kif",
      "sha256": "cb79e14c3ae057c3076b298d2bfe443120f4a1497b6c9c62c77f5f6093e991f5"
    },
    {
      "name": "emotion.kif",
      "sha256": "3d1fbc64cb8fa1d67f61008503b61b4df38b4093b33e354129f643cc66f938a9"
    },
    {
      "name": "engineering.kif",
      "sha256": "0d99e099d9795b66308e7c322d4bcd6ff6dad27187bc7aee1ba67a1290e65b73"
    },
    {
      "name": "Facebook.kif",
      "sha256": "c8b1fc61d4531ba4cce188f894d05f183112d26fa3cd5e2cd5ae51ec9b89140d"
    },
    {
      "name": "FinancialOntology.kif",
      "sha256": "074eb6b569e8a96a95e5dea8302399c455cc5a6f4e7f4ca026d9465ef83d111b"
    },
    {
      "name": "Food.kif",
      "sha256": "589d67c7fb7c6777b4bb8fac93ccb7358b120ecfff89f3651519a75897d6ff91"
    },
    {
      "name": "Geography.kif",
      "sha256": "a6994c4ef94cdc89c432626af2b839f9f62c94f874c556f125b9e96e5295b382"
    },
    {
      "name": "Government.kif",
      "sha256": "e78f07a2082c63168f525953068dde564c211a0b7f20ac50ab57b21229de08a1"
    },
    {
      "name": "Hotel.kif",
      "sha256": "6030add4a1c19b5409c5440331cdd47f5b362239c4f440c2850a9327f9e55591"
    },
    {
      "name": "HouseholdAppliances.kif",
      "sha256": "3568d5b6e9b6a7955ad9f3769543710f4fef6b42945076c20b66ee86addb8a65"
    },
    {
      "name": "Justice.kif",
      "sha256": "4c0060fc8625791cf0b604321f98673f0d449d819efa2906f00a48e6d6375ee3"
    },
    {
      "name": "Languages.kif",
      "sha256": "90c1673e9a1010850569438a2ff750d91213626452c72e101f5ce3ae851fe43d"
    },
    {
      "name": "Law.kif",
      "sha256": "ebf981201bd109b65c36e8df6d665acc582c99f780ec74867986e43e7a1cd85c"
    },
    {
      "name": "Media.kif",
      "sha256": "d3301cf1d3fd9acee6da07883c2640e04447a0e1fdcd91cd1b3966632a64aec0"
    },
    {
      "name": "Medicine.kif",
      "sha256": "81beb245fa0b5790e4a852f4174fb9e3a3ee7234218858b654387a12904d9869"
    },
    {
      "name": "Merge.kif",
      "sha256": "d1a77c04ef79890c6f85d33583efbbf3b7a2faa8bb5b5ca38baaa525c8765965"
    },
    {
      "name": "Mid-level-ontology.kif",
      "sha256": "cd7c6cdfe957efd997bd27bf247bd945479c3cc1f5e88f2d9ed0855ff7243577"
    },
    {
      "name": "MilitaryDevices.kif",
      "sha256": "c4047568efb5f3f2f9af12ede6c14da049cfe7debc0c94b59bdc9dd9eccd8364"
    },
    {
      "name": "Military.kif",
      "sha256": "b59281f36f1a3ce9add7a5208fdabc6888989e42026ac7f922a5c603b55620ff"
    },
    {
      "name": "MilitaryPersons.kif",
      "sha256": "410e17711b3129d66b4e255771a02880f19182ffc0688758236a63611a066570"
    },
    {
      "name": "MilitaryProcesses.kif",
      "sha256": "2e5f4c13aa3c326cd6fd0c7c67da254383f39f8dfabb6f9eeb979c491cd22de2"
    },
    {
      "name": "Music.kif",
      "sha256": "196323d7e3790cbd7d3324b57eebaa456a4f8e88cebeecb708429cb75479bef8"
    },
    {
      "name": "naics.kif",
      "sha256": "bc9b30caf8143a79c14e2642aacc98c7194ae3cd4ab252d5a33362d39911ba0b"
    },
    {
      "name": "People.kif",
      "sha256": "a72de08ee91aa9688c5a5ea9d04243119220661ee2ddef1d94adec4effb164ed"
    },
    {
      "name": "pictureList.kif",
      "sha256": "6122111b315f43515a9d509696239be02438dfb31b7385e541e3ea2041cf9c06"
    },
    {
      "name": "pictureList-ImageNet.kif",
      "sha256": "a4465c213a0081bd35b271109e7bfd14d6b117717ae4af68a12396cf94984510"
    },
    {
      "name": "QoSontology.kif",
      "sha256": "dc00993e038895ee9d001533403475ad5018dd5acfc2b0d0cb3f2a9d40b90d2b"
    },
    {
      "name": "Sports.kif",
      "sha256": "75e20eb63a9decc2c452d8e039330c77c83a78d9963583e680bec8ecb0a47080"
    },
    {
      "name": "TransnationalIssues.kif",
      "sha256": "abba48e36722e81fc8bef776e1e06a5d6059c1d54645364d1909c02534800b1a"
    },
    {
      "name": "Transportation.kif",
      "sha256": "4832269b3a0c941194cec0c95778ac68659ffaf8c0a048c54a6a57b5b62b8f1c"
    },
    {
      "name": "TransportDetail.kif",
      "sha256": "4a02e297a1a84c6a895632648d4ea4f0eb9d3693ef77bbc3d7130c8d2c1c6a58"
    },
    {
      "name": "UXExperimentalTerms.kif",
      "sha256": "35d3d98742ac0119cea40b29ba9a57348621591edea90ebdea9f5f7a99128873"
    },
    {
      "name": "VirusProteinAndCellPart.kif",
      "sha256": "b01e9ab38da5fbb8cf4d7291bf26e13a2590e4b9a9f53bff7a5357bc4362006e"
    },
    {
      "name": "Weather.kif",
      "sha256": "79c72e1ade834a78f5dfa48d4324be1b02ef21953d0a7f198d0a8e171845caaa"
    },
    {
      "name": "WMD.kif",
      "sha256": "35de3453b1b3abd9815505a36452bca5a46a1381294054caac9b3b441358ebc8"
    },
    {
      "name": "capabilities.kif",
      "sha256": "57ccdb0098346eb3a3b6ccb5742f9a660c44d716c4d6b557f7a2efba4d6daf62"
    }
  ],
  "config": {
    "backend": "native",
    "timeLimitSecs": 10,
    "maxSteps": 500000,
    "maxLits": 12,
    "forwardClose": true,
    "wantProof": true,
    "profile": false,
    "selectionTolerancePct": 0
  },
  "request": {
    "count": 1,
    "batch": 1,
    "limit": 64
  },
  "findings": [
    {
      "seed": 0,
      "step": 1214,
      "proof_steps": 5,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Breathing AutonomicProcess)",
          "line": 13076
        }
      ]
    },
    {
      "seed": 0,
      "step": 1214,
      "proof_steps": 5,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Breathing OrganismProcess)",
          "line": 13075
        }
      ]
    },
    {
      "seed": 0,
      "step": 1214,
      "proof_steps": 8,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        }
      ]
    },
    {
      "seed": 0,
      "step": 1214,
      "proof_steps": 39,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass CaseRole BinaryPredicate)",
          "line": 3118
        },
        {
          "file": "Merge.kif",
          "kif": "(instance result CaseRole)",
          "line": 3290
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(instance instance BinaryPredicate)",
          "line": 83
        },
        {
          "file": "Merge.kif",
          "kif": "(domain instance 2 Class)",
          "line": 85
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass BinaryPredicate)",
          "line": 135
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 2 Class)",
          "line": 138
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Physical Entity)",
          "line": 929
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Process Physical)",
          "line": 2120
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Breathing OrganismProcess)",
          "line": 13075
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass OrganismProcess PhysiologicProcess)",
          "line": 13012
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysiologicProcess BiologicalProcess)",
          "line": 12977
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BiologicalProcess InternalChange)",
          "line": 12953
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass InternalChange Process)",
          "line": 16162
        }
      ]
    },
    {
      "seed": 0,
      "step": 1214,
      "proof_steps": 41,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass CaseRole BinaryPredicate)",
          "line": 3118
        },
        {
          "file": "Merge.kif",
          "kif": "(instance result CaseRole)",
          "line": 3290
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(instance instance BinaryPredicate)",
          "line": 83
        },
        {
          "file": "Merge.kif",
          "kif": "(domain instance 2 Class)",
          "line": 85
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass BinaryPredicate)",
          "line": 135
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 2 Class)",
          "line": 138
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Breathing AutonomicProcess)",
          "line": 13076
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Physical Entity)",
          "line": 929
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Process Physical)",
          "line": 2120
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomicProcess PhysiologicProcess)",
          "line": 12985
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysiologicProcess BiologicalProcess)",
          "line": 12977
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BiologicalProcess InternalChange)",
          "line": 12953
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass InternalChange Process)",
          "line": 16162
        }
      ]
    },
    {
      "seed": 0,
      "step": 1224,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "Merge.kif",
          "kif": "(domainSubclass rangeSubclass 2 Class)",
          "line": 355
        },
        {
          "file": "Merge.kif",
          "kif": "(instance rangeSubclass BinaryPredicate)",
          "line": 353
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(rangeSubclass FoodForFn SelfConnectedObject)",
          "line": 19245
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass BodyOfWater SelfConnectedObject)",
          "line": 6970
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Ocean BodyOfWater)",
          "line": 7032
        },
        {
          "file": "Geography.kif",
          "kif": "(instance PacificOcean Ocean)",
          "line": 7085
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SelfConnectedObject Object)",
          "line": 961
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Class SetOrClass)",
          "line": 2814
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SetOrClass Abstract)",
          "line": 2803
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1224,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "Merge.kif",
          "kif": "(domainSubclass rangeSubclass 2 Class)",
          "line": 355
        },
        {
          "file": "Merge.kif",
          "kif": "(instance rangeSubclass BinaryPredicate)",
          "line": 353
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(rangeSubclass FoodForFn SelfConnectedObject)",
          "line": 19245
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass BodyOfWater SelfConnectedObject)",
          "line": 6970
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Ocean BodyOfWater)",
          "line": 7032
        },
        {
          "file": "Geography.kif",
          "kif": "(instance SouthernOcean Ocean)",
          "line": 7180
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SelfConnectedObject Object)",
          "line": 961
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Class SetOrClass)",
          "line": 2814
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SetOrClass Abstract)",
          "line": 2803
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1224,
      "proof_steps": 27,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "Merge.kif",
          "kif": "(domainSubclass rangeSubclass 2 Class)",
          "line": 355
        },
        {
          "file": "Merge.kif",
          "kif": "(instance rangeSubclass BinaryPredicate)",
          "line": 353
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(rangeSubclass FoodForFn SelfConnectedObject)",
          "line": 19245
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Ocean BodyOfWater)",
          "line": 7032
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass BodyOfWater SelfConnectedObject)",
          "line": 6970
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Geography.kif",
          "kif": "(instance PacificOcean Ocean)",
          "line": 7085
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SelfConnectedObject Object)",
          "line": 961
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Class SetOrClass)",
          "line": 2814
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SetOrClass Abstract)",
          "line": 2803
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1224,
      "proof_steps": 27,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "Merge.kif",
          "kif": "(domainSubclass rangeSubclass 2 Class)",
          "line": 355
        },
        {
          "file": "Merge.kif",
          "kif": "(instance rangeSubclass BinaryPredicate)",
          "line": 353
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(rangeSubclass FoodForFn SelfConnectedObject)",
          "line": 19245
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Ocean BodyOfWater)",
          "line": 7032
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass BodyOfWater SelfConnectedObject)",
          "line": 6970
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Geography.kif",
          "kif": "(instance SouthernOcean Ocean)",
          "line": 7180
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SelfConnectedObject Object)",
          "line": 961
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Class SetOrClass)",
          "line": 2814
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SetOrClass Abstract)",
          "line": 2803
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1227,
      "proof_steps": 5,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Touching Transfer)",
          "line": 14696
        }
      ]
    },
    {
      "seed": 0,
      "step": 1227,
      "proof_steps": 14,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "WMD.kif",
          "kif": "(domainSubclass biochemicalAgentDelivery 2 Process)",
          "line": 757
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "WMD.kif",
          "kif": "(instance biochemicalAgentDelivery BinaryPredicate)",
          "line": 755
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        }
      ]
    },
    {
      "seed": 0,
      "step": 1227,
      "proof_steps": 14,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "WMD.kif",
          "kif": "(domainSubclass biochemicalAgentDelivery 2 Process)",
          "line": 757
        },
        {
          "file": "WMD.kif",
          "kif": "(instance biochemicalAgentDelivery BinaryPredicate)",
          "line": 755
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        }
      ]
    },
    {
      "seed": 0,
      "step": 1238,
      "proof_steps": 21,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range ListOrderFn Entity)",
          "line": 3813
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Physical Entity)",
          "line": 929
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Process Physical)",
          "line": 2120
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Breathing OrganismProcess)",
          "line": 13075
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass OrganismProcess PhysiologicProcess)",
          "line": 13012
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysiologicProcess BiologicalProcess)",
          "line": 12977
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BiologicalProcess InternalChange)",
          "line": 12953
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass InternalChange Process)",
          "line": 16162
        }
      ]
    },
    {
      "seed": 0,
      "step": 1238,
      "proof_steps": 12,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "WMD.kif",
          "kif": "(domainSubclass biochemicalAgentDelivery 2 Process)",
          "line": 757
        },
        {
          "file": "WMD.kif",
          "kif": "(instance biochemicalAgentDelivery BinaryPredicate)",
          "line": 755
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        }
      ]
    },
    {
      "seed": 0,
      "step": 1270,
      "proof_steps": 18,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subAttribute ?ATTR1 ?ATTR2) (instance ?ATTR2 ?CLASS)) (instance ?ATTR1 ?CLASS))",
          "line": 786
        },
        {
          "file": "Military.kif",
          "kif": "(subAttribute USMilitaryRankWO4 Soldier)",
          "line": 846
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Military.kif",
          "kif": "(instance USMilitaryRankWO4 CommissionedOfficerRank)",
          "line": 845
        },
        {
          "file": "Military.kif",
          "kif": "(subclass CommissionedOfficerRank MilitaryRank)",
          "line": 508
        },
        {
          "file": "Military.kif",
          "kif": "(subclass MilitaryRank SkilledOccupation)",
          "line": 484
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass SkilledOccupation OccupationalRole)",
          "line": 12121
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass OccupationalRole SocialRole)",
          "line": 31597
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SocialRole RelationalAttribute)",
          "line": 22288
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass RelationalAttribute Attribute)",
          "line": 2393
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Attribute Abstract)",
          "line": 2239
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass MobileCellPhone Telephone)",
          "line": 35137
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass Telephone TelephonyDevice)",
          "line": 34555
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass TelephonyDevice ContactSite)",
          "line": 34539
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass ContactSite Object)",
          "line": 20310
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1270,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subAttribute ?ATTR1 ?ATTR2) (instance ?ATTR2 ?CLASS)) (instance ?ATTR1 ?CLASS))",
          "line": 786
        },
        {
          "file": "Military.kif",
          "kif": "(subAttribute USMilitaryRankWO2 Soldier)",
          "line": 824
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Military.kif",
          "kif": "(instance USMilitaryRankWO2 USWarrantOfficerRank)",
          "line": 821
        },
        {
          "file": "Military.kif",
          "kif": "(subclass USWarrantOfficerRank CommissionedOfficerRank)",
          "line": 807
        },
        {
          "file": "Military.kif",
          "kif": "(subclass CommissionedOfficerRank MilitaryRank)",
          "line": 508
        },
        {
          "file": "Military.kif",
          "kif": "(subclass MilitaryRank SkilledOccupation)",
          "line": 484
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass SkilledOccupation OccupationalRole)",
          "line": 12121
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass OccupationalRole SocialRole)",
          "line": 31597
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SocialRole RelationalAttribute)",
          "line": 22288
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass RelationalAttribute Attribute)",
          "line": 2393
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Attribute Abstract)",
          "line": 2239
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass MobileCellPhone Telephone)",
          "line": 35137
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass Telephone TelephonyDevice)",
          "line": 34555
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass TelephonyDevice ContactSite)",
          "line": 34539
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass ContactSite Object)",
          "line": 20310
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1270,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subAttribute ?ATTR1 ?ATTR2) (instance ?ATTR2 ?CLASS)) (instance ?ATTR1 ?CLASS))",
          "line": 786
        },
        {
          "file": "Military.kif",
          "kif": "(subAttribute USMilitaryRankWO3 Soldier)",
          "line": 835
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Military.kif",
          "kif": "(instance USMilitaryRankWO3 USWarrantOfficerRank)",
          "line": 832
        },
        {
          "file": "Military.kif",
          "kif": "(subclass USWarrantOfficerRank CommissionedOfficerRank)",
          "line": 807
        },
        {
          "file": "Military.kif",
          "kif": "(subclass CommissionedOfficerRank MilitaryRank)",
          "line": 508
        },
        {
          "file": "Military.kif",
          "kif": "(subclass MilitaryRank SkilledOccupation)",
          "line": 484
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass SkilledOccupation OccupationalRole)",
          "line": 12121
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass OccupationalRole SocialRole)",
          "line": 31597
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SocialRole RelationalAttribute)",
          "line": 22288
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass RelationalAttribute Attribute)",
          "line": 2393
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Attribute Abstract)",
          "line": 2239
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass MobileCellPhone Telephone)",
          "line": 35137
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass Telephone TelephonyDevice)",
          "line": 34555
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass TelephonyDevice ContactSite)",
          "line": 34539
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass ContactSite Object)",
          "line": 20310
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1270,
      "proof_steps": 16,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subAttribute ?ATTR1 ?ATTR2) (instance ?ATTR2 ?CLASS)) (instance ?ATTR1 ?CLASS))",
          "line": 786
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subAttribute MilitaryOfficer Soldier)",
          "line": 26748
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(instance MilitaryOfficer GovernmentPosition)",
          "line": 26749
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass GovernmentPosition Position)",
          "line": 26652
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Position SocialRole)",
          "line": 22320
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SocialRole RelationalAttribute)",
          "line": 22288
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass RelationalAttribute Attribute)",
          "line": 2393
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Attribute Abstract)",
          "line": 2239
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass MobileCellPhone Telephone)",
          "line": 35137
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass Telephone TelephonyDevice)",
          "line": 34555
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass TelephonyDevice ContactSite)",
          "line": 34539
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass ContactSite Object)",
          "line": 20310
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1270,
      "proof_steps": 5,
      "axioms": [
        {
          "file": "Media.kif",
          "kif": "(=> (instance ?SITE WebSite) (exists (?PAGE) (and (instance ?PAGE WebPage) (component ?PAGE ?SITE))))",
          "line": 1299
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "ComputingBrands.kif",
          "kif": "(instance IBookstore WebSite)",
          "line": 2667
        }
      ]
    },
    {
      "seed": 0,
      "step": 1290,
      "proof_steps": 21,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range ListOrderFn Entity)",
          "line": 3813
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Physical Entity)",
          "line": 929
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Process Physical)",
          "line": 2120
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Breathing AutonomicProcess)",
          "line": 13076
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomicProcess PhysiologicProcess)",
          "line": 12985
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysiologicProcess BiologicalProcess)",
          "line": 12977
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BiologicalProcess InternalChange)",
          "line": 12953
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass InternalChange Process)",
          "line": 16162
        }
      ]
    },
    {
      "seed": 0,
      "step": 1315,
      "proof_steps": 12,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass CommunicationDevice EngineeringComponent)",
          "line": 4558
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass Telephone CommunicationDevice)",
          "line": 4571
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass MobileCellPhone Telephone)",
          "line": 35137
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        }
      ]
    },
    {
      "seed": 0,
      "step": 1340,
      "proof_steps": 8,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance RockyMountains MountainRange)",
          "line": 343
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (attribute ?AREA MountainousTerrain) (exists (?MTN) (and (instance ?MTN Mountain) (part ?MTN ?AREA))))",
          "line": 3774
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (instance ?AREA MountainRange) (attribute ?AREA MountainousTerrain))",
          "line": 3788
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 49,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 56,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))",
          "line": 25
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5075
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 57,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))",
          "line": 25
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5075
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 85,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 59,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5075
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (climateTypeInArea ?AREA ?CLASS) (exists (?REGION ?TYPE) (and (instance ?REGION GeographicArea) (instance ?TYPE ?CLASS) (attribute ?REGION ?TYPE) (part ?REGION ?AREA))))",
          "line": 3149
        },
        {
          "file": "Geography.kif",
          "kif": "(climateTypeInArea GreatBasin AridClimateZone)",
          "line": 516
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 103,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))",
          "line": 2947
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially IrreflexiveRelation)",
          "line": 12338
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 57,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))",
          "line": 2947
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially IrreflexiveRelation)",
          "line": 12338
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 116,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))",
          "line": 25
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5075
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 107,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica NorthernHemisphere)",
          "line": 5692
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 107,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica WesternHemisphere)",
          "line": 5693
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 118,
      "axioms": [
        {
          "file": "Geography.kif",
          "kif": "(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))",
          "line": 8040
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))",
          "line": 2311
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))",
          "line": 2947
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially IrreflexiveRelation)",
          "line": 12338
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion LosAngelesCalifornia UnitedStates)",
          "line": 3215
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanCity City)",
          "line": 35
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass City LandArea)",
          "line": 18387
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 127,
      "axioms": [
        {
          "file": "Geography.kif",
          "kif": "(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))",
          "line": 8040
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))",
          "line": 2311
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))",
          "line": 2947
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially IrreflexiveRelation)",
          "line": 12338
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion LosAngelesCalifornia UnitedStates)",
          "line": 3215
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation GeopoliticalArea)",
          "line": 18359
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea GeographicArea)",
          "line": 18164
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanCity City)",
          "line": 35
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass City GeopoliticalArea)",
          "line": 18386
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 130,
      "axioms": [
        {
          "file": "Geography.kif",
          "kif": "(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))",
          "line": 8040
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))",
          "line": 2311
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))",
          "line": 2947
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially IrreflexiveRelation)",
          "line": 12338
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanCity City)",
          "line": 35
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass City GeopoliticalArea)",
          "line": 18386
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion LosAngelesCalifornia UnitedStates)",
          "line": 3215
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation GeopoliticalArea)",
          "line": 18359
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea GeographicArea)",
          "line": 18164
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica WesternHemisphere)",
          "line": 5693
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 130,
      "axioms": [
        {
          "file": "Geography.kif",
          "kif": "(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))",
          "line": 8040
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))",
          "line": 2311
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))",
          "line": 2947
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially IrreflexiveRelation)",
          "line": 12338
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanCity City)",
          "line": 35
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass City GeopoliticalArea)",
          "line": 18386
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion LosAngelesCalifornia UnitedStates)",
          "line": 3215
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation GeopoliticalArea)",
          "line": 18359
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea GeographicArea)",
          "line": 18164
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica NorthernHemisphere)",
          "line": 5692
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 125,
      "axioms": [
        {
          "file": "Geography.kif",
          "kif": "(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))",
          "line": 8040
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))",
          "line": 2311
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))",
          "line": 2947
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially IrreflexiveRelation)",
          "line": 12338
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanCity City)",
          "line": 35
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass City GeopoliticalArea)",
          "line": 18386
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion LosAngelesCalifornia UnitedStates)",
          "line": 3215
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 52,
      "axioms": [
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada California)",
          "line": 1074
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially SymmetricRelation)",
          "line": 12339
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        }
      ]
    },
    {
      "seed": 0,
      "step": 1349,
      "proof_steps": 150,
      "axioms": [
        {
          "file": "Geography.kif",
          "kif": "(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))",
          "line": 8040
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))",
          "line": 2311
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince LandArea)",
          "line": 18370
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))",
          "line": 2947
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially IrreflexiveRelation)",
          "line": 12338
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?N EuropeanNation) (part ?N Europe))",
          "line": 86
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedKingdom EuropeanNation)",
          "line": 377
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5075
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion Europe NorthernHemisphere)",
          "line": 5723
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass EuropeanNation Nation)",
          "line": 83
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation GeopoliticalArea)",
          "line": 18359
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanCity City)",
          "line": 35
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass City GeopoliticalArea)",
          "line": 18386
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion LosAngelesCalifornia UnitedStates)",
          "line": 3215
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea GeographicArea)",
          "line": 18164
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica NorthernHemisphere)",
          "line": 5692
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        }
      ]
    },
    {
      "seed": 0,
      "step": 1350,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "Merge.kif",
          "kif": "(domainSubclass rangeSubclass 2 Class)",
          "line": 355
        },
        {
          "file": "Merge.kif",
          "kif": "(instance rangeSubclass BinaryPredicate)",
          "line": 353
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(rangeSubclass FoodForFn SelfConnectedObject)",
          "line": 19245
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass BodyOfWater SelfConnectedObject)",
          "line": 6970
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass River BodyOfWater)",
          "line": 8230
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance MississippiRiver River)",
          "line": 764
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SelfConnectedObject Object)",
          "line": 961
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Class SetOrClass)",
          "line": 2814
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SetOrClass Abstract)",
          "line": 2803
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1350,
      "proof_steps": 21,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "Merge.kif",
          "kif": "(domainSubclass rangeSubclass 2 Class)",
          "line": 355
        },
        {
          "file": "Merge.kif",
          "kif": "(instance rangeSubclass BinaryPredicate)",
          "line": 353
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(rangeSubclass FoodForFn SelfConnectedObject)",
          "line": 19245
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass BodyOfWater SelfConnectedObject)",
          "line": 6970
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAtlanticOcean BodyOfWater)",
          "line": 7057
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SelfConnectedObject Object)",
          "line": 961
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Class SetOrClass)",
          "line": 2814
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SetOrClass Abstract)",
          "line": 2803
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1350,
      "proof_steps": 27,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "Merge.kif",
          "kif": "(domainSubclass rangeSubclass 2 Class)",
          "line": 355
        },
        {
          "file": "Merge.kif",
          "kif": "(instance rangeSubclass BinaryPredicate)",
          "line": 353
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(rangeSubclass FoodForFn SelfConnectedObject)",
          "line": 19245
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass River BodyOfWater)",
          "line": 8230
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass BodyOfWater SelfConnectedObject)",
          "line": 6970
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance MississippiRiver River)",
          "line": 764
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SelfConnectedObject Object)",
          "line": 961
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Class SetOrClass)",
          "line": 2814
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SetOrClass Abstract)",
          "line": 2803
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1374,
      "proof_steps": 8,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance AndesMountains MountainRange)",
          "line": 1522
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (attribute ?AREA MountainousTerrain) (exists (?MTN) (and (instance ?MTN Mountain) (part ?MTN ?AREA))))",
          "line": 3774
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (instance ?AREA MountainRange) (attribute ?AREA MountainousTerrain))",
          "line": 3788
        }
      ]
    },
    {
      "seed": 0,
      "step": 1380,
      "proof_steps": 8,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery ClostridiumTetani Injecting)",
          "line": 1447
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        }
      ]
    },
    {
      "seed": 0,
      "step": 1380,
      "proof_steps": 11,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass CaseRole BinaryPredicate)",
          "line": 3118
        },
        {
          "file": "Merge.kif",
          "kif": "(instance result CaseRole)",
          "line": 3290
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (equal (TemporalCompositionFn ?INTERVAL ?INTERVALTYPE) ?CLASS) (forall (?TIME1 ?TIME2) (=> (and (instance ?TIME1 ?INTERVALTYPE) (instance ?TIME2 ?CLASS)) (exists (?DURATION) (and (duration ?TIME1 ?DURATION) (duration ?TIME2 ?DURATION))))))",
          "line": 12109
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (equal (TemporalCompositionFn ?INTERVAL ?INTERVALTYPE) ?CLASS) (exists (?TIME) (and (instance ?TIME ?CLASS) (starts ?TIME ?INTERVAL))))",
          "line": 12139
        }
      ]
    },
    {
      "seed": 0,
      "step": 1380,
      "proof_steps": 42,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass CaseRole BinaryPredicate)",
          "line": 3118
        },
        {
          "file": "Merge.kif",
          "kif": "(instance result CaseRole)",
          "line": 3290
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(instance instance BinaryPredicate)",
          "line": 83
        },
        {
          "file": "Merge.kif",
          "kif": "(domain instance 2 Class)",
          "line": 85
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass BinaryPredicate)",
          "line": 135
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 2 Class)",
          "line": 138
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery ClostridiumTetani Injecting)",
          "line": 1447
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Physical Entity)",
          "line": 929
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Process Physical)",
          "line": 2120
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Translocation Motion)",
          "line": 14800
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Motion Process)",
          "line": 14063
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Injecting Inserting)",
          "line": 14637
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Inserting Putting)",
          "line": 14615
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Putting Transfer)",
          "line": 14582
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Transfer Translocation)",
          "line": 14457
        }
      ]
    },
    {
      "seed": 0,
      "step": 1387,
      "proof_steps": 38,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass BinaryPredicate)",
          "line": 135
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 2 Class)",
          "line": 138
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 376
        },
        {
          "file": "Merge.kif",
          "kif": "(rangeSubclass FoodForFn SelfConnectedObject)",
          "line": 19245
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 1 Class)",
          "line": 137
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Physical Entity)",
          "line": 929
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Process Physical)",
          "line": 2120
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Breathing AutonomicProcess)",
          "line": 13076
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomicProcess PhysiologicProcess)",
          "line": 12985
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysiologicProcess BiologicalProcess)",
          "line": 12977
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BiologicalProcess InternalChange)",
          "line": 12953
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass InternalChange Process)",
          "line": 16162
        }
      ]
    },
    {
      "seed": 0,
      "step": 1387,
      "proof_steps": 40,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "WMD.kif",
          "kif": "(domainSubclass biochemicalAgentDelivery 2 Process)",
          "line": 757
        },
        {
          "file": "WMD.kif",
          "kif": "(instance biochemicalAgentDelivery BinaryPredicate)",
          "line": 755
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass BinaryPredicate)",
          "line": 135
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 2 Class)",
          "line": 138
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 376
        },
        {
          "file": "Merge.kif",
          "kif": "(rangeSubclass FoodForFn SelfConnectedObject)",
          "line": 19245
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 1 Class)",
          "line": 137
        }
      ]
    },
    {
      "seed": 0,
      "step": 1387,
      "proof_steps": 45,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "WMD.kif",
          "kif": "(domainSubclass biochemicalAgentDelivery 2 Process)",
          "line": 757
        },
        {
          "file": "WMD.kif",
          "kif": "(instance biochemicalAgentDelivery BinaryPredicate)",
          "line": 755
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass BinaryPredicate)",
          "line": 135
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 2 Class)",
          "line": 138
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 376
        },
        {
          "file": "Merge.kif",
          "kif": "(rangeSubclass FoodForFn SelfConnectedObject)",
          "line": 19245
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 1 Class)",
          "line": 137
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range ListOrderFn Entity)",
          "line": 3813
        }
      ]
    },
    {
      "seed": 0,
      "step": 1387,
      "proof_steps": 49,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "WMD.kif",
          "kif": "(domainSubclass biochemicalAgentDelivery 2 Process)",
          "line": 757
        },
        {
          "file": "WMD.kif",
          "kif": "(instance biochemicalAgentDelivery BinaryPredicate)",
          "line": 755
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass BinaryPredicate)",
          "line": 135
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 2 Class)",
          "line": 138
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 376
        },
        {
          "file": "Merge.kif",
          "kif": "(rangeSubclass FoodForFn SelfConnectedObject)",
          "line": 19245
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 1 Class)",
          "line": 137
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range KappaFn Class)",
          "line": 6864
        }
      ]
    },
    {
      "seed": 0,
      "step": 1428,
      "proof_steps": 5,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        }
      ]
    },
    {
      "seed": 0,
      "step": 1428,
      "proof_steps": 17,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range ListOrderFn Entity)",
          "line": 3813
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Breathing OrganismProcess)",
          "line": 13075
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass OrganismProcess PhysiologicProcess)",
          "line": 13012
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysiologicProcess BiologicalProcess)",
          "line": 12977
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BiologicalProcess InternalChange)",
          "line": 12953
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass InternalChange Process)",
          "line": 16162
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Process Physical)",
          "line": 2120
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Physical Entity)",
          "line": 929
        }
      ]
    },
    {
      "seed": 0,
      "step": 1452,
      "proof_steps": 5,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biologicalAgentCarrier ?AGENT ?SUB) (subclass ?SUB ?ORGANISM)) (biologicalAgentCarrier ?AGENT ?ORGANISM))",
          "line": 930
        },
        {
          "file": "WMD.kif",
          "kif": "(biologicalAgentCarrier MalarialPlasmodium Mosquito)",
          "line": 1560
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass Mosquito Insect)",
          "line": 18056
        }
      ]
    },
    {
      "seed": 0,
      "step": 1456,
      "proof_steps": 10,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Transfer Translocation)",
          "line": 14457
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Touching Transfer)",
          "line": 14696
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        }
      ]
    },
    {
      "seed": 0,
      "step": 1456,
      "proof_steps": 12,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Touching Transfer)",
          "line": 14696
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Transfer Translocation)",
          "line": 14457
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Translocation Motion)",
          "line": 14800
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        }
      ]
    },
    {
      "seed": 0,
      "step": 1456,
      "proof_steps": 14,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Motion Process)",
          "line": 14063
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Touching Transfer)",
          "line": 14696
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Transfer Translocation)",
          "line": 14457
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Translocation Motion)",
          "line": 14800
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        }
      ]
    },
    {
      "seed": 0,
      "step": 1456,
      "proof_steps": 16,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Transfer Translocation)",
          "line": 14457
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Touching Transfer)",
          "line": 14696
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Translocation Motion)",
          "line": 14800
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Process Physical)",
          "line": 2120
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Motion Process)",
          "line": 14063
        }
      ]
    },
    {
      "seed": 0,
      "step": 1456,
      "proof_steps": 18,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Touching Transfer)",
          "line": 14696
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Transfer Translocation)",
          "line": 14457
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Translocation Motion)",
          "line": 14800
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Motion Process)",
          "line": 14063
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Physical Entity)",
          "line": 929
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Process Physical)",
          "line": 2120
        }
      ]
    },
    {
      "seed": 0,
      "step": 1456,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range ListOrderFn Entity)",
          "line": 3813
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Touching Transfer)",
          "line": 14696
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Transfer Translocation)",
          "line": 14457
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Translocation Motion)",
          "line": 14800
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Motion Process)",
          "line": 14063
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Physical Entity)",
          "line": 929
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Process Physical)",
          "line": 2120
        }
      ]
    },
    {
      "seed": 0,
      "step": 1456,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 259
        },
        {
          "file": "WMD.kif",
          "kif": "(domainSubclass biochemicalAgentDelivery 2 Process)",
          "line": 757
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Motion Process)",
          "line": 14063
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Touching Transfer)",
          "line": 14696
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Transfer Translocation)",
          "line": 14457
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Translocation Motion)",
          "line": 14800
        }
      ]
    },
    {
      "seed": 0,
      "step": 1456,
      "proof_steps": 21,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 259
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(domainSubclass typicalPart 2 Physical)",
          "line": 33371
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Transfer Translocation)",
          "line": 14457
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Touching Transfer)",
          "line": 14696
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Translocation Motion)",
          "line": 14800
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Process Physical)",
          "line": 2120
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Motion Process)",
          "line": 14063
        }
      ]
    },
    {
      "seed": 0,
      "step": 1456,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 259
        },
        {
          "file": "capabilities.kif",
          "kif": "(domainSubclass requiredRole 1 Process)",
          "line": 140
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Motion Process)",
          "line": 14063
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Touching Transfer)",
          "line": 14696
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Transfer Translocation)",
          "line": 14457
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Translocation Motion)",
          "line": 14800
        }
      ]
    },
    {
      "seed": 0,
      "step": 1456,
      "proof_steps": 21,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 259
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(domainSubclass typicalPart 1 Physical)",
          "line": 33370
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Transfer Translocation)",
          "line": 14457
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Touching Transfer)",
          "line": 14696
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Translocation Motion)",
          "line": 14800
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Process Physical)",
          "line": 2120
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Motion Process)",
          "line": 14063
        }
      ]
    },
    {
      "seed": 0,
      "step": 1456,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 259
        },
        {
          "file": "Merge.kif",
          "kif": "(domainSubclass capability 1 Process)",
          "line": 4851
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Motion Process)",
          "line": 14063
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Touching Transfer)",
          "line": 14696
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Transfer Translocation)",
          "line": 14457
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Translocation Motion)",
          "line": 14800
        }
      ]
    },
    {
      "seed": 0,
      "step": 1456,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 259
        },
        {
          "file": "capabilities.kif",
          "kif": "(domainSubclass requiredRole 3 Entity)",
          "line": 142
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Touching Transfer)",
          "line": 14696
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Transfer Translocation)",
          "line": 14457
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Translocation Motion)",
          "line": 14800
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Motion Process)",
          "line": 14063
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Physical Entity)",
          "line": 929
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Process Physical)",
          "line": 2120
        }
      ]
    },
    {
      "seed": 0,
      "step": 1456,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 259
        },
        {
          "file": "WMD.kif",
          "kif": "(domainSubclass diseaseMedicine 3 Process)",
          "line": 891
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Motion Process)",
          "line": 14063
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Touching Transfer)",
          "line": 14696
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Transfer Translocation)",
          "line": 14457
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Translocation Motion)",
          "line": 14800
        }
      ]
    },
    {
      "seed": 0,
      "step": 1488,
      "proof_steps": 7,
      "axioms": [
        {
          "file": "ComputerInput.kif",
          "kif": "(=> (instance ?KEYBOARD ComputerKeyboard_Generic) (exists (?KEY) (and (instance ?KEY ComputerKeyboardKey) (component ?KEY ?KEYBOARD))))",
          "line": 280
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))",
          "line": 33373
        },
        {
          "file": "ComputerInput.kif",
          "kif": "(typicalPart ComputerKeyboardKey ComputerKeyboard_Generic)",
          "line": 265
        }
      ]
    },
    {
      "seed": 0,
      "step": 1488,
      "proof_steps": 16,
      "axioms": [
        {
          "file": "ComputerInput.kif",
          "kif": "(=> (instance ?KEYBOARD ComputerKeyboard_Generic) (exists (?KEY) (and (instance ?KEY ComputerKeyboardKey) (component ?KEY ?KEYBOARD))))",
          "line": 280
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))",
          "line": 33373
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))",
          "line": 201
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subrelation partTypes typicalPart)",
          "line": 33526
        },
        {
          "file": "ComputerInput.kif",
          "kif": "(partTypes ComputerKeyboard ComputerKeyboardKey)",
          "line": 392
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(instance partTypes BinaryPredicate)",
          "line": 33523
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(instance typicalPart BinaryPredicate)",
          "line": 33359
        },
        {
          "file": "ComputerInput.kif",
          "kif": "(subclass ComputerKeyboard ComputerKeyboard_Generic)",
          "line": 387
        }
      ]
    },
    {
      "seed": 0,
      "step": 1488,
      "proof_steps": 14,
      "axioms": [
        {
          "file": "ComputerInput.kif",
          "kif": "(=> (instance ?KEYBOARD ComputerKeyboard_Generic) (exists (?KEY) (and (instance ?KEY ComputerKeyboardKey) (component ?KEY ?KEYBOARD))))",
          "line": 280
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "ComputerInput.kif",
          "kif": "(subclass ComputerKeyboard ComputerKeyboard_Generic)",
          "line": 387
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))",
          "line": 33373
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subrelation partTypes typicalPart)",
          "line": 33526
        },
        {
          "file": "ComputerInput.kif",
          "kif": "(partTypes ComputerKeyboard ComputerKeyboardKey)",
          "line": 392
        }
      ]
    },
    {
      "seed": 0,
      "step": 1492,
      "proof_steps": 12,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "WMD.kif",
          "kif": "(domainSubclass biochemicalAgentDelivery 2 Process)",
          "line": 757
        },
        {
          "file": "WMD.kif",
          "kif": "(instance biochemicalAgentDelivery BinaryPredicate)",
          "line": 755
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Touching)",
          "line": 178
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        }
      ]
    },
    {
      "seed": 0,
      "step": 1493,
      "proof_steps": 15,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Cars.kif",
          "kif": "(subclass Crankshaft Shaft)",
          "line": 251
        },
        {
          "file": "engineering.kif",
          "kif": "(subclass Shaft EngineeringComponent)",
          "line": 868
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (typicallyContainsPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))",
          "line": 33422
        },
        {
          "file": "Cars.kif",
          "kif": "(typicallyContainsPart Crankshaft IntermittentCombustionEngine)",
          "line": 254
        }
      ]
    },
    {
      "seed": 0,
      "step": 1493,
      "proof_steps": 15,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Cars.kif",
          "kif": "(subclass Crankshaft Shaft)",
          "line": 251
        },
        {
          "file": "engineering.kif",
          "kif": "(subclass Shaft EngineeringComponent)",
          "line": 868
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))",
          "line": 33373
        },
        {
          "file": "Cars.kif",
          "kif": "(typicalPart Crankshaft IntermittentCombustionEngine)",
          "line": 253
        }
      ]
    },
    {
      "seed": 0,
      "step": 1493,
      "proof_steps": 13,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "engineering.kif",
          "kif": "(subclass Shaft EngineeringComponent)",
          "line": 868
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))",
          "line": 33373
        },
        {
          "file": "Cars.kif",
          "kif": "(typicalPart Crankshaft IntermittentCombustionEngine)",
          "line": 253
        },
        {
          "file": "Cars.kif",
          "kif": "(subclass Crankshaft Shaft)",
          "line": 251
        }
      ]
    },
    {
      "seed": 0,
      "step": 1493,
      "proof_steps": 13,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "engineering.kif",
          "kif": "(subclass Shaft EngineeringComponent)",
          "line": 868
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (typicallyContainsPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))",
          "line": 33422
        },
        {
          "file": "Cars.kif",
          "kif": "(typicallyContainsPart Crankshaft IntermittentCombustionEngine)",
          "line": 254
        },
        {
          "file": "Cars.kif",
          "kif": "(subclass Crankshaft Shaft)",
          "line": 251
        }
      ]
    },
    {
      "seed": 0,
      "step": 1522,
      "proof_steps": 13,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))",
          "line": 33373
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subrelation partTypes typicalPart)",
          "line": 33526
        },
        {
          "file": "engineering.kif",
          "kif": "(partTypes Valve Tube)",
          "line": 1182
        },
        {
          "file": "engineering.kif",
          "kif": "(subclass Valve EngineeringComponent)",
          "line": 1163
        }
      ]
    },
    {
      "seed": 0,
      "step": 1541,
      "proof_steps": 5,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentSyndrome ?AGENT ?SYNDROME) (diseaseSymptom ?SYNDROME ?SYMPTOM)) (biochemicalAgentSyndrome ?AGENT ?SYMPTOM))",
          "line": 749
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentSyndrome CrimeanCongoHemorrhagicFeverVirus CrimeanCongoHemorrhagicFever)",
          "line": 1877
        },
        {
          "file": "WMD.kif",
          "kif": "(diseaseSymptom CrimeanCongoHemorrhagicFever Fever)",
          "line": 1871
        }
      ]
    },
    {
      "seed": 0,
      "step": 1541,
      "proof_steps": 5,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biologicalAgentCarrier ?AGENT ?SUB) (subclass ?SUB ?ORGANISM)) (biologicalAgentCarrier ?AGENT ?ORGANISM))",
          "line": 930
        },
        {
          "file": "WMD.kif",
          "kif": "(biologicalAgentCarrier CrimeanCongoHemorrhagicFeverVirus Arachnid)",
          "line": 1876
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Arachnid Arthropod)",
          "line": 18776
        }
      ]
    },
    {
      "seed": 0,
      "step": 1541,
      "proof_steps": 5,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biologicalAgentCarrier ?AGENT ?SUB) (subclass ?SUB ?ORGANISM)) (biologicalAgentCarrier ?AGENT ?ORGANISM))",
          "line": 930
        },
        {
          "file": "WMD.kif",
          "kif": "(biologicalAgentCarrier FrancisellaTularensis Rodent)",
          "line": 1162
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Rodent Mammal)",
          "line": 18906
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 50,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 57,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))",
          "line": 25
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5075
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 58,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))",
          "line": 25
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5075
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 86,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 60,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5075
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (climateTypeInArea ?AREA ?CLASS) (exists (?REGION ?TYPE) (and (instance ?REGION GeographicArea) (instance ?TYPE ?CLASS) (attribute ?REGION ?TYPE) (part ?REGION ?AREA))))",
          "line": 3149
        },
        {
          "file": "Geography.kif",
          "kif": "(climateTypeInArea GreatBasin AridClimateZone)",
          "line": 516
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 105,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))",
          "line": 2947
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially IrreflexiveRelation)",
          "line": 12338
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 58,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))",
          "line": 2947
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially IrreflexiveRelation)",
          "line": 12338
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 118,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))",
          "line": 25
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5075
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 109,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica NorthernHemisphere)",
          "line": 5692
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 109,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica WesternHemisphere)",
          "line": 5693
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 120,
      "axioms": [
        {
          "file": "Geography.kif",
          "kif": "(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))",
          "line": 8040
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))",
          "line": 2311
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))",
          "line": 2947
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially IrreflexiveRelation)",
          "line": 12338
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion LosAngelesCalifornia UnitedStates)",
          "line": 3215
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanCity City)",
          "line": 35
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass City GeopoliticalArea)",
          "line": 18386
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 125,
      "axioms": [
        {
          "file": "Geography.kif",
          "kif": "(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))",
          "line": 8040
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))",
          "line": 2311
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))",
          "line": 2947
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially IrreflexiveRelation)",
          "line": 12338
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion LosAngelesCalifornia UnitedStates)",
          "line": 3215
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanCity City)",
          "line": 35
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass City GeopoliticalArea)",
          "line": 18386
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 128,
      "axioms": [
        {
          "file": "Geography.kif",
          "kif": "(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))",
          "line": 8040
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))",
          "line": 2311
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))",
          "line": 2947
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially IrreflexiveRelation)",
          "line": 12338
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanCity City)",
          "line": 35
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass City GeopoliticalArea)",
          "line": 18386
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion LosAngelesCalifornia UnitedStates)",
          "line": 3215
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica WesternHemisphere)",
          "line": 5693
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 128,
      "axioms": [
        {
          "file": "Geography.kif",
          "kif": "(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))",
          "line": 8040
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))",
          "line": 2311
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))",
          "line": 2947
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially IrreflexiveRelation)",
          "line": 12338
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanCity City)",
          "line": 35
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass City GeopoliticalArea)",
          "line": 18386
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion LosAngelesCalifornia UnitedStates)",
          "line": 3215
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica NorthernHemisphere)",
          "line": 5692
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 53,
      "axioms": [
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada California)",
          "line": 1074
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially SymmetricRelation)",
          "line": 12339
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        }
      ]
    },
    {
      "seed": 0,
      "step": 1559,
      "proof_steps": 149,
      "axioms": [
        {
          "file": "Geography.kif",
          "kif": "(=> (connects ?BETWEEN ?END1 ?END2) (not (equal ?END1 ?END2)))",
          "line": 8040
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))) (connects ?OBJ1 ?OBJ2 ?OBJ3))",
          "line": 12321
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))",
          "line": 39
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))",
          "line": 2311
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (meetsSpatially ?AREA1 ?AREA2) (not (overlapsSpatially ?AREA1 ?AREA2)))",
          "line": 2546
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Idaho Nevada)",
          "line": 986
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Idaho AmericanState)",
          "line": 982
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanState StateOrProvince)",
          "line": 21
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass StateOrProvince GeopoliticalArea)",
          "line": 18369
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Nevada)",
          "line": 509
        },
        {
          "file": "Geography.kif",
          "kif": "(instance GreatBasin EndorheicBasin)",
          "line": 503
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass EndorheicBasin Basin)",
          "line": 486
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Basin LandForm)",
          "line": 6711
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Idaho)",
          "line": 513
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially Nevada Oregon)",
          "line": 1073
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance Nevada AmericanState)",
          "line": 1072
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Oregon)",
          "line": 511
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(meetsSpatially California Mexico)",
          "line": 947
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin Mexico)",
          "line": 515
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion GreatBasin California)",
          "line": 512
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?OBJ1 ?OBJ2 ?OBJ3) (and (connected ?OBJ1 ?OBJ2) (connected ?OBJ1 ?OBJ3) (not (connected ?OBJ2 ?OBJ3))))",
          "line": 12314
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connects ?ARC ?NODE1 ?NODE2) (connects ?ARC ?NODE2 ?NODE1))",
          "line": 12328
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation LandArea)",
          "line": 18360
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedStates Nation)",
          "line": 419
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL IrreflexiveRelation) (forall (?INST) (not (?REL ?INST ?INST))))",
          "line": 2947
        },
        {
          "file": "Merge.kif",
          "kif": "(instance meetsSpatially IrreflexiveRelation)",
          "line": 12338
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?N EuropeanNation) (part ?N Europe))",
          "line": 86
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance UnitedKingdom EuropeanNation)",
          "line": 377
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5075
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion Europe NorthernHemisphere)",
          "line": 5723
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass EuropeanNation Nation)",
          "line": 83
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation GeopoliticalArea)",
          "line": 18359
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(subclass AmericanCity City)",
          "line": 35
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass City GeopoliticalArea)",
          "line": 18386
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion LosAngelesCalifornia UnitedStates)",
          "line": 3215
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica NorthernHemisphere)",
          "line": 5692
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        }
      ]
    },
    {
      "seed": 0,
      "step": 1570,
      "proof_steps": 10,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))",
          "line": 33373
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(typicalPart GunChamber GunBarrel)",
          "line": 1819
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass GunBarrel EngineeringComponent)",
          "line": 1777
        }
      ]
    },
    {
      "seed": 0,
      "step": 1570,
      "proof_steps": 16,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))",
          "line": 33373
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))",
          "line": 201
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subrelation partTypes typicalPart)",
          "line": 33526
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(partTypes GunBore GunBarrel)",
          "line": 1891
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(instance partTypes BinaryPredicate)",
          "line": 33523
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(instance typicalPart BinaryPredicate)",
          "line": 33359
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass GunBarrel EngineeringComponent)",
          "line": 1777
        }
      ]
    },
    {
      "seed": 0,
      "step": 1570,
      "proof_steps": 13,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass GunBarrel EngineeringComponent)",
          "line": 1777
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))",
          "line": 33373
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subrelation partTypes typicalPart)",
          "line": 33526
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(partTypes GunBore GunBarrel)",
          "line": 1891
        }
      ]
    },
    {
      "seed": 0,
      "step": 1570,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass GunBarrel EngineeringComponent)",
          "line": 1777
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (and (partTypes ?PARTTYPE ?WHOLETYPE) (instance ?PART ?PARTTYPE)) (exists (?WHOLE) (and (instance ?WHOLE ?WHOLETYPE) (part ?PART ?WHOLE))))",
          "line": 33534
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(partTypes GunBore GunBarrel)",
          "line": 1891
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))",
          "line": 33373
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))",
          "line": 201
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subrelation partTypes typicalPart)",
          "line": 33526
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(instance partTypes BinaryPredicate)",
          "line": 33523
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(instance typicalPart BinaryPredicate)",
          "line": 33359
        }
      ]
    },
    {
      "seed": 0,
      "step": 1570,
      "proof_steps": 16,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass GunBarrel EngineeringComponent)",
          "line": 1777
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (and (partTypes ?PARTTYPE ?WHOLETYPE) (instance ?PART ?PARTTYPE)) (exists (?WHOLE) (and (instance ?WHOLE ?WHOLETYPE) (part ?PART ?WHOLE))))",
          "line": 33534
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(partTypes GunBore GunBarrel)",
          "line": 1891
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))",
          "line": 33373
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subrelation partTypes typicalPart)",
          "line": 33526
        }
      ]
    },
    {
      "seed": 0,
      "step": 1575,
      "proof_steps": 40,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass BinaryPredicate)",
          "line": 135
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 2 Class)",
          "line": 138
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 376
        },
        {
          "file": "Food.kif",
          "kif": "(rangeSubclass PlantFn Plant)",
          "line": 4672
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 1 Class)",
          "line": 137
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass InternalChange Process)",
          "line": 16162
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BiologicalProcess InternalChange)",
          "line": 12953
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Physical Entity)",
          "line": 929
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Process Physical)",
          "line": 2120
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Breathing OrganismProcess)",
          "line": 13075
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass OrganismProcess PhysiologicProcess)",
          "line": 13012
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysiologicProcess BiologicalProcess)",
          "line": 12977
        }
      ]
    },
    {
      "seed": 0,
      "step": 1575,
      "proof_steps": 42,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass BinaryPredicate)",
          "line": 135
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 2 Class)",
          "line": 138
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 376
        },
        {
          "file": "Food.kif",
          "kif": "(rangeSubclass PlantFn Plant)",
          "line": 4672
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 1 Class)",
          "line": 137
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Breathing AutonomicProcess)",
          "line": 13076
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass InternalChange Process)",
          "line": 16162
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BiologicalProcess InternalChange)",
          "line": 12953
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Physical Entity)",
          "line": 929
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Process Physical)",
          "line": 2120
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomicProcess PhysiologicProcess)",
          "line": 12985
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysiologicProcess BiologicalProcess)",
          "line": 12977
        }
      ]
    },
    {
      "seed": 0,
      "step": 1575,
      "proof_steps": 40,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "WMD.kif",
          "kif": "(domainSubclass biochemicalAgentDelivery 2 Process)",
          "line": 757
        },
        {
          "file": "WMD.kif",
          "kif": "(instance biochemicalAgentDelivery BinaryPredicate)",
          "line": 755
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass BinaryPredicate)",
          "line": 135
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 2 Class)",
          "line": 138
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 376
        },
        {
          "file": "Food.kif",
          "kif": "(rangeSubclass PlantFn Plant)",
          "line": 4672
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 1 Class)",
          "line": 137
        }
      ]
    },
    {
      "seed": 0,
      "step": 1575,
      "proof_steps": 45,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "WMD.kif",
          "kif": "(domainSubclass biochemicalAgentDelivery 2 Process)",
          "line": 757
        },
        {
          "file": "WMD.kif",
          "kif": "(instance biochemicalAgentDelivery BinaryPredicate)",
          "line": 755
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass BinaryPredicate)",
          "line": 135
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 2 Class)",
          "line": 138
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 376
        },
        {
          "file": "Food.kif",
          "kif": "(rangeSubclass PlantFn Plant)",
          "line": 4672
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 1 Class)",
          "line": 137
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range ListOrderFn Entity)",
          "line": 3813
        }
      ]
    },
    {
      "seed": 0,
      "step": 1575,
      "proof_steps": 49,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "WMD.kif",
          "kif": "(domainSubclass biochemicalAgentDelivery 2 Process)",
          "line": 757
        },
        {
          "file": "WMD.kif",
          "kif": "(instance biochemicalAgentDelivery BinaryPredicate)",
          "line": 755
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass BinaryPredicate)",
          "line": 135
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 2 Class)",
          "line": 138
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 376
        },
        {
          "file": "Food.kif",
          "kif": "(rangeSubclass PlantFn Plant)",
          "line": 4672
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subclass 1 Class)",
          "line": 137
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range KappaFn Class)",
          "line": 6864
        }
      ]
    },
    {
      "seed": 0,
      "step": 1577,
      "proof_steps": 5,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BurkholderiaPseudomallei Ingesting)",
          "line": 366
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Transfer)",
          "line": 13109
        }
      ]
    },
    {
      "seed": 0,
      "step": 1577,
      "proof_steps": 14,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BurkholderiaPseudomallei Breathing)",
          "line": 365
        },
        {
          "file": "WMD.kif",
          "kif": "(domainSubclass biochemicalAgentDelivery 2 Process)",
          "line": 757
        },
        {
          "file": "WMD.kif",
          "kif": "(instance biochemicalAgentDelivery BinaryPredicate)",
          "line": 755
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        }
      ]
    },
    {
      "seed": 0,
      "step": 1577,
      "proof_steps": 15,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "WMD.kif",
          "kif": "(domainSubclass biochemicalAgentDelivery 2 Process)",
          "line": 757
        },
        {
          "file": "WMD.kif",
          "kif": "(instance biochemicalAgentDelivery BinaryPredicate)",
          "line": 755
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BurkholderiaPseudomallei Breathing)",
          "line": 365
        }
      ]
    },
    {
      "seed": 0,
      "step": 1577,
      "proof_steps": 14,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "WMD.kif",
          "kif": "(domainSubclass biochemicalAgentDelivery 2 Process)",
          "line": 757
        },
        {
          "file": "WMD.kif",
          "kif": "(instance biochemicalAgentDelivery BinaryPredicate)",
          "line": 755
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery BurkholderiaPseudomallei Injecting)",
          "line": 364
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 29,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance RockyMountains MountainRange)",
          "line": 343
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))",
          "line": 201
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subrelation PartialOrderingRelation)",
          "line": 176
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion RockyMountains NorthAmerica)",
          "line": 350
        },
        {
          "file": "Merge.kif",
          "kif": "(instance geographicSubregion BinaryPredicate)",
          "line": 18142
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(instance partlyLocated BinaryPredicate)",
          "line": 5030
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 33,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance RockyMountains MountainRange)",
          "line": 343
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))",
          "line": 201
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subrelation PartialOrderingRelation)",
          "line": 176
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion RockyMountains NorthAmerica)",
          "line": 350
        },
        {
          "file": "Merge.kif",
          "kif": "(instance geographicSubregion BinaryPredicate)",
          "line": 18142
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(instance partlyLocated BinaryPredicate)",
          "line": 5030
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica WesternHemisphere)",
          "line": 5693
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 33,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance RockyMountains MountainRange)",
          "line": 343
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))",
          "line": 201
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subrelation PartialOrderingRelation)",
          "line": 176
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion RockyMountains NorthAmerica)",
          "line": 350
        },
        {
          "file": "Merge.kif",
          "kif": "(instance geographicSubregion BinaryPredicate)",
          "line": 18142
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(instance partlyLocated BinaryPredicate)",
          "line": 5030
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica NorthernHemisphere)",
          "line": 5692
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 32,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance RockyMountains MountainRange)",
          "line": 343
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))",
          "line": 201
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subrelation PartialOrderingRelation)",
          "line": 176
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion RockyMountains NorthAmerica)",
          "line": 350
        },
        {
          "file": "Merge.kif",
          "kif": "(instance geographicSubregion BinaryPredicate)",
          "line": 18142
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(instance partlyLocated BinaryPredicate)",
          "line": 5030
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 35,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance RockyMountains MountainRange)",
          "line": 343
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))",
          "line": 201
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subrelation PartialOrderingRelation)",
          "line": 176
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion RockyMountains NorthAmerica)",
          "line": 350
        },
        {
          "file": "Merge.kif",
          "kif": "(instance geographicSubregion BinaryPredicate)",
          "line": 18142
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(instance partlyLocated BinaryPredicate)",
          "line": 5030
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica WesternHemisphere)",
          "line": 5693
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 36,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance RockyMountains MountainRange)",
          "line": 343
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))",
          "line": 201
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subrelation PartialOrderingRelation)",
          "line": 176
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion RockyMountains NorthAmerica)",
          "line": 350
        },
        {
          "file": "Merge.kif",
          "kif": "(instance geographicSubregion BinaryPredicate)",
          "line": 18142
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(instance partlyLocated BinaryPredicate)",
          "line": 5030
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica NorthernHemisphere)",
          "line": 5692
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 33,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance RockyMountains MountainRange)",
          "line": 343
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))",
          "line": 201
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subrelation PartialOrderingRelation)",
          "line": 176
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion RockyMountains NorthAmerica)",
          "line": 350
        },
        {
          "file": "Merge.kif",
          "kif": "(instance geographicSubregion BinaryPredicate)",
          "line": 18142
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(instance partlyLocated BinaryPredicate)",
          "line": 5030
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 26,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance AndesMountains MountainRange)",
          "line": 1522
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion AndesMountains SouthAmerica)",
          "line": 1529
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 29,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance AndesMountains MountainRange)",
          "line": 1522
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion SouthAmerica WesternHemisphere)",
          "line": 5708
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion AndesMountains SouthAmerica)",
          "line": 1529
        },
        {
          "file": "Merge.kif",
          "kif": "(instance geographicSubregion TransitiveRelation)",
          "line": 18143
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 28,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance AndesMountains MountainRange)",
          "line": 1522
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion AndesMountains SouthAmerica)",
          "line": 1529
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 31,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance AndesMountains MountainRange)",
          "line": 1522
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion SouthAmerica WesternHemisphere)",
          "line": 5708
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion AndesMountains SouthAmerica)",
          "line": 1529
        },
        {
          "file": "Merge.kif",
          "kif": "(instance geographicSubregion TransitiveRelation)",
          "line": 18143
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 30,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance AndesMountains MountainRange)",
          "line": 1522
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion AndesMountains SouthAmerica)",
          "line": 1529
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 26,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance CaliforniaCoastRanges MountainRange)",
          "line": 443
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion CaliforniaCoastRanges California)",
          "line": 452
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 29,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance CaliforniaCoastRanges MountainRange)",
          "line": 443
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion CaliforniaCoastRanges California)",
          "line": 452
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 30,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance CaliforniaCoastRanges MountainRange)",
          "line": 443
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion CaliforniaCoastRanges California)",
          "line": 452
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 9,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance CaliforniaCoastRanges MountainRange)",
          "line": 443
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (attribute ?AREA MountainousTerrain) (exists (?MTN) (and (instance ?MTN Mountain) (part ?MTN ?AREA))))",
          "line": 3774
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (instance ?AREA MountainRange) (attribute ?AREA MountainousTerrain))",
          "line": 3788
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 36,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance RockyMountains MountainRange)",
          "line": 343
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?REL1 ?REL2) (instance ?REL1 Predicate) (instance ?REL2 Predicate) (?REL1 @ROW)) (?REL2 @ROW))",
          "line": 201
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subrelation PartialOrderingRelation)",
          "line": 176
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion RockyMountains NorthAmerica)",
          "line": 350
        },
        {
          "file": "Merge.kif",
          "kif": "(instance geographicSubregion BinaryPredicate)",
          "line": 18142
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(instance partlyLocated BinaryPredicate)",
          "line": 5030
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica WesternHemisphere)",
          "line": 5693
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 29,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance AndesMountains MountainRange)",
          "line": 1522
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion AndesMountains SouthAmerica)",
          "line": 1529
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 32,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance AndesMountains MountainRange)",
          "line": 1522
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion SouthAmerica WesternHemisphere)",
          "line": 5708
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion AndesMountains SouthAmerica)",
          "line": 1529
        },
        {
          "file": "Merge.kif",
          "kif": "(instance geographicSubregion TransitiveRelation)",
          "line": 18143
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 26,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance RockyMountains MountainRange)",
          "line": 343
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion RockyMountains NorthAmerica)",
          "line": 350
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 29,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance RockyMountains MountainRange)",
          "line": 343
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion RockyMountains NorthAmerica)",
          "line": 350
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica NorthernHemisphere)",
          "line": 5692
        },
        {
          "file": "Merge.kif",
          "kif": "(instance geographicSubregion TransitiveRelation)",
          "line": 18143
        }
      ]
    },
    {
      "seed": 0,
      "step": 1601,
      "proof_steps": 29,
      "axioms": [
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))",
          "line": 6439
        },
        {
          "file": "Geography.kif",
          "kif": "(instance RockyMountains MountainRange)",
          "line": 343
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion located)",
          "line": 18146
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion RockyMountains NorthAmerica)",
          "line": 350
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion NorthAmerica WesternHemisphere)",
          "line": 5693
        },
        {
          "file": "Merge.kif",
          "kif": "(instance geographicSubregion TransitiveRelation)",
          "line": 18143
        }
      ]
    },
    {
      "seed": 0,
      "step": 1636,
      "proof_steps": 15,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass CommunicationDevice EngineeringComponent)",
          "line": 4558
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass Telephone CommunicationDevice)",
          "line": 4571
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass MobileCellPhone Telephone)",
          "line": 35137
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        }
      ]
    },
    {
      "seed": 0,
      "step": 1636,
      "proof_steps": 17,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Communications.kif",
          "kif": "(=> (instance ?SYSTEM TelephoneSystem) (exists (?PHONE) (and (instance ?PHONE Telephone) (engineeringSubcomponent ?PHONE ?SYSTEM))))",
          "line": 31
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass Telephone CommunicationDevice)",
          "line": 4571
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass CommunicationDevice EngineeringComponent)",
          "line": 4558
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(subclass PublicSwitchedTelephoneNetwork TelephoneSystem)",
          "line": 1137
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        }
      ]
    },
    {
      "seed": 0,
      "step": 1636,
      "proof_steps": 15,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Communications.kif",
          "kif": "(=> (instance ?SYSTEM TelephoneSystem) (exists (?PHONE) (and (instance ?PHONE Telephone) (engineeringSubcomponent ?PHONE ?SYSTEM))))",
          "line": 31
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(subclass PublicSwitchedTelephoneNetwork TelephoneSystem)",
          "line": 1137
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(domain engineeringSubcomponent 2 EngineeringComponent)",
          "line": 20794
        },
        {
          "file": "Merge.kif",
          "kif": "(instance engineeringSubcomponent BinaryPredicate)",
          "line": 20792
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        }
      ]
    },
    {
      "seed": 0,
      "step": 1636,
      "proof_steps": 27,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(subclass PublicSwitchedTelephoneNetwork TelephoneSystem)",
          "line": 1137
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Communications.kif",
          "kif": "(subclass TelephoneSystem CommunicationSystem)",
          "line": 26
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass CommunicationSystem CollectionOfObjects)",
          "line": 11288
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (instance ?COLL CollectionOfObjects) (memberType ?COLL Object))",
          "line": 32155
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(instance memberType BinaryPredicate)",
          "line": 32145
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(domain memberType 1 Collection)",
          "line": 32146
        },
        {
          "file": "Merge.kif",
          "kif": "(instance instance BinaryPredicate)",
          "line": 83
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Predicate Relation)",
          "line": 4214
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Relation Abstract)",
          "line": 2843
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Collection Physical)",
          "line": 1545
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1636,
      "proof_steps": 28,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(subclass PublicSwitchedTelephoneNetwork TelephoneSystem)",
          "line": 1137
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Communications.kif",
          "kif": "(subclass TelephoneSystem CommunicationSystem)",
          "line": 26
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass CommunicationSystem CollectionOfObjects)",
          "line": 11288
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (instance ?COLL CollectionOfObjects) (memberType ?COLL Object))",
          "line": 32155
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(instance memberType BinaryPredicate)",
          "line": 32145
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(domain memberType 1 Collection)",
          "line": 32146
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subAttribute PartialOrderingRelation)",
          "line": 768
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TotalValuedRelation)",
          "line": 3077
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TotalValuedRelation Relation)",
          "line": 2884
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Relation Abstract)",
          "line": 2843
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Collection Physical)",
          "line": 1545
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1644,
      "proof_steps": 15,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass CommunicationDevice EngineeringComponent)",
          "line": 4558
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass ReceiverDevice CommunicationDevice)",
          "line": 3017
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass MobileCellPhone ReceiverDevice)",
          "line": 35136
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        }
      ]
    },
    {
      "seed": 0,
      "step": 1644,
      "proof_steps": 13,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass MobileCellPhone ReceiverDevice)",
          "line": 35136
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass ReceiverDevice CommunicationDevice)",
          "line": 3017
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass CommunicationDevice EngineeringComponent)",
          "line": 4558
        }
      ]
    },
    {
      "seed": 0,
      "step": 1674,
      "proof_steps": 5,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biologicalAgentCarrier ?AGENT ?SUB) (subclass ?SUB ?ORGANISM)) (biologicalAgentCarrier ?AGENT ?ORGANISM))",
          "line": 930
        },
        {
          "file": "WMD.kif",
          "kif": "(biologicalAgentCarrier BacillusAnthracis HoofedMammal)",
          "line": 264
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass HoofedMammal Mammal)",
          "line": 18876
        }
      ]
    },
    {
      "seed": 0,
      "step": 1684,
      "proof_steps": 18,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (instance ?PRED2 ?CLASS) (subclass ?CLASS InheritableRelation)) (instance ?PRED1 ?CLASS))",
          "line": 209
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Media.kif",
          "kif": "(subrelation keyName subString)",
          "line": 3041
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subrelation subString part)",
          "line": 34327
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subrelation PartialOrderingRelation)",
          "line": 176
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(instance part PartialOrderingRelation)",
          "line": 1047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation AntisymmetricRelation)",
          "line": 3075
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryRelation InheritableRelation)",
          "line": 2919
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AntisymmetricRelation BinaryRelation)",
          "line": 2990
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Media.kif",
          "kif": "(instance keyName PartialValuedRelation)",
          "line": 3038
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TotalValuedRelation)",
          "line": 3077
        },
        {
          "file": "Merge.kif",
          "kif": "(disjoint TotalValuedRelation PartialValuedRelation)",
          "line": 2852
        }
      ]
    },
    {
      "seed": 0,
      "step": 1684,
      "proof_steps": 17,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (instance ?PRED2 ?CLASS) (subclass ?CLASS InheritableRelation)) (instance ?PRED1 ?CLASS))",
          "line": 209
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subrelation subString part)",
          "line": 34327
        },
        {
          "file": "Merge.kif",
          "kif": "(instance part PartialOrderingRelation)",
          "line": 1047
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation AntisymmetricRelation)",
          "line": 3075
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryRelation InheritableRelation)",
          "line": 2919
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AntisymmetricRelation BinaryRelation)",
          "line": 2990
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Media.kif",
          "kif": "(subrelation keyName subString)",
          "line": 3041
        },
        {
          "file": "Media.kif",
          "kif": "(instance keyName PartialValuedRelation)",
          "line": 3038
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TotalValuedRelation)",
          "line": 3077
        },
        {
          "file": "Merge.kif",
          "kif": "(disjoint TotalValuedRelation PartialValuedRelation)",
          "line": 2852
        }
      ]
    },
    {
      "seed": 0,
      "step": 1776,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "Merge.kif",
          "kif": "(domainSubclass rangeSubclass 2 Class)",
          "line": 355
        },
        {
          "file": "Merge.kif",
          "kif": "(instance rangeSubclass BinaryPredicate)",
          "line": 353
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(rangeSubclass FoodForFn SelfConnectedObject)",
          "line": 19245
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass BodyOfWater SelfConnectedObject)",
          "line": 6970
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Ocean BodyOfWater)",
          "line": 7032
        },
        {
          "file": "Geography.kif",
          "kif": "(instance AtlanticOcean Ocean)",
          "line": 7049
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SelfConnectedObject Object)",
          "line": 961
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Class SetOrClass)",
          "line": 2814
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SetOrClass Abstract)",
          "line": 2803
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1776,
      "proof_steps": 25,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "Merge.kif",
          "kif": "(domainSubclass rangeSubclass 2 Class)",
          "line": 355
        },
        {
          "file": "Merge.kif",
          "kif": "(instance rangeSubclass BinaryPredicate)",
          "line": 353
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(rangeSubclass FoodForFn SelfConnectedObject)",
          "line": 19245
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass BodyOfWater SelfConnectedObject)",
          "line": 6970
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAtlanticOcean BodyOfWater)",
          "line": 7057
        },
        {
          "file": "Geography.kif",
          "kif": "(instance NorthAtlanticOcean SaltWaterArea)",
          "line": 7056
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SaltWaterArea WaterArea)",
          "line": 18254
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass WaterArea GeographicArea)",
          "line": 18234
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Class SetOrClass)",
          "line": 2814
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SetOrClass Abstract)",
          "line": 2803
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1776,
      "proof_steps": 25,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "Merge.kif",
          "kif": "(domainSubclass rangeSubclass 2 Class)",
          "line": 355
        },
        {
          "file": "Merge.kif",
          "kif": "(instance rangeSubclass BinaryPredicate)",
          "line": 353
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(rangeSubclass FoodForFn SelfConnectedObject)",
          "line": 19245
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass BodyOfWater SelfConnectedObject)",
          "line": 6970
        },
        {
          "file": "Geography.kif",
          "kif": "(instance SouthAtlanticOcean BodyOfWater)",
          "line": 7071
        },
        {
          "file": "Geography.kif",
          "kif": "(instance SouthAtlanticOcean SaltWaterArea)",
          "line": 7070
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SaltWaterArea WaterArea)",
          "line": 18254
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass WaterArea GeographicArea)",
          "line": 18234
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Class SetOrClass)",
          "line": 2814
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SetOrClass Abstract)",
          "line": 2803
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    },
    {
      "seed": 0,
      "step": 1776,
      "proof_steps": 27,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "Merge.kif",
          "kif": "(domainSubclass rangeSubclass 2 Class)",
          "line": 355
        },
        {
          "file": "Merge.kif",
          "kif": "(instance rangeSubclass BinaryPredicate)",
          "line": 353
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(rangeSubclass FoodForFn SelfConnectedObject)",
          "line": 19245
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Ocean BodyOfWater)",
          "line": 7032
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass BodyOfWater SelfConnectedObject)",
          "line": 6970
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Geography.kif",
          "kif": "(instance AtlanticOcean Ocean)",
          "line": 7049
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SelfConnectedObject Object)",
          "line": 961
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Class SetOrClass)",
          "line": 2814
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass SetOrClass Abstract)",
          "line": 2803
        },
        {
          "file": "Merge.kif",
          "kif": "(partition Entity Physical Abstract)",
          "line": 911
        }
      ]
    }
  ]
}
```
