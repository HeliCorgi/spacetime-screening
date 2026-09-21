#!/usr/bin/env python3
"""Auxiliary derivative-mixing Schur-complement lemma.

Consider the quadratic principal kinetic Lagrangian

    L = 1/2 xdot^T A xdot
        + xdot^T B ydot
        + 1/2 ydot^T C ydot,

where:
- A is the healthy kinetic matrix of an already-normalized sector;
- y denotes another set of perturbations;
- C is their direct kinetic matrix;
- B is derivative mixing.

If A is invertible, completing the square gives

    L = 1/2 (xdot + A^-1 B ydot)^T
              A
              (xdot + A^-1 B ydot)
        + 1/2 ydot^T
              (C - B^T A^-1 B)
              ydot.

Thus the reduced kinetic matrix is the Schur complement

    K_red = C - B^T A^-1 B.

In particular, if C=0 and A is positive definite,

    K_red = -B^T A^-1 B <= 0.

Every derivative-active direction in Im(B^T) therefore has negative
quadratic kinetic sign unless it is removed by an independent constraint /
gauge degeneracy.

This is elementary linear algebra, not a novelty theorem.  It is recorded as
a reusable principal-safety diagnostic.
"""

from __future__ import annotations

import sympy as sp


# A symbolic 2x2 positive diagonal healthy block and a general 2x2 mixing.
a1,a2=sp.symbols("a1 a2", positive=True, finite=True)
b11,b12,b21,b22=sp.symbols(
    "b11 b12 b21 b22", real=True
)
c11,c12,c22=sp.symbols(
    "c11 c12 c22", real=True
)

A=sp.diag(a1,a2)
B=sp.Matrix([
    [b11,b12],
    [b21,b22],
])
C=sp.Matrix([
    [c11,c12],
    [c12,c22],
])

Ainv=A.inv()
Kred=sp.simplify(C-B.T*Ainv*B)

# Auxiliary/no-direct-kinetic case.
Kaux=sp.simplify(Kred.subs({
    c11:0,c12:0,c22:0
}))

# For arbitrary vector y, y^T Kaux y = -(B y)^T A^-1 (B y).
y1,y2=sp.symbols("y1 y2", real=True)
y=sp.Matrix([y1,y2])

quad=sp.factor((y.T*Kaux*y)[0])
negative_norm=sp.factor(
    -(B*y).T*Ainv*(B*y)
)
assert sp.simplify(
    quad-negative_norm[0]
)==0

# Scalar healthy sector + N=2 auxiliary sector reproduces the rank-one
# structure used by the two-vector black-hole benchmark.
A0=sp.symbols("A0", positive=True)
p,q=sp.symbols("p q", real=True)
B1=sp.Matrix([[p,q]])
Krank1=sp.simplify(
    -B1.T*sp.Matrix([[1/A0]])*B1
)
expected_rank1=sp.Matrix([
    [-p**2/A0,-p*q/A0],
    [-p*q/A0,-q**2/A0],
])
assert sp.simplify(Krank1-expected_rank1)==sp.zeros(2)
assert sp.factor(Krank1.det())==0
assert sp.factor(sp.trace(Krank1)+(p**2+q**2)/A0)==0

# If a direct kinetic matrix C=lambda I is present, positivity requires it
# to dominate the mixing Schur term.  Along any y:
# y^T C y > (B y)^T A^-1(B y).
lam=sp.symbols("lambda_direct", positive=True)
Kwith=sp.simplify(
    lam*sp.eye(2)-B.T*Ainv*B
)


def main():
    print("== Auxiliary derivative-mixing lemma ==")
    print("A =")
    print(A)
    print("B =")
    print(B)
    print()
    print("K_red = C - B^T A^-1 B =")
    print(Kred)
    print()
    print("For C=0:")
    print(Kaux)
    print()
    print("For arbitrary y:")
    print("y^T K_aux y =")
    print(quad)
    print("= -(B y)^T A^-1 (B y) <= 0")
    print()
    print("== One healthy mode + two auxiliary modes ==")
    print(Krank1)
    print("det =",sp.factor(Krank1.det()))
    print("trace =",sp.factor(sp.trace(Krank1)))
    print()
    print(
        "Any nonzero derivative mixing produces a negative active direction "
        "when the auxiliary sector has no direct kinetic term, unless an "
        "independent constraint removes that direction."
    )
    print()
    print("With direct kinetic lambda I:")
    print(Kwith)
    print(
        "principal safety requires the direct kinetic matrix to dominate "
        "B^T A^-1 B in the positive-definite matrix ordering."
    )
    print("All Schur-complement assertions passed.")


if __name__=="__main__":
    main()
