#!/usr/bin/env python3
"""Algebraic checks for applying the published KRW theorem to the scalar proxy.

The theorem, compactness, domain-of-dependence argument and Hopf-bundle
identifications are proved/cited in the accompanying note, NOT by these asserts.
The neutral real dilaton-weighted massless scalar is exactly a minimally
coupled massless scalar for g_E = exp(-2 Phi) g in FOUR spacetime dimensions.
No claim is made that this proxy is the full heterotic string field theory.
"""
from __future__ import annotations

import platform
import sympy as sp


def zero(expr: sp.Expr) -> None:
    assert sp.simplify(expr) == 0, expr


def matrix_zero(mat: sp.Matrix) -> None:
    for entry in mat:
        zero(entry)


def main() -> None:
    print(f"Python {platform.python_version()}; SymPy {sp.__version__}")
    x, th = sp.symbols('x theta', real=True)
    K, lam, d = sp.symbols('K lambda d', positive=True)
    # Use independent positive s=sqrt(D); differentiating is done below.
    p = sp.Symbol('p', real=True)
    s = sp.Symbol('s', positive=True)
    sn, cs = sp.sin(th), sp.cos(th)
    # Coordinate ordering (q,x,theta,phi); xi=dq-lambda cos(theta)dphi.
    g = K * sp.Matrix([
        [-p/s**2, -1/s, 0, p*lam*cs/s**2],
        [-1/s, 0, 0, lam*cs/s],
        [0, 0, 1, 0],
        [p*lam*cs/s**2, lam*cs/s, 0, sn**2-p*lam**2*cs**2/s**2],
    ])
    gE = s*g
    invg, invE = g.inv(), gE.inv()
    zero(g.det()+K**4*sn**2/s**2)
    zero(gE.det()+K**4*s**2*sn**2)
    matrix_zero(invE-invg/s)
    # On the polar chart 0<theta<pi. The axes are covered by monopole charts.
    volg, volE, weight = K**2*sn/s, K**2*s*sn, s
    matrix_zero(volE*invE-weight*volg*invg)
    zero(volE/(weight*volg)-s)
    # Hence box_E = (1/s) P_Phi, not the inverse factor.
    zero(invE[1, 1]-p/(K*s))
    zero(invE[0, 1]+1/K)
    horizon = {p: 0, s: d}
    normal = invE[:, 1].subs(horizon)
    matrix_zero(normal-sp.Matrix([-1/K, 0, 0, 0]))
    zero(gE.det().subs(horizon)+K**4*d**2*sn**2)
    # Pullback to x=1: only the positive two-sphere metric remains.
    pullback = gE.extract([0, 2, 3], [0, 2, 3]).subs(horizon)
    matrix_zero(pullback-K*d*sp.diag(0, 1, sn**2))
    # Killing generator n=d/dq. Gamma^a_qq = -g^{ax} d_x g_qq/2.
    dp, ds = sp.symbols('dp ds', real=True)
    dxgqq = sp.diff(gE[0, 0], p)*dp+sp.diff(gE[0, 0], s)*ds
    acceleration = (-invE[:, 1]*dxgqq/2).subs(horizon).subs(dp, 2)
    matrix_zero(acceleration-sp.Matrix([-1/d, 0, 0, 0]))
    # Einstein conformal transformation in arbitrary dimension Dn.
    Dn = sp.symbols('Dn', integer=True, positive=True)
    omega = sp.symbols('conformal_factor', positive=True)
    dens_factor = omega**(Dn-2)
    zero(dens_factor.subs(Dn, 4)-omega**2)
    assert sp.simplify(dens_factor.subs(Dn, 3)-omega**2) != 0
    # Exact repository point, alpha'=1 and Phi0=0 for numerical display only.
    delta0, lam0 = sp.sqrt(sp.Rational(8,5)), sp.sqrt(sp.Rational(2,5))
    D = (x+delta0)**2-sp.Rational(2,5)*(x**2-1)
    factor_D = sp.Rational(3,5)*(x+sp.sqrt(10))*(x+sp.sqrt(10)/3)
    zero(D-factor_D)
    assert sp.sqrt(10)/3 > 1  # both D zeros lie below x=-1
    d0 = 1+delta0
    zero(D.subs(x, 1)-d0**2)
    period = 4*sp.pi*lam0
    kappa = -1/d0
    q = sp.symbols('q', real=True)
    affine_speed = sp.exp(q/d0)  # dq/daffine
    zero(sp.diff(affine_speed, q)+kappa*affine_speed)
    # q is periodic, affine tangent need not be. Recurrent curves suffice.
    boost = sp.exp(period/d0)
    # Linearized nontrivial null flow: d(x-1)/dq=-(x-1)/d0.
    return_multiplier = sp.exp(-period/d0)
    zero(boost*return_multiplier-1)
    print('EXACT: sqrt(-g_E) g_E^ab = exp(-2Phi) sqrt(-g) g^ab')
    print('EXACT: box_E = exp(2Phi) P_Phi; massless KG, not an EFT expansion')
    print('EXACT: det(g_E)|H = -K^4 (1+delta)^2 sin(theta)^2')
    print('EXACT: g_E^xx = (x^2-1)/(K sqrt(D)); grad(x)|H = -d/dq / K')
    print('EXACT: nabla_n n|H = -n/(1+delta)')
    print('D(x) =', sp.factor(factor_D, extension=sp.sqrt(10)))
    print('period =', sp.N(period, 40))
    print('kappa in stated q normalization =', sp.N(kappa, 40))
    print('future affine-tangent factor per fibre loop =', sp.N(boost, 40))
    print('Negative control: the same massless minimal conformal identity fails in D=3.')
    print('PASS local geometry/operator identities; global geometric proof is in the note.')
    print('KRW is a published theorem, not proved by this script. Full-string conclusion remains open.')


if __name__ == '__main__':
    main()
