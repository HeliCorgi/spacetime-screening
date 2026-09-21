#!/usr/bin/env python3
"""Principal-safety gate for analytic 4D Class-II / GQTG resummations.

This combines two repository results:

1. Every finite genuine 4D GQTG curvature order contributes O(r^3) to the
   integrated spherical equation at a regular de Sitter-type core.

2. If a nonzero mass M0 is to survive while a finite curvature variable c(r)
   approaches c_* as
       c-c_* = a r^p + ...,
   then the resummed spherical response must scale as
       G(c) ~ |c-c_*|^{-3/p}.

This script records the resulting derivative scaling:
       G'  ~ |dc|^{-3/p-1}
       G'' ~ |dc|^{-3/p-2}.

These divergences are a gate, not by themselves a proof that the fundamental
4D action is singular: the resummed spherical response need not equal a local
action coefficient.  A viable candidate must show how its full quadratic
operator remains finite/nondegenerate despite this nonuniform resummation.

Local analytic Class-II / GQTG additionally has the known reduced-spectrum
strong-coupling issue; that literature input is documented in the note, not
proved by this script.
"""

from __future__ import annotations
import sympy as sp

dc, a, p, M0 = sp.symbols(
    "Delta_c a p M0", positive=True, finite=True
)

alpha = sp.factor(sp.Rational(3, 1) / p)
G = sp.factor(M0 * a**alpha * dc**(-alpha))
Gp = sp.factor(sp.diff(G, dc))
Gpp = sp.factor(sp.diff(Gp, dc))

assert sp.simplify(
    Gp + alpha * G / dc
) == 0

assert sp.simplify(
    Gpp - alpha * (alpha + 1) * G / dc**2
) == 0

# Representative approaches.
pvals = {
    1: sp.Integer(3),
    2: sp.Rational(3, 2),
    3: sp.Integer(1),
}

for pp, aa in pvals.items():
    assert sp.simplify(alpha.subs(p, pp) - aa) == 0

def main():
    print("== Analytic Class-II / GQTG resummation gate ==")
    print(f"required response G(dc) = {G}")
    print(f"alpha = {alpha}")
    print(f"G'(dc) = {Gp}")
    print(f"G''(dc) = {Gpp}")
    print()
    print("Thus a nonzero-mass finite-curvature core requires a nonuniform")
    print("resummation whose spherical response and its derivatives become")
    print("singular as the limiting curvature is approached.")
    print()
    print("This does NOT by itself prove a singular 4D action.")
    print("Gate requirement: demonstrate a finite physical quadratic/principal")
    print("operator after the infinite tower is resummed.")
    print()
    print("All Class-II resummation-gate assertions passed.")

if __name__ == "__main__":
    main()
