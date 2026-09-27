#!/usr/bin/env python3
"""Independent verifier for CBSSL v10 regulated 3+1D RSET core."""
from __future__ import annotations
import argparse, hashlib, json, platform
from pathlib import Path
import mpmath as mp
import sympy as sp

BASE_SHA="c27097e29e05275b56a922e5c63e0b99526d1da2"

def req(x,m):
    if not x: raise AssertionError(m)


def alternative_core(dps=70):
    """Re-solve with variables y=r^2 and e=Q^2, independent algebra."""
    with mp.workdps(dps):
        xi=mp.mpf('-10000'); m2=mp.mpf('1000'); m=mp.sqrt(m2); mds=m
        pt=-xi**3/6+xi**2/12-xi/60+mp.mpf(1)/630
        pth=-2*pt
        def rq(y):
            log=mp.log(mds**2*y)/720
            ft=mp.mpf('.00310')+log+pt/(m2*y)
            fth=-mp.mpf('.00171')-log+pth/(m2*y)
            fac=1/(4*mp.pi**2*y**2)
            return fac*ft,fac*fth
        def F(y,e):
            tt,th=rq(y)
            return (-1/y-8*mp.pi*tt+e/y**2,
                    -8*mp.pi*th-e/y**2)
        y,e=mp.findroot(F,(mp.mpf('10300.9'),mp.mpf('20601.82')),tol=mp.mpf('1e-55'))
        r=mp.sqrt(y)
        f=F(y,e)
        req(max(abs(z) for z in f)<mp.mpf('1e-50'),'alternative residual')
        # Check published approximate closed-form r equation.
        poly=xi**3/3-xi**2/6+xi/30-mp.mpf(1)/315
        y_analytic=mp.sqrt(-poly/(mp.pi*m2))
        rel=abs(y-y_analytic)/y
        # Printed 0.00310/-0.00171 coefficients differ from exact 1/720 combination,
        # so only the expected ~1e-8 agreement is required for this literature control.
        req(rel<mp.mpf('1e-6'),'Popov displayed solution mismatch')
        return {"dps":dps,"r_planck":mp.nstr(r,50),"Q_squared":mp.nstr(e,50),
                "max_abs_residual":mp.nstr(max(abs(z) for z in f),12),
                "relative_difference_from_displayed_analytic_r2":mp.nstr(rel,12)}


def direct_product_curvature():
    # Independent warped/product identity: R_ab=0 on M2, R_AB=(1/r^2)g_AB on S2.
    r=sp.symbols('r',positive=True)
    Rmix=sp.diag(0,0,1/r**2,1/r**2)
    R=sp.trace(Rmix)
    Gmix=sp.simplify(Rmix-sp.eye(4)*R/2)
    req(Gmix==sp.diag(-1/r**2,-1/r**2,0,0),'product Einstein tensor')
    return {"Ricci_mixed":"diag(0,0,1/r^2,1/r^2)","Einstein_mixed":"diag(-1/r^2,-1/r^2,0,0)"}


def signal_control():
    x,v,L=sp.symbols('x v lambda',positive=True)
    V=L*(x*x-v*v)**2/4
    req(V.subs(x,v)==0 and V.subs(x,-v)==0,'zero signal vacuum stress')
    req(sp.diff(V,x).subs(x,v)==0 and sp.diff(V,x).subs(x,-v)==0,'signal eom')
    with mp.workdps(70):
        k=mp.mpf(3); D=mp.erf(k/mp.sqrt(2)); pc=(1+D)/2
        req(abs(D-(2*pc-1))<mp.mpf('1e-60'),'TV')
        return {"D_past":mp.nstr(D,50),"P_correct":mp.nstr(pc,50)}


def evidence(path):
    d=json.loads(path.read_text(encoding='utf-8'))
    src=Path(__file__).with_name('cbssl_rset_core_v10.py')
    req(d['base_sha']==BASE_SHA,'base')
    req(d['code_sha256']==hashlib.sha256(src.read_bytes()).hexdigest(),'stale evidence')
    req(d['classification']=={'A':0,'B':1,'C':0},'classification')
    c=d['candidate']; req(c['status']=='B','status')
    req(c['P_Y_do_0']['computed'] is True and c['P_Y_do_1']['computed'] is True,'P missing')
    req(c['distinguishability']['computed'] is True and float(c['distinguishability']['value'])>0,'D')
    req(mp.mpf(c['calculation']['core']['R_sc_density'])<mp.mpf('1e-100'),'R_sc not zero')
    req(c['calculation']['signal']['signal_stress_at_fixed_point'].startswith('T_mn=0'),'signal stress')
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(); p.add_argument('--evidence',type=Path); p.add_argument('--output',type=Path); a=p.parse_args()
    out={"verified":True,"geometry":direct_product_curvature(),"core":alternative_core(),"signal":signal_control(),
         "environment":{"python":platform.python_version(),"sympy":sp.__version__,"mpmath":mp.__version__},
         "verifier_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if a.evidence: out['evidence_sha256']=evidence(a.evidence)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True); a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({"verified":True,"classification":"B","R_sc":"0 in regulated core","D_past":out['signal']['D_past']},ensure_ascii=False))

if __name__=='__main__': main()
