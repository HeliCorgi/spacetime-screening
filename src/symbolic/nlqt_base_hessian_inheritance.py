#!/usr/bin/env python3
"""Inheritance of base-action Hessian singularities by the NLQT operator.

For a local QT base Lagrangian L(g,Riemann), define

    P^{abcd} = dL/dR_{abcd},

    Ehat_ab = P_{acde} R_b{}^{cde} - 1/2 L g_ab.

The NLQT form factor is built from the linearized operator

    delta Ehat_ab = Dhat_ab{}^{cd} h_cd.

At principal order,

    delta P = H . delta R,

where
    H = d^2 L / dRiemann dRiemann

is the curvature Hessian of the base action.

Therefore the principal coefficient of Dhat contains schematically

    (P + R . H) . delta R[h].

If H is divergent/undefined on the background, Dhat is generically divergent/
undefined unless a separate tensorial cancellation is proven.

The nonlocal entire function exp(Omega(Dhat)) cannot repair an operator that
is not defined before the form factor is applied.

This is a structural inheritance statement, not a claim that every singular
component of H necessarily survives every symmetry projection.
"""

from __future__ import annotations
import sympy as sp

P,H,Rbg=sp.symbols("P H Rbar", finite=True)
dR=sp.symbols("deltaR", finite=True)

# Scalar analogue of the tensor principal coefficient.
dP=H*dR
dEhat=sp.expand(dP*Rbg + P*dR)
principal_coeff=sp.factor(sp.diff(dEhat,dR))

assert sp.simplify(principal_coeff-(P+Rbg*H))==0

# Regulated singular base Hessian H=h_-1/delta + ...
delta,hminus1,P0,R0=sp.symbols(
    "delta h_-1 P0 R0", nonzero=True, finite=True
)
Hreg=hminus1/delta
coeff_reg=sp.factor(P0+R0*Hreg)

# Generic divergence coefficient.
lead=sp.simplify(sp.limit(delta*coeff_reg,delta,0))
assert sp.simplify(lead-R0*hminus1)==0

# Only a special contraction R0*hminus1=0 could remove it.
# Keep this explicit rather than silently assuming cancellation.

def main():
    print("== NLQT base-Hessian inheritance gate ==")
    print("delta P = H delta R")
    print(f"delta Ehat_pr = ({principal_coeff}) delta R")
    print()
    print("With H ~ h_-1/delta:")
    print(f"principal coefficient = {coeff_reg}")
    print(f"delta * coefficient -> {lead}")
    print()
    print("Thus a divergent/undefined base curvature Hessian is inherited")
    print("by Dhat unless a separate tensorial contraction cancels it.")
    print("The entire form factor acts only after Dhat is defined.")
    print()
    print("All base-Hessian inheritance assertions passed.")

if __name__=="__main__":
    main()
