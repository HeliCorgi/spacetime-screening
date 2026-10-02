#!/usr/bin/env python3
"""Independent verifier for R5. No import of the forward generator.

The kernel is recomputed as a POSITIVE gamma/Dirichlet mixture, not by
partial fractions. Central moments use separate positive Fourier integrals.
Coefficient membership is checked by exact positive-root counts.
Optional evidence is checked numerically and cryptographically, with
physical-overclaim fields rejected. Neither executable needs generated data
from another CI shard.
"""
from __future__ import annotations
import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import random
import mpmath as mp
import sympy as sp

BASE_SHA = 'a0639dd49667a1dac9585aafa99df6408125c472'


def req(ok, why):
    if not ok:
        raise AssertionError(why)


def number(a):
    f = Fraction(str(a))
    return mp.mpf(f.numerator)/f.denominator


def gamma_kernel(x, scale, n):
    y = x/mp.sqrt(scale)
    if n == 2:
        extra = y/2
    elif n == 3:
        extra = 5*y/8+y*y/8
    else:
        raise ValueError('this verifier supports two or three active factors')
    return (-mp.expm1(-y)-mp.exp(-y)*extra)/x


def positive_kernel(x, alpha, nq=64):
    aa = [number(a) for a in alpha if number(a) > 0]
    x = mp.mpf(x)
    if len(set(aa)) == 1:
        return gamma_kernel(x, aa[0], len(aa))
    if len(aa) == 2:
        a, b = aa
        return mp.quad(lambda u: gamma_kernel(x, u*a+(1-u)*b, 2), [0, .5, 1])
    if len(aa) != 3:
        raise ValueError('invalid factor count')
    z, w = mp.gauss_quadrature(nq, 'legendre')
    points = [( (z[i]+1)/2, w[i]/2) for i in range(nq)]
    a, b, c = aa
    # T=sum E_i and V_i=E_i/T are independent; T~Gamma(3,1),
    # V~Dirichlet(1,1,1). S=T sum alpha_i V_i. Density on triangle is 2.
    return mp.fsum(wu*wv*2*(1-u)*gamma_kernel(
        x, a*u+(1-u)*(b*v+c*(1-v)), 3)
        for u, wu in points for v, wv in points)


def positive_moments(alpha):
    aa = [number(a) for a in alpha if number(a) > 0]
    def A(k):
        return mp.fprod(1+a*k*k for a in aa)
    k0 = 2/mp.pi*mp.quad(lambda k: 1/A(k), [0,1,mp.inf])
    kap = 2/(3*mp.pi)*mp.quad(lambda k: k*k/A(k), [0,1,mp.inf])
    c4 = (1/(60*mp.pi)*mp.quad(lambda k:k**4/A(k), [0,1,mp.inf])) if len(aa)==3 else None
    return k0, kap, c4


def coefficient_root_tests():
    b, c, t = sp.symbols('b c t')
    disc = sp.discriminant(t**3-t*t+b*t-c, t)
    rng = random.Random(5102026)
    rows = []
    for _ in range(250):
        bb = sp.Rational(rng.randrange(-10, 50), 100)
        cc = sp.Rational(rng.randrange(1, 70), 1000)
        D = disc.subs({b:bb,c:cc})
        predicted = bool(bb>0 and D>=0)
        # Interior grid: c>0 and D!=0 avoids repeated/zero roots in Sturm count.
        if D == 0:
            continue
        positives = sp.Poly(t**3-t*t+bb*t-cc,t).count_roots(0,sp.oo)
        req(predicted == (positives==3), 'coefficient region vs positive-root count')
        rows.append(predicted)
    for aa in [(sp.Rational(1,3),)*3, (sp.Rational(1,2),sp.Rational(1,2),0)]:
        bb=aa[0]*aa[1]+aa[0]*aa[2]+aa[1]*aa[2];cc=sp.prod(aa)
        req(disc.subs({b:bb,c:cc})==0, 'boundary discriminant')
    return {'interior_coefficient_pairs_checked':len(rows), 'accepted':sum(rows),
            'method':'exact Sturm positive-root count; repeated boundaries separately checked'}


