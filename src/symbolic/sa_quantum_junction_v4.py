"""4D SA transmission conditions, endpoint data and finite Ramsey record.

This is NOT a global state construction. The common-KMS obstruction applies only
under the explicitly stated two-sided equilibrium/regularity assumptions.
Run directly; only stdout is written. See notes/sa-quantum-record-v4.md.
"""
from __future__ import annotations
import json
import hashlib
from pathlib import Path
import platform
import sympy as sp
import mpmath as mp


def exact_checks() -> dict:
    t,x,y,z,r,theta = sp.symbols('t x y z r theta', real=True)
    m,q = sp.symbols('m q', positive=True)
    ell,omega = sp.symbols('ell omega', real=True)
    U = sp.Function('U')(x,y,z)
    phi = sp.Function('phi')(t,x,y,z)
    # sqrt(-g)=U^2; sqrt(-g) g^{ab}=diag(-U^4,1,1,1).
    numerator = sp.diff(-U**4*sp.diff(phi,t),t)
    numerator += sum(sp.diff(phi,v,2) for v in (x,y,z))
    assert sp.simplify(numerator+U**4*sp.diff(phi,t,2)
                       -sum(sp.diff(phi,v,2) for v in (x,y,z))) == 0
    gmp=sp.diag(-U**-2,U**2,U**2,U**2)
    assert sp.simplify(gmp.det()+U**4)==0
    f = 1-2*m/r+q*q/r**2
    u=sp.Function('u')(r)
    V=f*(ell*(ell+1)/r**2+sp.diff(f,r)/r)
    radial=r*f*(omega**2/f*u/r+sp.diff(r*r*f*sp.diff(u/r,r),r)/r**2
                -ell*(ell+1)*u/r**3)
    expected=f**2*sp.diff(u,r,2)+f*sp.diff(f,r)*sp.diff(u,r)+(omega**2-V)*u
    assert sp.simplify(radial-expected)==0

    U0,F,A = sp.symbols('U0 F A',positive=True)
    clock_rate=1/(U0*sp.sqrt(F))  # dt_RN/dT_MP
    assert sp.simplify(F*clock_rate**2-1/U0**2)==0
    # Same outward normal, no scalar surface action: phi continuous and n.dphi continuous.
    value,dmp,drn=sp.symbols('value dmp drn',complex=True)
    matched_drn=dmp/(U0*sp.sqrt(F))
    assert sp.simplify(sp.sqrt(F)*matched_drn-dmp/U0)==0
    # KG flux equality follows pointwise, not just after angular averaging.
    assert sp.simplify(sp.conjugate(value)*(sp.sqrt(F)*matched_drn-dmp/U0))==0

    # r=0 is limit-circle for each fixed angular momentum; not hidden by ray turning.
    leading=sp.limit((r**3/(3*q*q))**2*V,r,0,dir='+')
    assert leading==sp.Rational(-2,9)
    a=sp.symbols('a')
    indices=sp.solve(a*(a-1)-leading,a)
    assert set(indices)=={sp.Rational(1,3),sp.Rational(2,3)}
    assert sp.limit((r**2/f)/r**4,r,0)==1/q**2
    assert sp.limit(r**2*f,r,0)==q**2

    rp,rm=sp.symbols('rp rm',positive=True)
    p=(rp-r)*(rm-r)
    I=sp.log(rm*(rp-r)/(rp*(rm-r)))/(rp-rm)
    assert sp.simplify(sp.diff(I,r)-1/p)==0
    assert sp.simplify(sp.diff(p*sp.diff(I,r),r))==0
    assert sp.simplify(I.subs(r,0))==0
    assert sp.simplify(sp.diff(I,r).subs(r,0)-1/(rp*rm))==0
    # Bulk energy and endpoint symplectic flux permit both phi(0)=0 and p phi'(0)=0.
    # Their threshold reflection phases are -1 and +1 respectively; no probability claim.

    # Inter-horizon zero-frequency l=0 connection, not an exterior probability.
    B=(rm/rp+rp/rm)/2
    C=(rm/rp-rp/rm)/2
    assert sp.simplify(B*B-C*C)==1
    assert sp.simplify(B+C-rm/rp)==0
    assert sp.simplify(B-C-rp/rm)==0
    rr_p=(2+sp.sqrt(3))/10; rr_m=(2-sp.sqrt(3))/10
    assert sp.simplify(B.subs({rp:rr_p,rm:rr_m}))==7
    assert sp.simplify(C.subs({rp:rr_p,rm:rr_m}))==-4*sp.sqrt(3)

    # One common Killing-temperature ansatz: smooth local Euclidean horizon requires
    # beta * kappa_T = 2 pi at EACH bifurcate horizon. The conditions differ.
    kplus=(rp-rm)/(2*rp**2); kminus=(rp-rm)/(2*rm**2)
    assert sp.simplify(kminus/kplus-(rp/rm)**2)==0
    kvals={rp:rr_p,rm:rr_m}
    assert sp.simplify(kminus.subs(kvals)-kplus.subs(kvals))==240
    ratio=sp.simplify((kminus/kplus).subs(kvals))
    assert sp.simplify(ratio-(97+56*sp.sqrt(3)))==0

    # Equal-stress coherent sign encoding: all minimal-scalar components are even.
    deriv=sp.Matrix(sp.symbols('d0:4',real=True)); metric=sp.diag(-1,1,1,1)
    stress=deriv*deriv.T-metric*(deriv.T*metric*deriv)[0]/2
    stress_minus=stress.xreplace({v:-v for v in deriv})
    assert sp.simplify(stress-stress_minus)==sp.zeros(4)
    # Detector parity: Z flips the UDW monopole but leaves the energy observable.
    sx=sp.Matrix([[0,1],[1,0]]); sz=sp.diag(1,-1); pe=sp.diag(1,0)
    assert sz*sx*sz == -sx
    assert sz*pe*sz == pe

    values={
        'dimension':4,
        'metric':'MP exterior + extended RN interior, equal proper time at both shells',
        'MP_wave_equation':'(-U^4 d_T^2 + flat_Delta) phi = 0',
        'RN_radial_potential':str(V),
        'clock_rate_dt_dT':str(clock_rate),
        'shell_matching':['[phi]=0','U0^-1 d_rho phi_MP = sqrt(f_A) d_r phi_RN'],
        'nonminimal_shell_coupling_used':False,
        'endpoint_inverse_square':str(leading),
        'endpoint_indices':[str(v) for v in sorted(indices)],
        'endpoint_field_branches':['constant','linear in r'],
        'both_branches_locally_L2_and_finite_bulk_energy':True,
        'zero_frequency_reflection':{'Dirichlet_phi_at_0':-1,'Neumann_phi_at_0':1},
        'inter_horizon_l0_low_frequency':{'B':7,'C':'-4*sqrt(3)','B2_minus_C2':1},
        'horizon_temperature_ratio':str(ratio),
        'common_KMS_both_bifurcate_horizons':'incompatible for 0<abs(q)<m',
        'finite_ramsey_law':'P(y|do(b))=[1+y*(-1)^b*exp(-2*V_h)*sin(2*m_h)]/2',
        'receiver_window':'h has compact spacetime support; coupling included in h',
        'actual_SA_m_h':None,'actual_SA_V_h':None,
        'sign_code_energy_readout':'identical distributions for a parity-invariant base state',
        'coherent_sign_stress_equal':True,
        'global_state_constructed':False,'past_receiver_probabilities_computed':False,
    }
    return values


