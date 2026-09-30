#!/usr/bin/env python3
"""Independent R3 checks; no import of the forward script.
Canonical constraint ranks, real-space density integration, heat-mixture
moments and binding mass accounting are recomputed by different routes.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import platform
from pathlib import Path
import mpmath as mp
import sympy as sp

BASE_SHA='7e25b4db8a81b6287c9f07e593a1c0f2310132de'


def req(ok,msg):
    if not ok:
        raise AssertionError(msg)


def txt(x):
    return mp.nstr(x,45)


def canonical_rank():
    h=sp.symbols('h11 h22 h33 h12 h13 h23')
    p=sp.symbols('p11 p22 p33 p12 p13 p23')
    k,A,M2=sp.symbols('k A M2',positive=True)
    # Off-diagonal p's here are canonical momenta, 2*pi^ij.
    D=[k*p[4]/2,k*p[5]/2,k*p[2]]
    H=-M2*A*k*k*(h[0]+h[1])/2
    C=p[0]+p[1]+p[2]
    cons=D+[H,C]
    pb=lambda f,g:sum(sp.diff(f,x)*sp.diff(g,y)-sp.diff(f,y)*sp.diff(g,x) for x,y in zip(h,p))
    P=sp.Matrix(5,5,lambda i,j:pb(cons[i],cons[j]))
    gradients=sp.Matrix(cons).jacobian(h+p)
    rank=P.rank();ind=gradients.rank()
    req(rank==2 and ind==5,'canonical constraint rank')
    req(6-(ind-rank)-rank/2==2,'canonical dof')
    req(P[3,4]==-M2*A*k*k,'mixed symbol')
    # Coefficient from scalar/tensor matching, without assuming it in advance.
    c=sp.symbols('c')
    req(sp.solve(sp.Eq(-6+16*c,2),c)==[sp.Rational(1,2)],'curvature matching')
    return {'independent_constraints':ind,'second_class_rank':rank,
            'first_class_count':ind-rank,'gravitational_dof':2,
            'scope':'Flat nonzero spatial Fourier mode; conditional nonlinear count uses invertibility of mixed constraint operator'}


def k2_density(r):
    a=1/mp.sqrt(2)
    # Newton's radial shell formula for rho_eff=e^(-r/a)/(8*pi*a^3).
    if not r:
        return 1/(2*a)
    inner=mp.gammainc(3,0,r/a)/(2*r)
    outer=mp.gammainc(2,r/a,mp.inf)/(2*a)
    return inner+outer


def root_control():
    f=lambda d:2*k2_density(3*d)-k2_density(4*d)-k2_density(2*d)
    lo=mp.mpf('.2');hi=mp.mpf('.6')
    req(f(lo)>0 and f(hi)<0,'bracket')
    for _ in range(220):
        mid=(lo+hi)/2
        if f(mid)>0:lo=mid
        else:hi=mid
    root=(lo+hi)/2
    req(abs(f(root))<mp.mpf('1e-50'),'density-integrated phase root')
    energy=mp.quad(lambda r:4*mp.pi*r*r*mp.exp(-r*r/4)*k2_density(r)/(4*mp.pi)**mp.mpf('1.5'),[0,1,mp.inf])/2
    freq=2/(3*mp.pi)*mp.quad(lambda k:k*k/(1+k*k/2)**2,[0,1,mp.inf])
    return {'P2_node':txt(root),'P2_binding':txt(energy),'P2_core_frequency_squared':txt(freq)}


def mixture(m,r):
    # Schwinger/Gamma mixture, independently of Yukawa polynomial recursion.
    return mp.quad(lambda s:mp.exp((m-1)*mp.log(s)-s-mp.loggamma(m))*mp.erf(r*mp.sqrt(m)/(2*mp.sqrt(s))),[0,1,m,mp.inf])/r


def binding_identity():
    G,M,Mr,Q=sp.symbols('G M_ADM M_rest I_rho_zeta',positive=True)
    eq=sp.Eq(16*sp.pi*G*M+2*(4*sp.pi*G*Q),16*sp.pi*G*Mr)
    solved=sp.solve(eq,M)[0]
    req(sp.simplify(solved-Mr+Q/2)==0,'self-source binding coefficient')
    return str(solved)


def verify_evidence(path,local):
    data=json.loads(path.read_text(encoding='utf-8'))
    src=Path(__file__).with_name('relational_qg_r3_constraints.py')
    req(data['base_sha']==BASE_SHA,'base mismatch')
    req(data['source_sha256']==hashlib.sha256(src.read_bytes()).hexdigest(),'stale source evidence')
    req(data['matching']['curvature_coefficient']=='1/2','curvature coefficient mismatch')
    req(data['matching']['regular_branch_gravitational_dof']==2,'physical dof overclaim')
    req(data['limits']['complete_quantum_gravity'] is False,'full QG overclaim')
    req(data['limits']['generic_singularity_resolution'] is False,'singularity overclaim')
    req(data['hierarchy']['nonlinear_m_to_infinity_limit_proved'] is False,'limit overclaim')
    req(abs(mp.mpf(data['hierarchy']['rows'][0]['point_probe_node'])-mp.mpf(local['P2_node']))<mp.mpf('1e-38'),'P2 phase mismatch')
    req(abs(mp.mpf(data['P2_binding']['binding_coefficient_pair_space'])-mp.mpf(local['P2_binding']))<mp.mpf('1e-38'),'binding mismatch')
    checks=[]
    for row in data['hierarchy']['rows']:
        m=row['order'];d=mp.mpf(row['point_probe_node'])
        req(m in (2,4,8,16,32) and mp.mpf('.1')<d<1,'invalid hierarchy row')
        f=2*mixture(m,3*d)-mixture(m,4*d)-mixture(m,2*d)
        req(abs(f)<mp.mpf('1e-38'),'independent heat-mixture node mismatch')
        c=mp.quad(lambda k:k*k/(1+k*k/m)**m,[0,1,mp.inf])*2/(3*mp.pi)
        req(abs(c-mp.mpf(row['Omega0_squared_ell3_over_GM']))<mp.mpf('1e-38'),'core frequency mismatch')
        checks.append({'order':m,'mixture_phase_residual':txt(f)})
    return {'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'mixture_checks':checks}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--evidence',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    with mp.workdps(65):
        local=root_control()
        out={'base_sha':BASE_SHA,'canonical':canonical_rank(),'radial_density':local,
             'binding_identity':binding_identity(),'global_nonlinear_wellposedness_proved':False}
        if args.evidence:out['evidence']=verify_evidence(args.evidence,local)
        out['all_implemented_assertions_passed']=True
        out['environment']={'python':platform.python_version(),'sympy':sp.__version__,'mpmath':mp.__version__}
        out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verified':True,'P2_node':local['P2_node'],'P2_binding':local['P2_binding'],
                      'two_modes_on_regular_branch':True,'global_QG':False}))


if __name__=='__main__':
    main()
