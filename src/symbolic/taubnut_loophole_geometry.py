#!/usr/bin/env python3
"""Attack, and retain failed attacks, on the exact heterotic NUT geometry.

1. Its interior has no closed NULL GEODESIC: the radial potential is strictly
   monotone (not a statement about accelerated CTCs or all quantum states).
2. The chosen horizon still has a nontrivial local boost identification after
   finite-k metric corrections. Large relative boosts invalidate a UNIFORM
   low-energy estimate for the specified image-momentum diagnostic, not a
   proof of a string backreaction catastrophe.

All model parameters/assumptions and literature comparisons are in
notes/chronology-loophole-attack.md. No global time-unwrapped NUT cover is used.
"""
from __future__ import annotations

import platform
import sympy as sp
from mpmath import mp


def algebra() -> None:
    x, delta, a, ell2, energy = sp.symbols('x delta a L2 E', real=True)
    theta, phi, t, px, pt, ptheta, pphi, lam = sp.symbols(
        'theta phi t p_x p_t p_theta p_phi lambda', real=True)
    p = x*x-1
    big_d = (x+delta)**2-a*p  # a=4/(k+2), 0<a<1 when k>2
    angular = ptheta**2 + (pphi+lam*sp.cos(theta)*pt)**2/sp.sin(theta)**2
    hamiltonian = (p*px**2+angular-big_d*pt**2/p)/2  # affine parameter rescaled by K
    qvars, pvars = [x, theta, phi, t], [px, ptheta, pphi, pt]
    bracket = sum(sp.diff(angular, q)*sp.diff(hamiltonian, r)
                  -sp.diff(angular, r)*sp.diff(hamiltonian, q)
                  for q, r in zip(qvars, pvars))
    assert sp.simplify(bracket) == 0
    assert sp.diff(hamiltonian, t) == 0
    radial_velocity = sp.diff(hamiltonian, px)
    assert radial_velocity == p*px
    # Hamilton's acceleration restricted to null energy shell and L^2=angular.
    acceleration = (sp.diff(radial_velocity, x)*sp.diff(hamiltonian, px)
                    -sp.diff(radial_velocity, px)*sp.diff(hamiltonian, x))
    acceleration = acceleration.subs(pt**2, energy**2)
    acceleration = acceleration.subs(px**2, (energy**2*big_d-ell2*p)/p**2)
    assert sp.simplify(acceleration-(energy**2*sp.diff(big_d, x)-ell2*sp.diff(p, x))/2) == 0
    derivative = sp.factor(sp.diff(big_d/p, x))
    expected = -2*(x+delta)*(delta*x+1)/p**2
    assert sp.simplify(derivative-expected) == 0
    turning_acceleration = sp.factor(
        (energy**2*sp.diff(big_d, x)-ell2*sp.diff(p, x)).subs(ell2, energy**2*big_d/p)/2)
    assert sp.simplify(turning_acceleration+energy**2*(x+delta)*(delta*x+1)/p) == 0
    # Certificate of signs for x=1+r, delta=1+s with r,s positive.
    rpos, spos = sp.symbols('r s', positive=True)
    assert (-derivative).subs({x: 1+rpos, delta: 1+spos}).is_positive
    assert sp.diff(derivative, a) == 0
    print('EXACT angular Hamiltonian conserved; xdot^2=E^2 D-L^2 p')
    print('EXACT (D/p)\' = -2(x+delta)(delta*x+1)/(x^2-1)^2 < 0 in first NUT')
    print('Every radial turning point is a strict maximum; no interior closed null geodesic.')
    print('This defeats an attempted NUT-interior trapped-null no-go, NOT the CTC geometry.')

    # Local near-horizon Einstein-metric fibre block, with rho=x-1.
    rho, q, d, kscale = sp.symbols('rho q d K', positive=True)
    horizon_metric = sp.Matrix([[-2*kscale*rho/d, -kscale], [-kscale, 0]])  # q,rho
    uv = sp.Matrix([sp.exp(-q/d), rho*sp.exp(q/d)])
    jac = uv.jacobian([q, rho])
    flat_metric = sp.Matrix([[0, kscale*d], [kscale*d, 0]])
    assert (jac.T*flat_metric*jac-horizon_metric).applyfunc(sp.simplify) == sp.zeros(2)
    period = sp.symbols('T', positive=True)
    assert sp.simplify(uv[0].subs(q, q+period)-sp.exp(-period/d)*uv[0]) == 0
    assert sp.simplify(uv[1].subs(q, q+period)-sp.exp(period/d)*uv[1]) == 0
    assert big_d.subs(x, 1) == (delta+1)**2
    assert sp.simplify(sp.diff(p/sp.sqrt(big_d), x).subs(x, 1).subs(delta, 1+spos)
                       -2/(2+spos)) == 0
    print('EXACT leading horizon metric is a local boost patch; rapidity T/(1+delta).')
    print('No finite-k cancellation at fixed delta,lambda; their anomaly constraints are not varied.')

    # Lorentz-invariant relative momentum diagnostic, not an actual collision calculation.
    chi, mass = sp.symbols('chi m', real=True)
    p0 = sp.Matrix([mass, 0])
    pn = sp.Matrix([mass*sp.cosh(chi), mass*sp.sinh(chi)])
    eta = sp.diag(-1, 1)
    invariant = -((p0+pn).T*eta*(p0+pn))[0]
    assert sp.trigsimp(invariant-2*mass**2*(1+sp.cosh(chi))) == 0
    assert sp.simplify(invariant.subs(chi, 0)-4*mass**2) == 0
    print('EXACT image-pair s_N=2 m^2[1+cosh(N rapidity)]; zero-boost control is finite.')


