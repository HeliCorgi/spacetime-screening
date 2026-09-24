"""Separate RN candidate verification. Does not import the model generator.

Checks a different rational stability formula, reconstructs the conserved EOS
potential, recomputes the full 4D Ricci tensor, bounds a polynomial by Bernstein
coefficients, and integrates the optical path. Same-author cross-check,
NOT independent scientific peer review. No extrapolation to a quantum source.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from math import comb
from pathlib import Path
import platform
import mpmath as mp
import sympy as sp
from architecture_search import load_json, validate_bundle, sha256, write_json, require

ROOT=Path(__file__).resolve().parents[1]


def ricci_check():
    t,r,theta,phi=sp.symbols('t r theta phi',real=True)
    M,Q=sp.symbols('M Q',real=True)
    coords=[t,r,theta,phi];f=1-2*M/r+Q**2/r**2
    g=sp.diag(-f,1/f,r*r,r*r*sp.sin(theta)**2); inv=g.inv()
    gamma={}
    for a in range(4):
        for b in range(4):
            for c in range(4):
                gamma[a,b,c]=sp.simplify(sum(inv[a,d]*(sp.diff(g[d,c],coords[b])+sp.diff(g[d,b],coords[c])-sp.diff(g[b,c],coords[d]))/2 for d in range(4)))
    ric=sp.zeros(4)
    for a in range(4):
        for b in range(4):
            ric[a,b]=sp.simplify(sum(sp.diff(gamma[c,a,b],coords[c])-sp.diff(gamma[c,a,c],coords[b])+sum(gamma[c,a,b]*gamma[d,c,d]-gamma[d,a,c]*gamma[c,b,d] for d in range(4)) for c in range(4)))
    scalar=sp.simplify(sp.trace(inv*ric));assert scalar==0
    einstein=sp.simplify(inv*ric)
    expected=sp.diag(-1,-1,1,1)*Q**2/r**4
    assert all(sp.simplify(x)==0 for x in einstein-expected)
    return 'all 16 mixed Einstein components recomputed from 4D metric and Christoffel symbols'


def bernstein_box(cert):
    m,z,e=sp.symbols('m z e')
    # Eiroa Eq. (37): Delta=-Vpp/2, with a0=1.
    numerator=-2*((1-m)**3+m*(m*m-z))-4*e*(1-3*m+2*z)*(1-2*m+z)
    u,v,w=sp.symbols('u v w'); variables=[u,v,w]
    lo=[sp.Rational(cert[k][0]) for k in ('mu','z','eta')]
    hi=[sp.Rational(cert[k][1]) for k in ('mu','z','eta')]
    transformed=sp.Poly(sp.expand(numerator.subs(dict(zip((m,z,e),(lo[i]+(hi[i]-lo[i])*variables[i] for i in range(3)))))),*variables)
    degrees=transformed.degree_list();coefficients=[]
    for i in range(degrees[0]+1):
        for j in range(degrees[1]+1):
            for k in range(degrees[2]+1):
                value=sp.Rational(0)
                for powers,c in transformed.terms():
                    if all(a<=b for a,b in zip(powers,(i,j,k))):
                        value+=c*sp.prod(sp.Rational(comb(b,a),comb(n,a)) for a,b,n in zip(powers,(i,j,k),degrees))
                coefficients.append(value)
    lower=min(coefficients);assert lower>0
    fmin=1-2*hi[0]+lo[1];fmax=1-2*lo[0]+hi[1]
    assert fmin>0 and lo[0]**2-hi[1]>0 and hi[0]<1
    return {'method':'independent Bernstein convex-hull bound of f*a0^2*Vpp',
            'positive_coefficients':len(coefficients),'numerator_lower':str(lower),
            'a2_Vpp_lower':str(lower/fmax)}


def verify_sweep(rows):
    stable=0;invalid=0
    for row in rows:
        m,z,e=map(F,(row['mu'],row['z'],row['eta']))
        outside=(z>=0 and m<1 and (1-m)**2>m*m-z)
        assert outside==row['outside_outer_horizon']
        if not outside:
            assert row['a2_Vpp'] is None and row['radially_stable'] is None
            invalid+=1;continue
        delta=((1-m)**3+m*(m*m-z))/(1-2*m+z)+2*(1-3*m+2*z)*e
        h=-2*delta
        assert h==F(row['a2_Vpp']) and (h>0)==row['radially_stable']
        stable+=h>0
    return {'checked_points':len(rows),'stable':stable,'invalid_exterior':invalid}


def potential_checks(dps):
    results=[]
    with mp.workdps(dps):
        for m,z,e in [('0.9','0.8099','0.75'),('0.9','0.81','0.75'),('0.8','0.64','1'),('0.6','0.36','0.5'),('0.3','0','0.5')]:
            m,z,e=map(mp.mpf,(m,z,e));f=lambda a:1-2*m/a+z/a**2
            sig0=-mp.sqrt(f(1))/(2*mp.pi)
            p0=(1-m)/(4*mp.pi*mp.sqrt(f(1)))
            b=p0-e*sig0
            # Integrate d(sigma*a^2)+p*d(a^2)=0; not the forward Hessian.
            density=lambda a:(sig0+b/(1+e))*a**(-2*(1+e))-b/(1+e)
            pot=lambda a:f(a)-(2*mp.pi*a*density(a))**2
            expected=-2*(((1-m)**3+m*(m*m-z))/f(1)+2*(1-3*m+2*z)*e)
            assert abs(pot(1))<mp.mpf('1e-42')
            assert abs(mp.diff(pot,mp.mpf(1)))<mp.mpf('1e-42')
            numerical=mp.diff(pot,mp.mpf(1),2)
            assert abs(numerical-expected)<mp.mpf('1e-42')
            # Direct acceleration from Israel pressure provides another check.
            def acceleration(a):
                sig=-mp.sqrt(f(a))/(2*mp.pi*a)
                p=p0+e*(sig-sig0)
                return 4*mp.pi*p*mp.sqrt(f(a))-f(a)/a-mp.diff(f,a)/2
            assert abs(mp.diff(acceleration,mp.mpf(1))+expected/2)<mp.mpf('1e-42')
            results.append(mp.nstr(numerical,42))
    return results


def optics_checks(rows,dps):
    with mp.workdps(dps):
        errors=[]
        for row in rows:
            e=mp.mpf(row['epsilon']);m=1-e
            numeric=2*mp.quad(lambda r:1/(1-m/r)**2,[1,1+e,mp.mpf('1.1'),2])
            expected=mp.mpf(row['optical_time_over_a'])
            err=abs(numeric-expected)/max(1,abs(numeric))
            assert err<mp.mpf('1e-40')
            errors.append(mp.nstr(err,4))
        # Raychaudhuri: integral theta^2/2 on both exterior legs is 4/a.
        a=mp.mpf('1.3')
        integral=2*mp.quad(lambda r:2/r**2,[a,mp.inf])
        anec=-integral/(8*mp.pi)
        assert abs(anec+1/(2*mp.pi*a))<mp.mpf('1e-45')
    return errors


def verify(raw,output):
    bundle=load_json(raw);validate_bundle(bundle,ROOT)
    ids={r['candidate_id'] for r in bundle['candidates']}
    require(ids=={'rn-causal-slope-support','rn-single-seam-offset'},'Unexpected candidate IDs')
    candidates={r['candidate_id']:r for r in bundle['candidates']}
    support=candidates['rn-causal-slope-support'];clock=candidates['rn-single-seam-offset']
    require(support['status']=='B' and clock['status']=='C','Unreviewed classification')
    calc=support['calculation'];counts=verify_sweep(calc['trials'])
    require(counts['stable']==calc['stable'],'Stable count mismatch')
    box=bernstein_box(calc['certificate'])
    tensor=ricci_check()
    potential={str(p):potential_checks(p) for p in (50,80)}
    optics={str(p):optics_checks(calc['near_extremal'],p) for p in (50,80)}
    for r in clock['calculation']['trials']:
        require(F(r['same_clock_roundtrip'])==F(14,3)+F(r['wait'])>0,'Offset treated as a causal loop')
        require(F(r['forward_leg_coordinate_delta'])+F(r['return_leg_coordinate_delta'])==F(14,3),'Seam reversal mismatch')
    # No saved response probability may be smuggled in from forward scattering.
    for r in bundle['candidates']:
        require(not r['P_Y_do_0']['computed'] and not r['P_Y_do_1']['computed'],'Past probability not constructed')
    record={'input_sha256':sha256(raw),'verification_program_sha256':sha256(Path(__file__)),
            'python':platform.python_version(),'external_peer_review':'not_performed',
            'candidates':{cid:{'software_check':'passed','method':'separate formula and/or reconstructed potential, geometry and clock audit'} for cid in ids},
            'sweep':counts,'certificate':box,'tensor':tensor,'potential_50_80':potential,'optics_errors':optics}
    write_json(output,record)
    print(json.dumps({'verified':sorted(ids),'sweep':counts,'Bernstein_bound':box},ensure_ascii=False))


if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--records',type=Path,required=True);parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();verify(args.records,args.output)
