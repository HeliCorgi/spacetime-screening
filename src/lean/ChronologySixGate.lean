/-
A conditional causal-order lemma, NOT chronology protection or string theory.
I is chronological reachability and J is causal reachability. The geometric
push-up lemma is an explicit hypothesis, not a derived Lorentzian theorem.
ChronalAt refers to the FULL chosen extension, not merely a local patch.
No imports, sorry, new axioms, or model-specific physical assumptions are hidden.
-/
namespace ChronologySixGate

def ChronalAt {E : Type} (I : E → E → Prop) (p : E) : Prop := ¬ I p p

theorem receiver_on_ctc {E : Type} (I J : E → E → Prop)
    (push : ∀ {a b c : E}, I a b → J b c → I a c)
    {A B : E} (earlier : I B A) (back : J A B) : I B B :=
  push earlier back

theorem no_causal_return_to_chronal {E : Type} (I J : E → E → Prop)
    (push : ∀ {a b c : E}, I a b → J b c → I a c)
    {A B : E} (earlier : I B A) (hB : ChronalAt I B) : ¬ J A B :=
  fun back => hB (push earlier back)

theorem no_signal_to_chronal_past {E : Type} (I J S : E → E → Prop)
    (push : ∀ {a b c : E}, I a b → J b c → I a c)
    (support : ∀ {a b : E}, S a b → J a b)
    {A B : E} (earlier : I B A) (hB : ChronalAt I B) : ¬ S A B :=
  fun sig => hB (push earlier (support sig))

#print axioms receiver_on_ctc
#print axioms no_causal_return_to_chronal
#print axioms no_signal_to_chronal_past
end ChronologySixGate
