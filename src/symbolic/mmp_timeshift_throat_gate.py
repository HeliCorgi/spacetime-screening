#!/usr/bin/env python3
"""Time-shifted Casimir source and a leading MMP/JT throat-passage gate.

This is an explicit extension of the leading, spherically averaged MMP
approximation: transparent massless NS loops, a constant physical time
holonomy, and no additional negative-null-energy source. It is NOT a
solution of the full time-dependent four-dimensional formation problem.
No time-shifted energy minimum is mistaken for a solution of the momentum
constraint. See notes/mmp-timeshift-relative-mode-audit.md.
"""
from __future__ import annotations

import platform
import sympy as sp
import mpmath as mp


def zero(expression: sp.Expr) -> None:
    assert sp.simplify(sp.trigsimp(sp.expand(expression))) == 0, expression


def source_checks() -> None:
    C, delta, ell, central = sp.symbols('C Delta ell c_eff', positive=True)
    um = C - delta
    up = C + delta
    flat_e = -sp.pi * central / 12 * (um**-2 + up**-2)
    flat_j = sp.pi * central / 12 * (um**-2 - up**-2)
    # Independent derivation: boost the ordinary spacelike-cylinder vacuum.
    # Identification (t,x)~(t+Delta,x+C), with |Delta|<C.
    rest_rho = -sp.pi * central / (6 * (C**2 - delta**2))
    zero(flat_e - rest_rho * (C**2 + delta**2) / (C**2 - delta**2))
    zero(flat_j + 2 * rest_rho * C * delta / (C**2 - delta**2))
    zero(flat_j - sp.pi * central * C * delta / (3*(C**2-delta**2)**2))

    # MMP conformal-anomaly contribution to the TRACeless 2D source.
    sigma = sp.symbols('sigma', real=True)
    rho = -sp.log(sp.cos(sigma))
    anomaly_chiral = -central/(48*sp.pi) * (sp.diff(rho, sigma)**2-sp.diff(rho, sigma, 2))
    zero(anomaly_chiral-central/(48*sp.pi))
    e = ell**2 * flat_e + central/(24*sp.pi)
    j = ell**2 * flat_j
    zero(e.subs({C: sp.pi*ell, delta: 0})+central/(8*sp.pi))
    zero(j.subs(delta, 0))
    # The short-direction null source uses the WEAKER opposite chirality.
    gate = 4*(sp.pi*ell)**2/up**2-1
    zero(-(e+j)-central/(24*sp.pi)*gate)
    zero(-(e-j)-central/(24*sp.pi)*(4*(sp.pi*ell)**2/um**2-1))

    # Recover the published unshifted, d << ell variational result.
    A, q = sp.symbols('A q', positive=True)  # A=r_e^3/G
    energy = A/ell**2-q/(8*ell)
    ell0 = 16*A/q
    zero(sp.diff(energy, ell).subs(ell, ell0))
    assert sp.simplify(sp.diff(energy, ell, 2).subs(ell, ell0)).is_positive
    zero(energy.subs(ell, ell0)+q**2/(256*A))
    print('EXACT: NS chiral Casimir source equals the boosted cylinder source.')
    print('EXACT: MMP anomaly and Delta=0 energy/length/source are recovered.')
    print('NONZERO FLUX: Delta>0 produces j>0; a static energy extremum alone is insufficient.')


