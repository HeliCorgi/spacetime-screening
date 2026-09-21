#!/usr/bin/env python3
"""Constraint / strong-coupling diagnostics for the two-vector benchmark.

Vector Lagrangian for one Weyl vector:
    L[W] = 4 G^{mu nu} W_mu W_nu
         + 8 W^2 nabla_mu W^mu
         + 6 (W^2)^2

This script studies the vector sector around flat space.

Main observations:
1. Around (eta_mu_nu, W_mu=0), the vector sector has no quadratic action.
   The first vector self-interaction is cubic.
2. Around a constant null vector background, the quadratic action is only
   first order in derivatives; its velocity Hessian vanishes.
3. The fixed-metric vector principal symbol has determinant zero and
   generically rank two. It is therefore a constrained/degenerate system,
   not an ordinary Proca wave operator.

These are diagnostics, not a complete Dirac-Hamiltonian analysis.
"""

from __future__ import annotations

import itertools
import sympy as sp


eps = sp.symbols("eps")
B2, Bw, w2, divw = sp.symbols("B2 Bw w2 divw")


def expansion_about_constant_background() -> dict[str, sp.Expr]:
    """Expand the flat-space vector self-interactions in perturbation order."""
    W2 = B2 + 2 * eps * Bw + eps**2 * w2
    divW = eps * divw

    L = sp.expand(8 * W2 * divW + 6 * W2**2)

    coeffs = {
        f"L{n}": sp.factor(sp.expand(L).coeff(eps, n))
        for n in range(5)
    }

    # On a null constant background B^2=0:
    null_L2 = sp.factor(coeffs["L2"].subs(B2, 0))
    expected_null_L2 = sp.factor(
        16 * Bw * divw + 24 * Bw**2
    )
    assert sp.simplify(null_L2 - expected_null_L2) == 0

    # On the asymptotic vacuum B=0:
    vacuum_L2 = sp.factor(
        coeffs["L2"].subs({B2: 0, Bw: 0})
    )
    vacuum_L3 = sp.factor(
        coeffs["L3"].subs({B2: 0, Bw: 0})
    )
    vacuum_L4 = sp.factor(
        coeffs["L4"].subs({B2: 0, Bw: 0})
    )

    assert vacuum_L2 == 0
    assert sp.simplify(vacuum_L3 - 8 * w2 * divw) == 0
    assert sp.simplify(vacuum_L4 - 6 * w2**2) == 0

    return {
        **coeffs,
        "null_L2": null_L2,
        "vacuum_L2": vacuum_L2,
        "vacuum_L3": vacuum_L3,
        "vacuum_L4": vacuum_L4,
    }


def null_background_velocity_hessian() -> sp.Matrix:
    """Compute the velocity Hessian on a constant null background.

    Choose Minkowski signature (-,+,+,+) and
        B^mu = b (1,1,0,0),
    so B^2=0.

    The quadratic vector Lagrangian is
        L2 = 16 (B.w) (partial.w) + 24 (B.w)^2.
    """
    b = sp.symbols("b", nonzero=True)
    w0, w1, w2c, w3 = sp.symbols("w0 w1 w2 w3")
    v0, v1, v2, v3 = sp.symbols("v0 v1 v2 v3")
    s1, s2, s3 = sp.symbols("s1 s2 s3")

    Bdotw = b * (-w0 + w1)
    divergence = v0 + s1 + s2 + s3
    L2 = sp.expand(
        16 * Bdotw * divergence
        + 24 * Bdotw**2
    )

    velocities = (v0, v1, v2, v3)
    H = sp.Matrix(
        [
            [
                sp.diff(L2, vi, vj)
                for vj in velocities
            ]
            for vi in velocities
        ]
    )

    assert H == sp.zeros(4)
    return H


