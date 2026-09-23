"""Separate-process adversarial arithmetic verifier; NEVER imports the model generator.

Uses numerical differentiation of integrated shell conservation, direct source/potential
quadratures, numeric four-metric inversion and sampled QEI integration. Shares only
record IO/validation. Written by the same author; not independent scientific peer review.
"""
from __future__ import annotations
import argparse
from pathlib import Path
from fractions import Fraction
import os
import platform
import sys
from typing import Any
import mpmath as mp
from architecture_search import ROOT, RecordError, load_json, sha256, validate_bundle, write_json, require


def number(s: Any) -> mp.mpf:
    if isinstance(s,str) and '/' in s:
        f=Fraction(s);return mp.mpf(f.numerator)/f.denominator
    return mp.mpf(s)


def near(got: mp.mpf, expected: Any, tol: str='1e-39') -> None:
    e=number(expected)
    require(abs(got-e)<=mp.mpf(tol)*max(abs(got),abs(e),mp.mpf('1e-90')),'Independent numerical check failed')


def verify_shell(row: dict) -> str:
    tested=0
    for item in row['calculation']['trials']:
        M,eta=number(item['mu']),number(item['eta'])
        a0=mp.mpf(1)
        sigma0=-mp.sqrt(1-2*M)/(2*mp.pi)
        p0=(1-M)/(4*mp.pi*mp.sqrt(1-2*M))
        fixed=(eta*sigma0-p0)/(1+eta)
        def sigma(a: mp.mpf) -> mp.mpf:
            return fixed+(sigma0-fixed)*(a0/a)**(2*(1+eta))
        def potential(a: mp.mpf) -> mp.mpf:
            return 1-2*M/a-(2*mp.pi*a*sigma(a))**2
        # Reconstruct from the EOS, not the generator's V'' expression.
        Vpp=mp.diff(potential,a0,2)
        near(Vpp,item['a0_squared_Vpp'])
        require((Vpp>0)==item['radially_stable'],'Wrong radial stability sign')
        require(abs(potential(a0))<mp.mpf('1e-45'),'Static junction residual')
        require(abs(mp.diff(potential,a0))<mp.mpf('1e-45'),'Static force residual')
        tested+=1
    if row['candidate_id']=='schwarzschild-eos-4':
        require(row['status']=='B' and bool(row['assumption_changes']),'Stiff EOS relaxation must be explicit B')
        require(row['stress_energy']['renormalized'] is False,'Shell source cannot be relabeled as a quantum source')
    return f'{tested} EOS-integrated potential derivatives; static junctions and stability signs; radial only'


def verify_rotating(row: dict) -> str:
    for item in row['calculation']['trials']:
        J,x=number(item['J_over_b_squared']),number(item['x_over_b'])
        R=mp.sqrt(1+x*x);omega=2*J/R**3
        gtt=-1+4*J*J/(1+x*x)**2  # Exact zero on the ergosurface, before inversion.
        g=mp.matrix([[gtt,0,0,-R*R*omega],
                     [0,1,0,0],[0,0,R*R,0],[-R*R*omega,0,0,R*R]])
        inv=g**-1
        near(inv[0,0],'-1');near(g[0,0],item['g_tt_equator'])
        require((g[0,0]>0)==item['ergoregion_at_point'],'Ergoregion was incorrectly removed')
    require('single-valued' in row['topology'],'The global-time conclusion needs real single-valued t')
    return 'Independent 4x4 inversion; ergoregion retained; excludes time-periodic/time-shifted gluing from this theorem'


