#!/usr/bin/env python3
"""Direct quadratic-in-field test of the R3_2 nonlinear Hamiltonian constraint.
Time-symmetric Gaussian rest density with sigma=ell=1, zeta=epsilon*f+
O(epsilon^2). The full spatial potential (not a pair-force insertion) gives
A Delta zeta2=S[f]/4. Integrating S extracts its asymptotic ADM mass coefficient.
This checks the self-source through second order, not a full nonlinear solve.
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


def require(ok,msg):
    if not ok:raise AssertionError(msg)


def symbolic_source():
    r=sp.symbols('r',positive=True)
    f=sp.Function('f')(r)
    D=lambda x:sp.diff(x,r,2)+2*sp.diff(x,r)/r
    L=lambda x:-D(x)
    dL=lambda x:2*f*D(x)-sp.diff(f,r)*sp.diff(x,r)
    A=lambda x:x+L(x)+L(L(x))/4
    R1=-4*D(f)
    R2=8*f*D(f)-2*sp.diff(f,r)**2
    ric=lambda x:(-2*sp.diff(x,r,2)-2*sp.diff(x,r)/r,-sp.diff(x,r,2)-3*sp.diff(x,r)/r)
    rr,rt=ric(f);lr,lt=ric(L(f))
    ricBric=rr*(rr+lr/4)+2*rt*(rt+lt/4)
    S=sp.expand(A(R2)+dL(R1)+(L(dL(R1))+dL(L(R1)))/4-ricBric+R1*(R1+L(R1)/4)/2+3*f*A(R1))
    jets=sp.symbols('f0:7')
    J=sp.expand(S.subs({sp.diff(f,r,j):jets[j] for j in range(6,-1,-1)}))
    # Independent implementation below is compared exactly as a polynomial.
    require(sp.expand(J-source_formula(r,*jets))==0,'nonlinear jet transcription')
    far=sp.simplify(S.subs({sp.diff(f,r,j):sp.diff(1/r,r,j) for j in range(6,-1,-1)}))
    require(sp.simplify(far-2*(-r**4+9*r*r-90)/r**8)==0,'asymptotic nonlinear source')
    return {'source_jet_polynomial':str(J),'far_source':str(far),
            'equation':'A_2 Delta zeta_2 = S[f]/4; coefficient(zeta_2~1/r)=-integral r^2 S dr/4'}


def source_formula(r,f0,f1,f2,f3,f4,f5,f6):
    return (-8*f0*f1/r-4*f0*f2-16*f0*f3/r-4*f0*f4+18*f0*f5/r+3*f0*f6
            -2*f1*f1+2*f1*f1/r**2+3*f1*f1/r**4-36*f1*f2/r-6*f1*f2/r**3
            -8*f1*f3+5*f1*f3/(2*r*r)+101*f1*f4/(2*r)+9*f1*f5
            -2*f2*f2+3*f2*f2/r**2+115*f2*f3/(2*r)+19*f2*f4/2+4*f3*f3)


def first_order_profile(r):
    root2=mp.sqrt(2)
    C=mp.erf(r/root2)/r if r else mp.sqrt(2/mp.pi)
    return C-mp.e/(2*root2)*(mp.exp(-root2*r)*mp.erfc(1-r/root2)+mp.exp(root2*r)*mp.erfc(1+r/root2))


def integrate_source(n,rmax):
    nodes,weights=mp.gauss_quadrature(n,'legendre')
    acc=mp.mpf(0)
    probes=list(map(mp.mpf,(0,1,5,10)))
    profile=[mp.mpf(0) for _ in probes]
    kap=mp.sqrt(2)
    def green(r,s):
        if not r:
            ker=(1-mp.exp(-kap*s)*(1+kap*s/2))/s
            return -s*s*ker/4
        primitive=lambda u:u+mp.exp(-kap*u)*(u/2+3/(2*kap))
        return -s*(primitive(r+s)-primitive(abs(r-s)))/(8*r)
    for node,weight in zip(nodes,weights):
        r=rmax*(node+1)/2
        jets=[mp.diff(first_order_profile,r,j) for j in range(7)]
        source=source_formula(r,*jets)
        acc+=weight*rmax/2*r*r*source/4
        for j,probe in enumerate(probes):
            profile[j]+=weight*rmax/2*source*green(probe,r)
    # Analytic asymptotic contribution for f=1/r; residual Yukawa tail is
    # checked by changing rmax, not silently treated as an exact tail.
    tail=-1/(2*rmax)+3/(2*rmax**3)-9/rmax**5
    for j,probe in enumerate(probes):
        profile[j]+=mp.quad(lambda s:2*(-s**4+9*s*s-90)/s**8*green(probe,s),[rmax,mp.inf])
    return acc+tail, {str(int(r)):mp.nstr(v,36) for r,v in zip(probes,profile)}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    with mp.workdps(55):
        print("deriving nonlinear source", flush=True)
        sy=symbolic_source()
        expected=mp.quad(lambda k:mp.exp(-k*k)/(1+k*k/2)**2,[0,1,mp.inf])/mp.pi
        print("pair integral computed", flush=True)
        rows=[]
        for n,rmax in ((32,30),(64,30),(64,32)):
            value,profile=integrate_source(n,mp.mpf(rmax))
            print("quadrature", n, rmax, mp.nstr(value,20), flush=True)
            rows.append({'quadrature_nodes':n,'rmax':rmax,'mass_deficit_coefficient':mp.nstr(value,40),
                         'difference_from_pair_energy':mp.nstr(abs(value-expected),20),
                         'zeta2_profile_at_r_over_ell':profile})
        require(abs(mp.mpf(rows[-1]['mass_deficit_coefficient'])-expected)<mp.mpf('1e-16'),'nonlinear ADM mass mismatch')
        require(abs(mp.mpf(rows[1]['mass_deficit_coefficient'])-mp.mpf(rows[2]['mass_deficit_coefficient']))<mp.mpf('1e-16'),'tail/refinement mismatch')
        out={'base_sha':BASE_SHA,'symbolic':sy,'runs':rows,'independent_pair_binding':mp.nstr(expected,42),
             'all_implemented_assertions_passed':True,'full_nonlinear_solution_constructed':False,
             'environment':{'python':platform.python_version(),'mpmath':mp.__version__,'sympy':sp.__version__},
             'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'ADM_binding':rows[-1]['mass_deficit_coefficient'],
                      'error':rows[-1]['difference_from_pair_energy'],'full_nonlinear_solution':False}))


if __name__=='__main__':main()
