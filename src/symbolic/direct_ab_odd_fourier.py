#!/usr/bin/env python3
"""Algorithmic local Fourier derivation of the direct odd principal action.

This script independently reconstructs the local principal sector from the
original action by generating the linearized Einstein tensor in a Minkowski
orthonormal frame.

Coordinates:
    x^mu = (t, x, y, z),
    eta = diag(-1,1,1,1).

Odd metric polarization:
    h_ty = Q,
    h_xy = H.

Fourier covector for exp[-i omega t + i k x]:
    p_mu = (-omega, k, 0, 0).

The script computes delta G_{mu nu} from the standard linearized Einstein
formula, raises indices, derives the Einstein-Hilbert quadratic form

    L_EH^(2) = -1/2 h_{mu nu} delta G^{mu nu},

and then contracts the second-order cross term of

    alpha G^{mu nu} W_mu W_nu

with a null background one-form
    W_mu = w (1,1,0,0)
and an odd vector perturbation delta W_y=u.

For the original A-B action
    alpha_A = +4 ell^2,
    alpha_B = -4 ell^2.

The result reproduces directly

    L_pr = 1/2 X^2 + Z X,

with X the odd metric field strength and
    Z ∝ a D u_A - b D u_B,
without importing any generalized-Proca perturbation coefficient.
"""

from __future__ import annotations

import sympy as sp


omega,k,Q,H=sp.symbols(
    "omega k Q H", real=True
)
u,v,a,b,ell=sp.symbols(
    "u v a b ell", real=True, finite=True
)

eta=sp.diag(-1,1,1,1)

# Symmetric odd metric perturbation h_{mu nu}.
h=sp.zeros(4)
h[0,2]=h[2,0]=Q
h[1,2]=h[2,1]=H

# Fourier covector p_mu for exp[-i omega t + i k x].
p=sp.Matrix([-omega,k,0,0])
p_up=eta*p
p2=sp.factor(p_up.dot(p))

h_updown=eta*h
h_upup=eta*h*eta
trace=sp.factor(
    sum(
        eta[i,j]*h[i,j]
        for i in range(4)
        for j in range(4)
    )
)

# Linearized Einstein tensor:
# delta G_{mu nu}
# = 1/2(
#   partial_a partial_mu h^a_nu
#  +partial_a partial_nu h^a_mu
#  -box h_mu_nu
#  -partial_mu partial_nu h
#  -eta_mu_nu(partial_a partial_b h^ab - box h)
# )
#
# In Fourier space partial_mu partial_nu -> -p_mu p_nu.
G=sp.zeros(4)

for mu in range(4):
    for nu in range(4):
        term1=sum(
            (-p[alpha]*p[mu])*h_updown[alpha,nu]
            for alpha in range(4)
        )
        term2=sum(
            (-p[alpha]*p[nu])*h_updown[alpha,mu]
            for alpha in range(4)
        )
        term3=p2*h[mu,nu]
        term4=p[mu]*p[nu]*trace

        divdiv=sum(
            (-p[alpha]*p[beta])*h_upup[alpha,beta]
            for alpha in range(4)
            for beta in range(4)
        )
        boxtrace=-p2*trace

        term5=-eta[mu,nu]*(divdiv-boxtrace)

        G[mu,nu]=sp.factor(
            sp.Rational(1,2)
            *(term1+term2+term3+term4+term5)
        )

Gup=sp.simplify(eta*G*eta)

# Fourier amplitude of X = dot H - Q':
# dot -> -i omega, prime -> +i k,
# so X_fourier = i*(-omega H-k Q).
Xamp=sp.factor(-omega*H-k*Q)

assert sp.simplify(
    Gup[0,2]-k*Xamp/2
)==0
assert sp.simplify(
    Gup[1,2]-omega*Xamp/2
)==0

# EH second-order action coefficient.
LEH=sp.factor(
    -sp.Rational(1,2)
    *sum(
        h[mu,nu]*Gup[mu,nu]
        for mu in range(4)
        for nu in range(4)
    )
)

assert sp.simplify(
    LEH-sp.Rational(1,2)*Xamp**2
)==0

# One-vector cross term from alpha G^{mu nu} W_mu W_nu.
# At O(eps^2):
#   2 alpha delta G^{a y} Wbar_a delta W_y.
#
# For the local null background Wbar_a=w(1,1):
def cross_term(alpha, w, amp):
    return sp.factor(
        2*alpha*amp*w*(Gup[0,2]+Gup[1,2])
    )

alphaA=4*ell**2
alphaB=-4*ell**2

LA_cross=cross_term(alphaA,a,u)
LB_cross=cross_term(alphaB,b,v)
Lcross=sp.factor(LA_cross+LB_cross)

expected_cross=sp.factor(
    4*ell**2*(omega+k)*(a*u-b*v)*Xamp
)
assert sp.simplify(Lcross-expected_cross)==0

# In position space (up to the common Fourier i convention):
# (omega+k) u corresponds to -(d_t-d_x)u, so this is the same
# Z X structure used in the direct real-space scripts.

# Velocity-symbol Hessian check.
# Use real principal variables:
Ht,ut,vt,Qx,ux,vx=sp.symbols(
    "H_t u_t v_t Q_x u_x v_x", real=True
)
Xreal=Ht-Qx
Zreal=sp.factor(
    4*ell**2*(a*(ux-ut)-b*(vx-vt))
)
Lreal=sp.expand(
    sp.Rational(1,2)*Xreal**2
    +Zreal*Xreal
)

Hvel=sp.hessian(Lreal,(Ht,ut,vt))
detH=sp.factor(Hvel.det())

assert detH==0

# The null velocity direction is (0,b,a).
null=sp.Matrix([0,b,a])
assert sp.simplify(Hvel*null)==sp.zeros(3,1)

# Two nonzero eigenvalues have opposite sign because a 2x2 principal minor
# is negative.
minor=sp.factor(
    Hvel.extract([0,1],[0,1]).det()
)
assert sp.simplify(
    minor + (4*ell**2*a)**2
)==0


def main():
    print("== Algorithmic linearized Einstein tensor ==")
    print(f"p^2 = {p2}")
    print(f"trace(h) = {trace}")
    print(f"delta G^ty = {Gup[0,2]}")
    print(f"delta G^xy = {Gup[1,2]}")
    print(f"X_fourier = {Xamp}")
    print()
    print("== Direct Einstein-Hilbert quadratic form ==")
    print(f"L_EH^(2) = {LEH}")
    print("= 1/2 X^2")
    print()
    print("== Direct original A-B cross term ==")
    print(f"A-sector = {LA_cross}")
    print(f"B-sector = {LB_cross}")
    print(f"sum = {Lcross}")
    print()
    print("Position-space principal structure:")
    print("L_pr = 1/2 X^2")
    print("     + 4 ell^2 [a(u'-udot)-b(v'-vdot)] X")
    print()
    print("== Velocity Hessian ==")
    print(Hvel)
    print(f"det = {detH}")
    print(f"negative 2x2 minor = {minor}")
    print("null velocity direction = (0,b,a)")
    print()
    print(
        "Conclusion: the indefinite odd kinetic structure follows directly "
        "from the original Einstein-Hilbert plus G^{mu nu}W_mu W_nu action "
        "at principal order, with no generalized-Proca coefficient mapping."
    )
    print("All algorithmic direct-action assertions passed.")


if __name__=="__main__":
    main()
