#!/usr/bin/env python3
"""Analyticity obstruction for linear R4 QTG-TNT terms.

For TNT geometries the 2026 classification proves that scalar invariants
analytic in the Riemann tensor contain R4 only through even powers.

This toy symbolic check encodes the local consequence:

    L_analytic(R4) = F(R4^2)

is even in R4, so
    dL/dR4 |_{R4=0} = 0.

Therefore an action term with a nonzero linear coefficient
    c R4
cannot arise from an analytic curvature scalar near R4=0.

Combining this with the separate square-root result
    R4 = sqrt(Q)
shows the tradeoff:
- analytic action -> no linear R4 / no first-order Class-I mechanism;
- linear R4 -> nonanalytic cusp in the displayed covariant representative.
"""

from __future__ import annotations

import sympy as sp


x=sp.symbols("R4", real=True)
c0,c1,c2,c3=sp.symbols("c0 c1 c2 c3", finite=True)

# Generic truncated analytic even expansion.
L_even=c0+c1*x**2+c2*x**4+c3*x**6

assert sp.simplify(L_even.subs(x,-x)-L_even)==0
assert sp.simplify(sp.diff(L_even,x).subs(x,0))==0

# A linear Class-I term is odd at leading order and has nonzero slope.
lam=sp.symbols("lambda", nonzero=True)
L_linear=lam*x
assert sp.diff(L_linear,x).subs(x,0)==lam
assert sp.simplify(L_linear.subs(x,-x)+L_linear)==0

# No finite polynomial in x^2 can reproduce a nonzero linear derivative.
coeffs=sp.symbols("a0:6")
F=sum(coeffs[n]*x**(2*n) for n in range(6))
assert sp.simplify(sp.diff(F,x).subs(x,0))==0


def main():
    print("== Analytic TNT dependence ==")
    print(f"L_even(R4) = {L_even}")
    print(f"L_even(-R4)-L_even(R4) = {sp.expand(L_even.subs(x,-x)-L_even)}")
    print(f"dL_even/dR4 at R4=0 = {sp.diff(L_even,x).subs(x,0)}")
    print()
    print("== Required first-order Class-I structure ==")
    print(f"L_linear = {L_linear}")
    print(f"dL_linear/dR4 at 0 = {lam}")
    print()
    print(
        "An analytic scalar curvature action restricted to TNT cannot "
        "generate a nonzero linear R4 coefficient at the SF branch."
    )
    print(
        "Thus retaining the algebraic/first-order Class-I mechanism requires "
        "nonanalytic curvature dependence, exactly as established by the "
        "2026 classification."
    )
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
