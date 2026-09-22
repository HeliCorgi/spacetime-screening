#!/usr/bin/env python3
"""Six-gate chronology audit: algebra, scalar time evolution and causal limits.

This does NOT certify full heterotic BRST cohomology, its physical norm,
a modular-invariant spectrum, a backreacted solution or past signalling.
No network/files are read. --json writes calculated evidence to a chosen path.
Dependencies: sympy==1.14.0, mpmath==1.3.0. See the companion research note.
"""
from __future__ import annotations
import argparse
import json
import math
import platform
from pathlib import Path
import mpmath as mp
import sympy as sp


def algebra() -> dict:
    # Recheck the old candidate, without promoting these equations to BRST.
    k1, k2 = sp.Integer(8), sp.Integer(4)
    de, la = sp.sqrt(sp.Rational(8, 5)), sp.sqrt(sp.Rational(2, 5))
    qa, pa, qb, pb = 2, 0, 2, 1
    anomalies = [-k1*(1-de**2)-2*(qa**2+pa**2-de**2),
                 k1*de*la-2*(qa*qb+pa*pb-de*la),
                 k2+k1*la**2-2*(qb**2+pb**2-1-la**2)]
    assert all(sp.simplify(a) == 0 for a in anomalies)
    j, ell, m, mb, nb = sp.Rational(1, 2)+sp.I/2, 1, -2, sp.sqrt(10)/2, -1
    assert sp.simplify(m+de*mb) == sp.simplify(la*mb+nb) == 0
    level = sp.Matrix([[8, 4], [4, 5]])
    num = sp.simplify(-j*(j-1)/(k1-2)+sp.Rational(ell*(ell+1), k2+2))
    sub = (sp.Matrix([m, 0]).T*level.inv()*sp.Matrix([m, 0]))[0]/2
    assert num == sub == sp.Rational(5, 12)
    s = sp.Symbol('s', real=True)
    formal_h = sp.simplify((sp.Rational(1, 4)+s**2+2)/6-sub)
    assert sp.simplify(formal_h-(s**2-sp.Rational(1, 4))/6) == 0

    # SU(2) current algebra: E=J^+_-1, F=J^-_1,
    # [F,E]=k-2J3_0. F E^n|0> = n(k-n+1) E^(n-1)|0>.
    # Norm recurrence is exact; the integrable quotient removes the null vector.
    def su2_norm(k: int, n: int) -> int:
        result = 1
        for r in range(1, n+1):
            result *= r*(k-r+1)
        return result
    norms = [su2_norm(4, n) for n in range(9)]
    assert norms[:5] == [1, 4, 24, 144, 576]
    assert all(n == 0 for n in norms[5:])
    old_grade, claimed_grade = 4*2, 4*2**2
    assert old_grade == 8 and claimed_grade == 16 and old_grade != claimed_grade

    # Neutral scalar angular mode: ell=1, q=1, m_phi=0.
    th = sp.Symbol('theta', real=True)
    angular = sp.diff(sp.sin(th)*sp.diff(sp.sin(th), th), th)/sp.sin(th) \
              - sp.cos(th)**2/sp.sin(th)
    assert sp.trigsimp(angular+sp.sin(th)) == 0
    assert sp.integrate(sp.sin(th)**3, (th, 0, sp.pi)) == sp.Rational(4, 3)

    # Taub time x=tanh(eta): (p R_x)_x + (omega^2 D/p-Lambda)R=0
    # becomes R_etaeta + (omega^2 D-Lambda*p)R=0.
    x = sp.Symbol('x', real=True)
    p = x*x-1
    D = (x+de)**2-sp.Rational(2, 5)*p
    O2 = sp.expand(sp.Rational(5, 2)*D-p)
    assert sp.simplify(O2-(6+2*sp.sqrt(10)*x+x*x/2)) == 0
    assert O2.subs(x, 0) == 6

    # Regular outgoing horizon chart, chosen for future increasing x in Taub.
    K, Dh, vx = sp.symbols('K Dh vx', positive=True)
    g_h = sp.Matrix([[0, -K/sp.sqrt(Dh)], [-K/sp.sqrt(Dh), 0]])
    v_tau = sp.Symbol('v_tau', real=True)
    v = sp.Matrix([v_tau, vx])
    n = sp.Matrix([1, 0])
    inner = sp.simplify((v.T*g_h*n)[0])
    assert inner == -K*vx/sp.sqrt(Dh)

    # Two-stream invariant in an ingoing regular chart (independent of the
    # choice of the future extension): assumptions A,B are explicit.
    pp, DD, AA, BB = sp.symbols('p D A B', positive=True)
    g = K*sp.Matrix([[-pp/DD, 1/sp.sqrt(DD)], [1/sp.sqrt(DD), 0]])
    li, no = sp.Matrix([1, 0]), sp.Matrix([1, -2*sp.sqrt(DD)/pp])
    inv = g.inv()
    assert sp.simplify((li.T*inv*li)[0]) == 0
    assert sp.simplify((no.T*inv*no)[0]) == 0
    stress = AA*li*li.T+BB*no*no.T
    invariant = sp.simplify(sp.trace((inv*stress)**2))
    assert sp.simplify(invariant-8*AA*BB*DD**2/(K**2*pp**2)) == 0

    return {'anomaly_residuals': ['0']*3, 'formal_weight': str(num-sub),
            'formal_weight_family': str(formal_h),
            'su2_k4_norms_n0_to_n8': norms,
            'fable_w2_literal_grade': old_grade, 'fable_w2_claimed_grade': claimed_grade,
            'taub_Omega_squared': str(O2),
            'future_exit_horizon_inner_product': str(inner),
            'assumed_two_stream_invariant': str(invariant)}


