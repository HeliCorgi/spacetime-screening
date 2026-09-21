#!/usr/bin/env python3
"""First-variation singularity of the representative QTG covariant lift.

On the regulated warped-product family
    A = eta^2 - 2 tau = delta,

the representative covariant densities satisfy
    dP/dI_Rhat3 =  1/(6 delta),
    dK/dI_Rhat3 = -1/(3 delta).

For the action
    L = H2(P) - H3(P) H + H4(P) K
        + 2 H4'(P) (H^2-T),

the potentially divergent derivative is

    dL/dI_Rhat3
      = B/(6 delta),

with, on the single-function branch P=psi, H=eta, K=R,
T=eta^2/2,

    B = H2' - eta H3' + R H4' + eta^2 H4'' - 2 H4.

Using the quasitopological subclass identities
    H2' = (H3 - 2 psi H3')/2
    H3  = 4 H4 - 4 psi H4'
implies
    H3' = -4 psi H4''

and therefore

    B = (R-2 psi) H4'
        + (eta+2 psi)^2 H4''.

Thus cancellation of the 1/delta first-variation singularity requires an
additional background condition not implied by the spherical QTG reduction.
"""

from __future__ import annotations

import sympy as sp


delta=sp.symbols("delta", nonzero=True)
R,eta,psi=sp.symbols("R eta psi", finite=True)

H2p,H3p,H4,H4p,H4pp=sp.symbols(
    "H2p H3p H4 H4p H4pp", finite=True
)

dP=1/(6*delta)
dK=-1/(3*delta)

# On the single-function branch:
# H=eta, T=eta^2/2, K=R.
LP=sp.factor(
    H2p
    - eta*H3p
    + R*H4p
    + eta**2*H4pp
)

dL=sp.factor(
    LP*dP + H4*dK
)

B=sp.factor(
    H2p
    - eta*H3p
    + R*H4p
    + eta**2*H4pp
    - 2*H4
)

assert sp.simplify(dL-B/(6*delta))==0

# Quasitopological subclass identities.
# H3'=-4 psi H4'' follows from differentiating
# H3=4 H4-4 psi H4'.
subs_qtg={
    H3p: -4*psi*H4pp,
    H2p: sp.Rational(1,2)*(
        (4*H4-4*psi*H4p)
        -2*psi*(-4*psi*H4pp)
    ),
}

B_qtg=sp.factor(B.subs(subs_qtg))
expected=sp.factor(
    (R-2*psi)*H4p
    +(eta+2*psi)**2*H4pp
)

assert sp.simplify(B_qtg-expected)==0

# GR check: constant H4 has H4'=H4''=0, so this particular divergence
# vanishes.  Nontrivial nonpolynomial H4 needs the additional condition.
assert expected.subs({H4p:0,H4pp:0})==0

# Hayward representative functions from the paper.
# A convenient dimensionless spot check M=ell=r=1 is sufficient to show
# that the extra cancellation condition is not an identity on the solution.
p,l,M,r=sp.symbols("p l M r", positive=True)

H4_hayward=(
    1
    - l**2*p/(1-l**2*p)
    + 2*l**2*p*sp.log((1-l**2*p)/p)
)

f_h=1-2*M*r**2/(r**3+2*M*l**2)
psi_h=sp.factor((1-f_h)/r**2)
eta_h=sp.factor(sp.diff(f_h,r)/r)
R_h=sp.factor(-sp.diff(f_h,r,2))

B_h=sp.factor(
    (
        (R_h-2*psi_h)*sp.diff(H4_hayward,p)
        +(eta_h+2*psi_h)**2*sp.diff(H4_hayward,p,2)
    ).subs(p,psi_h)
)

B_spot=sp.simplify(
    B_h.subs({M:1,l:1,r:1})
)
expected_spot=4+sp.Rational(16,3)*sp.log(2)
assert sp.simplify(B_spot-expected_spot)==0
assert B_spot!=0


def main():
    print("== Representative-lift action gradient ==")
    print(f"dP/dI_Rhat3 = {dP}")
    print(f"dK/dI_Rhat3 = {dK}")
    print(f"dL/dI_Rhat3 = {dL}")
    print()
    print("Potentially divergent numerator:")
    print(f"B = {B}")
    print()
    print("Using the QTG single-function identities:")
    print(f"B_QTG = {B_qtg}")
    print()
    print("Necessary cancellation condition:")
    print(
        "(R-2 psi) H4'(psi) "
        "+ (eta+2 psi)^2 H4''(psi) = 0"
    )
    print()
    print(
        "This condition is additional to the spherical QTG identities. "
        "If it is not satisfied on the background, the representative "
        "4D first variation diverges as 1/delta."
    )
    print()
    print("== Hayward spot check ==")
    print("Using the paper's H4 and units M=ell=r=1:")
    print(f"B_Hayward = {B_spot}")
    print("This is nonzero, so the cancellation condition is not an identity.")
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
