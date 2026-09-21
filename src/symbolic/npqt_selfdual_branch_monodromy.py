#!/usr/bin/env python3
"""Self-dual Weyl eigen-branch monodromy gate for NPQT representative design.

The local self-dual spectral projector is smooth while one chosen eigenvalue
remains isolated.  A full covariant action, however, needs a single-valued
expression on an open generic curvature neighborhood.

This script gives an explicit complex-symmetric tracefree self-dual Weyl
family with eigenvalue monodromy.

Let t=s^2 and define the 2x2 block

    A(t) = [[a, b],
            [b,-a]],

    a=(1+t)/2,
    b=(1-t)/(2 i).

Then

    A(t)^2 = t I,

so the full tracefree symmetric operator

    Q(t)=diag_block(A(t),0)

has eigenvalues {+sqrt(t), -sqrt(t), 0}.

Q depends only on t=s^2, hence Q(s)=Q(-s), but the two nonzero rank-one
eigenprojectors are exchanged under s -> -s.  Analytically continuing once
around t=0 therefore returns to the same Weyl operator while swapping two
eigenlines.

With a generic fixed Ricci probe Z that distinguishes those lines, the
principal-plane contraction also changes.  Thus a branch-specific Weyl
eigenline projector cannot define a globally single-valued generic 4D scalar
by itself.

Multiplying Q by an arbitrary epsilon leaves the monodromy intact and places
the entire loop arbitrarily close to Q=0.  The obstruction therefore
accumulates at the maximally symmetric core.

Scope: this rejects a global *Weyl-only branch labeling* as the completion of
the local principal-plane idea.  It does not rule out permutation-symmetric
mixed Weyl-Ricci concomitants or some other non-spectral representative.
"""

from __future__ import annotations

import sympy as sp


s = sp.symbols("s", nonzero=True)
z1, z2, z3 = sp.symbols("z1 z2 z3")
eps = sp.symbols("epsilon", nonzero=True)

t = s**2
I = sp.I

a = (1 + t) / 2
b = (1 - t) / (2 * I)

Q = sp.Matrix(
    [
        [a, b, 0],
        [b, -a, 0],
        [0, 0, 0],
    ]
)

assert sp.simplify(Q.T - Q) == sp.zeros(3)
assert sp.simplify(sp.trace(Q)) == 0

Q2 = sp.simplify(Q**2)
expected_Q2 = sp.diag(t, t, 0)
assert sp.simplify(Q2 - expected_Q2) == sp.zeros(3)

lam = sp.symbols("lambda")
charpoly = sp.factor(Q.charpoly(lam).as_expr())
assert sp.simplify(charpoly - lam * (lam**2 - t)) == 0

# The input operator is invariant under the two sheets s and -s.
Q_minus = sp.simplify(Q.subs(s, -s))
assert sp.simplify(Q_minus - Q) == sp.zeros(3)

B = sp.diag(1, 1, 0)

# Since Q^2=s^2 B, the two nonzero spectral projectors are
# P_± = (B ± Q/s)/2.
P_plus = sp.simplify((B + Q / s) / 2)
P_minus = sp.simplify((B - Q / s) / 2)

assert sp.simplify(P_plus**2 - P_plus) == sp.zeros(3)
assert sp.simplify(P_minus**2 - P_minus) == sp.zeros(3)
assert sp.simplify(P_plus * P_minus) == sp.zeros(3)
assert sp.simplify(P_plus + P_minus - B) == sp.zeros(3)
assert sp.simplify(Q * P_plus - s * P_plus) == sp.zeros(3)
assert sp.simplify(Q * P_minus + s * P_minus) == sp.zeros(3)

# Sheet exchange at identical Q.
P_plus_after = sp.simplify(P_plus.subs(s, -s))
assert sp.simplify(P_plus_after - P_minus) == sp.zeros(3)
assert sp.simplify(P_plus - P_minus) != sp.zeros(3)

# A generic Ricci probe makes the branch exchange observable in the scalar.
Z = sp.diag(z1, z2, z3)
H_plus = sp.eye(3) - P_plus
H_minus = sp.eye(3) - P_minus

Theta_plus = sp.factor(sp.trace(H_plus * Z) / 2)
Theta_minus = sp.factor(sp.trace(H_minus * Z) / 2)
Theta_jump = sp.factor(Theta_plus - Theta_minus)

# At t=1 (s=1), Q=diag(1,-1,0) and the two branches select the
# first versus second axis.
Theta_plus_1 = sp.simplify(Theta_plus.subs(s, 1))
Theta_minus_1 = sp.simplify(Theta_minus.subs(s, 1))
jump_1 = sp.factor(Theta_plus_1 - Theta_minus_1)

assert sp.simplify(Theta_plus_1 - (z2 + z3) / 2) == 0
assert sp.simplify(Theta_minus_1 - (z1 + z3) / 2) == 0
assert sp.simplify(jump_1 - (z2 - z1) / 2) == 0

# Scaling the entire Weyl loop toward the core preserves its projector
# monodromy for every nonzero epsilon.
Q_scaled = sp.simplify(eps * Q)
Q_scaled_minus = sp.simplify(Q_scaled.subs(s, -s))
assert sp.simplify(Q_scaled_minus - Q_scaled) == sp.zeros(3)

# The characteristic polynomial scales as expected and the spectral labels
# still exchange.  No lower bound on |epsilon| is required.
char_scaled = sp.factor(Q_scaled.charpoly(lam).as_expr())
assert sp.simplify(char_scaled - lam * (lam**2 - eps**2 * t)) == 0


def main() -> None:
    print("== NPQT self-dual branch-monodromy gate ==")
    print("Q(t) is complex symmetric and tracefree.")
    print(f"char(Q) = {charpoly}")
    print("Q(s) = Q(-s), but")
    print("P_plus(-s) = P_minus(s).")
    print()
    print("At t=1:")
    print(f"Theta_plus  = {Theta_plus_1}")
    print(f"Theta_minus = {Theta_minus_1}")
    print(f"difference  = {jump_1}")
    print()
    print("Thus a generic Ricci contraction distinguishes the two sheets even")
    print("though the Weyl tensor has returned to the same value.")
    print()
    print("Multiplying Q by arbitrary nonzero epsilon preserves the exchange,")
    print("so these monodromy loops occur arbitrarily close to the W=0 core.")
    print()
    print("Conclusion: a global Weyl-only eigenline labeling cannot be the")
    print("single-valued NPQT completion.  A viable representative must be")
    print("permutation symmetric or use additional mixed curvature data in a")
    print("way that remains C^2 at the core.")
    print("All branch-monodromy assertions passed.")


if __name__ == "__main__":
    main()
