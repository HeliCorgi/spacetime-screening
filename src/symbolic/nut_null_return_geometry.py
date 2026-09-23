#!/usr/bin/env python3
"""Exact Hamiltonian identities and independent high-precision null-return checks.

The companion integer certificate proves existence without a floating root.
This file verifies the full north-chart Hamiltonian, the analytic orbit, Hopf
point closure, and unequal endpoint covectors at 50/80 digits. It does not
numerically manufacture a two-point function or prove the propagation theorem.
"""
from __future__ import annotations

import platform
import sympy as sp
import mpmath as mp


def symbolic_checks() -> None:
    x, theta, lam, delta, a = sp.symbols('x theta lambda delta a', real=True)
    pt, px, ptheta, pphi = sp.symbols('p_tN p_x p_theta p_phi', real=True)
    j = sp.symbols('j', positive=True)
    p = x*x-1
    D = (x+delta)**2-a*p
    C = lam*(1-sp.cos(theta))
    # Coordinates (t_N,x,theta,phi); g/K and t_N regular near north pole.
    g = sp.Matrix([[-p/D, 0, 0, -p*C/D],
                   [0, 1/p, 0, 0],
                   [0, 0, 1, 0],
                   [-p*C/D, 0, 0, sp.sin(theta)**2-p*C*C/D]])
    covector = sp.Matrix([pt, px, ptheta, pphi])
    H = (p*px**2+ptheta**2+(pphi-C*pt)**2/sp.sin(theta)**2-D/p*pt**2)/2
    assert sp.trigsimp((covector.T*g.inv()*covector)[0]/2-H) == 0
    assert sp.simplify(g.det()+sp.sin(theta)**2/D) == 0

    cone = {pt: -1, ptheta: 0, pphi: j-lam}
    def on_cone(expr: sp.Expr) -> sp.Expr:
        expr = sp.trigsimp(expr.subs(cone))
        expr = expr.subs(sp.cos(theta), lam/j)
        # At 0<lambda/j<1, theta is in (0,pi/2).
        expr = expr.subs(sp.sin(theta)**2, 1-lam**2/j**2)
        return sp.simplify(expr)
    assert on_cone(sp.diff(H, pphi)) == j
    assert sp.simplify(on_cone(sp.diff(H, pt))-(D/p+lam**2-lam*j)) == 0
    # Clear a nonzero sin^3(theta) before substituting the constant cone.
    angular_force = sp.trigsimp(sp.diff(H, theta)*sp.sin(theta)**3)
    assert on_cone(angular_force) == 0
    angular_energy = (pphi-C*pt)**2/sp.sin(theta)**2
    assert on_cone(angular_energy) == j*j-lam*lam

    R = sp.expand(D-(j*j-lam*lam)*p)
    assert sp.simplify(R.subs(a,lam*lam)-((x+delta)**2-j*j*p)) == 0
    force = sp.diff(p,x)*p*px**2-p*sp.diff(H, x)
    force = on_cone(force).subs(px**2, R/p**2)
    assert sp.simplify(force-sp.diff(R,x)/2) == 0
    assert sp.simplify(on_cone(sp.diff(H,pt)).subs(a,lam*lam)
                       -((x+delta)**2/p-lam*j)) == 0
    assert sp.simplify(sp.diff((x+delta)**2/p,x)+2*(x+delta)*(delta*x+1)/p**2) == 0

    # Analytic radial trajectory, with maximum at sigma=0.
    c, sigma = sp.symbols('c sigma', positive=True)
    amp = sp.sqrt((c+1)*(c+delta**2))
    X = (delta+amp*sp.cos(sp.sqrt(c)*sigma))/c
    radial = (X+delta)**2-(c+1)*(X**2-1)
    assert sp.simplify(sp.expand_trig(sp.diff(X,sigma)**2-radial)) == 0
    assert sp.simplify(sp.diff(X,sigma,2)+c*X-delta) == 0

    # Endpoint covectors in the SAME north chart are not collinear.
    b = sp.symbols('radial_momentum', positive=True)
    k0 = sp.Matrix([-1,b,0,j-lam])
    k1 = sp.Matrix([-1,-b,0,j-lam])
    assert k0[0]*k1[1]-k0[1]*k1[0] == 2*b
    # Therefore (p,k1;p,-k0) is not of local Hadamard diagonal form.
    assert k1 != k0 and k1 != -k0
    print('EXACT: north-chart inverse metric, all Hamilton equations, constant cone, and radial orbit.')
    print('EXACT: endpoint radial momenta have opposite nonzero signs; covectors are not collinear.')
    print('The wavefront contradiction is an analytic application of propagation, not a finite-mode test.')


