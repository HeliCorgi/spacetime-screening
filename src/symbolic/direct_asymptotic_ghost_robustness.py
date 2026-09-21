#!/usr/bin/env python3
"""Robustness of the direct asymptotic odd ghost under null-field elimination.

The direct l=2 original-action calculation gives, after eliminating Q in a
large-r region where its algebraic coefficient is positive, a 2x2 kinetic
matrix K_Q for the remaining velocity-active variables (W,U) with

    det K_Q < 0.

Therefore K_Q already has one positive and one negative eigenvalue.

The derivative-null vector combination V has:
- no quadratic velocity;
- no linear velocity mixing in the direct audit;
- positive algebraic stiffness m_V>0 on the regular branch.

Even if one allowed an arbitrary residual linear velocity coupling
    V j^T dot q
not seen in the direct audit, eliminating V would shift

    K_Q -> K_Q - (j j^T)/(2 m_V)

(up to a positive convention factor).

This is a negative-semidefinite Schur-complement correction.  It cannot remove
an existing negative kinetic direction.

This script encodes that statement in a diagonal eigenbasis.
"""

from __future__ import annotations

import sympy as sp


kp,km,m=sp.symbols(
    "k_plus k_minus m_V", positive=True, finite=True
)
j1,j2=sp.symbols(
    "j1 j2", real=True
)

# K_Q has one positive and one negative eigenvalue.
KQ=sp.diag(kp,-km)

j=sp.Matrix([j1,j2])

Kfinal=sp.simplify(
    KQ-(j*j.T)/(2*m)
)

# Evaluate the final quadratic form on the original negative eigenvector e2.
e2=sp.Matrix([0,1])
rayleigh_negative=sp.factor(
    (e2.T*Kfinal*e2)[0]
)

expected=sp.factor(
    -km-j2**2/(2*m)
)

assert sp.simplify(
    rayleigh_negative-expected
)==0

# It is manifestly strictly negative for km,m>0.
# Direct audit gives j1=j2=0 for V, in which case Kfinal=KQ exactly.
K_direct=sp.simplify(
    Kfinal.subs({j1:0,j2:0})
)
assert sp.simplify(K_direct-KQ)==sp.zeros(2)


def main():
    print("== Null-field Schur-complement robustness ==")
    print("K_Q =")
    print(KQ)
    print()
    print("K_final after eliminating algebraic V =")
    print(Kfinal)
    print()
    print(
        "quadratic form along the pre-existing negative direction =",
        rayleigh_negative,
    )
    print("< 0 for k_minus>0 and m_V>0")
    print()
    print(
        "Therefore an algebraic positive-stiffness null field cannot repair "
        "the negative kinetic mode.  In the direct A-B audit its velocity "
        "coupling vanishes anyway, so K_final=K_Q."
    )
    print("All robustness assertions passed.")


if __name__=="__main__":
    main()
