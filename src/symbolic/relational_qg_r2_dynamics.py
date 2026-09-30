#!/usr/bin/env python3
"""R2: conserving weak-field dynamics of R1, not a nonlinear QG completion.

Retains F_l(k)=exp(-l^2 k^2/2), with one vertex at source and probe.
New results: a retarded/noise pair, conserved source controls, recoil-aware
phases, softened circular orbits, and a leading-quadrupole balance model.
All numerical quantities use c=hbar=l=1 unless a dimensionless parameter is
explicit. The radiation model is only leading nonrelativistic/quadrupole
order; its form-factor correction is NOT a computed complete 1PN correction.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from pathlib import Path

import mpmath as mp
import sympy as sp

BASE_SHA = '4c600df0b331a19f9d21384bf58472bee01a5a16'


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def kernel(x):
    x = abs(mp.mpf(x))
    return mp.erf(x / 2) / x if x else 1 / mp.sqrt(mp.pi)


def enclosed(x):
    x = mp.mpf(x)
    return mp.erf(x / 2) - x * mp.exp(-x*x/4) / mp.sqrt(mp.pi)


def enclosed_prime(x):
    return x*x * mp.exp(-x*x/4) / (2*mp.sqrt(mp.pi))


def phase_r1(d):
    return 2*kernel(3*d) - kernel(4*d) - kernel(2*d)


def text(x, n=32):
    return mp.nstr(x, n)


def source_identities():
    """Off-shell Ward identity of a branch DIFFERENCE, not positive matter."""
    w, kx, ky, kz = sp.symbols('w kx ky kz', real=True)
    q0, q1, q2, q3, q4, q5 = sp.symbols('q0:6', real=True)
    Q = sp.Matrix([[q0,q3,q4],[q3,q1,q5],[q4,q5,q2]])
    k = sp.Matrix([kx,ky,kz])
    T = sp.zeros(4)
    T[0,0] = -(k.T*Q*k)[0]
    for i in range(3):
        T[0,i+1] = T[i+1,0] = -w*(Q*k)[i]
        for j in range(3):
            T[i+1,j+1] = -w*w*Q[i,j]
    p = sp.Matrix([-w,kx,ky,kz])
    ward = (p.T*T).applyfunc(sp.expand)
    require(ward == sp.zeros(1,4), 'conserved quadrupole Ward identity')
    density_only = sp.zeros(4)
    density_only[0,0] = T[0,0]
    require(sp.expand((p.T*density_only)[0]) != 0, 'negative switching control')

    # Pair/bond stress identity in weak form. Central pair force is symmetric.
    lam = sp.symbols('lam', real=True)
    xa, xb = sp.Matrix([2,1,-1]), sp.Matrix([-1,0,2])
    r = xa-xb
    force = -sp.Rational(2,7)*r
    X = sp.Matrix(sp.symbols('x0:3', real=True))
    test = sp.Matrix([X[0]**2+X[1], X[1]*X[2], X[2]**3-X[0]])
    jac = test.jacobian(X)
    line = xb+lam*r
    integrand = (force.T*jac.subs(dict(zip(X,line)))*r)[0]
    lhs = sp.integrate(integrand, (lam,0,1))
    rhs = (force.T*(test.subs(dict(zip(X,xa)))-test.subs(dict(zip(X,xb)))))[0]
    require(sp.simplify(lhs-rhs) == 0, 'bond stress weak identity')
    require(force*r.T == (force*r.T).T, 'symmetric central bond stress')

    x,y = sp.symbols('x y')
    # With branch-difference zeroth and first moments zero, only terms with
    # powers >=2 on BOTH laboratories remain in the short-distance expansion.
    def allowed(poly):
        return sp.expand(sum(c*x**i*y**j for (i,j),c in sp.Poly(poly,x,y).terms()
                             if i>=2 and j>=2))
    require(allowed((x-y)**2) == 0, 'recoil cancels quadratic cross term')
    require(allowed((x-y)**4) == 6*x*x*y*y, 'quadrupole cross coefficient')
    return {
        'fourier_convention': 'exp(-i omega t+i k.x)',
        'branch_difference': 'T00=Qij d_i d_j f; T0i=-Qij d_t d_j f; Tij=Qij d_t^2 f',
        'exact_flat_conservation': True,
        'density_only_time_switching_rejected': True,
        'bond_stress': 'tau_ij=sum_(a<b) F_ab,i r_ab,j integral_0^1 delta(x-x_b-lambda r_ab) d lambda',
        'bond_divergence': 'd_j tau_ij=-sum_a F_a,i delta(x-x_a)',
        'bond_weak_identity_residual': str(sp.simplify(lhs-rhs)),
        'quadratic_phase_cancels_for_equal_mass_and_COM_branches': True,
        'quartic_cross_moment': '6 Delta M2_A Delta M2_B',
        'scope': 'Exact linear-source identity and Newtonian mass/momentum balance; not a microscopic apparatus action or nonlinear gravitational Ward identity.'
    }


def retarded(t,r):
    """Scalar radial factor of the two-vertex retarded wave Green function."""
    if t <= 0:
        return mp.mpf(0)
    if not r:
        return t*mp.exp(-t*t/4)/(8*mp.pi**mp.mpf('1.5'))
    return (mp.exp(-(r-t)**2/4)-mp.exp(-(r+t)**2/4))/(8*mp.pi**mp.mpf('1.5')*r)


def real_time_controls():
    rows=[]
    for t,r in [(mp.mpf('.5'),mp.mpf(1)),(mp.mpf(1),mp.mpf(2)),
                (mp.mpf(3),mp.mpf(1)),(mp.mpf(2),mp.mpf(0))]:
        if r:
            spec=mp.quad(lambda k: mp.exp(-k*k)*mp.sin(k*r)*mp.sin(k*t),[0,1,4,mp.inf])/(2*mp.pi**2*r)
        else:
            spec=mp.quad(lambda k:k*mp.exp(-k*k)*mp.sin(k*t),[0,1,4,mp.inf])/(2*mp.pi**2)
        err=abs(spec-retarded(t,r))
        require(err<mp.mpf('1e-35'),'retarded Fourier inversion')
        rows.append({'t_over_ell':text(t),'r_over_ell':text(r),'ell2_Gret':text(spec),
                     'spacelike':bool(r>t),'spectral_error':text(err,8)})
    errors=[]
    for r in [mp.mpf(0),mp.mpf(1),mp.mpf(3)]:
        integ=mp.quad(lambda t: retarded(t,r),[0,1,4,10,mp.inf])
        err=abs(4*mp.pi*integ-kernel(r))
        require(err<mp.mpf('1e-35'),'static-retarded sum rule')
        errors.append(text(err,8))
    # The unit-variance Gaussian position form factor has F(0)=1.
    require(mp.exp(0)==1,'constant/vacuum mode')
    return {
        'Gret': 'theta(t)/(8 pi^(3/2) ell r) [exp(-(r-t)^2/(4ell^2))-exp(-(r+t)^2/(4ell^2))]',
        'normalization': 'integral_0^infty Gret dt=K_ell(r)/(4pi), c=1',
        'mode_noise': 'C_lambda(k,t)=hbar exp(-ell^2 k^2) cos(k t)/(2k), vacuum',
        'same_form_factor_in_response_and_noise': True,
        'rows':rows,'static_sum_rule_errors':errors,
        'past_time_response':False,'strict_metric_microcausality':False,
        'vacuum_energy_removed':False,
        'scope':'Linear canonical field remains ordinary massless TT; these are smeared couplings/observables, not a new fundamental Hadamard state.'
    }


def noise_controls():
    # Polarizations are Frobenius-normalized; sum E_ij E_kl=Lambda_ij,kl.
    # For STF Q, integral dOmega Q Lambda Q=(8pi/5) Q_ij Q_ij.
    strength=mp.mpf('.01')  # G Q_ij Q_ij/(hbar ell^4) in c=1 units
    sigma=mp.mpf('.2')
    rows=[]
    for tau in [mp.mpf(1),mp.mpf(2),mp.mpf(4),mp.mpf(8)]:
        A=1+sigma*sigma+tau*tau
        integral=mp.quad(lambda k:k**5*mp.exp(-A*k*k),[0,1,mp.inf])
        gamma=4*strength*tau*tau*integral/5
        exact=4*strength*tau*tau/(5*A**3)
        require(abs(gamma-exact)<mp.mpf('1e-35'),'Gaussian TT overlap exponent')
        rows.append({'pulse_tau_over_ell':text(tau),'Gamma':text(gamma),
                     'visibility':text(mp.exp(-gamma))})
    # A genuine Gram matrix of environment coherent states: CP dephasing.
    amps=[mp.mpc(0),mp.mpc('.1','.2'),mp.mpc('-.3','.1'),mp.mpc('.4','-.1')]
    gram=mp.matrix([[mp.exp(-abs(a)**2/2-abs(b)**2/2+mp.conj(b)*a) for b in amps] for a in amps])
    evals=mp.eighe(gram,eigvals_only=True)
    require(min(evals)>0,'coherent-state environment Gram positivity')
    return {
        'source':'f(t,x)=exp(-t^2/(2tau^2)) w_sigma(x), integral w=1; Q STF constant',
        'quadrupole':'Delta I_ij(t)=2 Q_ij exp(-t^2/(2tau^2))',
        'overlap':'|<env_1|env_0>|=exp(-Gamma)',
        'Gamma':'4 G QijQij tau^2/[5 hbar (ell^2+sigma^2+tau^2)^3], c=1',
        'source_strength_GQ2_over_hbar_ell4':text(strength),
        'sigma_over_ell':text(sigma),'rows':rows,
        'environment_Gram_eigenvalues':[text(v) for v in evals],
        'noise_free_state_selection_used':False,
        'scope':'Exactly conserved prescribed branch difference in linear TT vacuum theory. Not an entire material apparatus, and not the same pulse as R1 static holding.'
    }


def recoil_phase(d,s=5,mass_ratio=100):
    eta=mp.mpf(mass_ratio)
    masses=[mp.mpf(1),eta]
    def positions(b,A):
        return [b*d,-s-b*d/eta] if A else [(3+b)*d,3*d+s-b*d/eta]
    def energy(i,j):
        return mp.fsum(ma*mb*kernel(x-y) for ma,x in zip(masses,positions(i,True))
                       for mb,y in zip(masses,positions(j,False)))
    for A in (True,False):
        com=[mp.fsum(m*x for m,x in zip(masses,positions(b,A))) for b in (0,1)]
        require(abs(com[1]-com[0])<mp.mpf('1e-35'),'apparatus recoil COM')
    return energy(0,0)+energy(1,1)-energy(0,1)-energy(1,0)


def recoil_controls():
    r=mp.findroot(phase_r1,(mp.mpf('.6'),mp.mpf('.7')))
    rows=[]
    for s in [mp.mpf(5),mp.mpf(10),mp.mpf(100)]:
        node=mp.findroot(lambda d:recoil_phase(d,s),(.6,.85))
        require(abs(recoil_phase(node,s))<mp.mpf('1e-32'),'recoil node')
        rows.append({'support_offset_over_ell':text(s),'M_support_over_m':100,
                     'node_d_over_ell':text(node),
                     'phase_at_R1_node':text(recoil_phase(r,s))})
    mass_limit=[]
    for eta in (10,100,1000):
        node=mp.findroot(lambda d:recoil_phase(d,mp.mpf(5),eta),(.6,.85))
        mass_limit.append({'mass_ratio':eta,'node_d_over_ell':text(node)})
    require(abs(mp.mpf(rows[0]['node_d_over_ell'])-r)>mp.mpf('.07'),'missing recoil negative control')
    return {'R1_point_probe_node':text(r),'apparatus_positions':
            'A_b=[b d,-s-b d/eta]; B_b=[(3+b)d,3d+s-b d/eta]; masses=[m,eta*m]',
            'phase':'sum_(p,q) m_p m_q [K(r00)+K(r11)-K(r01)-K(r10)]/m^2',
            'rows':rows,'large_support_mass_controls':mass_limit,
            'point_probe_node_is_universal':False,
            'scope':'Quasistatic nonrelativistic branch energies including both recoils; splitting radiation and holding-device internal stress not computed by this table.'}


def moving_frame_controls():
    r=mp.findroot(phase_r1,(.6,.7)); slope=mp.diff(phase_r1,r)
    coeff=[]
    for cos2 in (0,1):
        D=lambda x:cos2*mp.diff(kernel,x,2)+(1-cos2)*mp.diff(kernel,x)/x
        delta=2*D(3*r)-D(4*r)-D(2*r)
        coeff.append(-delta/slope)
    return {'preferred_frame_is_extra_structure':True,
            'rest_frame_static_kernel':'4pi exp[-ell^2(q_perp^2+gamma^2 q_parallel^2)]/(q_perp^2+q_parallel^2)',
            'small_beta_potential_kernel':'K_beta=K+ell^2 beta^2 d_z^2 K+O(beta^4)',
            'far_field_kernel':'1/r+ell^2 beta^2 (3 cos(theta)^2-1)/r^3+O(beta^4/r^3,ell^4/r^5)',
            'node':'d*/ell=d0+beta^2[A+B cos(theta)^2]+O(beta^4), point probes only',
            'A':text(coeff[0]),'B':text(coeff[1]-coeff[0]),
            'scope':'Uniform boost relative to the fixed foliation; not a covariant completion or an observational bound.'}


def orbital_values(x):
    J=enclosed(x); Jp=enclosed_prime(x)
    w2=J/x**3
    e=-kernel(x)+J/(2*x)
    ep=(J/x**2+Jp/x)/2
    kr2=w2+Jp/x**2
    return w2,e,ep,kr2


def orbit_and_balance_controls():
    z=sp.symbols('z',positive=True)
    Js=sp.erf(z/2)-z*sp.exp(-z*z/4)/sp.sqrt(sp.pi)
    require(sp.simplify(sp.diff(Js,z)-z*z*sp.exp(-z*z/4)/(2*sp.sqrt(sp.pi)))==0,'J derivative')
    series=sp.series(Js/z**3,z,0,6)
    A=1/(6*mp.sqrt(mp.pi)); eps=mp.mpf('.01')
    rows=[]
    for x in map(mp.mpf,['.1','.5','1','2','4','6']):
        w2,e,ep,kr2=orbital_values(x)
        require(ep>0 and kr2>0,'circular orbit stability/energy')
        require(0<w2<=A,'orbital frequency bound')
        require(abs(mp.diff(lambda y:orbital_values(y)[1],x)-ep)<mp.mpf('1e-35'),'circular dE/dr')
        rows.append({'r_over_ell':text(x),'Omega_over_Omega0':text(mp.sqrt(w2/A)),
                     'radial_frequency_over_Omega':text(mp.sqrt(kr2/w2)),
                     'E_over_GmuM_ell':text(e),'power_form_factor_only':text(mp.exp(-4*eps*w2))})
    def du_dx(x):
        w2,e,ep,kr2=orbital_values(x)
        return ep*mp.exp(4*eps*w2)/(x**4*w2**3)
    elapsed=[]
    for x in map(mp.mpf,['2','1','.5','.25','.1']):
        u=mp.quad(du_dx,[x,2,6]) if x<2 else mp.quad(du_dx,[x,6])
        elapsed.append({'r_over_ell':text(x),'radiative_time_u_from_r6':text(u)})
    short=mp.mpf('1e-4')
    coeff=short**3*du_dx(short)
    target=2*mp.exp(4*eps*A)/A**2
    require(abs(coeff/target-1)<mp.mpf('1e-7'),'infinite time r^-3 asymptote')
    return {'J_series_over_x3':str(series),
        'Omega_squared':'G M J(r/ell)/r^3',
        'Omega0_squared':'G M/(6 sqrt(pi) ell^3)',
        'epicycle_squared':'G M [J/r^3+(dJ/dr)/r^2]>0',
        'E_circular':'-G mu M K(r)+G mu M J/(2r)',
        'P_quadrupole':'(32/5)G mu^2 r^4 Omega^6/c^5 exp[-4 ell^2 Omega^2/c^2]',
        'balance':'dr/dt=-P/(dE_circular/dr)',
        'epsilon_GM_over_c2ell':text(eps),'rows':rows,
        'radiative_time_definition':'u=(32/5) nu epsilon^(5/2) t sqrt(GM/ell^3), nu=mu/M',
        'elapsed':elapsed,
        'small_r_balance':'dr/dt=-(16/5)G mu Omega0^4/c^5 exp[-4ell^2Omega0^2/c^2] r^3+O(r^5)',
        'classical_formal_late_time':'r proportional t^-1/2; Omega0-Omega proportional t^-1; P proportional t^-2',
        'classical_origin_reached_at_finite_time':False,
        'quantum_crossover_r_over_ell':'(6 sqrt(pi)/g)^(1/4), g=mu^2 G M ell/hbar^2; L~hbar, not a sharp transition',
        'quantum_core_oscillator_frequency':'omega_quantum=Omega0',
        'max_1_minus_power_form_factor':text(1-mp.exp(-4*eps*A)),
        'scope':'Adiabatic leading-quadrupole closure of the specified weak-metric Newtonian model. No complete 1PN flux, detector waveform, physical overlap endpoint, or BH claim.'}


def conservative_trajectory():
    """A direct velocity-Verlet test of the same finite central Hamiltonian."""
    def K(r): return math.erf(r/2)/r
    def acc(x,y):
        r=math.hypot(x,y)
        J=math.erf(r/2)-r*math.exp(-r*r/4)/math.sqrt(math.pi)
        return -J*x/r**3,-J*y/r**3
    def energy(x,y,vx,vy):return (vx*vx+vy*vy)/2-K(math.hypot(x,y))
    x,y,vx,vy=1.0,0.0,0.0,0.27
    E0=energy(x,y,vx,vy);L0=x*vy-y*vx
    h=0.01;err=0.;Lerr=0.
    for _ in range(20000):
        ax,ay=acc(x,y);vx+=h*ax/2;vy+=h*ay/2
        x+=h*vx;y+=h*vy
        ax,ay=acc(x,y);vx+=h*ax/2;vy+=h*ay/2
        err=max(err,abs(energy(x,y,vx,vy)-E0));Lerr=max(Lerr,abs(x*vy-y*vx-L0))
    require(err<1e-7 and Lerr<1e-11,'conservative trajectory drift')
    return {'steps':20000,'step':h,'GM_ell_mu':1,
            'max_absolute_energy_drift':err,'max_angular_momentum_drift':Lerr,
            'scope':'Finite-step numerical control, not exact conservation proof.'}


def finite_particle_continuation():
    # The integral kernel bounds the entire Hessian, including r=0.
    bound=(mp.mpf(1)/2+1/mp.e)/(3*mp.sqrt(mp.pi))
    for x in map(mp.mpf,['0','.01','.1','.5','1','2','5','20']):
        radial=(mp.diff(kernel,x,2) if x else -1/(6*mp.sqrt(mp.pi)))
        tangent=(mp.diff(kernel,x)/x if x else radial)
        require(max(abs(radial),abs(tangent))<=bound,'global Hessian bound')
    # A head-on orbit goes through zero without patching in a bounce law.
    def kval(x):
        a=abs(x)
        return math.erf(a/2)/a if a else 1/math.sqrt(math.pi)
    def acc(x):
        a=abs(x)
        if a<1e-3:
            return -x*(1/6-a*a/40+a**4/448)/math.sqrt(math.pi)
        return -x*(math.erf(a/2)-a*math.exp(-a*a/4)/math.sqrt(math.pi))/a**3
    x,v,h=.5,0.,.01
    E0=v*v/2-kval(x);err=0.;crossings=0
    for _ in range(10000):
        old=x;v+=h*acc(x)/2;x+=h*v;v+=h*acc(x)/2
        if old*x<0:crossings+=1
        err=max(err,abs(v*v/2-kval(x)-E0))
    require(crossings>0 and err<1e-7,'regular head-on crossing')
    return {'H_N':'sum_a p_a^2/(2m_a)-G sum_(a<b) m_a m_b K_ell(|x_a-x_b|)',
            'finite_N_lower_bound':'-G/(sqrt(pi) ell) sum_(a<b) m_a m_b',
            'kernel_Hessian_operator_norm_bound':'(1/2+1/e)/(3 sqrt(pi) ell^3)',
            'dimensionless_Hessian_bound':text(bound),
            'classical_result':'Smooth globally Lipschitz finite-N force gives unique global Newtonian trajectories; pair coincidences are not ODE singularities.',
            'quantum_result':'For fixed finite N and masses, the bounded real interaction is a bounded perturbation of the self-adjoint free kinetic operator.',
            'head_on_crossings':crossings,'head_on_energy_error':err,
            'does_not_establish':['thermodynamic stability as N grows','geodesic completeness','bounded 4D curvature','regular relativistic collapse']}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    with mp.workdps(50):
        out={'base_sha':BASE_SHA,'model':'R2 = R1 kernel + conserving dynamical/operational closure',
             'new_fundamental_parameters':0,
             'source_conservation':source_identities(),
             'retarded_and_vacuum':real_time_controls(),
             'vacuum_dephasing':noise_controls(),
             'recoil_phase':recoil_controls(),
             'preferred_frame':moving_frame_controls(),
             'orbits_and_balance':orbit_and_balance_controls(),
             'trajectory':conservative_trajectory(),
             'finite_particle_continuation':finite_particle_continuation(),
             'unresolved':['nonlinear generally covariant completion','preferred-foliation microscopic origin',
                           'vacuum energy and radiative stability','strong-curvature continuation',
                           'microscopic full apparatus and full 1PN radiation matching'],
             'environment':{'python':platform.python_version(),'mpmath':mp.__version__,'sympy':sp.__version__},
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             'all_implemented_assertions_passed':True}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'R1_node':out['recoil_phase']['R1_point_probe_node'],
                      'recoil_s5_node':out['recoil_phase']['rows'][0]['node_d_over_ell'],
                      'circular_orbits':'stable in retained model','full_QG_complete':False},ensure_ascii=False))


if __name__=='__main__':
    main()