def numerical(dps: int) -> dict[str, object]:
    with mp.workdps(dps):
        delta, lam = mp.sqrt(mp.mpf(8)/5), mp.sqrt(mp.mpf(2)/5)
        a = mp.mpf(2)/5
        period = 4*mp.pi*lam
        rapidity = period/(1+delta)
        factor = mp.exp(rapidity)
        def big_d(x):
            return (x+delta)**2-a*(x*x-1)
        results: dict[str, object] = {'rapidity': +rapidity, 'factor': +factor}
        for b2 in [mp.mpf(1), mp.mpf(2), mp.mpf(4)]:
            c = b2-(1-a)
            turning = (delta+mp.sqrt(delta**2+c*(delta**2+a+b2)))/c
            residual = big_d(turning)-b2*(turning**2-1)
            assert turning > 1 and abs(residual) < mp.mpf(10)**(-dps+8)
            acc = -(turning+delta)*(delta*turning+1)/(turning**2-1)
            assert acc < 0
            results[f'turn_{b2}'] = +turning
            print(f'dps={dps}; L2/E2={b2}; unique radial maximum x={mp.nstr(turning, 35)}')
        # No turning at b^2 <= 1-a, since D/p > 1-a on x>1 (proved analytically).
        for b2 in [mp.mpf(0), mp.mpf(1)/2, 1-a]:
            for x in [mp.mpf('1.01'), mp.mpf(2), mp.mpf(100)]:
                assert big_d(x)/(x*x-1) > b2
        for exponent in [6, 12, 30]:
            mu2 = mp.mpf(10)**(-exponent)  # explicitly chosen alpha' m^2, not source spectrum
            first = int(mp.ceil(mp.acosh(1/(2*mu2)-1)/rapidity))
            threshold = lambda n: 2*mu2*(1+mp.cosh(n*rapidity))
            assert threshold(first) >= 1 and threshold(first-1) < 1
            results[f'threshold_{exponent}'] = first
            print(f'dps={dps}; diagnostic alpha_prime*m^2=1e-{exponent}; first s_N*alpha_prime>=1: N={first}')
        print(f'dps={dps}; rapidity={mp.nstr(rapidity, 40)}; per-loop factor={mp.nstr(factor, 40)}')
        return results


if __name__ == '__main__':
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}')
    algebra()
    low, high = numerical(50), numerical(80)
    with mp.workdps(80):
        for key in low:
            assert abs(low[key]-high[key]) < mp.mpf('1e-40')*max(1, abs(high[key]))
    print('PASS geometry/boost assertions and 50/80-digit comparison.')
    print('No global NUT quantum state, actual image collision, or full string backreaction computed.')