def probability_controls(dps:int) -> list[dict]:
    """Independent real integrals over the Gaussian field observable, not SA data."""
    with mp.workdps(dps):
        out=[]
        for mu_s,var_s in [('0','0.5'),('0.2','0.5'),('0.7','0.1'),('0.2','2')]:
            mu=mp.mpf(mu_s);var=mp.mpf(var_s)
            for bit in (0,1):
                mean=(-1)**bit*mu
                norm=mp.sqrt(2*mp.pi*var)
                def pdf(v): return mp.exp(-(v-mean)**2/(2*var))/norm
                for result in (-1,1):
                    val=mp.quad(lambda v:pdf(v)*(1+result*mp.sin(2*v))/2,
                                [-mp.inf,mean-6*mp.sqrt(var),mean,mean+6*mp.sqrt(var),mp.inf])
                    expected=(1+result*(-1)**bit*mp.exp(-2*var)*mp.sin(2*mu))/2
                    assert abs(val-expected)<mp.mpf('1e-40')
                    assert 0 <= expected <= 1
                pp=(1+(-1)**bit*mp.exp(-2*var)*mp.sin(2*mu))/2
                out.append({'mu_control':mu_s,'variance_control':var_s,'bit':bit,
                            'P_y_plus_control':mp.nstr(pp,45)})
        return out



def flat_receiver_noise(dps:int) -> dict:
    """Actual 4D inertial-vacuum finite-time control, NOT the full SA covariance.

    chi(t)=sin^4(pi*t/T) on (0,T), pointlike gapless detector. C^3 switching
    makes this Wightman variance finite; smooth approximants give the same limit.
    The dimensionless result is T independent for a massless 4D vacuum.
    """
    with mp.workdps(dps):
        def sinc(x):return mp.sin(x)/x if x else mp.mpf(1)
        def amp(u):
            return (mp.mpf(3)/8*sinc(u/2)
                    +sum(sinc((u+sgn*2*mp.pi)/2) for sgn in (-1,1))/4
                    +sum(sinc((u+sgn*4*mp.pi)/2) for sgn in (-1,1))/16)
        cutoff=128*mp.pi
        val=sum(mp.quad(lambda u:u*amp(u)**2/(4*mp.pi**2),
                        [n*mp.pi,(n+1)*mp.pi]) for n in range(128))
        tail=mp.mpf(576)*mp.pi**6*(mp.mpf(4096)/2025)/(8*cutoff**8)
        return {'model':'4D Minkowski inertial-vacuum local noise CONTROL only',
                'switching':'sin^4(pi*t/T), 0<t<T; zero elsewhere',
                'spectral_cut_integral':mp.nstr(val,48),
                'positive_tail_upper_bound':mp.nstr(tail,25),
                'pointlike_detector':True,'actual_SA_noise':False}


def main() -> None:
    result=exact_checks()
    result['generator_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    low=probability_controls(50);high=probability_controls(80)
    for a,b in zip(low,high):
        with mp.workdps(80):
            assert abs(mp.mpf(a['P_y_plus_control'])-mp.mpf(b['P_y_plus_control']))<mp.mpf('1e-40')
    result['gaussian_integral_controls']=high
    noise_lo=flat_receiver_noise(50);noise_hi=flat_receiver_noise(80)
    with mp.workdps(90):
        assert abs(mp.mpf(noise_lo['spectral_cut_integral'])-mp.mpf(noise_hi['spectral_cut_integral']))<mp.mpf('1e-40')
    result['finite_time_4D_noise_control']=noise_hi
    result['runtime']={'python':platform.python_version(),'sympy':sp.__version__,'mpmath':mp.__version__}
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':
    main()
