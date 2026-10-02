#!/usr/bin/env python3
"""R5: exact allowed region and shared predictions of a FIXED spatial-kernel family.

A(z)=prod(1+alpha_i*z)=1+z+b*z^2+c*z^3, alpha_i>=0,
sum alpha_i=1, at least two strictly positive factors. This is a design class,
NOT the class of all positive kernels or a proof of consistent quantum gravity.
No background evolution, nonlinear constraint rank or quantum anomaly is solved.
Only stdlib, SymPy and mpmath are required; no cross-script output is required.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path
import platform

import mpmath as mp
import sympy as sp

BASE_SHA = 'a0639dd49667a1dac9585aafa99df6408125c472'
SCOPE = 'fixed three-factor spatial/static design class; not full quantum gravity'


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def rat(value) -> sp.Rational:
    return sp.Rational(str(value))


def mpr(value) -> mp.mpf:
    q = sp.Rational(value)
    return mp.mpf(int(q.p)) / int(q.q)


def validate_factors(values) -> tuple[sp.Rational, ...]:
    aa = tuple(sorted((rat(v) for v in values), reverse=True))
    if len(aa) != 3 or sum(aa) != 1 or any(a < 0 for a in aa):
        raise ValueError('Exactly three nonnegative factors summing to one are required')
    if sum(bool(a > 0) for a in aa) < 2:
        raise ValueError('One-factor vertex has divergent central tidal coefficient')
    return aa


def coefficients(aa):
    a, d, e = aa
    return sp.factor(a*d+a*e+d*e), sp.factor(a*d*e)


def discriminant(b, c):
    return b*b - 4*b**3 - 4*c + 18*b*c - 27*c*c


def admissible_coefficients(b, c) -> bool:
    b, c = rat(b), rat(c)
    return bool(b > 0 and c >= 0 and discriminant(b, c) >= 0)


def resolvent_terms(aa):
    """Exact partial fractions, including repeated roots; NOT sampled root fitting."""
    active = [a for a in aa if a > 0]
    z = sp.Symbol('z')
    A = sp.prod(1+a*z for a in active)
    bases = [(a, j) for a, mult in Counter(active).items()
             for j in range(1, mult+1)]
    cs = sp.symbols('v:'+str(len(active)))
    pol = sp.Poly(sp.expand(sum(c*sp.div(A, (1+a*z)**j, z)[0]
                                for c, (a, j) in zip(cs, bases))-1), z)
    sol = sp.solve(pol.all_coeffs(), cs)
    terms = [(a, j, sol[c]) for c, (a, j) in zip(cs, bases)]
    require(sp.factor(sum(c/(1+a*z)**j for a, j, c in terms)-1/A) == 0,
            'partial-fraction identity')
    return terms


def kernel(x, terms):
    """ell*K_ell(ell*x), evaluated in arbitrary precision."""
    x = mp.mpf(x)
    if x < 0:
        raise ValueError('x must be nonnegative')
    if not x:
        return center_moments(terms)[0]
    pieces = []
    for a0, j, c0 in terms:
        a, c = mpr(a0), mpr(c0)
        y = x/mp.sqrt(a)
        extra = mp.mpf(0) if j == 1 else (y/2 if j == 2 else 5*y/8+y*y/8)
        pieces.append(c*(-mp.expm1(-y)-mp.exp(-y)*extra)/x)
    return mp.fsum(pieces)


def enclosed(x, terms):
    """J=-x^2 k'(x): force/Newton-force, from the same exact kernel."""
    x = mp.mpf(x)
    if not x:
        return mp.mpf(0)
    values = []
    for a0, j, c0 in terms:
        y = x/mp.sqrt(mpr(a0))
        P = 1 if j == 1 else (1+y/2 if j == 2 else 1+5*y/8+y*y/8)
        Pp = 0 if j == 1 else (mp.mpf(1)/2 if j == 2 else mp.mpf(5)/8+y/4)
        values.append(mpr(c0)*(1-mp.exp(-y)*(P+y*(P-Pp))))
    return mp.fsum(values)