def scalar_calculation(dps: int) -> dict:
    with mp.workdps(dps):
        I = mp.j
        w = mp.sqrt(10)/2
        de = mp.sqrt(mp.mpf(8)/5)
        la = mp.sqrt(mp.mpf(2)/5)
        Op, Om = 2+w, 2-w
        h = -mp.mpf('0.5')+I/2
        # Future regular branch on outgoing extension: z^(+i Omega_+/2).
        al, be = I*Op/2, I*Om/2
        a, b, c = al+be-h, al+be+h+1, 1+2*al
        def future_mode(z):
            return z**al*(1-z)**be*mp.hyp2f1(a, b, c, z)
        def future_dz(z):
            F = mp.hyp2f1(a, b, c, z)
            return z**al*(1-z)**be*((al/z-be/(1-z))*F
                    + a*b/c*mp.hyp2f1(a+1, b+1, c+1, z))
        def O2(eta):
            x = mp.tanh(eta)
            return 6+2*mp.sqrt(10)*x+x*x/2
        def f_eta(eta):
            return future_mode((1-mp.tanh(eta))/2)
        residuals, norms = [], []
        for eta in [mp.mpf('-1'), mp.mpf('0'), mp.mpf('0.7'), mp.mpf('2')]:
            f = f_eta(eta)
            df = mp.diff(f_eta, eta)
            ddf = mp.diff(f_eta, eta, 2)
            residuals.append(abs(ddf+O2(eta)*f)/(1+abs(ddf)+abs(O2(eta)*f)))
            norms.append(abs(I*(mp.conj(f)*df-f*mp.conj(df))-2*Op))
        tolerance = mp.power(10, -(dps-15))
        assert max(residuals) < tolerance and max(norms) < tolerance

        # Instantaneous positive-frequency, KG-unit-normalized initial data.
        finite_time = []
        for eta0 in [0, 1, 2, 4]:
            xx = mp.tanh(eta0); z = (1-xx)/2; p = xx*xx-1
            O0 = mp.sqrt(O2(eta0))
            f, fs = future_mode(z), future_dz(z)*p/2
            u0 = 1/mp.sqrt(2*O0)
            du0 = -I*O0*u0
            C, E = mp.lu_solve(mp.matrix([[f, mp.conj(f)], [fs, mp.conj(fs)]]),
                              mp.matrix([u0, du0]))
            alpha, beta = mp.sqrt(2*Op)*C, mp.sqrt(2*Op)*E
            assert abs(abs(alpha)**2-abs(beta)**2-1) < tolerance
            finite_time.append({'eta0': eta0, 'beta_squared': mp.nstr(abs(beta)**2, 38)})
        # Tuned future-regular data: the second coefficient must vanish.
        f, fs = future_mode(mp.mpf('.5')), -future_dz(mp.mpf('.5'))/2
        C, E = mp.lu_solve(mp.matrix([[f, mp.conj(f)], [fs, mp.conj(fs)]]),
                          mp.matrix([f/mp.sqrt(2*Op), fs/mp.sqrt(2*Op)]))
        assert abs(E) < tolerance

        # Past-to-future Taub basis: no exterior-radial reciprocity assumption.
        al, be = I*Op/2, -I*Om/2
        aa, bb, ci = al+be-h, al+be+h+1, 1+2*be
        AB = mp.sqrt(Op/Om)*mp.gamma(ci)*mp.gamma(-2*al)/(mp.gamma(ci-aa)*mp.gamma(ci-bb))
        BBog = mp.sqrt(Op/Om)*mp.gamma(ci)*mp.gamma(2*al)/(mp.gamma(aa)*mp.gamma(bb))
        n_inout = abs(BBog)**2
        n_closed = mp.cosh(mp.pi*(w-mp.mpf('.5')))*mp.cosh(mp.pi*(w+mp.mpf('.5'))) \
                   /(mp.sinh(mp.pi*Om)*mp.sinh(mp.pi*Op))
        assert abs(n_closed-n_inout) < tolerance
        assert abs(abs(AB)**2-abs(BBog)**2-1) < tolerance
        # Verify the 1-z connection at interior points, not only Gamma arithmetic.
        for zz in [mp.mpf('.15'), mp.mpf('.4')]:
            fin = zz**al*(1-zz)**be*mp.hyp2f1(aa, bb, ci, 1-zz)/mp.sqrt(2*Om)
            fout = zz**al*(1-zz)**be*mp.hyp2f1(aa, bb, 1+2*al, zz)/mp.sqrt(2*Op)
            assert abs(fin-AB*fout-BBog*mp.conj(fout)) < tolerance

        # The historical exterior radial flux fraction: different observable.
        R = mp.cosh(mp.pi*(w-mp.mpf('.5')))*mp.cosh(mp.mpf('1.5')*mp.pi) \
             /(mp.cosh(mp.pi*(w+mp.mpf('.5')))*mp.cosh(mp.mpf('2.5')*mp.pi))
        T = mp.sinh(mp.pi*(w+2))*mp.sinh(mp.pi) \
             /(mp.cosh(mp.pi*(w+mp.mpf('.5')))*mp.cosh(mp.mpf('2.5')*mp.pi))
        assert abs(T+R-1) < tolerance
        # Positive x=2 loop is kinematic only; it already exists in the metric.
        x0, K = mp.mpf(2), mp.mpf(6)
        p = x0*x0-1; D = (x0+de)**2-mp.mpf('.4')*p
        Dp = mp.mpf('1.2')*x0+2*de
        period = 4*mp.pi*la
        proper = period*mp.sqrt(K*p/D)
        acc2 = p/(4*K)*(2*x0/p-Dp/D)**2
        return {'dps': dps, 'maximum_relative_ODE_residual': mp.nstr(max(residuals), 8),
                'maximum_mode_Wronskian_error': mp.nstr(max(norms), 8),
                'finite_time_preparations': finite_time,
                'tuned_future_regular_beta_squared': mp.nstr(abs(E)**2, 8),
                'Taub_in_out_beta_squared': mp.nstr(n_inout, 38),
                'Taub_in_out_alpha_squared': mp.nstr(abs(AB)**2, 38),
                'exterior_radial_T_NOT_signal_probability': mp.nstr(T, 38),
                'radial_L2_log_coefficient_NOT_BRST_norm': mp.nstr(2*(1+R), 38),
                'outgoing_envelope_decay_threshold_gamma': mp.nstr(1/(1+de), 30),
                'kinematic_loop_x2_proper_time_string_units': mp.nstr(proper, 30),
                'kinematic_loop_x2_acceleration_squared_string_units': mp.nstr(acc2, 30)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json', type=Path)
    args = parser.parse_args()
    a = algebra()
    low, high = scalar_calculation(50), scalar_calculation(80)
    with mp.workdps(60):
        assert abs(mp.mpf(low['Taub_in_out_beta_squared'])
                   -mp.mpf(high['Taub_in_out_beta_squared'])) < mp.mpf('1e-35')
        for x, y in zip(low['finite_time_preparations'], high['finite_time_preparations']):
            assert abs(mp.mpf(x['beta_squared'])-mp.mpf(y['beta_squared'])) < mp.mpf('1e-35')
    report = {'scope': 'Necessary algebra and neutral scalar/causal diagnostics only',
              'all_six_physical_gates_passed': False,
              'environment': {'python': platform.python_version(), 'sympy': sp.__version__,
                              'mpmath': mp.__version__},
              'algebra': a, 'scalar_50_digits': low, 'scalar_80_digits': high}
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=False, indent=2))
    print('PASS: the specified calculations; NOT a full-spectrum or signalling certificate.')


if __name__ == '__main__':
    main()