def jt_checks() -> None:
    tau, sigma = sp.symbols('tau sigma', real=True)
    kappa = sp.symbols('kappa', positive=True)
    a, j, u, v, w = sp.symbols('a j u v w', real=True)
    coordinates = (tau, sigma)
    metric = sp.diag(-1/sp.cos(sigma)**2, 1/sp.cos(sigma)**2)
    inverse = metric.inv()
    gamma = [[[sp.simplify(sum(inverse[c, d] * (
        sp.diff(metric[d, b], coordinates[a0])
        + sp.diff(metric[d, a0], coordinates[b])
        - sp.diff(metric[a0, b], coordinates[d])) / 2 for d in range(2)))
        for b in range(2)] for a0 in range(2)] for c in range(2)]

    def operator(field: sp.Expr) -> sp.Matrix:
        hessian = sp.Matrix(2, 2, lambda i, k:
            sp.diff(field, coordinates[i], coordinates[k])
            - sum(gamma[c][i][k]*sp.diff(field, coordinates[c]) for c in range(2)))
        box = sum(inverse[i, k]*hessian[i, k] for i in range(2) for k in range(2))
        return (metric*box-hessian-metric*field).applyfunc(sp.simplify)

    homogeneous = u*sp.cos(tau)/sp.cos(sigma) + v*sp.sin(tau)/sp.cos(sigma) + w*sp.tan(sigma)
    phi = kappa*(a*(1+sigma*sp.tan(sigma))-j*tau*sp.tan(sigma))+homogeneous
    target = kappa*sp.Matrix([[-a, j], [j, -a]])
    assert (operator(phi)-target).applyfunc(sp.trigsimp) == sp.zeros(2)
    assert operator(homogeneous).applyfunc(sp.trigsimp) == sp.zeros(2)
    # Omitting the secular term leaves the off-diagonal equation UNSOLVED.
    static_part = kappa*a*(1+sigma*sp.tan(sigma))+homogeneous
    assert sp.simplify((operator(static_part)-target)[0, 1]) == -kappa*j

    # Leading positive radius-growth coefficients at the two asymptotic ends.
    # cos(sigma)*phi is evaluated before the limit, avoiding infinity algebra.
    rescaled = kappa*(a*(sp.cos(sigma)+sigma*sp.sin(sigma))-j*tau*sp.sin(sigma))
    rescaled += u*sp.cos(tau)+v*sp.sin(tau)+w*sp.sin(sigma)
    left = sp.simplify(rescaled.subs(sigma, -sp.pi/2))
    right = sp.simplify(rescaled.subs(sigma, sp.pi/2))
    start = sp.symbols('tau_in', real=True)
    zero(left.subs(tau, start)+right.subs(tau, start+sp.pi)-kappa*sp.pi*(a-j))
    zero(right.subs(tau, start)+left.subs(tau, start+sp.pi)-kappa*sp.pi*(a+j))
    # All THREE homogeneous JT modes cancel in the entry/exit sum.
    # Replacing the two events by a same-time test would give the wrong gate.
    zero(left+right-(kappa*sp.pi*a+2*u*sp.cos(tau)+2*v*sp.sin(tau)))

    f = sp.Function('f')(sigma)
    zero(sp.diff(sp.cos(sigma)**2*sp.diff(f, sigma), sigma)
         -sp.cos(sigma)**2*(sp.diff(f,sigma,2)-2*sp.tan(sigma)*sp.diff(f,sigma)))
    ray = phi.subs(tau, start+sigma+sp.pi/2)
    zero(sp.diff(ray,sigma,2)-2*sp.tan(sigma)*sp.diff(ray,sigma)-2*kappa*(a-j))
    zero(sp.integrate(sp.cos(sigma)**2, (sigma, -sp.pi/2, sp.pi/2))-sp.pi/2)
    print('EXACT: all leading JT equations, all homogeneous modes and null focusing identity.')
    print('ENTRY/EXIT: B_left(t)+B_right(t+pi)=kappa*pi*(a-j), not a same-time test.')


def bound_checks() -> None:
    tw, d, delta, wait = sp.symbols('tau_w d Delta tau_read', positive=True)
    upper = 4*tw**2/(tw+d+delta)**2-1
    zero(upper-(tw-d-delta)*(3*tw+d+delta)/(tw+d+delta)**2)
    zero(sp.diff(upper, delta)+8*tw**2/(tw+d+delta)**3)
    margin = sp.symbols('margin', positive=True)
    # Gate implies Delta=tw-d-margin: later return, even before readout cost.
    arrival = tw+d+wait-delta
    zero(arrival.subs(delta, tw-d-margin)-(2*d+wait+margin))
    # At a blocked example, any rescuing source must provide negative
    # weighted null energy. Numbers are dimensionless normalized diagnostics.
    assert sp.simplify(upper.subs({tw: 1,d:sp.Rational(1,4),delta:1})) == -sp.Rational(17,81)
    print('BOUND: positive NS/JT entry and exit require Delta < tau_w-d.')
    print('Thus return time > 2d+tau_read in this leading passive model.')
    print('At tau_w=1,d=1/4,Delta=1: extra null integral must be < -17*c_eff/1944.')


