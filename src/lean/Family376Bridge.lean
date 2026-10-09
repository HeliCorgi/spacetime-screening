/-
Conditional interface lemmas for the Family 376 / gravity audit.

This file does NOT formalize Navier-Stokes, a Turing machine, Lorentzian
geometry, KRW, Hadamard states, or the semiclassical Einstein equation.
Physical implication premises and algorithm-class closure are explicit inputs.
In particular, Algorithm is NOT Lean's Decidable predicate: classical logical
decidability would not express Turing computability.

Standalone Lean 4.19.0. No imports, sorry, or new axiom declarations.
-/
namespace Family376Bridge

universe u v

/-- An immediately halting witness is enough; undecidability is not used. -/
theorem no_regular_horizon_compiler
    {Machine : Type u} {System : Type v}
    (encode : Machine → System) (Halts : Machine → Prop)
    (Regular BadHorizon : System → Prop)
    (obstruction : ∀ s, BadHorizon s → ¬ Regular s)
    (allRegular : ∀ m, Regular (encode m))
    (haltTrigger : ∀ m, Halts m → BadHorizon (encode m))
    (m : Machine) (halts : Halts m) : False :=
  obstruction (encode m) (haltTrigger m halts) (allRegular m)

/-- A compiler staying in a chronal class cannot use CTCs as a halting flag. -/
theorem no_chronal_ctc_compiler
    {Machine : Type u} {System : Type v}
    (encode : Machine → System) (Halts : Machine → Prop)
    (Chronal CTC : System → Prop)
    (chronalExcludes : ∀ s, Chronal s → ¬ CTC s)
    (allChronal : ∀ m, Chronal (encode m))
    (haltTrigger : ∀ m, Halts m → CTC (encode m))
    (m : Machine) (halts : Halts m) : False :=
  chronalExcludes (encode m) (allChronal m) (haltTrigger m halts)

/-- Generic many-one transfer. None of its physical/effectivity premises is
    supplied by the abstract proof; there is no unconditional CTC result. -/
theorem undecidability_transfer
    {Machine : Type u} {System : Type v}
    (encode : Machine → System)
    (Halts : Machine → Prop) (Event : System → Prop)
    (SourceAlgorithm : (Machine → Bool) → Prop)
    (TargetAlgorithm : (System → Bool) → Prop)
    (sourceUndecidable : ¬ ∃ d, SourceAlgorithm d ∧
      ∀ m, (d m = true ↔ Halts m))
    (effectiveComposition : ∀ d, TargetAlgorithm d →
      SourceAlgorithm (fun m => d (encode m)))
    (reduction : ∀ m, Halts m ↔ Event (encode m)) :
    ¬ ∃ d, TargetAlgorithm d ∧ ∀ s, (d s = true ↔ Event s) :=
  fun candidate => sourceUndecidable
    (Exists.elim candidate (fun d hd =>
      ⟨(fun m => d (encode m)), effectiveComposition d hd.1,
        (fun m => (hd.2 (encode m)).trans (reduction m).symm)⟩))

#print axioms no_regular_horizon_compiler
#print axioms no_chronal_ctc_compiler
#print axioms undecidability_transfer

end Family376Bridge
