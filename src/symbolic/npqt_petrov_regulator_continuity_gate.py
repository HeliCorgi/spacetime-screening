#!/usr/bin/env python3
"""Continuity gate for the Petrov-discriminant NPQT regulator.

The displayed cubic 4D NPQT representative contains the rational scalar

    N / D,

where

    D = (WZZ) W2 - 2 W3 Z2,
    N = W3 Z3 W2.

The previous proof-of-concept Petrov regulator was

    R_mu = N D / (D**2 + mu DeltaW Z2**2),
    DeltaW = W2**3 - 12 W3**2.

This script establishes three facts.

1. On a fully general local spherical algebraic-curvature configuration
   (including an off-diagonal time-radial traceless-Ricci block),

       N/D = W2 * Theta

   wherever D != 0. Theta is the repeated angular eigenvalue of the
   traceless Ricci tensor. Thus W2*Theta is the exact spherical target that
   any alternative representative for this rational term must reproduce.

2. The old Petrov regulator has no continuous extension at an intended
   spherical simultaneous zero D=DeltaW=0. A spherical path tends to
   48 q^2 theta, while a Weyl-splitting path tends identically to zero.

3. In the exact type-D diagonal family, the unmodified quotient has
   direction-dependent limits. A local principal-plane blending term can
   restore continuity, but the simplest such blend is not C^2. This
   identifies the next design target: construct a smooth covariant extension
   of Theta itself, rather than only lifting the old denominator.

All statements are algebraic and concern the displayed cubic rational term.
They do not establish a globally regular NPQT representative.
"""

from __future__ import annotations

import itertools

import sympy as sp


e1, e2 = sp.symbols("e1 e2", real=True)
z0, z1, z2 = sp.symbols("z0 z1 z2", real=True)
q, theta = sp.symbols("q theta", real=True, nonzero=True)
epsilon = sp.symbols("epsilon", real=True)
k = sp.symbols("k", real=True)
mu = sp.symbols("mu", positive=True, finite=True)

e3 = -e1 - e2
z3 = -z0 - z1 - z2

W2 = sp.factor(16 * (e1**2 + e1 * e2 + e2**2))
W3 = sp.factor(48 * e1 * e2 * (e1 + e2))
Z2 = sp.factor(z0**2 + z1**2 + z2**2 + z3**2)
Z3 = sp.factor(z0**3 + z1**3 + z2**3 + z3**3)
WZZ = sp.factor(
    -2
    * (
        e1 * z0**2
        + 2 * e1 * z0 * z1
        - 2 * e1 * z1 * z2
        - e1 * z2**2
        + e2 * z0**2
        + 2 * e2 * z0 * z2
        - e2 * z1**2
        - 2 * e2 * z1 * z2
    )
)

D = sp.factor(WZZ * W2 - 2 * W3 * Z2)
N = sp.factor(W3 * Z3 * W2)
DeltaW = sp.factor(W2**3 - 12 * W3**2)


# Exact spherical target with a general time-radial Ricci block.

eta = sp.diag(-1, 1, 1, 1)
E = sp.diag(-2 * q, q, q)


def eps3(i: int, j: int, k_: int) -> sp.Expr:
    return sp.LeviCivita(i - 1, j - 1, k_ - 1)


Cweyl = sp.MutableDenseNDimArray.zeros(4, 4, 4, 4)

for i in range(1, 4):
    for j in range(1, 4):
        value = E[i - 1, j - 1]
        Cweyl[0, i, 0, j] = value
        Cweyl[i, 0, 0, j] = -value
        Cweyl[0, i, j, 0] = -value
        Cweyl[i, 0, j, 0] = value

for i, j, k_, l in itertools.product(range(1, 4), repeat=4):
    value = 0
    for m, n in itertools.product(range(1, 4), repeat=2):
        value += -eps3(i, j, m) * eps3(k_, l, n) * E[m - 1, n - 1]
    Cweyl[i, j, k_, l] = sp.simplify(value)


def c_ab_upup(a_: int, b_: int, c_: int, d_: int) -> sp.Expr:
    return sp.simplify(
        sum(
            eta[c_, e] * eta[d_, f] * Cweyl[a_, b_, e, f]
            for e, f in itertools.product(range(4), repeat=2)
        )
    )


W2_sph = sp.factor(
    sum(
        c_ab_upup(a_, b_, c_, d_) * c_ab_upup(c_, d_, a_, b_)
        for a_, b_, c_, d_ in itertools.product(range(4), repeat=4)
    )
)
W3_sph = sp.factor(
    sum(
        c_ab_upup(a_, b_, c_, d_)
        * c_ab_upup(c_, d_, e_, f_)
        * c_ab_upup(e_, f_, a_, b_)
        for a_, b_, c_, d_, e_, f_ in itertools.product(range(4), repeat=6)
    )
)

