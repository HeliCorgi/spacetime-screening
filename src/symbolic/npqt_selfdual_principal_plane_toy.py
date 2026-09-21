#!/usr/bin/env python3
"""Self-dual Weyl spectral-cluster toy for the NPQT principal-plane route.

A real four-dimensional Weyl tensor can be encoded by its complex self-dual
Weyl operator Q on the three-dimensional self-dual bivector space.  In an
orthonormal SD basis Q is a complex symmetric tracefree 3x3 operator; its real
and imaginary parts encode electric and magnetic Weyl curvature.

This script studies the local split family

    spec(Q) = (-2 rho, rho + delta, rho - delta),

with complex rho and delta allowed.  Thus the calculation is not restricted to
purely electric curvature.

For an isolated simple eigenvalue lambda_s, the algebraic spectral projector is

    P_s = [Q^2 + lambda_s Q + (lambda_s^2 - a/2) I]
          / [3 lambda_s^2 - a/2],

where a = tr(Q^2).

For lambda_s=-2 rho the denominator is

    9 rho^2 - delta^2.

It is nonzero at the type-D point delta=0 whenever rho != 0.  Hence the simple
SD eigenline, and therefore its complementary two-dimensional spectral
cluster, extend analytically through a local type-D -> type-I splitting even
when rho and delta are complex.

At exact type D, with

    a = tr(Q^2), b = tr(Q^3), rho_D = -b/a,

the same projector reduces to the invariant expression

    P_D = (I - Q/rho_D)/3 = (I + (a/b) Q)/3.

A normalized non-null eigenbivector spanning this line is unique up to sign.
The associated real 2+2 structure tensor Pi=2 U dot conjugate(U) is therefore
sign independent.  The remaining problems are global eigen-branch selection,
algebraically special non-D types, and the rho -> 0 conformally-flat core.

This script checks only the operator algebra.  It does not construct the full
four-index spacetime concomitant or prove C^2 regularity at the core.
"""

from __future__ import annotations

import sympy as sp


rho, delta = sp.symbols("rho delta", nonzero=True)
I = sp.eye(3)

Q = sp.diag(-2 * rho, rho + delta, rho - delta)

assert sp.simplify(sp.trace(Q)) == 0

a = sp.factor(sp.trace(Q**2))
b = sp.factor(sp.trace(Q**3))

assert sp.simplify(a - 2 * (delta**2 + 3 * rho**2)) == 0
assert sp.simplify(b - 6 * rho * (delta**2 - rho**2)) == 0

lambda_s = -2 * rho
gap = sp.factor(3 * lambda_s**2 - a / 2)
assert sp.simplify(gap - (9 * rho**2 - delta**2)) == 0

P_simple = sp.simplify(
    (
        Q**2
        + lambda_s * Q
        + (lambda_s**2 - a / 2) * I
    )
    / gap
)
expected = sp.diag(1, 0, 0)

assert sp.simplify(P_simple - expected) == sp.zeros(3)
assert sp.simplify(P_simple**2 - P_simple) == sp.zeros(3)
assert sp.simplify(sp.trace(P_simple) - 1) == 0
assert sp.simplify(Q * P_simple - lambda_s * P_simple) == sp.zeros(3)

H_cluster = sp.simplify(I - P_simple)
assert sp.simplify(H_cluster**2 - H_cluster) == sp.zeros(3)
assert sp.simplify(sp.trace(H_cluster) - 2) == 0

# Exact type-D invariant identities.
a_D = sp.factor(a.subs(delta, 0))
b_D = sp.factor(b.subs(delta, 0))
rho_D = sp.factor(-b_D / a_D)
Q_D = Q.subs(delta, 0)

assert sp.simplify(a_D - 6 * rho**2) == 0
assert sp.simplify(b_D + 6 * rho**3) == 0
assert sp.simplify(rho_D - rho) == 0

P_D_invariant = sp.simplify((I - Q_D / rho_D) / 3)
P_D_ab = sp.simplify((I + (a_D / b_D) * Q_D) / 3)

assert sp.simplify(P_D_invariant - expected) == sp.zeros(3)
assert sp.simplify(P_D_ab - expected) == sp.zeros(3)

# The type-D minimal polynomial in this normalization:
# (Q + 2 rho I)(Q - rho I)=0.
minimal_D = sp.expand((Q_D + 2 * rho * I) * (Q_D - rho * I))
assert sp.simplify(minimal_D) == sp.zeros(3)

# The cluster gap at type D closes only at rho=0.
gap_D = sp.factor(gap.subs(delta, 0))
assert gap_D == 9 * rho**2


def main() -> None:
    print("== NPQT self-dual principal-plane spectral toy ==")
    print(f"a = tr(Q^2) = {a}")
    print(f"b = tr(Q^3) = {b}")
    print(f"simple-root gap = {gap}")
    print()
    print("P_simple =")
    sp.pprint(P_simple)
    print("H_cluster = I - P_simple =")
    sp.pprint(H_cluster)
    print()
    print("Exact type D:")
    print(f"a_D = {a_D}")
    print(f"b_D = {b_D}")
    print(f"rho_D = -b_D/a_D = {rho_D}")
    print("P_D = (I - Q/rho_D)/3 = (I + (a_D/b_D) Q)/3")
    print()
    print("Conclusion: allowing complex rho,delta (electric + magnetic Weyl)")
    print("does not spoil the local spectral-cluster continuation while the")
    print("simple root remains isolated.  The unresolved singular stratum is")
    print("the conformally-flat rho=0 core, together with global branch")
    print("selection and non-D algebraically special directions.")
    print("All self-dual spectral assertions passed.")


if __name__ == "__main__":
    main()
