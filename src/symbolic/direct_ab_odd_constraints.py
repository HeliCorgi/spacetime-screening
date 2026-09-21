#!/usr/bin/env python3
"""Direct canonical constraint analysis of the l=1 odd principal action.

This continues direct_ab_odd_principal.py and uses only the principal action
derived from the original A-B action:

    L = 1/2 X^2 - S (dot y - y') X,

    X = dot H - Q',

where y is the normalized derivative-active vector combination

    y ∝ a u_A - b u_B,

and S>0 denotes its local mixing magnitude.  The orthogonal vector
combination z has no principal derivatives.

Canonical variables:
    Q : axial metric Lagrange multiplier, no dot Q
    H : axial metric spatial component
    y : active vector combination
    z : principal-null vector combination

The velocity Hessian in (dot H, dot y) is nondegenerate with determinant
-S^2<0.  Thus there is no primary constraint involving y.

Primary constraints:
    p_Q = 0
    p_z = 0   (at principal order)

Preservation of p_Q gives the 2D Gauss constraint
    d_x p_H = 0.

For local finite-k modes this sets p_H=0 and removes the l=1 metric Maxwell
mode.  The remaining active-vector Hamiltonian is

    H_phys = p_y y' - p_y^2/(2 S^2),

which is unbounded below.

Hence the principal degeneracy removes the orthogonal vector combination,
not the negative-kinetic active combination.
"""

from __future__ import annotations

import sympy as sp


S=sp.symbols("S", positive=True, finite=True)

Qx,Ht,yt,yx=sp.symbols(
    "Q_x H_t y_t y_x", real=True
)

X=Ht-Qx
L=sp.expand(
    sp.Rational(1,2)*X**2
    -S*(yt-yx)*X
)

pH=sp.factor(sp.diff(L,Ht))
py=sp.factor(sp.diff(L,yt))

# Velocity Hessian in (H_t, y_t).
Hvel=sp.hessian(L,(Ht,yt))
detH=sp.factor(Hvel.det())

assert sp.simplify(
    Hvel-sp.Matrix([[1,-S],[-S,0]])
)==sp.zeros(2)
assert sp.simplify(detH+S**2)==0

# Solve velocities in terms of canonical momenta.
PH,PY=sp.symbols("p_H p_y", real=True)

sol=sp.solve(
    [sp.Eq(PH,pH),sp.Eq(PY,py)],
    [Ht,yt],
    dict=True,
)[0]

Ht_sol=sp.factor(sol[Ht])
yt_sol=sp.factor(sol[yt])

expected_Ht=sp.factor(Qx-PY/S)
expected_yt=sp.factor(
    yx-PH/S-PY/S**2
)

assert sp.simplify(Ht_sol-expected_Ht)==0
assert sp.simplify(yt_sol-expected_yt)==0

Hamiltonian=sp.factor(
    (PH*Ht+PY*yt-L).subs(sol)
)

expected_H=sp.factor(
    PH*Qx
    +PY*yx
    -PH*PY/S
    -PY**2/(2*S**2)
)

assert sp.simplify(Hamiltonian-expected_H)==0

# Q enters only through Q' p_H.  After spatial integration by parts it
# imposes p_H'=0.  For local k != 0 modes, p_H=0.
Hlocal=sp.factor(expected_H.subs(PH,0))
expected_local=sp.factor(
    PY*yx-PY**2/(2*S**2)
)
assert sp.simplify(Hlocal-expected_local)==0

# Principal Hamiltonian curvature in p_y is negative.
d2H_dpy2=sp.factor(sp.diff(Hlocal,PY,2))
assert sp.simplify(d2H_dpy2+1/S**2)==0

# Euler-Lagrange principal equations in symbolic derivative placeholders:
# Q: d_x (X - S(yt-yx)) = 0
# H: d_t (X - S(yt-yx)) = 0
# so the metric momentum is locally constant.
metric_momentum=sp.factor(
    X-S*(yt-yx)
)
assert sp.simplify(metric_momentum-pH)==0


def main():
    print("== Direct l=1 principal canonical system ==")
    print(f"L = {L}")
    print()
    print("velocity Hessian in (dot H, dot y):")
    print(Hvel)
    print(f"det = {detH} < 0")
    print("=> active y is not part of a primary kinetic degeneracy.")
    print()
    print("canonical momenta:")
    print(f"p_H = {pH}")
    print(f"p_y = {py}")
    print()
    print("solved velocities:")
    print(f"dot H = {Ht_sol}")
    print(f"dot y = {yt_sol}")
    print()
    print("Hamiltonian:")
    print(Hamiltonian)
    print()
    print("Gauss constraint from Q: d_x p_H = 0")
    print("for local k != 0 modes: p_H = 0")
    print(f"H_phys = {Hlocal}")
    print(f"d2 H_phys / d p_y^2 = {d2H_dpy2} < 0")
    print()
    print(
        "The l=1 metric mode is removed by the Gauss constraint, while the "
        "active vector combination remains with an unbounded-below quadratic "
        "momentum term.  The orthogonal vector combination is the principal "
        "zero mode handled separately by lower-derivative constraints."
    )
    print("All direct canonical assertions passed.")


if __name__=="__main__":
    main()
