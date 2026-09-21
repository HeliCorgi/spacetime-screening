#!/usr/bin/env python3
"""All-degree algebraic SPI sign gate on the aligned NPQT stratum.

Published input (Zakhary--McIntosh classification, as quoted in later
regular-black-hole invariant analyses):

For a four-dimensional Petrov-D spacetime with Segre type [(1,1)(11)], an
algebraically complete set of curvature invariants without curvature
derivatives is

    {R, I, I6, K},

with
    I6 = (1/12) S^a_b S^b_a,
    I  = (1/24) Cbar_abcd Cbar^abcd,
    K  = (1/4) Cbar_agdb S^gd S^ab,

where Cbar=(C+i *C)/2 in the convention used here.

This script evaluates that complete set on the aligned spherical/type-D
algebraic curvature family

    electric Weyl eigenvalues (-2q,q,q),
    S^a_b = diag(-theta,-theta,theta,theta).

It finds
    I  = q^2,
    I6 = theta^2/3,
    K  = -2 q theta^2,

while R is independent of the sign of theta.

Thus the complete algebraic scalar data are identical under theta -> -theta,
whereas the NPQT spherical target

    W2 theta = 48 q^2 theta

changes sign.

Conditional on the published completeness classification, no single-valued
function of algebraic scalar Riemann invariants can reproduce W2*theta on
both sign branches at this stratum.

Scope:
- no curvature derivatives are included;
- no Cartan/frame invariants are included;
- branch-restricted or explicitly multivalued/root prescriptions are not
  ruled out;
- this is an obstruction to a globally single-valued SPI-only lift.
"""

from __future__ import annotations

import itertools
import sympy as sp

eta = sp.diag(-1, 1, 1, 1)
q, theta, R = sp.symbols("q theta R", real=True)

E = sp.diag(-2*q, q, q)

def eps3(i: int, j: int, k: int) -> sp.Expr:
    return sp.LeviCivita(i-1, j-1, k-1)

C = sp.MutableDenseNDimArray.zeros(4,4,4,4)
for i in range(1,4):
    for j in range(1,4):
        v = E[i-1,j-1]
        C[0,i,0,j] = v
        C[i,0,0,j] = -v
        C[0,i,j,0] = -v
        C[i,0,j,0] = v

for i,j,k,l in itertools.product(range(1,4), repeat=4):
    C[i,j,k,l] = sp.simplify(sum(
        -eps3(i,j,m)*eps3(k,l,n)*E[m-1,n-1]
        for m,n in itertools.product(range(1,4), repeat=2)
    ))

def eps_ab_upmn(a,b,m,n):
    return sp.simplify(sum(
        sp.LeviCivita(a,b,p,r)*eta[p,m]*eta[r,n]
        for p,r in itertools.product(range(4), repeat=2)
    ))

Star = sp.MutableDenseNDimArray.zeros(4,4,4,4)
for a,b,c,d in itertools.product(range(4), repeat=4):
    Star[a,b,c,d] = sp.simplify(sp.Rational(1,2)*sum(
        eps_ab_upmn(a,b,m,n)*C[m,n,c,d]
        for m,n in itertools.product(range(4), repeat=2)
    ))

Cbar = sp.MutableDenseNDimArray.zeros(4,4,4,4)
for idx in itertools.product(range(4), repeat=4):
    Cbar[idx] = sp.simplify((C[idx] + sp.I*Star[idx])/2)

def raise4(T,a,b,c,d):
    return sp.simplify(sum(
        eta[a,A]*eta[b,B]*eta[c,Cc]*eta[d,D]*T[A,B,Cc,D]
        for A,B,Cc,D in itertools.product(range(4), repeat=4)
    ))

S_mix = sp.diag(-theta,-theta,theta,theta)
S_cov = eta*S_mix
S_up = eta*S_cov*eta

# Eigenstructure: two -theta eigenvectors (one timelike, one spacelike) and
# two +theta spacelike eigenvectors, matching the Segre [(1,1)(11)] stratum
# for theta != 0.
lam = sp.symbols("lambda")
charpoly = sp.factor(S_mix.charpoly(lam).as_expr())
assert charpoly == (lam-theta)**2*(lam+theta)**2

I6 = sp.factor(sp.trace(S_mix**2)/12)

Iinv = sp.factor(sp.Rational(1,24)*sum(
    Cbar[a,b,c,d]*raise4(Cbar,a,b,c,d)
    for a,b,c,d in itertools.product(range(4), repeat=4)
))

K = sp.factor(sp.Rational(1,4)*sum(
    Cbar[a,g,d,b]*S_up[g,d]*S_up[a,b]
    for a,g,d,b in itertools.product(range(4), repeat=4)
))

W2 = sp.factor(sum(
    C[a,b,c,d]*raise4(C,a,b,c,d)
    for a,b,c,d in itertools.product(range(4), repeat=4)
))
target = sp.factor(W2*theta)

assert Iinv == q**2
assert I6 == theta**2/3
assert K == -2*q*theta**2
assert W2 == 48*q**2
assert target == 48*q**2*theta

complete_set = (R, Iinv, I6, K)
for value in complete_set:
    assert sp.simplify(value.subs(theta,-theta)-value) == 0

assert sp.simplify(target.subs(theta,-theta)+target) == 0

def main() -> None:
    print("== NPQT aligned all-degree algebraic SPI sign gate ==")
    print(f"char(S) = {charpoly}")
    print(f"I  = {Iinv}")
    print(f"I6 = {I6}")
    print(f"K  = {K}")
    print("R is unchanged by theta -> -theta.")
    print()
    print(f"W2 = {W2}")
    print(f"target W2*theta = {target}")
    print()
    print("The algebraically complete Petrov-D / Segre [(1,1)(11)]")
    print("scalar set is even in theta, while the NPQT target is odd.")
    print("Conditional on the published Zakhary--McIntosh completeness")
    print("classification, a single-valued algebraic SPI-only lift cannot")
    print("represent both theta-sign branches.")
    print("All all-degree sign-gate assertions passed.")

if __name__ == "__main__":
    main()
