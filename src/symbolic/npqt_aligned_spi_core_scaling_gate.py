#!/usr/bin/env python3
"""Core-scaling version of the aligned NPQT SPI sign obstruction.

Take the paired aligned algebraic curvature directions

    (q, theta) and (q, -theta),

then scale the Weyl and traceless-Ricci tensors toward a maximally symmetric
curvature point:

    q -> epsilon q,
    theta -> epsilon theta.

For the algebraically complete Petrov-D / Segre [(1,1)(11)] set used by the
all-degree gate,

    I  = q^2,
    I6 = theta^2/3,
    K  = -2 q theta^2,

both sign branches have exactly identical scalar invariant coordinates at
every epsilon.

Their NPQT spherical targets are instead

    T_+ = +48 epsilon^3 q^2 theta,
    T_- = -48 epsilon^3 q^2 theta.

Thus the scalar-coordinate degeneracy accumulates arbitrarily close to the
maximally symmetric core.

This is a finite-dimensional algebraic scaling gate, conditional on the
published invariant-completeness classification used in
npqt_aligned_spi_all_degree_gate.py.
"""

from __future__ import annotations

import sympy as sp

eps = sp.symbols("epsilon", positive=True)
q, theta = sp.symbols("q theta", nonzero=True, real=True)

I = eps**2*q**2
I6 = eps**2*theta**2/3
K = -2*eps**3*q*theta**2

complete_plus = (I, I6, K)
complete_minus = tuple(sp.simplify(x.subs(theta,-theta)) for x in complete_plus)
assert complete_plus == complete_minus

Tplus = 48*eps**3*q**2*theta
Tminus = sp.simplify(Tplus.subs(theta,-theta))

assert Tminus == -Tplus
assert sp.limit(Tplus, eps, 0) == 0
assert sp.limit(Tminus, eps, 0) == 0
assert sp.simplify((Tplus-Tminus)/eps**3 - 96*q**2*theta) == 0

def main() -> None:
    print("== NPQT aligned SPI core-scaling gate ==")
    print(f"I(eps)  = {I}")
    print(f"I6(eps) = {I6}")
    print(f"K(eps)  = {K}")
    print("These are identical on theta and -theta branches.")
    print()
    print(f"T_plus  = {Tplus}")
    print(f"T_minus = {Tminus}")
    print()
    print("Both branches approach the same maximally symmetric scalar")
    print("invariant point, while their required cubic target coefficients")
    print("have opposite sign.")
    print("All core-scaling assertions passed.")

if __name__ == "__main__":
    main()
