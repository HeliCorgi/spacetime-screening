#!/usr/bin/env python3
"""Radial high-frequency tensor principal cone for the two-vector benchmark.

This is a principal-symbol calculation, not the full spherical quadratic
Regge-Wheeler action.

For a local transverse-traceless graviton propagating in the radial direction,
the null background vectors are parallel:
    A_mu = a k_mu,
    B_mu = b k_mu,
    k^2 = 0.

The vector self-interactions vanish for this pure TT principal perturbation.
The relevant nonminimal term is
    4 ell^2 G^{mu nu} (A_mu A_nu - B_mu B_nu).

An explicit local quadratic expansion gives, up to boundary terms,
    L2 = 1/2 [psi_t^2 - psi_x^2
              - zeta (psi_t - psi_x)^2],
where
    zeta k^mu k^nu = 4 ell^2
                     (A^mu A^nu - B^mu B^nu).

Thus the tensor principal inverse metric is a null Kerr-Schild deformation
    g_T^{mu nu}
      = g^{mu nu}
        + 4 ell^2 (A^mu A^nu - B^mu B^nu).

On the regular spherical solution this simplifies exactly to Schwarzschild in
the ingoing (v,r) block:
    f_T(r) = 1 - 2 M/r.

Caveat:
This proves the existence of this pure-TT radial characteristic in the
principal symbol.  The full l>=2 metric-vector quadratic action still needs to
be reduced to establish the complete mode spectrum and stability.
"""

from __future__ import annotations

import sympy as sp


r, M, q, ell = sp.symbols(
    "r M q ell", positive=True, finite=True
)


def regular_background():
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
    return D, f, a, b


def main():
    D, f, a, b = regular_background()

    # Difference of the two parallel-null background tensors:
    # A^mu A^nu - B^mu B^nu = d(r) l^mu l^nu.
    d = sp.factor(a**2 - b**2)
    expected_d = sp.factor(
        -M * q / (r * D)
    )
    assert sp.simplify(d - expected_d) == 0

    delta_f = sp.factor(
        4 * ell**2 * d
    )

    f_tensor = sp.factor(
        f + delta_f
    )

    expected_f_tensor = sp.factor(
        1 - 2 * M / r
    )
    assert sp.simplify(
        f_tensor - expected_f_tensor
    ) == 0

    # In ingoing coordinates the background inverse radial block is
    # [[0,1],[1,f]].  The null Kerr-Schild deformation changes only rr.
    gT_inv = sp.Matrix(
        [
            [0, 1],
            [1, f_tensor],
        ]
    )
    gT_cov = sp.simplify(gT_inv.inv())

    expected_cov = sp.Matrix(
        [
            [-expected_f_tensor, 1],
            [1, 0],
        ]
    )
    assert sp.simplify(gT_cov - expected_cov) == sp.zeros(2)

    # Null Kerr-Schild deformation preserves the 2D determinant.
    assert sp.simplify(gT_inv.det() + 1) == 0
    assert sp.simplify(gT_cov.det() + 1) == 0

    # Tensor characteristic horizon.
    r_tensor_h = sp.solve(
        sp.Eq(expected_f_tensor, 0),
        r,
    )[0]
    assert sp.simplify(r_tensor_h - 2 * M) == 0

    # Every physical metric horizon on the regular q>0 branch obeys r_h<2M:
    # f(r_h)=0 => 2M = r_h + 2 q ell^2/r_h^2.
    rh = sp.symbols(
        "r_h", positive=True, finite=True
    )
    mass_relation = (
        rh
        + 2 * q * ell**2 / rh**2
    ) / 2
    gap = sp.factor(
        2 * mass_relation - rh
    )
    assert sp.simplify(
        gap - 2 * q * ell**2 / rh**2
    ) == 0

    # Fully extremal background metric horizon.
    rh_ext = sp.Rational(4, 3) * M
    separation_ext = sp.simplify(
        2 * M - rh_ext
    )
    assert separation_ext == sp.Rational(2, 3) * M

    # Background metric is already outside its own horizon at r=2M.
    Q = sp.symbols("Q", positive=True)
    f_Q = sp.factor(
        f.subs(q * ell**2, Q)
    )
    f_at_2M = sp.factor(
        f_Q.subs(r, 2 * M)
    )
    expected_f_at_2M = sp.factor(
        Q / (4 * M**3 + Q)
    )
    assert sp.simplify(
        f_at_2M - expected_f_at_2M
    ) == 0

    # Characteristic curvature is exactly Schwarzschild if the full effective
    # tensor metric is ds_T^2=-f_T dv^2+2dvdr+r^2dOmega^2.
    K_tensor = sp.factor(
        48 * M**2 / r**6
    )

    print("== Parallel-null background difference ==")
    print(f"a^2-b^2 = {d}")
    print(f"4 ell^2 (a^2-b^2) = {delta_f}")
    print()

    print("== Radial tensor principal metric ==")
    print(f"f_background(r) = {f}")
    print(f"f_tensor(r) = {f_tensor}")
    print("Thus the radial TT principal cone is Schwarzschild-like.")
    print()
    print("inverse (v,r) block:")
    print(gT_inv)
    print("covariant (v,r) block:")
    print(gT_cov)
    print(f"determinant = {gT_cov.det()}")
    print()

    print("== Characteristic horizons ==")
    print(f"tensor characteristic horizon r_T = {r_tensor_h}")
    print(
        "physical regular-metric horizons obey "
        "2M-r_h = 2 q ell^2/r_h^2 > 0"
    )
    print(
        f"fully extremal metric horizon = {rh_ext}, "
        f"so r_T-r_h = {separation_ext}"
    )
    print(f"background f(2M) = {f_at_2M} > 0")
    print()

    print("== If promoted to the full tensor characteristic metric ==")
    print(f"K_T = {K_tensor}")
    print(
        "This characteristic geometry retains the Schwarzschild r^-6 "
        "curvature divergence."
    )
    print()
    print("All symbolic assertions passed.")


if __name__ == "__main__":
    main()
