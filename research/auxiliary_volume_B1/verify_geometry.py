#!/usr/bin/env python3
"""Independent metric curvature check; does not import check_candidate.py.
Checks the mu=1 isotropic stiff metric directly from Christoffel/Riemann.
This is a geometry check, not a quantum-gravity certification.
"""
from pathlib import Path
import hashlib
import json
import sympy as s

def main():
    t=s.symbols('t',real=True)
    a=(1+t*t)**s.Rational(1,6)
    metric=s.diag(-1,a*a,a*a,a*a)
    inv=metric.inv()
    derivative=lambda f,i: s.diff(f,t) if i==0 else s.Integer(0)
    G={}
    for i in range(4):
        for j in range(4):
            for k in range(4):
                val=s.simplify(sum(inv[i,l]*(derivative(metric[l,k],j)+derivative(metric[l,j],k)-derivative(metric[j,k],l)) for l in range(4))/2)
                if val!=0:G[i,j,k]=val
    conn=lambda i,j,k:G.get((i,j,k),s.Integer(0))
    R={}
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    val=s.simplify(derivative(conn(i,l,j),k)-derivative(conn(i,k,j),l)+sum(conn(i,k,m)*conn(m,l,j)-conn(i,l,m)*conn(m,k,j) for m in range(4)))
                    if val!=0:R[i,j,k,l]=val
    rr=lambda i,j,k,l:R.get((i,j,k,l),s.Integer(0))
    scalar=s.factor(sum(inv[j,j]*rr(i,j,i,j) for i in range(4) for j in range(4)))
    kr=s.factor(sum(metric[i,i]**2*inv[i,i]*inv[j,j]*inv[k,k]*inv[l,l]*value**2 for (i,j,k,l),value in R.items()))
    assert s.simplify(scalar-2*(3-t*t)/(3*(1+t*t)**2))==0
    assert s.simplify(kr-4*(9-12*t*t+5*t**4)/(27*(1+t*t)**4))==0
    # Upper bounds are polynomial nonnegativity, not numerical sampling.
    y=s.symbols('y',nonnegative=True)
    assert s.Poly(s.cancel((3*(1+y)**2)*(2-2*(3-y)/(3*(1+y)**2))),y).all_coeffs()==[6,14,0]
    k_margin=s.factor((s.Rational(4,3)-4*(9-12*y+5*y*y)/(27*(1+y)**4))*27*(1+y)**4/4)
    assert all(co>=0 for co in s.Poly(k_margin,y).all_coeffs())
    here=Path(__file__).resolve().parent
    data=json.loads((here/'results.json').read_text())
    assert data['source_sha256']==hashlib.sha256((here/'check_candidate.py').read_bytes()).hexdigest()
    assert data['full_quantum_gravity_claim'] is False
    assert data['generic_singularity_resolution_claim'] is False
    out={'verified':True,'method':'direct 4D Christoffel and Riemann contractions',
         'R_over_mu2':str(scalar),'K_over_mu4':str(kr),
         'isotropic_R_upper':'2 mu^2','isotropic_K_upper':'4 mu^4/3',
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'forward_evidence_sha256':hashlib.sha256((here/'results.json').read_bytes()).hexdigest(),
         'full_theory_health_claim':False}
    (here/'verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':
    main()
