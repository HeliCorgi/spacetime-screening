#!/usr/bin/env python3
"""C0 gate for NPQT mixed-invariant atlas chart 1.

Chart 1 is

    T_alt = -W2 M23/M22,

with

    M22 = W_ab{}^{cd} (Z^2)_c{}^a (Z^2)_d{}^b,
    M23 = W_ab{}^{cd} (Z^2)_c{}^a (Z^3)_d{}^b.

It reproduces W2*Theta on the spherical locus and covers the explicit old
type-I pole.

This script tests the spherical simultaneous-zero point

    type-D Weyl eigenvalues (-2q,q,q),
    mixed Z eigenvalues (-theta,-theta,theta,theta).

At that point M22=M23=0.

Two exact type-D-Weyl paths are compared:

1. spherical Ricci path
       z = (-theta+eps, -theta-eps, theta, theta),

2. off-spherical Ricci path
       z = (-theta+eps, -theta+eps, theta, theta-2eps).

The punctured chart tends to +48 q^2 theta on path 1 and
-48 q^2 theta on path 2.

Therefore chart 1 has no continuous extension at this simultaneous zero.

This does not kill the invariant-atlas strategy; it shows that chart 1 and
the old chart have complementary strengths but neither is a single global
C0 representative.
"""

from __future__ import annotations

import itertools
import sympy as sp

eta = sp.diag(-1, 1, 1, 1)

q, theta, eps = sp.symbols("q theta eps", real=True, nonzero=True)
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
assert W2 == 48 * q**2

def chart_for(zvals):
    Z = sp.diag(*zvals)
    Z2mat = sp.simplify(Z**2)
    Z3mat = sp.simplify(Z**3)

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
    T = sp.factor(-W2 * M23 / M22)
    return M22, M23, T

base = (-theta, -theta, theta, theta)
M22_base, M23_base, _ = chart_for(base)
assert M22_base == 0
assert M23_base == 0

spherical_path = (-theta + eps, -theta - eps, theta, theta)
off_path = (-theta + eps, -theta + eps, theta, theta - 2 * eps)

M22_sph, M23_sph, T_sph = chart_for(spherical_path)
M22_off, M23_off, T_off = chart_for(off_path)

lim_sph = sp.factor(sp.limit(T_sph, eps, 0))
lim_off = sp.factor(sp.limit(T_off, eps, 0))

assert lim_sph == 48 * q**2 * theta
assert lim_off == -48 * q**2 * theta
assert sp.simplify(lim_sph - lim_off) == 96 * q**2 * theta

def main() -> None:
    print("== NPQT atlas chart 1: simultaneous-zero C0 gate ==")
    print(f"M22(base) = {M22_base}")
    print(f"M23(base) = {M23_base}")
    print()
    print("Spherical path:")
    print(f"  M22 = {M22_sph}")
    print(f"  M23 = {M23_sph}")
    print(f"  T_alt -> {lim_sph}")
    print()
    print("Off-spherical Ricci path:")
    print(f"  M22 = {M22_off}")
    print(f"  M23 = {M23_off}")
    print(f"  T_alt -> {lim_off}")
    print()
    print("Conclusion: chart 1 is not C0 at the spherical simultaneous zero.")
    print("It covers the old type-I pole but is not a global representative.")
    print("All chart-1 C0 assertions passed.")

if __name__ == "__main__":
    main()
