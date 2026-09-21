#!/usr/bin/env python3
"""Local spectral-cluster extension of the spherical NPQT Ricci mode.

The continuity gate for the displayed cubic NPQT rational term identifies its
exact spherical target as

    T_sph = W2 * Theta,

where Theta is the repeated angular eigenvalue of the traceless Ricci tensor.

This script asks whether the repeated spacelike Weyl two-plane itself can be
continued through a local Petrov-D -> type-I eigenvalue splitting, at least in
the purely-electric algebraic sector.

For a real symmetric tracefree electric-Weyl operator E with an isolated
simple eigenvalue lambda_s, the spectral projector onto that eigenspace is

    P_s = [E^2 + lambda_s E + (lambda_s^2 - I2/2) I]
          / [3 lambda_s^2 - I2/2],

where I2 = tr(E^2).  The complementary projector h = I-P_s selects the
two-dimensional eigenvalue cluster that is degenerate at type D.

For the split family

    eigenvalues(E) = (-2q, q+delta, q-delta),

the projector denominator is

    9 q^2 - delta^2.

Hence it remains finite at the type-D point delta=0 whenever q != 0.

Rotating the split cluster and an anisotropic Ricci block together, the scalar

    Theta_ext = (1/2) tr(h Z_spatial)

is exactly the cluster-average Ricci eigenvalue theta, independent of the
rotation angle, Weyl splitting delta, and internal Ricci anisotropy.

With the purely-electric normalization W2 = 8 tr(E^2),

    W2 Theta_ext = 16 theta (delta^2 + 3 q^2)
                  -> 48 q^2 theta

at type D, matching the spherical target.

This is a local algebraic proof of concept only.  It does not solve the
magnetic-Weyl, Petrov-II/III/N, global branch-selection, or conformally-flat
core C^2 problems.
"""

from __future__ import annotations

import sympy as sp


q, delta, phi = sp.symbols("q delta phi", real=True)
theta, anis, zr = sp.symbols("theta anis zr", real=True)

c = sp.cos(phi)
s = sp.sin(phi)

# Rotate inside the two-dimensional cluster only.
R = sp.Matrix(
    [
        [1, 0, 0],
        [0, c, -s],
        [0, s, c],
    ]
)

Ediag = sp.diag(-2 * q, q + delta, q - delta)
E = sp.simplify(R * Ediag * R.T)

assert sp.simplify(sp.trace(E)) == 0

I2 = sp.factor(sp.trigsimp(sp.trace(E**2)))
assert sp.simplify(I2 - 2 * (delta**2 + 3 * q**2)) == 0

lambda_s = -2 * q
gap_denominator = sp.factor(sp.trigsimp(3 * lambda_s**2 - I2 / 2))
assert sp.simplify(gap_denominator - (9 * q**2 - delta**2)) == 0

I3 = sp.eye(3)

P_simple = sp.simplify(
    (
        E**2
        + lambda_s * E
        + (lambda_s**2 - I2 / 2) * I3
    )
    / gap_denominator
)

expected_P_simple = sp.diag(1, 0, 0)
for i in range(3):
    for j in range(3):
        assert sp.simplify(sp.trigsimp(P_simple[i, j] - expected_P_simple[i, j])) == 0

h = sp.simplify(I3 - P_simple)
expected_h = sp.diag(0, 1, 1)
for i in range(3):
    for j in range(3):
        assert sp.simplify(sp.trigsimp(h[i, j] - expected_h[i, j])) == 0

assert sp.simplify(h * h - h) == sp.zeros(3)
assert sp.simplify(sp.trace(h) - 2) == 0

# A generic Ricci tensor inside the same split cluster.  theta is the cluster
# average and anis is the internal anisotropy.
Zdiag = sp.diag(zr, theta + anis, theta - anis)
Zsp = sp.simplify(R * Zdiag * R.T)

Theta_ext = sp.factor(sp.trigsimp(sp.trace(h * Zsp) / 2))
assert sp.simplify(Theta_ext - theta) == 0

# Purely-electric Weyl normalization used in the repository:
# W2 = 8 tr(E^2).
W2 = sp.factor(8 * I2)
T_ext = sp.factor(sp.trigsimp(W2 * Theta_ext))

assert sp.simplify(W2 - 16 * (delta**2 + 3 * q**2)) == 0
assert sp.simplify(T_ext - 16 * theta * (delta**2 + 3 * q**2)) == 0
assert sp.simplify(T_ext.subs(delta, 0) - 48 * q**2 * theta) == 0

# The spectral cluster is isolated near type D; the first collision with the
# simple eigenvalue occurs at |delta|=3|q|.
assert sp.factor(gap_denominator.subs(delta, 0)) == 9 * q**2


def main() -> None:
    print("== NPQT principal-plane spectral toy ==")
    print(f"I2 = {I2}")
    print(f"simple-eigenvalue gap denominator = {gap_denominator}")
    print()
    print("P_simple =")
    sp.pprint(P_simple)
    print("h = I - P_simple =")
    sp.pprint(h)
    print()
    print(f"Theta_ext = {Theta_ext}")
    print(f"W2 = {W2}")
    print(f"T_ext = W2 Theta_ext = {T_ext}")
    print()
    print("At delta=0 and q!=0 the cluster gap is 9 q^2, so the")
    print("two-plane projector is smooth through the local type-D -> type-I")
    print("splitting and T_ext -> 48 q^2 theta.")
    print()
    print("This does not address the conformally-flat q=0 core, magnetic")
    print("Weyl curvature, algebraically special non-D types, or global")
    print("branch selection.")
    print("All spectral-projector assertions passed.")


if __name__ == "__main__":
    main()
