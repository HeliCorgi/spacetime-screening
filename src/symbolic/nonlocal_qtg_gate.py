#!/usr/bin/env python3
"""Nonlocal-QTG principal-safety gate: exact restricted factorization.

For the nonlocal completion of arXiv:2607.07790,

    F(D) = [exp(Omega(D)) - 1] / D.

On perturbation subspaces where
    D = Dhat = Dhat^dagger,
the quadratic linearized operator factorizes schematically as

    D [1 + F(D) D] = D exp(Omega(D)).

Because exp(entire) has no finite zeros, its kernel is trivial and the
linearized kernel equals that of D: no additional pole/mode is introduced on
that restricted subspace.

The source proves this for maximally symmetric perturbations and for
spherically symmetric perturbations of spherically symmetric vacuum
backgrounds.

For generic nonspherical perturbations of a regular black hole, the paper
states D != Dhat in general, so this scalar commuting factorization cannot be
used as a proof.  That sector remains the repository's next gate.
"""

from __future__ import annotations
import sympy as sp

z = sp.symbols("z", finite=True)
gamma = sp.symbols("gamma", positive=True, finite=True)

# Representative zero-free entire choice used in the paper.
Omega = gamma**2 * z**2
E = sp.exp(Omega)

# Removable definition at z=0.
F = (E - 1) / z

effective = sp.simplify(z * (1 + F * z))
assert sp.simplify(effective - z * E) == 0

# IR normalization.
assert sp.limit(E, z, 0) == 1
assert sp.limit(F, z, 0) == 0

# The exponential multiplier is structurally zero-free.
assert E.func == sp.exp

# A polynomial truncation of the exponential generally has zeros somewhere
# in the complex plane; we do not use it as a ghost-free replacement.
x = sp.symbols("x")
E2 = 1 + x + x**2 / 2
roots = sp.solve(sp.Eq(E2, 0), x)
assert len(roots) == 2

def main():
    print("== Nonlocal-QTG restricted factorization gate ==")
    print(f"Omega(z) = {Omega}")
    print(f"E(z) = {E}")
    print(f"F(z) = {F}")
    print(f"z [1 + F(z) z] = {effective}")
    print()
    print("On a commuting/self-adjoint perturbation subspace:")
    print("kernel[z exp(Omega(z))] = kernel[z].")
    print()
    print("This passes the no-extra-pole / no-order-reduction gate only")
    print("where D=Dhat=Dhat^dagger is established.")
    print("Generic nonspherical RBH perturbations remain OPEN.")
    print()
    print("All NLQT gate assertions passed.")

if __name__ == "__main__":
    main()
