#!/usr/bin/env python3
"""Dipole (l=1) odd-sector ghost diagnostic for the two-vector benchmark.

For l=1, L=l(l+1)=2, so every term proportional to (L-2) in the standard
odd-parity quadratic action vanishes.  The metric axial dipole does not carry
a local gravitational-wave degree of freedom.

At principal derivative order the two-vector action is therefore

    L_pr = C1 X^2 + 2 Y X,

    X = dot W - Q' + 2Q/r,
    Y = c^T dot u + d^T u',

with no direct Maxwell-type vector kinetic/gradient terms in this model.

Completing the square gives

    L_pr = C1 (X + Y/C1)^2 - Y^2/C1.

The first square is the nondynamical metric-dipole combination.  On the null
regular branch d=-f c, leaving the local physical derivative term

    L_vec,pr = -(1/C1) [ c^T (dot u - f u') ]^2.

For C1>0 outside the metric horizon, the one derivative-active vector
combination has a negative kinetic energy.  The combination orthogonal to c
has no principal quadratic operator.

This is a cleaner ghost diagnostic than the l>=2 tensor analysis because no
propagating odd gravitational mode exists at l=1.

Caveat: this is the principal derivative sector.  The complete lower-
derivative dipole constraint algebra should still be written explicitly for a
publication-level theorem, but lower-derivative terms cannot flip the sign of
a nonzero high-frequency kinetic coefficient.
"""

from __future__ import annotations

import sympy as sp


C1,f=sp.symbols("C1 f", positive=True, finite=True)
cA,cB=sp.symbols("c_A c_B", real=True)
udA,udB,urA,urB,X=sp.symbols(
    "udot_A udot_B uprime_A uprime_B X",
    real=True,
)

Y=sp.expand(
    cA*(udA-f*urA)
    +cB*(udB-f*urB)
)

L=sp.expand(C1*X**2+2*Y*X)
L_completed=sp.expand(
    C1*(X+Y/C1)**2 - Y**2/C1
)
assert sp.simplify(L-L_completed)==0

Lred=sp.factor(-Y**2/C1)

# Velocity Hessian in the two vector perturbations.
vel=(udA,udB)
H=sp.Matrix([
    [sp.diff(Lred,vi,vj) for vj in vel]
    for vi in vel
])

expected_H=sp.Matrix([
    [-2*cA**2/C1,-2*cA*cB/C1],
    [-2*cA*cB/C1,-2*cB**2/C1],
])
assert sp.simplify(H-expected_H)==sp.zeros(2)

tr=sp.factor(sp.trace(H))
det=sp.factor(H.det())
assert det==0
assert sp.simplify(
    tr+2*(cA**2+cB**2)/C1
)==0

epar=sp.Matrix([cA,cB])
eperp=sp.Matrix([-cB,cA])
assert sp.simplify(H*eperp)==sp.zeros(2,1)
assert sp.simplify(H*epar-tr*epar)==sp.zeros(2,1)

# Normalize the derivative-active mode locally:
# y=(c.u)/sqrt(c^2), so L=-c^2/C1 (dot y - f y')^2.
c2=sp.factor(cA**2+cB**2)
Aghost=sp.factor(c2/C1)

ydot,yprime,p=sp.symbols(
    "ydot yprime p", real=True
)
Lmode=sp.expand(-Aghost*(ydot-f*yprime)**2)
pmode=sp.diff(Lmode,ydot)
assert sp.simplify(
    pmode+2*Aghost*(ydot-f*yprime)
)==0

# Legendre transform.
ydot_sol=sp.solve(sp.Eq(p,pmode),ydot)[0]
Hamiltonian=sp.factor(
    (p*ydot-Lmode).subs(ydot,ydot_sol)
)
expected_Ham=sp.factor(
    -p**2/(4*Aghost)+f*p*yprime
)
assert sp.simplify(Hamiltonian-expected_Ham)==0

# Principal EOM has double one-way null characteristic.
omega,k=sp.symbols("omega k", real=True)
principal=sp.factor(
    -Aghost*(omega+f*k)**2
)


def main():
    print("== l=1 odd principal action ==")
    print(f"Y = {Y}")
    print(f"L_reduced = {Lred}")
    print()
    print("velocity Hessian =")
    print(H)
    print(f"trace = {tr}")
    print(f"det = {det}")
    print()
    print(
        "For nonzero vector-metric mixing c, the derivative-active "
        "combination has a strictly negative kinetic eigenvalue."
    )
    print("The orthogonal vector combination has zero principal kinetic term.")
    print()
    print("== Normalized active mode ==")
    print(f"A_ghost = {Aghost}")
    print(f"L_mode = {Lmode}")
    print(f"canonical Hamiltonian density = {Hamiltonian}")
    print(
        "The quadratic momentum term is -p^2/(4 A_ghost), hence unbounded "
        "below for A_ghost>0."
    )
    print()
    print("principal Fourier factor =",principal)
    print("characteristic: omega = -f k (double)")
    print()
    print(
        "This gives an l=1 high-frequency ghost diagnostic independent of "
        "the l>=2 gravitational-wave characteristic question."
    )
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
