#!/usr/bin/env python3
"""Independent algebra verifier for v8 stress scaling and Deutsch non-affinity."""
from __future__ import annotations
import argparse, json, hashlib
from pathlib import Path
import sympy as sp
import mpmath as mp

BASE_SHA="6a408e42abef6355699d276c1bc45547198954ae"

def req(x,m):
    if not x: raise AssertionError(m)

def exact():
    a=sp.Rational(1,2); c=sp.pi/8; q=sp.Rational(1,2)
    mu=c/(1-a)
    noise=(1-a*a)/2
    # Affine mixture of fixed states
    va=sp.Rational(1,2)+4*q*(1-q)*mu**2
    # Fixed point of convexly mixed operations
    vm=sp.simplify((noise+4*q*(1-q)*c**2)/(1-a*a))
    gap=sp.simplify(va-vm)
    req(mu==sp.pi/4,"mean")
    req(va==sp.Rational(1,2)+sp.pi**2/16,"va")
    req(vm==sp.Rational(1,2)+sp.pi**2/48,"vm")
    req(gap==sp.pi**2/24,"gap")
    # signal oscillator energy from v7
    E=sp.simplify((sp.Rational(1,2)+sp.Rational(5,6)+sp.pi**2/16)/2)
    req(E==sp.Rational(2,3)+sp.pi**2/32,"energy")
    return {"gap":"pi^2/24","gap_numeric":float(sp.N(gap,20)),
            "v7_energy":"2/3+pi^2/32"}

def scale():
    with mp.workdps(50):
        G=mp.mpf("6.67430e-11"); c=mp.mpf("299792458"); hb=mp.mpf("1.054571817e-34")
        lp=mp.sqrt(hb*G/c**3)
        nc=1/(8*mp.pi*lp**2)
        req(mp.mpf("1.52e68")<nc<mp.mpf("1.53e68"),"scale")
        return {"lp":mp.nstr(lp,20),"N_times_C":mp.nstr(nc,20)}

def evidence(path):
    d=json.loads(path.read_text())
    src=Path(__file__).with_name("stress_deutsch_qft_v8.py")
    req(d["base_sha"]==BASE_SHA,"base")
    req(d["code_sha256"]==hashlib.sha256(src.read_bytes()).hexdigest(),"hash")
    req(d["classification"]=={"A":0,"B":5,"C":1},"class")
    q=d["deutsch_nonaffinity"]
    req(q["nonaffinity_variance_gap"]=="pi^2/24","record gap")
    req(any(x["id"]=="deutsch-from-standard-qft" and x["status"]=="C" for x in d["candidates"]),"missing C")
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    p=argparse.ArgumentParser();p.add_argument("--evidence",type=Path);p.add_argument("--output",type=Path);a=p.parse_args()
    out={"verified":True,"exact":exact(),"scale":scale()}
    if a.evidence: out["evidence_sha256"]=evidence(a.evidence)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(out,indent=2)+"\n")
    print(json.dumps({"verified":True,"Deutsch_standard_QFT":"C","gap":out["exact"]["gap_numeric"]}))
if __name__=="__main__": main()
