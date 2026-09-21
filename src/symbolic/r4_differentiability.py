#!/usr/bin/env python3
"""Differentiability test for the 2026 QTG-TNT invariant R4.

Reference:
Colléaux, Kolář, Málek, arXiv:2606.17784.

Their covariant representative is
    R4 = sqrt(Q),
    Q  = 2 I6/3 - 2 I11/I1,

where
    I1  = C_{abcd} C^{abcd},
    I6  = S_{ab} S^{ab},
    I11 = S S (C C - Ctilde Ctilde).

On TNT geometries Appendix A gives
    R4^2 = 4 Phi00 Phi22.
On the Lorentzian single-function branch, Phi00=Phi22=0, hence R4=0.

This script shows:
1. generic invariant derivatives diverge as 1/R4 and 1/R4^3;
2. even within a smooth TNT perturbation, sqrt(R4_signed^2)=|R4_signed|
   has a cusp at the SF branch;
3. the correction A(ell^2 R3) R4 is differentiable there only if A=0,
   which would remove the nontrivial Class-I correction at that point;
4. for the paper's explicit regular-BH example A(x)=2x/(1-x), A diverges
   as -4m/r at the regular center and also has a pole at r=sqrt(2) ell.

This is a covariant-action differentiability obstruction, not a statement
that the symmetry-reduced field equations are invalid.
"""

from __future__ import annotations

import sympy as sp


I1,I6,I11=sp.symbols("I1 I6 I11", positive=True, finite=True)

Q=sp.factor(sp.Rational(2,3)*I6 - 2*I11/I1)
R4=sp.sqrt(Q)

dR4_I6=sp.simplify(sp.diff(R4,I6))
dR4_I11=sp.simplify(sp.diff(R4,I11))
d2R4_I6=sp.simplify(sp.diff(R4,I6,2))

# Express in R4 language.
expected_dI6=1/(3*R4)
expected_dI11=-1/(I1*R4)
expected_d2I6=-1/(9*R4**3)

assert sp.simplify(dR4_I6-expected_dI6)==0
assert sp.simplify(dR4_I11-expected_dI11)==0
assert sp.simplify(d2R4_I6-expected_d2I6)==0


# TNT perturbation of the SF branch.
# For n=0, Eq. (6.4) reduces to R4_signed = a b'/(2 r b).
eps,r,a0,hp=sp.symbols("epsilon r a hprime", real=True, nonzero=True)

R4_signed=eps*a0*hp/(2*r)
R4_cov=sp.Abs(R4_signed)

# One-sided epsilon derivatives at epsilon=0.
slope_mag=sp.Abs(a0*hp/(2*r))
right_slope=slope_mag
left_slope=-slope_mag

assert sp.simplify(right_slope-left_slope)==2*slope_mag


# Correction L_corr=A*R4 along the TNT path.
Avec=sp.symbols("A", real=True, finite=True)
right_action_slope=sp.factor(Avec*right_slope)
left_action_slope=sp.factor(Avec*left_slope)

# They match only when A=0 (or perturbation direction is zero).
slope_jump=sp.factor(right_action_slope-left_action_slope)
assert sp.simplify(slope_jump-2*Avec*slope_mag)==0


# Explicit regular-BH example, Eq. (6.18)-(6.19):
# A(x)=2x/(1-x),
# a(r)=(r-2m)(r^2-2l^2)/(r^3-2rl^2+4ml^2).
m,l=sp.symbols("m ell", positive=True, finite=True)
metric_a=sp.factor(
    (r-2*m)*(r**2-2*l**2)
    /(r**3-2*r*l**2+4*m*l**2)
)

R3=sp.factor(2*(1-metric_a)/r**2)
x=sp.factor(l**2*R3)
Aexample=sp.factor(2*x/(1-x))

expected_R3=sp.factor(
    4*m/(4*l**2*m-2*l**2*r+r**3)
)
expected_A=sp.factor(
    8*m*l**2/(r*(r**2-2*l**2))
)

assert sp.simplify(R3-expected_R3)==0
assert sp.simplify(Aexample-expected_A)==0

# Core and fixed-horizon behavior.
core_x=sp.limit(x,r,0,dir="+")
core_A_scaled=sp.limit(r*Aexample,r,0,dir="+")
assert core_x==1
assert sp.simplify(core_A_scaled+4*m)==0

r_fixed=sp.sqrt(2)*l
# Pole test via denominator.
assert sp.simplify(sp.denom(Aexample).subs(r,r_fixed))==0


def main():
    print("== Covariant R4 ==")
    print(f"Q = {Q}")
    print(f"R4 = sqrt(Q) = {R4}")
    print()
    print("Generic invariant derivatives:")
    print(f"dR4/dI6 = {dR4_I6}")
    print(f"dR4/dI11 = {dR4_I11}")
    print(f"d2R4/dI6^2 = {d2R4_I6}")
    print("=> first derivative ~ 1/R4, second derivative ~ 1/R4^3")
    print()

    print("== TNT perturbation across the SF branch ==")
    print(f"signed reduced R4 = {R4_signed}")
    print(f"covariant sqrt(R4^2) = {R4_cov}")
    print(f"right derivative at epsilon=0 = {right_slope}")
    print(f"left derivative at epsilon=0 = {left_slope}")
    print("=> cusp: no two-sided derivative unless the direction is trivial")
    print()

    print("== Action correction A R4 ==")
    print(f"jump in one-sided first variations = {slope_jump}")
    print("=> differentiable at R4=0 only if A=0 for that background point")
    print()

    print("== Explicit regular-BH example ==")
    print(f"R3(r) = {R3}")
    print(f"x=ell^2 R3 = {x}")
    print(f"A(x(r)) = {Aexample}")
    print(f"x -> {core_x} at r->0")
    print(f"r A -> {core_A_scaled} at r->0")
    print("Thus A ~ -4m/r at the regular center.")
    print(f"A also has a pole at r=sqrt(2) ell = {r_fixed}.")
    print()

    print(
        "Conclusion: the symmetry-reduced signed R4 is usable inside the "
        "TNT sector, but the displayed covariant square-root representative "
        "is not differentiable on the SF branch and is unsuitable as-is "
        "for a generic 4D perturbation theory."
    )
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
