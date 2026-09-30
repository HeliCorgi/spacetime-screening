#!/usr/bin/env python3
"""Independent checks of R2; does not import the forward research script.

Uses bisection, light-cone convolution, a direct polarization angular sum,
radial effective-potential derivatives and a boosted Schwinger integral.
A pass certifies these scoped calculations, not completed quantum gravity.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from pathlib import Path

import mpmath as mp
import sympy as sp

BASE_SHA='4c600df0b331a19f9d21384bf58472bee01a5a16'


def req(ok,message):
    if not ok:
        raise AssertionError(message)


def K(x):
    return mp.erf(abs(x)/2)/abs(x) if x else 1/mp.sqrt(mp.pi)


def bisect(f,a,b,steps=190):
    a,b=mp.mpf(a),mp.mpf(b)
    fa,fb=f(a),f(b)
    req(fa*fb<0,'root must be bracketed')
    for _ in range(steps):
        mid=(a+b)/2;fm=f(mid)
        if fa*fm<=0:
            b=mid
        else:
            a=mid;fa=fm
    return (a+b)/2


def phase_checks():
    f=lambda d:2*K(3*d)-K(4*d)-K(2*d)
    node=bisect(f,'.5','.75')
    # Signed branch-density differences; no four-energy subtraction is used.
    def closed_phase(d,s):
        a=[(1,0),(100,-s),(-1,d),(-100,-s-d/100)]
        b=[(1,3*d),(100,3*d+s),(-1,4*d),(-100,3*d+s-d/100)]
        for lab in (a,b):
            req(mp.fsum(m for m,x in lab)==0,'mass branch difference')
            req(abs(mp.fsum(m*x for m,x in lab))<mp.mpf('1e-50'),'COM branch difference')
        return mp.fsum(ma*mb*K(x-y) for ma,x in a for mb,y in b)
    values=[]
    for s in [mp.mpf(5),mp.mpf(10),mp.mpf(100)]:
        n=bisect(lambda d:closed_phase(d,s),'.6','.85')
        req(abs(closed_phase(n,s))<mp.mpf('1e-48'),'recoil residual')
        values.append({'s':str(s),'node':mp.nstr(n,42)})
    # The integral representation is separate from the erf calculation above.
    for r in [node,2*node,3*node,4*node]:
        integral=mp.quad(lambda t:mp.exp(-r*r*t*t/4),[0,1])/mp.sqrt(mp.pi)
        req(abs(integral-K(r))<mp.mpf('1e-50'),'Gaussian average kernel')
    return {'R1_node':mp.nstr(node,42),'recoil':values}


def convolution_checks():
    rows=[]
    for t,r in [(mp.mpf('.5'),mp.mpf(1)),(mp.mpf(3),mp.mpf(1)),(mp.mpf(2),mp.mpf(0))]:
        # Convolution of delta(t-|y|)/(4pi |y|) with a normalized spatial Gaussian.
        conv=(t/2)*mp.quad(lambda c:mp.exp(-(r*r+t*t-2*r*t*c)/4)/(4*mp.pi)**mp.mpf('1.5'),[-1,1])
        closed=((mp.exp(-(r-t)**2/4)-mp.exp(-(r+t)**2/4))/(8*mp.pi**mp.mpf('1.5')*r)
                if r else t*mp.exp(-t*t/4)/(8*mp.pi**mp.mpf('1.5')))
        req(abs(conv-closed)<mp.mpf('1e-50'),'retarded light-cone convolution')
        rows.append({'t':str(t),'r':str(r),'Gret':mp.nstr(conv,40)})
    req(mp.mpf(rows[0]['Gret'])>0,'spacelike response must not be hidden')
    return {'rows':rows,'strict_microcausality_passed':False}


def tensor_and_noise_checks():
    # Explicit real-space divergence, independently of Fourier implementation.
    t,x,y,z=sp.symbols('t x y z',real=True)
    f=sp.exp(-t*t-x*x-y*y-z*z)
    Q=sp.diag(1,-1,0);coords=[x,y,z]
    T=sp.zeros(4)
    T[0,0]=sum(Q[i,j]*sp.diff(f,coords[i],coords[j]) for i in range(3) for j in range(3))
    for i in range(3):
        T[0,i+1]=T[i+1,0]=-sum(Q[i,j]*sp.diff(f,t,coords[j]) for j in range(3))
        for j in range(3):T[i+1,j+1]=Q[i,j]*sp.diff(f,t,2)
    full=[t,x,y,z]
    req(all(sp.simplify(sum(sp.diff(T[a,b],full[a]) for a in range(4)))==0 for b in range(4)),
        'real-space conserved pulse')
    # Direct TT projector angular contraction for QijQij=1.
    norm=mp.sqrt(2)
    def angular(mu,phi):
        n=mp.matrix([mp.sqrt(1-mu*mu)*mp.cos(phi),mp.sqrt(1-mu*mu)*mp.sin(phi),mu])
        P=mp.eye(3)-n*n.T;Qm=mp.diag([1/norm,-1/norm,0])
        tr=lambda a:sum(a[i,i] for i in range(3))
        return tr(Qm*P*Qm*P)-tr(Qm*P)**2/2
    # Polynomial in mu after the exact periodic trapezoid sum over phi.
    angular_integral=mp.quad(lambda mu:mp.fsum(angular(mu,2*mp.pi*j/16) for j in range(16))*2*mp.pi/16,[-1,0,1])
    req(abs(angular_integral-8*mp.pi/5)<mp.mpf('1e-45'),'TT angular normalization')
    # Independently use N_gravitons=integral dE/(hbar omega), Gamma=N/2,
    # dE/domega=G/(5pi) omega^6 |Delta Iij(omega)|^2 F^2.
    strength=mp.mpf('.01');sigma=mp.mpf('.2')
    rows=[]
    for tau in map(mp.mpf,[1,2,4,8]):
        def dN(k):
            I_squared=8*mp.pi*tau*tau*mp.exp(-tau*tau*k*k)  # I=2Q f, Q^2=1
            return strength/(5*mp.pi)*k**5*I_squared*mp.exp(-(1+sigma*sigma)*k*k)
        gamma=mp.quad(dN,[0,1,mp.inf])/2
        target=4*strength*tau*tau/(5*(1+sigma*sigma+tau*tau)**3)
        req(abs(gamma-target)<mp.mpf('1e-45'),'noise versus emitted graviton count')
        rows.append(mp.nstr(gamma,40))
    return {'Ward_identity':True,'TT_angular_integral':mp.nstr(angular_integral,40),'Gamma_rows':rows,
            'full_apparatus_derived':False}


def orbit_checks():
    A=1/(6*mp.sqrt(mp.pi));eps=mp.mpf('.01')
    rows=[]
    for x in map(mp.mpf,['.1','.5','1','2','4','6']):
        # Average Gaussian density instead of subtracting nearly equal erf terms.
        w2=mp.quad(lambda u:u*u*mp.exp(-x*x*u*u/4),[0,1])/(2*mp.sqrt(mp.pi))
        force=-mp.diff(K,x)
        req(abs(w2-force/x)<mp.mpf('1e-45'),'Kepler force from potential')
        L2=x**4*w2
        effective=lambda r:-K(r)+L2/(2*r*r)
        kr2=mp.diff(effective,x,2)
        req(kr2>0 and w2<=A,'circular stability and bounded frequency')
        J=x**3*w2;Jp=x*x*mp.exp(-x*x/4)/(2*mp.sqrt(mp.pi))
        req(abs(kr2-(w2+Jp/x**2))<mp.mpf('1e-45'),'epicycle curvature')
        rows.append({'x':str(x),'Omega_over_Omega0':mp.nstr(mp.sqrt(w2/A),40)})
    # Same harmonic frequency follows from the quantum relative Hamiltonian.
    x=sp.symbols('x',real=True)
    V=-sp.erf(x/2)/x
    curvature=sp.limit(sp.diff(V,x,2),x,0)
    req(sp.simplify(curvature-1/(6*sp.sqrt(sp.pi)))==0,'classical/quantum core frequency')
    # Quantum quartic first-order shift in R1 energy units.
    shift=sp.simplify((-1/(160*sp.sqrt(sp.pi)))*sp.Rational(15,4)*6*sp.sqrt(sp.pi))
    req(shift==-sp.Rational(9,64),'quartic quantum shift')
    return {'rows':rows,'core_curvature':str(curvature),'quantum_quartic_shift':str(shift),
            'max_form_factor_power_loss_eps_0p01':mp.nstr(1-mp.exp(-4*eps*A),40)}


def boost_check():
    beta=mp.mpf('.01');a=beta*beta/(1-beta*beta)
    f=lambda d:2*K(3*d)-K(4*d)-K(2*d)
    d0=bisect(f,'.5','.75')
    rows=[]
    for cos2 in (0,1):
        def Kg(r):
            return mp.quad(lambda u:mp.exp(-r*r*u*u*((1-cos2)+cos2/(1+a*u*u))/4)/mp.sqrt(1+a*u*u),[0,1])/mp.sqrt(mp.pi)
        boosted=lambda d:2*Kg(3*d)-Kg(4*d)-Kg(2*d)
        # An independent root of the exact boosted Schwinger integral.
        root=mp.findroot(boosted,(d0-mp.mpf('.01'),d0+mp.mpf('.01')))
        D=lambda r:cos2*mp.diff(K,r,2)+(1-cos2)*mp.diff(K,r)/r
        shift=-(2*D(3*d0)-D(4*d0)-D(2*d0))/mp.diff(f,d0)
        residual=root-d0-beta*beta*shift
        req(abs(residual)<mp.mpf('5e-9'),'boost perturbation versus exact kernel')
        rows.append({'cos_theta_squared':cos2,'exact_node_at_beta_0p01':mp.nstr(root,35),
                     'beta2_coefficient':mp.nstr(shift,35),'higher_order_remainder':mp.nstr(residual,12)})
    return rows


def evidence_check(path,derived):
    data=json.loads(path.read_text(encoding='utf-8'))
    source=Path(__file__).with_name('relational_qg_r2_dynamics.py')
    req(data['base_sha']==BASE_SHA,'wrong R1 base')
    req(data['source_sha256']==hashlib.sha256(source.read_bytes()).hexdigest(),'stale forward evidence')
    req(data['new_fundamental_parameters']==0,'parameter accounting')
    bound=(mp.mpf(1)/2+1/mp.e)/(3*mp.sqrt(mp.pi))
    req(abs(mp.mpf(data['finite_particle_continuation']['dimensionless_Hessian_bound'])-bound)<mp.mpf('1e-30'),'Hessian continuation bound')
    req(data['finite_particle_continuation']['head_on_crossings']>0,'collision continuation control')
    req(data['retarded_and_vacuum']['strict_metric_microcausality'] is False,'microcausality overclaim')
    req(data['retarded_and_vacuum']['vacuum_energy_removed'] is False,'vacuum overclaim')
    req(data['recoil_phase']['point_probe_node_is_universal'] is False,'node overclaim')
    for fwd,own in zip(data['recoil_phase']['rows'],derived['phases']['recoil']):
        req(abs(mp.mpf(fwd['node_d_over_ell'])-mp.mpf(own['node']))<mp.mpf('1e-28'),'independent recoil mismatch')
    for fwd,own in zip(data['vacuum_dephasing']['rows'],derived['noise']['Gamma_rows']):
        req(abs(mp.mpf(fwd['Gamma'])-mp.mpf(own))<mp.mpf('1e-30'),'independent noise mismatch')
    for fwd,own in zip(data['orbits_and_balance']['rows'],derived['orbits']['rows']):
        req(abs(mp.mpf(fwd['Omega_over_Omega0'])-mp.mpf(own['Omega_over_Omega0']))<mp.mpf('1e-28'),'independent orbit mismatch')
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--evidence',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    with mp.workdps(60):
        out={'base_sha':BASE_SHA,'phases':phase_checks(),'convolution':convolution_checks(),
             'noise':tensor_and_noise_checks(),'orbits':orbit_checks(),'boost':boost_check()}
        if args.evidence:out['evidence_sha256']=evidence_check(args.evidence,out)
        out['all_implemented_assertions_passed']=True
        out['environment']={'python':platform.python_version(),'mpmath':mp.__version__,'sympy':sp.__version__}
        out['source_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verified':True,'R1_node':out['phases']['R1_node'],
                      'recoil_s5_node':out['phases']['recoil'][0]['node'],
                      'nonlinear_completion':False},ensure_ascii=False))


if __name__=='__main__':
    main()
