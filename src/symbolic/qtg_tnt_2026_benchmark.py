#!/usr/bin/env python3
"""2026 4D QTG-TNT regular-black-hole benchmark.

Based on Colléaux, Kolář, Málek, arXiv:2606.17784.

For Lambda=0, k=1, n=0 and
    A(x)=2x/(1-x),
the exact static single-function solution is
    a(r)=((r-2m)(r^2-2 ell^2))/
         (r^3-2 r ell^2+4m ell^2).

This script verifies:
- exact reduced field equation;
- center expansion and finite polynomial curvature invariants;
- divergent box(R) caused by the unavoidable odd-power term;
- the two exact horizons 2m and sqrt(2) ell;
- extremality m=ell/sqrt(2);
- the denominator critical mass 2 ell/(3 sqrt(6));
- the curvature variable x=ell^2 R3 reaches the action pole x=1
  both at the center and at the theory-fixed horizon;
- the Class-I action A(R3) R4 is non-differentiable on the SF branch
  because R4=sqrt(Delta) with Delta=0.
"""

from __future__ import annotations

import sympy as sp


r,m,ell=sp.symbols(
    "r m ell", positive=True, finite=True
)
pi=sp.pi

den=r**3-2*r*ell**2+4*m*ell**2
a=sp.factor(
    (r-2*m)*(r**2-2*ell**2)/den
)

# Static spherical reduced curvature variable.
R3=sp.factor(2*(1-a)/r**2)
x=sp.factor(ell**2*R3)

A=sp.factor(2*x/(1-x))

# Curvature invariants for ds^2=-a dt^2+dr^2/a+r^2 dOmega^2.
ap=sp.diff(a,r)
app=sp.diff(a,r,2)

R=sp.factor(
    -app-4*ap/r+2*(1-a)/r**2
)
Ricci2=sp.factor(
    2*(app/2+ap/r)**2
    +2*(ap/r+(a-1)/r**2)**2
)
K=sp.factor(
    app**2
    +4*(ap/r)**2
    +4*((1-a)/r**2)**2
)

boxR=sp.factor(
    sp.diff(r**2*a*sp.diff(R,r),r)/r**2
)


