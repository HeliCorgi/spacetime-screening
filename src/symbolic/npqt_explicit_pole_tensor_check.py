#!/usr/bin/env python3
"""Direct index-contraction validation of the explicit NPQT cubic pole.

The source cubic density is

 Z(3) = polynomial curvature terms
      + (9/2) * W3 * Z3 * W2 / D,

 D = (WZZ) W2 - 2 W3 Z2.

This script constructs the Lorentzian Weyl tensor explicitly in an orthonormal
frame, rather than assuming closed invariant formulas.

Take a purely-electric Weyl tensor with
    E = diag(1,5,-6),
and vanishing magnetic Weyl part.

Take mixed traceless Ricci
    Z^a_b = diag(z0,1,1,-z0-2),
    z0 = -1 + 8/sqrt(61).

We build C_abcd with
    C_0i0j=E_ij,
    C_ijkl=-eps_ijm eps_kln E_mn,
and compute every invariant by direct index contraction with
eta=diag(-1,1,1,1).

The result is
    W2=496,
    W3=1440,
    Z3=-384/61,
    D=0,
    W3 Z3 W2=-274268160/61 !=0.

Since all other terms in the published Z(3) are polynomial curvature
contractions, they are finite on this finite algebraic curvature tensor and
cannot cancel the rational pole.

This validates the explicit off-spherical singular direction at the tensor
index level.
"""

from __future__ import annotations
import itertools
import sympy as sp

eta=sp.diag(-1,1,1,1)

Evals=(sp.Integer(1),sp.Integer(5),sp.Integer(-6))
E=sp.diag(*Evals)

def eps3(i,j,k):
    # spatial indices i,j,k = 1,2,3
    return sp.LeviCivita(i-1,j-1,k-1)

C=sp.MutableDenseNDimArray.zeros(4,4,4,4)

# Purely electric components.
for i in range(1,4):
    for j in range(1,4):
        v=E[i-1,j-1]
        C[0,i,0,j]=v
        C[i,0,0,j]=-v
        C[0,i,j,0]=-v
        C[i,0,j,0]=v

for i,j,k,l in itertools.product(range(1,4),repeat=4):
    v=0
    for m,n in itertools.product(range(1,4),repeat=2):
        v += -eps3(i,j,m)*eps3(k,l,n)*E[m-1,n-1]
    C[i,j,k,l]=sp.simplify(v)

def C_ab_upup(a,b,c,d):
    return sp.simplify(
        sum(
            eta[c,e]*eta[d,f]*C[a,b,e,f]
            for e,f in itertools.product(range(4),repeat=2)
        )
    )

# Basic Weyl invariants.
W2=sp.factor(
    sum(
        C_ab_upup(a,b,c,d)*C_ab_upup(c,d,a,b)
        for a,b,c,d in itertools.product(range(4),repeat=4)
    )
)

W3=sp.factor(
    sum(
        C_ab_upup(a,b,c,d)
        *C_ab_upup(c,d,e,f)
        *C_ab_upup(e,f,a,b)
        for a,b,c,d,e,f in itertools.product(range(4),repeat=6)
    )
)

z0=sp.factor(-1+8*sp.sqrt(61)/61)
z=(z0,sp.Integer(1),sp.Integer(1),sp.factor(-z0-2))

Z2=sp.factor(sum(zi**2 for zi in z))
Z3=sp.factor(sum(zi**3 for zi in z))

# W_ab^{cd} Z_c^a Z_d^b for diagonal mixed Z.
WZZ=sp.factor(
    sum(
        C_ab_upup(a,b,c,d)
        *(z[a] if a==c else 0)
        *(z[b] if b==d else 0)
        for a,b,c,d in itertools.product(range(4),repeat=4)
    )
)

D=sp.factor(WZZ*W2-2*W3*Z2)
N=sp.factor(W3*Z3*W2)

assert W2==496
assert W3==1440
assert Z3==-sp.Rational(384,61)
assert D==0
assert N==-sp.Rational(274268160,61)
assert N!=0

# Basic algebraic Weyl checks.
# Trace C^a_{bad}=0 in all components.
for b,d in itertools.product(range(4),repeat=2):
    tr=0
    for a,c in itertools.product(range(4),repeat=2):
        # g^{ac} C_{a b c d}
        tr += eta[a,c]*C[a,b,c,d]
    assert sp.simplify(tr)==0

def main():
    print("== Direct tensor-contraction NPQT cubic pole check ==")
    print("signature eta=(-,+,+,+)")
    print(f"E eigenvalues = {Evals}")
    print(f"mixed traceless-Ricci eigenvalues = {z}")
    print()
    print(f"W2 = {W2}")
    print(f"W3 = {W3}")
    print(f"Z2 = {Z2}")
    print(f"Z3 = {Z3}")
    print(f"WZZ = {WZZ}")
    print(f"D = WZZ W2 - 2 W3 Z2 = {D}")
    print(f"N = W3 Z3 W2 = {N}")
    print()
    print("Published cubic rational term: (9/2) N/D.")
    print("D=0 and N!=0, while all polynomial pieces remain finite.")
    print("Therefore the displayed cubic density has a genuine pole here.")
    print("All direct index-contraction assertions passed.")

if __name__=="__main__":
    main()
