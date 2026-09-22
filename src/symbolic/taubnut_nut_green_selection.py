#!/usr/bin/env python3
"""Exact NUT operator, causal-lift and Green-selection diagnostics.

Not a quantum-state construction. A PDE bisolution need not satisfy the local
commutator or positivity conditions. The global causal/topological arguments
are in the associated note, not proved by the finite symbolic checks here.
"""
from __future__ import annotations

import platform
import sympy as sp
import mpmath as mp


def check_geometry() -> None:
    x = sp.symbols('x', positive=True)
    t, th, ph = sp.symbols('t theta phi', real=True)
    K, lam, delta, k = sp.symbols('K lambda delta k', positive=True)
    p = x**2 - 1
    D = (x + delta)**2 - 4*p/(k + 2)
    s, c = sp.sin(th), sp.cos(th)
    # Coordinates (t,x,theta,phi); local monopole gauge away from the axes.
    g = K*sp.Matrix([
        [-p/D, 0, 0, lam*p*c/D],
        [0, 1/p, 0, 0],
        [0, 0, 1, 0],
        [lam*p*c/D, 0, 0, s**2-lam**2*p*c**2/D],
    ])
    inv = sp.Matrix([
        [-D/p+lam**2*c**2/s**2, 0, 0, lam*c/s**2],
        [0, p, 0, 0],
        [0, 0, 1, 0],
        [lam*c/s**2, 0, 0, 1/s**2],
    ])/K
    assert (g*inv-sp.eye(4)).applyfunc(sp.simplify) == sp.zeros(4)
    assert sp.simplify(g.det()+K**4*s**2/D) == 0
    # Phi_0=0; in the NUT chart sin(theta)>0 and D>0.
    mu = K**2*s  # sqrt(-g) exp(-2Phi)
    coords = (t, x, th, ph)
    f = sp.Function('f')(*coords)
    divergence = sum(sp.diff(mu*inv[i, j]*sp.diff(f, coords[j]), coords[i])
                     for i in range(4) for j in range(4))/mu
    angular = (sp.diff(f, ph, 2)+2*lam*c*sp.diff(f, t, ph)
               + lam**2*c**2*sp.diff(f, t, 2))/s**2
    expected = (sp.diff(p*sp.diff(f, x), x)
                + sp.diff(s*sp.diff(f, th), th)/s
                + angular - D/p*sp.diff(f, t, 2))/K
    assert sp.simplify(divergence-expected) == 0
    D0 = sp.factor(D.subs({k: 8, delta: sp.sqrt(sp.Rational(8, 5))}),
                    extension=sp.sqrt(10))
    assert sp.simplify(D0-sp.Rational(3, 5)*(x+sp.sqrt(10)/3)*(x+sp.sqrt(10))) == 0
    print('EXACT metric inverse, density and four-dimensional wave operator.')
    print('D at the repository point =', D0, '; positive for x>1.')

    # A spatial path can be lifted with fibre speed a > its optical speed.
    pp, dd, hh, aa = sp.symbols('p D h a', positive=True)
    norm = K*(hh-pp*aa**2/dd)
    margin = sp.symbols('margin', positive=True)
    lifted = sp.simplify(norm.subs(aa, sp.sqrt(dd/pp)*sp.sqrt(hh+margin)))
    assert lifted == -K*margin
    assert sp.simplify((-K*pp*aa/dd).subs(aa, sp.sqrt(dd/pp)*sp.sqrt(hh+margin))).is_negative
    print('EXACT timelike lift norm = -K*margin; orientation is future.')
    speed = sp.symbols('speed', positive=True)
    radial = K*(1/pp-pp/dd*(speed*sp.sqrt(dd)/pp)**2)
    assert sp.simplify(radial-K*(1-speed**2)/pp) == 0
    assert sp.simplify(radial.subs(speed, 1)) == 0
    print('EXACT radial null ray at speed=1; lab return is timelike for speed>1.')

    # Principal circle coordinate psi=t/(2lambda), of period 2pi.
    # A=dpsi-cos(theta)dphi/2; its curvature has first Chern number +1.
    c1 = sp.integrate(sp.sin(th)/2, (th, 0, sp.pi))*2*sp.pi/(2*sp.pi)
    assert c1 == 1
    print('EXACT Hopf first Chern number = 1: not a global R-time product.')


