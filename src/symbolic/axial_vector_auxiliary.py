#!/usr/bin/env python3
"""Axial-vector auxiliary equation on the regular two-vector background.

For one vector sector
    L[W] = 4 G^{mu nu} W_mu W_nu
         + 8 W^2 nabla_mu W^mu
         + 6 (W^2)^2

the vector equation, divided by an overall factor 8, is

    E^mu =
        G^{mu nu} W_nu
      + 2 W^mu (nabla.W)
      - nabla^mu(W^2)
      + 3 W^2 W^mu
      = 0.

On the static spherical null background
    W = a(r) dv
in ingoing EF coordinates, W^2=0.

For an odd-parity angular perturbation w_A:
- delta(W^2)=0 at linear order;
- delta(nabla.W)=0 because the axial vector harmonic is divergence-free;
- the w_A part of the vector equation is algebraic.

The coefficient multiplying w^A is
    C(r) = G^theta_theta + 2 (nabla.W).

For the regular q_b=-q_a=q branch, both vector backgrounds have the same
divergence and the same C(r).
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

    # q_a=q, q_b=-q
    a = sp.factor(
        (r - r * f - q / 2) / (2 * r**2)
    )
    b = sp.factor(
        (r - r * f + q / 2) / (2 * r**2)
    )

    return D, f, a, b


def angular_einstein(f):
    fp = sp.diff(f, r)
    fpp = sp.diff(f, r, 2)
    return sp.factor(
        fpp / 2 + fp / r
    )


def null_vector_divergence(profile):
    # In EF coordinates:
    # W_mu dx^mu = profile(r) dv
    # W^mu partial_mu = profile(r) partial_r
    return sp.factor(
        sp.diff(profile, r)
        + 2 * profile / r
    )


def main():
    D, f, a, b = regular_background()

    Gomega = angular_einstein(f)
    theta_a = null_vector_divergence(a)
    theta_b = null_vector_divergence(b)

    # Coulomb-like +/- q/(4 r^2) pieces are divergence-free, so both
    # background vectors have the same divergence.
    assert sp.simplify(theta_a - theta_b) == 0

    expected_theta = sp.factor(
        6 * M * q * ell**2 / D**2
    )
    assert sp.simplify(
        theta_a - expected_theta
    ) == 0

    C_a = sp.factor(
        Gomega + 2 * theta_a
    )
    C_b = sp.factor(
        Gomega + 2 * theta_b
    )

    expected_C = sp.factor(
        36 * M * q * ell**2 * r**3 / D**3
    )

    assert sp.simplify(C_a - expected_C) == 0
    assert sp.simplify(C_b - expected_C) == 0

    # C is exactly the effective-stress anisotropy in geometric units:
    # G^theta_theta - G^t_t.
    Gtt = sp.factor(
        (r * sp.diff(f, r) + f - 1) / r**2
    )
    assert sp.simplify(
        expected_C - (Gomega - Gtt)
    ) == 0

    # Endpoint degeneracy.
    assert sp.limit(expected_C, r, 0) == 0
    assert sp.limit(expected_C, r, sp.oo) == 0

    center_coeff = sp.simplify(
        sp.limit(expected_C / r**3, r, 0)
    )
    infinity_coeff = sp.simplify(
        sp.limit(r**6 * expected_C, r, sp.oo)
    )

    assert sp.simplify(
        center_coeff
        - sp.Rational(9, 2) * M / (q**2 * ell**4)
    ) == 0
    assert sp.simplify(
        infinity_coeff
        - 36 * M * q * ell**2
    ) == 0

    # Fully extremal branch q ell^2 = 16 M^3 / 27.
    Q = sp.symbols("Q", positive=True)
    C_Q = sp.factor(
        expected_C.subs(q * ell**2, Q)
    )
    Qext = sp.Rational(16, 27) * M**3
    Cext = sp.factor(C_Q.subs(Q, Qext))
    rh = sp.Rational(4, 3) * M

    C_h = sp.simplify(
        Cext.subs(r, rh)
    )
    assert sp.simplify(
        C_h - sp.Rational(9, 8) / M**2
    ) == 0

    center_ext = sp.simplify(
        sp.limit(Cext / r**3, r, 0)
    )
    infinity_ext = sp.simplify(
        sp.limit(r**6 * Cext, r, sp.oo)
    )

    assert sp.simplify(
        center_ext
        - sp.Rational(6561, 512) / M**5
    ) == 0
    assert sp.simplify(
        infinity_ext
        - sp.Rational(64, 3) * M**4
    ) == 0

    print("== Regular branch ==")
    print(f"a(r) = {a}")
    print(f"b(r) = {b}")
    print(f"nabla.A = nabla.B = {theta_a}")
    print(f"G^theta_theta = {Gomega}")
    print()
    print("== Axial auxiliary coefficient ==")
    print(f"C(r) = {expected_C}")
    print(
        "Linear axial vector equation has the form "
        "C(r) w^A + metric-source^A = 0."
    )
    print("There are no derivatives acting on w^A.")
    print()
    print("C(r) = G^theta_theta - G^t_t")
    print(f"C/r^3 -> {center_coeff} as r->0")
    print(f"r^6 C -> {infinity_coeff} as r->infinity")
    print()
    print("== Fully extremal branch ==")
    print(f"C_ext(r) = {Cext}")
    print(f"C_ext(r_h=4M/3) = {C_h}")
    print(f"C_ext/r^3 -> {center_ext} at the center")
    print(f"r^6 C_ext -> {infinity_ext} at infinity")
    print()
    print(
        "The auxiliary equation is nondegenerate at the extremal horizon, "
        "but degenerates at both the regular center and asymptotic infinity."
    )
    print("All symbolic assertions passed.")


if __name__ == "__main__":
    main()
