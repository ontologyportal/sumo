tff(fn_s__DeadFn, type, s__DeadFn: $i > $i).
tff(fn_s__DayFn__1InFn, type, s__DayFn__1InFn: ($int * $i) > $i).
tff(fn_s__OrganicObjectFn, type, s__OrganicObjectFn: $i > $i).
tff(pred_s__instance_2, type, s__instance: ($i * $i) > $o).
tff(pred_s__subclass_2, type, s__subclass: ($i * $i) > $o).
tff(pred_s__part_2, type, s__part: ($i * $i) > $o).
tff(kb_10484458193534519347, axiom, ![X1: $i] : ![X0: $i] : ((X0 = s__OrganicObjectFn(X1) & s__subclass(X0,s__Object)) => ?[X2: $i] : ?[X3: $i] : (s__instance(X2,s__DeadFn(X1)) & s__part(X2,X3) & s__instance(X3,X1)))).
tff(kb_12717946372653837961, axiom, ![X2: $i] : ![X1: $int] : ![X0: $i] : (s__instance(X0,s__DayFn__1InFn(X1,X2)) => $lesseq(X1,31))).
tff(kb_13915356782297013560, axiom, ![X3: $i] : ![X2: $i] : (s__OrganicObjectFn(X2) = X3 => s__subclass(X3,s__Object))).
