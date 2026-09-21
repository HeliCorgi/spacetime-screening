#!/usr/bin/env python3
"""No-go check for a minimal static radial scalar-tensor support of Hayward.

Action:
    S = ∫ sqrt(-g) [ F(chi) R/(16*pi*G)
                    - 1/2 (∂chi)^2 - V(chi) ]

Metric ansatz:
    ds^2 = -f(r) dt^2 + dr^2/f(r) + r^2 dOmega^2

Scalar ansatz:
    chi = chi(r)

For this one-function metric, G^t_t = G^r_r identically.
The difference of the scalar-tensor field equations implies

    F''(r) = -8*pi*G * chi'(r)^2.

Thus F(r) is concave. If both the center and infinity are regular with
F'(0)=F'(infinity)=0, then F' must vanish identically, hence chi'=0.
So a nontrivial localized static radial canonical scalar cannot support
a Hayward-type one-function geometry in this minimal theory.

The same logic extends to k-essence with positive P_X:
    F'' = -8*pi*G * P_X * chi'^2 <= 0.
"""

from __future__ import annotations

import sympy as sp


r, G, M, ell = sp.symbols("r G M ell", positive=True, finite=True)
f = sp.Function("f")(r)
chi = sp.Function("chi")(r)
F = sp.Function("F")(r)
V = sp.Function("V")(r)

pi = sp.pi


def scalar_tensor_difference() -> sp.Expr:
    """Return rr - tt equation residual for the minimal scalar-tensor ansatz."""
    fp = sp.diff(f, r)
    chip = sp.diff(chi, r)
    Fp = sp.diff(F, r)
    Fpp = sp.diff(F, r, 2)

    # Canonical scalar mixed components:
    # T^t_t = -1/2 f chi'^2 - V
    # T^r_r = +1/2 f chi'^2 - V
    Ttt = -sp.Rational(1, 2) * f * chip**2 - V
    Trr = +sp.Rational(1, 2) * f * chip**2 - V

    # Mixed second derivatives of F(r):
    # ∇^t∇_t F = f'/2 F'
    # ∇^r∇_r F = f F'' + f'/2 F'
    nabla_t = fp * Fp / 2
    nabla_r = f * Fpp + fp * Fp / 2

    # Since G^r_r-G^t_t=0 for ds²=-f dt²+dr²/f+...
    residual = sp.factor(
        8 * pi * G * (Trr - Ttt)
        + (nabla_r - nabla_t)
    )

    expected = sp.factor(
        f * (Fpp + 8 * pi * G * chip**2)
    )
    assert sp.simplify(residual - expected) == 0
    return residual


def hayward_anisotropy() -> sp.Expr:
    """Show Hayward is not an Einstein space away from r=0."""
    fh = 1 - 2 * G * M * r**2 / (r**3 + 2 * G * M * ell**2)
    fp = sp.diff(fh, r)
    fpp = sp.diff(fh, r, 2)

    Gtt = sp.simplify((r * fp + fh - 1) / r**2)
    Grr = Gtt
    Gth = sp.simplify(fpp / 2 + fp / r)

    assert sp.simplify(Grr - Gtt) == 0

    delta = sp.factor(Gth - Gtt)
    expected = sp.factor(
        36 * G**2 * M**2 * ell**2 * r**3
        / (r**3 + 2 * G * M * ell**2) ** 3
    )
    assert sp.simplify(delta - expected) == 0
    return delta


def k_essence_extension() -> sp.Expr:
    """Symbolic form of the generalized radial difference equation.

    For L=P(X,chi), T^r_r-T^t_t = P_X f chi'^2.
    The field-equation difference becomes
        f [F'' + 8*pi*G P_X chi'^2] = 0.
    """
    PX = sp.symbols("P_X", nonnegative=True)
    chip = sp.diff(chi, r)
    Fpp = sp.diff(F, r, 2)
    return sp.factor(
        f * (Fpp + 8 * pi * G * PX * chip**2)
    )


def main() -> None:
    canonical = scalar_tensor_difference()
    hayward_delta = hayward_anisotropy()
    kessence = k_essence_extension()

    print("== Minimal scalar-tensor rr-tt residual ==")
    print(canonical)
    print()
    print("For f != 0:")
    print("F''(r) = -8*pi*G*chi'(r)^2 <= 0")
    print()
    print("Regular localized boundary conditions:")
    print("F'(0)=0 and F'(infinity)=0")
    print("Concavity then forces F'(r)=0 everywhere, hence chi'(r)=0.")
    print()
    print("== Hayward angular anisotropy ==")
    print("G^theta_theta - G^t_t =")
    print(hayward_delta)
    print("This is nonzero for r>0, so constant chi/F plus a potential")
    print("cannot reproduce the full Hayward geometry.")
    print()
    print("== Stable radial k-essence generalization ==")
    print(kessence)
    print("If P_X >= 0, the same concavity obstruction remains.")
    print()
    print("All symbolic assertions passed.")


if __name__ == "__main__":
    main()
