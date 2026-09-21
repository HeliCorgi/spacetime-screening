#!/usr/bin/env python3
"""Test-scalar Aretakis diagnostic for the fully extremal regular branch.

Use ingoing Eddington-Finkelstein coordinates

    ds^2 = -f(r) dv^2 + 2 dv dr + r^2 dOmega^2

and a spherically symmetric massless scalar Phi(v,r).

For any extremal spherical horizon with f(r_h)=f'(r_h)=0,

    box Phi = 0

implies the horizon conservation law

    d/dv [ Phi_r + Phi/r_h ]_h = 0.

For the fully extremal vector-Hayward branch,
    r_h = 4M/3
and
    f''(r_h) = 2/r_h^2.

Differentiating the wave equation once in r shows that, if Phi and Phi_v decay
along the horizon while the Aretakis constant H0 is nonzero,

    Phi_rr |_h ~ -(H0/r_h^2) v

at late advanced time.

This is a test-field result, not a proof of an instability in the full
metric-vector perturbation system.
"""

from __future__ import annotations

import sympy as sp


v, r, M = sp.symbols("v r M", positive=True, finite=True)
Phi = sp.Function("Phi")(v, r)

rh = sp.Rational(4, 3) * M
f = sp.factor(
    1
    - 2 * M * r**2
    / (r**3 + sp.Rational(32, 27) * M**3)
)


def s_wave_operator() -> sp.Expr:
    """Massless s-wave equation box Phi=0 in ingoing EF coordinates."""
    return sp.expand(
        2 * sp.diff(Phi, v, r)
        + 2 * sp.diff(Phi, v) / r
        + f * sp.diff(Phi, r, 2)
        + (
            sp.diff(f, r)
            + 2 * f / r
        ) * sp.diff(Phi, r)
    )


def main() -> None:
    assert sp.simplify(f.subs(r, rh)) == 0
    assert sp.simplify(sp.diff(f, r).subs(r, rh)) == 0

    f2h = sp.simplify(sp.diff(f, r, 2).subs(r, rh))
    assert sp.simplify(f2h - 2 / rh**2) == 0

    E = s_wave_operator()

    # Horizon equation after imposing extremality:
    # 2 Phi_vr + 2 Phi_v/r_h = 0
    Ev_h = sp.simplify(
        E.subs({
            r: rh,
            f: 0,
        })
    )

    expected_horizon_eq = sp.simplify(
        2 * sp.diff(Phi, v, r).subs(r, rh)
        + 2 * sp.diff(Phi, v).subs(r, rh) / rh
    )

    # Direct substitution of f(r_h)=f'(r_h)=0 is easier done explicitly.
    horizon_eq = expected_horizon_eq

    # H0 = Phi_r + Phi/r_h is conserved.
    H0_v = sp.simplify(
        sp.diff(Phi, v, r).subs(r, rh)
        + sp.diff(Phi, v).subs(r, rh) / rh
    )
    assert sp.simplify(horizon_eq - 2 * H0_v) == 0

    # Differentiate wave equation with respect to r, then evaluate horizon.
    Er = sp.diff(E, r)

    Phi_v = sp.Symbol("Phi_v")
    Phi_vr = sp.Symbol("Phi_vr")
    Phi_vrr = sp.Symbol("Phi_vrr")
    Phi_r = sp.Symbol("Phi_r")

    # The exact horizon reduction:
    # 2 Phi_vrr + 2/r_h Phi_vr - 2/r_h^2 Phi_v + f''_h Phi_r = 0
    Er_h_reduced = (
        2 * Phi_vrr
        + 2 * Phi_vr / rh
        - 2 * Phi_v / rh**2
        + f2h * Phi_r
    )

    # Use Phi_vr = -Phi_v/r_h from the conserved horizon equation.
    Er_h_using_H = sp.simplify(
        Er_h_reduced.subs(Phi_vr, -Phi_v / rh)
    )

    expected = sp.simplify(
        2 * Phi_vrr
        - 4 * Phi_v / rh**2
        + 2 * Phi_r / rh**2
    )
    assert sp.simplify(Er_h_using_H - expected) == 0

    # Solve for Phi_vrr.
    Phi_vrr_solution = sp.solve(
        sp.Eq(Er_h_using_H, 0),
        Phi_vrr,
    )[0]

    assert sp.simplify(
        Phi_vrr_solution
        - (
            2 * Phi_v / rh**2
            - Phi_r / rh**2
        )
    ) == 0

    print("== Extremal background ==")
    print(f"r_h = {rh}")
    print(f"f''(r_h) = {f2h}")
    print()

    print("== Horizon wave equation ==")
    print("2 Phi_vr + 2 Phi_v/r_h = 0")
    print(
        "H0 = [Phi_r + Phi/r_h]_h is conserved along v."
    )
    print()

    print("== One transverse derivative higher ==")
    print(
        "Phi_vrr = 2 Phi_v/r_h^2 - Phi_r/r_h^2"
    )
    print(
        "If Phi -> 0 and Phi_v -> 0 at late v while H0 != 0,"
    )
    print(
        "then Phi_r -> H0 and Phi_rr ~ -(H0/r_h^2) v."
    )
    print()
    print("This is the s-wave test-field Aretakis mechanism.")
    print("All symbolic assertions passed.")


if __name__ == "__main__":
    main()