a, b = sp.symbols("a b", real=True)
Zcov_sph = sp.Matrix(
    [
        [a, b, 0, 0],
        [b, a - 2 * theta, 0, 0],
        [0, 0, theta, 0],
        [0, 0, 0, theta],
    ]
)
Zmix_sph = eta * Zcov_sph

assert sp.trace(Zmix_sph) == 0

Z2_sph = sp.factor(sp.trace(Zmix_sph**2))
Z3_sph = sp.factor(sp.trace(Zmix_sph**3))
WZZ_sph = sp.factor(
    sum(
        c_ab_upup(aa, bb, cc, dd)
        * Zmix_sph[cc, aa]
        * Zmix_sph[dd, bb]
        for aa, bb, cc, dd in itertools.product(range(4), repeat=4)
    )
)

D_sph_general = sp.factor(WZZ_sph * W2_sph - 2 * W3_sph * Z2_sph)
N_sph_general = sp.factor(W3_sph * Z3_sph * W2_sph)

spherical_factor = sp.factor((a - b - theta) * (a + b - theta))

assert W2_sph == 48 * q**2
assert W3_sph == 96 * q**3
assert D_sph_general == -576 * q**3 * spherical_factor
assert N_sph_general == -27648 * q**5 * theta * spherical_factor
assert sp.factor(N_sph_general / D_sph_general) == W2_sph * theta


# Old Petrov regulator: exact continuity failure.

type_d = {e1: -2 * q, e2: q}
W2_d = sp.factor(W2.subs(type_d))
W3_d = sp.factor(W3.subs(type_d))
D_d = sp.factor(D.subs(type_d))
N_d = sp.factor(N.subs(type_d))
Delta_d = sp.factor(DeltaW.subs(type_d))

assert W2_d == 48 * q**2
assert W3_d == 96 * q**3
assert Delta_d == 0

A, B = sp.symbols("A B", real=True)
local_z = {
    z0: A - theta,
    z1: B - theta,
    z2: theta,
}
D_local = sp.factor(D_d.subs(local_z))
N_local = sp.factor(N_d.subs(local_z))

assert D_local == -288 * q**3 * (A**2 + B**2)
assert N_local == -13824 * q**5 * A * B * (A + B - 2 * theta)

spherical_path = {A: epsilon, B: -epsilon}
spherical_ratio = sp.factor((N_local / D_local).subs(spherical_path))
assert spherical_ratio == 48 * q**2 * theta

simultaneous_zero = {
    e1: -2 * q,
    e2: q,
    z0: -theta,
    z1: -theta,
    z2: theta,
}
assert sp.simplify(D.subs(simultaneous_zero)) == 0
assert sp.simplify(N.subs(simultaneous_zero)) == 0
assert sp.simplify(DeltaW.subs(simultaneous_zero)) == 0
assert sp.simplify(Z3.subs(simultaneous_zero)) == 0

R_mu = sp.factor(N * D / (D**2 + mu * DeltaW * Z2**2))

spherical_full = {
    e1: -2 * q,
    e2: q,
    z0: -theta + epsilon,
    z1: -theta - epsilon,
    z2: theta,
}
D_spherical_path = sp.factor(D.subs(spherical_full))
N_spherical_path = sp.factor(N.subs(spherical_full))

assert D_spherical_path == -576 * epsilon**2 * q**3
assert N_spherical_path == -27648 * epsilon**2 * q**5 * theta
assert sp.factor(N_spherical_path / D_spherical_path) == 48 * q**2 * theta

weyl_split = {
    e1: -2 * q + epsilon,
    e2: q,
    z0: -theta,
    z1: -theta,
    z2: theta,
}
D_split = sp.factor(D.subs(weyl_split))
N_split = sp.factor(N.subs(weyl_split))
Delta_split = sp.factor(DeltaW.subs(weyl_split))
Z2_split = sp.factor(Z2.subs(weyl_split))

assert D_split == 128 * epsilon**2 * theta**2 * (-epsilon + 2 * q)
assert N_split == 0
assert Delta_split == 1024 * epsilon**2 * (-2 * epsilon + 3 * q) ** 2 * (
    -epsilon + 3 * q
) ** 2
assert Z2_split == 4 * theta**2
assert sp.simplify(R_mu.subs(weyl_split)) == 0


# Direction dependence inside type D.

type_d_path = {A: epsilon, B: k * epsilon}
type_d_ratio = sp.factor((N_local / D_local).subs(type_d_path))
type_d_limit = sp.factor(sp.limit(type_d_ratio, epsilon, 0))
expected_type_d_limit = -96 * q**2 * theta * k / (1 + k**2)

