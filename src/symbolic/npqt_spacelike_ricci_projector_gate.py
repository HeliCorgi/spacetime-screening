#!/usr/bin/env python3
"""Recover the signed spherical Ricci mode from the spacelike eigenplane.

Ferrando--Saez (2017) give an algebraic Ricci concomitant for a symmetric
tensor with a strict two-eigenplane:

    P = N^2 + 2 nu N + (3 nu^2 - b/2) I,
    h = 2 P / tr(P),

where N is traceless Ricci, b=tr(N^2), and for the two-double-eigenvalue
Segre type [(1,1)(11)]

    nu = +/- sqrt(b)/2.

The correct branch is the one for which h is a spacelike rank-two projector.

On the aligned NPQT stratum

    N = diag(-theta,-theta,+theta,+theta)

in a Lorentz orthonormal frame.  This script verifies:

- b=4 theta^2;
- the two algebraic roots are +/- |theta|;
- the spacelike condition selects nu=theta (the signed angular eigenvalue);
- h=diag(0,0,1,1);
- (1/2) tr(h N)=theta;
- therefore W2*(1/2)tr(hN)=W2*theta.

This is a constructive escape from the scalar-invariant sign blindness on the
exact spherical Segre stratum.

It is NOT yet a viable 4D action:
- a strict two-eigenplane is not stable under generic nonspherical Ricci
  perturbations;
- h becomes undefined when theta=0 if Ricci is used alone;
- an open-neighborhood extension and C2 gate remain necessary.
"""

from __future__ import annotations

import sympy as sp

theta, q = sp.symbols("theta q", real=True, nonzero=True)

# Mixed traceless Ricci endomorphism in Lorentz orthonormal frame.
N = sp.diag(-theta,-theta,theta,theta)
I4 = sp.eye(4)
b = sp.factor(sp.trace(N**2))
d = sp.factor(sp.trace(N**4))

assert b == 4*theta**2
assert d == 4*theta**4
assert sp.simplify(b**2-4*d) == 0

# Work branch-by-branch with the physically signed choices.
def projector(nu):
    P = sp.simplify(
        N**2 + 2*nu*N + (3*nu**2-b/2)*I4
    )
    trP = sp.factor(sp.trace(P))
    h = sp.simplify(2*P/trP)
    return P,trP,h

P_plus,trP_plus,h_plus = projector(theta)
P_minus,trP_minus,h_minus = projector(-theta)

h_ang = sp.diag(0,0,1,1)
h_base = sp.diag(1,1,0,0)

assert sp.simplify(h_plus-h_ang) == sp.zeros(4)
assert sp.simplify(h_minus-h_base) == sp.zeros(4)

assert sp.simplify(h_plus**2-h_plus) == sp.zeros(4)
assert sp.simplify(h_minus**2-h_minus) == sp.zeros(4)
assert sp.trace(h_plus) == 2
assert sp.trace(h_minus) == 2

# Signature test: angular projector has no component on an arbitrary timelike
# basis vector e0, while the complementary branch contains the timelike line.
e0 = sp.Matrix([1,0,0,0])
eta = sp.diag(-1,1,1,1)

# Covariant projector form for testing h(x,x).
hplus_cov = eta*h_plus
hminus_cov = eta*h_minus
assert (e0.T*hplus_cov*e0)[0] == 0
assert (e0.T*hminus_cov*e0)[0] == -1

Theta_recovered = sp.factor(sp.trace(h_plus*N)/2)
wrong_branch = sp.factor(sp.trace(h_minus*N)/2)

assert Theta_recovered == theta
assert wrong_branch == -theta

W2 = 48*q**2
T = sp.factor(W2*Theta_recovered)
assert T == 48*q**2*theta

def main() -> None:
    print("== NPQT spacelike Ricci-projector sign gate ==")
    print(f"b = tr(N^2) = {b}")
    print("two algebraic nu branches: +theta and -theta")
    print()
    print(f"h(nu=+theta) = {h_plus}")
    print(f"h(nu=-theta) = {h_minus}")
    print()
    print("The +theta branch is the spacelike angular two-plane;")
    print("the other branch contains the timelike direction.")
    print(f"Theta_recovered = {Theta_recovered}")
    print(f"W2 Theta = {T}")
    print()
    print("Conclusion: causal eigenspace data recovers the sign that SPIs lose.")
    print("The remaining problem is a single-valued generic off-spherical")
    print("extension with controlled C2 behavior.")
    print("All spacelike-projector assertions passed.")

if __name__=="__main__":
    main()
