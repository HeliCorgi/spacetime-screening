#!/usr/bin/env python3
"""Local off-spherical Ricci spectral-cluster extension for the NPQT target.

Take a Lorentz-self-adjoint traceless-Ricci endomorphism with eigenvalues

    base cluster:   -theta + a, -theta - a
    angular cluster: theta + d, theta - d.

The spherical aligned point is a=d=0.

As long as the two clusters do not collide, the rank-two projector onto the
angular cluster is a cubic polynomial in N,

    h = p(N),

where p vanishes on the two base eigenvalues and equals one on the two angular
eigenvalues.

The unique interpolation polynomial has denominator

    Delta_gap =
      (a-d-2theta)(a-d+2theta)
      (a+d-2theta)(a+d+2theta),

i.e. the product of the four cross-cluster eigenvalue gaps.

Therefore h is analytic under generic eigenvalue splitting while the two
clusters remain separated.  Moreover

    (1/2) tr(h N) = theta,

so W2*(1/2)tr(hN) reproduces the signed spherical target and its natural local
off-spherical cluster-average extension.

A Lorentz similarity transformation (boost) is included explicitly to verify
that the construction is covariant under changes of the spectral frame.

Scope:
- this is a local spectral-cluster construction, not a globally defined 4D
  Lagrangian;
- the gap closes at cluster-collision strata, including the Ricci-isotropic
  core;
- the Weyl sector may be needed to bridge those strata.
"""

from __future__ import annotations

import sympy as sp

theta, a, d, u, q = sp.symbols("theta a d u q", real=True)

lam1 = -theta + a
lam2 = -theta - a
mu1 = theta + d
mu2 = theta - d

gap = sp.factor(
    (a-d-2*theta)*(a-d+2*theta)
    *(a+d-2*theta)*(a+d+2*theta)
)

c0 = sp.factor(
    (a**4-a**2*d**2-9*a**2*theta**2+d**2*theta**2+8*theta**4)/gap
)
c1 = sp.factor(2*theta*(a**2+d**2+6*theta**2)/gap)
c2 = sp.factor((-a**2+d**2)/gap)
c3 = sp.factor(-4*theta/gap)

x = sp.symbols("x")
p = sp.factor(c0+c1*x+c2*x**2+c3*x**3)

assert sp.simplify(p.subs(x,lam1)) == 0
assert sp.simplify(p.subs(x,lam2)) == 0
assert sp.simplify(p.subs(x,mu1)-1) == 0
assert sp.simplify(p.subs(x,mu2)-1) == 0

D = sp.diag(lam1,lam2,mu1,mu2)
I4 = sp.eye(4)

def poly(M):
    return sp.simplify(c0*I4+c1*M+c2*(M**2)+c3*(M**3))

hD = poly(D)
expected = sp.diag(0,0,1,1)
assert sp.simplify(hD-expected) == sp.zeros(4)
assert sp.simplify(hD**2-hD) == sp.zeros(4)
assert sp.trace(hD) == 2
assert sp.factor(sp.trace(hD*D)/2) == theta

# Lorentz boost mixing one base timelike direction with one angular spacelike
# direction.  Similarity preserves the Lorentz-self-adjoint spectral problem.
ch = sp.cosh(u)
sh = sp.sinh(u)
L = sp.Matrix([
    [ch,0,sh,0],
    [0,1,0,0],
    [sh,0,ch,0],
    [0,0,0,1],
])
eta = sp.diag(-1,1,1,1)
assert sp.simplify(L.T*eta*L-eta) == sp.zeros(4)

N = sp.simplify(L*D*L.inv())
hN = sp.simplify(poly(N))
h_expected = sp.simplify(L*expected*L.inv())

assert sp.simplify(hN-h_expected) == sp.zeros(4)
assert sp.simplify(hN**2-hN) == sp.zeros(4)
assert sp.simplify(sp.trace(hN)-2) == 0
assert sp.simplify(sp.trace(hN*N)/2-theta) == 0

# The target if W2 keeps its spherical normalization at the reference point.
W2 = 48*q**2
T = sp.factor(W2*sp.trace(hN*N)/2)
assert sp.simplify(T-48*q**2*theta) == 0

# At the aligned point a=d=0 the gap is nonzero for theta != 0.
gap_aligned = sp.factor(gap.subs({a:0,d:0}))
assert gap_aligned == 16*theta**4

def main() -> None:
    print("== NPQT local Ricci spectral-cluster extension ==")
    print(f"gap denominator = {gap}")
    print(f"aligned gap = {gap_aligned}")
    print()
    print(f"p(x) = {p}")
    print("p(base eigenvalues)=0, p(angular eigenvalues)=1.")
    print()
    print("After an explicit Lorentz boost:")
    print("h(N)=L diag(0,0,1,1) L^{-1}")
    print(f"(1/2) tr(hN) = {sp.simplify(sp.trace(hN*N)/2)}")
    print(f"W2*(1/2)tr(hN) = {T}")
    print()
    print("Conclusion: generic splitting inside the two clusters is not a")
    print("local obstruction while the inter-cluster spectral gap is open.")
    print("All Ricci-cluster assertions passed.")

if __name__=="__main__":
    main()
