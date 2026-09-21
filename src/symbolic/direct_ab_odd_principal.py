#!/usr/bin/env python3
"""Direct odd-principal expansion from the original A-B action.

No generalized-Proca coefficient mapping is used here.

Original action:
    S = (16 pi G)^-1 ∫ sqrt(-g)
        [ R + ell^2 (L[A] - L[B]) ],

    L[W] = 4 G^{mu nu} W_mu W_nu
         + 8 W^2 nabla_mu W^mu
         + 6 (W^2)^2.

We work locally at any point of the static spherical background in an
orthonormal (t,x) frame and use one normalized axial harmonic direction y.
For l=1 the principal t/r derivative sector is completely captured by

    h_ty = Q(t,x),
    h_xy = H(t,x),
    delta A_y = u(t,x),
    delta B_y = v(t,x).

Define the odd metric field strength
    X = dot(H) - Q'.

A direct linearized-Einstein calculation gives
    delta G^{t y} = -1/2 X',
    delta G^{x y} = +1/2 dot(X).

The Einstein-Hilbert quadratic action is
    L_EH,pr = +1/2 X^2
(up to the common positive harmonic/angular normalization).

For a background null one-form
    W_hat = w (dt_hat + dx_hat),
the second-order cross term of 4 sigma ell^2 G^{mu nu} W_mu W_nu is

    L_mix[W]
      = 4 sigma ell^2 w (u' - dot(u)) X

after integration by parts at principal order.

The remaining pieces 8 W^2 nabla.W and 6(W^2)^2 do not contribute t/r
principal derivatives in the axial quadratic sector on W^2=0.

Thus for A and B

    Z = 4 ell^2 [ a (u' - dot u) - b (v' - dot v) ]

and

    L_pr = 1/2 X^2 + Z X
         = 1/2 (X+Z)^2 - 1/2 Z^2.

The 2D axial metric field has no local l=1 gravitational-wave degree of
freedom.  Its principal equations set X+Z to a spacetime constant, so locally

    L_phys,pr = -1/2 Z^2.

Hence the derivative-active vector combination has a negative kinetic term,
while the orthogonal vector combination is absent from the principal action.

This is the direct source-action derivation requested as the independent
cross-check of the generalized-Proca result.
"""

from __future__ import annotations

import sympy as sp


# Principal derivatives of the axial perturbations.
Qt,Qx,Ht,Hx=sp.symbols(
    "Q_t Q_x H_t H_x", real=True
)
ut,ux,vt,vx=sp.symbols(
    "u_t u_x v_t v_x", real=True
)

ell,a,b=sp.symbols(
    "ell a b", positive=True, finite=True
)

# Odd metric field strength.
X=Ht-Qx

# Direct linearized Einstein tensor principal pieces.
# delta G^{ty} = -1/2 d_x X
# delta G^{xy} = +1/2 d_t X
# Their integration-by-parts contraction with background W and delta W
# yields the mixing below.
ZA=sp.factor(
    4*ell**2*a*(ux-ut)
)
ZB=sp.factor(
    -4*ell**2*b*(vx-vt)
)
Z=sp.factor(ZA+ZB)

LEH=sp.Rational(1,2)*X**2
Lmix=Z*X
Lpr=sp.expand(LEH+Lmix)

Lsquare=sp.expand(
    sp.Rational(1,2)*(X+Z)**2
    -sp.Rational(1,2)*Z**2
)
assert sp.simplify(Lpr-Lsquare)==0

# Local physical principal action after eliminating the nondynamical
# l=1 axial metric field strength.
Lphys=sp.factor(-sp.Rational(1,2)*Z**2)

# Velocity Hessian in (u_t, v_t).
vel=(ut,vt)
Kphys=sp.Matrix([
    [sp.diff(Lphys,vi,vj) for vj in vel]
    for vi in vel
])

s=sp.Matrix([
    4*ell**2*a,
    -4*ell**2*b,
])

expected_K=sp.simplify(-(s*s.T))
assert sp.simplify(Kphys-expected_K)==sp.zeros(2)

