#!/usr/bin/env python3
"""Scalar-invariant sign-blind gate at the NPQT simultaneous-zero stratum.

Consider the aligned spherical/type-D algebraic curvature point

    electric Weyl eigenvalues (-2q,q,q),
    mixed traceless-Ricci eigenvalues (-theta,-theta,theta,theta).

Then

    Z^2 = theta^2 I.

The two configurations theta and -theta have the same low-degree scalar
polynomial invariants relevant to the standard Carminati-McLenaghan
spherical generator set.

In particular:
- pure Ricci odd trace Z3 vanishes;
- the cubic mixed invariant WZZ is even in theta;
- the direct W^2 Z scalar vanishes by the 4D Weyl identity;
- the CM-type odd quintic contraction M4 (two Weyl, three Z), including its
  dual-Weyl partner, vanishes at this aligned point.

All other standard CM generators contain an even number of traceless-Ricci
factors or are pure Weyl/Ricci-even at this stratum.

This is evidence for a scalar-polynomial-invariant sign-blind obstruction:
an expression depending only on these scalar invariants cannot reproduce a
quantity proportional to W2*theta on both theta-sign branches.

Scope: this script checks the algebraic stratum and the relevant generator
parity.  The use of the CM set as a complete spherical invariant set is a
literature input, not proved by this script.
"""

from __future__ import annotations

import itertools
import sympy as sp

eta = sp.diag(-1, 1, 1, 1)

q, theta = sp.symbols("q theta", real=True)
E = sp.diag(-2 * q, q, q)

def eps3(i: int, j: int, k: int) -> sp.Expr:
    return sp.LeviCivita(i - 1, j - 1, k - 1)

def eps4(a: int, b: int, c: int, d: int) -> sp.Expr:
    return sp.LeviCivita(a, b, c, d)

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

def C_ac_updb(a: int, c: int, d: int, b: int) -> sp.Expr:
    return sp.simplify(
        sum(
            eta[d, m] * eta[b, n] * C[a, c, m, n]
            for m, n in itertools.product(range(4), repeat=2)
        )
    )

Star = sp.MutableDenseNDimArray.zeros(4, 4, 4, 4)
for a, b, c, d in itertools.product(range(4), repeat=4):
    Star[a, b, c, d] = sp.simplify(
        sp.Rational(1, 2)
        * sum(
            eps4(a, b, p, r) * eta[p, m] * eta[r, n] * C[m, n, c, d]
            for p, r, m, n in itertools.product(range(4), repeat=4)
        )
    )

def Star_ac_updb(a: int, c: int, d: int, b: int) -> sp.Expr:
    return sp.simplify(
        sum(
            eta[d, m] * eta[b, n] * Star[a, c, m, n]
            for m, n in itertools.product(range(4), repeat=2)
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

Z = sp.diag(-theta, -theta, theta, theta)
Zminus = -Z

assert sp.simplify(Z**2 - theta**2 * sp.eye(4)) == sp.zeros(4)

def basic_invariants(Zm: sp.Matrix):
    Z2 = sp.factor(sp.trace(Zm**2))
    Z3 = sp.factor(sp.trace(Zm**3))
    Z4 = sp.factor(sp.trace(Zm**4))
    WZZ = sp.factor(
        sum(
            C_ab_upup(a, b, c, d) * Zm[c, a] * Zm[d, b]
            for a, b, c, d in itertools.product(range(4), repeat=4)
        )
    )
    return Z2, Z3, Z4, WZZ

plus = basic_invariants(Z)
minus = basic_invariants(Zminus)

assert plus == minus
Z2, Z3, Z4, WZZ = plus
assert Z2 == 4 * theta**2
assert Z3 == 0
assert Z4 == 4 * theta**4
assert WZZ == 16 * q * theta**2

# Direct cubic W^2 Z scalar.
Zcov = eta * Z
Zup = eta * Zcov * eta

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

W2Z = sp.factor(
    sum(Zup[a, b] * S[a, b] for a, b in itertools.product(range(4), repeat=2))
)
assert W2Z == 0

# CM-M4-type numerator, normalization omitted:
# Z^{ag} Z^{ef} Z^c_d [ C_ac^{db} C_befg + *C_ac^{db} *C_befg ].
def odd_quintic(Zm: sp.Matrix):
    Zcov_m = eta * Zm
    Zup_m = eta * Zcov_m * eta
    value = 0
    for a, c, d, b, e, f, g in itertools.product(range(4), repeat=7):
        value += (
            Zup_m[a, g]
            * Zup_m[e, f]
            * Zm[c, d]
            * (
                C_ac_updb(a, c, d, b) * C[b, e, f, g]
                + Star_ac_updb(a, c, d, b) * Star[b, e, f, g]
            )
        )
    return sp.factor(value)

M4_plus = odd_quintic(Z)
M4_minus = odd_quintic(Zminus)

assert M4_plus == 0
assert M4_minus == 0

assert W2 == 48 * q**2
assert W3 == 96 * q**3

def main() -> None:
    print("== NPQT spherical sign-blind SPI gate ==")
    print(f"W2 = {W2}")
    print(f"W3 = {W3}")
    print(f"Z2 = {Z2}")
    print(f"Z3 = {Z3}")
    print(f"Z4 = {Z4}")
    print(f"WZZ = {WZZ}")
    print(f"W^2 Z cubic = {W2Z}")
    print(f"CM-type odd quintic M4 numerator = {M4_plus}")
    print()
    print("The checked spherical scalar generators are unchanged under")
    print("theta -> -theta at this aligned simultaneous-zero stratum.")
    print("A scalar-invariant-only lift of W2*theta therefore faces a")
    print("discrete sign-information obstruction here.")
    print("All sign-blind-gate assertions passed.")

if __name__ == "__main__":
    main()
