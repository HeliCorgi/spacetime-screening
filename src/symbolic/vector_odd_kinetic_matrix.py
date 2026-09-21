#!/usr/bin/env python3
"""Odd-parity kinetic diagnostics for the two-vector regular-BH benchmark.

This uses the general odd-parity quadratic-action structure of generalized
Proca / quartic vector-tensor theories.

For one odd vector perturbation u, after completing the square in

    X_g = dot(W) - Q' + 2 Q/r,

the kinetic coefficient is

    q_vec = C5 - C2^2/C1.

In the two-vector model there is no Maxwell/F^2 kinetic term, hence the direct
odd-vector kinetic block C5_ij vanishes.  With two vector perturbations u_A,u_B

    K_vec = -(1/C1) c c^T,

where c=(C2_A,C2_B).  Therefore K_vec is negative semidefinite with one
negative eigenvalue and one zero eigenvalue whenever c != 0.

The same calculation also derives the exact pure-metric odd principal block.
Its radial characteristic roots agree with the previously found null
Kerr-Schild tensor metric; one null direction remains the background one and
the other is deformed by the vector hair.

This is a principal/high-frequency quadratic-action diagnostic.  A complete
publication-level result still requires checking all lower-derivative
constraints and the precise physical degree-of-freedom count of the
degenerate two-vector system.
"""

from __future__ import annotations

import sympy as sp


r,M,q,ell,f=sp.symbols(
    "r M q ell f", positive=True, finite=True
)
a,b=sp.symbols("a b", real=True, finite=True)

# Quartic generalized-Proca slopes corresponding, up to boundary terms, to
# +/- 4 ell^2 G_{mu nu} W^mu W^nu.
betaA=4*ell**2
betaB=-4*ell**2

# Single-function diagonal background h=f and null profiles:
# A0=a, A1=a/f; B0=b, B1=b/f.
C1=sp.factor(1/(2*r**2))

C2A=sp.factor(-betaA*a/(2*f*r**2))
C2B=sp.factor(-betaB*b/(2*f*r**2))

c=sp.Matrix([C2A,C2B])
Kvec=sp.simplify(-(c*c.T)/C1)

traceK=sp.factor(sp.trace(Kvec))
detK=sp.factor(Kvec.det())

expected_nonzero=sp.factor(
    -8*ell**4*(a**2+b**2)/(f**2*r**2)
)

assert sp.simplify(traceK-expected_nonzero)==0
assert detK==0

# Rank-one matrix: its eigenvalues are {trace,0}.
assert sp.simplify(Kvec*Kvec-traceK*Kvec)==sp.zeros(2)


# Pure metric odd block.
Delta=sp.factor(betaA*a**2+betaB*b**2)

C8=sp.factor(-(f+Delta)/(2*r**4))
D=sp.factor(Delta/(f*r**4))  # coefficient of W Q
C10=sp.factor((f-Delta)/(2*f**2*r**4))

disc=sp.factor(D**2-4*C8*C10)
assert sp.simplify(disc-1/r**8)==0

vplus=sp.factor(
    (D+sp.sqrt(disc))/(2*C10)
)
vminus=sp.factor(
    (D-sp.sqrt(disc))/(2*C10)
)

expected_plus=sp.factor(
    f*(f+Delta)/(f-Delta)
)
expected_minus=-f

assert sp.simplify(vplus-expected_plus)==0
assert sp.simplify(vminus-expected_minus)==0

# Specialize to the exact regular branch profiles.
D0=r**3+2*q*ell**2
freg=sp.factor(1-2*M*r**2/D0)
areg=sp.factor((r-r*freg-q/2)/(2*r**2))
breg=sp.factor((r-r*freg+q/2)/(2*r**2))

Delta_reg=sp.factor(
    Delta.subs({a:areg,b:breg})
)
expected_Delta=sp.factor(
    -4*M*q*ell**2/(r*D0)
)
assert sp.simplify(Delta_reg-expected_Delta)==0

fT=sp.factor(freg+Delta_reg)
assert sp.simplify(fT-(1-2*M/r))==0

# Negative vector kinetic eigenvalue on the regular branch.
lambda_neg=sp.factor(
    expected_nonzero.subs({
        a:areg,
        b:breg,
        f:freg,
    })
)

# Express a^2+b^2 compactly via sum/difference basis.
expected_sum_sq=sp.factor(
    2*M**2*r**2/D0**2
    + q**2/(8*r**4)
)
assert sp.simplify(
    areg**2+breg**2-expected_sum_sq
)==0

lambda_expected=sp.factor(
    -8*ell**4*expected_sum_sq/(freg**2*r**2)
)
assert sp.simplify(lambda_neg-lambda_expected)==0

# Endpoint asymptotics in regular regions where f -> 1.
core_scaled=sp.simplify(
    sp.limit(r**6*lambda_neg,r,0,dir="+")
)
assert sp.simplify(core_scaled+ell**4*q**2)==0

infinity_scaled=sp.simplify(
    sp.limit(r**6*lambda_neg,r,sp.oo)
)
expected_inf=sp.factor(
    -8*ell**4*((M-q/4)**2+(M+q/4)**2)
)
assert sp.simplify(infinity_scaled-expected_inf)==0


def main():
    print("== Odd vector kinetic block ==")
    print("C1 =",C1)
    print("C2_A =",C2A)
    print("C2_B =",C2B)
    print("K_vec =")
    print(Kvec)
    print("det K_vec =",detK)
    print("nonzero eigenvalue =",traceK)
    print()
    print(
        "For f>0 and nonzero background vector hair, the nonzero eigenvalue "
        "is strictly negative; the orthogonal vector combination has zero "
        "quadratic kinetic coefficient."
    )
    print()

    print("== Pure metric odd principal block ==")
    print("C8 =",C8)
    print("D_WQ =",D)
    print("C10 =",C10)
    print("discriminant =",disc)
    print("radial coordinate characteristic roots:")
    print("v_- =",vminus)
    print("v_+ =",vplus)
    print()

    print("== Exact regular branch ==")
    print("Delta =",Delta_reg)
    print("f + Delta =",fT)
    print("=> deformed null direction contains 1-2M/r exactly.")
    print()
    print("negative kinetic eigenvalue:")
    print(lambda_neg)
    print("r^6 lambda_neg ->",core_scaled,"at r->0")
    print("r^6 lambda_neg ->",infinity_scaled,"at infinity")
    print()
    print(
        "Interpretation: the standard odd-sector completion-of-square "
        "diagnostic gives one negative kinetic vector combination plus one "
        "zero-kinetic combination.  This is a strong ghost/strong-coupling "
        "warning, but the fully degenerate constraint count still has to be "
        "completed before calling it a physical ghost theorem."
    )
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
