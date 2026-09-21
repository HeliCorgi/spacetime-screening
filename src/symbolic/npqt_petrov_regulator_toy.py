#!/usr/bin/env python3
"""Petrov-discriminant regulator toy for an alternative 4D NPQT representative.

The displayed 2025 NPQT cubic rational term contains N/D with
    N = W3 Z3 W2,
    D = (WZZ) W2 - 2 W3 Z2.

A covariant representative is only fixed modulo terms that vanish in the
spherical sector. Static spherical Weyl tensors are Petrov type D, so the
Weyl speciality discriminant vanishes there.

In the purely-electric Weyl family used by
npqt_explicit_singular_direction.py,

    Delta_W = W2^3 - 12 W3^2
            = 1024 (e1-e2)^2 (e1+2e2)^2 (2e1+e2)^2.

It vanishes whenever two Weyl eigenvalues coincide (type-D/O pattern), but is
strictly nonzero at the explicit type-I singular direction (e1,e2,e3)=(1,5,-6).

A toy spherical-equivalent replacement is

    R_mu = N D / [D^2 + mu Delta_W Z2^2].

All terms have the same curvature degree:
    deg(ND)=13,
    deg(D^2)=deg(Delta_W Z2^2)=10,
so R_mu remains homogeneous degree 3.

On the type-D spherical locus Delta_W=0 and D !=0:
    R_mu=N/D.

At the explicit off-spherical D=0, Delta_W !=0, Z2 !=0 point:
    R_mu=0,
so that particular pole is removed.

This is NOT yet a full solution: simultaneous zeros
    D=Delta_W=0
or the full complex Petrov-speciality locus can still cause singularities.
The script only demonstrates that spherical-equivalent covariant
regularization is algebraically possible in principle.
"""

from __future__ import annotations
import sympy as sp

e1,e2=sp.symbols("e1 e2", real=True)
z0,z1,z2=sp.symbols("z0 z1 z2", real=True)
mu=sp.symbols("mu", positive=True, finite=True)

e3=-e1-e2
z3=-z0-z1-z2

W2=sp.factor(16*(e1**2+e1*e2+e2**2))
W3=sp.factor(48*e1*e2*(e1+e2))
Z2=sp.factor(z0**2+z1**2+z2**2+z3**2)
Z3=sp.factor(z0**3+z1**3+z2**3+z3**3)
WZZ=sp.factor(
    -2*(
        e1*z0**2+2*e1*z0*z1-2*e1*z1*z2-e1*z2**2
        +e2*z0**2+2*e2*z0*z2-e2*z1**2-2*e2*z1*z2
    )
)
D=sp.factor(WZZ*W2-2*W3*Z2)
N=sp.factor(W3*Z3*W2)

DeltaW=sp.factor(W2**3-12*W3**2)
expected_Delta=sp.factor(
    1024*(e1-e2)**2*(e1+2*e2)**2*(2*e1+e2)**2
)
assert sp.simplify(DeltaW-expected_Delta)==0

Rmu=sp.factor(
    N*D/(D**2+mu*DeltaW*Z2**2)
)

# Type-D electric-Weyl pattern: e2=e3 -> e1=-2 e2.
q=sp.symbols("q", nonzero=True, real=True)
typeD={e1:-2*q,e2:q}
assert sp.simplify(DeltaW.subs(typeD))==0

# Wherever D !=0 on this locus, regulated ratio equals original N/D.
difference=sp.factor(
    (Rmu-N/D).subs(typeD)
)
assert sp.simplify(difference)==0

# Explicit singular direction from previous script.
z0_star=sp.factor(-1+8*sp.sqrt(61)/61)
point={
    e1:1,e2:5,z0:z0_star,z1:1,z2:1
}
Dstar=sp.simplify(D.subs(point))
Nstar=sp.simplify(N.subs(point))
Delstar=sp.simplify(DeltaW.subs(point))
Z2star=sp.simplify(Z2.subs(point))
Rstar=sp.simplify(Rmu.subs(point))

assert Dstar==0
assert Nstar!=0
assert Delstar==97140736
assert Z2star!=0
assert Rstar==0

# Homogeneity check under common curvature scaling.
eps=sp.symbols("epsilon", positive=True, finite=True)
# invariant degrees: W2 2, W3 3, Z2 2, Z3 3, WZZ 3
# D degree 5, N degree 8, DeltaW degree 6.
scale_ratio=sp.factor(
    (eps**8*N)*(eps**5*D)
    /(
        (eps**5*D)**2
        +mu*(eps**6*DeltaW)*(eps**2*Z2)**2
    )
)
assert sp.simplify(scale_ratio-eps**3*Rmu)==0

def main():
    print("== Petrov-discriminant regulator toy ==")
    print(f"Delta_W = {DeltaW}")
    print()
    print("Type-D locus e1=-2q,e2=q:")
    print(f"Delta_W = {sp.simplify(DeltaW.subs(typeD))}")
    print("R_mu = N/D wherever D != 0.")
    print()
    print("Explicit former pole direction:")
    print(f"D = {Dstar}")
    print(f"N = {Nstar}")
    print(f"Delta_W = {Delstar}")
    print(f"Z2 = {Z2star}")
    print(f"R_mu = {Rstar}")
    print()
    print("Homogeneity:")
    print("R_mu(epsilon curvature) = epsilon^3 R_mu.")
    print()
    print("Conclusion: an invariant that vanishes on the spherical/type-D")
    print("locus can remove this specific off-spherical pole without changing")
    print("the spherical ratio. Simultaneous-zero loci remain to be analyzed.")
    print("All regulator-toy assertions passed.")

if __name__=="__main__":
    main()
