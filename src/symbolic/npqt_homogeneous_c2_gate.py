#!/usr/bin/env python3
"""Homogeneous rational densities: fixed-ray scaling is not enough for C^2.

A rational curvature density may be homogeneous of positive degree m=p-q:

    F(X)=N_p(X)/D_q(X).

If X=epsilon * X0 and D_q(X0) != 0, then
    F = O(epsilon^m),
so for m>=3 the value, first derivative and second derivative can all look
harmless along that fixed ray.

But this does NOT guarantee a continuous/C^2 extension at X=0 when the
homogeneous denominator has nontrivial zero directions.

Toy example:
    F(x,y) = x^8/(x^5+y^5),
which is homogeneous of degree 3.

Along a generic ray y=a x with 1+a^5 !=0,
    F ~ x^3/(1+a^5).

Along the tuned path
    y=-x+x^5,
the denominator cancels at leading order and
    F ~ -1/(5 x),
so the origin is not even continuous.

This is the correct caution for 4D NPQT rational densities: degree counting
can show that a fixed-ray Hessian need not diverge, but an open-neighborhood
C^2 extension requires control of the denominator-zero set and numerator
cancellations there.
"""

from __future__ import annotations
import sympy as sp

x,a=sp.symbols("x a", real=True)
y=sp.symbols("y", real=True)

F=sp.factor(x**8/(x**5+y**5))

# Generic ray y=a x.
Fray=sp.factor(F.subs(y,a*x))
assert sp.simplify(
    Fray - x**3/(1+a**5)
)==0

# First/second x derivatives along a fixed generic ray.
d1=sp.factor(sp.diff(Fray,x))
d2=sp.factor(sp.diff(Fray,x,2))
assert sp.simplify(d1-3*x**2/(1+a**5))==0
assert sp.simplify(d2-6*x/(1+a**5))==0

# Tuned approach to the denominator-zero ray y=-x.
Fbad=sp.factor(F.subs(y,-x+x**5))

# Leading divergence.
lead=sp.simplify(sp.limit(x*Fbad,x,0))
assert lead == -sp.Rational(1,5)

def main():
    print("== Homogeneous rational C^2 gate ==")
    print(f"F(x,y) = {F}")
    print()
    print("Generic fixed ray y=a x:")
    print(f"F = {Fray}")
    print(f"dF/dx = {d1}")
    print(f"d2F/dx2 = {d2}")
    print("=> for fixed nonzero denominator direction: F~x^3, dF~x^2, d2F~x")
    print()
    print("Tuned path y=-x+x^5:")
    print(f"F = {Fbad}")
    print(f"x F -> {lead}")
    print("=> F ~ -1/(5x): no continuous extension.")
    print()
    print("Conclusion: positive homogeneous degree is insufficient.")
    print("Need denominator-zero-set cancellation/divisibility for a true C^2 extension.")
    print("All homogeneous-rational gate assertions passed.")

if __name__=="__main__":
    main()
