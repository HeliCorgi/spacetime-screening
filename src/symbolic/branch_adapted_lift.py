#!/usr/bin/env python3
"""Branch-adapted square-root lift on the single-function Hayward branch.

The rational representative P is 0/0 on n=1 metrics.  One can instead use
the traceless-Ricci norm on the single-function branch:

    Sigma = I_Rhat2 = (R2D - 2 psi)^2 / 4.

Together with
    rho = I_R = R2D - 4 eta + 2 psi

this gives, on a branch of definite sign,

    psi = eta + rho/4 +/- sqrt(Sigma)/2.

For the Hayward solution R2D-2 psi < 0 for r>0, so the plus-square-root branch
recovers psi exactly.

The value is finite, but its derivative with respect to Sigma is
    dP/dSigma = 1/(4 sqrt(Sigma)),
which diverges whenever Sigma->0.  Hayward has Sigma->0 both at the de Sitter
center and asymptotically.

Thus this alternative removes the 0/0 value but not differentiability at the
symmetry-enhanced endpoints.
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
rho=sp.factor(R2D-4*eta+2*psi)

Sigma=sp.factor((R2D-2*psi)**2/4)
sqrtSigma=sp.factor(
    36*M**2*ell**2*r**3/D**3
)

Pplus=sp.factor(
    eta+rho/4+sqrtSigma/2
)

x=sp.factor(R2D-2*psi)


def main():
    expected_x=sp.factor(
        -72*M**2*ell**2*r**3/D**3
    )
    expected_Sigma=sp.factor(
        1296*M**4*ell**4*r**6/D**6
    )

    assert sp.simplify(x-expected_x)==0
    assert sp.simplify(Sigma-expected_Sigma)==0
    assert sp.simplify(sp.sqrt(expected_Sigma)-sqrtSigma)==0
    assert sp.simplify(Pplus-psi)==0

    # Generic derivative of the square-root branch.
    S=sp.symbols("Sigma", positive=True)
    dP_dS=sp.diff(sp.sqrt(S)/2,S)
    assert sp.simplify(
        dP_dS-1/(4*sp.sqrt(S))
    )==0

    dP_r=sp.factor(
        1/(4*sqrtSigma)
    )

    # Endpoint asymptotics.
    center_scaled=sp.simplify(
        sp.limit(r**3*dP_r,r,0)
    )
    infinity_scaled=sp.simplify(
        sp.limit(dP_r/r**6,r,sp.oo)
    )

    assert sp.simplify(
        center_scaled-M*ell**4/18
    )==0
    assert sp.simplify(
        infinity_scaled-1/(144*M**2*ell**2)
    )==0

    assert sp.limit(Sigma,r,0)==0
    assert sp.limit(Sigma,r,sp.oo)==0

    print("== Single-function branch identity ==")
    print(f"R2D - 2 psi = {x}")
    print(f"Sigma = {Sigma}")
    print()
    print("Hayward has R2D-2psi < 0 for finite r>0, so")
    print("P_sqrt = eta + I_R/4 + sqrt(I_Rhat2)/2")
    print(f"P_sqrt = {Pplus}")
    print(f"psi = {psi}")
    print()
    print("== Differentiability ==")
    print(f"dP_sqrt/dSigma = {dP_dS}")
    print(f"on Hayward = {dP_r}")
    print()
    print("Endpoint behavior:")
    print(f"Sigma(0) = {sp.limit(Sigma,r,0)}")
    print(f"Sigma(infinity) = {sp.limit(Sigma,r,sp.oo)}")
    print(
        "r^3 dP/dSigma -> "
        f"{center_scaled} at the center"
    )
    print(
        "(dP/dSigma)/r^6 -> "
        f"{infinity_scaled} at infinity"
    )
    print()
    print(
        "Conclusion: a square-root branch removes the 0/0 value but is "
        "not differentiable when the traceless Ricci tensor vanishes."
    )
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
