#!/usr/bin/env python3
"""State-independent negative-null-energy gate in the specified leading MMP/JT model.

The circle QEI follows analytically from the positive-energy Virasoro
representation and its Schwarzian transformation law; this script verifies
its coefficients, the JT null constraint, and independent numerical controls.
It does not prove those representation-theoretic premises or 4D chronology
protection. In particular, a null-line QEI is NOT imported into 4D.
"""
from __future__ import annotations

import platform
import sympy as sp
import mpmath as mp


def symbolic_checks() -> None:
    v, sigma, tau = sp.symbols('v sigma tau', real=True)
    ell, cc, kap, length, eps = sp.symbols('ell c kappa L epsilon', positive=True)
    f = sp.Function('phi')(tau, sigma)
    g = sp.diag(-1 / sp.cos(sigma)**2, 1 / sp.cos(sigma)**2)
    inv = g.inv()
    coords = (tau, sigma)
    connection = [[[sp.simplify(sum(inv[a, d] * (
        sp.diff(g[d, b], coords[c]) + sp.diff(g[d, c], coords[b])
        - sp.diff(g[b, c], coords[d])) / 2 for d in range(2)))
        for c in range(2)] for b in range(2)] for a in range(2)]
    hdd = sum(sp.diff(f, coords[a], coords[b])
              - sum(connection[k][a][b] * sp.diff(f, coords[k])
                    for k in range(2)) for a in range(2) for b in range(2))
    df = sp.diff(f, tau) + sp.diff(f, sigma)
    dd = sp.diff(df, tau) + sp.diff(df, sigma)
    assert sp.simplify(hdd - dd + 2 * sp.tan(sigma) * df) == 0
    # The derivative along the ray tau=sigma+constant gives the exact weight.
    weighted = (sp.diff(sp.cos(sigma)**2 * df, tau)
                + sp.diff(sp.cos(sigma)**2 * df, sigma))
    assert sp.simplify(weighted - sp.cos(sigma)**2 * hdd) == 0
    # MMP conformal anomaly: trace terms have zero null contraction.
    omega = -sp.log(sp.cos(sigma))
    anomaly = -cc / (12 * sp.pi) * (sp.diff(omega, sigma)**2
                                  - sp.diff(omega, sigma, 2))
    assert sp.trigsimp(anomaly - cc / (12 * sp.pi)) == 0
    i_anomaly = sp.integrate(cc / (12 * sp.pi) * sp.cos(sigma)**2,
                             (sigma, -sp.pi / 2, sp.pi / 2))
    assert i_anomaly == cc / 24
    w = sp.sin(v / (2 * ell))**2
    assert sp.trigsimp(w.subs(v, 2 * ell * (sigma + sp.pi / 2))
                       - sp.cos(sigma)**2) == 0
    dw_norm = sp.integrate(sp.diff(sp.sin(v / (2 * ell)), v)**2,
                            (v, 0, 2 * sp.pi * ell))
    assert dw_norm == sp.pi / (4 * ell)
    qei_line = -cc / (12 * sp.pi) * dw_norm
    assert sp.simplify(i_anomaly + 2 * ell * qei_line) == 0

    # Circle formula: V'=a/h, Schwarzian=-h''/h+(h'/h)^2/2.
    h = sp.Function('h')(v)
    scale = sp.symbols('a', positive=True)
    vp = scale / h
    schwarz = sp.diff(vp, v, 2) / vp - sp.Rational(3, 2) * (sp.diff(vp, v) / vp)**2
    assert sp.simplify(schwarz + sp.diff(h, v, 2) / h
                       - sp.diff(h, v)**2 / (2 * h**2)) == 0
    assert sp.simplify(h * schwarz + sp.diff(h, v, 2)
                       - sp.diff(h, v)**2 / (2 * h)) == 0
    integral_inv = sp.symbols('J', positive=True)
    e0 = -sp.pi * cc / (12 * length)
    assert sp.simplify(length / integral_inv * e0
                       + sp.pi * cc / (12 * integral_inv)) == 0

    # A finite-energy refinement from h=w+eps (smooth approximation in note).
    tw, gap, work = sp.symbols('tau_w gap W', positive=True)
    L = 2 * tw + gap
    energy = -sp.pi * cc / (12 * L) + work
    A = cc / 12 + cc * tw / (6 * gap) + 2 * tw * energy / sp.pi
    assert sp.simplify(A - (cc / 12 + cc * tw / (6 * gap)
                            - cc * tw / (6 * L) + 2 * tw * work / sp.pi)) == 0
    t = sp.symbols('sqrt_epsilon', positive=True)
    lower = cc * t / 12 - A * t**2
    best_t = cc / (24 * A)
    assert sp.simplify(lower.subs(t, best_t) - cc**2 / (576 * A)) == 0
    assert sp.simplify(sp.diff(lower, t).subs(t, best_t)) == 0
    # A>0 for W>=0: 1/gap-1/L=2 tau_w/(gap L)>0.
    assert sp.simplify(1 / gap - 1 / L - 2 * tw / (gap * L)) == 0

    tau_w = sp.symbols('tau_w', positive=True)
    i_vac = cc / 24 * (1 - 4 * tau_w**2 / length**2)
    assert sp.simplify(i_vac.subs({tau_w: 1, length: sp.Rational(9, 4)})
                       - 17 * cc / 1944) == 0
    assert sp.simplify(i_vac.subs(length, 2 * tau_w)) == 0
    # A wrapping-circle control: the ordinary long MMP branch is NOT excluded.
    assert sp.simplify(i_vac.subs({tau_w: 1, length: sp.Rational(5, 4)})
                       + sp.Rational(13, 200) * cc) == 0
    assert sp.trigsimp(sp.sin(v / (2 * ell))**2
                      + sp.sin((v + sp.pi * ell) / (2 * ell))**2 - 1) == 0
    print('EXACT: general JT null constraint and MMP anomaly contribute +c/24.')
    print('EXACT: nonwrapping chiral QEI contributes at least -c/24; I_total>=0.')
    print('EXACT: at tau_w=1,L=9/4, I_extra>=-17*c/1944, but rescue requires strict <.')
    print('EXACT: finite-energy bound I>=c^2/(576 A)>0 for L>2*tau_w.')
    print('WRAPPING CONTROL: tau_w=1,L=5/4 has I_vac=-13*c/200 and is outside this QEI gate.')


