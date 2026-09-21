#!/usr/bin/env python3
"""Rewrite the regular two-vector branch in sum/difference variables.

Define
    U = (A+B)/sqrt(2),
    V = (A-B)/sqrt(2).

On the regular branch q_b=-q_a=q:
- U is regular at the center;
- V is a divergence-free Coulomb-like null auxiliary profile ~ r^-2;
- both are parallel null vectors;
- the tensor-principal deformation is the cross tensor U_(mu V_nu).

This basis makes the cancellation mechanism and the hidden characteristic
singularity more transparent.
"""

from __future__ import annotations

import sympy as sp


r,M,q,ell=sp.symbols("r M q ell", positive=True, finite=True)
sqrt2=sp.sqrt(2)


def main():
    D=r**3+2*q*ell**2
    f=sp.factor(1-2*M*r**2/D)

    a=sp.factor((r-r*f-q/2)/(2*r**2))
    b=sp.factor((r-r*f+q/2)/(2*r**2))

    u=sp.factor((a+b)/sqrt2)
    v=sp.factor((a-b)/sqrt2)

    expected_u=sp.factor(sqrt2*M*r/D)
    expected_v=sp.factor(-q/(2*sqrt2*r**2))

    assert sp.simplify(u-expected_u)==0
    assert sp.simplify(v-expected_v)==0

    div=lambda p: sp.factor(sp.diff(p,r)+2*p/r)
    divu=div(u)
    divv=div(v)

    assert sp.simplify(divv)==0
    assert sp.simplify(
        divu-6*sqrt2*M*q*ell**2/D**2
    )==0

    # Cross tensor amplitude:
    # AA-BB = U V + V U; for parallel profiles amplitude = 2 u v.
    cross_amp=sp.factor(2*u*v)
    expected_cross=sp.factor(-M*q/(r*D))
    assert sp.simplify(cross_amp-expected_cross)==0

    center_u=sp.simplify(sp.limit(u/r,r,0))
    center_v=sp.simplify(sp.limit(r**2*v,r,0))
    assert sp.simplify(
        center_u-M/(sqrt2*q*ell**2)
    )==0
    assert sp.simplify(
        center_v+q/(2*sqrt2)
    )==0

    center_cross=sp.simplify(
        sp.limit(r*cross_amp,r,0)
    )
    assert sp.simplify(
        center_cross+M/(2*ell**2)
    )==0

    # The null cross tensor has vanishing polynomial norm if U,V are parallel
    # null vectors.  Algebraically, with U^2=V^2=U.V=0:
    U2,V2,UV=sp.symbols("U2 V2 UV")
    # T_mn = U_m V_n + V_m U_n
    # T_mn T^mn = 2 U^2 V^2 + 2 (U.V)^2
    T2=sp.factor(2*U2*V2+2*UV**2)
    assert T2.subs({U2:0,V2:0,UV:0})==0

    # Rewrite L[A]-L[B] algebraically.
    S,P,thetaU,thetaV=sp.symbols(
        "S P theta_U theta_V"
    )
    # S=U^2+V^2, P=U.V
    A2=(S+2*P)/2
    B2=(S-2*P)/2
    thetaA=(thetaU+thetaV)/sqrt2
    thetaB=(thetaU-thetaV)/sqrt2

    cubic=sp.factor(
        8*(A2*thetaA-B2*thetaB)
    )
    quartic=sp.factor(
        6*(A2**2-B2**2)
    )

    expected_cubic=sp.factor(
        4*sqrt2*S*thetaV
        +8*sqrt2*P*thetaU
    )
    expected_quartic=sp.factor(12*S*P)

    assert sp.simplify(cubic-expected_cubic)==0
    assert sp.simplify(quartic-expected_quartic)==0

    print("== Sum/difference profiles ==")
    print(f"U profile u(r) = {u}")
    print(f"V profile v(r) = {v}")
    print()
    print(f"div U = {divu}")
    print(f"div V = {divv}")
    print()
    print("Near r=0:")
    print(f"u/r -> {center_u}")
    print(f"r^2 v -> {center_v}")
    print("Thus U is regular while V ~ r^-2.")
    print()
    print("== Cross tensor ==")
    print(f"2 u v = {cross_amp}")
    print(f"r (2uv) -> {center_cross}")
    print(
        "AA-BB = U_mu V_nu + V_mu U_nu is null-rank-one "
        "on the background."
    )
    print(f"its polynomial norm T_mn T^mn = {T2} -> 0")
    print()
    print("== Interaction in U,V variables ==")
    print("Einstein-tensor piece: 8 G^{mu nu} U_mu V_nu")
    print(f"cubic difference = {cubic}")
    print(f"quartic difference = {quartic}")
    print()
    print(
        "The regular background is supported by an off-diagonal constrained "
        "system containing a singular divergence-free null auxiliary profile."
    )
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