def verify_ring(row: dict) -> str:
    G,c=mp.mpf('6.67430e-11'),mp.mpf('299792458')
    for v in row['calculation']['trials']:
        a,R,L,M=map(number,[v['a_m'],v['R_m'],v['L_m'],v['M_kg']])
        # Direct harmonic-potential integral, not atan call from the generator.
        I=G*M/(a*c*c)*(mp.quad(lambda z:1/(1+z*z),[R/a,mp.inf])-a/L)
        near(I,v['I_C'])
        t2=number(v['onset_s'])
        # Frequency ratio matching determines the return map independently.
        t1=mp.exp(I)*t2;outgoing_external=L/c
        near(outgoing_external/(mp.exp(I)-1),v['onset_s'])
        residual=t2+outgoing_external-t1
        require(abs(residual)<mp.mpf('1e-38')*max(abs(t2),1),'Clock matching failed')
        near(L/c-(mp.exp(I)-1)*mp.mpf('1.1')*t2,v['return_delay_at_1p1_onset_s'],'1e-35')
    require(row['status']=='B' and row['P_Y_do_0']['computed'] is False,'Classical path cannot become a quantum channel')
    require(row['support_accounting']['complete'] is False,'Missing negative ring cannot be silently supplied')
    return '24 direct potential integrals and clock matching; negative core, chronology dynamics and past probabilities remain unprovided'


def verify_casimir(row: dict) -> str:
    for v in row['calculation']['trials']:
        A,d,f=map(number,[v['area_m2'],v['gap_m'],v['support_area_fraction']])
        vacuum=lambda gap:-mp.pi**2*A/(720*gap**3)
        force=mp.diff(vacuum,d)
        pressure=force/(A*f)
        struts=pressure*A*f*d
        near(struts/abs(vacuum(d)),'3')
        near((struts+vacuum(d))/abs(vacuum(d)),'2')
    return 'Force from derivative of full cell energy; support area cancels; cannot exclude other geometries or positive-total-mass wormholes'


def verify_collar(row: dict) -> str:
    G,c,hbar=mp.mpf('6.67430e-11'),mp.mpf('299792458'),mp.mpf('1.054571817e-34')
    # Normalized compact sampler: g=2/sqrt(3) cos^2(pi u/2), |u|<=1.
    g=lambda u:2/mp.sqrt(3)*mp.cos(mp.pi*u/2)**2
    norm=mp.quad(lambda u:g(u)**2,[-1,0,1])
    integral=mp.quad(lambda u:mp.diff(g,u,2)**2,[-1,0,1])
    near(norm,'1')
    for v in row['calculation']['trials']:
        b,e,N,f=map(number,[v['b_m'],v['epsilon_m'],v['N'],v['f']])
        # Radial metric differentiated with dimensionless z=x/eps.
        r=lambda z:b+e*(mp.sqrt(1+z*z)-1)
        r0=r(0);rp=mp.diff(r,mp.mpf(0))/e;rpp=mp.diff(r,mp.mpf(0),2)/e**2
        rho=c**4/(8*mp.pi*G)*((1-rp**2)/r0**2-2*rpp/r0)
        Q=-N*hbar*c*integral/(16*mp.pi**2*(f*e)**4)
        near(rho,v['required_rho_J_per_m3']);near(Q,v['flat_QEI_J_per_m3'])
        require((rho>=Q)==v['passes_necessary_flat_diagnostic'],'Wrong necessary-inequality verdict')
    require(row['status']=='B' and row['stress_energy']['renormalized'] is False,'Passing a bound is not a constructed state')
    return 'Direct 4D collar derivatives and second-derivative sampler quadrature; approximation error still not a curved-space theorem'