def ns_source(C: mp.mpf, delta: mp.mpf, ell: mp.mpf, central: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    if C <= abs(delta) or ell <= 0 or central <= 0:
        raise ValueError('NS ground-state continuation is used only for a spacelike loop and positive scales')
    e = central/(24*mp.pi)-central*mp.pi*ell**2/12*((C-delta)**-2+(C+delta)**-2)
    j = central*mp.pi*ell**2/12*((C-delta)**-2-(C+delta)**-2)
    return e,j


def precision_checks(dps: int) -> list[mp.mpf]:
    with mp.workdps(dps):
        ell = 1/mp.pi
        q, kappa = mp.mpf(7), mp.mpf('0.03')
        d = mp.mpf(1)/4
        result = []
        for delta in (mp.mpf(0),mp.mpf(1)/2,mp.mpf(3)/4,mp.mpf(1)):
            C = 1+d
            e,j = ns_source(C,delta,ell,q)
            a = -e
            gate = 4/(C+delta)**2-1
            start, u,v,w = map(mp.mpf, ('0.17','0.013','-0.007','0.009'))
            def phi(t, x):
                return kappa*(a*(1+x*mp.tan(x))-j*t*mp.tan(x))+(u*mp.cos(t)+v*mp.sin(t))/mp.cos(x)+w*mp.tan(x)
            left = kappa*a*mp.pi/2+kappa*j*start+u*mp.cos(start)+v*mp.sin(start)-w
            end = start+mp.pi
            right = kappa*a*mp.pi/2-kappa*j*end+u*mp.cos(end)+v*mp.sin(end)+w
            direct_integral = -kappa*mp.quad(lambda x: 2*(e+j)*mp.cos(x)**2,[-mp.pi/2,0,mp.pi/2])
            target = kappa*q/24*gate
            tol = mp.power(10, -dps+8)
            assert abs(left+right-target)<tol
            assert abs(direct_integral-target)<tol
            for x in (mp.mpf('-0.8'),mp.mpf('0.2'),mp.mpf('0.9')):
                f=lambda z: phi(start+z+mp.pi/2,z)
                assert abs(mp.diff(f,x,2)-2*mp.tan(x)*mp.diff(f,x)-2*kappa*(a-j))<tol
            result.extend((+gate, +target))
            print(f'dps={dps}; tau_w=1,d=1/4,Delta={delta}; gate={mp.nstr(gate,32)}; loop_delay={mp.nstr(C-delta,12)}')
        # Reject an unphysical analytic continuation instead of reporting a
        # vacuum beyond the null loop.
        for invalid in (mp.mpf('1.25'),mp.mpf('1.5')):
            try:
                ns_source(mp.mpf('1.25'),invalid,ell,q)
            except ValueError:
                pass
            else:
                raise AssertionError('timelike/null NS loop must be rejected')
        # The obstruction can occur with small leading gravitational source.
        # epsilon_br=kappa*c_eff/(24*pi); this is NOT a full 4D solution.
        e,j=ns_source(mp.mpf('1.25'),mp.mpf('.75'),ell,q)
        epsilon_br=mp.mpf('1e-6')
        effective_kappa=epsilon_br*24*mp.pi/q
        assert abs(effective_kappa*e+mp.mpf('7.5e-6'))<mp.power(10,-dps+8)
        assert abs(effective_kappa*j-mp.mpf('7.5e-6'))<mp.power(10,-dps+8)
        print('CONTROL: at gate zero and epsilon_br=1e-6, kappa*(e,j)=(-7.5e-6,+7.5e-6), finite.')
        # A longer-loop distribution can only worsen this upper bound.
        lengths=(d,mp.mpf('0.5'),mp.mpf(1))
        weights=(mp.mpf(1)/2,mp.mpf(1)/3,mp.mpf(1)/6)
        distributed=lambda shift: 4*sum(wt/(1+ln+shift)**2 for wt,ln in zip(weights,lengths))-1
        root=mp.findroot(distributed,(mp.mpf('0.4'),mp.mpf('0.7')))
        assert 0<root<mp.mpf('0.75')
        result.append(+root)
        print(f'dps={dps}; comparison longer-loop distribution gate zero={mp.nstr(root,36)}')
        return result


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}; mpmath {mp.__version__}')
    source_checks()
    jt_checks()
    bound_checks()
    low, high = precision_checks(50), precision_checks(80)
    with mp.workdps(90):
        assert max(abs(x-y) for x,y in zip(low,high)) < mp.mpf('1e-40')
    print('PASS exact algebra and independent 50/80-digit checks.')
    print('Conditional leading-MMP/JT obstruction; NOT full 4D dynamics, all quantum states or a natural probability.')


if __name__ == '__main__':
    main()
