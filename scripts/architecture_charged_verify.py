"""Separate calculation; never imports architecture_charged_models.

Same-author alternative implementation, NOT independent scientific peer review.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import mpmath as mp
import sympy as s


def tensors(coords, g):
    n=len(coords); inv=g.inv()
    C=[[[s.simplify(sum(inv[i,k]*(s.diff(g[k,j],coords[l])+s.diff(g[k,l],coords[j])-s.diff(g[j,l],coords[k])) for k in range(n))/2)
          for l in range(n)] for j in range(n)] for i in range(n)]
    ric=s.Matrix(n,n,lambda i,j:s.simplify(sum(s.diff(C[k][i][j],coords[k])-s.diff(C[k][i][k],coords[j])
            +sum(C[k][i][j]*C[l][k][l]-C[l][i][k]*C[k][j][l] for l in range(n)) for k in range(n))))
    R=s.simplify(s.trace(inv*ric))
    return C,ric,R,s.simplify(ric-g*R/2)


def geometry_checks():
    t,x,y,z=s.symbols('t x y z',real=True)
    U=s.Function('U')(x,y,z); g=s.diag(-U**-2,U**2,U**2,U**2)
    C,ric,R,E=tensors((t,x,y,z),g); inv=g.inv(); F=s.zeros(4)
    for i,w in enumerate((x,y,z),1):
        F[i,0]=s.diff(1/U,w);F[0,i]=-F[i,0]
    ff=s.simplify(sum(F[i,j]*(inv*F*inv)[i,j] for i in range(4) for j in range(4)))
    lap=sum(s.diff(U,w,2) for w in (x,y,z))
    residual=s.simplify(E-2*(F*inv*F.T-g*ff/4))
    assert s.simplify(residual-s.diag(-2*lap/U**5,0,0,0))==s.zeros(4)
    assert s.simplify(sum(s.diff(U**2*(inv*F*inv)[i,0],w) for i,w in enumerate((x,y,z),1))-lap)==0
    # Direct four-dimensional curvature of the smooth RN metric.
    r=s.Function('r')(x); f=s.Function('f')(x)
    g=s.diag(-f,1/f,r**2,r**2*s.sin(y)**2)
    C,ric,R,E=tensors((t,x,y,z),g)
    stress=[s.simplify(E[0,0]/f),s.simplify(E[1,1]*f),s.simplify(E[2,2]/r**2)]
    A=s.diff(f,x,2)/2; B=s.diff(f,x)*s.diff(r,x)/(2*r)
    CC=-(f*s.diff(r,x,2)+s.diff(f,x)*s.diff(r,x)/2)/r
    D=(1-f*s.diff(r,x)**2)/r**2
    assert s.simplify(R-(-2*A-4*B+4*CC+2*D))==0
    assert all(s.simplify(q-target)==0 for q,target in zip(stress,(2*CC+D,2*B-D,A+B-CC)))
    Ric2=s.trace(g.inv()*ric*g.inv()*ric)
    assert s.simplify(Ric2-((A+2*B)**2+(-A+2*CC)**2+2*(-B+CC+D)**2))==0
    # Riemann contraction from the connection, independent of sectional formula.
    inv=g.inv(); coords=(t,x,y,z); K=0
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(k+1,4):
                    q=s.simplify(s.diff(C[i][j][l],coords[k])-s.diff(C[i][j][k],coords[l])
                        +sum(C[i][k][m]*C[m][j][l]-C[i][l][m]*C[m][j][k] for m in range(4)))
                    if q!=0: K+=2*g[i,i]*inv[j,j]*inv[k,k]*inv[l,l]*q*q
    assert s.simplify(K-4*(A*A+2*B*B+2*CC*CC+D*D))==0
    # Independent large-x Laurent calculation; no symbolic limit in areal radius.
    a,e,M,Q2,X=s.symbols('a e M Q2 X',positive=True)
    rr=X+a-e+e**2/(2*X)-e**4/(8*X**3)
    ff=s.series(1-2*M/rr+Q2/rr**2,X,s.oo,6).removeO()
    scalar=-s.diff(ff,X,2)-4*(ff*s.diff(rr,X,2)+s.diff(ff,X)*s.diff(rr,X))/rr+2*(1-ff*s.diff(rr,X)**2)/rr**2
    assert s.series(scalar,X,s.oo,5).removeO().expand()==-2*e**2/X**4
    # Derive the separated four-dimensional KG operator, not a 2D field model.
    u=s.Function('u')(x); ell, mass=s.symbols('ell mass', nonnegative=True)
    radial=f/r*s.diff(r**2*f*s.diff(u/r,x),x)-f*(ell*(ell+1)/r**2+mass**2)*u
    potential=f*(ell*(ell+1)/r**2+mass**2+(s.diff(f,x)*s.diff(r,x)+f*s.diff(r,x,2))/r)
    assert s.simplify(radial-(f**2*s.diff(u,x,2)+f*s.diff(f,x)*s.diff(u,x)-potential*u))==0
    # Minimal scalar has a nonnegative spatial potential if f,df/dr,r''>0.
    # This checks a test field only; not a quantum support source.
    return {'MP_bulk_Einstein_Maxwell':'direct 4D tensor identity',
            'RN_stress':'direct 4D connection/Ricci', 'RN_Kretschmann':'direct Riemann contraction',
            'RN_trace_tail':'independent Laurent series','minimal_KG':'full 4D separated operator',
            'independent_researcher_review':False}


def close(value, expected, tolerance='1e-39'):
    with mp.workdps(85):
        v,e=mp.mpf(value),mp.mpf(expected)
        if not (mp.isfinite(v) and mp.isfinite(e)):
            raise ValueError('Nonfinite arithmetic is not agreement')
        if abs(v-e)>mp.mpf(tolerance)*max(abs(v),abs(e),mp.mpf('1e-80')):
            raise ValueError('Independent arithmetic mismatch')


def verify_trial(row):
    with mp.workdps(80):
        kind=row['kind']
        if kind.startswith('RN'):
            a=mp.mpf(1); e=mp.mpf(row['epsilon']);M=mp.mpf('.9');q2=mp.mpf('.8099')
            rr=lambda x:a+mp.sqrt(x*x+e*e)-e
            f=lambda x:1-2*M/rr(x)+q2/rr(x)**2
            if kind=='RN_ANEC':
                # Raychaudhuri: integrate expansion squared, not the generator's r''/r.
                integral=mp.quad(lambda x:mp.diff(rr,x)**2/rr(x)**2,[0,e,mp.mpf('.1'),1,10,mp.inf])
                close(row['ANEC_G1'],-integral/(2*mp.pi));return
            x=mp.mpf(row['x']);r=rr(x);v=mp.diff(rr,x);w=mp.diff(rr,x,2)
            f0=f(x);fx=mp.diff(f,x);fxx=mp.diff(f,x,2)
            # Curvature sections with independently numerically differentiated metric.
            A=fxx/2;B=fx*v/(2*r);C=-(f0*w+fx*v/2)/r;D=(1-f0*v*v)/r**2
            R=-2*A-4*B+4*C+2*D
            vals={'eight_pi_G_rho_extra':2*C+D-q2/r**4,
                  'eight_pi_G_pr_extra':2*B-D+q2/r**4,
                  'eight_pi_G_pt_extra':A+B-C-q2/r**4,'R':R,'r':r,'f':f0,'minimal_scalar_l0_potential':f0*(fx*v+f0*w)/r}
            for k,vv in vals.items():close(row[k],vv)
            K=4*(A*A+2*B*B+2*C*C+D*D)
            ric=(A+2*B)**2+(-A+2*C)**2+2*(-B+C+D)**2
            an=(K-2*ric+R*R/3)/(1920*mp.pi**2)-(K-4*ric+R*R)/(5760*mp.pi**2)
            close(row['scalar_anomaly_beta0'],an);close(row['trace_residual_G1'],-R/(8*mp.pi)-an)
        elif kind.startswith('MP'):
            a,d=mp.mpf(row['a']),mp.mpf(row['d']);m=mp.mpf(1)
            # Local polar radius around one mouth, polar direction toward the other.
            U=lambda r,u:1+m/r+m/mp.sqrt(d*d+r*r-2*d*r*u)
            if kind=='MP_boundary':
                u=mp.mpf(row['u']);V=U(a,u);n=mp.diff(lambda r:U(r,u),a)
                # Obtain K from derivatives of the induced timelike metric.
                ktime=mp.diff(lambda r:-U(r,u)**-2,a)/(2*V*(-V**-2))
                kang=mp.diff(lambda r:U(r,u)**2*r*r,a)/(2*V*(V*V*a*a))
                close(row['sigma_G1'],-kang/(2*mp.pi));close(row['p_G1'],(ktime+kang)/(4*mp.pi))
                close(row['charge_G1'],-n/(2*mp.pi*V*V));close(row['U'],V)
                return
            # Null energy conservation gives dt/ds=(1+m/s+m/(d-s))^2.
            T=mp.quad(lambda s:(1+m/s+m/(d-s))**2,[a,d/2,d-a]);V=U(a,mp.mpf(1))
            close(row['T_axis'],T)
            if kind=='MP_fixed_witness':
                close(row['U_face'],V);close(row['coordinate_margin'],mp.mpf(row['Delta'])-T)
                close(row['proper_margin'],(mp.mpf(row['Delta'])-T)/V)
                assert T<mp.mpf(row['Delta'])
            else:
                # Integrate the actual angular-dependent shell, not an averaged lapse.
                Es=-a*mp.quad(lambda u:U(a,u)+a*mp.diff(lambda r:U(r,u),a),[-1,0,1])
                qs=-a*a*mp.quad(lambda u:mp.diff(lambda r:U(r,u),a),[-1,0,1])
                close(row['shell_proper_energy_G1'],Es);close(row['shell_charge_G1'],qs)
                close(row['proper_return_minus_send'],(T-mp.mpf(row['prescribed_Delta']))/V)
        else: raise ValueError('Unknown calculation kind')


def verify(records: Path, output: Path):
    raw=records.read_bytes();bundle=json.loads(raw)
    checks=geometry_checks();results=[]
    for candidate in bundle['candidates']:
        trials=candidate['calculation']['trials']
        if not trials:raise ValueError('No calculation')
        for row in trials:verify_trial(row)
        results.append({'candidate_id':candidate['candidate_id'],'checked':len(trials),'passed':True})
    out={'records_sha256':hashlib.sha256(raw).hexdigest(), 'checks':checks,
         'candidates':results,'external_peer_review':'not_performed'}
    output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n')
    return out

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--records',type=Path,required=True);p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();print(json.dumps(verify(args.records,args.output),ensure_ascii=False))
