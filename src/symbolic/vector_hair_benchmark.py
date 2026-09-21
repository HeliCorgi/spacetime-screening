#!/usr/bin/env python3
"""Symbolic benchmark for the two-vector regular-black-hole solution.

Based on the vector-tensor family discussed by Eichhorn & Fernandes,
Phys. Rev. D 113, L081501 (2026), arXiv:2508.00686.

We use geometric units G=c=1, matching the paper.

General metric function:
    f(r) = 1 - [8 M r^3 + ell^2 (qa^2-qb^2)]
                 / [4 r (r^3 + (qa-qb) ell^2)]

Regularity requires qb = -qa, yielding
    f(r) = 1 - 2 M r^2 / (r^3 + 2 qa ell^2).

qa=M recovers the standard Hayward metric in these units.
"""

from __future__ import annotations

import sympy as sp


r, M, ell = sp.symbols("r M ell", positive=True, finite=True)
qa = sp.symbols("q_a", positive=True, finite=True)
qb = sp.symbols("q_b", finite=True)
pi = sp.pi


def general_metric() -> sp.Expr:
    return sp.factor(
        1
        - (
            8 * M * r**3
            + ell**2 * (qa**2 - qb**2)
        )
        / (
            4 * r
            * (r**3 + (qa - qb) * ell**2)
        )
    )


def regular_metric() -> sp.Expr:
    return sp.factor(
        1 - 2 * M * r**2 / (r**3 + 2 * qa * ell**2)
    )


def invariants(f: sp.Expr) -> dict[str, sp.Expr]:
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


def effective_fluid(f: sp.Expr) -> dict[str, sp.Expr]:
    fp = sp.diff(f, r)
    fpp = sp.diff(f, r, 2)

    Gtt = sp.factor((r * fp + f - 1) / r**2)
    Gth = sp.factor(fpp / 2 + fp / r)

    # In G=1 units, G^mu_nu = 8*pi*T^mu_nu.
    rho = sp.factor(-Gtt / (8 * pi))
    pr = sp.factor(Gtt / (8 * pi))
    pt = sp.factor(Gth / (8 * pi))

    return {"rho": rho, "p_r": pr, "p_t": pt}


