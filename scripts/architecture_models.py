"""Bounded 3+1D architecture experiments; no imported 2D no-go or assumed past channel.

Primary sources and domains are in architecture/batch-v1.json and the methods note.
Symbolic construction is separate from architecture_verify.py's numerical verifier.
All returned decimals are strings; no JSON NaN/Infinity or invented zero probability.
"""
from __future__ import annotations

from fractions import Fraction
from typing import Any
import mpmath as mp
import sympy as sp


def decimal(x: Any) -> str:
    return mp.nstr(x, 45)


def rational(x: Fraction) -> str:
    return str(x)


def thin_shell_curvature(mu: Fraction, eta: Fraction) -> Fraction:
    """a0^2 V'' for two Schwarzschild exteriors; mu=GM/(c^2 a0)."""
    if not 0 <= mu < Fraction(1, 2):
        raise ValueError("The shell must be outside r=2M; negative M is not this family")
    return -2 * (2*mu + mu*mu/(1-2*mu) + (1+2*eta)*(1-3*mu))


def shell_symbolic_checks() -> dict[str, str]:
    a, mass, sig, pres, eta = sp.symbols('a M sigma p eta', real=True)
    sigma_prime = -2*(sig+pres)/a
    # Differentiate the full Israel potential using surface conservation.
    V = 1-2*mass/a-(2*sp.pi*a*sig)**2
    def derivative(expr: sp.Expr) -> sp.Expr:
        return sp.diff(expr, a) + sp.diff(expr, sig)*sigma_prime + sp.diff(expr, pres)*eta*sigma_prime
    Vp, Vpp = derivative(V), derivative(derivative(V))
    sigma0 = -sp.sqrt(1-2*mass/a)/(2*sp.pi*a)
    p0 = (1-mass/a)/(4*sp.pi*a*sp.sqrt(1-2*mass/a))
    at_static = {sig: sigma0, pres: p0}
    assert sp.simplify(V.subs(at_static)) == 0
    assert sp.simplify(Vp.subs(at_static)) == 0
    mu = sp.symbols('mu', real=True)
    target = -2*(2*mu+mu**2/(1-2*mu)+(1+2*eta)*(1-3*mu))
    assert sp.simplify((a*a*Vpp.subs(at_static)).subs(mass, mu*a)-target) == 0
    numerator = sp.cancel(-target*(1-2*mu)/2)
    assert sp.simplify(numerator.subs(eta, 0)-(3*(mu-sp.Rational(1,2))**2+sp.Rational(1,4))) == 0
    assert sp.simplify(numerator.subs(eta, 1)-(15*(mu-sp.Rational(13,30))**2+sp.Rational(11,60))) == 0
    assert sp.expand(numerator.subs(eta, 4)) == 51*mu**2-43*mu+9
    assert target.subs({mu:sp.Rational(2,5),eta:4}) == sp.Rational(2,5)
    return {'source': 'Poisson-Visser (1995), Eqs. (11)-(27)',
            'Vpp_dimensionless': str(target),
            'certificate': 'For mu<=1/3 min_eta N=N(0)=3(mu-1/2)^2+1/4; for mu>=1/3 min_eta N=N(1)=15(mu-13/30)^2+11/60; Vpp=-2N/(1-2mu)<0.',
            'stable_relaxation': 'eta=4; (43-sqrt(13))/102 < mu < (43+sqrt(13))/102; mu=2/5 gives a0^2 Vpp=2/5'}


def shell_scan(stiff: bool = False) -> dict[str, Any]:
    checks = shell_symbolic_checks()
    etas = [Fraction(4)] if stiff else [Fraction(i, 20) for i in range(21)]
    rows = []
    for i in range(100):
        mu = Fraction(i, 200)
        for eta in etas:
            value = thin_shell_curvature(mu, eta)
            rows.append({'mu':rational(mu), 'eta':rational(eta), 'a0_squared_Vpp':rational(value),
                         'radially_stable':value > 0})
    count = sum(row['radially_stable'] for row in rows)
    assert count > 0 if stiff else count == 0
    return {'checks':checks, 'trials':rows, 'tested':len(rows), 'stable':count,
            'verdict':'conditional_radial_stability' if stiff else 'radial_instability_on_stated_domain',
            'probability_law_computed':False}