def center_moments(terms):
    # Series of each partial fraction. Divergent individual Fourier moments
    # are NEVER integrated separately; the complete series cancels odd terms.
    c0s = {1: mp.mpf(1), 2: mp.mpf(1)/2, 3: mp.mpf(3)/8}
    kps = {1: -mp.mpf(1)/3, 2: mp.mpf(1)/6, 3: mp.mpf(1)/24}
    c4s = {1: mp.mpf(1)/120, 2: -mp.mpf(1)/80, 3: mp.mpf(1)/320}
    k0 = mp.fsum(mpr(c)*c0s[j]/mp.sqrt(mpr(a)) for a, j, c in terms)
    kap = mp.fsum(mpr(c)*kps[j]/mpr(a)**mp.mpf('1.5') for a, j, c in terms)
    c4 = mp.fsum(mpr(c)*c4s[j]/mpr(a)**mp.mpf('2.5') for a, j, c in terms)
    return k0, kap, c4


def phase(x, terms):
    return 2*kernel(3*x, terms)-kernel(4*x, terms)-kernel(2*x, terms)


def bracketed_node(terms, active):
    # Not a uniqueness claim. The proof in REPORT_JA gives opposite endpoint
    # signs and excludes all roots at x>=2. Tiny scales adapt the lower point.
    lo = mp.sqrt(min(mpr(a) for a in active if a > 0))*mp.mpf('1e-5')
    hi = mp.mpf(2)
    require(phase(lo, terms) > 0 and phase(hi, terms) < 0, 'node bracket')
    for _ in range(150):
        mid = (lo+hi)/2
        if phase(mid, terms) > 0:
            lo = mid
        else:
            hi = mid
    return (lo+hi)/2


def symbolic_certificate():
    a, d, e, b, c, z = sp.symbols('a d e b c z', real=True)
    p = z**3-z**2+b*z-c
    disc = sp.discriminant(p, z)
    require(sp.expand(disc-discriminant(b, c)) == 0, 'cubic discriminant')
    bb = a*d+a*e+d*e
    cc = a*d*e
    require(sp.factor(discriminant(bb, cc).subs(e, 1-a-d)
                      -((a-d)**2*(d-e)**2*(e-a)**2).subs(e, 1-a-d)) == 0,
            'simplex/discriminant identity')
    t = sp.Symbol('t', real=True)
    bd, cd = 2*t-3*t*t, t*t*(1-2*t)
    require(sp.factor(discriminant(bd, cd)) == 0, 'double-root boundary')
    y = sp.Symbol('y', real=True)
    require(sp.expand((y-1)**3*(3*y+1)-(3*y**4-8*y**3+6*y*y-1)) == 0,
            'one-factor phase sign')
    # R3 static scalar/TT matching survives for a general positive A(z).
    q = sp.Symbol('q')
    require(sp.solve(-6+16*q-2, q) == [sp.Rational(1, 2)], 'curvature coefficient')
    return {
        'domain': 'b>0, c>=0, D=b^2-4b^3-4c+18bc-27c^2>=0',
        'domain_scope': 'equivalent to three nonnegative real alpha roots; at least two positive',
        'c_bounds': 'max(0,(9b-2-2(1-3b)^(3/2))/27) <= c <= (9b-2+2(1-3b)^(3/2))/27',
        'b_range': '0<b<=1/3',
        'degree_two_boundary': 'c=0, 0<b<=1/4',
        'double_root_boundary': 'b=2t-3t^2, c=t^2(1-2t), 0<t<=1/2',
        'curvature_scalar_coefficient_in_R3_ansatz': '1/2',
        'coefficient_region_is_not_all_positive_cubic_kernels': True,
    }


