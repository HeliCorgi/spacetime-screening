#!/usr/bin/env python3
"""Required resummation singularity for a nonzero-mass regular 4D GQTG core.

Suppose the integrated spherical equation near a regular center has the form

    M_eff = r^3 * G(c(r)) + subleading,

where c(r) is a finite curvature-response variable approaching c_* as

    c(r) - c_* = a r^p + ...

with p>0.

If M_eff -> M0 != 0, then necessarily

    G(c(r)) ~ M0 / r^3

and hence

    G(c) ~ const * |c-c_*|^{-3/p}.

This is a response/resummation singularity required to compensate the
universal r^3 suppression of each finite analytic 4D GQTG order.

It is NOT by itself a pathology of the fundamental 4D action.  The pathology
question is whether the action and the physical reduced quadratic operator
remain differentiable and principal-safe.
"""

from __future__ import annotations

import sympy as sp


r,a,p,M0=sp.symbols(
    "r a p M0", positive=True, finite=True
)
dc=sp.symbols("Delta_c", positive=True, finite=True)


def main():
    # c-c* = a r^p  => r = (dc/a)^(1/p)
    r_of_dc=(dc/a)**(1/p)
    G_required=sp.factor(M0/r_of_dc**3)

    expected=sp.factor(
        M0*a**(sp.Rational(3,1)/p)
        *dc**(-sp.Rational(3,1)/p)
    )
    assert sp.simplify(G_required-expected)==0

    # Representative core approaches.
    exponents={
        "Hayward-like p=3": sp.simplify(sp.Rational(3,3)),
        "even-smooth p=2": sp.simplify(sp.Rational(3,2)),
        "linear approach p=1": sp.simplify(sp.Rational(3,1)),
    }

    print("== Required resummation singularity ==")
    print("Assume c-c_* = a r^p and r^3 G(c(r)) -> M0 != 0.")
    print(f"G(c) = {G_required}")
    print()
    print("Therefore G(c) ~ |c-c_*|^{-3/p}.")
    print()
    for name,alpha in exponents.items():
        print(f"{name}: required pole exponent alpha = {alpha}")
    print()
    print(
        "Interpretation: the inverse/resummed spherical response must become "
        "nonuniform at the limiting curvature. This is expected from "
        "saturation and is not, by itself, a four-dimensional action "
        "pathology."
    )
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
