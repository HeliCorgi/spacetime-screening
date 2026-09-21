#!/usr/bin/env python3
"""Near-horizon analysis of the fully extremal regular branch.

Geometric units G=c=1.

Fully extremal branch:
    f(r) = 1 - 2 M r^2 / (r^3 + 32 M^3/27)
    r_h  = 4 M / 3

The script verifies:
- f(r_h)=f'(r_h)=0;
- the double-zero coefficient;
- near-horizon AdS2 x S2 with equal radii;
- curvature invariants at the horizon;
- Maxwell-like effective stress tensor at the horizon.
"""

from __future__ import annotations

import sympy as sp


r, M = sp.symbols("r M", positive=True, finite=True)
pi = sp.pi

rh = sp.Rational(4, 3) * M
qell2 = sp.Rational(16, 27) * M**3
D = r**3 + 2 * qell2
f = sp.factor(1 - 2 * M * r**2 / D)


def invariants() -> dict[str, sp.Expr]:
    fp = sp.diff(f, r)
    fpp = sp.diff(f, r, 2)

    R = sp.factor(
        -fpp - 4 * fp / r + 2 * (1 - f) / r**2
    )
    Ricci2 = sp.factor(
        2 * (fpp / 2 + fp / r) ** 2
        + 2 * (fp / r + (f - 1) / r**2) ** 2
    )
    K = sp.factor(
        fpp**2
        + 4 * (fp / r) ** 2
        + 4 * ((1 - f) / r**2) ** 2
    )
    return {"R": R, "Ricci2": Ricci2, "K": K}


def effective_fluid() -> dict[str, sp.Expr]:
    fp = sp.diff(f, r)
    fpp = sp.diff(f, r, 2)

    Gtt = sp.factor((r * fp + f - 1) / r**2)
    Gth = sp.factor(fpp / 2 + fp / r)

    rho = sp.factor(-Gtt / (8 * pi))
    pr = sp.factor(Gtt / (8 * pi))
    pt = sp.factor(Gth / (8 * pi))
    return {"rho": rho, "p_r": pr, "p_t": pt}


def main() -> None:
    assert sp.simplify(f.subs(r, rh)) == 0
    assert sp.simplify(sp.diff(f, r).subs(r, rh)) == 0

    f2 = sp.simplify(sp.diff(f, r, 2).subs(r, rh))
    f3 = sp.simplify(sp.diff(f, r, 3).subs(r, rh))

    assert sp.simplify(f2 - sp.Rational(9, 8) / M**2) == 0
    assert sp.simplify(f3 + sp.Rational(27, 8) / M**3) == 0

    # f ~ (r-rh)^2/L2^2.  Since coefficient is f''/2:
    L2_sq = sp.factor(2 / f2)
    L2 = sp.factor(sp.sqrt(L2_sq))

    assert sp.simplify(L2_sq - rh**2) == 0

    inv = invariants()
    R_h = sp.simplify(inv["R"].subs(r, rh))
    Ricci2_h = sp.simplify(inv["Ricci2"].subs(r, rh))
    K_h = sp.simplify(inv["K"].subs(r, rh))

    assert R_h == 0
    assert sp.simplify(
        Ricci2_h - sp.Rational(81, 64) / M**4
    ) == 0
    assert sp.simplify(
        K_h - sp.Rational(81, 32) / M**4
    ) == 0

    # Product AdS2 x S2 with equal radius L=rh:
    # R_total = -2/L^2 + 2/L^2 = 0
    R_product = sp.simplify(-2 / L2_sq + 2 / rh**2)
    Ricci2_product = sp.simplify(
        2 / L2_sq**2 + 2 / rh**4
    )
    K_product = sp.simplify(
        4 / L2_sq**2 + 4 / rh**4
    )

    assert sp.simplify(R_product - R_h) == 0
    assert sp.simplify(Ricci2_product - Ricci2_h) == 0
    assert sp.simplify(K_product - K_h) == 0

    fluid = effective_fluid()
    rho_h = sp.simplify(fluid["rho"].subs(r, rh))
    pr_h = sp.simplify(fluid["p_r"].subs(r, rh))
    pt_h = sp.simplify(fluid["p_t"].subs(r, rh))

    expected_rho = sp.Rational(9, 128) / (pi * M**2)
    assert sp.simplify(rho_h - expected_rho) == 0
    assert sp.simplify(pr_h + rho_h) == 0
    assert sp.simplify(pt_h - rho_h) == 0

    trace_h = sp.simplify(-rho_h + pr_h + 2 * pt_h)
    assert trace_h == 0

    # Core curvature / horizon curvature ratio.
    K_core = sp.Rational(2187, 32) / M**4
    ratio = sp.simplify(K_core / K_h)
    assert ratio == 27

    print("== Extremal horizon ==")
    print(f"r_h = {rh}")
    print("f(r_h) = 0")
    print("f'(r_h) = 0")
    print(f"f''(r_h) = {f2}")
    print()
    print("Near horizon:")
    print("f(r) ~ (r-r_h)^2 / L_2^2")
    print(f"L_2^2 = {L2_sq}")
    print(f"r_h^2 = {rh**2}")
    print("Therefore L_AdS2 = R_S2 = r_h.")
    print()
    print("== Horizon curvature ==")
    print(f"R_h = {R_h}")
    print(f"Ricci^2_h = {Ricci2_h}")
    print(f"K_h = {K_h}")
    print()
    print("== Effective stress at horizon ==")
    print(f"rho_h = {rho_h}")
    print(f"p_r,h = {pr_h}")
    print(f"p_t,h = {pt_h}")
    print(f"trace T_h = {trace_h}")
    print("Equation of state: p_r=-rho, p_t=+rho.")
    print()
    print(f"K_core / K_h = {ratio}")
    print()
    print("All symbolic assertions passed.")


if __name__ == "__main__":
    main()
