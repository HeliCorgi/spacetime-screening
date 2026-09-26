#!/usr/bin/env python3
"""Independent verifier for the CBSSL v9 toy state-selection law."""
from __future__ import annotations
import argparse, hashlib, json, platform
from pathlib import Path
import sympy as sp
import mpmath as mp

BASE_SHA="fbf98de97fe11b9dea40e7d195227ea4a088b5a5"

def req(x,m):
    if not x: raise AssertionError(m)

def exact_v7():
    a=sp.Rational(1,2); c=sp.pi/8; vx=sp.Rational(1,2); vp=sp.Rational(5,6)
    mean=sp.simplify(c/(1-a))
    d=sp.simplify(sp.exp(-2*vx)*sp.sin(2*mean))
    E=sp.simplify((vx+vp-1+mean**2)/2)
    req(mean==sp.pi/4,"mean"); req(d==sp.exp(-1),"D"); req(E==sp.Rational(1,6)+sp.pi**2/32,"energy")
    return {"mean":"pi/4","D":"exp(-1)","energy_excess":str(E)}

def nonaffinity():
    a=sp.Rational(1,2);c=sp.pi/8;q=sp.Rational(1,2)
    mu=c/(1-a)
    va=sp.Rational(1,2)+4*q*(1-q)*mu**2
    vm=((1-a*a)/2+4*q*(1-q)*c**2)/(1-a*a)
    gap=sp.simplify(va-vm)
    req(gap==sp.pi**2/24,"gap")
    return {"gap":"pi^2/24","numeric":float(sp.N(gap,18))}

def relative_entropy_tie():
    p=sp.symbols('p',positive=True)
    D=p*sp.log(3*p/2)+(1-p)*sp.log(3*(1-p))
    req(sp.simplify(sp.diff(D,p).subs(p,sp.Rational(2,3)))==0,"tie derivative")
    req(sp.simplify(sp.diff(D,p,2).subs(p,sp.Rational(2,3)))>0,"tie second")
    return {"selected_p":"2/3"}

def remote_control():
    bell=sp.Matrix([1,0,0,1])/sp.sqrt(2);rho=bell*bell.T
    H=sp.Matrix([[1,1],[1,-1]])/sp.sqrt(2);U=sp.kronecker_product(sp.eye(2),H)
    out=U*rho*U.T
    ptr=lambda rr:sp.Matrix(2,2,lambda i,j:sum(rr[2*i+k,2*j+k] for k in range(2)))
    req(ptr(rho)==sp.eye(2)/2 and ptr(out)==sp.eye(2)/2,"remote reduced state")
    return {"remote_unitary_preserves_loop_reduced_state":True}

def evidence(path):
    d=json.loads(path.read_text(encoding='utf-8'))
    src=Path(__file__).with_name('chronology_backreaction_selection_v9.py')
    req(d['base_sha']==BASE_SHA,'base')
    req(d['code_sha256']==hashlib.sha256(src.read_bytes()).hexdigest(),'hash')
    req(d['classification']=={'A':0,'B':1,'C':0},'classification')
    law=d['law']; req(law['status']=='B','status')
    req(law['claim_type'].startswith('new toy physical law'),'claim scope')
    v=law['v7_positive_channel']; req(v['D_past']=='exp(-1)','D record')
    req(abs(v['numeric']['D_past']-float(mp.e**-1))<1e-15,'D numeric')
    req(d['controls']['chronology_protection']['admissible_fixed_point_exists'] is False,'protection')
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser();p.add_argument('--evidence',type=Path);p.add_argument('--output',type=Path);a=p.parse_args()
    out={"verified":True,"exact_v7":exact_v7(),"nonaffinity":nonaffinity(),"tie":relative_entropy_tie(),"remote":remote_control(),"environment":{"python":platform.python_version(),"sympy":sp.__version__,"mpmath":mp.__version__},"verifier_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if a.evidence: out['evidence_sha256']=evidence(a.evidence)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding='utf-8')
    print(json.dumps({"verified":True,"classification":"B","D_past":float(mp.e**-1),"law":"CBSSL"},ensure_ascii=False))
if __name__=='__main__':main()
