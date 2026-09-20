#!/usr/bin/env python3
"""Effective stress-energy required by the Hayward metric in Einstein gravity.

We interpret the Hayward geometry through the ordinary Einstein equation

    G^mu_nu = 8*pi*G * T^mu_nu

with anisotropic effective stress tensor

    T^mu_nu = diag(-rho, p_r, p_t, p_t).

This is an *effective GR source* for the chosen geometry. It need not be the
fundamental matter stress tensor of an underlying modified-gravity or
quantum-gravity completion.
"""

from __future__ import annotations

import sympy as sp


r, G, M, ell = sp.symbols("r G M ell", positive=True, finite=True)
pi = sp.pi

D = r**3 + 2 * G * M * ell**2
f = 1 - 2 * G * M * r**2 / D


def einstein_components(f_expr: sp.Expr) -> dict[str, sp.Expr]:
    """Mixed Einstein-tensor components for ds^2=-f dt^2+dr^2/f+r^2 dOmega^2."""
    fp = sp.diff(f_expr, r)
    fpp = sp.diff(fp, r)

    gtt = sp.simplify((r * fp + f_expr - 1) / r**2)
    grr = gtt
    gtheta = sp.simplify(fpp / 2 + fp / r)

    return {
        "G^t_t": sp.factor(gtt),
        "G^r_r": sp.factor(grr),
        "G^theta_theta": sp.factor(gtheta),
    }


def effective_fluid() -> dict[str, sp.Expr]:
    E = einstein_components(f)

    rho = sp.factor(-E["G^t_t"] / (8 * pi * G))
    p_r = sp.factor(E["G^r_r"] / (8 * pi * G))
    p_t = sp.factor(E["G^theta_theta"] / (8 * pi * G))

    return {
        "rho": rho,
        "p_r": p_r,
        "p_t": p_t,
    }


def energy_condition_combinations(
    rho: sp.Expr, p_r: sp.Expr, p_t: sp.Expr
) -> dict[str, sp.Expr]:
    return {
        "rho+p_r": sp.factor(rho + p_r),
        "rho+p_t": sp.factor(rho + p_t),
        "rho+p_r+2p_t": sp.factor(rho + p_r + 2 * p_t),
        "rho-p_t": sp.factor(rho - p_t),
        "trace_T": sp.factor(-rho + p_r + 2 * p_t),
        "anisotropy_p_t-p_r": sp.factor(p_t - p_r),
    }


def mass_function() -> sp.Expr:
    """m(r) defined by f=1-2Gm(r)/r."""
    return sp.factor(M * r**3 / D)


def main() -> None:
    fluid = effective_fluid()
    rho = fluid["rho"]
    p_r = fluid["p_r"]
    p_t = fluid["p_t"]

    combos = energy_condition_combinations(rho, p_r, p_t)
    m = mass_function()

    expected_rho = (
        3 * G * M**2 * ell**2
        / (2 * pi * D**2)
    )
    expected_pr = -expected_rho
    expected_pt = (
        3 * G * M**2 * ell**2
        * (r**3 - G * M * ell**2)
        / (pi * D**3)
    )

    assert sp.simplify(rho - expected_rho) == 0
    assert sp.simplify(p_r - expected_pr) == 0
    assert sp.simplify(p_t - expected_pt) == 0

    # Effective mass density relation.
    assert sp.simplify(sp.diff(m, r) - 4 * pi * r**2 * rho) == 0
    assert sp.limit(m, r, 0) == 0
    assert sp.limit(m, r, sp.oo) == M

    # Bianchi / anisotropic-fluid conservation equation.
    fp = sp.diff(f, r)
    conservation = sp.factor(
        sp.diff(p_r, r)
        + (rho + p_r) * fp / (2 * f)
        + 2 * (p_r - p_t) / r
    )
    assert sp.simplify(conservation) == 0

    # De Sitter-like center.
    rho0 = sp.limit(rho, r, 0)
    pr0 = sp.limit(p_r, r, 0)
    pt0 = sp.limit(p_t, r, 0)

    expected_rho0 = 3 / (8 * pi * G * ell**2)
    assert sp.simplify(rho0 - expected_rho0) == 0
    assert sp.simplify(pr0 + expected_rho0) == 0
    assert sp.simplify(pt0 + expected_rho0) == 0

    # Equation-of-state ratio for tangential pressure.
    x = sp.symbols("x", nonnegative=True)
    pt_over_rho = sp.factor(p_t / rho)
    pt_over_rho_x = sp.factor(
        pt_over_rho.subs(r**3, x * G * M * ell**2)
    )
    assert sp.simplify(pt_over_rho_x - 2 * (x - 1) / (x + 2)) == 0

    # Energy-condition boundaries:
    # SEC changes sign when p_t=0 => r^3 = G M ell^2.
    r_sec = (G * M * ell**2) ** sp.Rational(1, 3)

    # DEC tangential bound rho >= p_t changes sign when rho-p_t=0
    # => r^3 = 4 G M ell^2.  The lower bound p_t >= -rho is
    # automatically satisfied for r>=0.
    r_dec = (4 * G * M * ell**2) ** sp.Rational(1, 3)

    # Trace relation from Einstein equations: R = -8*pi*G*T.
    R_scalar = sp.factor(
        -sp.diff(f, r, 2)
        - 4 * sp.diff(f, r) / r
        + 2 * (1 - f) / r**2
    )
    assert sp.simplify(R_scalar + 8 * pi * G * combos["trace_T"]) == 0

    print("== Hayward effective stress-energy ==")
    for key, value in fluid.items():
        print(f"{key} = {value}")

    print("\n== Useful combinations ==")
    for key, value in combos.items():
        print(f"{key} = {value}")

    print("\n== Center ==")
    print(f"rho(0) = {rho0}")
    print(f"p_r(0) = {pr0}")
    print(f"p_t(0) = {pt0}")

    print("\n== Tangential equation of state ==")
    print("x = r^3/(G M ell^2)")
    print(f"p_t/rho = {pt_over_rho_x}")

    print("\n== Energy conditions ==")
    print("NEC: satisfied everywhere; radial NEC is saturated.")
    print("WEC: satisfied everywhere.")
    print(f"SEC: violated for r < {r_sec}; saturated at r = {r_sec}.")
    print(
        "DEC: satisfied for 0 <= r <= "
        f"{r_dec}; violated for r > {r_dec}."
    )

    print("\n== Effective mass ==")
    print(f"m(r) = {m}")
    print("m(0) = 0, m(infinity) = M")

    print("\nConservation equation = 0")
    print("All symbolic assertions passed.")


if __name__ == "__main__":
    main()