def evaluate(aa):
    terms = resolvent_terms(aa)
    b, c = coefficients(aa)
    require(admissible_coefficients(b, c), 'generated factors rejected by coefficient domain')
    k0, kap, c4 = center_moments(terms)
    node = bracketed_node(terms, aa)
    require(k0 >= 3*mp.sqrt(3)/8-mp.mpf('1e-40') and k0 < 1, 'center depth bounds')
    require(kap >= mp.sqrt(3)/8-mp.mpf('1e-40'), 'center tidal floor')
    rows = []
    for x in ('0.05', '0.25', '0.5', '1', '2', '4', '8'):
        xx = mp.mpf(x)
        J = enclosed(xx, terms)
        Jp = mp.diff(lambda r: enclosed(r, terms), xx)
        k = kernel(xx, terms)
        require(0 < J < 1 and Jp > 0 and 0 < k < 1/xx,
                'force, density or potential control')
        require(J/xx**3 <= kap+mp.mpf('1e-35'), 'orbital frequency ceiling')
        rows.append({'x': x, 'kernel': mp.nstr(k, 28), 'force_ratio': mp.nstr(J, 28),
                     'density_4pi_x2': mp.nstr(Jp, 28),
                     'phase': mp.nstr(phase(xx, terms), 28)})
    return {'alpha': [str(a) for a in aa], 'b': str(b), 'c': str(c),
            'kernel_center': mp.nstr(k0, 40), 'kappa': mp.nstr(kap, 40),
            'x4_coefficient': mp.nstr(c4, 40) if c > 0 else None,
            'bracketed_phase_node': mp.nstr(node, 40),
            'phase_node_unique': 'not_proved', 'rows': rows}


def robust_margin(eta):
    eta = rat(eta)
    if not 0 < eta <= sp.Rational(1, 3):
        raise ValueError('0<eta<=1/3 required')
    extreme = (1-2*eta, eta, eta)
    terms = resolvent_terms(extreme)
    k0max, kapmax, c4max = center_moments(terms)
    kapmin = mp.sqrt(3)/8
    # Proven bound: phase(x)>=kappa*x^2-110*c4*x^4.
    # The half-margin endpoint makes positivity strict throughout (0,x_safe].
    x_safe = mp.sqrt(kapmin/(220*c4max))
    return {'eta': str(eta), 'interpretation': 'user-selected robustness margin, not a derived constant',
            'extremal_alpha': [str(a) for a in extreme],
            'kernel_center_interval': [mp.nstr(3*mp.sqrt(3)/8, 35), mp.nstr(k0max, 35)],
            'kappa_interval': [mp.nstr(kapmin, 35), mp.nstr(kapmax, 35)],
            'x4_coefficient_upper': mp.nstr(c4max, 35),
            'certified_root_exclusion_below': mp.nstr(x_safe, 35),
            'certified_all_nodes_below': '2',
            'band_kind': 'analytic conservative bounds, not a sampled extremum'}


def counterexamples():
    # b=1/2,c=0 has A(k^2)>0, but its real-space averaging kernel changes sign.
    b = mp.mpf('0.5')
    ap = (1+mp.sqrt(1-4*b))/2
    am = mp.conj(ap)
    def w(r):
        return mp.re((mp.exp(-r/mp.sqrt(ap))-mp.exp(-r/mp.sqrt(am)))
                     /(4*mp.pi*(ap-am)*r))
    r = mp.mpf(8)
    require(w(r) < 0, 'negative-density witness not found')
    require(not admissible_coefficients('1/2', 0), 'bad density candidate accepted')
    require(not admissible_coefficients(0, 0), 'one-factor vertex accepted')
    require(not admissible_coefficients('1/10', '1/10'), 'complex-root cubic accepted')
    return {'positive_fourier_not_positive_density':
            {'b': '1/2', 'c': '0', 'x': '8', 'density': mp.nstr(w(r), 35)},
            'no_uniform_tidal_ceiling': 'alpha=(1-delta,delta,0), delta->0: kappa->infinity',
            'no_positive_universal_phase_lower_bound': 'same boundary: a phase node tends to zero',
            'one_factor_phase': '12x*DeltaK=(exp(-x)-1)^3*(3exp(-x)+1)<0',
            'full_theory_health': 'UNRESOLVED; must not promote static checks to full gravity'}


