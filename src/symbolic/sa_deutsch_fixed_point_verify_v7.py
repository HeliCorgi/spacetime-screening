#!/usr/bin/env python3
"""Separate algebraic verifier for SA v7 Deutsch fixed-point toy."""
from __future__ import annotations
import argparse, hashlib, json, platform
from pathlib import Path
import mpmath as mp
import sympy as sp

BASE_SHA="fbc4e2bf567e00e021f94216f470198f5ce41880"

def require(ok,msg):
    if not ok: raise AssertionError(msg)

def verify_exact():
    a=sp.Rational(1,2); c=sp.pi/8; lam=sp.Integer(1); vx=sp.Rational(1,2)
    m=sp.simplify(c/(1-a)); d=sp.simplify(sp.exp(-2*lam**2*vx)*sp.sin(2*lam*m))
    require(m==sp.pi/4 and d==sp.exp(-1),"fixed signal")
    K=sp.Matrix([[(1+d)/2,(1-d)/2],[(1-d)/2,(1+d)/2]])
    X=sp.Matrix([[0,1],[1,0]]); u=sp.Matrix([sp.Rational(1,2)]*2)
    require(K*u==u and K*X*u==u,"copy/NOT fixed points")
    require(sp.simplify(sp.Rational(1,2)*sum(abs(x) for x in (d,-d)))==d,"TV")
    # Functional-equation moment checks for the exact fixed-point characteristic function.
    # chi(kx,0)=exp(i*m*kx-kx^2/4), so <X>=m and Var X=1/2.
    k=sp.symbols('k',real=True)
    chi=sp.exp(sp.I*m*k-k**2/4)
    mean=sp.simplify(sp.diff(chi,k).subs(k,0)/sp.I)
    second=sp.simplify(-sp.diff(chi,k,2).subs(k,0))
    require(mean==m and sp.simplify(second-mean**2)==sp.Rational(1,2),"characteristic moments")
    return {"mean":str(mean),"V_X":"1/2","D_past":"exp(-1)","copy_record_fixed":"(1/2,1/2)","not_record_fixed":"(1/2,1/2)"}

def evidence(path):
    data=json.loads(path.read_text(encoding='utf-8'))
    src=Path(__file__).with_name('sa_deutsch_fixed_point_v7.py')
    require(data['base_sha']==BASE_SHA,'wrong base')
    require(data['code_sha256']==hashlib.sha256(src.read_bytes()).hexdigest(),'stale evidence')
    r=data['candidate']
    require(r['status']=='B','classification changed')
    require(r['P_Y_do_0']['computed'] is True and r['P_Y_do_1']['computed'] is True,'probabilities not computed')
    require(r['distinguishability']['computed'] is True,'D not computed')
    require(abs(float(r['distinguishability']['numeric'])-float(mp.e**-1))<1e-14,'D mismatch')
    require(r['sender_intervention']['uses_postselection'] is False,'postselection introduced')
    require(len(r['unresolved_assumptions'])>0,'B lacks unresolved assumptions')
    runs=r['calculation']['fock_runs']; require([x['cutoff'] for x in runs]==[10,14],'Fock cutoffs changed')
    require(abs(float(runs[-1]['rows']['copy']['P_plus'])-.5)<1e-12,'copy quantum fixed point')
    require(abs(float(runs[-1]['rows']['not']['P_plus'])-.5)<1e-12,'NOT quantum fixed point')
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--evidence',type=Path);p.add_argument('--output',type=Path);a=p.parse_args()
    out={"verified":True,"environment":{"python":platform.python_version(),"sympy":sp.__version__,"mpmath":mp.__version__},"exact":verify_exact(),"verifier_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if a.evidence: out['evidence_sha256']=evidence(a.evidence)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding='utf-8')
    print(json.dumps({"verified":True,"D_past":float(mp.e**-1),"classification":"B"},ensure_ascii=False))
if __name__=='__main__': main()