def principal_symbol() -> dict[str, sp.Expr | sp.Matrix]:
    """Principal symbol of the fixed-metric vector equation.

    Flat-space vector equation:
        E^mu = 3 W^2 W^mu
             + 2 W^mu partial_alpha W^alpha
             - partial^mu(W^2) = 0.

    Linearizing around a constant null background B gives the principal symbol
        P^mu_nu(k) = 2 (B^mu k_nu - k^mu B_nu).
    """
    b = sp.symbols("b", nonzero=True)
    k0, k1, k2, k3 = sp.symbols("k0 k1 k2 k3")

    # Minkowski signature (-,+,+,+).
    B_up = sp.Matrix([b, b, 0, 0])
    B_dn = sp.Matrix([-b, b, 0, 0])

    # k_mu = (k0,k1,k2,k3), k^mu=(-k0,k1,k2,k3)
    k_dn = sp.Matrix([k0, k1, k2, k3])
    k_up = sp.Matrix([-k0, k1, k2, k3])

    P = sp.factor(2) * (
        B_up * k_dn.T
        - k_up * B_dn.T
    )

    detP = sp.factor(P.det())
    assert detP == 0

    # Every 3x3 minor vanishes: rank <= 2 for all k.
    minors3 = []
    for rows in itertools.combinations(range(4), 3):
        for cols in itertools.combinations(range(4), 3):
            minor = sp.factor(
                P.extract(rows, cols).det()
            )
            minors3.append(minor)
            assert sp.simplify(minor) == 0

    # A representative 2x2 minor is generically nonzero.
    minor2 = sp.factor(
        P.extract((0, 2), (0, 2)).det()
    )
    assert sp.simplify(minor2 + 4 * b**2 * k2**2) == 0

    return {
        "P": P,
        "detP": detP,
        "representative_2x2_minor": minor2,
    }


def asymptotic_black_hole_vector_profiles() -> dict[str, sp.Expr]:
    """Asymptotic profiles on the regular q_b=-q_a branch, G=c=1."""
    r, M, q, ell = sp.symbols(
        "r M q ell", positive=True, finite=True
    )

    D = r**3 + 2 * q * ell**2
    f = 1 - 2 * M * r**2 / D

    a = sp.factor(
        (r - r * f - q / 2) / (2 * r**2)
    )
    bprof = sp.factor(
        (r - r * f + q / 2) / (2 * r**2)
    )

    # r^2 a and r^2 b have finite nonzero asymptotic limits.
    a2_inf = sp.simplify(sp.limit(r**2 * a, r, sp.oo))
    b2_inf = sp.simplify(sp.limit(r**2 * bprof, r, sp.oo))

    assert sp.simplify(a2_inf - (M - q / 4)) == 0
    assert sp.simplify(b2_inf - (M + q / 4)) == 0

    return {
        "a(r)": a,
        "b(r)": bprof,
        "lim r^2 a": a2_inf,
        "lim r^2 b": b2_inf,
    }


def regularity_hypersurface() -> dict[str, sp.Expr]:
    """Quantify how leaving q_b=-q_a restores the r=0 singularity."""
    r, M, qa, qb, ell = sp.symbols(
        "r M q_a q_b ell", finite=True
    )

    f = sp.factor(
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

    fp = sp.diff(f, r)
    fpp = sp.diff(f, r, 2)
    K = sp.factor(
        fpp**2
        + 4 * (fp / r) ** 2
        + 4 * ((1 - f) / r**2) ** 2
    )

    leading_K = sp.factor(
        sp.limit(r**6 * K, r, 0)
    )
    expected = sp.factor(
        sp.Rational(3, 4) * (qa + qb) ** 2
    )
    assert sp.simplify(leading_K - expected) == 0

    return {
        "lim r^6 K": leading_K,
        "regularity_condition": sp.Eq(qa + qb, 0),
    }


def main() -> None:
    expn = expansion_about_constant_background()
    H = null_background_velocity_hessian()
    principal = principal_symbol()
    profiles = asymptotic_black_hole_vector_profiles()
    regularity = regularity_hypersurface()

    print("== Flat-space perturbative expansion ==")
    print(f"L2 around W=0 = {expn['vacuum_L2']}")
    print(f"L3 around W=0 = {expn['vacuum_L3']}")
    print(f"L4 around W=0 = {expn['vacuum_L4']}")
    print()
    print("No vector quadratic action exists around W=0.")
    print("The first vector self-interaction is cubic.")
    print()

    print("== Constant null background ==")
    print(f"L2 = {expn['null_L2']}")
    print("velocity Hessian =")
    print(H)
    print("rank(H) = 0")
    print()

    print("== Vector principal symbol ==")
    print("P^mu_nu =")
    print(principal["P"])
    print(f"det(P) = {principal['detP']}")
    print(
        "representative nonzero 2x2 minor = "
        f"{principal['representative_2x2_minor']}"
    )
    print("generic rank = 2; all 3x3 minors vanish")
    print()

    print("== Regular BH asymptotics ==")
    for key, value in profiles.items():
        print(f"{key} = {value}")
    print("Both vector backgrounds vanish as r^-2.")
    print()

    print("== Regularity hypersurface ==")
    for key, value in regularity.items():
        print(f"{key} = {value}")
    print(
        "Any static hair mismatch q_a+q_b != 0 gives "
        "K ~ 3(q_a+q_b)^2/(4 r^6)."
    )
    print()
    print("All symbolic assertions passed.")


if __name__ == "__main__":
    main()
