#!/usr/bin/env python3
"""Algebraic root structure for the spherical angular Ricci mode Theta.

For a general spherical/class-B traceless-Ricci spectrum

    {lambda_1, lambda_2, Theta, Theta},
    lambda_1 + lambda_2 + 2 Theta = 0,

use the Carminati-McLenaghan normalizations

    r1 = (1/4) tr(S^2),
    r2 = -(1/8) tr(S^3).

Eliminating lambda_1 lambda_2 gives the cubic

    3 Theta^3 - 3 r1 Theta + 2 r2 = 0.

Thus Theta is an algebraic root over the scalar-invariant field, not a
globally rational scalar function.

At the aligned sign-blind stratum

    r1 = Theta0^2,
    r2 = 0,

the cubic factors as

    3 x (x-Theta0)(x+Theta0),

so the invariant data admit the three roots 0,+Theta0,-Theta0.

For either nonzero sign root the implicit-function derivative is

    dF/dx = 6 Theta0^2 != 0,

so a chosen branch is locally analytic at a fixed nonzero aligned point.

At the maximally symmetric core r1=r2=x=0 all three roots coalesce and
dF/dx=0, so the implicit-function theorem no longer selects a smooth branch.

This is a branch/root gate, not a proof that every weighted density built
from a chosen root fails C2.
"""

from __future__ import annotations

import sympy as sp

x, theta = sp.symbols("x theta", real=True)
l1, l2 = sp.symbols("lambda1 lambda2", real=True)

trace_constraint = {l2: -2*theta-l1}

r1 = sp.factor(
    (l1**2+l2**2+2*theta**2).subs(trace_constraint)/4
)
r2 = sp.factor(
    -(l1**3+l2**3+2*theta**3).subs(trace_constraint)/8
)

# Eliminate the remaining product/eigenvalue information through r1.
# Direct substitution verifies the cubic identity.
Ftheta = sp.factor(3*theta**3 - 3*r1*theta + 2*r2)
assert sp.simplify(Ftheta) == 0

R1, R2 = sp.symbols("r1 r2", real=True)
F = 3*x**3 - 3*R1*x + 2*R2

aligned = sp.factor(F.subs({R1:theta**2,R2:0}))
assert aligned == 3*x*(x-theta)*(x+theta)

Fx = sp.diff(F,x)
dplus = sp.factor(Fx.subs({R1:theta**2,R2:0,x:theta}))
dminus = sp.factor(Fx.subs({R1:theta**2,R2:0,x:-theta}))
dcore = sp.factor(Fx.subs({R1:0,R2:0,x:0}))

assert dplus == 6*theta**2
assert dminus == 6*theta**2
assert dcore == 0

# Cubic discriminant: positive/zero/negative determines the real-root pattern.
disc = sp.factor(sp.discriminant(F,x))
assert sp.expand(disc - 324*(R1**3 - 3*R2**2)) == 0

def main() -> None:
    print("== NPQT spherical Theta root gate ==")
    print(f"r1 = {r1}")
    print(f"r2 = {r2}")
    print("Theta obeys 3 Theta^3 - 3 r1 Theta + 2 r2 = 0.")
    print()
    print(f"aligned polynomial = {aligned}")
    print(f"dF/dx at +Theta = {dplus}")
    print(f"dF/dx at -Theta = {dminus}")
    print(f"dF/dx at core = {dcore}")
    print(f"discriminant = {disc}")
    print()
    print("Conclusion: each nonzero aligned sign branch is locally analytic,")
    print("but scalar invariants do not select which branch, and all roots")
    print("coalesce at the maximally symmetric core.")
    print("All Theta-root assertions passed.")

if __name__=="__main__":
    main()
