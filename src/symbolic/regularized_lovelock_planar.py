#!/usr/bin/env python3
"""Regularized-Lovelock planar black-hole benchmark.

Based on:
- P. G. S. Fernandes, Phys. Rev. D 112, 084028 (2025)
- A. De Felice & S. Tsujikawa, Phys. Rev. D 112, 064023 (2025)

Model 2 uses the resummed regular metric
    f(r) = -(r^2/ell^2) tanh(x),
    x(r) = -ell^2/LambdaL^2 + 2 M ell^2/r^3,

with scalar profile phi'(r)=1/r.

The background is regular at r=0:
    f ~ -r^2/ell^2,
    X = -f phi'^2/2 -> 1/(2 ell^2),
    K -> 24/ell^4.

But the published odd-parity angular propagation speed is
    c_Omega^2 = 1 - 12 M ell^2 tanh(x)/r^3,
which tends to -infinity for M>0 as r->0.

The published even-parity analysis further finds det K = det G = 0
for the scalar-containing mode on phi'=1/r, i.e. infinite strong coupling.
"""

from __future__ import annotations

import sympy as sp


r,M,ell,L=sp.symbols(
    "r M ell L", positive=True, finite=True
)

x=-ell**2/L**2 + 2*M*ell**2/r**3
f=sp.factor(-r**2/ell**2*sp.tanh(x))

# phi'=1/r and X=-1/2 g^rr phi'^2=-f/(2r^2)
X=sp.factor(-f/(2*r**2))

# Planar k=0 curvature formulas for ds^2=-f dt^2+dr^2/f+r^2(dx^2+dy^2).
fp=sp.diff(f,r)
fpp=sp.diff(f,r,2)

R=sp.factor(
    -fpp - 4*fp/r - 2*f/r**2
)

K=sp.factor(
    fpp**2
    + 4*(fp/r)**2
    + 4*(f/r**2)**2
)

# Published Model-2 odd angular propagation speed.
cOmega2=sp.factor(
    1 - 12*M*ell**2*sp.tanh(x)/r**3
)


def main():
    # Core limits: x->+infty for M>0.
    assert sp.limit(sp.tanh(x),r,0,dir="+")==1

    f_over_r2=sp.simplify(
        sp.limit(f/r**2,r,0,dir="+")
    )
    X0=sp.simplify(
        sp.limit(X,r,0,dir="+")
    )
    R0=sp.simplify(
        sp.limit(R,r,0,dir="+")
    )
    K0=sp.simplify(
        sp.limit(K,r,0,dir="+")
    )

    assert sp.simplify(f_over_r2 + 1/ell**2)==0
    assert sp.simplify(X0 - 1/(2*ell**2))==0
    assert sp.simplify(R0 - 12/ell**2)==0
    assert sp.simplify(K0 - 24/ell**4)==0

    # Odd angular speed becomes negative and divergent.
    core_scaled=sp.simplify(
        sp.limit(r**3*cOmega2,r,0,dir="+")
    )
    assert sp.simplify(
        core_scaled + 12*M*ell**2
    )==0
    assert sp.limit(cOmega2,r,0,dir="+")==-sp.oo

    # Horizon is x=0.
    rh=(2*M*L**2)**sp.Rational(1,3)
    assert sp.simplify(x.subs(r,rh))==0
    assert sp.simplify(f.subs(r,rh))==0
    assert sp.simplify(X.subs(r,rh))==0

    # Scalar derivative diverges while scalar kinetic invariant stays finite.
    phiprime=1/r
    assert sp.limit(phiprime,r,0,dir="+")==sp.oo

    print("== Regularized-Lovelock planar Model 2 ==")
    print(f"x(r) = {x}")
    print(f"f(r) = {f}")
    print("phi'(r) = 1/r")
    print(f"X(r) = {X}")
    print()
    print("== Core limits ==")
    print(f"f/r^2 -> {f_over_r2}")
    print(f"X -> {X0}")
    print(f"R -> {R0}")
    print(f"K -> {K0}")
    print("phi' -> +infinity while X remains finite.")
    print()
    print("== Horizon ==")
    print(f"r_h = {rh}")
    print("x(r_h)=0, f(r_h)=0, X(r_h)=0")
    print()
    print("== Published odd-parity principal diagnostic ==")
    print(f"c_Omega^2 = {cOmega2}")
    print(f"r^3 c_Omega^2 -> {core_scaled}")
    print("c_Omega^2 -> -infinity at the regular core.")
    print()
    print(
        "Background metric/scalar invariants can be finite while a physical "
        "perturbation characteristic is violently unstable."
    )
    print(
        "The literature additionally finds det(K)=det(G)=0 for the "
        "even-parity scalar-containing mode on phi'=1/r."
    )
    print("All symbolic background/odd-speed assertions passed.")


if __name__=="__main__":
    main()
