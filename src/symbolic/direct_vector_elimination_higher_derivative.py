#!/usr/bin/env python3
"""Direct algebraic-vector elimination and hidden higher-derivative mode.

This uses coefficients obtained from the DIRECT original-action harmonic
expansion in direct_two_vector_odd_l2.py, not generalized-Proca formulas.

For the l=2 odd harmonic used there, the highest-time-derivative part of one
original vector sector is

    L_V^(2) ⊃ N [ C(r) u^2 + (p(r)/f(r)) u dot(X) ],

    N = 96 pi / 5,

where
    X = dot(W) - Q' + 2 Q/r

is the odd gauge-invariant Regge-Wheeler derivative combination, and

    C(r) = G^theta_theta + 2 nabla_mu V_bar^mu.

The vector perturbation u has no intrinsic derivative term and is algebraic:

    2 C u + (p/f) dot(X) = 0.

For the A-B theory the overall signs are +ell^2 and -ell^2, so eliminating
u_A and u_B gives

    L_eff ⊃ N ell^2 (b^2-a^2)/(4 f^2 C) dot(X)^2.

On the exact regular branch,

    b^2-a^2 = M q / [ r (r^3+2 q ell^2) ],

    C = 36 M q ell^2 r^3 / (r^3+2 q ell^2)^3,

hence

    L_eff ⊃ [2 pi/15] *
             (r^3+2 q ell^2)^2/(r^4 f^2) * dot(X)^2.

The coefficient is strictly positive and nonzero for r>0 away from metric
horizons.  Since X contains dot(W), dot(X) contains ddot(W).  In
Regge-Wheeler gauge for l>=2 this produces a nonzero Hessian with respect to
the highest time derivative ddot(W).

This is a direct hidden-higher-derivative diagnostic.  Calling the associated
mode a physical Ostrogradsky ghost still requires the complete constraint
analysis, but a nonzero highest-derivative Hessian is a substantially stronger
obstruction than the earlier heuristic kinetic-sign argument.
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
    (r - r * f - q / 2) / (2 * r**2)
)
b = sp.factor(
    (r - r * f + q / 2) / (2 * r**2)
)

C = sp.factor(
    36 * M * q * ell**2 * r**3 / D**3
)

b2_minus_a2 = sp.factor(
    b**2 - a**2
)

expected_diff = sp.factor(
    M * q / (r * D)
)

assert sp.simplify(
    b2_minus_a2 - expected_diff
) == 0


N = sp.Rational(96, 5) * pi

coeff_eff = sp.factor(
    N * ell**2
    * b2_minus_a2
    / (4 * f**2 * C)
)

expected_coeff = sp.factor(
    sp.Rational(2, 15)
    * pi
    * D**2
    / (r**4 * f**2)
)

assert sp.simplify(
    coeff_eff - expected_coeff
) == 0


# Algebraic elimination check using abstract Xdot.
xdot = sp.symbols("Xdot", real=True)

uA_star = sp.factor(
    -a * xdot / (2 * f * C)
)
uB_star = sp.factor(
    -b * xdot / (2 * f * C)
)

LA = sp.factor(
    N * ell**2
    * (
        C * uA_star**2
        + a * uA_star * xdot / f
    )
)

LB = sp.factor(
    -N * ell**2
    * (
        C * uB_star**2
        + b * uB_star * xdot / f
    )
)

Leff = sp.factor(LA + LB)

assert sp.simplify(
    Leff - coeff_eff * xdot**2
) == 0


# Highest-time-derivative Hessian.
# X = dot(W)-Q'+2Q/r, so dot(X) contains ddot(W) with unit coefficient.
Wdd = sp.symbols("Wdd", real=True)
highest = sp.expand(
    coeff_eff * Wdd**2
)

highest_hessian = sp.factor(
    sp.diff(highest, Wdd, 2)
)

assert sp.simplify(
    highest_hessian - 2 * coeff_eff
) == 0


# Endpoint scaling.
center_scaled = sp.simplify(
    sp.limit(
        r**4 * coeff_eff,
        r,
        0,
        dir="+",
    )
)

# f(0)=1 and D(0)=2 q ell^2.
expected_center = sp.factor(
    sp.Rational(8, 15)
    * pi
    * q**2
    * ell**4
)

assert sp.simplify(
    center_scaled - expected_center
) == 0

infinity_scaled = sp.simplify(
    sp.limit(
        coeff_eff / r**2,
        r,
        sp.oo,
    )
)

assert sp.simplify(
    infinity_scaled - sp.Rational(2, 15) * pi
) == 0


def main() -> None:
    print("== Direct algebraic-vector elimination ==")
    print(f"b^2-a^2 = {b2_minus_a2}")
    print(f"C(r) = {C}")
    print()
    print("u_A* =", uA_star)
    print("u_B* =", uB_star)
    print()
    print("effective highest-derivative coefficient:")
    print(coeff_eff)
    print()
    print("L_eff_high =", Leff)
    print("d^2 L / d(ddot W)^2 =", highest_hessian)
    print()
    print("Endpoint scaling:")
    print(f"r^4 coeff -> {center_scaled} at the regular center")
    print(f"coeff/r^2 -> {infinity_scaled} at infinity")
    print()
    print(
        "The coefficient of dot(X)^2 is nonzero throughout every regular "
        "static region with r>0."
    )
    print(
        "This exposes a hidden higher-time-derivative metric mode after the "
        "algebraic vectors are eliminated."
    )
    print("All direct elimination assertions passed.")


if __name__ == "__main__":
    main()
