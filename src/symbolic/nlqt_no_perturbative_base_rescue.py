#!/usr/bin/env python3
"""Perturbative NLQT cannot create a nearby new SS branch.

Published NLQT structure, restricted to SS perturbations of an SS QT vacuum:

    D = Dhat = Dhat^\dagger,

and with the zero-free entire choice,

    exp[Omega(D)] e = 0.

Since exp(entire) has no kernel,

    e = 0.

The metric perturbation then obeys the original QT linearized equation.
If the base QT theory satisfies a Birkhoff/unicity theorem, the only local
continuous SS vacuum deformation is the existing one-parameter family
(e.g. a mass shift).

This script encodes the local implicit-function logic in a finite-dimensional
analogue:
    E0(x,m)=0 defines a one-parameter base branch x=X(m).
    NLQT auxiliary equation A e=0 with det A !=0 forces e=0.
    The remaining linearized equation has only the tangent X'(m) delta m.

Therefore a bad/missing base SS branch is not perturbatively repaired by the
nonlocal completion.  A genuinely new NLQT SS branch would have to be
disconnected/nonperturbative or occur where the zero-kernel assumptions fail.
"""

from __future__ import annotations
import sympy as sp

# Simple one-dimensional analogue of a unique base branch x=m^2.
x,m=sp.symbols("x m", real=True)
dx,dm,e=sp.symbols("dx dm e", real=True)
A=sp.symbols("A", nonzero=True, finite=True)

E0=x-m**2

# Background branch.
X=m**2
assert sp.simplify(E0.subs(x,X))==0

# Linearized base equation.
dE=sp.expand(
    sp.diff(E0,x)*dx + sp.diff(E0,m)*dm
)
assert sp.simplify(dE-(dx-2*m*dm))==0

# Zero-kernel auxiliary equation A e=0.
e_solution=sp.solve(sp.Eq(A*e,0),e)[0]
assert e_solution==0

# Remaining perturbation is tangent to the base branch.
dx_solution=sp.solve(sp.Eq(dE,0),dx)[0]
assert sp.simplify(dx_solution-sp.diff(X,m)*dm)==0

def main():
    print("== Perturbative NLQT SS branch gate ==")
    print("base branch: x=X(m)=m^2")
    print(f"linearized base equation: {dE}=0")
    print(f"zero-kernel auxiliary equation -> e={e_solution}")
    print(f"remaining SS deformation: dx={dx_solution}")
    print()
    print("Interpretation:")
    print("When the NLQT exponential operator is invertible on the SS sector,")
    print("the auxiliary deformation vanishes and the metric perturbation")
    print("lies in the original QT solution family.")
    print()
    print("Thus NLQT cannot perturbatively manufacture a nearby regular SS")
    print("branch absent from the base QT theory.")
    print("All perturbative-branch assertions passed.")

if __name__=="__main__":
    main()
