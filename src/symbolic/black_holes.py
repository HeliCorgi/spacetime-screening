#!/usr/bin/env python3
"""Symbolic checks for Schwarzschild and Hayward black holes.

Metric convention:
    ds^2 = -f(r) dt^2 + dr^2/f(r) + r^2 dOmega^2

The script derives curvature invariants from f(r), verifies known limits,
and derives Hayward horizon thermodynamics.
"""

from __future__ import annotations

import sympy as sp


r, G, M, ell = sp.symbols("r G M ell", positive=True, finite=True)
rh = sp.symbols("r_h", positive=True, finite=True)


def spherical_invariants(f: sp.Expr) -> dict[str, sp.Expr]:
    """Return R, Ricci^2, and Kretschmann scalar for the metric ansatz."""
    fp = sp.diff(f, r)
    fpp = sp.diff(fp, r)

    ricci_scalar = sp.simplify(
        -fpp - 4 * fp / r + 2 * (1 - f) / r**2
    )

    # Mixed Ricci tensor has two doubly-degenerate eigenvalues:
    # -(f''/2 + f'/r) and -(f'/r + (f-1)/r^2).
    ricci_sq = sp.factor(
        2 * (fpp / 2 + fp / r) ** 2
        + 2 * (fp / r + (f - 1) / r**2) ** 2
    )

    kretschmann = sp.factor(
        fpp**2
        + 4 * (fp / r) ** 2
        + 4 * ((1 - f) / r**2) ** 2
    )

    return {
        "R": sp.factor(ricci_scalar),
        "Ricci2": ricci_sq,
        "K": kretschmann,
    }


def schwarzschild() -> dict[str, sp.Expr]:
    f = 1 - 2 * G * M / r
    inv = spherical_invariants(f)

    expected_k = 48 * G**2 * M**2 / r**6
    assert sp.simplify(inv["R"]) == 0
    assert sp.simplify(inv["Ricci2"]) == 0
    assert sp.simplify(inv["K"] - expected_k) == 0

    return {"f": f, **inv}


def hayward() -> dict[str, sp.Expr]:
    f = 1 - 2 * G * M * r**2 / (r**3 + 2 * G * M * ell**2)
    inv = spherical_invariants(f)

    expected_r = (
        24 * G**2 * M**2 * ell**2
        * (4 * G * M * ell**2 - r**3)
        / (r**3 + 2 * G * M * ell**2) ** 3
    )
    expected_ricci2 = (
        288 * G**4 * M**4 * ell**4
        * (
            8 * G**2 * M**2 * ell**4
            - 4 * G * M * ell**2 * r**3
            + 5 * r**6
        )
        / (r**3 + 2 * G * M * ell**2) ** 6
    )
    expected_k = (
        48 * G**2 * M**2
        * (
            32 * G**4 * M**4 * ell**8
            - 16 * G**3 * M**3 * ell**6 * r**3
            + 72 * G**2 * M**2 * ell**4 * r**6
            - 8 * G * M * ell**2 * r**9
            + r**12
        )
        / (r**3 + 2 * G * M * ell**2) ** 6
    )

    assert sp.simplify(inv["R"] - expected_r) == 0
    assert sp.simplify(inv["Ricci2"] - expected_ricci2) == 0
    assert sp.simplify(inv["K"] - expected_k) == 0

    # Center limits: de Sitter core.
    assert sp.simplify(sp.limit(inv["R"], r, 0) - 12 / ell**2) == 0
    assert sp.simplify(sp.limit(inv["Ricci2"], r, 0) - 36 / ell**4) == 0
    assert sp.simplify(sp.limit(inv["K"], r, 0) - 24 / ell**4) == 0

    # Large-r limit: Schwarzschild curvature.
    assert sp.limit(inv["R"], r, sp.oo) == 0
    assert sp.limit(inv["Ricci2"], r, sp.oo) == 0
    assert sp.limit(
        sp.simplify(inv["K"] / (48 * G**2 * M**2 / r**6)),
        r,
        sp.oo,
    ) == 1

    return {"f": f, **inv}


def hayward_horizon_thermodynamics(f: sp.Expr) -> dict[str, sp.Expr]:
    # f(r_h)=0 gives M as a function of horizon radius.
    mass_on_horizon = sp.factor(rh**3 / (2 * G * (rh**2 - ell**2)))

    fprime_h = sp.factor(
        sp.diff(f, r).subs({r: rh, M: mass_on_horizon})
    )

    # For the outer horizon, r_h >= sqrt(3) ell and f'(r_h) >= 0.
    kappa_outer = sp.factor(fprime_h / 2)
    temperature_outer = sp.factor(fprime_h / (4 * sp.pi))

    extremal_radius = sp.sqrt(3) * ell
    extremal_mass = sp.simplify(
        mass_on_horizon.subs(rh, extremal_radius)
    )

    dT = sp.factor(sp.diff(temperature_outer, rh))
    temperature_peak_radius = 3 * ell
    temperature_max = sp.simplify(
        temperature_outer.subs(rh, temperature_peak_radius)
    )

    assert sp.simplify(
        fprime_h - (rh**2 - 3 * ell**2) / rh**3
    ) == 0
    assert sp.simplify(
        extremal_mass - 3 * sp.sqrt(3) * ell / (4 * G)
    ) == 0
    assert sp.simplify(
        temperature_max - 1 / (18 * sp.pi * ell)
    ) == 0
    assert sp.simplify(dT.subs(rh, 3 * ell)) == 0

    horizon_polynomial = r**3 - 2 * G * M * r**2 + 2 * G * M * ell**2

    return {
        "horizon_polynomial": horizon_polynomial,
        "M(r_h)": mass_on_horizon,
        "fprime(r_h)": fprime_h,
        "kappa_outer": kappa_outer,
        "T_outer": temperature_outer,
        "r_ext": extremal_radius,
        "M_ext": extremal_mass,
        "r_Tmax": temperature_peak_radius,
        "T_max": temperature_max,
    }


def print_block(title: str, data: dict[str, sp.Expr]) -> None:
    print(f"\n== {title} ==")
    for key, value in data.items():
        print(f"{key} = {sp.factor(value)}")


def main() -> None:
    sch = schwarzschild()
    hay = hayward()
    thermo = hayward_horizon_thermodynamics(hay["f"])

    print_block("Schwarzschild", sch)
    print_block("Hayward", hay)
    print("\nHayward small-r f(r):")
    print(sp.series(hay["f"], r, 0, 9))
    print_block("Hayward horizons and thermodynamics", thermo)
    print("\nAll symbolic assertions passed.")


if __name__ == "__main__":
    main()