def numerical_checks(dps: int) -> tuple:
    with mp.workdps(dps):
        delta = mp.sqrt(mp.mpf(8)/5)
        lam = delta/2
        period = 4*mp.pi*lam
        def parameters(j):
            c = j*j-1
            amp = mp.sqrt((c+1)*(c+delta*delta))
            length = 3*mp.pi/j
            return c, amp, length
        def point(j,sigma):
            c, amp, _ = parameters(j)
            return (delta+amp*mp.cos(mp.sqrt(c)*sigma))/c
        def delta_time(j):
            _, _, length = parameters(j)
            return 2*mp.quad(lambda s: (point(j,s)+delta)**2/(point(j,s)**2-1)-lam*j,
                             [0,length/2,length])
        def residual(j):
            return delta_time(j)-period
        j = mp.findroot(residual, (mp.mpf('1.02'),mp.mpf('1.025')),
                        solver='anderson', tol=mp.power(10,-dps+8))
        c, amp, length = parameters(j)
        x0 = point(j,length)
        xmax = point(j,0)
        theta = mp.acos(lam/j)
        speed = amp/mp.sqrt(c)*mp.sin(mp.sqrt(c)*length)
        radial_momentum = speed/(x0*x0-1)
        dt = delta_time(j)
        dphi = 2*j*length
        tolerance = mp.power(10,-dps+6)
        assert mp.mpf('1.02') < j < mp.mpf('1.025')
        assert x0 > 2 and xmax < 80 and radial_momentum > 0
        assert abs(dt-period) < tolerance
        assert abs(dphi-6*mp.pi) < tolerance
        # Hopf embedding: t_N/(2 lambda) is the fibre phase; not symmetric t.
        def hopf(tn,phi):
            psi = tn/(2*lam)
            return (mp.cos(theta/2)*mp.exp(1j*psi),
                    mp.sin(theta/2)*mp.exp(1j*(psi+phi)))
        start, end = hopf(0,0), hopf(dt,dphi)
        assert max(abs(u-v) for u,v in zip(start,end)) < tolerance
        symmetric_dt = dt+lam*dphi
        assert abs(symmetric_dt/period-mp.mpf('2.5')) < tolerance
        assert abs(mp.exp(2j*mp.pi*symmetric_dt/period)+1) < tolerance
        assert dt > 0  # Without the fibre identification the endpoints are distinct.
        max_error = mp.mpf(0)
        for fraction in (-1,mp.mpf('-0.7'),mp.mpf('-0.2'),0,mp.mpf('0.4'),1):
            s = fraction*length
            xx = point(j,s)
            vel = -amp/mp.sqrt(c)*mp.sin(mp.sqrt(c)*s)
            pp = xx*xx-1
            DD = (xx+delta)**2-lam*lam*pp
            tdot = (xx+delta)**2/pp-lam*j
            shift = lam*(1-mp.cos(theta))
            # Direct metric contraction of the full tangent vector.
            norm = vel*vel/pp + mp.sin(theta)**2*j*j-pp/DD*(tdot+shift*j)**2
            energy = -pp/DD*(tdot+shift*j)
            max_error = max(max_error,abs(norm),abs(energy+1))
            assert abs(norm) < tolerance and abs(energy+1) < tolerance
            # Radial acceleration checked by numerical differentiation, separately.
            assert abs(mp.diff(lambda u:point(j,u),s,2)-(delta-c*xx)) < tolerance
        print(f'dps={dps}; j*={mp.nstr(j,45)}')
        print(f'  x_return={mp.nstr(x0,40)}; x_max={mp.nstr(xmax,40)}')
        print(f'  p_x(start/end)=+/-{mp.nstr(radial_momentum,40)}; theta={mp.nstr(theta,30)}')
        print(f'  Delta t_N/T={mp.nstr(dt/period,30)}; Delta phi/(2pi)=3; symmetric Delta t/T=2.5')
        print(f'  max metric/null/orientation residual={mp.nstr(max_error,7)}')
        return tuple(+v for v in (j,x0,xmax,radial_momentum,theta,dt,max_error))


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}; mpmath {mp.__version__}')
    symbolic_checks()
    low,high = numerical_checks(50),numerical_checks(80)
    with mp.workdps(90):
        for a,b in zip(low[:-1],high[:-1]):
            assert abs(a-b) < mp.mpf('1e-40')
    print('PASS exact identities and independent 50/80-digit verification.')
    print('A self-returning segment is NOT a smooth periodic null orbit: the radial tangent reverses.')
    print('Only the specified fixed-background, globally defined, locally Hadamard scalar model is rejected.')
    print('No full-string or universal chronology-protection result is asserted.')


if __name__ == '__main__':
    main()
