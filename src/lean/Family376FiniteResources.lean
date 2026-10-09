/-
Finite-resource logic for the Family 376 matter audit.

Standalone Lean 4.19.0; no imports, sorry, or new axioms.
Costs are natural-number units of an EXPLICIT usable-resource budget.
Nothing here proves that a physical gate has a positive cost floor.
This does not formalize fluids, energy conditions, GR, or a Turing machine.
-/
namespace Family376FiniteResources

/-- A ledger for the first n operations. -/
def spent (cost : Nat → Nat) : Nat → Nat
  | 0 => 0
  | n + 1 => spent cost n + cost n

/-- Every operation has a cost of at least q, under the supplied premise. -/
theorem floor_bound (cost : Nat → Nat) (q : Nat)
    (floor : ∀ k, q ≤ cost k) (n : Nat) : n * q ≤ spent cost n := by
  induction n with
  | zero => simp [spent]
  | succ n ih =>
      simpa [spent, Nat.succ_mul] using Nat.add_le_add ih (floor n)

/-- This is an accounting consequence, not a physical law imposing a floor. -/
theorem budget_bounds_count (cost : Nat → Nat) (q B n : Nat)
    (floor : ∀ k, q ≤ cost k) (budget : spent cost n ≤ B) : n * q ≤ B :=
  Nat.le_trans (floor_bound cost q floor n) budget

/-- No fixed finite usable budget supports all lengths at a positive floor. -/
theorem no_unbounded_positive_cost (cost : Nat → Nat) (q B : Nat)
    (positive : 0 < q) (floor : ∀ k, q ≤ cost k)
    (budget : ∀ n, spent cost n ≤ B) : False := by
  have one_le : 1 ≤ q := positive
  have lower : B + 1 ≤ (B + 1) * q := by
    simpa using Nat.mul_le_mul_left (B + 1) one_le
  have upper : (B + 1) * q ≤ B :=
    budget_bounds_count cost q B (B + 1) floor (budget (B + 1))
  exact Nat.not_succ_le_self B (Nat.le_trans lower upper)

/-- Each finite prefix may be funded by a different budget. -/
theorem every_prefix_has_a_budget : ∀ n : Nat, ∃ B : Nat, n ≤ B :=
  fun n => ⟨n, Nat.le_refl n⟩

/-- Exchanging the two quantifiers is invalid even for unit-cost operations. -/
theorem no_single_budget_for_all_prefixes : ¬ ∃ B : Nat, ∀ n : Nat, n ≤ B := by
  intro h
  obtain ⟨B, bound⟩ := h
  exact Nat.not_succ_le_self B (bound (B + 1))

#print axioms floor_bound
#print axioms budget_bounds_count
#print axioms no_unbounded_positive_cost
#print axioms every_prefix_has_a_budget
#print axioms no_single_budget_for_all_prefixes

end Family376FiniteResources
