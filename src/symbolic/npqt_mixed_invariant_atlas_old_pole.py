#!/usr/bin/env python3
"""Stress test atlas chart 1 on the explicit old NPQT type-I pole.

The old displayed cubic rational term has

    D_old = (WZZ) W2 - 2 W3 Z2 = 0

at the real Lorentzian algebraic-curvature point

    electric Weyl eigenvalues (1,5,-6),
    mixed Z eigenvalues (z0,1,1,-z0-2),
    z0 = -1 + 8/sqrt(61),

while its numerator is nonzero.

This script evaluates the alternative atlas invariants

    M22 = W_ab{}^{cd} (Z^2)_c{}^a (Z^2)_d{}^b,
    M23 = W_ab{}^{cd} (Z^2)_c{}^a (Z^3)_d{}^b,

directly on that same point.

Result:

    M22 = -138240/3721 != 0,
    M23 = +138240/3721,

so chart 1 is finite there and gives

    -W2 M23/M22 = 496.

Thus the old explicit denominator-zero point is chart-specific rather than
a common zero of these two rational representations.

This does not prove global regularity; the spherical simultaneous-zero gate
is tested separately.
"""

from __future__ import annotations

import itertools
import sympy as sp

eta = sp.diag(-1, 1, 1, 1)

Evals = (sp.Integer(1), sp.Integer(5), sp.Integer(-6))
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

def C_ab_upup(a: int, b: int, c: int, d: int) -> sp.Expr:
    return sp.simplify(
        sum(
            eta[c, e] * eta[d, f] * C[a, b, e, f]
            for e, f in itertools.product(range(4), repeat=2)
        )
    )

W2 = sp.factor(
    sum(
        C_ab_upup(a, b, c, d) * C_ab_upup(c, d, a, b)
        for a, b, c, d in itertools.product(range(4), repeat=4)
    )
)
W3 = sp.factor(
    sum(
        C_ab_upup(a, b, c, d)
        * C_ab_upup(c, d, e, f)
        * C_ab_upup(e, f, a, b)
        for a, b, c, d, e, f in itertools.product(range(4), repeat=6)
    )
)

z0 = sp.factor(-1 + 8 * sp.sqrt(61) / 61)
z = (z0, sp.Integer(1), sp.Integer(1), sp.factor(-z0 - 2))
Z = sp.diag(*z)
Z2mat = sp.simplify(Z**2)
Z3mat = sp.simplify(Z**3)

Z2 = sp.factor(sp.trace(Z2mat))

WZZ = sp.factor(
    sum(
        C_ab_upup(a, b, c, d)
        * Z[c, a]
        * Z[d, b]
        for a, b, c, d in itertools.product(range(4), repeat=4)
    )
)

D_old = sp.factor(WZZ * W2 - 2 * W3 * Z2)

M22 = sp.factor(
    sum(
        C_ab_upup(a, b, c, d)
        * Z2mat[c, a]
        * Z2mat[d, b]
        for a, b, c, d in itertools.product(range(4), repeat=4)
    )
)

M23 = sp.factor(
    sum(
        C_ab_upup(a, b, c, d)
        * Z2mat[c, a]
        * Z3mat[d, b]
        for a, b, c, d in itertools.product(range(4), repeat=4)
    )
)

T_alt = sp.factor(-W2 * M23 / M22)

assert W2 == 496
assert W3 == 1440
assert D_old == 0
assert M22 == -sp.Rational(138240, 3721)
assert M23 == sp.Rational(138240, 3721)
assert M22 != 0
assert T_alt == 496

def main() -> None:
    print("== NPQT atlas chart 1: old-pole coverage ==")
    print(f"W2 = {W2}")
    print(f"D_old = {D_old}")
    print(f"M22 = {M22}")
    print(f"M23 = {M23}")
    print(f"T_alt = -W2 M23/M22 = {T_alt}")
    print()
    print("Conclusion: the explicit old type-I pole is covered by chart 1.")
    print("The old denominator zero is therefore not a common zero of the")
    print("available invariant charts.")
    print("All old-pole coverage assertions passed.")

if __name__ == "__main__":
    main()