def check_bisolutions() -> None:
    x, y = sp.symbols('x y', positive=True)
    # On x,y>1 these are real and smooth, but diverge at the excluded horizon.
    u = sp.log((x-1)/(x+1))/2
    v = sp.log((y-1)/(y+1))/2
    Lx = lambda f: sp.simplify(sp.diff((x*x-1)*sp.diff(f, x), x))
    Ly = lambda f: sp.simplify(sp.diff((y*y-1)*sp.diff(f, y), y))
    for f in (sp.Integer(1), u):
        assert Lx(f) == 0
    B = v-u
    assert Lx(B) == Ly(B) == 0
    assert sp.simplify(B+B.xreplace({x:y, y:x})) == 0
    assert sp.simplify(B.subs({x:2, y:3})-sp.log(sp.Rational(3, 2))/2) == 0
    print('EXACT antisymmetric periodic bisolution: B(x,y)=u(y)-u(x).')
    print('B(2,3) = log(3/2)/2 =', sp.N(B.subs({x:2,y:3}), 25))
    # This correction is not licensed as a physical commutator: it modifies
    # local spacelike commutators. A concrete equal-t radial separation is
    # spacelike in a small NUT chart, yet B is nonzero for every small dx>0.
    dx = sp.symbols('dx', positive=True)
    slope = sp.limit((u.subs(x, 2+dx)-u.subs(x, 2))/dx, dx, 0, dir='+')
    assert slope == sp.Rational(1, 3)
    print('NEGATIVE CONTROL: local radial slope 1/3; arbitrary B breaks F-locality.')
    print('PDE+periodicity+causal support do NOT select a physical Green function.')


def check_local_return() -> None:
    results = []
    for dps in (50, 80):
        with mp.workdps(dps):
            delta, lam, K = mp.sqrt(mp.mpf(8)/5), mp.sqrt(mp.mpf(2)/5), mp.mpf(6)
            period = 4*mp.pi*lam
            xa, xb = mp.mpf(2), mp.mpf('2.01')
            p = lambda x: x*x-1
            D = lambda x: (x+delta)**2-mp.mpf(2)/5*p(x)
            dt = mp.quad(lambda x: mp.sqrt(D(x))/p(x), [xa, xb])
            speed = (period-dt)/dt
            assert 0 < 2*dt < period and speed > 1
            tau = mp.sqrt(K*(speed**2-1))*(mp.acosh(xb)-mp.acosh(xa))
            independent = mp.quad(lambda x: mp.sqrt(K*(speed**2-1)/p(x)), [xa, xb])
            assert abs(tau-independent) < mp.power(10, -dps+8)
            # A=(x_a,t=0), B=(x_b,t=dt), lab ends at A=(x_a,t=T).
            assert abs(dt+speed*dt-period) < mp.power(10, -dps+8)
            print(f'dps={dps}; A->B null dt={mp.nstr(dt, 32)}; '
                  f'B->A lab proper time={mp.nstr(tau, 32)}')
            results.append((+dt, +tau))
    with mp.workdps(90):
        assert all(abs(a-b) < mp.mpf('1e-40') for a,b in zip(*results))
    print('This computes rays, NOT a global quantum channel or a probability.')
    print('A common convex normal patch is guaranteed for sufficiently small dx;')
    print('the finite dx=0.01 example is not a certified injectivity-radius bound.')


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}')
    check_geometry()
    check_bisolutions()
    check_local_return()
    print('PASS algebraic diagnostics; no Taub-NUT receiver probability assigned.')


if __name__ == '__main__':
    main()
