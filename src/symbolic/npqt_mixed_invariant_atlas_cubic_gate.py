#!/usr/bin/env python3
"""Lowest-degree mixed Weyl-Ricci gate for the NPQT invariant atlas.

In four dimensions one has the dimensionally dependent identity

    C_{a c d e} C_b{}^{c d e}
      = (1/4) g_{ab} C_{c d e f} C^{c d e f}.

Therefore the most direct cubic scalar with two Weyl tensors and one
traceless-Ricci tensor vanishes:

    Z^{ab} C_{a c d e} C_b{}^{c d e} = 0.

This script verifies the identity explicitly on a generic purely-electric
Lorentzian algebraic Weyl family with eigenvalues
    (e1,e2,-e1-e2)
and then contracts it with a generic diagonal traceless-Ricci tensor.

Scope: this is a low-degree obstruction, not a proof that every possible
cubic mixed contraction is impossible.  The exact 4D identity itself is
standard and is used here as a fast atlas gate.
"""

from __future__ import annotations

import itertools
import sympy as sp

eta = sp.diag(-1, 1, 1, 1)

e1, e2 = sp.symbols("e1 e2", real=True)
Evals = (e1, e2, -e1 - e2)
E = sp.diag(*Evals)

def eps3(i: int, j: int, k: int) -> sp.Expr:
    return sp.LeviCivita(i - 1, j - 1, k - 1)

C = sp.MutableDenseNDimArray.zeros(4, 4, 4, 4)

for i in range(1, 4):
    for j in range(1, 4):
        value = E[i - 1, j - 1]
        C[0, i, 0, j] = value
        C[i, 0, 0, j] = -value
        C[0, i, j, 0] = -value
        C[i, 0, j, 0] = value

for i, j, k, l in itertools.product(range(1, 4), repeat=4):
    C[i, j, k, l] = sp.simplify(
        sum(
            -eps3(i, j, m) * eps3(k, l, n) * E[m - 1, n - 1]
            for m, n in itertools.product(range(1, 4), repeat=2)
        )
    )

def raise_all(a: int, b: int, c: int, d: int) -> sp.Expr:
    return sp.simplify(
        sum(
            eta[a, A] * eta[b, B] * eta[c, Cc] * eta[d, D] * C[A, B, Cc, D]
            for A, B, Cc, D in itertools.product(range(4), repeat=4)
        )
    )

W2 = sp.factor(
    sum(
        C[a, b, c, d] * raise_all(a, b, c, d)
        for a, b, c, d in itertools.product(range(4), repeat=4)
    )
)

S = sp.Matrix.zeros(4, 4)
for a, b in itertools.product(range(4), repeat=2):
    value = 0
    for c, d, e in itertools.product(range(4), repeat=3):
        C_b_up = sum(
            eta[c, Cc] * eta[d, D] * eta[e, Ee] * C[b, Cc, D, Ee]
            for Cc, D, Ee in itertools.product(range(4), repeat=3)
        )
        value += C[a, c, d, e] * C_b_up
    S[a, b] = sp.factor(value)

assert W2 == 16 * (e1**2 + e1 * e2 + e2**2)
assert sp.simplify(S - eta * W2 / 4) == sp.zeros(4)

z0, z1, z2 = sp.symbols("z0 z1 z2", real=True)
z3 = -z0 - z1 - z2
Zmix = sp.diag(z0, z1, z2, z3)
Zcov = eta * Zmix
Zup = eta * Zcov * eta

cubic = sp.factor(
    sum(Zup[a, b] * S[a, b] for a, b in itertools.product(range(4), repeat=2))
)

assert sp.trace(Zmix) == 0
assert cubic == 0

def main() -> None:
    print("== NPQT mixed-invariant atlas: cubic gate ==")
    print(f"W2 = {W2}")
    print("C_acde C_b^{cde} = (W2/4) g_ab on the test family.")
    print(f"Z^ab C_acde C_b^cde = {cubic}")
    print()
    print("Conclusion: the direct W^2 Z cubic scalar vanishes for traceless Z.")
    print("The atlas must therefore use a different mixed contraction and/or")
    print("a higher-degree rational representative.")
    print("All cubic-gate assertions passed.")

if __name__ == "__main__":
    main()