def require_nonwrapping(tau_w: mp.mpf, period: mp.mpf) -> None:
    if tau_w <= 0 or period <= 0:
        raise ValueError('Both optical duration and chiral period must be positive.')
    if period < 2 * tau_w:
        raise ValueError('The sampling path wraps: periodize the weight instead of using a null-line bound.')


def quadrature_checks(dps: int) -> list[mp.mpf]:
    with mp.workdps(dps):
        tw, L, cc = mp.mpf(1), mp.mpf(9) / 4, mp.mpf(1)
        ell = tw / mp.pi
        require_nonwrapping(tw, L)
        require_nonwrapping(tw, 2 * tw)
        for bad in ((tw, mp.mpf(5) / 4), (mp.mpf(0), L)):
            try:
                require_nonwrapping(*bad)
            except ValueError:
                pass
            else:
                raise AssertionError('Invalid QEI geometry was silently accepted.')
        results = []
        for ep in (mp.mpf(1) / 4, mp.mpf(1) / 100, mp.mpf(1) / 10000):
            weight = lambda x: mp.sin(mp.pi * x / (2 * tw))**2
            dw = lambda x: mp.pi / (2 * tw) * mp.sin(mp.pi * x / tw)
            bounds = [0, tw / 8, tw / 2, tw, 3 * tw / 2, 15 * tw / 8, 2 * tw]
            J_num = (L - 2 * tw) / ep + mp.quad(lambda x: 1 / (ep + weight(x)), bounds)
            J = (L - 2 * tw) / ep + 2 * tw / mp.sqrt(ep * (1 + ep))
            D_num = mp.quad(lambda x: dw(x)**2 / (ep + weight(x)), bounds)
            D = mp.pi**2 / tw * (1 + 2 * ep - 2 * mp.sqrt(ep * (1 + ep)))
            tol = mp.power(10, -dps + 8)
            assert abs(J_num - J) < tol
            assert abs(D_num - D) < tol
            for W in (mp.mpf(0), mp.mpf(1), mp.mpf(10)):
                E = -mp.pi * cc / (12 * L) + W
                refined = cc / 24 - 2 * ell * (mp.pi * cc / (12 * J)
                                             + cc * D / (48 * mp.pi) + ep * E)
                A = cc / 12 + cc * tw / (6 * (L - 2 * tw)) + 2 * tw * E / mp.pi
                crude = cc * mp.sqrt(ep) / 12 - ep * A
                assert refined >= crude - tol
            results.extend((+J, +D))
        # Independent direct integration of the actual ray weight.
        i_vac_num = mp.quad(lambda x: mp.cos(x)**2 * (
            cc / (12 * mp.pi) - mp.pi * cc * ell**2 / (3 * L**2)),
            [-mp.pi/2, 0, mp.pi/2])
        assert abs(i_vac_num - mp.mpf(17)/1944) < mp.power(10, -dps + 8)
        bad_addition = -mp.mpf(17) / 1944 - mp.mpf(1) / 1000
        assert i_vac_num + bad_addition < 0  # A rejected source, not a constructed state.
        for W in (mp.mpf(0), mp.mpf('0.1'), mp.mpf(1), mp.mpf(10)):
            E = -mp.pi / (12 * L) + W
            A = cc/12 + cc*tw/(6*(L-2*tw)) + 2*tw*E/mp.pi
            bound = cc**2/(576*A)
            assert bound > 0
            results.append(+bound)
            print(f'dps={dps}; prep work W={W}; finite-energy lower bound I>={mp.nstr(bound, 35)}')
        results.append(+i_vac_num)
        print(f'dps={dps}; vacuum deficit={mp.nstr(i_vac_num, 40)}; '
              'allowed extra >= -deficit, not strictly below it.')
        return results


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}; mpmath {mp.__version__}')
    symbolic_checks()
    low, high = quadrature_checks(50), quadrature_checks(80)
    with mp.workdps(100):
        assert len(low) == len(high)
        assert all(abs(a-b) < mp.mpf('1e-40') for a, b in zip(low, high))
    print('PASS QEI/JT algebra and 50/80-digit integrals. Analytic theorem and domain in note.')
    print('No extra negative source, full 4D apparatus, time-dependent holonomy or past signalling certified.')


if __name__ == '__main__':
    main()
