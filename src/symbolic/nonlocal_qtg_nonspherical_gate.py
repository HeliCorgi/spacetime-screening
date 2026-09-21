#!/usr/bin/env python3
"""Why the NLQT zero-free proof does not automatically extend off the proven subspace.

The quadratic NLQT operator has the schematic form

    Q = D + Dhat^dagger F(Dhat) Dhat,

with
    F(Dhat) = [exp(Omega(Dhat)) - I] / Dhat.

On the restricted subspace where
    D = Dhat = Dhat^dagger,
this factorizes as
    Q = D exp(Omega(D)),
so a zero-free exponential adds no new kernel.

For a generic nonspherical regular-BH perturbation the source states
    D != Dhat
in general.  Even in the simplified commuting/self-adjoint scalar model,
write
    D = h + delta,
    Dhat = h.

Then
    Q = delta + h exp(Omega(h)).

A zero-free exp(Omega) does not prevent Q=0 if delta is nonzero.
Thus the zero-free form factor alone is insufficient off the factorizing
subspace; one must control the operator mismatch delta D directly.

This script is a logical gate/counterexample to an overextended proof, not a
claim that the actual NLQT regular black hole contains an extra ghost.
"""

from __future__ import annotations
import sympy as sp

h,delta,gamma=sp.symbols(
    "h delta gamma", real=True, finite=True
)

Omega=gamma**2*h**2
E=sp.exp(Omega)

# Scalar commuting analogue of the generic quadratic operator.
Q=sp.factor(
    (h+delta)
    + h*((E-1)/h)*h
)

expected=sp.factor(delta+h*E)
assert sp.simplify(Q-expected)==0

# Restricted factorizing subspace delta=0.
Q_restricted=sp.factor(Q.subs(delta,0))
assert sp.simplify(Q_restricted-h*E)==0

# Off the subspace, a kernel is possible even though E is zero-free.
delta_kernel=sp.factor(-h*E)
assert sp.simplify(Q.subs(delta,delta_kernel))==0

# Relative mismatch epsilon: delta=epsilon*h.
eps=sp.symbols("epsilon", real=True, finite=True)
Qeps=sp.factor(Q.subs(delta,eps*h))
assert sp.simplify(Qeps-h*(E+eps))==0

def main():
    print("== NLQT nonspherical factorization gate ==")
    print(f"E(h) = {E}")
    print(f"Q(h,delta) = {Q}")
    print()
    print("Restricted subspace delta=0:")
    print(f"Q = {Q_restricted} = h exp(Omega(h))")
    print()
    print("Generic mismatch:")
    print("Q = delta + h exp(Omega(h))")
    print(f"kernel occurs in scalar toy model at delta = {delta_kernel}")
    print()
    print("Therefore zero-free exp(Omega) is not, by itself, a proof")
    print("of zero kernel when D != Dhat.")
    print("The required next calculation is the actual odd/even operator")
    print("mismatch DeltaD = D-Dhat on the regular-BH background.")
    print()
    print("All nonspherical NLQT gate assertions passed.")

if __name__=="__main__":
    main()