def rotating_scan() -> dict[str, Any]:
    N,Q,R,sn,omega = sp.symbols('N Q R sin_theta omega', positive=True)
    g = sp.diag(-N*N, Q*Q, R*R, R*R*sn*sn)
    g[0,0] += R*R*sn*sn*omega*omega
    g[0,3] = g[3,0] = -R*R*sn*sn*omega
    inverse = sp.simplify(g.inv())
    assert sp.simplify(inverse[0,0]+1/(N*N)) == 0
    normal = sp.Matrix([1/N,0,0,omega/N])
    assert sp.simplify((normal.T*g*normal)[0]+1) == 0
    assert sp.simplify(g.det()+N*N*Q*Q*R**4*sn**2) == 0
    rows = []
    # This specializes Teo's form, not his exact illustrative functions.
    for spin in [Fraction(0),Fraction(1,4),Fraction(1),Fraction(10)]:
        for x in [Fraction(0),Fraction(1),Fraction(5)]:
            radius_squared = 1+x*x
            cov_gtt = -1+4*spin*spin/(radius_squared*radius_squared)
            rows.append({'J_over_b_squared':str(spin),'x_over_b':str(x),
                         'g_tt_equator':str(cov_gtt),'g_inverse_tt':'-1',
                         'ergoregion_at_point':cov_gtt>0})
    assert any(r['ergoregion_at_point'] for r in rows)
    return {'checks':{'metric_dimensions':4,'g_inverse_tt':'-1/N^2','normal_norm':'-1',
                      'global_input':'t is a single-valued real coordinate; no time-shift gluing'},
            'tested':len(rows),'trials':rows,'verdict':'global_time_obstruction',
            'probability_law_computed':False}


def casimir_scan() -> dict[str, Any]:
    area, gap, fraction, C = sp.symbols('area gap fraction C', positive=True)
    energy = -C*area/gap**3
    force = sp.diff(energy, gap)
    pressure = force/(area*fraction)
    strut_energy = pressure*area*fraction*gap
    assert sp.simplify(strut_energy+3*energy) == 0
    assert sp.simplify(energy+strut_energy+2*energy) == 0
    rows=[]
    for A in [Fraction(1,10**6),Fraction(1,10**4)]:
        for d in [Fraction(1,10**7),Fraction(1,10**6)]:
            for f in [Fraction(1,100),Fraction(1,10),Fraction(1,2)]:
                rows.append({'area_m2':str(A),'gap_m':str(d),'support_area_fraction':str(f),
                             'minimum_support_over_abs_casimir':'3',
                             'minimum_total_over_abs_casimir':'2'})
    return {'tested':len(rows),'trials':rows,'verdict':'independent_cells_cannot_supply_negative_total_line_energy',
            'checks':{'support_energy':'3|E_Cas| or greater','total_energy':'2|E_Cas| or greater',
                      'domain':'flat parallel-plate approximation, finite independent cells, static force balance, DEC struts'},
            'probability_law_computed':False}


def fkz_scan(dps: int) -> dict[str, Any]:
    with mp.workdps(dps):
        G,c = mp.mpf('6.67430e-11'),mp.mpf('299792458')
        rows=[]
        for a in [1,10]:
            for ra in [10,30]:
                for lr in [100,1000]:
                    for mass in ['1e3','1e12','1e20']:
                        R,L = a*ra,a*ra*lr
                        M=mp.mpf(mass)
                        I = G*M/(a*c*c)*(mp.atan(mp.mpf(a)/R)-mp.mpf(a)/L)
                        B=mp.mpf(L)/c
                        onset=B/mp.expm1(I)
                        t2=mp.mpf('1.1')*onset
                        delay=B-mp.expm1(I)*t2
                        weak=G*M/(R*c*c)
                        assert 0 < weak < mp.mpf('1e-6') and delay < 0
                        rows.append({'a_m':a,'R_m':R,'L_m':L,'M_kg':mass,
                                     'I_C':decimal(I),'onset_s':decimal(onset),'weak_field_parameter':decimal(weak),
                                     'return_delay_at_1p1_onset_s':decimal(delay),
                                     'negative_line_energy_J_per_m':decimal(-c**4/(4*G))})
        return {'tested':len(rows),'trials':rows,'verdict':'conditional_classical_past_path',
                'checks':{'B_opt':'approximated by L/c','warning':'No error bound for long-time weak-field continuation or quantum horizon; no supported device.'},
                'probability_law_computed':False}


