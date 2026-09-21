#!/usr/bin/env python3
"""Curvature-projector obstruction at symmetry-enhanced cores.

Many covariant lifts of a spherical reduced variable implicitly reconstruct
the 2+2 warped-product splitting from curvature eigenvectors/projectors.

For an operator with two eigenvalues lambda_B and lambda_S, the spectral
projectors are

    P_B = (A-lambda_S I)/(lambda_B-lambda_S),
    P_S = (A-lambda_B I)/(lambda_S-lambda_B).

They become undefined when the eigenvalue gap closes.

At a maximally symmetric/de Sitter core, Ricci is proportional to the metric
and Weyl vanishes.  The curvature no longer distinguishes the radial/base
plane from the sphere.  Any local covariant formula that tries to recover
that directional split by dividing by curvature eigenvalue gaps is therefore
necessarily singular or non-differentiable at the symmetry-enhanced point.

This is a kinematical linear-algebra statement, not a no-go theorem against
smooth covariant actions that never introduce such projectors.
"""

from __future__ import annotations

import sympy as sp


lb,ls=sp.symbols("lambda_B lambda_S", finite=True)
eps=sp.symbols("epsilon", nonzero=True)

# A simple diagonal 2+2 endomorphism with two doubly-degenerate eigenvalues.
A=sp.diag(lb,lb,ls,ls)
I=sp.eye(4)

PB=sp.simplify((A-ls*I)/(lb-ls))
PS=sp.simplify((A-lb*I)/(ls-lb))


def main():
    expected_PB=sp.diag(1,1,0,0)
    expected_PS=sp.diag(0,0,1,1)

    assert sp.simplify(PB-expected_PB)==sp.zeros(4)
    assert sp.simplify(PS-expected_PS)==sp.zeros(4)
    assert sp.simplify(PB+PS-I)==sp.zeros(4)
    assert sp.simplify(PB*PB-PB)==sp.zeros(4)
    assert sp.simplify(PS*PS-PS)==sp.zeros(4)

    # Approach a maximally symmetric point:
    # lambda_B=lambda+eps, lambda_S=lambda.
    lam=sp.symbols("lambda", finite=True)
    Aeps=sp.diag(lam+eps,lam+eps,lam,lam)
    PB_raw=(Aeps-lam*I)/eps

    # The value along this specially correlated path remains a projector.
    assert sp.simplify(PB_raw-expected_PB)==sp.zeros(4)

    # But generic variations of A at fixed eigenvalue labels are amplified by
    # 1/eps.  Model one off-block perturbation.
    h=sp.symbols("h", finite=True)
    dA=sp.zeros(4)
    dA[0,2]=h
    dA[2,0]=h

    dPB=sp.simplify(dA/eps)
    assert dPB[0,2]==h/eps
    assert dPB[2,0]==h/eps

    # Frobenius norm squared of the variation scales as eps^-2.
    norm2=sp.factor(sum(dPB[i,j]**2 for i in range(4) for j in range(4)))
    assert sp.simplify(norm2-2*h**2/eps**2)==0

    print("== Spectral projectors for a 2+2 curvature split ==")
    print("P_B =")
    print(PB)
    print("P_S =")
    print(PS)
    print()
    print("As lambda_B-lambda_S = epsilon -> 0,")
    print("the projector value can remain finite along a tuned diagonal path,")
    print("but a generic off-block variation gives")
    print(f"delta P_B[0,2] = {dPB[0,2]}")
    print(f"||delta P_B||^2 = {norm2}")
    print()
    print(
        "Thus the derivative of a curvature-defined directional projector "
        "diverges when the eigenvalue gap closes."
    )
    print(
        "A de Sitter/maximally symmetric core has precisely such enhanced "
        "degeneracy; smooth actions should avoid explicit curvature "
        "projector reconstruction there."
    )
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
