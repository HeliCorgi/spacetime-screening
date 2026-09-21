#!/usr/bin/env python3
"""Reduced high-frequency odd-vector principal matrices for the two-vector model.

The published generalized-Proca odd action gives, for one vector,
    q2 = C5 - C2^2/C1,
    R22 = -2 C2 C3/C1,
    G22 = C7 - C3^2/C1
(up to the common l-dependent factor).

For N odd vector perturbations u_i, the direct matrix generalization is
    K = C5_matrix - c2 c2^T/C1
    R = C6_matrix - (c2 c3^T + c3 c2^T)/C1
    G = C7_matrix - c3 c3^T/C1.

Our model contains no Maxwell/F^2 term, so the direct C5,C6,C7 matrices vanish.
On the null regular background h=f and A1=A0/f for each vector, one has
    c3 = -f c2.

Therefore
    K = -c c^T/C1,
    R = -2 f K,
    G = f^2 K,

and the nonzero vector combination has
    det_principal ~ (omega + f k)^2.

The orthogonal vector combination has zero principal quadratic operator.

The nonzero kinetic eigenvalue is negative outside the metric horizon,
providing a high-frequency odd-sector ghost warning.  This is stronger than
the earlier local-TT heuristic but still assumes that the direct multi-vector
extension of the published reduced odd action is valid; a full explicit
two-vector harmonic expansion remains the final publication-level check.
"""

from __future__ import annotations

import sympy as sp


C1,f,omega,k=sp.symbols(
    "C1 f omega k", positive=True, finite=True
)
cA,cB=sp.symbols("c_A c_B", real=True)

c=sp.Matrix([cA,cB])
d=-f*c

K=sp.simplify(-(c*c.T)/C1)
R=sp.simplify(-(c*d.T+d*c.T)/C1)
G=sp.simplify(-(d*d.T)/C1)

assert sp.simplify(R+2*f*K)==sp.zeros(2)
assert sp.simplify(G-f**2*K)==sp.zeros(2)

P=sp.simplify(
    omega**2*K - omega*k*R + k**2*G
)
assert sp.simplify(
    P-(omega+f*k)**2*K
)==sp.zeros(2)

traceK=sp.factor(sp.trace(K))
detK=sp.factor(K.det())
assert detK==0
assert sp.simplify(
    traceK+(cA**2+cB**2)/C1
)==0

# Eigenvector for the nonzero mode is c itself; orthogonal mode is (-cB,cA).
epar=c
eperp=sp.Matrix([-cB,cA])

assert sp.simplify(
    K*epar-traceK*epar
)==sp.zeros(2)
assert sp.simplify(K*eperp)==sp.zeros(2)

# Full kinetic Hessian in velocities (Xg_dot-like metric odd velocity, uA,uB)
# for L = C1 x^2 + 2(c.u_dot)x.
H=sp.Matrix([
    [2*C1,2*cA,2*cB],
    [2*cA,0,0],
    [2*cB,0,0],
])

# Characteristic polynomial of H.
lam=sp.symbols("lambda")
charH=sp.factor(H.charpoly(lam).as_expr())
expected_char=sp.factor(
    lam*(lam**2-2*C1*lam-4*(cA**2+cB**2))
)
assert sp.simplify(charH-expected_char)==0

# Two nonzero eigenvalues have opposite signs because their product is
# -4(cA^2+cB^2)<0.
disc=sp.factor(C1**2+4*(cA**2+cB**2))
lambda_plus=sp.factor(C1+sp.sqrt(disc))
lambda_minus=sp.factor(C1-sp.sqrt(disc))

assert sp.simplify(lambda_plus*lambda_minus+4*(cA**2+cB**2))==0


def main():
    print("== Reduced vector principal matrices ==")
    print("K =")
    print(K)
    print("R =")
    print(R)
    print("G =")
    print(G)
    print()
    print(f"tr(K) = {traceK}")
    print(f"det(K) = {detK}")
    print("nonzero-mode eigenvector ~ (c_A,c_B)")
    print("zero-principal eigenvector ~ (-c_B,c_A)")
    print()
    print("== Radial principal polynomial ==")
    print("P(omega,k) =")
    print(P)
    print("= (omega+f k)^2 K")
    print()
    print("The propagating principal vector combination has a double")
    print("background-null characteristic omega=-f k.")
    print()
    print("== Unreduced velocity Hessian ==")
    print(H)
    print(f"characteristic polynomial = {charH}")
    print(f"lambda_plus = {lambda_plus}")
    print(f"lambda_minus = {lambda_minus}")
    print(
        "For nonzero c, lambda_plus>0 and lambda_minus<0; the third "
        "eigenvalue is zero."
    )
    print()
    print(
        "Interpretation: after separating the tensor-like square, the "
        "nonzero vector combination inherits a negative kinetic coefficient; "
        "the orthogonal combination remains kinetically degenerate."
    )
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