def evidence_preflight(path):
    """Cheap independent checks first; full positive-mixture checks still follow."""
    d=json.loads(path.read_text(encoding='utf-8'))
    req(d['base_sha']==BASE_SHA,'base mismatch')
    f=Path(__file__).with_name('relational_qg_r5_inverse_design.py')
    req(d['source_sha256']==hashlib.sha256(f.read_bytes()).hexdigest(),'stale forward evidence')
    req(d['shared_results']['full_consistent_gravity'] is False,'physical overclaim')
    req(d['shared_results']['nonlinear_stability']=='not_tested','nonlinear overclaim')
    req(d['certificate']['curvature_scalar_coefficient_in_R3_ansatz']=='1/2',
        'incorrect scalar/TT coefficient')
    for row in d['selected_models']:
        req(row['phase_node_unique']=='not_proved','uniqueness overclaim')
        aa=[Fraction(a) for a in row['alpha']]
        req(Fraction(row['b'])==aa[0]*aa[1]+aa[0]*aa[2]+aa[1]*aa[2],
            'coefficient/factor mismatch')
        req(Fraction(row['c'])==aa[0]*aa[1]*aa[2],'coefficient/factor mismatch')
        k0,kp,c4=positive_moments(row['alpha'])
        req(abs(kp-mp.mpf(row['kappa']))<mp.mpf('1e-35'),'positive integral mismatch: kappa')
        active=[a for a in aa if a>0]
        if len(set(active))==1:
            x=mp.mpf(row['bracketed_phase_node']); n=len(active)
            residual=2*gamma_kernel(3*x,mp.mpf(1)/n,n)-gamma_kernel(4*x,mp.mpf(1)/n,n)-gamma_kernel(2*x,mp.mpf(1)/n,n)
            req(abs(residual)<mp.mpf('1e-35'),'independent node mismatch')
    for row in d['robustness_margins']:
        e=Fraction(row['eta']); aa=[str(1-2*e),str(e),str(e)]
        k0,kp,c4=positive_moments(aa)
        req(abs(kp-mp.mpf(row['kappa_interval'][1]))<mp.mpf('1e-30'),
            'robust upper bound mismatch')


