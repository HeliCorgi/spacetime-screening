#!/usr/bin/env python3
"""Locally symmetric product realization of the aligned NPQT sign pair.

Consider the four-dimensional direct product

    M_2(k_L) x S^2(k_S),

where the first factor is two-dimensional Lorentzian constant curvature and
the second is a positive-curvature two-sphere.

Set

    k_L = 3 q - theta,
    k_S = 3 q + theta.

Then the four-dimensional scalar curvature is R=12q and the mixed traceless
Ricci tensor has eigenvalues

    (-theta,-theta,+theta,+theta).

The Weyl tensor is purely electric with eigenvalues

    (-2q,q,q),

independent of theta.

Thus theta -> -theta exchanges the curvatures of the Lorentzian and spherical
two-planes while leaving q fixed.  The two metrics have the same algebraic
scalar invariant data used in the NPQT sign gate, but the source spherical
target W2*theta changes sign.

Because each factor is constant curvature, the direct product is locally
symmetric:

    nabla_e R_abcd = 0.

Hence every scalar invariant containing at least one covariant derivative of
the Riemann tensor vanishes on both members of the pair.  Derivative
invariants therefore do not recover the missing sign on this test family.

The local-symmetry statement is a standard geometric fact about products of
locally symmetric spaces; this script verifies the algebraic curvature
relations at a point.
"""

from __future__ import annotations

import itertools
import sympy as sp

eta = sp.diag(-1,1,1,1)
q, theta = sp.symbols("q theta", real=True)

kL = 3*q-theta
kS = 3*q+theta

Riem = sp.MutableDenseNDimArray.zeros(4,4,4,4)
for a,b,c,d in itertools.product(range(4),repeat=4):
    if all(x in (0,1) for x in (a,b,c,d)):
        Riem[a,b,c,d] = sp.simplify(
            kL*(eta[a,c]*eta[b,d]-eta[a,d]*eta[b,c])
        )
    elif all(x in (2,3) for x in (a,b,c,d)):
        Riem[a,b,c,d] = sp.simplify(
            kS*(eta[a,c]*eta[b,d]-eta[a,d]*eta[b,c])
        )

Ric = sp.Matrix(
    4,4,
    lambda b,d: sp.simplify(sum(
        eta[a,c]*Riem[a,b,c,d]
        for a,c in itertools.product(range(4),repeat=2)
    ))
)
R4 = sp.factor(sum(
    eta[a,b]*Ric[a,b]
    for a,b in itertools.product(range(4),repeat=2)
))
Ricmix = sp.simplify(eta*Ric)
Zmix = sp.simplify(Ricmix - R4*sp.eye(4)/4)

assert R4 == 12*q
assert Ricmix == sp.diag(kL,kL,kS,kS)
assert Zmix == sp.diag(-theta,-theta,theta,theta)

C = sp.MutableDenseNDimArray.zeros(4,4,4,4)
for a,b,c,d in itertools.product(range(4),repeat=4):
    C[a,b,c,d] = sp.simplify(
        Riem[a,b,c,d]
        - sp.Rational(1,2)*(
            eta[a,c]*Ric[d,b]
            - eta[a,d]*Ric[c,b]
            - eta[b,c]*Ric[d,a]
            + eta[b,d]*Ric[c,a]
        )
        + R4/sp.Integer(6)*(
            eta[a,c]*eta[d,b]-eta[a,d]*eta[c,b]
        )
    )

E = sp.Matrix(3,3,lambda i,j: sp.simplify(C[0,i+1,0,j+1]))
assert E == sp.diag(-2*q,q,q)

def raise4(T,a,b,c,d):
    return sp.simplify(sum(
        eta[a,A]*eta[b,B]*eta[c,Cc]*eta[d,D]*T[A,B,Cc,D]
        for A,B,Cc,D in itertools.product(range(4),repeat=4)
    ))

W2 = sp.factor(sum(
    C[a,b,c,d]*raise4(C,a,b,c,d)
    for a,b,c,d in itertools.product(range(4),repeat=4)
))
Z2 = sp.factor(sp.trace(Zmix**2))
Z3 = sp.factor(sp.trace(Zmix**3))

assert W2 == 48*q**2
assert Z2 == 4*theta**2
assert Z3 == 0

target = sp.factor(W2*theta)
target_flip = sp.factor(target.subs(theta,-theta))
assert target_flip == -target

# Spherical reduction variables for a constant-radius product:
# psi=k_S, R_2d=2 k_L, Box(phi)=0.
psi = kS
R2 = 2*kL
B = sp.Integer(0)
Omega = sp.factor(2*psi/3 + R2/3 + 2*B/3)
Theta_source = sp.factor(psi/2 - R2/4)

assert Omega == 4*q
assert Theta_source == theta
assert sp.simplify(3*Omega**2-W2) == 0

def main() -> None:
    print("== NPQT locally symmetric product sign pair ==")
    print(f"k_L = {kL}")
    print(f"k_S = {kS}")
    print(f"R4 = {R4}")
    print(f"Z^a_b = {Zmix}")
    print(f"electric Weyl = {E}")
    print(f"W2 = {W2}")
    print(f"Omega = {Omega}")
    print(f"Theta(source) = {Theta_source}")
    print()
    print(f"target(+theta) = {target}")
    print(f"target(-theta) = {target_flip}")
    print()
    print("theta -> -theta exchanges k_L and k_S while the algebraic scalar")
    print("invariant data remain sign blind.  Since the product is locally")
    print("symmetric, all invariants containing covariant curvature")
    print("derivatives vanish on both members of the pair.")
    print("All product-pair algebraic assertions passed.")

if __name__=="__main__":
    main()
