#!/usr/bin/env python3
"""Exact Taub scalar transfer for a restricted neutral candidate family.

Gamma connection coefficients, a separate hyperbolic expression, the ODE,
Wronskians, and function-level connection identities are checked at 50/80 dps.
These are scalar diagnostics, NOT string amplitudes or signal probabilities.
No affine spectral-flow/GSO/global gluing membership is inferred.
"""
from __future__ import annotations

import platform
import mpmath as mp


def calculate(dps: int) -> list[tuple[mp.mpf, mp.mpf]]:
    with mp.workdps(dps):
        tol = mp.mpf(10)**(-(dps-12))
        delta, lam = mp.sqrt(mp.mpf(8)/5), mp.sqrt(mp.mpf(2)/5)
        maxima = {'ode': mp.mpf(0), 'wronskian': mp.mpf(0),
                  'connection': mp.mpf(0), 'rate': mp.mpf(0)}
        result = []
        for n, ell, s2 in ((2, mp.mpf(1), mp.mpf(1)/4),
                           (3, mp.mpf(3)/2, mp.mpf(13)/8),
                           (4, mp.mpf(2), mp.mpf(15)/4)):
            omega, s = n/(2*lam), mp.sqrt(s2)
            angular = ell*(ell+1)-mp.mpf(n*n)/4
            assert abs(s2-(mp.mpf(3)/5*omega**2-angular-mp.mpf(1)/4)) < tol
            om, op = omega*(delta-1), omega*(delta+1)
            ah, bh, h = 1j*op/2, -1j*om/2, -mp.mpf(1)/2+1j*s
            a, b = ah+bh-h, ah+bh+h+1
            ci, co = 1+2*bh, 1+2*ah
            A = mp.sqrt(op/om)*mp.gamma(ci)*mp.gamma(-2*ah)/(
                mp.gamma(ci-a)*mp.gamma(ci-b))
            B = mp.sqrt(op/om)*mp.gamma(ci)*mp.gamma(2*ah)/(
                mp.gamma(a)*mp.gamma(b))
            B2 = abs(B)**2
            closed = mp.cosh(mp.pi*(omega-s))*mp.cosh(mp.pi*(omega+s))/(
                mp.sinh(mp.pi*om)*mp.sinh(mp.pi*op))
            maxima['rate'] = max(maxima['rate'], abs(B2-closed))
            assert abs(B2-closed) < tol
            assert B2 > 0
            assert abs(abs(A)**2-B2-1) < tol

            def mode(eta: mp.mpf, incoming: bool = False) -> mp.mpc:
                z = (1-mp.tanh(eta))/2
                prefactor = z**ah*(1-z)**bh
                return prefactor*(mp.hyp2f1(a, b, ci, 1-z)/mp.sqrt(2*om)
                                  if incoming else mp.hyp2f1(a, b, co, z)/mp.sqrt(2*op))

            def freq2(eta: mp.mpf) -> mp.mpf:
                x = mp.tanh(eta)
                return omega**2*((x+delta)**2+mp.mpf(4)/10*(1-x*x))+angular*(1-x*x)

            for eta in (mp.mpf('-1'), mp.mpf('0'), mp.mpf('0.7')):
                u, du = mode(eta), mp.diff(mode, eta)
                ode = abs(mp.diff(mode, eta, 2)+freq2(eta)*u)/(1+abs(freq2(eta)*u))
                wr = abs(1j*(mp.conj(u)*du-mp.conj(du)*u)-1)
                connection = abs(mode(eta, True)-A*u-B*mp.conj(u))
                maxima['ode'] = max(maxima['ode'], ode)
                maxima['wronskian'] = max(maxima['wronskian'], wr)
                maxima['connection'] = max(maxima['connection'], connection)
                assert max(ode, wr, connection) < tol
                # Future-regular solution in the past basis; it has unit KG norm.
                ui = mode(eta, True)
                assert abs(u-(mp.conj(A)*ui-B*mp.conj(ui))) < tol
            # For Haar-orthonormal spatial modes and unit incoming coefficients:
            # lim (x-1)^2 ||d_x Phi_bad||^2 = sum Omega_+ |B|^2/2.
            result.append((+B2, +(op*B2/2)))
            print(f'dps={dps}; n={n}; ell={ell}; s2={s2}; '
                  f'beta2={mp.nstr(B2, 42)}; bad_derivative_coefficient={mp.nstr(op*B2/2, 32)}')
        print(f'dps={dps}; residuals:', {k: mp.nstr(v, 5) for k, v in maxima.items()})
        # Orthogonality/positivity negative control: opposite amplitudes do not
        # cancel the integrated bad branch in different Fourier/harmonic modes.
        assert result[0][1]+result[1][1] > 0
        print('Different-mode amplitudes +1,-1 have positive integrated bad-branch weight.')
        return result


def main() -> None:
    print(f'Python {platform.python_version()}; mpmath {mp.__version__}')
    low, high = calculate(50), calculate(80)
    with mp.workdps(80):
        for l, h in zip(low, high):
            for lv, hv in zip(l, h):
                assert abs(lv-hv) < mp.mpf('1e-38')
    print('For real s, omega>0, delta>1, the displayed cosh/sinh expression is strictly positive.')
    print('This excludes simultaneous pure-positive in/out branches in this scalar continuum.')
    print('Tuned positive-KG out modes remain; source control is a separate calculation.')
    print('PASS scalar transfer assertions; all_six_physical_gates_passed=False')


if __name__ == '__main__':
    main()
