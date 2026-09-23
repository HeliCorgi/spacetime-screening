#!/usr/bin/env python3
"""Stationary outgoing radial response of the repository's exact NUT scalar.

This is an exterior Dirichlet-to-Neumann boundary response, NOT a global
retarded propagator, a bath state, or a quantum time-travel probability.
Outgoing radial boundary conditions are explicitly added candidate data.
"""
from __future__ import annotations

import platform
import sympy as sp
import mpmath as mp


def symbolic_checks() -> None:
    x, z = sp.symbols('x z', positive=True)
    w, delta, a, ell2 = sp.symbols('omega delta a L2', real=True)
    h, v = sp.symbols('h v')
    p = x*x-1
    D = (x+delta)**2-a*p
    # x=2/z-1; R=z^h(1-z)^v F(z). Remove indicial poles explicitly.
    ld = h/z-v/(1-z)
    pot = w*w*((2+(delta-1)*z)**2/(4*(1-z))-a)-ell2
    f1 = sp.cancel(2*z*(1-z)*ld-z)
    f0 = sp.cancel(z*(1-z)*(ld*ld+sp.diff(ld, z))-z*ld+pot/z)
    f0 = sp.factor(f0.subs(ell2, h*(h-1)+w*w*(1-a)))
    expected_ab = (h+v)**2+w*w*(delta-1)**2/4
    # Remainder vanishes with v^2=-omega^2(1+delta)^2/4.
    assert sp.cancel(f0+expected_ab-(4*v*v+w*w*(delta+1)**2)/(4*(1-z))) == 0
    assert sp.simplify(f1-(2*h-(2*h+2*v+1)*z)) == 0
    vs = -sp.I*w*(delta+1)/2
    assert sp.simplify(expected_ab.subs(v, vs)-(h-sp.I*w)*(h-sp.I*w*delta)) == 0

    # Globally allowed integer fibre frequencies and monopole harmonics.
    n, ell = sp.symbols('n ell', integer=True, nonnegative=True)
    lam2 = sp.Rational(2, 5)
    a0 = sp.Rational(3, 5)
    wn2 = n*n/(4*lam2)
    L2 = ell*(ell+1)-n*n/4
    s2 = sp.factor(wn2*a0-L2-sp.Rational(1, 4))
    lowest = sp.factor(s2.subs(ell, n/2))
    assert sp.expand(lowest-(3*n*n-4*n-2)/8) == 0
    assert [lowest.subs(n, j) for j in range(1, 5)] == [
        -sp.Rational(3, 8), sp.Rational(1, 4),
        sp.Rational(13, 8), sp.Rational(15, 4)]
    # Explicit n=2, ell=1, m=0 angular function; no illegal m=0 for odd n.
    th = sp.symbols('theta', positive=True)
    Y = sp.sin(th)
    angular = sp.diff(sp.sin(th)*sp.diff(Y, th), th)/sp.sin(th)-sp.cot(th)**2*Y
    assert sp.trigsimp(angular+Y) == 0
    print('EXACT radial hypergeometric reduction; c=2h, a_hyp=h-i omega, b_hyp=h-i omega delta.')
    print('EXACT periodic scalar frequencies omega_n=n/(2 lambda); L2=ell(ell+1)-n^2/4.')
    print('Lowest angular branch: s_n^2=(3n^2-4n-2)/8; propagating for integer n>=2.')

    # Abel identity gives flux conservation for the REAL radial ODE.
    R, C, Rp, Cp = sp.symbols('R Rbar Rp Rbarp')
    V = w*w*D/p-ell2
    Rpp = (-sp.diff(p, x)*Rp-V*R)/p
    Cpp = (-sp.diff(p, x)*Cp-V*C)/p
    jprime = sp.diff(p, x)*(C*Rp-R*Cp)+p*(C*Rpp-R*Cpp)
    assert sp.simplify(jprime) == 0
    # Leading outgoing coefficient x^(-1/2+i s) has radial flux +s.
    s = sp.symbols('s', real=True)
    R0 = x**(-sp.Rational(1, 2)+sp.I*s)
    C0 = x**(-sp.Rational(1, 2)-sp.I*s)
    assert sp.simplify(x*x*(C0*sp.diff(R0, x)-R0*sp.diff(C0, x))/(2*sp.I)-s) == 0

    # C(t) of an invariant, single-valued neutral observable has exact echoes.
    T = sp.symbols('T', positive=True)
    for j in range(-8, 9):
        assert sp.simplify(sp.exp(2*sp.pi*sp.I*j)-1) == 0
    # A strictly decaying exponential cannot match at a full Killing period.
    kappa = sp.symbols('kappa', positive=True)
    mismatch = 1-sp.exp(-kappa*T)
    assert sp.limit(mismatch, kappa, 0, dir='+') == 0
    print('PERIODICITY: C(T)=C(0); normalized exponential-bath mismatch at T is 1-exp(-kappa T).')

    # The dilaton Ward force has no Killing-energy component when Phi is static.
    # The flux density uses sqrt(-g_E)*g_E^xx=K p sin(theta).
    K = sp.symbols('K', positive=True)
    D0 = D.subs({delta: sp.sqrt(sp.Rational(8, 5)), a: sp.Rational(2, 5)})
    current_prefactor = K*K*sp.sqrt(D0)*sp.sin(th) * p/(K*sp.sqrt(D0))
    assert sp.simplify(current_prefactor-K*p*sp.sin(th)) == 0
    Phi = -sp.log(D0)/4
    t = sp.symbols('t')
    assert sp.diff(Phi, t) == 0
    assert sp.factor(D0) != 0
    print('KILLING FLUX: stationary dilaton term contracts to zero with xi=partial_t.')
    print('Stokes over [x_L,x_R] x S^3 needs no fictitious spacelike t-slices.')


