#!/usr/bin/env python3
"""Conditional no-go: regular GQTG core vs normally convergent base Hessian.

For the genuine 4D GQTG tower, the integrated order-n contribution on an
exact de Sitter-type core f=1-c r^2 is

    F_n = -(1/2) lambda_n c^n r^3.

Let
    G(c) = sum_{n>=3} lambda_n c^n.

A nonzero mass integration constant at r->0 requires
    r^3 G(c(r)) -> M0 != 0,
so G(c(r)) must diverge as r^-3 while c(r)->c_* finite.

If the curvature expansion is normally convergent in a neighborhood of c_*,
then G(c_*) is finite and the nonzero-mass core is impossible.

Moreover, termwise twice differentiability requires convergence of
    H(c) = sum n(n-1) lambda_n c^(n-2),
the same type of series entering curvature Hessians on constant-curvature
backgrounds.

Representative geometric coefficients lambda_n=c_*^(1-n) produce
    G ~ 1/(1-c/c_*)
and
    H ~ (1-c/c_*)^-3,
showing explicitly that the response pole comes with a divergent Hessian.

This is a conditional no-go under normal-convergence/termwise-differentiation
assumptions, not a theorem for every possible resummation prescription.
"""

from __future__ import annotations
import sympy as sp

z,zs=sp.symbols("z z_*", positive=True, finite=True)
q=sp.factor(z/zs)

# Representative geometric tower beginning at n=3:
# lambda_n = zs^(1-n), so lambda_n z^n = zs q^n.
G=sp.factor(
    zs * q**3/(1-q)
)

Gp=sp.factor(sp.diff(G,z))
Gpp=sp.factor(sp.diff(G,z,2))

# Verify pole orders at q->1 using eps=1-q.
eps=sp.symbols("epsilon", positive=True)
subs={z:zs*(1-eps)}

Ge=sp.factor(G.subs(subs))
Gpe=sp.factor(Gp.subs(subs))
Gppe=sp.factor(Gpp.subs(subs))

assert sp.simplify(sp.limit(eps*Ge,eps,0)-zs)==0
assert sp.simplify(sp.limit(eps**2*Gpe,eps,0)-1)==0
assert sp.simplify(sp.limit(eps**3*Gppe,eps,0)-2/zs)==0

# Core approach c_*-c ~ a r^p.
r,a,p=sp.symbols("r a p", positive=True, finite=True)
eps_r=a*r**p/zs
Gr=sp.factor(Ge.subs(eps,eps_r))

# r^3 G finite nonzero requires p=3 for the simple pole.
core_p3=sp.simplify(sp.limit(r**3*Gr.subs(p,3),r,0))
assert sp.simplify(core_p3-zs**2/a)==0

def main():
    print("== Conditional GQTG core/Hessian no-go ==")
    print(f"G(z) = {G}")
    print(f"G'(z) = {Gp}")
    print(f"G''(z) = {Gpp}")
    print()
    print("Near z=z_* with epsilon=1-z/z_*:")
    print(f"epsilon G -> {sp.limit(eps*Ge,eps,0)}")
    print(f"epsilon^2 G' -> {sp.limit(eps**2*Gpe,eps,0)}")
    print(f"epsilon^3 G'' -> {sp.limit(eps**3*Gppe,eps,0)}")
    print()
    print("For z_*-z ~ a r^3:")
    print(f"r^3 G -> {core_p3}")
    print()
    print("Thus the simplest resummation that supports a nonzero-mass")
    print("finite-curvature core places the core at a pole of the response")
    print("and makes its second derivative diverge.")
    print()
    print("General gate: if the local curvature series and its Hessian")
    print("converge normally at c_*, then G(c_*) is finite and r^3 G -> 0.")
    print("All conditional no-go assertions passed.")

if __name__=="__main__":
    main()
