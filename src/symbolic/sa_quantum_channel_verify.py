"""Separate checks for the SA scalar/pulse audit; never imports its generator.

A finite detector law is checked algebraically. Its control numbers are NOT
probabilities of the full two-shell past-directed experiment.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
import mpmath as mp
import sympy as s


def symbolic_verification():
    z=s.symbols('z',real=True); h=s.exp(-1/(1-z*z))
    hp=s.diff(h,z); hpp=s.diff(h,z,2)
    assert s.simplify(hp/h+2*z/(1-z*z)**2)==0
    assert s.simplify(hpp/h-(4*z*z/(1-z*z)**4-2/(1-z*z)**2-8*z*z/(1-z*z)**3))==0
    # Receiver qubit: a compactly smeared single field observable; sigma_z^2=I.
    theta=s.symbols('theta',real=True)
    U=s.diag(s.exp(-s.I*theta),s.exp(s.I*theta))
    rho=s.Matrix([[1,1],[1,1]])/2; sy=s.Matrix([[0,-s.I],[s.I,0]])
    assert s.simplify(s.expand_complex(s.trace(U*rho*U.conjugate().T*sy))-s.sin(2*theta))==0
    # Exact 4D coherent displacement stress is insensitive to the sign bit.
    f=s.symbols('f',nonzero=True);rr=s.symbols('r',positive=True)
    g=s.diag(-f,1/f,rr**2,rr**2);gi=g.inv()
    p=s.Matrix(s.symbols('p0:4',real=True));norm=(p.T*gi*p)[0]
    tp=p*p.T-g*norm/2
    assert tp==(-p)*(-p).T-g*((-p).T*gi*(-p))[0]/2
    # Two-ended 4D zero-frequency solution from its radial differential equation.
    r,m,e=s.symbols('r m e',positive=True); D=r*r-2*m*r+e*e
    for ell in (0,1,2,3):
        R=s.legendre(ell,(r-m)/s.sqrt(m*m-e*e))
        assert s.simplify(s.diff(D*s.diff(R,r),r)-ell*(ell+1)*R)==0
    # The singular endpoint admits constant and linear leading phi, both L2.
    assert s.integrate(r**4,(r,0,s.Rational(1,10)))>0
    assert s.integrate(r**6,(r,0,s.Rational(1,10)))>0
    return {'receiver_unitary':True,'bit_stress_equality':True,
            '4d_static_radial_ODE_ell_0_to_3':True,'derivative_and_endpoint_checks':True}


def independent_numbers(dps):
    with mp.workdps(dps):
        # A different integration variable and finite tail estimate.
        def values(u):
            c=mp.cosh(u);sh=mp.sinh(u);h=mp.exp(-c*c)
            hz=-2*sh*c**3*h
            hzz=(4*sh**2*c**6-2*c**4-8*sh**2*c**4)*h
            return mp.tanh(u),h,hz,hzz,1/c**2
        cuts=[-4,-2,-1,0,1,2,4]
        def integ(fn):return mp.quad(lambda u:fn(*values(u)),cuts)
        area=integ(lambda z,h,hz,hzz,j:h*j)
        moment=integ(lambda z,h,hz,hzz,j:mp.exp(z)*h*j)
        cancelled=integ(lambda z,h,hz,hzz,j:mp.exp(z)*(h+hz)*j)
        E0=integ(lambda z,h,hz,hzz,j:hz*hz*j)
        E2=integ(lambda z,h,hz,hzz,j:hzz*hzz*j)
        direct=integ(lambda z,h,hz,hzz,j:(hzz+hz)**2*j)
        assert abs(cancelled)<mp.mpf('1e-45')
        assert abs(direct-E0-E2)<mp.mpf('1e-44')
        t0=mp.cosh(4)**2
        # For area/moments, each omitted half is <= e*exp(-t0)/t0^2.
        assert 2*mp.e*mp.exp(-t0)/t0**2<mp.mpf('1e-300')
        # Enumerate analytic pole slots, not actual residues or a full spectrum.
        rows=[]
        for qtext in ('.5','.99','.999'):
            q=mp.mpf(qtext);d=mp.sqrt(1-q*q);p=((1-d)/(1+d))**2
            kp=d/(mp.mpf(1)/5*(1+d)**2);km=d/(mp.mpf(1)/5*(1-d)**2)
            assert abs(kp/km-p)<mp.mpf('1e-45')
            T=2/(q*q)-1;R=-2*d/(q*q)
            assert abs(T*T-R*R-1)<mp.mpf('1e-44')
            rows.append({'charge_ratio':qtext,'p':mp.nstr(p,46),'T_zero':mp.nstr(T,46),
                         'R_zero':mp.nstr(R,46),'slots':int(mp.ceil(1/p)-1)})
        # Numerical controls: integrate the actual spectral measure of Phi(F).
        controls=[]
        for lam,mu,var in ((mp.mpf('.8'),mp.mpf('.2'),mp.mpf('.3')),
                           (mp.mpf('.5'),mp.mpf('0'),mp.mpf('1')),
                           (mp.mpf('1'),mp.mpf('.4'),mp.mpf('.7'))):
            exact=mp.exp(-2*lam*lam*var)*mp.sin(2*lam*mu)
            avg=mp.quad(lambda x:mp.exp(-x*x/2)/mp.sqrt(2*mp.pi)*mp.sin(2*lam*(mu+mp.sqrt(var)*x)),[-mp.inf,0,mp.inf])
            assert abs(exact-avg)<mp.mpf('1e-44')
            for sign in (-1,1):
                probs=[(1+y*sign*exact)/2 for y in (-1,1)]
                assert sum(probs)==1 and all(0<=p<=1 for p in probs)
            controls.append({'lambda':str(lam),'test_mu':str(mu),'test_variance':str(var),
                'algebra_only_D':mp.nstr(abs(exact),46),'physical_past_probability':False})
        # A displaced input pulse restores the Laplace moment; tune error never zeroed.
        eps=mp.mpf('1e-6')
        actual=integ(lambda z,h,hz,hzz,j:mp.exp(z)*(hz+(1+eps)*h)*j)
        assert abs(actual-eps*moment)<mp.mpf('1e-44') and abs(actual)>0
        return {'area':mp.nstr(area,46),'moment':mp.nstr(moment,46),
                'E0':mp.nstr(E0,46),'E1':mp.nstr(direct,46),
                'energy_ratio':mp.nstr(direct/E0,46),'geometries':rows,
                'receiver_algebra_controls':controls,'error_moment':mp.nstr(actual,46)}


def candidate(numbers):
    unknown={'computed':False,'distribution':None,
             'reason':'No global positive Hadamard bisolution, prepared exterior source, and receiver beyond both shells have been constructed.'}
    state_names=['literature','classical_geometry','quantum_source','backreaction','support_accounting','stability','information_channel']
    c={'candidate_id':'sa-shaped-horizon-pulse-v4','status':'B','dimension':4,'dimension_split':{'space':3,'time':1},
       'geometry':'Exact classical Schein-Aichelburg MP/two-shell/extended-RN geometry; R=m1=1,d=3,M=1/5; Q/M=.99 test.',
       'matter_content':'Classical charged shells and Maxwell; neutral massless minimally coupled quantum test scalar; compactly switched degenerate qubit receiver.',
       'quantum_state':'Reference zero-mean Gaussian state only conditional. Smooth coherent displacements specified at one outer horizon; no full two-shell state.',
       'topology':'Same MP exterior sewn to different blocks of eternal RN. Timelike singularities and Cauchy horizons remain.',
       'assumptions':['Imported KSR RN-interior scattering theorem with purely incoming characteristic data and unchanged second branch.',
                      'Fixed smooth background is tested, not imposed as a solved backreacted quantum spacetime.',
                      'Matched scalar has no direct shell coupling; no postselection.',
                      'Tail cancellation is imposed on horizon data; its preparation by a finite exterior source is NOT proved.'],
       'boundary_conditions':'Phi and the oriented normal derivative continuous on each shell. Other horizon sectors and singularity boundary data are unresolved.',
       'symmetries':['Axisymmetric MP exterior; spherical RN interior; ell=0 signal component only. Angular modes of the quantum state are not discarded.'],
       'approximation_order':'Exact classical piecewise 4D wave operators; linear test field; imported late-horizon asymptotic. No global renormalized source.',
       'stress_energy':{'kind':'conditional_coherent_difference','formula':'Delta<T_ab>_ren = T_ab[phi], identical for +/-phi where reference state is Hadamard.',
                        'renormalized':False,'full_tensor_matched':False},
       'backreaction':{'level':'necessary_regularity_test','details':'For an uncancelled first pole, the CH_B trace approaching B+ has coherent T_VV scaling |V|^(2p-2); KSR propagates C1 failure to CH_A. No full SA route or final geometry solved.'},
       'support_accounting':{'complete':False,'details':'Same positive-energy shell certificate is retained; horizon-pulse energy ratio calculated, not pump work or fabrication budget.'},
       'stability':'First-pole cancellation has codimension one. A small admixture restores this singular term. Higher poles, all other branches, gravity, and charge loss are not controlled.',
       'causal_structure':'Past-directed classical route imported from SA; no actual source-to-past-detector Green function obtained.',
       'sender_intervention':{'description':'Opposite signs of f(v)=h(kappa+ v)+hprime(kappa+ v). Horizon data, not an implemented exterior source.',
           'same_preparation':True,'uses_postselection':False,'future_boundary_condition_is_input':False},
       'receiver_observable':'Stored sigma_y outcome +/-1 after compact smooth coupling lambda*sigma_z*Phi(F).',
       'P_Y_do_0':dict(unknown),'P_Y_do_1':dict(unknown),
       'distinguishability':{'metric':'total_variation','computed':False,'value':None,'error_bound':None,'receiver_precedes_sender':None},
       'conditional_receiver_formula':'P_b(y)=[1+y*(-1)^b*exp(-2 lambda^2 V_F)*sin(2 lambda s_F)]/2. s_F,V_F not obtained for the complete device.',
       'obstructions':['Ordinary one-sided nonnegative compact ell=0 horizon pulses with nonzero first pole moment fail C1 on CH_A and B+ in the KSR fixed-RN sector, not every finite-v point of CH_B.'],
       'unresolved_assumptions':['Global quantum two-point function and all its shell/horizon/singularity conditions.',
           'Finite exterior source that prepares the specified horizon pulse.', 'All poles/branches and quantum stress, not only the first classical coherent tail.',
           'Finite apparatus and self-consistent time-dependent geometry.', 'Actual past receiver mean, variance and stored record.'],
       'assumption_changes':[{'field':'interior charge ratio','old':'Q/M=.5','new':'Q/M=.99','reason':'Raises p=kappa+/kappa- while retaining the same shell DEC bound.'},
           {'field':'signal shape','old':'one-sided nonnegative compact horizon pulse h','new':'h+hprime','reason':'Cancel only the leading KSR pole without erasing the zero-frequency area.'}],
       'stages':{str(i+1):{'name':n,'state':'partial'} for i,n in enumerate(state_names)},
       'literature':[
         {'title':'Traversable Wormholes in Geometries of Charged Shells','authors':'Schein and Aichelburg','year':1996,'url':'https://arxiv.org/abs/gr-qc/9606069','used_for':'same-exterior classical geometry; not quantum state','checked_on':'2026-09-24'},
         {'title':'A scattering theory for linear waves on the interior of Reissner-Nordstrom black holes','authors':'Kehle and Shlapentokh-Rothman','year':2019,'url':'https://arxiv.org/abs/1804.05438','used_for':'Proposition 2.5; Theorems 3-5, especially compact-input first-pole obstruction','checked_on':'2026-09-24'},
         {'title':'Regular Quantum States on the Cauchy Horizon of a Charged Black Hole','authors':'Taylor','year':2020,'url':'https://arxiv.org/abs/1904.05941','used_for':'Counterexample to claiming that every RN horizon state is singular; not transplanted to shells','checked_on':'2026-09-24'},
         {'title':'Dynamics in Non-Globally-Hyperbolic Static Spacetimes II','authors':'Ishibashi and Wald','year':2003,'url':'https://arxiv.org/abs/gr-qc/0305012','used_for':'Boundary dynamics in a static sector, not global CTC quantization','checked_on':'2026-09-24'}],
       'code':['src/symbolic/sa_quantum_channel_gate.py','src/symbolic/sa_quantum_channel_verify.py'],
       'verification':{'computational':'separate_derivations_checked','external_peer_review':'not_performed','human_review_for_A':True},
       'scope':'B is an engineered characteristic pulse and a field/detector compatibility target, not a functioning past channel.',
       'calculation':{'charge_ratios':['.5','.99','.999'],'tested_geometry_points':3,
                      'geometry_trials':numbers['geometries'],
                      'numerical_error_budget':'50/80 dps; 1e-40 numerical agreement, not a rigorous global quadrature bound',
                      'horizon_pulse_equal_area_energy_ratio':numbers['energy_ratio'],
                      'receiver_control_numbers_are_not_device_probabilities':True}}
    return c


def reject_false_success(c):
    assert c['status']=='B' and c['unresolved_assumptions']
    assert c['dimension_split']=={'space':3,'time':1} and c['dimension']==4
    assert c['verification']['human_review_for_A'] is True
    for name in ('P_Y_do_0','P_Y_do_1'):
        assert c[name]['computed'] is False and c[name]['distribution'] is None and c[name]['reason']
    assert c['distinguishability']['value'] is None and c['support_accounting']['complete'] is False


def main():
    p=argparse.ArgumentParser();p.add_argument('--output',type=Path);args=p.parse_args()
    exact=symbolic_verification();lo=independent_numbers(50);hi=independent_numbers(80)
    for k in ('area','moment','E0','E1','energy_ratio','error_moment'):
        with mp.workdps(90):assert abs(mp.mpf(lo[k])-mp.mpf(hi[k]))<mp.mpf('1e-40')
    c=candidate(hi);reject_false_success(c)
    bad=dict(c);bad['status']='A'
    try:reject_false_success(bad)
    except AssertionError:pass
    else:raise AssertionError('An unconstructed A must fail')
    result={'source_base_sha':'2304cbc39b638491d20cb9ece2f44b05bb216426',
            'python':platform.python_version(),'sympy':s.__version__,'mpmath':mp.__version__,
            'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'exact':exact,'independent_numbers':hi,'candidates':[c],
            'counts':{'A':0,'B':1,'C':0},'external_peer_review':'not_performed'}
    text=json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(text+'\n',encoding='utf-8')
    print(text);print('PASS separate pulse, 4D ODE and receiver algebra checks; global channel still unknown.')

if __name__=='__main__':main()
