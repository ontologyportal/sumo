# Full SUMO contradiction report

Open https://sigmakee.dev/audit and choose Latest master contradiction report.
Save any work you want to keep before confirming replacement and replay.
The app verifies master, constituents, and engine inputs before replaying only the steps below.

## Contradiction 1

- Seed: `0`
- Start step: `174`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `65`

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

#### Merge.kif:3047

```lisp
(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))
```

#### Merge.kif:1276

```lisp
(subclass Substance SelfConnectedObject)
```

#### WMD.kif:536

```lisp
(subclass NerveAgent ChemicalAgent)
```

#### WMD.kif:445

```lisp
(subclass ChemicalAgent BiologicallyActiveSubstance)
```

#### Merge.kif:18990

```lisp
(subclass BiologicallyActiveSubstance Substance)
```

#### Merge.kif:136

```lisp
(instance subclass PartialOrderingRelation)
```

#### Merge.kif:3074

```lisp
(subclass PartialOrderingRelation TransitiveRelation)
```

#### Merge.kif:961

```lisp
(subclass SelfConnectedObject Object)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:929

```lisp
(subclass Physical Entity)
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

#### WMD.kif:537

```lisp
(biochemicalAgentDelivery NerveAgent Breathing)
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

#### Merge.kif:509

```lisp
(=> (contraryAttribute @ROW) (=> (inList ?ELEMENT (ListFn @ROW)) (instance ?ELEMENT Attribute)))
```

#### Merge.kif:23444

```lisp
(contraryAttribute Dead Living)
```

#### Merge.kif:83

```lisp
(instance instance BinaryPredicate)
```

#### Merge.kif:85

```lisp
(domain instance 2 Class)
```

#### Merge.kif:4725

```lisp
(=> (instance ?PROC1 Process) (exists (?PROC2) (causes ?PROC2 ?PROC1)))
```

## Contradiction 2

- Seed: `0`
- Start step: `378`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### VirusProteinAndCellPart.kif:969

```lisp
(part (ViralPartFn ?VIR ?PARTTYPE) ?VIR)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:12256

```lisp
(instance connected BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:12261

```lisp
(domain connected 2 Object)
```

#### Merge.kif:2814

```lisp
(subclass Class SetOrClass)
```

#### Merge.kif:2803

```lisp
(subclass SetOrClass Abstract)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
```

#### Merge.kif:911

```lisp
(partition Entity Physical Abstract)
```

## Contradiction 3

- Seed: `0`
- Start step: `378`
- Axioms to check: `1`
- Axioms per subproblem: `1`
- Backend: `SUPr`
- Proof steps reported by Sigma: `19`

### Cited source axioms

#### Merge.kif:12357

```lisp
(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))
```

#### VirusProteinAndCellPart.kif:969

```lisp
(part (ViralPartFn ?VIR ?PARTTYPE) ?VIR)
```

#### Merge.kif:5011

```lisp
(subrelation overlapsSpatially connected)
```

#### Merge.kif:3828

```lisp
(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))
```

#### Merge.kif:12256

```lisp
(instance connected BinaryPredicate)
```

#### Merge.kif:4395

```lisp
(subclass BinaryPredicate Predicate)
```

#### Merge.kif:12260

```lisp
(domain connected 1 Object)
```

#### Merge.kif:2814

```lisp
(subclass Class SetOrClass)
```

#### Merge.kif:2803

```lisp
(subclass SetOrClass Abstract)
```

#### Merge.kif:946

```lisp
(subclass Object Physical)
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
  "sumo_commit": "7afe4785fb698b3d8569b3bf9c134ec3c0c22b17",
  "run_id": "37636863202",
  "run_attempt": 1,
  "engine": {
    "commit": "ada893a2ed46d99ec81fed70d24a621477c98100",
    "fingerprint": "e337aa8a44a4a750d9cb2bd37284facb9ec770fe5e8196f9caf10b4b500e4a76"
  },
  "fingerprint": "01266245d6162c9cd780d02c9038bf4560643bb29f8e7d03eb68af3042901ad0",
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
      "sha256": "0aee55b27956beb7550ecce4d7fda1f330afb0faec1e2e3d8b82bf389be1d0d7"
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
      "sha256": "321ebd70d149769764dd200391e08e78ae5674fd8f228aa8c4bd636f194e2d49"
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
      "sha256": "bb8fb9e2dcb48fa10a36bdcb81c8e2b96cb205d2d0fcb7411f2192805e424b5a"
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
      "sha256": "90852bbc5f5be9027680c7f591c2a12a7f534e0489cbd158dc33a95e964d7bf0"
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
      "step": 174,
      "proof_steps": 65,
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
          "kif": "(=> (instance ?REL TransitiveRelation) (forall (?INST1 ?INST2 ?INST3) (=> (and (?REL ?INST1 ?INST2) (?REL ?INST2 ?INST3)) (?REL ?INST1 ?INST3))))",
          "line": 3047
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass Substance SelfConnectedObject)",
          "line": 1276
        },
        {
          "file": "WMD.kif",
          "kif": "(subclass NerveAgent ChemicalAgent)",
          "line": 536
        },
        {
          "file": "WMD.kif",
          "kif": "(subclass ChemicalAgent BiologicallyActiveSubstance)",
          "line": 445
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BiologicallyActiveSubstance Substance)",
          "line": 18990
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
          "kif": "(subclass Physical Entity)",
          "line": 929
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
          "kif": "(biochemicalAgentDelivery NerveAgent Breathing)",
          "line": 537
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
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (contraryAttribute @ROW) (=> (inList ?ELEMENT (ListFn @ROW)) (instance ?ELEMENT Attribute)))",
          "line": 509
        },
        {
          "file": "Merge.kif",
          "kif": "(contraryAttribute Dead Living)",
          "line": 23444
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
          "kif": "(=> (instance ?PROC1 Process) (exists (?PROC2) (causes ?PROC2 ?PROC1)))",
          "line": 4725
        }
      ]
    },
    {
      "seed": 0,
      "step": 378,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "VirusProteinAndCellPart.kif",
          "kif": "(part (ViralPartFn ?VIR ?PARTTYPE) ?VIR)",
          "line": 969
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected BinaryPredicate)",
          "line": 12256
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(domain connected 2 Object)",
          "line": 12261
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
      "step": 378,
      "proof_steps": 19,
      "axioms": [
        {
          "file": "Merge.kif",
          "kif": "(=> (and (part ?OBJ3 ?OBJ1) (part ?OBJ3 ?OBJ2)) (overlapsSpatially ?OBJ1 ?OBJ2))",
          "line": 12357
        },
        {
          "file": "VirusProteinAndCellPart.kif",
          "kif": "(part (ViralPartFn ?VIR ?PARTTYPE) ?VIR)",
          "line": 969
        },
        {
          "file": "Merge.kif",
          "kif": "(subrelation overlapsSpatially connected)",
          "line": 5011
        },
        {
          "file": "Merge.kif",
          "kif": "(=> (and (domain ?REL ?NUMBER ?CLASS) (instance ?REL Predicate) (?REL @ROW)) (instance (ListOrderFn (ListFn @ROW) ?NUMBER) ?CLASS))",
          "line": 3828
        },
        {
          "file": "Merge.kif",
          "kif": "(instance connected BinaryPredicate)",
          "line": 12256
        },
        {
          "file": "Merge.kif",
          "kif": "(subclass BinaryPredicate Predicate)",
          "line": 4395
        },
        {
          "file": "Merge.kif",
          "kif": "(domain connected 1 Object)",
          "line": 12260
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
          "kif": "(subclass Object Physical)",
          "line": 946
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
