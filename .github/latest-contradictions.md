# Full SUMO contradiction report

Open https://sigmakee.dev/audit and choose Latest master contradiction report.
Save any work you want to keep before confirming replacement and replay.
The app verifies master, constituents, and engine inputs before replaying only the steps below.

## Contradiction 1

- Seed: `0`
- Start step: `9`
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
- Start step: `9`
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
- Start step: `13`
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

## Contradiction 4

- Seed: `0`
- Start step: `13`
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

## Contradiction 5

- Seed: `0`
- Start step: `13`
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

## Contradiction 6

- Seed: `0`
- Start step: `13`
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

## Contradiction 7

- Seed: `0`
- Start step: `13`
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

## Contradiction 8

- Seed: `0`
- Start step: `13`
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

## Contradiction 9

- Seed: `0`
- Start step: `13`
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

## Contradiction 10

- Seed: `0`
- Start step: `13`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `24`

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

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3813

```lisp
(range ListOrderFn Entity)
```

## Contradiction 11

- Seed: `0`
- Start step: `13`
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

## Contradiction 12

- Seed: `0`
- Start step: `13`
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

## Contradiction 13

- Seed: `0`
- Start step: `13`
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

## Contradiction 14

- Seed: `0`
- Start step: `13`
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

## Contradiction 15

- Seed: `0`
- Start step: `13`
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

## Contradiction 16

- Seed: `0`
- Start step: `13`
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

## Contradiction 17

- Seed: `0`
- Start step: `13`
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

## Contradiction 18

- Seed: `0`
- Start step: `13`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `40`

### Cited source axioms

#### Merge.kif:376

```lisp
(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
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

#### Merge.kif:137

```lisp
(domain subclass 1 Class)
```

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### Merge.kif:138

```lisp
(domain subclass 2 Class)
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

## Contradiction 19

- Seed: `0`
- Start step: `13`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `39`

### Cited source axioms

#### Merge.kif:376

```lisp
(=> (and (rangeSubclass ?REL ?CLASS1) (rangeSubclass ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:19245

```lisp
(rangeSubclass FoodForFn SelfConnectedObject)
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

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
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

## Contradiction 20

- Seed: `0`
- Start step: `25`
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

#### engineering.kif:868

```lisp
(subclass Shaft EngineeringComponent)
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### engineering.kif:869

```lisp
(typicalPart Shaft Motor)
```

## Contradiction 21

- Seed: `0`
- Start step: `25`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `12`

### Cited source axioms

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:20781

```lisp
(=> (instance ?MACHINE Machine) (exists (?COMP1 ?COMP2) (and (instance ?COMP1 EngineeringComponent) (instance ?COMP2 EngineeringComponent) (not (equal ?COMP1 ?COMP2)) (part ?COMP1 ?MACHINE) (part ?COMP2 ?MACHINE))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### engineering.kif:869

```lisp
(typicalPart Shaft Motor)
```

#### engineering.kif:738

```lisp
(subclass Motor Machine)
```

## Contradiction 22

- Seed: `0`
- Start step: `31`
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

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

## Contradiction 23

- Seed: `0`
- Start step: `86`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `5`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1726

```lisp
(biochemicalAgentDelivery HepatitisAVirus Ingesting)
```

## Contradiction 24

- Seed: `0`
- Start step: `86`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `8`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1726

```lisp
(biochemicalAgentDelivery HepatitisAVirus Ingesting)
```

#### Merge.kif:13109

```lisp
(subclass Ingesting Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

## Contradiction 25

- Seed: `0`
- Start step: `88`
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

## Contradiction 26

- Seed: `0`
- Start step: `88`
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

#### Merge.kif:13075

```lisp
(subclass Breathing OrganismProcess)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
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

## Contradiction 27

- Seed: `0`
- Start step: `88`
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

## Contradiction 28

- Seed: `0`
- Start step: `92`
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

## Contradiction 29

- Seed: `0`
- Start step: `92`
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

## Contradiction 30

- Seed: `0`
- Start step: `92`
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

## Contradiction 31

- Seed: `0`
- Start step: `92`
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

## Contradiction 32

- Seed: `0`
- Start step: `92`
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

## Contradiction 33

- Seed: `0`
- Start step: `107`
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

#### Geography.kif:7150

```lisp
(instance IndianOcean Ocean)
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

## Contradiction 34

- Seed: `0`
- Start step: `107`
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

#### Geography.kif:7136

```lisp
(instance SouthPacificOcean BodyOfWater)
```

#### Geography.kif:7135

```lisp
(instance SouthPacificOcean SaltWaterArea)
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

## Contradiction 35

- Seed: `0`
- Start step: `107`
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

#### Geography.kif:7150

```lisp
(instance IndianOcean Ocean)
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

## Contradiction 36

- Seed: `0`
- Start step: `111`
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

## Contradiction 37

- Seed: `0`
- Start step: `122`
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

## Contradiction 38

- Seed: `0`
- Start step: `122`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `13`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Mid-level-ontology.kif:35137

```lisp
(subclass MobileCellPhone Telephone)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
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

#### Mid-level-ontology.kif:4558

```lisp
(subclass CommunicationDevice EngineeringComponent)
```

## Contradiction 39

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `24`

### Cited source axioms

#### Merge.kif:259

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:253

```lisp
(=> (and (subrelation ?REL1 ?REL2) (domainSubclass ?REL2 ?NUMBER ?CLASS1)) (domainSubclass ?REL1 ?NUMBER ?CLASS1))
```

#### Mid-level-ontology.kif:33370

```lisp
(domainSubclass typicalPart 1 Physical)
```

#### Mid-level-ontology.kif:33526

```lisp
(subrelation partTypes typicalPart)
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

## Contradiction 40

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `24`

### Cited source axioms

#### Merge.kif:259

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:253

```lisp
(=> (and (subrelation ?REL1 ?REL2) (domainSubclass ?REL2 ?NUMBER ?CLASS1)) (domainSubclass ?REL1 ?NUMBER ?CLASS1))
```

#### Mid-level-ontology.kif:33526

```lisp
(subrelation partTypes typicalPart)
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

## Contradiction 41

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `26`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:195

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))
```

#### Merge.kif:5534

```lisp
(domain represents 2 Entity)
```

#### Mid-level-ontology.kif:20302

```lisp
(subrelation record represents)
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

## Contradiction 42

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:9422

```lisp
(domain measure 1 Physical)
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

## Contradiction 43

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:6862

```lisp
(domain KappaFn 1 Entity)
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

## Contradiction 44

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Mid-level-ontology.kif:20320

```lisp
(domain record 2 Physical)
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

## Contradiction 45

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:685

```lisp
(domain relatedInternalConcept 1 Entity)
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

## Contradiction 46

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:4709

```lisp
(domain causes 1 Process)
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

## Contradiction 47

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:5534

```lisp
(domain represents 2 Entity)
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

## Contradiction 48

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Mid-level-ontology.kif:38244

```lisp
(domain conventionalShortName 2 Entity)
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

## Contradiction 49

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3165

```lisp
(domain destination 2 Entity)
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

## Contradiction 50

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Mid-level-ontology.kif:38229

```lisp
(domain conventionalLongName 2 Entity)
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

## Contradiction 51

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `26`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:195

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))
```

#### Merge.kif:5484

```lisp
(domain refers 1 Entity)
```

#### Merge.kif:5500

```lisp
(subrelation names refers)
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

## Contradiction 52

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3181

```lisp
(domain experiencer 1 Process)
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

## Contradiction 53

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `13`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:14499

```lisp
(domain objectTransferred 1 Transfer)
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

## Contradiction 54

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:4677

```lisp
(domain subProcess 1 Process)
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

## Contradiction 55

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3952

```lisp
(domain inList 1 Entity)
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

## Contradiction 56

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `28`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:195

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))
```

#### Economy.kif:53

```lisp
(subrelation economyType attribute)
```

#### Merge.kif:2251

```lisp
(domain property 1 Entity)
```

#### Merge.kif:2264

```lisp
(subrelation attribute property)
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

## Contradiction 57

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:397

```lisp
(domain documentation 1 Entity)
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

## Contradiction 58

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:764

```lisp
(domain externalImage 1 Entity)
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

## Contradiction 59

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3211

```lisp
(domain origin 1 Process)
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

## Contradiction 60

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:5484

```lisp
(domain refers 1 Entity)
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

## Contradiction 61

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `26`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:195

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))
```

#### Merge.kif:3243

```lisp
(subrelation resource patient)
```

#### Merge.kif:3228

```lisp
(domain patient 2 Entity)
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

## Contradiction 62

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3228

```lisp
(domain patient 2 Entity)
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

## Contradiction 63

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### engineering.kif:39

```lisp
(domain lexicon 1 Entity)
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

## Contradiction 64

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:9504

```lisp
(domain length 1 Physical)
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

## Contradiction 65

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `26`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:195

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))
```

#### Merge.kif:5533

```lisp
(domain represents 1 Entity)
```

#### Merge.kif:5700

```lisp
(subrelation realization represents)
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
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:5485

```lisp
(domain refers 2 Entity)
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

## Contradiction 67

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `26`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:195

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))
```

#### Merge.kif:2251

```lisp
(domain property 1 Entity)
```

#### Merge.kif:22364

```lisp
(subrelation modalAttribute property)
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

## Contradiction 68

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `17`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:14129

```lisp
(domain path 1 Motion)
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

## Contradiction 69

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3292

```lisp
(domain result 1 Process)
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

## Contradiction 70

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `26`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:195

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))
```

#### Merge.kif:3194

```lisp
(subrelation instrument patient)
```

#### Merge.kif:3228

```lisp
(domain patient 2 Entity)
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

## Contradiction 71

- Seed: `0`
- Start step: `132`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:1566

```lisp
(domain member 1 Physical)
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

## Contradiction 72

- Seed: `0`
- Start step: `139`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `11`

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

#### Merge.kif:2804

```lisp
(partition SetOrClass Set Class)
```

## Contradiction 73

- Seed: `0`
- Start step: `142`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:10291

