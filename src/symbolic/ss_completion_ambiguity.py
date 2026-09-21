#!/usr/bin/env python3
"""Spherical-background completion ambiguity for nonspherical perturbations.

A static spherically symmetric parity-even background has vanishing
gravitational Pontryagin pseudoscalar

    P = *R R.

Consider adding to any 4D action

    Delta L = lambda P^2.

On a background with P_bar=0:
- Delta L_bar = 0;
- the first variation vanishes identically;
- therefore the background equations/solution are unchanged.

But the quadratic action changes by

    Delta L^(2) = lambda (delta P)^2

(up to the conventional 1/2 definition of S^(2)).

Odd/axial metric perturbations generically induce a nonzero magnetic Weyl
tensor and therefore nonzero delta P.  Thus two actions can have the same
spherical background and spherical response h(psi), while having different
odd quadratic/principal operators.

This is an underdetermination result: generic nonspherical zero-kernel,
kinetic sign, and characteristic structure cannot be inferred from the
spherical black-hole solution alone.
"""

from __future__ import annotations
import sympy as sp

eps, lam = sp.symbols("epsilon lambda", real=True)
P1, P2 = sp.symbols("P1 P2", real=True)

# Background Pontryagin scalar vanishes, so perturbatively
# P(eps)=eps P1 + eps^2 P2/2 + ...
P = eps*P1 + eps**2*P2/2

DeltaL = sp.expand(lam*P**2)

L0 = sp.expand(DeltaL).coeff(eps, 0)
L1 = sp.expand(DeltaL).coeff(eps, 1)
L2coeff = sp.expand(DeltaL).coeff(eps, 2)

assert L0 == 0
assert L1 == 0
assert sp.simplify(L2coeff - lam*P1**2) == 0

# Electric/magnetic Weyl diagnostic:
# Pontryagin is proportional to E_ij B^ij (convention-dependent overall
# factor).  A spherical parity-even background has B_bar=0, while an axial
# perturbation can generate delta B != 0.
e, b = sp.symbols("e b", real=True)

Ebar = sp.diag(-2*e, e, e)       # tracefree type-D electric Weyl pattern
dB   = sp.diag( 2*b,-b,-b)       # tracefree magnetic perturbation example

contraction = sp.factor(
    sum(Ebar[i,j]*dB[i,j] for i in range(3) for j in range(3))
)
assert sp.simplify(contraction + 6*e*b) == 0

# Therefore an odd perturbation direction exists with delta P !=0 whenever
# the background Weyl curvature e and magnetic perturbation b are nonzero.

# Quadratic Hessian in the perturbative Pontryagin amplitude.
hess = sp.diff(lam*P1**2, P1, 2)
assert sp.simplify(hess - 2*lam) == 0

def main():
    print("== Spherical-completion ambiguity ==")
    print(f"Delta L = lambda P^2 = {DeltaL}")
    print(f"background term = {L0}")
    print(f"first-order term = {L1}")
    print(f"quadratic coefficient = {L2coeff}")
    print()
    print("Thus the background and its equations are unchanged,")
    print("while the nonspherical quadratic action is shifted.")
    print()
    print("Electric/magnetic Weyl example:")
    print(f"Ebar_ij dB^ij = {contraction}")
    print("which is generically nonzero for an axial/magnetic perturbation.")
    print()
    print(f"quadratic Hessian with respect to delta P amplitude = {hess}")
    print()
    print("Conclusion: the spherical response h(psi) does not uniquely fix")
    print("the generic odd quadratic/principal operator in 4D.")
    print("All completion-ambiguity assertions passed.")

if __name__=="__main__":
    main()
