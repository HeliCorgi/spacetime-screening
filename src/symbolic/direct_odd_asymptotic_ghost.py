#!/usr/bin/env python3
"""Direct asymptotic odd-sector constraint reduction and ghost sign.

This calculation uses ONLY coefficients independently obtained from the
original A-B harmonic expansion:

    direct_two_vector_odd_l2.py
    direct_two_vector_odd_principal_tr.py

No generalized-Proca odd coefficient is imported.

After passing to active/null vector combinations

    U = (-a u_A + b u_B)/n,
    V = ( b u_A + a u_B)/n,
    n^2=a^2+b^2,

the direct temporal quadratic action has:

- two velocity-active variables W and U;
- no velocity for Q;
- no velocity for V.

The null V field has nonzero algebraic V^2 stiffness on the regular branch.
The direct Q-V algebraic mixing vanishes identically.

Thus, in any region where the Q^2 coefficient E_Q is nonzero, Q and V form
ordinary auxiliary/second-class directions and can be eliminated locally.

This script performs that elimination for the kinetic sector and proves that
the remaining (W,U) Hessian determinant is NEGATIVE in the asymptotic exterior:

    det K_red
      ~ - [1152 pi^2 M ell^4 (16 M^2+q^2)] / [25 r^5] < 0.

Therefore, for every M,q,ell>0, sufficiently large but finite r contains one
positive- and one negative-kinetic odd mode after the direct auxiliary
reduction.

At the same time the negative eigenvalue tends to zero as r->infinity,
connecting the ghost sign to the previously found asymptotic strong-coupling
degeneracy.

This is substantially stronger than the earlier "ghost candidate" statement:
within the l=2 quadratic theory and in the asymptotic exterior, the direct
source-action reduction leaves a negative physical kinetic eigenvalue.

A full global-in-r Dirac analysis is still needed to classify every special
surface where the auxiliary rank may change.
"""

from __future__ import annotations

import sympy as sp


r, M, q, ell = sp.symbols(
    "r M q ell", positive=True, finite=True
)
pi = sp.pi

D = r**3 + 2 * q * ell**2
f = sp.factor(
    1 - 2 * M * r**2 / D
)

a = sp.factor(
    (r - r * f - q / 2)
    / (2 * r**2)
)

b = sp.factor(
    (r - r * f + q / 2)
    / (2 * r**2)
)

n2 = sp.factor(
    a**2 + b**2
)

fp = sp.diff(f, r)
fpp = sp.diff(f, r, 2)


# ---------------------------------------------------------------------------
# Direct Q^2 coefficient from the original l=2 quadratic expansion.
# ---------------------------------------------------------------------------

E_EH = sp.factor(
    12 * pi
    * (
        r**2 * f * fpp
        - r**2 * fp**2
        - 2 * r * f * fp
        - 2 * f**2
        + 6 * f
    )
    / (
        5 * r**2 * f**2
    )
)


def E_vec(p: sp.Expr) -> sp.Expr:
    return sp.factor(
        96 * pi
        * (
            2 * r**2 * sp.diff(p, r)
            + 4 * r * p
            - f
            - 3
        )
        * p**2
        / (
            5 * r**2 * f**2
        )
    )


E_Q = sp.factor(
    E_EH
    + ell**2
    * (
        E_vec(a)
        - E_vec(b)
    )
)

assert sp.simplify(
    sp.limit(
        r**2 * E_Q,
        r,
        sp.oo,
    )
    - 48 * pi / 5
) == 0


# ---------------------------------------------------------------------------
# Direct Q-u algebraic coefficient.
# ---------------------------------------------------------------------------

def F_Qu(p: sp.Expr) -> sp.Expr:
    return sp.factor(
        192 * pi
        * p
        * (
            2 * r**2 * sp.diff(p, r)
            + 4 * r * p
            + r * fp
            - 3
        )
        / (
            5 * r**2 * f
        )
    )


F_A = F_Qu(a)
F_B = F_Qu(b)

# Full A-B Q-u term is ell^2 Q [F_A u_A - F_B u_B].
# In active/null variables:
#   u_A=(-a U+b V)/n
#   u_B=( b U+a V)/n
# so QV coefficient is proportional to b F_A-a F_B.
QV_numerator = sp.factor(
    b * F_A
    - a * F_B
)

assert sp.simplify(
    QV_numerator
) == 0


