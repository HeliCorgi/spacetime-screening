#!/usr/bin/env python3
"""Core scaling of analytic 4D generalized quasi-topological gravity.

Uses the all-order integrated spherical equation F(n,j) from
Bueno et al., CQG 40 (2023) 015004.

In D=4 there is one genuine GQTG family per curvature order n>=3, with
couplings satisfying (up to normalization)
    alpha_{n,n-1} = -n/(n-2) alpha_{n,n}.

For an exact de Sitter-type core
    f(r)=1-c r^2,  k=1,
the order-n integrated contribution reduces to
    F_n = -(1/2) c^n r^3
(up to the overall order-n coupling normalization).

Thus every finite curvature order vanishes as r^3 at a regular center.
A normally/uniformly convergent infinite tower also vanishes as r^3 and
cannot equal a nonzero ADM-mass integration constant.

Therefore a nonzero-mass regular vacuum core requires a nonuniform infinite
sum / singular resummed response at the limiting curvature, or some ingredient
outside the assumptions.
"""

from __future__ import annotations

import sympy as sp


r,c=sp.symbols("r c", positive=True, finite=True)
n,j=sp.symbols("n j", integer=True, positive=True)

D=4
k=1
f=1-c*r**2
fp=sp.diff(f,r)
fpp=sp.diff(f,r,2)


def F_nj(nsym, jsym):
    return sp.factor(
        (-1)**(jsym+1)
        /2**(jsym+1)
        *r**(D-2+jsym-2*nsym)
        *(k-f)**(nsym-jsym-1)
        *fp**(jsym-2)
        *(
            fp*(
                jsym*(D-1+jsym-2*nsym)*(k-f)*f
                -(jsym-1)*r*(k+(nsym-jsym-1)*f)*fp
            )
            +jsym*(jsym-1)*r*(k-f)*f*fpp
        )
    )


def main():
    Fgeneral=sp.factor(F_nj(n,j))
    expected_general=sp.factor(
        sp.Rational(1,2)
        *c**(n-1)*r
        *(2*j-n-c*r**2*(j-n+1))
    )
    assert sp.simplify(Fgeneral-expected_general)==0

    Fnn=sp.factor(expected_general.subs(j,n))
    Fn1=sp.factor(expected_general.subs(j,n-1))

    # Unique D=4 genuine GQTG combination, setting alpha_{n,n}=1.
    F4=sp.factor(
        Fnn-sp.Rational(1,1)*n/(n-2)*Fn1
    )
    expected_F4=sp.factor(
        -sp.Rational(1,2)*c**n*r**3
    )
    assert sp.simplify(F4-expected_F4)==0

    # General regular core with the first odd correction:
    # f=1-c r^2+d r^3+O(r^4).
    d=sp.symbols("d", finite=True)
    freg=1-c*r**2+d*r**3

    def F_nj_regular(nsym, jsym):
        fpreg=sp.diff(freg,r)
        fppreg=sp.diff(freg,r,2)
        return sp.factor(
            (-1)**(jsym+1)
            /2**(jsym+1)
            *r**(D-2+jsym-2*nsym)
            *(k-freg)**(nsym-jsym-1)
            *fpreg**(jsym-2)
            *(
                fpreg*(
                    jsym*(D-1+jsym-2*nsym)*(k-freg)*freg
                    -(jsym-1)*r*(k+(nsym-jsym-1)*freg)*fpreg
                )
                +jsym*(jsym-1)*r*(k-freg)*freg*fppreg
            )
        )

    Freg=sp.factor(
        F_nj_regular(n,n)
        -n/(n-2)*F_nj_regular(n,n-1)
    )
    core_coeff=sp.simplify(
        sp.limit(Freg/r**3,r,0)
    )
    expected_core_coeff=sp.factor(
        -sp.Rational(1,2)*c**n
        +sp.Rational(3,16)*n*(n-1)*c**(n-3)*d**2
    )
    assert sp.simplify(
        core_coeff-expected_core_coeff
    )==0

    # Einstein-Hilbert integrated contribution in D=4:
    # F_EH=-(D-2)(f-k) r^(D-3).
    FEH=sp.factor(
        -(D-2)*(f-k)*r**(D-3)
    )
    assert sp.simplify(FEH-2*c*r**3)==0

    # Finite truncations vanish at the center.
    lam3,lam4,lam5=sp.symbols(
        "lambda3 lambda4 lambda5", finite=True
    )
    trunc=sp.factor(
        FEH
        +lam3*(-sp.Rational(1,2)*c**3*r**3)
        +lam4*(-sp.Rational(1,2)*c**4*r**3)
        +lam5*(-sp.Rational(1,2)*c**5*r**3)
    )
    assert sp.limit(trunc,r,0)==0

    print("== All-order D=4 GQTG core scaling ==")
    print(f"F(n,j) on f=1-c r^2 = {Fgeneral}")
    print()
    print("Unique D=4 combination:")
    print(f"F_n = {F4}")
    print("= -(1/2) c^n r^3")
    print()
    print(f"Einstein term = {FEH}")
    print()
    print("== Generic regular core f=1-c r^2+d r^3+... ==")
    print("F_n/r^3 ->")
    print(core_coeff)
    print("Thus the O(r^3) scaling survives the generic odd correction.")
    print()
    print("Any finite truncation therefore vanishes as r^3.")
    print(
        "If the infinite tower converges uniformly/normally at the "
        "limiting curvature c, its sum also vanishes as r^3."
    )
    print(
        "A nonzero mass integration constant requires nonuniform "
        "resummation / singular response at the limiting curvature."
    )
    print()
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