assert sp.simplify(type_d_limit - expected_type_d_limit) == 0
assert sp.simplify(type_d_limit.subs(k, -1) - 48 * q**2 * theta) == 0
assert sp.simplify(type_d_limit.subs(k, 1) + 48 * q**2 * theta) == 0


# Local principal-plane target and a continuity-only blend.

Csum = A + B - 2 * theta
Theta_h = sp.factor(-Csum / 2)
T = sp.factor(W2_d * Theta_h)
J_h = sp.factor((A + B) ** 2 / 2)

assert T == -24 * q**2 * Csum
assert sp.simplify(T.subs(B, -A) - 48 * q**2 * theta) == 0

z3_local = sp.factor(z3.subs(local_z))
assert sp.simplify(z2.subs(local_z) - z3_local - (A + B)) == 0
assert sp.simplify(J_h - (z2.subs(local_z) - z3_local) ** 2 / 2) == 0

defect = sp.factor(N_local - T * D_local)
assert defect == -6912 * q**5 * Csum * (A + B) ** 2

A_align = sp.factor(mu * W2_d**4 * J_h)
R_blend = sp.factor(
    (N_local * D_local + T * A_align) / (D_local**2 + A_align)
)
blend_difference = sp.factor(R_blend - T)

S = A + B
R2 = A**2 + B**2
expected_blend_difference = sp.factor(
    24 * q**2 * S**2 * R2 * Csum / (R2**2 + 32 * mu * q**2 * S**2)
)
assert sp.simplify(blend_difference - expected_blend_difference) == 0

for k_value in (-2, -1, 0, 1, 2):
    limit_value = sp.factor(
        sp.limit(
            R_blend.subs({A: epsilon, B: k_value * epsilon}),
            epsilon,
            0,
        )
    )
    assert sp.simplify(limit_value - 48 * q**2 * theta) == 0

# The simplest alignment blend is continuous but not C^2.
alpha, beta, t = sp.symbols("alpha beta t", real=True)
generic_line = sp.factor(
    blend_difference.subs({A: alpha * t, B: beta * t})
)

generic_second = sp.factor(sp.limit(2 * generic_line / t**2, t, 0))
expected_generic_second = -3 * theta * (alpha**2 + beta**2) / mu
assert sp.simplify(generic_second - expected_generic_second) == 0

tangent_line = sp.simplify(generic_line.subs({alpha: 1, beta: -1}))
normal_line = sp.factor(generic_line.subs({alpha: 1, beta: 1}))

assert tangent_line == 0
normal_second = sp.simplify(sp.limit(2 * normal_line / t**2, t, 0))
assert sp.simplify(normal_second + 6 * theta / mu) == 0

delta = sp.symbols("delta", real=True)
near_tangent_second = sp.simplify(
    expected_generic_second.subs({alpha: 1, beta: -1 + delta})
)
assert sp.simplify(sp.limit(near_tangent_second, delta, 0) + 6 * theta / mu) == 0


def main() -> None:
    print("== NPQT Petrov-regulator continuity gate ==")
    print("General spherical algebraic curvature:")
    print(f"W2 = {W2_sph}")
    print(f"D = {D_sph_general}")
    print(f"N = {N_sph_general}")
    print(f"N/D = {sp.factor(N_sph_general / D_sph_general)}")
    print()
    print("Type-D diagonal family:")
    print(f"D = {D_local}")
    print(f"N = {N_local}")
    print(f"spherical N/D = {spherical_ratio}")
    print()
    print("At A=B=0: D=N=Delta_W=0.")
    print("Old Petrov regulator path limits:")
    print(f"  spherical path -> {spherical_ratio}")
    print("  Weyl-splitting path -> 0")
    print("Therefore the old toy has no continuous extension there.")
    print()
    print("Within exact type D, B=kA gives")
    print(f"lim N/D = {type_d_limit}")
    print("so k=-1 gives +48 q^2 theta and k=+1 gives -48 q^2 theta.")
    print()
    print("Principal-plane local target:")
    print(f"Theta_h = {Theta_h}")
    print(f"T = W2 Theta_h = {T}")
    print(f"J_h = {J_h}")
    print(f"N - T D = {defect}")
    print()
    print("Continuity-only blend:")
    print("R_blend = (N D + T A_align)/(D^2 + A_align)")
    print("A_align = mu W2^4 J_h")
    print(f"R_blend - T = {blend_difference}")
    print("This is continuous at A=B=0, but it is not C^2:")
    print(f"  generic non-tangent second directional correction = {generic_second}")
    print("  exact spherical-tangent second directional correction = 0")
    print("  nearby directions approach -6*theta/mu at (1,-1)")
    print()
    print("Conclusion: the next representative should construct a smooth")
    print("covariant extension of the spherical target Theta itself, not")
    print("merely add a Petrov/alignment term to the old denominator.")
    print("All continuity-gate assertions passed.")


if __name__ == "__main__":
    main()
