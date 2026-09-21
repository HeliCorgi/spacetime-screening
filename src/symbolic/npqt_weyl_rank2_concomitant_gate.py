#!/usr/bin/env python3
"""Low-degree Weyl rank-2 concomitant obstruction in four dimensions.

Four-dimensional dimensionally dependent identities imply

    C_{a c d e} C_b{}^{c d e}
      = (1/4) g_{ab} W2,

and the cubic chain analogue

    C_{a c}{}^{de} C_{de}{}^{fg} C_{fg}{}^{bc}
      = (1/4) delta_a^b W3.

Therefore quadratic and cubic polynomial rank-2 Weyl concomitants of these
natural chain forms carry no principal-plane information: they collapse to
the metric/identity.

In particular, contracting either with traceless Ricci cannot produce the
signed spherical angular mode required by W2*Theta.

This script verifies both identities on a generic purely-electric
four-dimensional Lorentzian algebraic Weyl family.
"""

from __future__ import annotations

import itertools
import sympy as sp

eta=sp.diag(-1,1,1,1)
e1,e2=sp.symbols("e1 e2",real=True)
E=sp.diag(e1,e2,-e1-e2)

def eps3(i,j,k):
    return sp.LeviCivita(i-1,j-1,k-1)

C=sp.MutableDenseNDimArray.zeros(4,4,4,4)
for i in range(1,4):
    for j in range(1,4):
        v=E[i-1,j-1]
        C[0,i,0,j]=v
        C[i,0,0,j]=-v
        C[0,i,j,0]=-v
        C[i,0,j,0]=v

for i,j,k,l in itertools.product(range(1,4),repeat=4):
    C[i,j,k,l]=sp.simplify(sum(
        -eps3(i,j,m)*eps3(k,l,n)*E[m-1,n-1]
        for m,n in itertools.product(range(1,4),repeat=2)
    ))

def Cup(a,b,c,d):
    return sp.simplify(sum(
        eta[c,e]*eta[d,f]*C[a,b,e,f]
        for e,f in itertools.product(range(4),repeat=2)
    ))

W2=sp.factor(sum(
    Cup(a,b,c,d)*Cup(c,d,a,b)
    for a,b,c,d in itertools.product(range(4),repeat=4)
))
W3=sp.factor(sum(
    Cup(a,b,c,d)*Cup(c,d,e,f)*Cup(e,f,a,b)
    for a,b,c,d,e,f in itertools.product(range(4),repeat=6)
))

Q2=sp.Matrix.zeros(4,4)
for a,b in itertools.product(range(4),repeat=2):
    # lower-lower form C_acde C_b^{cde}; compare with g_ab.
    val=0
    for c,d,e in itertools.product(range(4),repeat=3):
        Cbup=sum(
            eta[c,Cc]*eta[d,D]*eta[e,Ee]*C[b,Cc,D,Ee]
            for Cc,D,Ee in itertools.product(range(4),repeat=3)
        )
        val += C[a,c,d,e]*Cbup
    Q2[a,b]=sp.factor(val)

Q3=sp.Matrix.zeros(4,4)
for a,b in itertools.product(range(4),repeat=2):
    Q3[a,b]=sp.factor(sum(
        Cup(a,c,d,e)*Cup(d,e,f,g)*Cup(f,g,b,c)
        for c,d,e,f,g in itertools.product(range(4),repeat=5)
    ))

assert sp.simplify(Q2-eta*W2/4)==sp.zeros(4)
assert sp.simplify(Q3-sp.eye(4)*W3/4)==sp.zeros(4)

z0,z1,z2=sp.symbols("z0 z1 z2",real=True)
z3=-z0-z1-z2
Zmix=sp.diag(z0,z1,z2,z3)
assert sp.trace(Zmix)==0

# Contract the mixed cubic concomitant with Z^a_b.
linear3=sp.factor(sp.trace(Q3*Zmix))
assert linear3==0

def main():
    print("== NPQT low-degree Weyl rank-2 concomitant gate ==")
    print(f"W2 = {W2}")
    print(f"W3 = {W3}")
    print("Q2_ab = (W2/4) g_ab")
    print("Q3_a^b = (W3/4) delta_a^b")
    print(f"tr(Q3 Z) = {linear3}")
    print()
    print("Conclusion: low-degree polynomial Weyl rank-2 chains do not")
    print("carry principal-plane information in 4D. A signed angular-mode")
    print("lift therefore needs non-polynomial normalization/root data,")
    print("curvature derivatives, or additional structure.")
    print("All Weyl rank-2 assertions passed.")

if __name__=="__main__":
    main()
