#!/usr/bin/env python3
"""First alternative rational chart for the NPQT spherical target.

Define the mixed invariants

    M22 = W_ab{}^{cd} (Z^2)_c{}^a (Z^2)_d{}^b,
    M23 = W_ab{}^{cd} (Z^2)_c{}^a (Z^3)_d{}^b.

On the general local spherical algebraic-curvature family used in the
repository,

    W: type-D purely electric, eigenvalues (-2q,q,q),
    Z_ab = [[a,b,0,0],[b,a-2Theta,0,0],[0,0,Theta,0],[0,0,0,Theta]],

one finds exactly

    M23 = -Theta M22.

Therefore, wherever M22 != 0,

    T_alt = -W2 M23/M22 = W2 Theta,

which reproduces the exact spherical target of the displayed cubic NPQT
rational term.

This is an invariant-atlas chart only.  It is not yet a globally regular
representative.
"""

from __future__ import annotations

import itertools
import sympy as sp

eta = sp.diag(-1, 1, 1, 1)

q, a, b, theta = sp.symbols("q a b theta", real=True)
E = sp.diag(-2 * q, q, q)

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

def C_ab_upup(aa: int, bb: int, cc: int, dd: int) -> sp.Expr:
    return sp.simplify(
        sum(
            eta[cc, e] * eta[dd, f] * C[aa, bb, e, f]
            for e, f in itertools.product(range(4), repeat=2)
        )
    )

Zcov = sp.Matrix(
    [
        [a, b, 0, 0],
        [b, a - 2 * theta, 0, 0],
        [0, 0, theta, 0],
        [0, 0, 0, theta],
    ]
)
Z = eta * Zcov

assert sp.trace(Z) == 0

Z2mat = sp.simplify(Z**2)
Z3mat = sp.simplify(Z**3)

W2 = sp.factor(
    sum(
        C_ab_upup(a0, b0, c0, d0) * C_ab_upup(c0, d0, a0, b0)
        for a0, b0, c0, d0 in itertools.product(range(4), repeat=4)
    )
)

M22 = sp.factor(
    sum(
        C_ab_upup(a0, b0, c0, d0)
        * Z2mat[c0, a0]
        * Z2mat[d0, b0]
        for a0, b0, c0, d0 in itertools.product(range(4), repeat=4)
    )
)

M23 = sp.factor(
    sum(
        C_ab_upup(a0, b0, c0, d0)
        * Z2mat[c0, a0]
        * Z3mat[d0, b0]
        for a0, b0, c0, d0 in itertools.product(range(4), repeat=4)
    )
)

F = sp.factor((a - theta) ** 2 - b**2)
S = sp.factor(-a**2 + 2 * a * theta + b**2 + 3 * theta**2)

assert W2 == 48 * q**2
assert sp.expand(M22 + 4 * q * F * S) == 0
assert sp.expand(M23 - 4 * q * theta * F * S) == 0
assert sp.simplify(M23 + theta * M22) == 0

T_alt = sp.factor(-W2 * M23 / M22)
assert sp.simplify(T_alt - W2 * theta) == 0

def main() -> None:
    print("== NPQT mixed-invariant atlas: chart 1 ==")
    print(f"W2  = {W2}")
    print(f"M22 = {M22}")
    print(f"M23 = {M23}")
    print()
    print("Exact spherical identity:")
    print("M23 = -Theta M22")
    print(f"T_alt = -W2 M23/M22 = {T_alt}")
    print()
    print("Conclusion: this gives a branch-free covariant rational chart for")
    print("the spherical target wherever M22 is nonzero.")
    print("All chart-1 assertions passed.")

if __name__ == "__main__":
    main()