def run(evidence=None):
    with mp.workdps(60):
        if evidence is not None:
            evidence_preflight(evidence)
        structural=coefficient_root_tests()
        models=[('1/2','1/2','0'),('1/3','1/3','1/3'),('1/2','1/3','1/6'),
                ('4/5','1/10','1/10'),('9/10','1/20','1/20'),
                ('99/100','1/100','0'),('9999/10000','1/10000','0')]
        controls=[]
        for aa in models:
            k0,kap,c4=positive_moments(aa)
            xs=['0.25','1','2']
            kernels=[]
            for x in xs:
                low=positive_kernel(x,aa,48)
                high=positive_kernel(x,aa,80)
                # This is a quadrature refinement check, not 60-digit accuracy.
                req(abs(high-low)<mp.mpf('1e-17'),'positive mixture quadrature not converged')
                kernels.append({'x':x,'kernel':mp.nstr(high,35),
                                'refinement_difference':mp.nstr(abs(high-low),8)})
            controls.append({'alpha':list(aa),'kernel_center':mp.nstr(k0,40),
                             'kappa':mp.nstr(kap,40),
                             'x4_coefficient':None if c4 is None else mp.nstr(c4,40),
                             'kernels':kernels})
        # Independently solve equal-factor benchmarks through positive gamma kernels.
        nodes=[]
        for n in (2,3):
            def ph(x):
                return 2*gamma_kernel(3*x,mp.mpf(1)/n,n)-gamma_kernel(4*x,mp.mpf(1)/n,n)-gamma_kernel(2*x,mp.mpf(1)/n,n)
            lo,hi=mp.mpf('.1'),mp.mpf('1')
            for _ in range(180):
                mid=(lo+hi)/2
                if ph(mid)>0:lo=mid
                else:hi=mid
            root=(lo+hi)/2
            req(abs(ph(root))<mp.mpf('1e-50'),'independent gamma node')
            nodes.append(mp.nstr(root,45))
        margin=[]
        for eta in ('1/20','1/10','1/6','1/3'):
            e=number(eta)
            aa=[str(Fraction(1)-2*Fraction(eta)),eta,eta]
            k0,kp,c4=positive_moments(aa)
            small=mp.sqrt((mp.sqrt(3)/8)/(220*c4))
            margin.append({'eta':eta,'kappa_upper':mp.nstr(kp,40),
                           'phase_positive_up_to':mp.nstr(small,35)})
        out={'base_sha':BASE_SHA,'coefficient_checks':structural,'positive_integral_controls':controls,
             'independent_equal_factor_nodes':nodes,'robustness_margins':margin,
             'full_gravity_certified':False,'all_implemented_assertions_passed':True,
             'environment':{'python':platform.python_version(),'mpmath':mp.__version__,
                            'sympy':sp.__version__,'working_dps':60},
             'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
        if evidence is not None:
            data=json.loads(evidence.read_text(encoding='utf-8'))
            req(data['base_sha']==BASE_SHA,'base mismatch')
            forward=Path(__file__).with_name('relational_qg_r5_inverse_design.py')
            req(data['source_sha256']==hashlib.sha256(forward.read_bytes()).hexdigest(),'stale forward evidence')
            req(data['shared_results']['full_consistent_gravity'] is False,'physical overclaim')
            req(data['shared_results']['nonlinear_stability']=='not_tested','nonlinear overclaim')
            req(data['certificate']['coefficient_region_is_not_all_positive_cubic_kernels'] is True,
                'design class enlarged without proof')
            req(data['certificate']['curvature_scalar_coefficient_in_R3_ansatz']=='1/2',
                'incorrect scalar/TT coefficient')
            req(len(data['selected_models'])==len(controls),'missing numerical controls')
            for i,(ctl,fwd) in enumerate(zip(controls,data['selected_models'])):
                req([Fraction(a) for a in ctl['alpha']]==[Fraction(a) for a in fwd['alpha']],
                    'model factors mismatch')
                aa=[Fraction(v) for v in ctl['alpha']]
                expected_b=aa[0]*aa[1]+aa[0]*aa[2]+aa[1]*aa[2]
                req(Fraction(fwd['b'])==expected_b and Fraction(fwd['c'])==aa[0]*aa[1]*aa[2],
                    'coefficient/factor mismatch')
                for key in ('kernel_center','kappa'):
                    req(abs(mp.mpf(ctl[key])-mp.mpf(fwd[key]))<mp.mpf('1e-35'),
                        'positive integral mismatch: '+key)
                for k in ctl['kernels']:
                    target=next(q for q in fwd['rows'] if q['x']==k['x'])
                    req(abs(mp.mpf(k['kernel'])-mp.mpf(target['kernel']))<mp.mpf('1e-17'),
                        'independent kernel mismatch')
                node=mp.mpf(fwd['bracketed_phase_node'])
                if i<2:
                    req(abs(node-mp.mpf(nodes[i]))<mp.mpf('1e-35'),'independent node mismatch')
                else:
                    phase_res=2*positive_kernel(3*node,ctl['alpha'],80)-positive_kernel(4*node,ctl['alpha'],80)-positive_kernel(2*node,ctl['alpha'],80)
                    req(abs(phase_res)<mp.mpf('1e-17'),'independent mixture node mismatch')
                # In particular reject a fabricated uniqueness proof.
                req(fwd['phase_node_unique']=='not_proved','uniqueness overclaim')
            for a,b in zip(margin,data['robustness_margins']):
                req(abs(mp.mpf(a['kappa_upper'])-mp.mpf(b['kappa_interval'][1]))<mp.mpf('1e-30'),
                    'robust upper bound mismatch')
                req(abs(mp.mpf(a['phase_positive_up_to'])-mp.mpf(b['certified_root_exclusion_below']))<mp.mpf('1e-30'),
                    'phase exclusion mismatch')
            out['evidence_sha256']=hashlib.sha256(evidence.read_bytes()).hexdigest()
        return out


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--evidence',type=Path)
    p.add_argument('--output',type=Path)
    a=p.parse_args()
    data=run(a.evidence)
    text=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(text,encoding='utf-8')
        print(json.dumps({'verified':True,'scope':'fixed spatial family only','output':str(a.output)}))
    else:
        print(text)


if __name__=='__main__':
    main()
