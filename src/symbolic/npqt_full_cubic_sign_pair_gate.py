#!/usr/bin/env python3
"""Full cubic spherical-density sign-pair gate for 4D NPQT.

The displayed cubic density has the structure

    Z_(3) = P_(3)(Riemann) + (9/2) * N/D,

where P_(3) is polynomial in the curvature and, on the general spherical
family,

    N/D = W2 * Theta.

On the aligned paired curvature tensors

    (q, +Theta), (q, -Theta),

all algebraic scalar polynomial Riemann invariants are identical conditional
on the Zakhary--McIntosh complete-set result documented in the companion
all-degree gate.  Hence the polynomial cubic piece has the same value on the
two tensors.

The rational spherical target changes sign.  Therefore the full spherical
density difference is

    Delta Z_(3)
      = (9/2)[W2 Theta - (-W2 Theta)]
      = 9 W2 Theta
      = 432 q^2 Theta.

Consequently, adding a covariant density that vanishes identically on every
spherical configuration cannot remove this paired-density distinction.

Scope:
- this concerns representatives with the same *pointwise spherical density*;
- it does not exclude changing the reduced action by spherical total
  derivatives while preserving equations of motion;
- it inherits the conditional invariant-completeness premise of the
  all-degree SPI sign gate.
"""

from __future__ import annotations

import sympy as sp

q, theta = sp.symbols("q theta", nonzero=True, real=True)
P3 = sp.symbols("P3", real=True)

W2 = 48*q**2
Rplus = W2*theta
Rminus = -W2*theta

Z3plus = P3 + sp.Rational(9,2)*Rplus
Z3minus = P3 + sp.Rational(9,2)*Rminus

difference = sp.factor(Z3plus-Z3minus)

assert difference == 432*q**2*theta
assert difference != 0

# A spherical-vanishing deformation V has V=0 on both paired configurations.
Vplus = sp.Integer(0)
Vminus = sp.Integer(0)
assert sp.simplify((Z3plus+Vplus)-(Z3minus+Vminus)-difference) == 0

# Under common tracefree-curvature scaling the distinction accumulates at the
# maximally symmetric core with cubic order.
eps = sp.symbols("epsilon", positive=True)
scaled = sp.factor(difference.subs({q:eps*q,theta:eps*theta}))
assert scaled == 432*eps**3*q**2*theta
assert sp.limit(scaled,eps,0) == 0

def main() -> None:
    print("== NPQT full cubic spherical-density sign-pair gate ==")
    print(f"W2 = {W2}")
    print(f"rational + branch = {Rplus}")
    print(f"rational - branch = {Rminus}")
    print(f"Delta Z_(3) = {difference}")
    print()
    print("Any deformation that vanishes on all spherical configurations")
    print("takes the same zero value on the pair and cannot remove this")
    print("density distinction.")
    print(f"Under common scaling: Delta Z_(3) = {scaled}")
    print("All full-density sign-pair assertions passed.")

if __name__=="__main__":
    main()
