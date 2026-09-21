#!/usr/bin/env python3
"""Cotton-projector differentiability at a smooth spherical core.

The 2026 4D NPG action uses the normalized non-analytic tensor

    u ~ (C C) / (C^2),

where C is the Cotton tensor.

For a smooth single-function spherical center

    f(r) = 1 - c r^2 + d r^4 + O(r^6),

the spherical Weyl scalar from the NPG paper is

    psi_W = f''/2 - f'/r - (1-f)/r^2
          = 3 d r^2 + O(r^4).

The Cotton tensor is built schematically from
    partial psi_W + (1/r) psi_W,
so its nonzero amplitudes vanish as O(r).

Hence C^2=O(r^2).

A normalized quadratic direction tensor
    U(v)=v v^T/(v.v)
has a finite directional value for v=epsilon w, but
    dU/dv = O(1/epsilon),
    d^2U/dv^2 = O(1/epsilon^2).

Therefore an NPG action whose covariant definition fundamentally uses this
normalized Cotton tensor is not differentiable in generic curvature
directions at a smooth conformally-flat spherical core, unless a special
full-action cancellation is proved.

This is a structural principal-safety obstruction, not a statement that the
symmetry-reduced equations are singular.
"""

from __future__ import annotations
import sympy as sp

r,c,d,e=sp.symbols(
    "r c d e", finite=True
)

# Smooth spherical core through r^4.
f=1-c*r**2+d*r**4+e*r**6

psiW=sp.factor(
    sp.diff(f,r,2)/2
    -sp.diff(f,r)/r
    -(1-f)/r**2
)

assert sp.expand(psiW).coeff(r,0)==0
assert sp.expand(psiW).coeff(r,2)==3*d
assert sp.expand(psiW).coeff(r,4)==10*e

# Schematic Cotton radial amplitude: psi' and psi/r have the same O(r).
Cot1=sp.factor(sp.diff(psiW,r))
Cot2=sp.factor(psiW/r)

assert sp.limit(Cot1/r,r,0)==6*d
assert sp.limit(Cot2/r,r,0)==3*d

# Cotton norm scaling represented by C2 ~ kappa r^2.
kappa=sp.symbols("kappa", positive=True, finite=True)
C2=kappa*r**2
assert sp.limit(C2,r,0)==0

# Normalized projector toy U = vv^T/(v.v).
eps=sp.symbols("epsilon", positive=True, finite=True)
w1,w2=sp.symbols("w1 w2", real=True)
v1=eps*w1
v2=eps*w2
norm=sp.factor(v1**2+v2**2)

U=sp.Matrix([
    [v1*v1/norm, v1*v2/norm],
    [v2*v1/norm, v2*v2/norm],
])
Us=sp.simplify(U)
assert not Us.has(eps)

# Generic derivative before restricting to the ray.
x,y=sp.symbols("x y", real=True)
n=x**2+y**2
Uxx=x**2/n

dUdx=sp.factor(sp.diff(Uxx,x))
d2Udx2=sp.factor(sp.diff(Uxx,x,2))

ray={x:eps*w1,y:eps*w2}
dU_ray=sp.factor(dUdx.subs(ray))
d2U_ray=sp.factor(d2Udx2.subs(ray))

# Scale tests.
assert sp.simplify(
    sp.diff(sp.log(sp.Abs(dU_ray)),eps)
    +1/eps
)==0
assert sp.simplify(
    sp.diff(sp.log(sp.Abs(d2U_ray)),eps)
    +2/eps
)==0

def main():
    print("== Smooth spherical core ==")
    print(f"f(r) = {f}")
    print(f"Weyl scalar psi_W = {psiW}")
    print(f"psi_W/r^2 -> {sp.limit(psiW/r**2,r,0)}")
    print(f"psi_W'/r -> {sp.limit(Cot1/r,r,0)}")
    print(f"(psi_W/r)/r -> {sp.limit(Cot2/r,r,0)}")
    print()
    print("Thus Weyl = O(r^2), Cotton = O(r), Cotton^2 = O(r^2).")
    print()
    print("== Normalized direction tensor ==")
    print("U(v)=v v^T/(v.v) is finite along v=epsilon w:")
    print(Us)
    print()
    print(f"d U_xx/dx on ray = {dU_ray}")
    print(f"d2 U_xx/dx2 on ray = {d2U_ray}")
    print("=> first derivative ~ epsilon^-1, Hessian ~ epsilon^-2.")
    print()
    print(
        "Conclusion: normalized Cotton/Weyl direction tensors can have a "
        "finite symmetry-reduced value while their generic covariant "
        "variation diverges at a smooth spherical core."
    )
    print("All Cotton-projector core assertions passed.")

if __name__=="__main__":
    main()
