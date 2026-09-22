#!/usr/bin/env python3
"""Retarded scalar mode control and a regular continuation into first NUT.

An explicitly prescribed, spatially extended harmonic source is allowed here.
It is NOT a local laboratory operation, a BRST string source, a backreacted
solution, or an operational probability model. The calculation shows why
future regularity alone cannot rule out all controlled scalar preparations.
"""
from __future__ import annotations

import platform
import mpmath as mp


def calculate(dps: int) -> tuple[mp.mpc, mp.mpf]:
    with mp.workdps(dps):
        tol = mp.mpf(10)**(-(dps-14))
        k, angular = mp.mpf(8), mp.mpf(1)
        delta, omega = mp.sqrt(mp.mpf(8)/5), mp.sqrt(10)/2
        d = 1+delta
        om, op = omega*(delta-1), omega*d
        ah, bh, h = 1j*op/2, -1j*om/2, -mp.mpf(1)/2+1j/2
        a, b, c = ah+bh-h, ah+bh+h+1, 1+2*ah
        normalization = mp.sqrt(2*op)

        mode_cache: dict[tuple[mp.mpf, int], tuple[mp.mpc, mp.mpc]] = {}

        def mode(eta: mp.mpf) -> tuple[mp.mpc, mp.mpc]:
            key = (eta, mp.mp.prec)  # Differentiation changes working precision.
            if key in mode_cache:
                return mode_cache[key]
            z = (1-mp.tanh(eta))/2
            pref = z**ah*(1-z)**bh/normalization
            f = mp.hyp2f1(a, b, c, z)
            fz = a*b/c*mp.hyp2f1(a+1, b+1, c+1, z)
            dz = -2*z*(1-z)
            value = (pref*f, dz*pref*(fz+(ah/z-bh/(1-z))*f))
            mode_cache[key] = value
            return value

        def switch(eta: mp.mpf) -> tuple[mp.mpf, mp.mpf, mp.mpf]:
            if eta <= -1:
                return mp.mpf(0), mp.mpf(0), mp.mpf(0)
            if eta >= 1:
                return mp.mpf(1), mp.mpf(0), mp.mpf(0)
            s = (eta+1)/2
            left, right = mp.exp(-1/s), mp.exp(-1/(1-s))
            total = left+right
            slope = 1/s**2+1/(1-s)**2
            curvature = -2/s**3+2/(1-s)**3
            product = left*right/total**2
            return (left/total, product*slope/2,
                    product*((right-left)/total*slope**2+curvature)/4)

        def source(eta: mp.mpf) -> mp.mpc:
            _, dc, ddc = switch(eta)
            if dc == ddc == 0:
                return mp.mpc(0)
            u, du = mode(eta)
            return ddc*u+2*dc*du

        def forced(eta: mp.mpf) -> mp.mpc:
            return switch(eta)[0]*mode(eta)[0]

        def freq2(eta: mp.mpf) -> mp.mpf:
            x = mp.tanh(eta)
            return 6+2*mp.sqrt(10)*x+x*x/2

        # An independent derivative check of the smooth switch and forced ODE.
        for eta in (mp.mpf('-.6'), mp.mpf('0'), mp.mpf('.7')):
            chi, dc, ddc = switch(eta)
            assert abs(mp.diff(lambda t: switch(t)[0], eta)-dc) < tol
            assert abs(mp.diff(lambda t: switch(t)[0], eta, 2)-ddc) < tol
            assert abs(mp.diff(forced, eta, 2)+freq2(eta)*forced(eta)-source(eta)) < tol
        assert forced(mp.mpf(-2)) == source(mp.mpf(-2)) == 0
        assert source(mp.mpf(2)) == 0

        interval = [mp.mpf(-1), mp.mpf('-.5'), mp.mpf(0), mp.mpf('.5'), mp.mpf(1)]
        # Retarded Green: [u(xi)u*(eta)-u*(xi)u(eta)]/i for eta>xi.
        # Thus late coefficients are A_J=i int u* J, B_J=-i int u J.
        good = 1j*mp.quad(lambda t: mp.conj(mode(t)[0])*source(t), interval)
        bad = -1j*mp.quad(lambda t: mode(t)[0]*source(t), interval)
        assert abs(good-1) < tol and abs(bad) < tol
        u, du = mode(mp.mpf(2))
        retarded_late = good*u+bad*mp.conj(u)
        assert abs(retarded_late-forced(mp.mpf(2))) < tol
        assert abs(1j*(mp.conj(u)*du-mp.conj(du)*u)-1) < tol
        # A smooth allowed scalar source perturbation leaves the regular kernel:
        # J_error=chi' u*, so B_error=-i int chi' |u|^2 is provably nonzero.
        sensitivity = mp.quad(lambda t: switch(t)[1]*abs(mode(t)[0])**2, interval)
        assert sensitivity > 0

        def D(x: mp.mpf) -> mp.mpf:
            return (x+delta)**2-4*(x*x-1)/(k+2)

        def regular_tortoise_derivative(x: mp.mpf) -> mp.mpf:
            # r_* = d/2 log(|(1-x)/2|) + s(x), s(1)=0.
            # Rationalization removes the apparent 0/0 at x=1 in s'.
            aa = 4-16/(k+2)-d*d
            bb = d*d-4*delta*delta-16/(k+2)
            return (aa*x+bb)/(2*(x+1)*(2*mp.sqrt(D(x))+d*(x+1)))

        def regular_mode(x: mp.mpf) -> tuple[mp.mpc, mp.mpc, mp.mpc]:
            z = (1-x)/2
            phase_integral = mp.quad(regular_tortoise_derivative, [mp.mpf(1), x])
            sp = regular_tortoise_derivative(x)
            spp = mp.diff(regular_tortoise_derivative, x)
            f = mp.hyp2f1(a, b, c, z)
            f1 = a*b/c*mp.hyp2f1(a+1, b+1, c+1, z)
            f2 = a*b*(a+1)*(b+1)/(c*(c+1))*mp.hyp2f1(a+2, b+2, c+2, z)
            hz = -bh*(1-z)**(bh-1)*f+(1-z)**bh*f1
            hzz = bh*(bh-1)*(1-z)**(bh-2)*f-2*bh*(1-z)**(bh-1)*f1+(1-z)**bh*f2
            hh = (1-z)**bh*f
            phase = mp.exp(-1j*omega*phase_integral)/normalization
            return (phase*hh, phase*(-hz/2-1j*omega*sp*hh),
                    phase*(hzz/4+1j*omega*sp*hz+(-1j*omega*spp-omega**2*sp**2)*hh))

        max_regular_residual = mp.mpf(0)
        for x in (mp.mpf(0), mp.mpf('.8'), mp.mpf(1), mp.mpf('1.2'), mp.mpf(2)):
            g, gp, gpp = regular_mode(x)
            sqrtD = mp.sqrt(D(x))
            Dp = 2*(x+delta)-8*x/(k+2)
            residual = abs((x*x-1)*gpp+(2*x+2j*omega*sqrtD)*gp+
                           (1j*omega*Dp/(2*sqrtD)-angular)*g)
            max_regular_residual = max(max_regular_residual, residual)
            assert residual < tol
        gh, gph, _ = regular_mode(mp.mpf(1))
        expected_slope = (angular-1j*omega*(2*d-8/(k+2))/(2*d))/(2+2j*omega*d)*gh
        assert abs(gh-1/normalization) < tol
        assert abs(gph-expected_slope) < tol
        # Independent numerical derivative check across the regular interface.
        assert abs(mp.diff(lambda x: regular_mode(x)[0], mp.mpf(1))-gph) < tol
        g2 = regular_mode(mp.mpf(2))[0]
        assert abs(g2) > mp.mpf('.01')
        print(f'dps={dps}; |A_J-1|={mp.nstr(abs(good-1), 5)}; |B_J|={mp.nstr(abs(bad), 5)}')
        print(f'dps={dps}; error_source_bad_amplitude/epsilon=-i*{mp.nstr(sensitivity, 40)}')
        print(f'dps={dps}; regular_G(x=2)={mp.nstr(g2, 40)}; regular_ODE_residual={mp.nstr(max_regular_residual, 5)}')
        print('Same zero early data, compact-in-Taub-time source, unit-KG late scalar mode.')
        return +g2, +sensitivity


def main() -> None:
    print(f'Python {platform.python_version()}; mpmath {mp.__version__}')
    low, high = calculate(50), calculate(80)
    with mp.workdps(80):
        assert max(abs(a-b) for a, b in zip(low, high)) < mp.mpf('1e-36')
    print('Negative control: generic smooth source error creates a nonregular branch.')
    print('Source is prescribed and spatially extended; no local string-source certification.')
    print('No source-dependent response before the source inside Taub; delta_g=0 by assumption.')
    print('No NUT quantum detector distribution or operational past signal computed.')
    print('PASS scalar-control assertions; all_six_physical_gates_passed=False')


if __name__ == '__main__':
    main()