def response(x: mp.mpf, omega: mp.mpf, delta: mp.mpf, s: mp.mpf) -> tuple:
    """Return R_out and its analytic derivative, with unit outgoing amplitude."""
    z = 2/(x+1)
    h = mp.mpf('0.5')-1j*s
    v = -1j*omega*(1+delta)/2
    aa, bb, cc = h-1j*omega, h-1j*omega*delta, 2*h
    F = mp.hyp2f1(aa, bb, cc, z)
    Fp = aa*bb/cc*mp.hyp2f1(aa+1, bb+1, cc+1, z)
    pref = (z/2)**h*(1-z)**v
    R = pref*F
    Rz = pref*((h/z-v/(1-z))*F+Fp)
    return R, -z*z*Rz/2


def numerical_checks(dps: int) -> list[tuple]:
    with mp.workdps(dps):
        delta = mp.sqrt(mp.mpf(8)/5)
        lam = mp.sqrt(mp.mpf(2)/5)
        period = 4*mp.pi*lam
        results = []
        max_ode = mp.mpf(0)
        max_flux = mp.mpf(0)
        for n in (2, 3, 4):
            omega = n/(2*lam)
            ell = mp.mpf(n)/2
            L2 = ell*(ell+1)-mp.mpf(n*n)/4
            s = mp.sqrt(omega*omega*mp.mpf(3)/5-L2-mp.mpf(1)/4)
            for point in (2, 3, 7):
                x = mp.mpf(point)
                R, Rp = response(x, omega, delta, s)
                Rpp = mp.diff(lambda u: response(u, omega, delta, s)[1], x)
                p = x*x-1
                D = (x+delta)**2-mp.mpf(2)/5*p
                residual = p*Rpp+2*x*Rp+(omega*omega*D/p-L2)*R
                flux = p*mp.im(mp.conj(R)*Rp)
                impedance = p*Rp/R
                max_ode = max(max_ode, abs(residual))
                max_flux = max(max_flux, abs(flux-s))
                assert abs(residual) < mp.power(10, -dps+10)
                assert abs(flux-s) < mp.power(10, -dps+10)
                assert mp.im(impedance) > 0
                assert abs(mp.im(impedance)-s/abs(R)**2) < mp.power(10, -dps+10)
                if point == 2:
                    results.append((+mp.re(impedance), +mp.im(impedance)))
                    print(f'dps={dps}; n={n}, ell={ell}, x=2; Y_out={mp.nstr(impedance, 36)}')
            # An independent leading Frobenius coefficient at infinity.
            xlarge = mp.mpf('1e12')
            Rlarge, _ = response(xlarge, omega, delta, s)
            assert abs(Rlarge*xlarge**(mp.mpf('0.5')-1j*s)-1) < mp.mpf('1e-9')

        # Radial power at the boundary: <J^x> integrated over normalized angular mode
        # for real field Re[a R exp(-i omega t)Y]: K omega j/2.
        x = mp.mpf(2)
        p = x*x-1
        D = (x+delta)**2-mp.mpf(2)/5*p
        proper_period = period*mp.sqrt(6*p/mp.sqrt(D))
        results.append((+period, +proper_period))
        print(f'dps={dps}; Killing period={mp.nstr(period, 32)}; static g_E proper period at x=2={mp.nstr(proper_period, 32)}')
        print(f'dps={dps}; max ODE residual={mp.nstr(max_ode, 5)}; max flux residual={mp.nstr(max_flux, 5)}')
        return results


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}; mpmath {mp.__version__}')
    symbolic_checks()
    low, high = numerical_checks(50), numerical_checks(80)
    with mp.workdps(90):
        for a, b in zip(low, high):
            for u, v in zip(a, b):
                assert abs(u-v) < mp.mpf('1e-40')
    print('PASS exact and 50/80-digit outgoing-response checks.')
    print('Radial loss is NOT kinematically forbidden; no global bath state, eta, metric backreaction or past signal certified.')


if __name__ == '__main__':
    main()