def main():
    # Reduced equation (6.12):
    # -(1+A/2)a+1=2m/r.
    reduced=sp.simplify(
        -(1+A/2)*a+1-2*m/r
    )
    assert reduced==0

    expected_x=sp.factor(
        4*m*ell**2/den
    )
    assert sp.simplify(x-expected_x)==0

    # Screening-like factor multiplying Schwarzschild.
    Sigma=sp.factor(1-x)
    expected_sigma=sp.factor(
        r*(r**2-2*ell**2)/den
    )
    assert sp.simplify(Sigma-expected_sigma)==0
    assert sp.simplify(
        a-(1-2*m/r)*Sigma
    )==0

    # Center expansion.
    series_a=sp.series(a,r,0,5)
    a2=sp.simplify(
        sp.expand(series_a.removeO()).coeff(r,2)
    )
    a3=sp.simplify(
        sp.expand(series_a.removeO()).coeff(r,3)
    )
    a4=sp.simplify(
        sp.expand(series_a.removeO()).coeff(r,4)
    )
    assert sp.simplify(a2+1/(2*ell**2))==0
    assert sp.simplify(a3+1/(4*m*ell**2))==0
    assert sp.simplify(a4+1/(8*m**2*ell**2))==0

    R0=sp.simplify(sp.limit(R,r,0))
    Ricci20=sp.simplify(sp.limit(Ricci2,r,0))
    K0=sp.simplify(sp.limit(K,r,0))
    assert sp.simplify(R0-6/ell**2)==0
    assert sp.simplify(Ricci20-9/ell**4)==0
    assert sp.simplify(K0-6/ell**4)==0

    # Curvature-derivative singularity.
    boxR_lead=sp.simplify(
        sp.limit(r*boxR,r,0)
    )
    assert sp.simplify(
        boxR_lead-10/(ell**2*m)
    )==0

    # Exact horizons.
    assert sp.simplify(a.subs(r,2*m))==0
    assert sp.simplify(
        a.subs(r,sp.sqrt(2)*ell)
    )==0

    # Extremality when horizons coincide.
    m_ext=ell/sp.sqrt(2)
    assert sp.simplify(
        2*m_ext-sp.sqrt(2)*ell
    )==0

    # Critical mass from double root of the denominator.
    rcrit=sp.sqrt(sp.Rational(2,3))*ell
    mcrit=2*ell/(3*sp.sqrt(6))
    assert sp.simplify(
        den.subs({r:rcrit,m:mcrit})
    )==0
    assert sp.simplify(
        sp.diff(den,r).subs({r:rcrit,m:mcrit})
    )==0

    # For regular m>mcrit, x is maximal at the denominator minimum.
    xcrit=sp.factor(x.subs(r,rcrit))
    expected_xcrit=sp.factor(m/(m-mcrit))
    assert sp.simplify(xcrit-expected_xcrit)==0

    # Action pole x=1 at center and fixed horizon.
    assert sp.limit(x,r,0)==1
    assert sp.simplify(
        x.subs(r,sp.sqrt(2)*ell)-1
    )==0

    # At the Schwarzschild-like horizon x depends on mass.
    x_2m=sp.simplify(x.subs(r,2*m))
    assert sp.simplify(
        x_2m-ell**2/(2*m**2)
    )==0

    # Horizon temperatures on each outer branch.
    ap_2m=sp.factor(ap.subs(r,2*m))
    ap_fixed=sp.factor(
        ap.subs(r,sp.sqrt(2)*ell)
    )
    assert sp.simplify(
        ap_2m-(2*m**2-ell**2)/(4*m**3)
    )==0
    assert sp.simplify(
        ap_fixed
        -sp.sqrt(2)*(sp.sqrt(2)*ell-2*m)/(2*ell*m)
    )==0

    # Generic non-differentiability of the R4=sqrt(Delta) factor.
    Delta=sp.symbols("Delta", positive=True)
    R4=sp.sqrt(Delta)
    dR4=sp.diff(R4,Delta)
    assert dR4==1/(2*sp.sqrt(Delta))
    assert sp.limit(dR4,Delta,0,dir="+")==sp.oo

    # The interaction A(x) R4 has derivative A/(2 sqrt Delta).
    xind=sp.symbols("x", finite=True)
    Aind=2*xind/(1-xind)
    dLint=sp.factor(Aind*dR4)
    assert sp.limit(
        dLint.subs(xind,sp.Rational(1,2)),
        Delta,0,dir="+"
    )==sp.oo

    print("== 2026 first-order QTG-TNT static solution ==")
    print(f"a(r) = {a}")
    print(f"x=ell^2 R3 = {x}")
    print(f"A(x) = {A}")
    print(f"Sigma=1-x = {Sigma}")
    print("a=(1-2m/r) Sigma")
    print()

    print("== Center ==")
    print(f"a(r) = {series_a}")
    print(f"R(0) = {R0}")
    print(f"Ricci^2(0) = {Ricci20}")
    print(f"K(0) = {K0}")
    print(f"r box(R) -> {boxR_lead}")
    print("Thus box(R) ~ 10/(ell^2 m r).")
    print()

    print("== Horizons and mass scales ==")
    print("r_h1 = 2m")
    print("r_h2 = sqrt(2) ell")
    print(f"m_ext = {m_ext}")
    print(f"m_crit = {mcrit}")
    print(f"x_max at r=sqrt(2/3)ell = {xcrit}")
    print("x_max -> infinity as m -> m_crit from above.")
    print()

    print("== Curvature/action pole ==")
    print("x -> 1 at r->0")
    print("x=1 at r=sqrt(2) ell")
    print(f"x(2m) = {x_2m}")
    print(
        "The infinite-tower coupling A=2x/(1-x) diverges at the "
        "regular core and at the theory-fixed horizon."
    )
    print()

    print("== Covariant differentiability warning ==")
    print("R4=sqrt(Delta), with Delta=0 on the SF branch.")
    print(f"dR4/dDelta = {dR4} -> infinity")
    print(f"d[A(x)R4]/dDelta = {dLint}")
    print(
        "So a generic off-SF 4D first variation is non-differentiable "
        "unless an additional extension/cancellation is specified."
    )
    print()
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