```lisp
(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:10273

```lisp
(instance beforeOrEqual BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:10276

```lisp
(domain beforeOrEqual 1 TimePoint)
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
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

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2754

```lisp
(subclass TimePoint TimePosition)
```

#### Merge.kif:2735

```lisp
(subclass TimePosition TimeMeasure)
```

#### Merge.kif:2718

```lisp
(subclass TimeMeasure ConstantQuantity)
```

#### Merge.kif:2693

```lisp
(subclass ConstantQuantity PhysicalQuantity)
```

#### Merge.kif:2670

```lisp
(subclass PhysicalQuantity FiniteQuantity)
```

#### Merge.kif:2406

```lisp
(subclass FiniteQuantity Quantity)
```

#### Merge.kif:2230

```lisp
(subclass Quantity Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 74

- Seed: `0`
- Start step: `142`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:10291

```lisp
(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:10273

```lisp
(instance beforeOrEqual BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:10277

```lisp
(domain beforeOrEqual 2 TimePoint)
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
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

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2754

```lisp
(subclass TimePoint TimePosition)
```

#### Merge.kif:2735

```lisp
(subclass TimePosition TimeMeasure)
```

#### Merge.kif:2718

```lisp
(subclass TimeMeasure ConstantQuantity)
```

#### Merge.kif:2693

```lisp
(subclass ConstantQuantity PhysicalQuantity)
```

#### Merge.kif:2670

```lisp
(subclass PhysicalQuantity FiniteQuantity)
```

#### Merge.kif:2406

```lisp
(subclass FiniteQuantity Quantity)
```

#### Merge.kif:2230

```lisp
(subclass Quantity Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 75

- Seed: `0`
- Start step: `142`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:10291

```lisp
(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:10273

```lisp
(instance beforeOrEqual BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:10276

```lisp
(domain beforeOrEqual 1 TimePoint)
```

#### CountriesAndRegions.kif:2181

```lisp
(instance NewYorkCityUnitedStates AmericanCity)
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

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2754

```lisp
(subclass TimePoint TimePosition)
```

#### Merge.kif:2735

```lisp
(subclass TimePosition TimeMeasure)
```

#### Merge.kif:2718

```lisp
(subclass TimeMeasure ConstantQuantity)
```

#### Merge.kif:2693

```lisp
(subclass ConstantQuantity PhysicalQuantity)
```

#### Merge.kif:2670

```lisp
(subclass PhysicalQuantity FiniteQuantity)
```

#### Merge.kif:2406

```lisp
(subclass FiniteQuantity Quantity)
```

#### Merge.kif:2230

```lisp
(subclass Quantity Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 76

- Seed: `0`
- Start step: `142`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:10291

```lisp
(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:10273

```lisp
(instance beforeOrEqual BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:10277

```lisp
(domain beforeOrEqual 2 TimePoint)
```

#### CountriesAndRegions.kif:2181

```lisp
(instance NewYorkCityUnitedStates AmericanCity)
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

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2754

```lisp
(subclass TimePoint TimePosition)
```

#### Merge.kif:2735

```lisp
(subclass TimePosition TimeMeasure)
```

#### Merge.kif:2718

```lisp
(subclass TimeMeasure ConstantQuantity)
```

#### Merge.kif:2693

```lisp
(subclass ConstantQuantity PhysicalQuantity)
```

#### Merge.kif:2670

```lisp
(subclass PhysicalQuantity FiniteQuantity)
```

#### Merge.kif:2406

```lisp
(subclass FiniteQuantity Quantity)
```

#### Merge.kif:2230

```lisp
(subclass Quantity Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 77

- Seed: `0`
- Start step: `142`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `27`

### Cited source axioms

#### Merge.kif:10291

```lisp
(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:10273

```lisp
(instance beforeOrEqual BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:10277

```lisp
(domain beforeOrEqual 2 TimePoint)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:2754

```lisp
(subclass TimePoint TimePosition)
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
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

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2735

```lisp
(subclass TimePosition TimeMeasure)
```

#### Merge.kif:2718

```lisp
(subclass TimeMeasure ConstantQuantity)
```

#### Merge.kif:2693

```lisp
(subclass ConstantQuantity PhysicalQuantity)
```

#### Merge.kif:2670

```lisp
(subclass PhysicalQuantity FiniteQuantity)
```

#### Merge.kif:2406

```lisp
(subclass FiniteQuantity Quantity)
```

#### Merge.kif:2230

```lisp
(subclass Quantity Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 78

- Seed: `0`
- Start step: `142`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `27`

### Cited source axioms

#### Merge.kif:10291

```lisp
(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:10273

```lisp
(instance beforeOrEqual BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:10277

```lisp
(domain beforeOrEqual 2 TimePoint)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:2754

```lisp
(subclass TimePoint TimePosition)
```

#### CountriesAndRegions.kif:2181

```lisp
(instance NewYorkCityUnitedStates AmericanCity)
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

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2735

```lisp
(subclass TimePosition TimeMeasure)
```

#### Merge.kif:2718

```lisp
(subclass TimeMeasure ConstantQuantity)
```

#### Merge.kif:2693

```lisp
(subclass ConstantQuantity PhysicalQuantity)
```

#### Merge.kif:2670

```lisp
(subclass PhysicalQuantity FiniteQuantity)
```

#### Merge.kif:2406

```lisp
(subclass FiniteQuantity Quantity)
```

#### Merge.kif:2230

```lisp
(subclass Quantity Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 79

- Seed: `0`
- Start step: `142`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `27`

### Cited source axioms

#### Merge.kif:10291

```lisp
(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:10273

```lisp
(instance beforeOrEqual BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:10276

```lisp
(domain beforeOrEqual 1 TimePoint)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:2754

```lisp
(subclass TimePoint TimePosition)
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
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

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2735

```lisp
(subclass TimePosition TimeMeasure)
```

#### Merge.kif:2718

```lisp
(subclass TimeMeasure ConstantQuantity)
```

#### Merge.kif:2693

```lisp
(subclass ConstantQuantity PhysicalQuantity)
```

#### Merge.kif:2670

```lisp
(subclass PhysicalQuantity FiniteQuantity)
```

#### Merge.kif:2406

```lisp
(subclass FiniteQuantity Quantity)
```

#### Merge.kif:2230

```lisp
(subclass Quantity Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 80

- Seed: `0`
- Start step: `142`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `27`

### Cited source axioms

#### Merge.kif:10291

```lisp
(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:10273

```lisp
(instance beforeOrEqual BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:10276

```lisp
(domain beforeOrEqual 1 TimePoint)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:2754

```lisp
(subclass TimePoint TimePosition)
```

#### CountriesAndRegions.kif:2181

```lisp
(instance NewYorkCityUnitedStates AmericanCity)
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

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:2735

```lisp
(subclass TimePosition TimeMeasure)
```

#### Merge.kif:2718

```lisp
(subclass TimeMeasure ConstantQuantity)
```

#### Merge.kif:2693

```lisp
(subclass ConstantQuantity PhysicalQuantity)
```

#### Merge.kif:2670

```lisp
(subclass PhysicalQuantity FiniteQuantity)
```

#### Merge.kif:2406

```lisp
(subclass FiniteQuantity Quantity)
```

#### Merge.kif:2230

```lisp
(subclass Quantity Abstract)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 81

- Seed: `0`
- Start step: `160`
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

## Contradiction 82

- Seed: `0`
- Start step: `160`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `11`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:4409

```lisp
(subclass TernaryPredicate Predicate)
```

#### Merge.kif:410

```lisp
(instance format TernaryPredicate)
```

#### Merge.kif:12109

```lisp
(=> (equal (TemporalCompositionFn ?INTERVAL ?INTERVALTYPE) ?CLASS) (forall (?TIME1 ?TIME2) (=> (and (instance ?TIME1 ?INTERVALTYPE) (instance ?TIME2 ?CLASS)) (exists (?DURATION) (and (duration ?TIME1 ?DURATION) (duration ?TIME2 ?DURATION))))))
```

#### Merge.kif:12139

```lisp
(=> (equal (TemporalCompositionFn ?INTERVAL ?INTERVALTYPE) ?CLASS) (exists (?TIME) (and (instance ?TIME ?CLASS) (starts ?TIME ?INTERVAL))))
```

## Contradiction 83

- Seed: `0`
- Start step: `160`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `11`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:2969

```lisp
(subclass AsymmetricRelation IrreflexiveRelation)
```

#### Geography.kif:762

```lisp
(instance tangentialProperPart AsymmetricRelation)
```

#### Merge.kif:12109

```lisp
(=> (equal (TemporalCompositionFn ?INTERVAL ?INTERVALTYPE) ?CLASS) (forall (?TIME1 ?TIME2) (=> (and (instance ?TIME1 ?INTERVALTYPE) (instance ?TIME2 ?CLASS)) (exists (?DURATION) (and (duration ?TIME1 ?DURATION) (duration ?TIME2 ?DURATION))))))
```

#### Merge.kif:12139

```lisp
(=> (equal (TemporalCompositionFn ?INTERVAL ?INTERVALTYPE) ?CLASS) (exists (?TIME) (and (instance ?TIME ?CLASS) (starts ?TIME ?INTERVAL))))
```

## Contradiction 84

- Seed: `0`
- Start step: `161`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `14`

### Cited source axioms

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Mid-level-ontology.kif:3017

```lisp
(subclass ReceiverDevice CommunicationDevice)
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

#### Mid-level-ontology.kif:35136

```lisp
(subclass MobileCellPhone ReceiverDevice)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

## Contradiction 85

- Seed: `0`
- Start step: `166`
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

## Contradiction 86

- Seed: `0`
- Start step: `166`
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

## Contradiction 87

- Seed: `0`
- Start step: `178`
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

#### WMD.kif:537

```lisp
(biochemicalAgentDelivery NerveAgent Breathing)
```

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

## Contradiction 88

- Seed: `0`
- Start step: `194`
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

## Contradiction 89

- Seed: `0`
- Start step: `194`
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

## Contradiction 90

- Seed: `0`
- Start step: `194`
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

## Contradiction 91

- Seed: `0`
- Start step: `194`
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

## Contradiction 92

- Seed: `0`
- Start step: `198`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `39`

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

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### Mid-level-ontology.kif:44807

```lisp
(domainSubclass roomTempState 1 Substance)
```

#### Mid-level-ontology.kif:44771

```lisp
(roomTempState Alcohol Liquid)
```

#### Mid-level-ontology.kif:44812

```lisp
(instance roomTempState BinaryPredicate)
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

## Contradiction 93

- Seed: `0`
- Start step: `198`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `41`

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

#### Merge.kif:3839

```lisp
(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))
```

#### Mid-level-ontology.kif:44807

```lisp
(domainSubclass roomTempState 1 Substance)
```

#### Mid-level-ontology.kif:44771

```lisp
(roomTempState Alcohol Liquid)
```

#### Mid-level-ontology.kif:44812

```lisp
(instance roomTempState BinaryPredicate)
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

#### Merge.kif:13075

```lisp
(subclass Breathing OrganismProcess)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
```

#### Merge.kif:2120

```lisp
(subclass Process Physical)
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

## Contradiction 94

- Seed: `0`
- Start step: `238`
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

#### Merge.kif:20774

```lisp
(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Mid-level-ontology.kif:3017

```lisp
(subclass ReceiverDevice CommunicationDevice)
```

#### Mid-level-ontology.kif:35136

```lisp
(subclass MobileCellPhone ReceiverDevice)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

## Contradiction 95

- Seed: `0`
- Start step: `261`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `12`

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

#### engineering.kif:1180

```lisp
(subclass Faucet FluidPowerDevice)
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### engineering.kif:1184

```lisp
(typicalPart Faucet Bathroom)
```

#### engineering.kif:733

```lisp
(subclass FluidPowerDevice EngineeringComponent)
```

## Contradiction 96

- Seed: `0`
- Start step: `261`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `12`

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

#### engineering.kif:1180

```lisp
(subclass Faucet FluidPowerDevice)
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### engineering.kif:1183

```lisp
(typicalPart Faucet Kitchen)
```

#### engineering.kif:733

```lisp
(subclass FluidPowerDevice EngineeringComponent)
```

## Contradiction 97

- Seed: `0`
- Start step: `261`
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

#### engineering.kif:1181

```lisp
(partTypes Valve Faucet)
```

#### engineering.kif:1163

```lisp
(subclass Valve EngineeringComponent)
```

## Contradiction 98

- Seed: `0`
- Start step: `261`
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

## Contradiction 99

- Seed: `0`
- Start step: `261`
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

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### Mid-level-ontology.kif:33526

```lisp
(subrelation partTypes typicalPart)
```

#### engineering.kif:1181

```lisp
(partTypes Valve Faucet)
```

#### engineering.kif:1180

```lisp
(subclass Faucet FluidPowerDevice)
```

#### engineering.kif:733

```lisp
(subclass FluidPowerDevice EngineeringComponent)
```

## Contradiction 100

- Seed: `0`
- Start step: `261`
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

#### engineering.kif:733

```lisp
(subclass FluidPowerDevice EngineeringComponent)
```

#### Mid-level-ontology.kif:33373

```lisp
(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))
```

#### Mid-level-ontology.kif:33526

```lisp
(subrelation partTypes typicalPart)
```

#### engineering.kif:1181

```lisp
(partTypes Valve Faucet)
```

#### engineering.kif:1164

```lisp
(subclass Valve FluidPowerDevice)
```

## Contradiction 101

- Seed: `0`
- Start step: `261`
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

#### engineering.kif:733

```lisp
(subclass FluidPowerDevice EngineeringComponent)
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

#### engineering.kif:1164

```lisp
(subclass Valve FluidPowerDevice)
```

## Contradiction 102

- Seed: `0`
- Start step: `282`
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

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

## Contradiction 103

- Seed: `0`
- Start step: `282`
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

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

## Contradiction 104

- Seed: `0`
- Start step: `282`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `20`

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

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

## Contradiction 105

- Seed: `0`
- Start step: `282`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `10`

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

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

## Contradiction 106

- Seed: `0`
- Start step: `282`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `13`

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

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:14696

```lisp
(subclass Touching Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

## Contradiction 107

- Seed: `0`
- Start step: `282`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `15`

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

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
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

## Contradiction 108

- Seed: `0`
- Start step: `321`
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

#### Cars.kif:257

```lisp
(typicallyContainsPart Crankshaft Crankcase)
```

## Contradiction 109

- Seed: `0`
- Start step: `321`
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

#### Cars.kif:256

```lisp
(typicalPart Crankshaft Crankcase)
```

## Contradiction 110

- Seed: `0`
- Start step: `321`
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

#### Cars.kif:256

```lisp
(typicalPart Crankshaft Crankcase)
```

#### Cars.kif:251

```lisp
(subclass Crankshaft Shaft)
```

## Contradiction 111

- Seed: `0`
- Start step: `321`
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

#### Cars.kif:257

```lisp
(typicallyContainsPart Crankshaft Crankcase)
```

#### Cars.kif:251

```lisp
(subclass Crankshaft Shaft)
```

## Contradiction 112

- Seed: `0`
- Start step: `341`
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

## Contradiction 113

- Seed: `0`
- Start step: `341`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `8`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1429

```lisp
(biochemicalAgentDelivery VibrioCholera Ingesting)
```

#### Merge.kif:13109

```lisp
(subclass Ingesting Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

## Contradiction 114

- Seed: `0`
- Start step: `341`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `22`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1429

```lisp
(biochemicalAgentDelivery VibrioCholera Ingesting)
```

#### Merge.kif:13109

```lisp
(subclass Ingesting Transfer)
```

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:195

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))
```

#### Merge.kif:14498

```lisp
(subrelation objectTransferred patient)
```

#### Merge.kif:3227

```lisp
(domain patient 1 Process)
```

#### Merge.kif:14499

```lisp
(domain objectTransferred 1 Transfer)
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

## Contradiction 115

- Seed: `0`
- Start step: `341`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `20`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1429

```lisp
(biochemicalAgentDelivery VibrioCholera Ingesting)
```

#### Merge.kif:13109

```lisp
(subclass Ingesting Transfer)
```

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:195

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))
```

#### Merge.kif:14498

```lisp
(subrelation objectTransferred patient)
```

#### Merge.kif:3227

```lisp
(domain patient 1 Process)
```

#### Merge.kif:14499

```lisp
(domain objectTransferred 1 Transfer)
```

#### Merge.kif:13107

```lisp
(subclass Ingesting Consuming)
```

#### Merge.kif:13086

```lisp
(subclass Consuming Decreasing)
```

#### Merge.kif:13963

```lisp
(subclass Decreasing QuantityChange)
```

#### Merge.kif:13877

```lisp
(subclass QuantityChange InternalChange)
```

#### Merge.kif:16162

```lisp
(subclass InternalChange Process)
```

## Contradiction 116

- Seed: `0`
- Start step: `341`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `11`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1429

```lisp
(biochemicalAgentDelivery VibrioCholera Ingesting)
```

#### Merge.kif:13109

```lisp
(subclass Ingesting Transfer)
```

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:14499

```lisp
(domain objectTransferred 1 Transfer)
```

## Contradiction 117

- Seed: `0`
- Start step: `341`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `14`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3246

```lisp
(domain resource 1 Process)
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

## Contradiction 118

- Seed: `0`
- Start step: `341`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `14`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3246

```lisp
(domain resource 1 Process)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1429

```lisp
(biochemicalAgentDelivery VibrioCholera Ingesting)
```

#### Merge.kif:13107

```lisp
(subclass Ingesting Consuming)
```

#### Merge.kif:13086

```lisp
(subclass Consuming Decreasing)
```

#### Merge.kif:13963

```lisp
(subclass Decreasing QuantityChange)
```

#### Merge.kif:13877

```lisp
(subclass QuantityChange InternalChange)
```

#### Merge.kif:16162

```lisp
(subclass InternalChange Process)
```

## Contradiction 119

- Seed: `0`
- Start step: `341`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `28`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:14129

```lisp
(domain path 1 Motion)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### WMD.kif:1429

```lisp
(biochemicalAgentDelivery VibrioCholera Ingesting)
```

#### Merge.kif:13109

```lisp
(subclass Ingesting Transfer)
```

#### Merge.kif:195

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))
```

#### Merge.kif:14498

```lisp
(subrelation objectTransferred patient)
```

#### Merge.kif:3227

```lisp
(domain patient 1 Process)
```

#### Merge.kif:14499

```lisp
(domain objectTransferred 1 Transfer)
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

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

## Contradiction 120

- Seed: `0`
- Start step: `341`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `12`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:14129

```lisp
(domain path 1 Motion)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1429

```lisp
(biochemicalAgentDelivery VibrioCholera Ingesting)
```

#### Merge.kif:13109

```lisp
(subclass Ingesting Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

## Contradiction 121

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `32`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Mid-level-ontology.kif:20320

```lisp
(domain record 2 Physical)
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

#### Merge.kif:195

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))
```

#### Merge.kif:5534

```lisp
(domain represents 2 Entity)
```

#### Mid-level-ontology.kif:20302

```lisp
(subrelation record represents)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
```

## Contradiction 122

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `24`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:14499

```lisp
(domain objectTransferred 1 Transfer)
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

#### Merge.kif:195

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))
```

#### Merge.kif:14498

```lisp
(subrelation objectTransferred patient)
```

#### Merge.kif:3227

```lisp
(domain patient 1 Process)
```

#### Merge.kif:14063

```lisp
(subclass Motion Process)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

## Contradiction 123

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:4678

```lisp
(domain subProcess 2 Process)
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

## Contradiction 124

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Media.kif:2051

```lisp
(domain codeMapping 3 Entity)
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

## Contradiction 125

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:4710

```lisp
(domain causes 2 Process)
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

## Contradiction 126

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:412

```lisp
(domain format 2 Entity)
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

## Contradiction 127

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Mid-level-ontology.kif:1343

```lisp
(domain dateEstablished 1 Physical)
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

## Contradiction 128

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:686

```lisp
(domain relatedInternalConcept 2 Entity)
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

## Contradiction 129

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3756

```lisp
(domain ListFn 1 Entity)
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

## Contradiction 130

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:10667

```lisp
(domain WhenFn 1 Physical)
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

## Contradiction 131

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:5503

```lisp
(domain names 2 Entity)
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

## Contradiction 132

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:5533

```lisp
(domain represents 1 Entity)
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

## Contradiction 133

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:84

```lisp
(domain instance 1 Entity)
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

## Contradiction 134

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:422

```lisp
(domain termFormat 2 Entity)
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

## Contradiction 135

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3246

```lisp
(domain resource 1 Process)
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

## Contradiction 136

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:9693

```lisp
(domain distance 1 Physical)
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

## Contradiction 137

- Seed: `0`
- Start step: `353`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3227

```lisp
(domain patient 1 Process)
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

## Contradiction 138

- Seed: `0`
- Start step: `374`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `15`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Mid-level-ontology.kif:34555

```lisp
(subclass Telephone TelephonyDevice)
```

#### Mid-level-ontology.kif:35137

```lisp
(subclass MobileCellPhone Telephone)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Mid-level-ontology.kif:34540

```lisp
(subclass TelephonyDevice CommunicationDevice)
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

## Contradiction 139

- Seed: `0`
- Start step: `396`
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

## Contradiction 140

- Seed: `0`
- Start step: `396`
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

## Contradiction 141

- Seed: `0`
- Start step: `396`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `15`

### Cited source axioms

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Communications.kif:41

```lisp
(=> (instance ?SYSTEM TelephoneSystem) (exists (?LINE) (and (instance ?LINE MainTelephoneLine) (engineeringSubcomponent ?LINE ?SYSTEM))))
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

## Contradiction 142

- Seed: `0`
- Start step: `396`
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

## Contradiction 143

- Seed: `0`
- Start step: `396`
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

## Contradiction 144

- Seed: `0`
- Start step: `410`
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

## Contradiction 145

- Seed: `0`
- Start step: `410`
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

## Contradiction 146

- Seed: `0`
- Start step: `410`
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

#### Geography.kif:7071

```lisp
(instance SouthAtlanticOcean BodyOfWater)
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

## Contradiction 147

- Seed: `0`
- Start step: `410`
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

## Contradiction 148

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `18`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
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

#### Geography.kif:1418

```lisp
(geographicSubregion SierraNevada Nevada)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 149

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `18`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
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

#### Geography.kif:1417

```lisp
(geographicSubregion SierraNevada California)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 150

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
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

#### Geography.kif:1418

```lisp
(geographicSubregion SierraNevada Nevada)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 151

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
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

#### Geography.kif:1417

```lisp
(geographicSubregion SierraNevada California)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 152

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `22`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
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

#### Geography.kif:1418

```lisp
(geographicSubregion SierraNevada Nevada)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 153

- Seed: `0`
- Start step: `422`
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

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
```

#### Geography.kif:3774

```lisp
(=> (attribute ?AREA MountainousTerrain) (exists (?MTN) (and (instance ?MTN Mountain) (part ?MTN ?AREA))))
```

#### Geography.kif:3788

```lisp
(=> (instance ?AREA MountainRange) (attribute ?AREA MountainousTerrain))
```

## Contradiction 154

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `18`

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

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 155

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

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

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 156

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `22`

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

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Geography.kif:5692

```lisp
(geographicSubregion NorthAmerica NorthernHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 157

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `22`

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

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Geography.kif:5693

```lisp
(geographicSubregion NorthAmerica WesternHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 158

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `22`

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

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 159

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `25`

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

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
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

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 160

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `24`

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

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Geography.kif:5693

```lisp
(geographicSubregion NorthAmerica WesternHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 161

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `18`

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

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 162

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `20`

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

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 163

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `24`

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

#### Geography.kif:1529

```lisp
(geographicSubregion AndesMountains SouthAmerica)
```

#### Geography.kif:5708

```lisp
(geographicSubregion SouthAmerica WesternHemisphere)
```

#### Geography.kif:5704

```lisp
(instance SouthAmerica Continent)
```

#### Merge.kif:18313

```lisp
(subclass Continent LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 164

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `22`

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

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 165

- Seed: `0`
- Start step: `422`
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

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
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

#### Geography.kif:1529

```lisp
(geographicSubregion AndesMountains SouthAmerica)
```

#### Geography.kif:5708

```lisp
(geographicSubregion SouthAmerica WesternHemisphere)
```

#### Geography.kif:5704

```lisp
(instance SouthAmerica Continent)
```

#### Merge.kif:18313

```lisp
(subclass Continent LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 166

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `18`

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

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 167

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

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

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 168

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `22`

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

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 169

- Seed: `0`
- Start step: `422`
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

## Contradiction 170

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `18`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1373

```lisp
(instance PeninsularRanges MountainRange)
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

#### Geography.kif:1383

```lisp
(geographicSubregion PeninsularRanges California)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 171

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1373

```lisp
(instance PeninsularRanges MountainRange)
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

#### Geography.kif:1383

```lisp
(geographicSubregion PeninsularRanges California)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 172

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `22`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1373

```lisp
(instance PeninsularRanges MountainRange)
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

#### Geography.kif:1383

```lisp
(geographicSubregion PeninsularRanges California)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 173

- Seed: `0`
- Start step: `422`
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

#### Geography.kif:1373

```lisp
(instance PeninsularRanges MountainRange)
```

#### Geography.kif:3774

```lisp
(=> (attribute ?AREA MountainousTerrain) (exists (?MTN) (and (instance ?MTN Mountain) (part ?MTN ?AREA))))
```

#### Geography.kif:3788

```lisp
(=> (instance ?AREA MountainRange) (attribute ?AREA MountainousTerrain))
```

## Contradiction 174

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `18`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1357

```lisp
(instance TransverseRanges MountainRange)
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

#### Geography.kif:1363

```lisp
(geographicSubregion TransverseRanges California)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 175

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1357

```lisp
(instance TransverseRanges MountainRange)
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

#### Geography.kif:1363

```lisp
(geographicSubregion TransverseRanges California)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 176

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `22`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1357

```lisp
(instance TransverseRanges MountainRange)
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

#### Geography.kif:1363

```lisp
(geographicSubregion TransverseRanges California)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 177

- Seed: `0`
- Start step: `422`
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

#### Geography.kif:1357

```lisp
(instance TransverseRanges MountainRange)
```

#### Geography.kif:3774

```lisp
(=> (attribute ?AREA MountainousTerrain) (exists (?MTN) (and (instance ?MTN Mountain) (part ?MTN ?AREA))))
```

#### Geography.kif:3788

```lisp
(=> (instance ?AREA MountainRange) (attribute ?AREA MountainousTerrain))
```

## Contradiction 178

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
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

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:1418

```lisp
(geographicSubregion SierraNevada Nevada)
```

## Contradiction 179

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
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

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:1417

```lisp
(geographicSubregion SierraNevada California)
```

## Contradiction 180

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

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

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
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

## Contradiction 181

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `27`

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

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
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

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

## Contradiction 182

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `27`

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

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
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

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

## Contradiction 183

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `25`

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

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Geography.kif:5693

```lisp
(geographicSubregion NorthAmerica WesternHemisphere)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
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

## Contradiction 184

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

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

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
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

## Contradiction 185

- Seed: `0`
- Start step: `422`
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

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
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

#### Geography.kif:5708

```lisp
(geographicSubregion SouthAmerica WesternHemisphere)
```

#### Geography.kif:5704

```lisp
(instance SouthAmerica Continent)
```

#### Merge.kif:18313

```lisp
(subclass Continent LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

## Contradiction 186

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

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

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
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

## Contradiction 187

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `27`

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

#### Geography.kif:1529

```lisp
(geographicSubregion AndesMountains SouthAmerica)
```

#### Geography.kif:5708

```lisp
(geographicSubregion SouthAmerica WesternHemisphere)
```

#### Geography.kif:5704

```lisp
(instance SouthAmerica Continent)
```

#### Merge.kif:18313

```lisp
(subclass Continent LandArea)
```

#### Merge.kif:18279

```lisp
(subclass LandArea GeographicArea)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
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

## Contradiction 188

- Seed: `0`
- Start step: `422`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `23`

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

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
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

## Contradiction 189

- Seed: `0`
- Start step: `452`
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

## Contradiction 190

- Seed: `0`
- Start step: `452`
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

## Contradiction 191

- Seed: `0`
- Start step: `452`
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

## Contradiction 192

- Seed: `0`
- Start step: `474`
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

## Contradiction 193

- Seed: `0`
- Start step: `474`
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

## Contradiction 194

- Seed: `0`
- Start step: `475`
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

## Contradiction 195

- Seed: `0`
- Start step: `476`
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

## Contradiction 196

- Seed: `0`
- Start step: `476`
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

## Contradiction 197

- Seed: `0`
- Start step: `476`
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

## Contradiction 198

- Seed: `0`
- Start step: `476`
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

## Contradiction 199

- Seed: `0`
- Start step: `499`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `8`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1657

```lisp
(biochemicalAgentDelivery EscherichiaColi0157H7 Ingesting)
```

#### Merge.kif:13109

```lisp
(subclass Ingesting Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

## Contradiction 200

- Seed: `0`
- Start step: `499`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `22`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1657

```lisp
(biochemicalAgentDelivery EscherichiaColi0157H7 Ingesting)
```

#### Merge.kif:13109

```lisp
(subclass Ingesting Transfer)
```

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:195

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))
```

#### Merge.kif:14498

```lisp
(subrelation objectTransferred patient)
```

#### Merge.kif:3227

```lisp
(domain patient 1 Process)
```

#### Merge.kif:14499

```lisp
(domain objectTransferred 1 Transfer)
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

## Contradiction 201

- Seed: `0`
- Start step: `499`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `20`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1657

```lisp
(biochemicalAgentDelivery EscherichiaColi0157H7 Ingesting)
```

#### Merge.kif:13109

```lisp
(subclass Ingesting Transfer)
```

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:195

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))
```

#### Merge.kif:14498

```lisp
(subrelation objectTransferred patient)
```

#### Merge.kif:3227

```lisp
(domain patient 1 Process)
```

#### Merge.kif:14499

```lisp
(domain objectTransferred 1 Transfer)
```

#### Merge.kif:13108

```lisp
(subclass Ingesting OrganismProcess)
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

## Contradiction 202

- Seed: `0`
- Start step: `499`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `11`

### Cited source axioms

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1657

```lisp
(biochemicalAgentDelivery EscherichiaColi0157H7 Ingesting)
```

#### Merge.kif:13109

```lisp
(subclass Ingesting Transfer)
```

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:14499

```lisp
(domain objectTransferred 1 Transfer)
```

## Contradiction 203

- Seed: `0`
- Start step: `499`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `14`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:3246

```lisp
(domain resource 1 Process)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1657

```lisp
(biochemicalAgentDelivery EscherichiaColi0157H7 Ingesting)
```

#### Merge.kif:13108

```lisp
(subclass Ingesting OrganismProcess)
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

## Contradiction 204

- Seed: `0`
- Start step: `499`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `28`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:14129

```lisp
(domain path 1 Motion)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### WMD.kif:1657

```lisp
(biochemicalAgentDelivery EscherichiaColi0157H7 Ingesting)
```

#### Merge.kif:13109

```lisp
(subclass Ingesting Transfer)
```

#### Merge.kif:195

```lisp
(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))
```

#### Merge.kif:14498

```lisp
(subrelation objectTransferred patient)
```

#### Merge.kif:3227

```lisp
(domain patient 1 Process)
```

#### Merge.kif:14499

```lisp
(domain objectTransferred 1 Transfer)
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

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

## Contradiction 205

- Seed: `0`
- Start step: `499`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `12`

### Cited source axioms

#### Merge.kif:233

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:14129

```lisp
(domain path 1 Motion)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:1657

```lisp
(biochemicalAgentDelivery EscherichiaColi0157H7 Ingesting)
```

#### Merge.kif:13109

```lisp
(subclass Ingesting Transfer)
```

#### Merge.kif:14457

```lisp
(subclass Transfer Translocation)
```

#### Merge.kif:14800

```lisp
(subclass Translocation Motion)
```

## Contradiction 206

- Seed: `0`
- Start step: `550`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `21`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
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

#### Geography.kif:1484

```lisp
(geographicSubregion MountWhitney SierraNevada)
```

#### Geography.kif:1478

```lisp
(instance MountWhitney Mountain)
```

#### Geography.kif:6449

```lisp
(subclass Mountain LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 207

- Seed: `0`
- Start step: `550`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `22`

### Cited source axioms

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
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

#### Geography.kif:1484

```lisp
(geographicSubregion MountWhitney SierraNevada)
```

#### Geography.kif:1478

```lisp
(instance MountWhitney Mountain)
```

#### Geography.kif:6449

```lisp
(subclass Mountain LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
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

## Contradiction 208

- Seed: `0`
- Start step: `550`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `33`

### Cited source axioms

#### CountriesAndRegions.kif:25

```lisp
(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Merge.kif:5075

```lisp
(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
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

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Geography.kif:1417

```lisp
(geographicSubregion SierraNevada California)
```

#### Merge.kif:18145

```lisp
(subrelation geographicSubregion properPart)
```

#### Merge.kif:1063

```lisp
(subrelation properPart part)
```

## Contradiction 209

- Seed: `0`
- Start step: `550`
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

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
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

#### Geography.kif:1418

```lisp
(geographicSubregion SierraNevada Nevada)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 210

- Seed: `0`
- Start step: `550`
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

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
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

#### Geography.kif:1484

```lisp
(geographicSubregion MountWhitney SierraNevada)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6449

```lisp
(subclass Mountain LandForm)
```

#### Geography.kif:1478

```lisp
(instance MountWhitney Mountain)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 211

- Seed: `0`
- Start step: `550`
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

#### Geography.kif:343

```lisp
(instance RockyMountains MountainRange)
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

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 212

- Seed: `0`
- Start step: `550`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `45`

### Cited source axioms

#### Geography.kif:2304

```lisp
(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))
```

#### Geography.kif:1418

```lisp
(geographicSubregion SierraNevada Nevada)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:1484

```lisp
(geographicSubregion MountWhitney SierraNevada)
```

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

#### Geography.kif:6449

```lisp
(subclass Mountain LandForm)
```

#### Geography.kif:1478

```lisp
(instance MountWhitney Mountain)
```

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Geography.kif:1485

```lisp
(geographicSubregion MountWhitney California)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

## Contradiction 213

- Seed: `0`
- Start step: `550`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `63`

### Cited source axioms

#### CountriesAndRegions.kif:25

```lisp
(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Geography.kif:2311

```lisp
(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))
```

#### Merge.kif:12269

```lisp
(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

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

#### Merge.kif:5045

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
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

#### Geography.kif:1418

```lisp
(geographicSubregion SierraNevada Nevada)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
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

#### Geography.kif:1417

```lisp
(geographicSubregion SierraNevada California)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### CountriesAndRegions.kif:835

```lisp
(part LosAngelesCalifornia California)
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Merge.kif:12259

```lisp
(instance connected SymmetricRelation)
```

## Contradiction 214

- Seed: `0`
- Start step: `550`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `81`

### Cited source axioms

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

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### Geography.kif:6439

```lisp
(=> (and (instance ?Range MountainRange) (part ?Mountain1 ?Range)) (exists (?Mountain2) (and (component ?Mountain2 ?Range) (instance ?Mountain2 Mountain) (meetsSpatially ?Mountain1 ?Mountain2))))
```

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
```

#### Merge.kif:12350

```lisp
(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))
```

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

#### Geography.kif:1418

```lisp
(geographicSubregion SierraNevada Nevada)
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
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

#### Geography.kif:1417

```lisp
(geographicSubregion SierraNevada California)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### Merge.kif:18360

```lisp
(subclass Nation LandArea)
```

#### CountriesAndRegions.kif:419

```lisp
(instance UnitedStates Nation)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

#### CountriesAndRegions.kif:39

```lisp
(=> (instance ?CITY AmericanCity) (part ?CITY UnitedStates))
```

#### CountriesAndRegions.kif:834

```lisp
(instance LosAngelesCalifornia AmericanCity)
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
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

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:18359

```lisp
(subclass Nation GeopoliticalArea)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

## Contradiction 215

- Seed: `0`
- Start step: `550`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `104`

### Cited source axioms

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

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:146

```lisp
(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))
```

#### Geography.kif:6432

```lisp
(subclass MountainRange LandForm)
```

#### Merge.kif:18156

```lisp
(subclass LandForm GeographicArea)
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
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

#### Geography.kif:350

```lisp
(geographicSubregion RockyMountains NorthAmerica)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:79

```lisp
(instance NorthAmerica GeographicArea)
```

#### CountriesAndRegions.kif:25

```lisp
(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))
```

#### CountriesAndRegions.kif:929

```lisp
(instance California AmericanState)
```

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
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

#### Geography.kif:1411

```lisp
(instance SierraNevada MountainRange)
```

#### Merge.kif:5051

```lisp
(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))
```

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

#### Geography.kif:1418

```lisp
(geographicSubregion SierraNevada Nevada)
```

#### Geography.kif:1417

```lisp
(geographicSubregion SierraNevada California)
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

#### Merge.kif:18165

```lisp
(subclass GeopoliticalArea AutonomousAgent)
```

#### Merge.kif:18359

```lisp
(subclass Nation GeopoliticalArea)
```

#### Merge.kif:1999

```lisp
(subclass AutonomousAgent Object)
```

#### CountriesAndRegions.kif:418

```lisp
(geographicSubregion UnitedStates NorthAmerica)
```

#### Merge.kif:18145

```lisp
(subrelation geographicSubregion properPart)
```

#### Merge.kif:1063

```lisp
(subrelation properPart part)
```

## Contradiction 216

- Seed: `0`
- Start step: `560`
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

## Contradiction 217

- Seed: `0`
- Start step: `560`
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

#### WMD.kif:1662

```lisp
(biochemicalAgentDelivery MycobacteriumTuberculosis Breathing)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

#### Merge.kif:925

```lisp
(=> (instance ?CLASS Class) (subclass ?CLASS Entity))
```

## Contradiction 218

- Seed: `0`
- Start step: `560`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `13`

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

#### WMD.kif:1662

```lisp
(biochemicalAgentDelivery MycobacteriumTuberculosis Breathing)
```

#### WMD.kif:760

```lisp
(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))
```

#### WMD.kif:177

```lisp
(biochemicalAgentDelivery BacterialAgent Breathing)
```

## Contradiction 219

- Seed: `0`
- Start step: `560`
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

## Contradiction 220

- Seed: `0`
- Start step: `560`
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

## Contradiction 221

- Seed: `0`
- Start step: `560`
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

## Contradiction 222

- Seed: `0`
- Start step: `573`
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

## Contradiction 223

- Seed: `0`
- Start step: `573`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `18`

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

#### Military.kif:822

```lisp
(instance USMilitaryRankWO2 USMilitaryRank)
```

#### Military.kif:493

```lisp
(subclass USMilitaryRank MilitaryRank)
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

## Contradiction 224

- Seed: `0`
- Start step: `573`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `15`

### Cited source axioms

#### Merge.kif:786

```lisp
(=> (and (subAttribute ?ATTR1 ?ATTR2) (instance ?ATTR2 ?CLASS)) (instance ?ATTR1 ?CLASS))
```

#### MilitaryProcesses.kif:916

```lisp
(subAttribute DirectorJS MilitaryCommander)
```

#### Cellular&TelephoneArchitecture.kif:1161

```lisp
(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))
```

#### MilitaryProcesses.kif:915

```lisp
(instance DirectorJS Position)
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

## Contradiction 225

- Seed: `0`
- Start step: `573`
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

## Contradiction 226

- Seed: `0`
- Start step: `573`
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

## Contradiction 227

- Seed: `0`
- Start step: `573`
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

## Contradiction 228

- Seed: `0`
- Start step: `583`
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

## Contradiction 229

- Seed: `0`
- Start step: `596`
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

## Contradiction 230

- Seed: `0`
- Start step: `596`
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

## Replay metadata

```sigma-audit-replay
{
  "version": 1,
  "complete": true,
  "sumo_commit": "8d86020fc77e46353ad66167ea6ba3f66c161162",
  "run_id": "36930514293",
  "run_attempt": 1,
  "engine": {
    "commit": "7a2994b7d779c9074c1d46c0c647ff5e3b76517a",
    "fingerprint": "89d63d28e814e6044efaac7baa2f5f6770c3252a9bc3d4752ef46ba3f4895288"
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
      "step": 9,
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
      "step": 9,
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
      "step": 13,
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
      "step": 13,
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
      "step": 13,
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
      "step": 13,
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
      "step": 13,
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
      "step": 13,
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
      "step": 13,
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
      "step": 13,
      "proof_steps": 24,
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
      "step": 13,
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
      "step": 13,
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
      "step": 13,
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
      "step": 13,
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
      "step": 13,
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
      "step": 13,
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
      "step": 13,
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
      "step": 13,
      "proof_steps": 40,
      "axioms": [
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
          "kif": "(domain subclass 1 Class)",
          "line": 137
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
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
      "step": 13,
      "proof_steps": 39,
      "axioms": [
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
      "step": 25,
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
          "file": "engineering.kif",
          "kif": "(typicalPart Shaft Motor)",
          "line": 869
        }
      ]
    },
    {
      "seed": 0,
      "step": 25,
      "proof_steps": 12,
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
          "kif": "(=> (instance ?MACHINE Machine) (exists (?COMP1 ?COMP2) (and (instance ?COMP1 EngineeringComponent) (instance ?COMP2 EngineeringComponent) (not (equal ?COMP1 ?COMP2)) (part ?COMP1 ?MACHINE) (part ?COMP2 ?MACHINE))))",
          "line": 20781
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
          "file": "engineering.kif",
          "kif": "(typicalPart Shaft Motor)",
          "line": 869
        },
        {
          "file": "engineering.kif",
          "kif": "(subclass Motor Machine)",
          "line": 738
        }
      ]
    },
    {
      "seed": 0,
      "step": 31,
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
      "step": 86,
      "proof_steps": 5,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery HepatitisAVirus Ingesting)",
          "line": 1726
        }
      ]
    },
    {
      "seed": 0,
      "step": 86,
      "proof_steps": 8,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery HepatitisAVirus Ingesting)",
          "line": 1726
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Transfer)",
          "line": 13109
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
      "step": 88,
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
      "step": 88,
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
          "kif": "(subclass Breathing OrganismProcess)",
          "line": 13075
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
      "step": 88,
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
      "step": 92,
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
      "step": 92,
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
      "step": 92,
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
      "step": 92,
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
      "step": 92,
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
      "step": 107,
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
          "kif": "(instance IndianOcean Ocean)",
          "line": 7150
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
      "step": 107,
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
          "kif": "(instance SouthPacificOcean BodyOfWater)",
          "line": 7136
        },
        {
          "file": "Geography.kif",
          "kif": "(instance SouthPacificOcean SaltWaterArea)",
          "line": 7135
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
      "step": 107,
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
          "kif": "(instance IndianOcean Ocean)",
          "line": 7150
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
      "step": 111,
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
      "step": 122,
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
      "step": 122,
      "proof_steps": 13,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
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
          "kif": "(subclass CommunicationDevice EngineeringComponent)",
          "line": 4558
        }
      ]
    },
    {
      "seed": 0,
      "step": 132,
      "proof_steps": 24,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?REL1 ?REL2) (domainSubclass ?REL2 ?NUMBER ?CLASS1)) (domainSubclass ?REL1 ?NUMBER ?CLASS1))",
          "line": 253
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(domainSubclass typicalPart 1 Physical)",
          "line": 33370
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subrelation partTypes typicalPart)",
          "line": 33526
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
      "step": 132,
      "proof_steps": 24,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS1) (domainSubclass ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 259
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?REL1 ?REL2) (domainSubclass ?REL2 ?NUMBER ?CLASS1)) (domainSubclass ?REL1 ?NUMBER ?CLASS1))",
          "line": 253
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subrelation partTypes typicalPart)",
          "line": 33526
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
      "step": 132,
      "proof_steps": 26,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))",
          "line": 195
        },
        {
          "file": "Merge.kif",
          "kif": "(domain represents 2 Entity)",
          "line": 5534
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subrelation record represents)",
          "line": 20302
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
      "step": 132,
      "proof_steps": 21,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain measure 1 Physical)",
          "line": 9422
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
      "step": 132,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain KappaFn 1 Entity)",
          "line": 6862
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
      "step": 132,
      "proof_steps": 21,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(domain record 2 Physical)",
          "line": 20320
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
      "step": 132,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain relatedInternalConcept 1 Entity)",
          "line": 685
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
      "step": 132,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain causes 1 Process)",
          "line": 4709
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
      "step": 132,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain represents 2 Entity)",
          "line": 5534
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
      "step": 132,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(domain conventionalShortName 2 Entity)",
          "line": 38244
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
      "step": 132,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain destination 2 Entity)",
          "line": 3165
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
      "step": 132,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(domain conventionalLongName 2 Entity)",
          "line": 38229
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
      "step": 132,
      "proof_steps": 26,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))",
          "line": 195
        },
        {
          "file": "Merge.kif",
          "kif": "(domain refers 1 Entity)",
          "line": 5484
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation names refers)",
          "line": 5500
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
      "step": 132,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain experiencer 1 Process)",
          "line": 3181
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
      "step": 132,
      "proof_steps": 13,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain objectTransferred 1 Transfer)",
          "line": 14499
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
        }
      ]
    },
    {
      "seed": 0,
      "step": 132,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subProcess 1 Process)",
          "line": 4677
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
      "step": 132,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain inList 1 Entity)",
          "line": 3952
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
      "step": 132,
      "proof_steps": 28,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))",
          "line": 195
        },
        {
          "file": "Economy.kif",
          "kif": "(subrelation economyType attribute)",
          "line": 53
        },
        {
          "file": "Merge.kif",
          "kif": "(domain property 1 Entity)",
          "line": 2251
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation attribute property)",
          "line": 2264
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
      "step": 132,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain documentation 1 Entity)",
          "line": 397
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
      "step": 132,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain externalImage 1 Entity)",
          "line": 764
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
      "step": 132,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain origin 1 Process)",
          "line": 3211
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
      "step": 132,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain refers 1 Entity)",
          "line": 5484
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
      "step": 132,
      "proof_steps": 26,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))",
          "line": 195
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation resource patient)",
          "line": 3243
        },
        {
          "file": "Merge.kif",
          "kif": "(domain patient 2 Entity)",
          "line": 3228
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
      "step": 132,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain patient 2 Entity)",
          "line": 3228
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
      "step": 132,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "engineering.kif",
          "kif": "(domain lexicon 1 Entity)",
          "line": 39
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
      "step": 132,
      "proof_steps": 21,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain length 1 Physical)",
          "line": 9504
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
      "step": 132,
      "proof_steps": 26,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))",
          "line": 195
        },
        {
          "file": "Merge.kif",
          "kif": "(domain represents 1 Entity)",
          "line": 5533
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation realization represents)",
          "line": 5700
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
      "step": 132,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain refers 2 Entity)",
          "line": 5485
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
      "step": 132,
      "proof_steps": 26,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))",
          "line": 195
        },
        {
          "file": "Merge.kif",
          "kif": "(domain property 1 Entity)",
          "line": 2251
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation modalAttribute property)",
          "line": 22364
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
      "step": 132,
      "proof_steps": 17,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain path 1 Motion)",
          "line": 14129
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
        }
      ]
    },
    {
      "seed": 0,
      "step": 132,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain result 1 Process)",
          "line": 3292
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
      "step": 132,
      "proof_steps": 26,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))",
          "line": 195
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation instrument patient)",
          "line": 3194
        },
        {
          "file": "Merge.kif",
          "kif": "(domain patient 2 Entity)",
          "line": 3228
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
      "step": 132,
      "proof_steps": 21,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain member 1 Physical)",
          "line": 1566
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
      "step": 139,
      "proof_steps": 11,
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
          "file": "Merge.kif",
          "kif": "(partition SetOrClass Set Class)",
          "line": 2804
        }
      ]
    },
    {
      "seed": 0,
      "step": 142,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))",
          "line": 10291
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(instance beforeOrEqual BinaryPredicate)",
          "line": 10273
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(domain beforeOrEqual 1 TimePoint)",
          "line": 10276
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
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
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePoint TimePosition)",
          "line": 2754
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePosition TimeMeasure)",
          "line": 2735
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimeMeasure ConstantQuantity)",
          "line": 2718
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass ConstantQuantity PhysicalQuantity)",
          "line": 2693
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysicalQuantity FiniteQuantity)",
          "line": 2670
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass FiniteQuantity Quantity)",
          "line": 2406
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Quantity Abstract)",
          "line": 2230
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
      "step": 142,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))",
          "line": 10291
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(instance beforeOrEqual BinaryPredicate)",
          "line": 10273
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(domain beforeOrEqual 2 TimePoint)",
          "line": 10277
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
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
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePoint TimePosition)",
          "line": 2754
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePosition TimeMeasure)",
          "line": 2735
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimeMeasure ConstantQuantity)",
          "line": 2718
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass ConstantQuantity PhysicalQuantity)",
          "line": 2693
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysicalQuantity FiniteQuantity)",
          "line": 2670
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass FiniteQuantity Quantity)",
          "line": 2406
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Quantity Abstract)",
          "line": 2230
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
      "step": 142,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))",
          "line": 10291
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(instance beforeOrEqual BinaryPredicate)",
          "line": 10273
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(domain beforeOrEqual 1 TimePoint)",
          "line": 10276
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance NewYorkCityUnitedStates AmericanCity)",
          "line": 2181
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
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePoint TimePosition)",
          "line": 2754
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePosition TimeMeasure)",
          "line": 2735
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimeMeasure ConstantQuantity)",
          "line": 2718
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass ConstantQuantity PhysicalQuantity)",
          "line": 2693
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysicalQuantity FiniteQuantity)",
          "line": 2670
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass FiniteQuantity Quantity)",
          "line": 2406
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Quantity Abstract)",
          "line": 2230
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
      "step": 142,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))",
          "line": 10291
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(instance beforeOrEqual BinaryPredicate)",
          "line": 10273
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(domain beforeOrEqual 2 TimePoint)",
          "line": 10277
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance NewYorkCityUnitedStates AmericanCity)",
          "line": 2181
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
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePoint TimePosition)",
          "line": 2754
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePosition TimeMeasure)",
          "line": 2735
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimeMeasure ConstantQuantity)",
          "line": 2718
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass ConstantQuantity PhysicalQuantity)",
          "line": 2693
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysicalQuantity FiniteQuantity)",
          "line": 2670
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass FiniteQuantity Quantity)",
          "line": 2406
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Quantity Abstract)",
          "line": 2230
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
      "step": 142,
      "proof_steps": 27,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))",
          "line": 10291
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(instance beforeOrEqual BinaryPredicate)",
          "line": 10273
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(domain beforeOrEqual 2 TimePoint)",
          "line": 10277
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePoint TimePosition)",
          "line": 2754
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
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
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePosition TimeMeasure)",
          "line": 2735
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimeMeasure ConstantQuantity)",
          "line": 2718
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass ConstantQuantity PhysicalQuantity)",
          "line": 2693
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysicalQuantity FiniteQuantity)",
          "line": 2670
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass FiniteQuantity Quantity)",
          "line": 2406
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Quantity Abstract)",
          "line": 2230
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
      "step": 142,
      "proof_steps": 27,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))",
          "line": 10291
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(instance beforeOrEqual BinaryPredicate)",
          "line": 10273
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(domain beforeOrEqual 2 TimePoint)",
          "line": 10277
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePoint TimePosition)",
          "line": 2754
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance NewYorkCityUnitedStates AmericanCity)",
          "line": 2181
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
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePosition TimeMeasure)",
          "line": 2735
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimeMeasure ConstantQuantity)",
          "line": 2718
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass ConstantQuantity PhysicalQuantity)",
          "line": 2693
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysicalQuantity FiniteQuantity)",
          "line": 2670
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass FiniteQuantity Quantity)",
          "line": 2406
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Quantity Abstract)",
          "line": 2230
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
      "step": 142,
      "proof_steps": 27,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))",
          "line": 10291
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(instance beforeOrEqual BinaryPredicate)",
          "line": 10273
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(domain beforeOrEqual 1 TimePoint)",
          "line": 10276
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePoint TimePosition)",
          "line": 2754
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance LosAngelesCalifornia AmericanCity)",
          "line": 834
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
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePosition TimeMeasure)",
          "line": 2735
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimeMeasure ConstantQuantity)",
          "line": 2718
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass ConstantQuantity PhysicalQuantity)",
          "line": 2693
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysicalQuantity FiniteQuantity)",
          "line": 2670
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass FiniteQuantity Quantity)",
          "line": 2406
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Quantity Abstract)",
          "line": 2230
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
      "step": 142,
      "proof_steps": 27,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (or (before ?POINT1 ?POINT2) (equal ?POINT1 ?POINT2)) (beforeOrEqual ?POINT1 ?POINT2))",
          "line": 10291
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(instance beforeOrEqual BinaryPredicate)",
          "line": 10273
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(domain beforeOrEqual 1 TimePoint)",
          "line": 10276
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePoint TimePosition)",
          "line": 2754
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance NewYorkCityUnitedStates AmericanCity)",
          "line": 2181
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
          "file": "Merge.kif",
          "kif": "(subclass Object Physical)",
          "line": 946
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimePosition TimeMeasure)",
          "line": 2735
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TimeMeasure ConstantQuantity)",
          "line": 2718
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass ConstantQuantity PhysicalQuantity)",
          "line": 2693
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PhysicalQuantity FiniteQuantity)",
          "line": 2670
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass FiniteQuantity Quantity)",
          "line": 2406
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Quantity Abstract)",
          "line": 2230
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
      "step": 160,
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
      "step": 160,
      "proof_steps": 11,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass TernaryPredicate Predicate)",
          "line": 4409
        },
        {
          "file": "Merge.kif",
          "kif": "(instance format TernaryPredicate)",
          "line": 410
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
      "step": 160,
      "proof_steps": 11,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AsymmetricRelation IrreflexiveRelation)",
          "line": 2969
        },
        {
          "file": "Geography.kif",
          "kif": "(instance tangentialProperPart AsymmetricRelation)",
          "line": 762
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
      "step": 161,
      "proof_steps": 14,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (instance ?COMP EngineeringComponent) (exists (?DEVICE) (and (instance ?DEVICE Device) (component ?COMP ?DEVICE))))",
          "line": 20774
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
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
          "kif": "(subclass ReceiverDevice CommunicationDevice)",
          "line": 3017
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
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass MobileCellPhone ReceiverDevice)",
          "line": 35136
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
      "step": 166,
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
      "step": 166,
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
      "step": 178,
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
          "kif": "(biochemicalAgentDelivery NerveAgent Breathing)",
          "line": 537
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
          "kif": "(biochemicalAgentDelivery BacterialAgent Breathing)",
          "line": 177
        }
      ]
    },
    {
      "seed": 0,
      "step": 194,
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
      "step": 194,
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
      "step": 194,
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
      "step": 194,
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
      "step": 198,
      "proof_steps": 39,
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
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(domainSubclass roomTempState 1 Substance)",
          "line": 44807
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(roomTempState Alcohol Liquid)",
          "line": 44771
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(instance roomTempState BinaryPredicate)",
          "line": 44812
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
      "step": 198,
      "proof_steps": 41,
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
          "kif": "(=> (and (domainSubclass ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (exists (?ARG) (and (equal ?ARG (ListOrderFn (ListFn @ROW) ?NUMBER)) (instance ?ARG Class) (subclass ?ARG ?CLASS))))",
          "line": 3839
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(domainSubclass roomTempState 1 Substance)",
          "line": 44807
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(roomTempState Alcohol Liquid)",
          "line": 44771
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(instance roomTempState BinaryPredicate)",
          "line": 44812
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
          "kif": "(subclass Breathing OrganismProcess)",
          "line": 13075
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
      "step": 238,
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
          "kif": "(subclass ReceiverDevice CommunicationDevice)",
          "line": 3017
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
        }
      ]
    },
    {
      "seed": 0,
      "step": 261,
      "proof_steps": 12,
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
          "kif": "(subclass Faucet FluidPowerDevice)",
          "line": 1180
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))",
          "line": 33373
        },
        {
          "file": "engineering.kif",
          "kif": "(typicalPart Faucet Bathroom)",
          "line": 1184
        },
        {
          "file": "engineering.kif",
          "kif": "(subclass FluidPowerDevice EngineeringComponent)",
          "line": 733
        }
      ]
    },
    {
      "seed": 0,
      "step": 261,
      "proof_steps": 12,
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
          "kif": "(subclass Faucet FluidPowerDevice)",
          "line": 1180
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(=> (typicalPart ?PART ?WHOLE) (exists (?X ?Y) (and (instance ?X ?WHOLE) (instance ?Y ?PART) (part ?Y ?X))))",
          "line": 33373
        },
        {
          "file": "engineering.kif",
          "kif": "(typicalPart Faucet Kitchen)",
          "line": 1183
        },
        {
          "file": "engineering.kif",
          "kif": "(subclass FluidPowerDevice EngineeringComponent)",
          "line": 733
        }
      ]
    },
    {
      "seed": 0,
      "step": 261,
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
          "kif": "(partTypes Valve Faucet)",
          "line": 1181
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
      "step": 261,
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
      "step": 261,
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
          "kif": "(partTypes Valve Faucet)",
          "line": 1181
        },
        {
          "file": "engineering.kif",
          "kif": "(subclass Faucet FluidPowerDevice)",
          "line": 1180
        },
        {
          "file": "engineering.kif",
          "kif": "(subclass FluidPowerDevice EngineeringComponent)",
          "line": 733
        }
      ]
    },
    {
      "seed": 0,
      "step": 261,
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
          "file": "engineering.kif",
          "kif": "(subclass FluidPowerDevice EngineeringComponent)",
          "line": 733
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
          "kif": "(partTypes Valve Faucet)",
          "line": 1181
        },
        {
          "file": "engineering.kif",
          "kif": "(subclass Valve FluidPowerDevice)",
          "line": 1164
        }
      ]
    },
    {
      "seed": 0,
      "step": 261,
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
          "file": "engineering.kif",
          "kif": "(subclass FluidPowerDevice EngineeringComponent)",
          "line": 733
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
          "kif": "(subclass Valve FluidPowerDevice)",
          "line": 1164
        }
      ]
    },
    {
      "seed": 0,
      "step": 282,
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
      "step": 282,
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
      "step": 282,
      "proof_steps": 20,
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
      "step": 282,
      "proof_steps": 10,
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
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
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
      "step": 282,
      "proof_steps": 13,
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
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
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
        }
      ]
    },
    {
      "seed": 0,
      "step": 282,
      "proof_steps": 15,
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
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass PartialOrderingRelation TransitiveRelation)",
          "line": 3074
        },
        {
          "file": "Merge.kif",
          "kif": "(instance subclass PartialOrderingRelation)",
          "line": 136
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
      "step": 321,
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
          "kif": "(typicallyContainsPart Crankshaft Crankcase)",
          "line": 257
        }
      ]
    },
    {
      "seed": 0,
      "step": 321,
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
          "kif": "(typicalPart Crankshaft Crankcase)",
          "line": 256
        }
      ]
    },
    {
      "seed": 0,
      "step": 321,
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
          "kif": "(typicalPart Crankshaft Crankcase)",
          "line": 256
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
      "step": 321,
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
          "kif": "(typicallyContainsPart Crankshaft Crankcase)",
          "line": 257
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
      "step": 341,
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
      "step": 341,
      "proof_steps": 8,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery VibrioCholera Ingesting)",
          "line": 1429
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Transfer)",
          "line": 13109
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
      "step": 341,
      "proof_steps": 22,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery VibrioCholera Ingesting)",
          "line": 1429
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Transfer)",
          "line": 13109
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))",
          "line": 195
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation objectTransferred patient)",
          "line": 14498
        },
        {
          "file": "Merge.kif",
          "kif": "(domain patient 1 Process)",
          "line": 3227
        },
        {
          "file": "Merge.kif",
          "kif": "(domain objectTransferred 1 Transfer)",
          "line": 14499
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
        }
      ]
    },
    {
      "seed": 0,
      "step": 341,
      "proof_steps": 20,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery VibrioCholera Ingesting)",
          "line": 1429
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Transfer)",
          "line": 13109
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))",
          "line": 195
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation objectTransferred patient)",
          "line": 14498
        },
        {
          "file": "Merge.kif",
          "kif": "(domain patient 1 Process)",
          "line": 3227
        },
        {
          "file": "Merge.kif",
          "kif": "(domain objectTransferred 1 Transfer)",
          "line": 14499
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Consuming)",
          "line": 13107
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Consuming Decreasing)",
          "line": 13086
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Decreasing QuantityChange)",
          "line": 13963
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass QuantityChange InternalChange)",
          "line": 13877
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
      "step": 341,
      "proof_steps": 11,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery VibrioCholera Ingesting)",
          "line": 1429
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Transfer)",
          "line": 13109
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain objectTransferred 1 Transfer)",
          "line": 14499
        }
      ]
    },
    {
      "seed": 0,
      "step": 341,
      "proof_steps": 14,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain resource 1 Process)",
          "line": 3246
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
        }
      ]
    },
    {
      "seed": 0,
      "step": 341,
      "proof_steps": 14,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain resource 1 Process)",
          "line": 3246
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery VibrioCholera Ingesting)",
          "line": 1429
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Consuming)",
          "line": 13107
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Consuming Decreasing)",
          "line": 13086
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Decreasing QuantityChange)",
          "line": 13963
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass QuantityChange InternalChange)",
          "line": 13877
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
      "step": 341,
      "proof_steps": 28,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain path 1 Motion)",
          "line": 14129
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
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery VibrioCholera Ingesting)",
          "line": 1429
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Transfer)",
          "line": 13109
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))",
          "line": 195
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation objectTransferred patient)",
          "line": 14498
        },
        {
          "file": "Merge.kif",
          "kif": "(domain patient 1 Process)",
          "line": 3227
        },
        {
          "file": "Merge.kif",
          "kif": "(domain objectTransferred 1 Transfer)",
          "line": 14499
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
      "step": 341,
      "proof_steps": 12,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain path 1 Motion)",
          "line": 14129
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery VibrioCholera Ingesting)",
          "line": 1429
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Transfer)",
          "line": 13109
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
      "step": 353,
      "proof_steps": 32,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(domain record 2 Physical)",
          "line": 20320
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
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))",
          "line": 195
        },
        {
          "file": "Merge.kif",
          "kif": "(domain represents 2 Entity)",
          "line": 5534
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subrelation record represents)",
          "line": 20302
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
      "step": 353,
      "proof_steps": 24,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain objectTransferred 1 Transfer)",
          "line": 14499
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
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))",
          "line": 195
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation objectTransferred patient)",
          "line": 14498
        },
        {
          "file": "Merge.kif",
          "kif": "(domain patient 1 Process)",
          "line": 3227
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Motion Process)",
          "line": 14063
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
      "step": 353,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain subProcess 2 Process)",
          "line": 4678
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
      "step": 353,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Media.kif",
          "kif": "(domain codeMapping 3 Entity)",
          "line": 2051
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
      "step": 353,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain causes 2 Process)",
          "line": 4710
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
      "step": 353,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain format 2 Entity)",
          "line": 412
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
      "step": 353,
      "proof_steps": 21,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(domain dateEstablished 1 Physical)",
          "line": 1343
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
      "step": 353,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain relatedInternalConcept 2 Entity)",
          "line": 686
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
      "step": 353,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain ListFn 1 Entity)",
          "line": 3756
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
      "step": 353,
      "proof_steps": 21,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain WhenFn 1 Physical)",
          "line": 10667
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
      "step": 353,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain names 2 Entity)",
          "line": 5503
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
      "step": 353,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain represents 1 Entity)",
          "line": 5533
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
      "step": 353,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain instance 1 Entity)",
          "line": 84
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
      "step": 353,
      "proof_steps": 23,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain termFormat 2 Entity)",
          "line": 422
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
      "step": 353,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain resource 1 Process)",
          "line": 3246
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
      "step": 353,
      "proof_steps": 21,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain distance 1 Physical)",
          "line": 9693
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
      "step": 353,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain patient 1 Process)",
          "line": 3227
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
      "step": 374,
      "proof_steps": 15,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass Telephone TelephonyDevice)",
          "line": 34555
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
        },
        {
          "file": "Mid-level-ontology.kif",
          "kif": "(subclass TelephonyDevice CommunicationDevice)",
          "line": 34540
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
      "step": 396,
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
      "step": 396,
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
      "step": 396,
      "proof_steps": 15,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Communications.kif",
          "kif": "(=> (instance ?SYSTEM TelephoneSystem) (exists (?LINE) (and (instance ?LINE MainTelephoneLine) (engineeringSubcomponent ?LINE ?SYSTEM))))",
          "line": 41
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
      "step": 396,
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
      "step": 396,
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
      "step": 410,
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
      "step": 410,
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
      "step": 410,
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
          "kif": "(instance SouthAtlanticOcean BodyOfWater)",
          "line": 7071
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
      "step": 410,
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
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 18,
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
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
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
          "kif": "(geographicSubregion SierraNevada Nevada)",
          "line": 1418
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 18,
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
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
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
          "kif": "(geographicSubregion SierraNevada California)",
          "line": 1417
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 21,
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
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
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
          "kif": "(geographicSubregion SierraNevada Nevada)",
          "line": 1418
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 21,
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
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
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
          "kif": "(geographicSubregion SierraNevada California)",
          "line": 1417
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 22,
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
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
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
          "kif": "(geographicSubregion SierraNevada Nevada)",
          "line": 1418
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
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
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
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
      "step": 422,
      "proof_steps": 18,
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
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 21,
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
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 22,
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
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 22,
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
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 22,
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
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 25,
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
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 24,
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
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 18,
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
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 20,
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
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 24,
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
          "file": "Geography.kif",
          "kif": "(geographicSubregion AndesMountains SouthAmerica)",
          "line": 1529
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion SouthAmerica WesternHemisphere)",
          "line": 5708
        },
        {
          "file": "Geography.kif",
          "kif": "(instance SouthAmerica Continent)",
          "line": 5704
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Continent LandArea)",
          "line": 18313
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 22,
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
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
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
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
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
          "file": "Geography.kif",
          "kif": "(geographicSubregion AndesMountains SouthAmerica)",
          "line": 1529
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion SouthAmerica WesternHemisphere)",
          "line": 5708
        },
        {
          "file": "Geography.kif",
          "kif": "(instance SouthAmerica Continent)",
          "line": 5704
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Continent LandArea)",
          "line": 18313
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 18,
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
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 21,
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
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 22,
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
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
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
      "step": 422,
      "proof_steps": 18,
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
          "kif": "(instance PeninsularRanges MountainRange)",
          "line": 1373
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
          "kif": "(geographicSubregion PeninsularRanges California)",
          "line": 1383
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 21,
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
          "kif": "(instance PeninsularRanges MountainRange)",
          "line": 1373
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
          "kif": "(geographicSubregion PeninsularRanges California)",
          "line": 1383
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 22,
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
          "kif": "(instance PeninsularRanges MountainRange)",
          "line": 1373
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
          "kif": "(geographicSubregion PeninsularRanges California)",
          "line": 1383
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
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
          "kif": "(instance PeninsularRanges MountainRange)",
          "line": 1373
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
      "step": 422,
      "proof_steps": 18,
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
          "kif": "(instance TransverseRanges MountainRange)",
          "line": 1357
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
          "kif": "(geographicSubregion TransverseRanges California)",
          "line": 1363
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 21,
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
          "kif": "(instance TransverseRanges MountainRange)",
          "line": 1357
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
          "kif": "(geographicSubregion TransverseRanges California)",
          "line": 1363
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 22,
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
          "kif": "(instance TransverseRanges MountainRange)",
          "line": 1357
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
          "kif": "(geographicSubregion TransverseRanges California)",
          "line": 1363
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
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
          "kif": "(instance TransverseRanges MountainRange)",
          "line": 1357
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
      "step": 422,
      "proof_steps": 23,
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
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
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
          "kif": "(subclass Region Object)",
          "line": 1532
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
          "kif": "(geographicSubregion SierraNevada Nevada)",
          "line": 1418
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 23,
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
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
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
          "kif": "(subclass Region Object)",
          "line": 1532
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
          "kif": "(geographicSubregion SierraNevada California)",
          "line": 1417
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 23,
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
          "kif": "(subclass Region Object)",
          "line": 1532
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
      "step": 422,
      "proof_steps": 27,
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
          "kif": "(subclass Region Object)",
          "line": 1532
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
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 27,
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
          "kif": "(subclass Region Object)",
          "line": 1532
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
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 25,
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
          "file": "Geography.kif",
          "kif": "(instance NorthAmerica GeographicArea)",
          "line": 79
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
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
      "step": 422,
      "proof_steps": 23,
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
          "kif": "(subclass Region Object)",
          "line": 1532
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
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
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
          "kif": "(subclass Region Object)",
          "line": 1532
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
          "file": "Geography.kif",
          "kif": "(geographicSubregion AndesMountains SouthAmerica)",
          "line": 1529
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion SouthAmerica WesternHemisphere)",
          "line": 5708
        },
        {
          "file": "Geography.kif",
          "kif": "(instance SouthAmerica Continent)",
          "line": 5704
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Continent LandArea)",
          "line": 18313
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        }
      ]
    },
    {
      "seed": 0,
      "step": 422,
      "proof_steps": 21,
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
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
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
      "step": 422,
      "proof_steps": 27,
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
          "file": "Geography.kif",
          "kif": "(geographicSubregion AndesMountains SouthAmerica)",
          "line": 1529
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion SouthAmerica WesternHemisphere)",
          "line": 5708
        },
        {
          "file": "Geography.kif",
          "kif": "(instance SouthAmerica Continent)",
          "line": 5704
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Continent LandArea)",
          "line": 18313
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandArea GeographicArea)",
          "line": 18279
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
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
      "step": 422,
      "proof_steps": 23,
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
          "kif": "(subclass Region Object)",
          "line": 1532
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
      "step": 452,
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
      "step": 452,
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
      "step": 452,
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
      "step": 474,
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
      "step": 474,
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
      "step": 475,
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
      "step": 476,
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
      "step": 476,
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
      "step": 476,
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
      "step": 476,
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
      "step": 499,
      "proof_steps": 8,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery EscherichiaColi0157H7 Ingesting)",
          "line": 1657
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Transfer)",
          "line": 13109
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
      "step": 499,
      "proof_steps": 22,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery EscherichiaColi0157H7 Ingesting)",
          "line": 1657
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Transfer)",
          "line": 13109
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))",
          "line": 195
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation objectTransferred patient)",
          "line": 14498
        },
        {
          "file": "Merge.kif",
          "kif": "(domain patient 1 Process)",
          "line": 3227
        },
        {
          "file": "Merge.kif",
          "kif": "(domain objectTransferred 1 Transfer)",
          "line": 14499
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
        }
      ]
    },
    {
      "seed": 0,
      "step": 499,
      "proof_steps": 20,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery EscherichiaColi0157H7 Ingesting)",
          "line": 1657
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Transfer)",
          "line": 13109
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))",
          "line": 195
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation objectTransferred patient)",
          "line": 14498
        },
        {
          "file": "Merge.kif",
          "kif": "(domain patient 1 Process)",
          "line": 3227
        },
        {
          "file": "Merge.kif",
          "kif": "(domain objectTransferred 1 Transfer)",
          "line": 14499
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting OrganismProcess)",
          "line": 13108
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
      "step": 499,
      "proof_steps": 11,
      "axioms": [
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery EscherichiaColi0157H7 Ingesting)",
          "line": 1657
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Transfer)",
          "line": 13109
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain objectTransferred 1 Transfer)",
          "line": 14499
        }
      ]
    },
    {
      "seed": 0,
      "step": 499,
      "proof_steps": 14,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain resource 1 Process)",
          "line": 3246
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery EscherichiaColi0157H7 Ingesting)",
          "line": 1657
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting OrganismProcess)",
          "line": 13108
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
      "step": 499,
      "proof_steps": 28,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain path 1 Motion)",
          "line": 14129
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
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery EscherichiaColi0157H7 Ingesting)",
          "line": 1657
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Transfer)",
          "line": 13109
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subrelation ?PRED1 ?PRED2) (domain ?PRED2 ?NUMBER ?CLASS1)) (domain ?PRED1 ?NUMBER ?CLASS1))",
          "line": 195
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation objectTransferred patient)",
          "line": 14498
        },
        {
          "file": "Merge.kif",
          "kif": "(domain patient 1 Process)",
          "line": 3227
        },
        {
          "file": "Merge.kif",
          "kif": "(domain objectTransferred 1 Transfer)",
          "line": 14499
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
      "step": 499,
      "proof_steps": 12,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS1) (domain ?REL ?NUMBER ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 233
        },
        {
          "file": "Merge.kif",
          "kif": "(domain path 1 Motion)",
          "line": 14129
        },
        {
          "file": "WMD.kif",
          "kif": "(=> (and (biochemicalAgentDelivery ?AGENT ?SUB) (subclass ?SUB ?PROCESS)) (biochemicalAgentDelivery ?AGENT ?PROCESS))",
          "line": 760
        },
        {
          "file": "WMD.kif",
          "kif": "(biochemicalAgentDelivery EscherichiaColi0157H7 Ingesting)",
          "line": 1657
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Ingesting Transfer)",
          "line": 13109
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
      "step": 550,
      "proof_steps": 21,
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
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
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
          "kif": "(geographicSubregion MountWhitney SierraNevada)",
          "line": 1484
        },
        {
          "file": "Geography.kif",
          "kif": "(instance MountWhitney Mountain)",
          "line": 1478
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Mountain LandForm)",
          "line": 6449
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 550,
      "proof_steps": 22,
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
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
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
          "kif": "(geographicSubregion MountWhitney SierraNevada)",
          "line": 1484
        },
        {
          "file": "Geography.kif",
          "kif": "(instance MountWhitney Mountain)",
          "line": 1478
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Mountain LandForm)",
          "line": 6449
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
          "kif": "(subclass Region Object)",
          "line": 1532
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
      "step": 550,
      "proof_steps": 33,
      "axioms": [
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))",
          "line": 25
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (located ?OBJ1 ?OBJ2) (forall (?SUB) (=> (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5075
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
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
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
          "kif": "(subclass Region Object)",
          "line": 1532
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation located partlyLocated)",
          "line": 5063
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion SierraNevada California)",
          "line": 1417
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion properPart)",
          "line": 18145
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation properPart part)",
          "line": 1063
        }
      ]
    },
    {
      "seed": 0,
      "step": 550,
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
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
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
          "kif": "(geographicSubregion SierraNevada Nevada)",
          "line": 1418
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 550,
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
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
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
          "kif": "(geographicSubregion MountWhitney SierraNevada)",
          "line": 1484
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subclass ?X ?Y) (instance ?Z ?X)) (instance ?Z ?Y))",
          "line": 146
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass Mountain LandForm)",
          "line": 6449
        },
        {
          "file": "Geography.kif",
          "kif": "(instance MountWhitney Mountain)",
          "line": 1478
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 550,
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
          "kif": "(geographicSubregion RockyMountains NorthAmerica)",
          "line": 350
        },
        {
          "file": "Geography.kif",
          "kif": "(subclass MountainRange LandForm)",
          "line": 6432
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 550,
      "proof_steps": 45,
      "axioms": [
        {
          "file": "Geography.kif",
          "kif": "(=> (and (partlyLocated ?PLACE ?SUBAREA) (instance ?SUBAREA GeographicArea) (geographicSubregion ?SUBAREA ?AREA)) (partlyLocated ?PLACE ?AREA))",
          "line": 2304
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion SierraNevada Nevada)",
          "line": 1418
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
          "file": "Geography.kif",
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass LandForm GeographicArea)",
          "line": 18156
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
          "kif": "(geographicSubregion MountWhitney SierraNevada)",
          "line": 1484
        },
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
          "kif": "(subclass Mountain LandForm)",
          "line": 6449
        },
        {
          "file": "Geography.kif",
          "kif": "(instance MountWhitney Mountain)",
          "line": 1478
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion MountWhitney California)",
          "line": 1485
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
      "step": 550,
      "proof_steps": 63,
      "axioms": [
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(=> (instance ?STATE AmericanState) (part ?STATE UnitedStates))",
          "line": 25
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Geography.kif",
          "kif": "(=> (and (connected ?X ?Y) (part ?Y ?Z)) (connected ?X ?Z))",
          "line": 2311
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (connected ?OBJ1 ?OBJ2) (or (meetsSpatially ?OBJ1 ?OBJ2) (overlapsSpatially ?OBJ1 ?OBJ2)))",
          "line": 12269
        },
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
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
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
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 5045
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
          "kif": "(geographicSubregion SierraNevada Nevada)",
          "line": 1418
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
          "kif": "(geographicSubregion SierraNevada California)",
          "line": 1417
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(part LosAngelesCalifornia California)",
          "line": 835
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
          "kif": "(instance connected SymmetricRelation)",
          "line": 12259
        }
      ]
    },
    {
      "seed": 0,
      "step": 550,
      "proof_steps": 81,
      "axioms": [
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
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (overlapsSpatially ?OBJ1 ?OBJ2) (exists (?OBJ3) (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2))))",
          "line": 12350
        },
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
          "kif": "(geographicSubregion SierraNevada Nevada)",
          "line": 1418
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
          "kif": "(geographicSubregion SierraNevada California)",
          "line": 1417
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
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
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
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
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
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
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation GeopoliticalArea)",
          "line": 18359
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
      "step": 550,
      "proof_steps": 104,
      "axioms": [
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
          "file": "Geography.kif",
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
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
          "kif": "(geographicSubregion RockyMountains NorthAmerica)",
          "line": 350
        },
        {
          "file": "Merge.kif",
          "kif": "(instance overlapsSpatially SymmetricRelation)",
          "line": 5016
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Region Object)",
          "line": 1532
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
          "file": "CountriesAndRegions.kif",
          "kif": "(instance California AmericanState)",
          "line": 929
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
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
          "file": "Geography.kif",
          "kif": "(instance SierraNevada MountainRange)",
          "line": 1411
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (instance ?OBJ1 Object) (partlyLocated ?OBJ1 ?OBJ2)) (exists (?SUB) (and (part ?SUB ?OBJ1) (located ?SUB ?OBJ2))))",
          "line": 5051
        },
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
          "kif": "(geographicSubregion SierraNevada Nevada)",
          "line": 1418
        },
        {
          "file": "Geography.kif",
          "kif": "(geographicSubregion SierraNevada California)",
          "line": 1417
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
          "kif": "(subclass GeopoliticalArea AutonomousAgent)",
          "line": 18165
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Nation GeopoliticalArea)",
          "line": 18359
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass AutonomousAgent Object)",
          "line": 1999
        },
        {
          "file": "CountriesAndRegions.kif",
          "kif": "(geographicSubregion UnitedStates NorthAmerica)",
          "line": 418
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation geographicSubregion properPart)",
          "line": 18145
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation properPart part)",
          "line": 1063
        }
      ]
    },
    {
      "seed": 0,
      "step": 560,
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
      "step": 560,
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
          "kif": "(biochemicalAgentDelivery MycobacteriumTuberculosis Breathing)",
          "line": 1662
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
          "kif": "(=> (instance ?CLASS Class) (subclass ?CLASS Entity))",
          "line": 925
        }
      ]
    },
    {
      "seed": 0,
      "step": 560,
      "proof_steps": 13,
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
          "kif": "(biochemicalAgentDelivery MycobacteriumTuberculosis Breathing)",
          "line": 1662
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
        }
      ]
    },
    {
      "seed": 0,
      "step": 560,
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
      "step": 560,
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
      "step": 560,
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
      "step": 573,
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
      "step": 573,
      "proof_steps": 18,
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
          "kif": "(instance USMilitaryRankWO2 USMilitaryRank)",
          "line": 822
        },
        {
          "file": "Military.kif",
          "kif": "(subclass USMilitaryRank MilitaryRank)",
          "line": 493
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
      "step": 573,
      "proof_steps": 15,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (subAttribute ?ATTR1 ?ATTR2) (instance ?ATTR2 ?CLASS)) (instance ?ATTR1 ?CLASS))",
          "line": 786
        },
        {
          "file": "MilitaryProcesses.kif",
          "kif": "(subAttribute DirectorJS MilitaryCommander)",
          "line": 916
        },
        {
          "file": "Cellular&TelephoneArchitecture.kif",
          "kif": "(and (instance ?X MobileCellPhone) (instance ?P PublicSwitchedTelephoneNetwork) (not (component ?X ?P)))",
          "line": 1161
        },
        {
          "file": "MilitaryProcesses.kif",
          "kif": "(instance DirectorJS Position)",
          "line": 915
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
      "step": 573,
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
      "step": 573,
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
      "step": 573,
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
      "step": 583,
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
      "step": 596,
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
      "step": 596,
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
    }
  ]
}
```
