#!/usr/bin/env python3
"""Asymptotic obstruction to exact Hayward from analytic 4D GQTG.

For the unique genuine 4D GQTG combination at curvature order n>=3, use the
all-order integrated spherical expression from the repository's existing
analytic_gqtg_core_scaling.py.

Evaluated on Schwarzschild f=1-2M/r, the order-n contribution is

    F_n =
      (-1)^n [
        (9/4)n(n-1) M^(n-1) r^(-(3n-4))
        + O(r^(-(3n-3)))
      ].

The Einstein integrated term is
    F_EH = 4M - 2 r delta f + ...

Hence a small order-n correction produces

    delta f_n = O(r^(-(3n-3))).

The first genuine 4D GQTG term is cubic n=3:
    delta f_3 = O(r^-6).

By contrast the Hayward metric has

    f_H = 1 - 2M/r + 4 M^2 ell^2/r^4 + O(r^-7).

Therefore no finite analytic 4D GQTG truncation, and no normally convergent
tower whose large-r expansion is termwise valid, can reproduce exact Hayward
asymptotics.  A nonuniform/nonanalytic resummation at infinity would be
required, which is incompatible with the intended ordinary EFT expansion.

This does not rule out regular black holes with GQTG-compatible r^-6 leading
corrections.
"""

from __future__ import annotations
import sympy as sp

r,M,ell,n=sp.symbols(
    "r M ell n", positive=True, finite=True
)

fS=1-2*M/r

def F_nj(nsym, jsym):
    fp=sp.diff(fS,r)
    fpp=sp.diff(fS,r,2)
    return sp.factor(
        (-1)**(jsym+1)
        /2**(jsym+1)
        *r**(2+jsym-2*nsym)
        *(1-fS)**(nsym-jsym-1)
        *fp**(jsym-2)
        *(
            fp*(
                jsym*(3+jsym-2*nsym)*(1-fS)*fS
                -(jsym-1)*r*(1+(nsym-jsym-1)*fS)*fp
            )
            +jsym*(jsym-1)*r*(1-fS)*fS*fpp
        )
    )

Fn=sp.factor(
    F_nj(n,n)-n/(n-2)*F_nj(n,n-1)
)

expected=sp.factor(
    (-1)**n
    *(
        sp.Rational(9,4)*n*(n-1)*M**(n-1)/r**(3*n-4)
        +(-18*n**2+24*n-2)*M**n/(4*r**(3*n-3))
    )
)
assert sp.simplify(Fn-expected)==0

# First genuine term n=3.
F3=sp.factor(Fn.subs(n,3))
assert sp.simplify(
    F3
    -(
        -sp.Rational(27,2)*M**2/r**5
        +23*M**3/r**6
    )
)==0

# Linearized integrated Einstein response: -2 r delta f + lambda_n F_n=0.
lam=sp.symbols("lambda", finite=True)
df3=sp.factor(lam*F3/(2*r))
assert sp.simplify(
    sp.limit(r**6*df3,r,sp.oo)
    +sp.Rational(27,4)*lam*M**2
)==0

# Hayward asymptotic series.
fH=1-2*M*r**2/(r**3+2*M*ell**2)
x=sp.symbols("x", positive=True)
seriesH=sp.series(fH.subs(r,1/x),x,0,8).removeO()
coeff4=sp.expand(seriesH).coeff(x,4)
assert sp.simplify(coeff4-4*M**2*ell**2)==0

# No n>=3 leading exponent 3n-3 equals 4.
sol=sp.solve(sp.Eq(3*n-3,4),n)
assert sol==[sp.Rational(7,3)]

def main():
    print("== 4D GQTG Schwarzschild asymptotics ==")
    print(f"F_n = {Fn}")
    print()
    print(f"F_3 = {F3}")
    print(f"delta f_3 = {df3}")
    print("leading cubic metric correction: r^-6")
    print()
    print("== Hayward ==")
    print(f"f_H large-r = {seriesH}")
    print(f"r^-4 coefficient = {coeff4}")
    print()
    print("No integer n>=3 satisfies 3n-3=4.")
    print("Therefore exact Hayward asymptotics are incompatible with a")
    print("normally convergent analytic 4D GQTG tower.")
    print()
    print("A new GQTG-compatible regular target must start with r^-6")
    print("corrections rather than the Hayward r^-4 correction.")
    print("All asymptotic-obstruction assertions passed.")

if __name__=="__main__":
    main()