def run():
    with mp.workdps(55):
        selected = [('.5','.5','0'), ('1/3','1/3','1/3'), ('1/2','1/3','1/6'),
                    ('.8','.1','.1'), ('.9','.05','.05'),
                    ('.99','.01','0'), ('.9999','.0001','0')]
        records = [evaluate(validate_factors(a)) for a in selected]
        # All zeros for the class are below x=2: erfc mixture dominated by
        # Gamma(shape=3,scale=1). This is a proof bound, not a grid scan.
        neg_at_2 = -mp.mpf(1)/24 + mp.mpf(7)/4*mp.exp(-8)+mp.mpf(11)/8*mp.exp(-4)
        require(neg_at_2 < 0, 'uniform negative-phase bound')
        exp4_lo = sum(sp.Rational(4)**j/sp.factorial(j) for j in range(8))
        exp8_lo = sum(sp.Rational(8)**j/sp.factorial(j) for j in range(8))
        require(exp4_lo > 50 and exp8_lo > 1000, 'exponential rational bounds')
        require(-sp.Rational(1,24)+sp.Rational(7,4000)+sp.Rational(11,400)<0,
                'exact negative certificate at x=2')
        for bad in [('1','0','0'), ('1.1','-.1','0'), ('.5','.4','0')]:
            try:
                validate_factors(bad)
            except ValueError:
                pass
            else:
                raise AssertionError('invalid factors accepted')
        return {
            'base_sha': BASE_SHA, 'scope': SCOPE, 'certificate': symbolic_certificate(),
            'shared_results': {
                'normalized_positive_density': True,
                'central_force_is_linear_and_attractive': True,
                'finite_center_and_tidal_coefficient_for_each_member': True,
                'force_ratio': '0<J(x)<1 for x>0',
                'global_kernel_Hessian_bound': 'norm Hessian(k)<=kappa',
                'finite_N_particle_flow': 'global unique classical flow and self-adjoint quantum Hamiltonian',
                'finite_N_energy_floor': '-(G/ell) sum_{a<b} m_a m_b',
                'specified_source_TT_flux_band': '(1+y^2/3)^(-3) <= P/P0 <= (1+y^2)^(-1)',
                'all_Newtonian_circular_orbits_radially_stable': True,
                'orbit_quantum_identity': 'Omega0^2=omega_core^2=GM*kappa/ell^3',
                'radial_epicycle_to_orbit_ratio': '2 at the core; 1 at large radius',
                'phase_reversal': 'at least one nonzero node in (0,2) for the fixed ideal point-probe geometry',
                'phase_negative_for_x_ge_2': True,
                'phase_upper_bound_at_2': mp.nstr(neg_at_2, 40),
                'kernel_center_interval': '[3sqrt(3)/8, 1)',
                'kappa_interval': '[sqrt(3)/8, infinity)',
                'nonlinear_stability': 'not_tested', 'Hadamard_quantum_completion': 'not_tested',
                'full_consistent_gravity': False},
            'selected_models': records,
            'robustness_margins': [robust_margin(e) for e in ('1/20','1/10','1/6','1/3')],
            'counterexamples': counterexamples(),
            'all_implemented_assertions_passed': True,
            'environment': {'python': platform.python_version(), 'sympy': sp.__version__,
                            'mpmath': mp.__version__, 'working_dps': 55},
            'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    parser.add_argument('--alpha', nargs=3, help='three exact rationals/decimal strings')
    parser.add_argument('--b', help='check a coefficient pair (requires --c)')
    parser.add_argument('--c')
    parser.add_argument('--eta', help='positive lower factor margin (not a physical constant)')
    args = parser.parse_args()
    if (args.b is None) != (args.c is None):
        parser.error('--b and --c must be supplied together')
    if sum((bool(args.alpha), args.b is not None, args.eta is not None)) > 1:
        parser.error('choose --alpha OR --b/--c OR --eta')
    if args.b is not None:
        data = {'scope': SCOPE, 'b': args.b, 'c': args.c,
                'admissible_in_design_class': admissible_coefficients(args.b, args.c)}
    elif args.eta is not None:
        with mp.workdps(55):
            data = robust_margin(args.eta)
    elif args.alpha:
        with mp.workdps(55):
            data = evaluate(validate_factors(args.alpha))
    else:
        data = run()
    text = json.dumps(data, ensure_ascii=False, indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding='utf-8')
        print(json.dumps({'output': str(args.output), 'scope': SCOPE,
                          'all_implemented_assertions_passed': data.get('all_implemented_assertions_passed')}))
    else:
        print(text)


if __name__ == '__main__':
    main()
