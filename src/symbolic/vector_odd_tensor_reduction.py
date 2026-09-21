#!/usr/bin/env python3
"""High-frequency odd tensor reduction for the two-vector regular branch.

Using the standard l>=2 odd quadratic-action coefficients, define

    Delta = 4 ell^2 (a^2-b^2).

For the shared metric block (h=f),

    C1  = 1/(2 r^2),
    C8  = -(f+Delta)/(2 r^4),
    D   = Delta/(f r^4),   # W-Q derivative mixing coefficient
    C10 = (f-Delta)/(2 f^2 r^4).

The reduced tensor kinetic coefficient is

    q_T = 4 C1^2 C10 / (D^2 - 4 C8 C10)
        = (f-Delta)/(2 f^2).

The radial coordinate characteristics are

    v_\pm = [D +/- sqrt(D^2-4 C8 C10)]/(2 C10),

giving
    v_- = -f,
    v_+ = f (f+Delta)/(f-Delta).

On the exact regular branch,
    f+Delta = 1 - 2M/r.

Thus r=2M is a tensor characteristic horizon.  The background metric is
regular there and its own outer horizon lies strictly inside 2M for q>0.

This is the standard odd quadratic-action principal block, stronger than the
earlier local-TT-only heuristic.  A fully explicit two-vector harmonic
derivation is still retained as the final independent verification.
"""

from __future__ import annotations

import sympy as sp


r,M,q,ell=sp.symbols(
    "r M q ell", positive=True, finite=True
)

D0=r**3+2*q*ell**2
f=sp.factor(1-2*M*r**2/D0)

a=sp.factor((r-r*f-q/2)/(2*r**2))
b=sp.factor((r-r*f+q/2)/(2*r**2))

Delta=sp.factor(4*ell**2*(a**2-b**2))
expected_Delta=sp.factor(
    -4*M*q*ell**2/(r*D0)
)
assert sp.simplify(Delta-expected_Delta)==0

C1=sp.factor(1/(2*r**2))
C8=sp.factor(-(f+Delta)/(2*r**4))
mix=sp.factor(Delta/(f*r**4))
C10=sp.factor((f-Delta)/(2*f**2*r**4))

disc=sp.factor(mix**2-4*C8*C10)
assert sp.simplify(disc-1/r**8)==0

qT=sp.factor(
    4*C1**2*C10/disc
)
expected_qT=sp.factor(
    (f-Delta)/(2*f**2)
)
assert sp.simplify(qT-expected_qT)==0

vplus=sp.factor(
    (mix+1/r**4)/(2*C10)
)
vminus=sp.factor(
    (mix-1/r**4)/(2*C10)
)

assert sp.simplify(
    vplus-f*(f+Delta)/(f-Delta)
)==0
assert sp.simplify(vminus+f)==0

fT=sp.factor(f+Delta)
assert sp.simplify(
    fT-(1-2*M/r)
)==0

# At r=2M the background is not a metric horizon.
f2M=sp.factor(f.subs(r,2*M))
expected_f2M=sp.factor(
    q*ell**2/(4*M**3+q*ell**2)
)
assert sp.simplify(f2M-expected_f2M)==0

Delta2M=sp.factor(Delta.subs(r,2*M))
assert sp.simplify(Delta2M+f2M)==0

qT2M=sp.factor(qT.subs(r,2*M))
assert sp.simplify(qT2M-1/f2M)==0

# Near-center behavior.
qT_core=sp.simplify(
    sp.limit(r*qT,r,0,dir="+")
)
assert sp.simplify(qT_core-M)==0

# The tensor characteristic function has Schwarzschild surface gravity
# derivative at r=2M.
dfT=sp.diff(fT,r)
dfT_h=sp.simplify(dfT.subs(r,2*M))
assert sp.simplify(dfT_h-1/(2*M))==0


def main():
    print("== Exact odd tensor coefficients ==")
    print(f"Delta = {Delta}")
    print(f"C1 = {C1}")
    print(f"C8 = {C8}")
    print(f"D_mix = {mix}")
    print(f"C10 = {C10}")
    print(f"discriminant = {disc}")
    print()
    print("== Reduced tensor kinetic coefficient ==")
    print(f"q_T = {qT}")
    print()
    print("== Coordinate radial characteristics ==")
    print(f"v_- = {vminus}")
    print(f"v_+ = {vplus}")
    print()
    print("== Hidden tensor horizon ==")
    print(f"f_T = f+Delta = {fT}")
    print("r_T = 2M")
    print(f"background f(2M) = {f2M} > 0")
    print(f"q_T(2M) = {qT2M} > 0")
    print(f"f_T'(2M) = {dfT_h}")
    print()
    print("== Core ==")
    print(f"r q_T -> {qT_core}")
    print("so q_T ~ M/r diverges positively toward the regular center.")
    print()
    print(
        "Interpretation: r=2M is a regular tensor characteristic horizon, "
        "not a kinetic ghost surface.  The tensor principal coefficients "
        "nevertheless become singular toward the metric-regular core."
    )
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
