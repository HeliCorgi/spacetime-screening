#!/usr/bin/env python3
"""Explicit Lorentzian algebraic-curvature singular direction for 4D NPQT.

The 2025 four-dimensional NPQT representative uses the common denominator

    D = (WZZ) W2 - 2 W3 Z2,

with
    W2  = W_ab{}^{cd} W_cd{}^{ab},
    W3  = W_ab{}^{cd} W_cd{}^{ef} W_ef{}^{ab},
    Z2  = Z_a{}^b Z_b{}^a,
    Z3  = Z_a{}^b Z_b{}^c Z_c{}^a,
    WZZ = W_ab{}^{cd} Z_c{}^a Z_d{}^b.

Its cubic representative contains the rational numerator
    N3 = W3 Z3 W2
(up to the overall coefficient 9/2).

We construct an actual real Lorentzian algebraic curvature direction for
which
    D=0
but
    N3 != 0.

Weyl tensor:
take a purely electric Weyl tensor in an orthonormal Lorentzian frame, with
electric eigenvalues
    (e1,e2,e3),  e3=-e1-e2.

Traceless Ricci:
take mixed eigenvalues
    (z0,z1,z2,z3),  z3=-z0-z1-z2.

For this algebraic family the invariants reduce to the closed expressions
implemented below.

At
    e1=1, e2=5,
    z1=z2=1,
    z0=-1+8/sqrt(61),
we find exactly
    D=0,
    Z3=-384/61,
    W2=496,
    W3=1440,
so
    N3=-274268160/61 !=0.

Scaling W,Z -> epsilon W, epsilon Z approaches an arbitrary maximally
symmetric curvature point while remaining on the denominator-zero ray.
Therefore the displayed cubic rational representative has no open
neighborhood on which that formula is defined.

This does not prove that every possible NPQT representative is singular; it
rules out this displayed representative as an immediately usable 4D NLQT
base without a different covariant completion.
"""

from __future__ import annotations
import sympy as sp

e1,e2=sp.symbols("e1 e2", real=True)
z0,z1,z2=sp.symbols("z0 z1 z2", real=True)

# Pure-electric Weyl and diagonal traceless-Ricci invariants in signature
# (-,+,+,+).  e3 and z3 are fixed by tracelessness.
e3=-e1-e2
z3=-z0-z1-z2

W2=sp.factor(
    16*(e1**2+e1*e2+e2**2)
)

W3=sp.factor(
    48*e1*e2*(e1+e2)
)

Z2=sp.factor(
    z0**2+z1**2+z2**2+z3**2
)

Z3=sp.factor(
    z0**3+z1**3+z2**3+z3**3
)

WZZ=sp.factor(
    -2*(
        e1*z0**2
        +2*e1*z0*z1
        -2*e1*z1*z2
        -e1*z2**2
        +e2*z0**2
        +2*e2*z0*z2
        -e2*z1**2
        -2*e2*z1*z2
    )
)

D=sp.factor(WZZ*W2-2*W3*Z2)
N3=sp.factor(W3*Z3*W2)

# Explicit real Lorentzian algebraic curvature direction.
z0_star=sp.factor(
    -1+8*sp.sqrt(61)/61
)

point={
    e1:sp.Integer(1),
    e2:sp.Integer(5),
    z0:z0_star,
    z1:sp.Integer(1),
    z2:sp.Integer(1),
}

Dstar=sp.simplify(D.subs(point))
W2star=sp.simplify(W2.subs(point))
W3star=sp.simplify(W3.subs(point))
Z2star=sp.simplify(Z2.subs(point))
Z3star=sp.simplify(Z3.subs(point))
N3star=sp.simplify(N3.subs(point))

assert Dstar==0
assert W2star==496
assert W3star==1440
assert Z3star==-sp.Rational(384,61)
assert N3star==-sp.Rational(274268160,61)
assert N3star!=0

# Homogeneous scaling toward a maximally symmetric point.
eps=sp.symbols("epsilon", positive=True, finite=True)

# W2~eps^2, W3~eps^3, Z2~eps^2, Z3~eps^3, WZZ~eps^3.
D_scaled=sp.factor(
    eps**5*Dstar
)
N_scaled=sp.factor(
    eps**8*N3star
)

assert D_scaled==0
assert N_scaled!=0

# Nearby off-zero direction: perturb the WZZ invariant so that
# D = eps^5 delta while N~eps^8.  If delta=eps^4, the ratio diverges as 1/eps.
delta=sp.symbols("delta", positive=True, finite=True)
ratio_model=sp.factor(
    eps**8*N3star/(eps**5*delta)
)
ratio_tuned=sp.factor(
    ratio_model.subs(delta,eps**4)
)
assert sp.simplify(
    sp.limit(eps*ratio_tuned,eps,0)-N3star
)==0

def main():
    print("== Explicit Lorentzian NPQT denominator-zero direction ==")
    print(f"eigenvalues E = (1,5,-6)")
    print(f"z0 = {z0_star}")
    print("mixed Z eigenvalues = (z0,1,1,-z0-2)")
    print()
    print(f"W2 = {W2star}")
    print(f"W3 = {W3star}")
    print(f"Z2 = {Z2star}")
    print(f"Z3 = {Z3star}")
    print(f"D_NPQT = {Dstar}")
    print(f"N3 = W3 Z3 W2 = {N3star}")
    print()
    print("Thus the displayed cubic rational term has denominator zero")
    print("while its numerator is nonzero on a real Lorentzian algebraic")
    print("curvature direction.")
    print()
    print("Under W,Z -> epsilon(W,Z), the same singular ray approaches")
    print("arbitrarily close to a maximally symmetric curvature point.")
    print()
    print(f"nearby tuned ratio model = {ratio_tuned}")
    print("so a path with denominator coefficient delta~epsilon^4 gives")
    print("a 1/epsilon divergence.")
    print()
    print("Conclusion: fixed-ray O(epsilon^3) counting does not rescue")
    print("the displayed cubic NPQT representative on an open neighborhood.")
    print("All explicit NPQT singular-direction assertions passed.")

if __name__=="__main__":
    main()