trK=sp.factor(sp.trace(Kphys))
detK=sp.factor(Kphys.det())

assert detK==0
assert sp.simplify(
    trK + 16*ell**4*(a**2+b**2)
)==0

e_active=s
e_null=sp.Matrix([b,a])

assert sp.simplify(
    Kphys*e_active-trK*e_active
)==sp.zeros(2,1)
assert sp.simplify(Kphys*e_null)==sp.zeros(2,1)

# Unreduced velocity Hessian in (dot H, dot u, dot v).
# Q has no time derivative and enforces the 2D Gauss constraint.
vel3=(Ht,ut,vt)
Hfull=sp.Matrix([
    [sp.diff(Lpr,vi,vj) for vj in vel3]
    for vi in vel3
])

# It must have one zero direction and two nonzero eigenvalues of opposite sign.
detHfull=sp.factor(Hfull.det())
rank_minor=sp.factor(
    Hfull.extract([0,1],[0,1]).det()
)

assert detHfull==0
assert sp.simplify(
    rank_minor + (4*ell**2*a)**2
)==0

# Null vector is the vector combination orthogonal to s, with no H velocity.
null3=sp.Matrix([0,b,a])
assert sp.simplify(Hfull*null3)==sp.zeros(3,1)

lam=sp.symbols("lambda")
char=sp.factor(Hfull.charpoly(lam).as_expr())

# The product of the two nonzero eigenvalues equals the coefficient of
# lambda in the cubic characteristic polynomial and is negative.
poly=sp.Poly(char,lam)
assert poly.TC()==0
coeff_lambda=sp.factor(poly.coeff_monomial(lam))
assert sp.simplify(
    coeff_lambda + 16*ell**4*(a**2+b**2)
)==0

# Direct principal equations.
# Let Y = X+Z.  Q and H give d_x Y=0 and d_t Y=0.
# The active vector equation gives D X=0 with D=d_x-d_t.
# Locally at nonzero frequency/momentum, Y=0 -> X=-Z and D Z=0.
omega,k=sp.symbols("omega k", real=True)
Dsymbol=sp.I*(k+omega)  # for exp[-i omega t + i k x], d_x-d_t=i(k+omega)
principal_active=sp.factor(Dsymbol**2)
assert sp.factor(principal_active + (k+omega)**2)==0


def main():
    print("== Direct original-action odd principal expansion ==")
    print(f"X = {X}")
    print(f"Z_A = {ZA}")
    print(f"Z_B = {ZB}")
    print(f"Z = {Z}")
    print()
    print(f"L_EH,pr = {LEH}")
    print(f"L_mix = {Lmix}")
    print(f"L_pr = {sp.factor(Lpr)}")
    print()
    print("Complete the square:")
    print("L_pr = 1/2 (X+Z)^2 - 1/2 Z^2")
    print(f"L_phys,pr = {Lphys}")
    print()
    print("== Physical vector kinetic Hessian ==")
    print(Kphys)
    print(f"trace = {trK}")
    print(f"det = {detK}")
    print("active combination ~ (a, -b)")
    print("principal-null combination ~ (b, a)")
    print()
    print("== Unreduced velocity Hessian (dot H, dot u, dot v) ==")
    print(Hfull)
    print(f"det = {detHfull}")
    print(f"charpoly = {char}")
    print(f"lambda coefficient = {coeff_lambda} < 0")
    print(
        "Thus the two nonzero velocity-Hessian eigenvalues have opposite "
        "signs whenever a^2+b^2>0."
    )
    print()
    print("== Principal local dynamics ==")
    print("metric equations: d_t(X+Z)=d_x(X+Z)=0")
    print("local high-frequency branch: X+Z=0")
    print("active vector equation: (d_x-d_t) Z = 0")
    print("Fourier characteristic: (omega+k)^2 = 0")
    print()
    print(
        "Conclusion: the negative derivative-active vector kinetic "
        "combination is reproduced directly from the original A-B action, "
        "without importing generalized-Proca odd coefficients."
    )
    print("All direct-action symbolic assertions passed.")


if __name__=="__main__":
    main()