# ---------------------------------------------------------------------------
# Direct algebraic stiffness of the derivative-null V combination.
# ---------------------------------------------------------------------------

C = sp.factor(
    36 * M * q * ell**2 * r**3
    / D**3
)

N = sp.Rational(96, 5) * pi

b2_minus_a2 = sp.factor(
    b**2 - a**2
)

assert sp.simplify(
    b2_minus_a2
    - M * q / (r * D)
) == 0

mV = sp.factor(
    N
    * ell**2
    * C
    * b2_minus_a2
    / n2
)

# mV is manifestly positive for positive parameters.
assert sp.simplify(
    sp.limit(
        r**6 * mV,
        r,
        sp.oo,
    )
    - (
        sp.Rational(27648, 5)
        * pi
        * M**2
        * ell**4
        * q**2
        / (
            16 * M**2 + q**2
        )
    )
) == 0


# ---------------------------------------------------------------------------
# Direct active (W,U) temporal kinetic matrix before/after Q elimination.
# ---------------------------------------------------------------------------

A = sp.Rational(12, 5) * pi

# L contains h Wdot Udot.
h = sp.factor(
    96 * pi
    * ell**2
    * sp.sqrt(n2)
    / (
        5 * f
    )
)

# Q couples as Cw Q Wdot + d Q Udot.
Cw = sp.factor(
    48 * pi
    / (
        5 * r
    )
)

d = sp.factor(
    2 * h / r
)

# Eliminate Q:
#   Q* = -(Cw Wdot+d Udot)/(2 E_Q).
# Reduced L coefficients:
Ared = sp.factor(
    A
    - Cw**2
    / (
        4 * E_Q
    )
)

hred = sp.factor(
    h
    - Cw * d
    / (
        2 * E_Q
    )
)

U2red = sp.factor(
    -d**2
    / (
        4 * E_Q
    )
)

# Hessian in (Wdot,Udot):
# [[2 Ared, hred],
#  [hred, 2 U2red]]
detK = sp.factor(
    4 * Ared * U2red
    - hred**2
)

# Useful exact simplification.
det_expected = sp.factor(
    h**2
    * (
        -1
        + 48 * pi
        / (
            5 * E_Q * r**2
        )
    )
)

assert sp.simplify(
    detK - det_expected
) == 0


# Asymptotic sign.
asym_det = sp.simplify(
    sp.limit(
        r**5 * detK,
        r,
        sp.oo,
    )
)

expected_asym_det = sp.factor(
    -sp.Rational(1152, 25)
    * pi**2
    * M
    * ell**4
    * (
        16 * M**2
        + q**2
    )
)

assert sp.simplify(
    asym_det
    - expected_asym_det
) == 0

# Strictly negative for positive M,ell and nonzero hair parameters.
assert expected_asym_det.could_extract_minus_sign()


# Q is an ordinary auxiliary asymptotically because E_Q>0 there.
E_asym = sp.simplify(
    sp.limit(
        r**2 * E_Q,
        r,
        sp.oo,
    )
)

# V is an ordinary auxiliary asymptotically because mV>0 there.
mV_asym = sp.simplify(
    sp.limit(
        r**6 * mV,
        r,
        sp.oo,
    )
)


def main() -> None:
    print("== Direct asymptotic auxiliary reduction ==")
    print(f"lim r^2 E_Q = {E_asym}")
    print(f"Q-V mixing numerator = {QV_numerator}")
    print(f"lim r^6 m_V = {mV_asym}")
    print()
    print("Q and V are therefore nondegenerate auxiliary directions")
    print("throughout a sufficiently large-r open region.")
    print()
    print("== Reduced (W,U) kinetic determinant ==")
    print(f"det K_red = {detK}")
    print()
    print("asymptotic coefficient:")
    print(f"lim r^5 det K_red = {asym_det}")
    print()
    print(
        "For M,q,ell>0 this is strictly negative, so the two remaining "
        "odd kinetic eigenvalues have opposite signs."
    )
    print()
    print(
        "Thus the direct original-action l=2 quadratic theory contains an "
        "asymptotic negative-kinetic odd mode after the two auxiliary "
        "directions are locally eliminated."
    )
    print(
        "The global-in-r constraint classification remains open at special "
        "rank-changing surfaces."
    )
    print("All direct asymptotic constraint assertions passed.")


if __name__ == "__main__":
    main()
