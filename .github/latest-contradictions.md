# Full SUMO contradiction report

Open https://sigmakee.dev/audit and choose Latest master contradiction report.
Save any work you want to keep before confirming replacement and replay.
The app verifies master, constituents, and engine inputs before replaying only the steps below.

## Contradiction 1

- Seed: `0`
- Start step: `282`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `17`

### Cited source axioms

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:10053

```lisp
(range BeginFn TimePoint)
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

## Contradiction 2

- Seed: `0`
- Start step: `282`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `17`

### Cited source axioms

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:10053

```lisp
(range BeginFn TimePoint)
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

## Contradiction 3

- Seed: `0`
- Start step: `282`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `17`

### Cited source axioms

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:10668

```lisp
(range WhenFn TimeInterval)
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

## Contradiction 4

- Seed: `0`
- Start step: `282`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `17`

### Cited source axioms

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:10668

```lisp
(range WhenFn TimeInterval)
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

## Contradiction 5

- Seed: `0`
- Start step: `282`
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

## Contradiction 6

- Seed: `0`
- Start step: `282`
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
- Start step: `282`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `17`

### Cited source axioms

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:5832

```lisp
(range AdditionFn RealNumber)
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
- Start step: `282`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `17`

### Cited source axioms

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:5832

```lisp
(range AdditionFn RealNumber)
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
- Start step: `282`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `17`

### Cited source axioms

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:6864

```lisp
(range KappaFn Class)
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
- Start step: `282`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `17`

### Cited source axioms

#### Merge.kif:345

```lisp
(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))
```

#### Merge.kif:6864

```lisp
(range KappaFn Class)
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

## Contradiction 11

- Seed: `0`
- Start step: `540`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `46`

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

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Geography.kif:1485

```lisp
(geographicSubregion MountWhitney California)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 12

- Seed: `0`
- Start step: `540`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `57`

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

#### Geography.kif:1484

```lisp
(geographicSubregion MountWhitney SierraNevada)
```

#### Geography.kif:6449

```lisp
(subclass Mountain LandForm)
```

#### Geography.kif:1478

```lisp
(instance MountWhitney Mountain)
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

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
```

#### Merge.kif:5063

```lisp
(subrelation located partlyLocated)
```

#### Merge.kif:18146

```lisp
(subrelation geographicSubregion located)
```

#### Geography.kif:1485

```lisp
(geographicSubregion MountWhitney California)
```

#### Merge.kif:5016

```lisp
(instance overlapsSpatially SymmetricRelation)
```

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

#### Geography.kif:1417

```lisp
(geographicSubregion SierraNevada California)
```

## Contradiction 13

- Seed: `0`
- Start step: `540`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `38`

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

#### Geography.kif:5648

```lisp
(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))
```

#### Merge.kif:18124

```lisp
(subclass GeographicArea Region)
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

#### Merge.kif:1532

```lisp
(subclass Region Object)
```

## Contradiction 14

- Seed: `0`
- Start step: `583`
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

## Contradiction 15

- Seed: `0`
- Start step: `583`
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
  "sumo_commit": "7f73fe6a8e6fd7b170279b7414f645ac9e96b226",
  "run_id": "37476544844",
  "run_attempt": 1,
  "engine": {
    "commit": "3051b50b11dd1d372d2db94d664e6ad56e0efa62",
    "fingerprint": "82b958b3104df4cb7576711153b2e3ddb631e9f2094df084f7f2d9b343e352ac"
  },
  "fingerprint": "38acbaa016c34c1fe0bd0ddd475a1730637e7999eeb09ea9f543d392a4bab088",
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
      "sha256": "61ef5df5691dc62c23693b8617d1a4ddc3085bb33ab0ef82064a87b38005e02f"
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
      "sha256": "d386bc120f3abfd50e4a6c75896d4c9ce9fa28a638f9f86fd9c21aed340d6ca1"
    },
    {
      "name": "Merge.kif",
      "sha256": "9de30c008f622393bbf64ea094157097e8e634707d0b4a353576f0ce3b73cc72"
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
      "sha256": "f91c8a64eb8feeb2b49afd5e07a519f9a7f0152b3cd1333e79879fe519c6f053"
    },
    {
      "name": "Weather.kif",
      "sha256": "79c72e1ade834a78f5dfa48d4324be1b02ef21953d0a7f198d0a8e171845caaa"
    },
    {
      "name": "WMD.kif",
      "sha256": "6a17770304555877ddf6685c087dc8f408b5af05cc3865ff5be105e7cc57deff"
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
      "step": 282,
      "proof_steps": 17,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range BeginFn TimePoint)",
          "line": 10053
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
      "step": 282,
      "proof_steps": 17,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range BeginFn TimePoint)",
          "line": 10053
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
      "step": 282,
      "proof_steps": 17,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range WhenFn TimeInterval)",
          "line": 10668
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
      "step": 282,
      "proof_steps": 17,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range WhenFn TimeInterval)",
          "line": 10668
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
      "step": 282,
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
      "step": 282,
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
      "step": 282,
      "proof_steps": 17,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range AdditionFn RealNumber)",
          "line": 5832
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
      "step": 282,
      "proof_steps": 17,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range AdditionFn RealNumber)",
          "line": 5832
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
      "step": 282,
      "proof_steps": 17,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range KappaFn Class)",
          "line": 6864
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
      "step": 282,
      "proof_steps": 17,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (range ?REL ?CLASS1) (range ?REL ?CLASS2)) (or (subclass ?CLASS1 ?CLASS2) (subclass ?CLASS2 ?CLASS1)))",
          "line": 345
        },
        {
          "file": "Merge.kif",
          "kif": "(range KappaFn Class)",
          "line": 6864
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
      "step": 540,
      "proof_steps": 46,
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
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
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
      "step": 540,
      "proof_steps": 57,
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
          "file": "Geography.kif",
          "kif": "(geographicSubregion MountWhitney SierraNevada)",
          "line": 1484
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
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
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
          "kif": "(geographicSubregion MountWhitney California)",
          "line": 1485
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
          "kif": "(geographicSubregion SierraNevada California)",
          "line": 1417
        }
      ]
    },
    {
      "seed": 0,
      "step": 540,
      "proof_steps": 38,
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
          "kif": "(=> (and (overlapsSpatially ?ONE ?TWO) (instance ?TWO Region) (not (equal ?ONE ?TWO))) (partlyLocated ?ONE ?TWO))",
          "line": 5648
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass GeographicArea Region)",
          "line": 18124
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
          "kif": "(subclass Region Object)",
          "line": 1532
        }
      ]
    },
    {
      "seed": 0,
      "step": 583,
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
      "step": 583,
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
