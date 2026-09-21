#!/usr/bin/env python3
"""Weyl-ratio degeneracy of the representative 4D QTG lift on Hayward.

The representative covariant density
    H = -I_R/6 + I_C3/I_C2
uses a ratio of Weyl invariants.

On warped products,
    I_C2 = Omega^2/3,
    I_C3 = Omega^3/18,
so I_C3/I_C2 = Omega/6 when Omega != 0.

The reduced value is smooth through Omega=0, but the literal 4D invariant
gradient is singular:
    dH/dI_C3 = 1/I_C2 = 3/Omega^2,
    dH/dI_C2 = -I_C3/I_C2^2 = -1/(2 Omega).

For Hayward, Omega vanishes:
- at r=0,
- at r^3=4 M ell^2,
- asymptotically as r->infinity.

Thus the displayed rational lift encounters additional differentiability
problems even apart from the branch-wide P/K 0/0 surface.
"""

from __future__ import annotations

import sympy as sp


r,M,ell=sp.symbols(
    "r M ell", positive=True, finite=True
)

D=r**3+2*M*ell**2
f=sp.factor(1-2*M*r**2/D)

psi=sp.factor((1-f)/r**2)
eta=sp.factor(sp.diff(f,r)/r)
R2D=sp.factor(-sp.diff(f,r,2))

Omega=sp.factor(
    R2D+2*eta+2*psi
)

IC2=sp.factor(Omega**2/3)
IC3=sp.factor(Omega**3/18)

ratio=sp.cancel(IC3/IC2)

dH_dC3=sp.factor(1/IC2)
dH_dC2=sp.factor(-IC3/IC2**2)


def main():
    expected_Omega=sp.factor(
        12*M*r**3*(r**3-4*M*ell**2)/D**3
    )
    assert sp.simplify(Omega-expected_Omega)==0

    assert sp.simplify(ratio-Omega/6)==0
    assert sp.simplify(dH_dC3-3/Omega**2)==0
    assert sp.simplify(dH_dC2+1/(2*Omega))==0

    rw=(4*M*ell**2)**sp.Rational(1,3)

    assert sp.limit(Omega,r,0)==0
    assert sp.simplify(Omega.subs(r,rw))==0
    assert sp.limit(Omega,r,sp.oo)==0

    # Reduced ratio has a finite removable value at all zeros.
    assert sp.limit(ratio,r,0)==0
    assert sp.simplify(ratio.subs(r,rw))==0
    assert sp.limit(ratio,r,sp.oo)==0

    # Leading center scaling.
    center_Omega=sp.simplify(
        sp.limit(Omega/r**3,r,0)
    )
    assert sp.simplify(
        center_Omega+6/(M*ell**4)
    )==0

    # At infinity Omega ~ 12 M/r^3.
    inf_Omega=sp.simplify(
        sp.limit(r**3*Omega,r,sp.oo)
    )
    assert sp.simplify(inf_Omega-12*M)==0

    print("== Hayward Weyl variable ==")
    print(f"Omega(r) = {Omega}")
    print()
    print("Zeros:")
    print("r = 0")
    print(f"r_W = {rw}")
    print("Omega -> 0 as r -> infinity")
    print()
    print("== Reduced ratio ==")
    print(f"I_C3/I_C2 = {ratio}")
    print("This has a removable value Omega/6.")
    print()
    print("== Literal 4D invariant gradients ==")
    print(f"dH/dI_C3 = {dH_dC3}")
    print(f"dH/dI_C2 = {dH_dC2}")
    print("They diverge when Omega -> 0.")
    print()
    print(f"Omega/r^3 -> {center_Omega} at the center")
    print(f"r^3 Omega -> {inf_Omega} at infinity")
    print()
    print(
        "Conclusion: the representative Weyl-ratio lift is value-regular "
        "after spherical cancellation but not differentiable at Weyl-zero "
        "surfaces without an additional extension prescription."
    )
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
