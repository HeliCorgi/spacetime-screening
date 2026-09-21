#!/usr/bin/env python3
"""C1 gate for the simplest single-valued SPI root completion.

On the aligned stratum the complete scalar data contain

    I6 = theta^2/3.

The principal real square-root prescription gives

    theta_abs = sqrt(3 I6) = |theta|,

so the NPQT target would be replaced by

    T_abs = W2 |theta| = 48 q^2 |theta|.

This is continuous but not C1 at theta=0 whenever q != 0:

    dT/dtheta|_{0+} = +48 q^2,
    dT/dtheta|_{0-} = -48 q^2.

Because q can be arbitrarily small but nonzero, such cusp points occur in
every curvature neighborhood of the maximally symmetric core.

Scope: this rejects the branch-independent principal-square-root/absolute
value completion.  It does not reject locally signed spectral-projector
branches, Cartan data, derivative invariants, or other non-SPI structures.
"""

from __future__ import annotations

import sympy as sp

q, theta, eps = sp.symbols("q theta epsilon", real=True, positive=True)

# Use a positive approach variable u to encode the two theta sides.
u = sp.symbols("u", positive=True)

T_plus = 48*q**2*u
T_minus = 48*q**2*u  # |theta| on theta=-u

# Derivative with respect to theta.  On the negative side theta=-u, so
# d/dtheta = -d/du.
dplus = sp.diff(T_plus,u)
dminus = -sp.diff(T_minus,u)

assert dplus == 48*q**2
assert dminus == -48*q**2
assert sp.simplify(dplus-dminus) == 96*q**2

# Cusp points can be moved arbitrarily close to the maximally symmetric core
# by q -> epsilon q while theta=0.
jump_scaled = sp.factor((dplus-dminus).subs(q,eps*q))
assert jump_scaled == 96*eps**2*q**2
assert sp.limit(jump_scaled,eps,0) == 0
assert jump_scaled != 0

def main() -> None:
    print("== NPQT absolute-root C1 gate ==")
    print("T_abs = 48 q^2 |theta|")
    print(f"right derivative at theta=0: {dplus}")
    print(f"left derivative at theta=0:  {dminus}")
    print(f"derivative jump: {dplus-dminus}")
    print()
    print(f"under q -> epsilon q, jump = {jump_scaled}")
    print("It becomes small near the core but remains nonzero at every")
    print("nonzero epsilon, so no open C1 curvature neighborhood exists.")
    print("All absolute-root C1 assertions passed.")

if __name__=="__main__":
    main()