def collar_scan(dps: int) -> dict[str, Any]:
    x,b,e = sp.symbols('x b eps', real=True, positive=True)
    radius = b+sp.sqrt(x*x+e*e)-e
    rp,rpp = sp.diff(radius,x),sp.diff(radius,x,2)
    # Orthonormal Einstein tensor for 4D ultrastatic dx^2+r(x)^2 dOmega^2.
    density = (1-rp**2-2*radius*rpp)/radius**2 # 8 pi G times rho
    radial = (rp**2-1)/radius**2
    transverse = rpp/radius
    assert sp.simplify(density.subs(x,0)-(1-2*b/e)/b**2) == 0
    assert sp.simplify(radial.subs(x,0)+1/b**2) == 0
    assert sp.simplify(transverse.subs(x,0)-1/(b*e)) == 0
    assert sp.simplify(sp.diff(radial,x)+2*rp/radius*(radial-transverse)) == 0
    with mp.workdps(dps):
        G,c,hbar = mp.mpf('6.67430e-11'),mp.mpf('299792458'),mp.mpf('1.054571817e-34')
        lp2=hbar*G/c**3
        rows=[]
        for b0 in ['1e-6','1e-3','1']:
            bb=mp.mpf(b0)
            for N in [1,100]:
                f=mp.mpf('.01')
                maximum=(N*mp.pi**3*lp2*bb/(12*f**4))**(mp.mpf(1)/3)
                for ratio in [mp.mpf('.25'),mp.mpf('.5'),mp.mpf('1'),mp.mpf('2')]:
                    ee=ratio*maximum
                    rho=c**4*(1-2*bb/ee)/(8*mp.pi*G*bb**2)
                    qei=-N*hbar*c*mp.pi**2/(48*(f*ee)**4)
                    compatible=rho>=qei
                    rows.append({'b_m':b0,'N':N,'f':'0.01','epsilon_factor':decimal(ratio),
                                 'epsilon_m':decimal(ee),'required_rho_J_per_m3':decimal(rho),
                                 'flat_QEI_J_per_m3':decimal(qei),'passes_necessary_flat_diagnostic':compatible})
        assert any(r['passes_necessary_flat_diagnostic'] for r in rows)
        assert any(not r['passes_necessary_flat_diagnostic'] for r in rows)
        return {'tested':len(rows),'trials':rows,
                'compatible':sum(r['passes_necessary_flat_diagnostic'] for r in rows),
                'checks':{'four_dimensional_tensor':'8piG(rho,pr,pt) at x=0 = ((1-2b/eps)/b^2,-1/b^2,1/(b eps))',
                          'interpretation':'Only a necessary local-flat, short-time diagnostic; not a curved-space existence theorem'},
                'verdict':'thin_layer_not_excluded_by_this_necessary_diagnostic','probability_law_computed':False}


def flat_signal(dps: int) -> dict[str, Any]:
    """Finite-radius spherical source, 4D retarded Green function; c=hbar=1.

J_b=(-1)^b lambda f(t) delta(r-a)/(4pi a^2), f=sin^4(pi t/T)
inside [0,T]. Receiver is outside the shell. A modeled Gaussian meter with
unit variance is an explicit readout assumption, not a full detector derivation.
"""
    with mp.workdps(dps):
        a,R,T,lam = mp.mpf(1),mp.mpf(5),mp.mpf(2),mp.mpf(1)
        def f(t: mp.mpf) -> mp.mpf:
            return mp.sin(mp.pi*t/T)**4 if 0<t<T else mp.mpf(0)
        def primitive(t: mp.mpf) -> mp.mpf:
            z=max(mp.mpf(0),min(t,T))
            return 3*z/8-T*mp.sin(2*mp.pi*z/T)/(4*mp.pi)+T*mp.sin(4*mp.pi*z/T)/(32*mp.pi)
        def mean(t: mp.mpf) -> mp.mpf:
            return lam*(primitive(t-R+a)-primitive(t-R-a))/(8*mp.pi*R*a)
        times=[mp.mpf(t) for t in [-2,-1,0,3,4,5,6,7,8,9]]
        rows=[{'t':decimal(t),'mean_do0':decimal(mean(t)),'mean_do1':decimal(-mean(t))} for t in times]
        assert all(mean(t)==0 for t in times if t<=R-a)
        expected=3*lam*T/(64*mp.pi*R*a)
        assert mp.almosteq(mean(R+T/2),expected)
        # Positive finite radiated energy, not zero-cost state preparation.
        integrand=lambda u: ((f(u+a)-f(u-a))/(2*a))**2
        radiation=lam**2/(4*mp.pi)*mp.quad(integrand,[-a,T-a,T+a])
        expected_energy=35*lam**2*T/(1024*mp.pi*a*a) # specific T=2a
        assert abs(radiation-expected_energy)<mp.mpf('1e-42')
        return {'tested':len(rows),'trials':rows,'verdict':'retarded_local_source_no_past_dependence',
                'probability_law_computed':True,
                'past_receiver_time':'-1','sender_onset':'0','front_time':decimal(R-a),
                'past_mean_do0':'0','past_mean_do1':'0','meter_variance':'1','past_total_variation':'0',
                'future_mean':decimal(expected),'future_total_variation':decimal(mp.erf(expected/mp.sqrt(2))),
                'radiated_energy_natural_units':decimal(radiation),
                'checks':{'dimension':4,'retarded_kernel':'delta(t-|x|)/(4pi|x|)',
                          'warning':'Future contrast is not a past channel; source/apparatus mean-field backreaction not solved.'}}


def all_experiments(dps: int) -> dict[str, dict[str, Any]]:
    return {'flat-local-source':flat_signal(dps), 'rotating-global-time':rotating_scan(),
            'schwarzschild-eos-0-to-1':shell_scan(), 'schwarzschild-eos-4':shell_scan(True),
            'fkz-mass-controlled-ring':fkz_scan(dps), 'finite-casimir-cell-line':casimir_scan(),
            'thin-collar-qei-window':collar_scan(dps)}
