#!/usr/bin/env python3
"""Misner-space principal-symbol gate for chronology-protection research.

Metric convention:

    ds^2 = -2 dT dpsi - T dpsi^2,

with psi periodically identified.

The script verifies that:
- det(g)=-1 everywhere, including the chronology horizon T=0;
- the spacetime is flat;
- the periodic generator d/dpsi is spacelike for T<0, null at T=0,
  and timelike for T>0;
- the Klein-Gordon principal metric remains nondegenerate Lorentzian at T=0;
- the horizon normal dT becomes characteristic at T=0;
- the scalar wave operator has principal polynomial
      P(xi)=T xi_T^2 - 2 xi_T xi_psi.

Thus the appearance of CTCs in fixed-background Misner space is not caused by
a local rank loss of the wave operator's principal symbol.  The global Cauchy
property ends at a smooth characteristic horizon instead.

This is a REPRODUCED HERE / diagnostic calculation, not a novelty claim.
"""

from __future__ import annotations

import sympy as sp


T, psi = sp.symbols("T psi", real=True)
xi_T, xi_psi = sp.symbols("xi_T xi_psi", real=True)

coords = (T, psi)

# Coordinates ordered as (T, psi).
g = sp.Matrix(
    [
        [0, -1],
        [-1, -T],
    ]
)
g_inv = sp.simplify(g.inv())

assert sp.factor(g.det()) == -1
assert g_inv == sp.Matrix([[T, -1], [-1, 0]])
assert sp.factor(g_inv.det()) == -1

# Periodic Killing/generator k = partial_psi.
k = sp.Matrix([0, 1])
k_norm = sp.factor((k.T * g * k)[0])
assert k_norm == -T

# Scalar principal polynomial P(xi)=g^{ab} xi_a xi_b.
xi = sp.Matrix([xi_T, xi_psi])
P = sp.factor((xi.T * g_inv * xi)[0])
assert sp.expand(P - (T * xi_T**2 - 2 * xi_T * xi_psi)) == 0

# The horizon T=0 is characteristic: its normal is dT.
dT = sp.Matrix([1, 0])
normal_norm = sp.factor((dT.T * g_inv * dT)[0])
assert normal_norm == T
assert sp.simplify(normal_norm.subs(T, 0)) == 0

# Yet the principal metric itself does not lose rank at the horizon.
assert sp.factor(g_inv.det().subs(T, 0)) == -1

# Direct curvature check.
n = 2
Gamma = [[[sp.Integer(0) for _ in range(n)] for _ in range(n)] for _ in range(n)]
for a in range(n):
    for b in range(n):
        for c in range(n):
            Gamma[a][b][c] = sp.simplify(
                sp.Rational(1, 2)
                * sum(
                    g_inv[a, d]
                    * (
                        sp.diff(g[d, c], coords[b])
                        + sp.diff(g[d, b], coords[c])
                        - sp.diff(g[b, c], coords[d])
                    )
                    for d in range(n)
                )
            )

Riemann = sp.MutableDenseNDimArray.zeros(n, n, n, n)
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                Riemann[a, b, c, d] = sp.simplify(
                    sp.diff(Gamma[a][b][d], coords[c])
                    - sp.diff(Gamma[a][b][c], coords[d])
                    + sum(
                        Gamma[a][c][e] * Gamma[e][b][d]
                        - Gamma[a][d][e] * Gamma[e][b][c]
                        for e in range(n)
                    )
                )

Ricci = sp.Matrix(
    n,
    n,
    lambda b, d: sp.simplify(sum(Riemann[a, b, a, d] for a in range(n))),
)
assert Ricci == sp.zeros(2)

R_scalar = sp.simplify(
    sum(g_inv[a, b] * Ricci[a, b] for a in range(n) for b in range(n))
)
assert R_scalar == 0

# Full massless scalar wave operator, since sqrt(|det g|)=1.
phi = sp.Function("phi")(T, psi)
box_phi = sp.expand(
    sp.diff(
        g_inv[0, 0] * sp.diff(phi, T)
        + g_inv[0, 1] * sp.diff(phi, psi),
        T,
    )
    + sp.diff(
        g_inv[1, 0] * sp.diff(phi, T)
        + g_inv[1, 1] * sp.diff(phi, psi),
        psi,
    )
)

expected_box = (
    T * sp.diff(phi, T, 2)
    + sp.diff(phi, T)
    - 2 * sp.diff(phi, T, psi)
)
assert sp.simplify(box_phi - expected_box) == 0


def main() -> None:
    print("== Misner chronology / principal-symbol gate ==")
    print(f"det(g) = {sp.factor(g.det())}")
    print(f"g^(-1) = {g_inv}")
    print(f"Ricci = {Ricci}")
    print(f"R = {R_scalar}")
    print()
    print(f"norm(partial_psi) = {k_norm}")
    print("  T<0: periodic orbit spacelike")
    print("  T=0: periodic orbit null (chronology/Cauchy horizon)")
    print("  T>0: periodic orbit timelike -> CTC")
    print()
    print(f"P(xi) = {P}")
    print(f"P(dT) = {normal_norm}")
    print(f"det(g^ab)|_T=0 = {sp.factor(g_inv.det().subs(T, 0))}")
    print(f"Box phi = {box_phi}")
    print()
    print("Conclusion:")
    print("The local Klein-Gordon principal metric remains nondegenerate and")
    print("Lorentzian at T=0.  The chronology horizon is characteristic, but")
    print("there is no local principal-rank singularity there.  Chronology")
    print("failure is therefore a global/QFT-state obstruction in this")
    print("testbed, not a classical local principal-symbol degeneration.")
    print("All Misner principal-gate assertions passed.")


if __name__ == "__main__":
    main()