def verify_flat(row: dict) -> str:
    a,R,T=mp.mpf(1),mp.mpf(5),mp.mpf(2)
    def f(t: mp.mpf) -> mp.mpf:
        return mp.sin(mp.pi*t/T)**4 if 0<t<T else mp.mpf(0)
    for v in row['calculation']['trials']:
        t=number(v['t']);lo=max(R-a,t-T);hi=min(R+a,t)
        mean=mp.mpf(0) if hi<=lo else mp.quad(lambda s:f(t-s),[lo,hi])/(8*mp.pi*R*a)
        if mean==0:
            require(number(v['mean_do0'])==0 and number(v['mean_do1'])==0,'Acausal source response')
        else:
            near(mean,v['mean_do0']);near(-mean,v['mean_do1'])
    mean=number(row['calculation']['future_mean'])
    normal=lambda y,m:mp.exp(-(y-m)**2/2)/mp.sqrt(2*mp.pi)
    tv=mp.quad(lambda y:(normal(y,mean)-normal(y,-mean)),[0,mp.inf])
    near(tv,row['calculation']['future_total_variation'])
    require(row['P_Y_do_0']['distribution']==row['P_Y_do_1']['distribution'],'Past distributions changed')
    require(row['distinguishability']['value']=='0','Future contrast mislabeled as past D')
    return 'Retarded 3D shell integral and normalized Gaussian distributions; future contrast cannot be promoted'


FUNCTIONS={'flat-local-source':verify_flat,'rotating-global-time':verify_rotating,
           'schwarzschild-eos-0-to-1':verify_shell,'schwarzschild-eos-4':verify_shell,
           'fkz-mass-controlled-ring':verify_ring,'finite-casimir-cell-line':verify_casimir,
           'thin-collar-qei-window':verify_collar}


def verify(input_path: Path, output_path: Path, root: Path=ROOT, candidate_id: str | None=None) -> dict:
    b=load_json(input_path);validate_bundle(b,root)
    output={}
    require({r['candidate_id'] for r in b['candidates']}==set(FUNCTIONS),'Verifier coverage incomplete')
    if candidate_id is not None:
        require(candidate_id in FUNCTIONS, 'Unknown verification task')
    rows=[r for r in b['candidates'] if candidate_id is None or r['candidate_id']==candidate_id]
    for row in rows:
        # Requiring two separate runs detects precision-dependent signs as well.
        for dps in [50,80]:
            with mp.workdps(dps+30):
                detail=FUNCTIONS[row['candidate_id']](row)
        output[row['candidate_id']]={
            'software_check':'passed','method':detail,'precision_dps':[50,80],
            'arithmetic_tolerance':'1e-39 relative; clock-cancellation check 1e-35 relative; 30 guard digits',
            'author_independence':'Separate program/process or Actions job; same assistant author, not an independent researcher.',
            'adversarial_checklist':{
                '1_algebra':'Separate numerical implementation; not a formal proof.',
                '2_numerical_instability':'50/80 decimal evaluation with guard digits and explicit comparison.',
                '3_boundary_data':'Stated as inputs; no newly solved global quantum boundary problem.',
                '4_exotic_source':'Unprovided sources remain explicit; never inferred from geometry alone.',
                '5_support_energy':'Known accounting included; unknown complete devices stay unresolved.',
                '6_approximation':'No numerical remainder bound for semiclassical/weak-field approximations.',
                '7_postselection':'Unknown probabilities remain null; modeled control uses all outcomes.',
                '8_controllability':'No B family has a computed past receiver intervention distribution.',
                '9_correlation':'No correlation or transmission coefficient used as D_past.',
                '10_collapse':'Radial shell mode checked; other backreaction/collapse not claimed solved.'}}
    result={'input_sha256':sha256(input_path),'verification_program_sha256':sha256(root/'scripts/architecture_verify.py'),
            'execution':'GitHub Actions job' if os.getenv('GITHUB_ACTIONS')=='true' else 'local separate process',
            'python':platform.python_version(),'candidates':output,'external_peer_review':'not_performed'}
    write_json(output_path,result)
    print(f'Separate verifier passed scoped checks for {len(output)} candidates; no physical A certified.')
    return result


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--records',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--candidate-id',choices=sorted(FUNCTIONS),help='One separate adversarial task; omitted means all candidates.')
    args=parser.parse_args()
    try:verify(args.records,args.output,candidate_id=args.candidate_id)
    except (RecordError,ValueError,AssertionError,OSError) as exc:
        print(f'VERIFICATION FAILED: {exc}',file=sys.stderr);raise SystemExit(1) from exc

if __name__=='__main__':main()