def main() -> None:
    fg = general_metric()

    # Leading singular term of the general family.
    singular_coeff = sp.simplify(
        sp.limit(r * fg, r, 0)
    )
    expected_singular_coeff = -(qa + qb) / 4
    assert sp.simplify(
        singular_coeff - expected_singular_coeff
    ) == 0

    # Regularity condition qb=-qa.
    fr = sp.factor(fg.subs(qb, -qa))
    assert sp.simplify(fr - regular_metric()) == 0

    # Small-r de Sitter form.
    core_a = sp.simplify(
        sp.limit((1 - fr) / r**2, r, 0)
    )
    assert sp.simplify(core_a - M / (qa * ell**2)) == 0

    inv = invariants(fr)

    R0 = sp.simplify(sp.limit(inv["R"], r, 0))
    Ricci20 = sp.simplify(sp.limit(inv["Ricci2"], r, 0))
    K0 = sp.simplify(sp.limit(inv["K"], r, 0))

    assert sp.simplify(
        R0 - 12 * M / (qa * ell**2)
    ) == 0
    assert sp.simplify(
        Ricci20 - 36 * M**2 / (qa**2 * ell**4)
    ) == 0
    assert sp.simplify(
        K0 - 24 * M**2 / (qa**2 * ell**4)
    ) == 0

    # Diagnostic screening factor:
    # f = 1 - (2M/r) S(r).
    S = sp.factor(r**3 / (r**3 + 2 * qa * ell**2))
    assert sp.simplify(
        fr - (1 - 2 * M * S / r)
    ) == 0
    assert sp.limit(S, r, 0) == 0
    assert sp.limit(S, r, sp.oo) == 1

    fluid = effective_fluid(fr)
    rho = fluid["rho"]
    pr = fluid["p_r"]
    pt = fluid["p_t"]

    expected_rho = sp.factor(
        3 * M * qa * ell**2
        / (2 * pi * (r**3 + 2 * qa * ell**2) ** 2)
    )
    expected_pt = sp.factor(
        3 * M * qa * ell**2
        * (r**3 - qa * ell**2)
        / (pi * (r**3 + 2 * qa * ell**2) ** 3)
    )

    assert sp.simplify(rho - expected_rho) == 0
    assert sp.simplify(pr + rho) == 0
    assert sp.simplify(pt - expected_pt) == 0

    # Strong-energy-condition boundary.
    sec_combo = sp.factor(rho + pr + 2 * pt)
    expected_sec = sp.factor(
        6 * M * qa * ell**2
        * (r**3 - qa * ell**2)
        / (pi * (r**3 + 2 * qa * ell**2) ** 3)
    )
    assert sp.simplify(sec_combo - expected_sec) == 0

    r_sec = (qa * ell**2) ** sp.Rational(1, 3)

    # Extremality: f(rh)=0 and f'(rh)=0.
    rh = sp.symbols("r_h", positive=True, finite=True)
    horizon_mass = sp.factor(
        (rh**3 + 2 * qa * ell**2) / (2 * rh**2)
    )

    fp_h = sp.factor(
        sp.diff(fr, r)
        .subs(r, rh)
        .subs(M, horizon_mass)
    )

    # f'=0 -> rh^3 = 4 qa ell^2.
    extremal_relation = sp.factor(
        sp.solve(sp.Eq(fp_h, 0), qa)[0]
    )
    expected_qa_rh = sp.factor(rh**3 / (4 * ell**2))
    assert sp.simplify(
        extremal_relation - expected_qa_rh
    ) == 0

    M_ext_as_rh = sp.factor(
        horizon_mass.subs(qa, expected_qa_rh)
    )
    assert sp.simplify(M_ext_as_rh - 3 * rh / 4) == 0

    # Therefore rh=4M/3 and qa=16 M^3/(27 ell^2).
    rh_ext = sp.Rational(4, 3) * M
    qa_ext = sp.factor(16 * M**3 / (27 * ell**2))

    assert sp.simplify(
        qa_ext - expected_qa_rh.subs(rh, rh_ext)
    ) == 0

    f_ext = sp.factor(fr.subs(qa, qa_ext))
    expected_f_ext = sp.factor(
        1
        - 2 * M * r**2
        / (r**3 + sp.Rational(32, 27) * M**3)
    )
    assert sp.simplify(f_ext - expected_f_ext) == 0

    # Core-curvature tradeoff.
    # Define L_core^2 = qa ell^2 / M so f=1-r^2/L_core^2+...
    Lcore2 = sp.factor(qa * ell**2 / M)
    K0_general = sp.factor(24 / Lcore2**2)
    assert sp.simplify(K0_general - K0) == 0

    # Original Hayward choice qa=M gives universal limiting curvature.
    K0_hayward = sp.simplify(K0_general.subs(qa, M))
    assert sp.simplify(K0_hayward - 24 / ell**4) == 0

    # Fully extremal choice removes ell from the metric and makes the
    # core curvature mass-dependent.
    Lcore2_ext = sp.factor(Lcore2.subs(qa, qa_ext))
    K0_ext = sp.factor(K0_general.subs(qa, qa_ext))
    assert sp.simplify(
        Lcore2_ext - sp.Rational(16, 27) * M**2
    ) == 0
    assert sp.simplify(
        K0_ext - sp.Rational(2187, 32) / M**4
    ) == 0

    # Screening factor at the degenerate horizon.
    S_ext_h = sp.simplify(
        S.subs({qa: qa_ext, r: rh_ext})
    )
    assert sp.simplify(S_ext_h - sp.Rational(2, 3)) == 0

    print("== General family ==")
    print(f"f_general = {fg}")
    print(f"coefficient of 1/r near center = {singular_coeff}")
    print("regularity requires q_b = -q_a")
    print()

    print("== Regular branch ==")
    print(f"f_regular = {fr}")
    print(f"screening factor S(r) = {S}")
    print(f"core R(0) = {R0}")
    print(f"core Ricci^2(0) = {Ricci20}")
    print(f"core K(0) = {K0}")
    print()

    print("== Effective GR source ==")
    print(f"rho = {rho}")
    print(f"p_r = {pr}")
    print(f"p_t = {pt}")
    print(f"SEC combination = {sec_combo}")
    print(f"SEC violation for r < {r_sec}")
    print()

    print("== Extremal regular branch ==")
    print(f"r_ext = {rh_ext}")
    print(f"q_a,ext = {qa_ext}")
    print(f"f_ext = {f_ext}")
    print("surface gravity vanishes at the degenerate horizon")
    print(f"L_core^2(extremal) = {Lcore2_ext}")
    print(f"K_core(extremal) = {K0_ext}")
    print(f"screening factor at extremal horizon = {S_ext_h}")
    print()
    print("== Limiting-curvature tradeoff ==")
    print(f"K_core(general) = {K0_general}")
    print(f"K_core(q_a=M) = {K0_hayward}")
    print("q_a=M keeps the core curvature set by ell.")
    print("q_a=16 M^3/(27 ell^2) makes all masses extremal,")
    print("but the core curvature scales as M^-4.")
    print()
    print("All symbolic assertions passed.")


if __name__ == "__main__":
    main()
