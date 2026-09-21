#!/usr/bin/env python3
"""Direct specialization of published odd-parity coefficients.

Source:
Kase, Minamitsuji, Tsujikawa, Zhang,
JCAP 02 (2018) 048, arXiv:1801.01787.

Their generalized-Proca action includes a canonical Maxwell term F explicitly:
    S = ∫ sqrt(-g) [ F + sum_i L_i ].

To map the present auxiliary-vector model, the Maxwell term must therefore be
cancelled through
    G2 = -F + 24 sigma ell^2 X^2,
where sigma=+1 for A and sigma=-1 for B.

The remaining functions are
    G3 = -16 sigma ell^2 X,
    G4 = G4_EH + 4 sigma ell^2 X,
    G5=G6=g5=0.

On the null branch X=0 with h=f and A1=A0/f, Appendix-C coefficients reduce to
    C2 = -beta A0/(2 f r^2),
    C3 =  beta A0/(2 r^2) = -f C2,
    C5=C6=C7=0,
while the quartic vector contributions to C8,C9,C10 are the ones used by the
repo's odd-principal calculations.

This script is the source-formula cross-check that was previously missing.
"""

from __future__ import annotations

import sympy as sp


r,f,A0,beta,G40=sp.symbols(
    "r f A0 beta G40", nonzero=True, finite=True
)

h=f
A1=A0/f
X=sp.Integer(0)

# Mapping data.
G2F=-1                   # cancels the explicit canonical Maxwell F
G4=G40                   # value at X=0
G4X=beta
G4XX=0

# Other generalized-Proca functions absent.
G5X=0
G6=0
G6X=0
g5=0

# Appendix C coefficients specialized to G5=G6=g5=0.
C1=sp.factor(
    h*(r*G4-2*r*X*G4X)/(2*r**3*f)
)

C2=sp.factor(
    -h*(2*r*f*A1*G4X)/(4*r**3*f**2)
)

C3=sp.factor(
    h*(r*A0*G4X)/(2*r**3*f)
)

C5=sp.factor(
    (r*(1+G2F))/(2*r**3*f)
)

C6=sp.Integer(0)

C7=sp.factor(
    -h*(r*f*(1+G2F))/(2*r**3*f)
)

C8=sp.factor(
    -h*(2*f*G4+2*f*h*A1**2*G4X)/(4*r**4*f)
)

C9=sp.factor(
    h*(2*f*A1*G4X)/(2*r**4*f)
)

C10=sp.factor(
    (2*f**2*G4-2*f*A0**2*G4X)/(4*r**4*f**3)
)

C11=sp.factor(
    -(4*f**2*A0*G4X)/(4*r**4*f**3)
)

expected={
    "C1": G40/(2*r**2),
    "C2": -beta*A0/(2*f*r**2),
    "C3": beta*A0/(2*r**2),
    "C5": 0,
    "C6": 0,
    "C7": 0,
    "C8": -(f*G40+beta*A0**2)/(2*r**4),
    "C9": beta*A0/r**4,
    "C10": (f*G40-beta*A0**2)/(2*f**2*r**4),
    "C11": -beta*A0/(f*r**4),
}

actual={
    "C1":C1,"C2":C2,"C3":C3,"C5":C5,"C6":C6,"C7":C7,
    "C8":C8,"C9":C9,"C10":C10,"C11":C11,
}

for name,val in actual.items():
    assert sp.simplify(val-expected[name])==0

assert sp.simplify(C3+f*C2)==0

# One-vector no-ghost coefficient from Eq. (39):
q2=sp.factor((C1*C5-C2**2)/C1)
expected_q2=sp.factor(
    -beta**2*A0**2/(2*G40*f**2*r**2)
)
assert sp.simplify(q2-expected_q2)==0

# Split C8/C10 into EH and vector parts.  For the two-vector model the EH
# contribution is included once and vector parts are additive.
C8_EH=sp.factor(C8.subs(beta,0))
C8_vec=sp.factor(C8-C8_EH)
C10_EH=sp.factor(C10.subs(beta,0))
C10_vec=sp.factor(C10-C10_EH)

assert sp.simplify(C8_EH+f*G40/(2*r**4))==0
assert sp.simplify(C8_vec+beta*A0**2/(2*r**4))==0
assert sp.simplify(C10_EH-G40/(2*f*r**4))==0
assert sp.simplify(C10_vec+beta*A0**2/(2*f**2*r**4))==0


def main():
    print("== Generalized-Proca mapping correction ==")
    print("Published action contains canonical Maxwell F explicitly.")
    print("Our model requires G2,F = -1 to cancel it.")
    print()
    for name in ["C1","C2","C3","C5","C6","C7","C8","C9","C10","C11"]:
        print(f"{name} = {actual[name]}")
    print()
    print(f"C3 + f C2 = {sp.simplify(C3+f*C2)}")
    print(f"q2 = {q2}")
    print()
    print("For G40>0, f>0 and beta*A0 !=0, q2<0.")
    print("This is exactly the published odd no-ghost diagnostic specialized")
    print("to a vector sector whose canonical Maxwell kinetic term is cancelled.")
    print()
    print("All source-formula specialization assertions passed.")


if __name__=="__main__":
    main()
