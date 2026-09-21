#!/usr/bin/env python3
"""Audit all one-time-derivative/algebraic-vector mixings in direct l=2.

This module imports the brute-force original-action expansion from
direct_two_vector_odd_l2.py and inspects the canonicalized one-vector
quadratic expression Vc.

The goal is to verify whether the derivative-null A/B combination can still
couple linearly to dot(W) or other velocities.  Such terms do not appear in
the velocity Hessian, but eliminating an algebraic null field could feed back
into the reduced kinetic matrix.

We extract all coefficients relevant to one vector sector:

    u * dot(W)
    W * dot(u)
    u * dot(u)
    Q * dot(u)
    Q * dot(W)

and reduce u*dot(W) by time integration by parts so the invariant first-order
mixing is represented as W*dot(u).

The script prints exact expressions for CI/log inspection and encodes the
relations needed by the active/null basis audit.
"""

from __future__ import annotations

import sympy as sp

import direct_two_vector_odd_l2 as d


Vc=sp.expand(d.Vc)

u_wd=sp.factor(
    sp.diff(sp.diff(Vc,d.u0),d.wd)
)
w_ud=sp.factor(
    sp.diff(sp.diff(Vc,d.w0),d.ud)
)
u_ud=sp.factor(
    sp.diff(sp.diff(Vc,d.u0),d.ud)
)
q_ud=sp.factor(
    sp.diff(sp.diff(Vc,d.q0),d.ud)
)
q_wd=sp.factor(
    sp.diff(sp.diff(Vc,d.q0),d.wd)
)

# Because background coefficients are time independent,
# c*u*Wdot = -c*W*udot + total_t derivative.
# Hence the canonical W*udot coefficient is:
canonical_w_ud=sp.factor(
    w_ud-u_wd
)

# The direct source-action calculation already found no vector contribution
# to Q*Wdot.
assert q_wd==0

# u*udot is a pure time boundary term for a time-independent coefficient and
# can be discarded from the canonical quadratic action.
# Record rather than assume it vanishes.
canonical_u_ud=sp.factor(u_ud)

# Known Q*udot coefficient for cross-check.
assert sp.simplify(
    q_ud
    +96*sp.pi*d.p*2/(5*d.r*d.f)
)==0


def main():
    print("== Direct l=2 one-velocity audit ==")
    print(f"u * Wdot coefficient = {u_wd}")
    print(f"W * udot coefficient = {w_ud}")
    print(f"canonical W * udot coefficient = {canonical_w_ud}")
    print(f"u * udot coefficient = {canonical_u_ud}")
    print(f"Q * udot coefficient = {q_ud}")
    print(f"Q * Wdot vector coefficient = {q_wd}")
    print()
    print(
        "Use canonical W*udot together with the A-B signs to test whether "
        "the derivative-null vector combination couples to the remaining "
        "kinetic variables after basis rotation."
    )
    print("One-velocity audit completed.")


if __name__=="__main__":
    main()
