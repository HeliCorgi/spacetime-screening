#!/usr/bin/env python3
"""Independent R4 checks: full invariant Euler equation, not Galerkin code.

Does not import the forward solver. It differentiates the original sixth-order
radial curvature density, reconstructs a stored rational-Chebyshev solution at
high precision, and checks the continuum equations at new points. The stored
coefficients are double precision; high precision controls evaluation error,
not their approximation error. No proof of full evolution or stability.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import platform
from pathlib import Path
import mpmath as mp
import sympy as sp

BASE_SHA = '39fa44951a83d44d3bdae88ee6a0ab9b6ad5af34'


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def invariant_equations():
    r = sp.symbols('r', positive=True)
    z, n = sp.symbols('z0:13'), sp.symbols('n0:7')
    def dr(f):
        return (sp.diff(f,r)+sum(sp.diff(f,z[j])*z[j+1] for j in range(12))
                +sum(sp.diff(f,n[j])*n[j+1] for j in range(6)))
    def lap(f):
        return sp.exp(-2*z[0])*(dr(dr(f))+(2/r+z[1])*dr(f))
    rr = sp.exp(-2*z[0])*(-2*z[2]-2*z[1]/r)
    tt = sp.exp(-2*z[0])*(-z[2]-3*z[1]/r-z[1]**2)
    R = rr+2*tt
    lr = lap(rr)-4*sp.exp(-2*z[0])*(1/r+z[1])**2*(rr-tt)
    lt = lap(tt)+2*sp.exp(-2*z[0])*(1/r+z[1])**2*(rr-tt)
    V = (R-lap(R)+lap(lap(R))/4-rr**2-2*tt**2+(rr*lr+2*tt*lt)/4
         +R**2/2-R*lap(R)/8)
    # Direct Euler derivative of sqrt(gamma)*N*V, with no use of the
    # integration-by-parts weak functional used by the numerical solver.
    density = sp.expand(r**2*sp.exp(3*z[0])*n[0]*V)
    EL = 0
    for j in range(7):
        term = sp.diff(density,z[j])
        for _ in range(j):
            term = sp.expand(dr(term))
        EL += (-1)**j*term
    EL = sp.expand(EL)
    require(not (set(z[7:]) & EL.free_symbols), 'higher derivatives did not cancel')
    require(sp.simplify(sp.diff(sp.exp(3*z[0])*V,z[6])+sp.exp(-3*z[0]))==0,
            'curved sixth-derivative coefficient')
    return (sp.lambdify((r,*z[:7]),sp.exp(3*z[0])*V,'mpmath',cse=True),
            sp.lambdify((r,*z[:7],*n),EL/r**2,'mpmath',cse=True))


def matrix_control():
    # Integrate the actual nonconstant positive lapse against TT profiles.
    with mp.workdps(65):
        modes = [1,5]
        N = mp.matrix(2)
        for i,ki in enumerate(modes):
            for j,kj in enumerate(modes):
                N[i,j] = mp.quad(lambda x: 2*mp.cos(ki*x)*mp.cos(kj*x)
                                  *(1+mp.cos(4*x)/2),[0,mp.pi,2*mp.pi])/(2*mp.pi)
        invA = mp.diag([mp.mpf(4)/9,mp.mpf(4)/729])
        S = mp.diag([mp.mpf(2)/3,mp.mpf(2)/27])
        old, new = (N*invA+invA*N)/2, S*N*S
        eold, enew = mp.eigsy(old,eigvals_only=True),mp.eigsy(new,eigvals_only=True)
        require(eold[0]<0 and enew[0]>0, 'kinetic ordering counterexample')
        require(abs(mp.det(old)+mp.mpf(385)/531441)<mp.mpf('1e-60'),'old determinant')
        require(abs(mp.det(new)-mp.mpf(5)/2187)<mp.mpf('1e-60'),'new determinant')
        return dict(old_smallest=mp.nstr(eold[0],40),repaired_smallest=mp.nstr(enew[0],40),
                    scope='positive-lapse TT test, not an on-shell curved-background ghost theorem')


def verify_profile(data, equations):
    require(data['model']=='R4_2' and data['base_sha']==BASE_SHA,'model/base mismatch')
    require(data['kinetic_ordering']=='S N S','unrepaired kinetic ordering')
    for flag in ('full_evolution_solved','generic_stability_proved','full_quantum_gravity'):
        require(data[flag] is False,'unsupported claim: '+flag)
    for rows in data['runs']:
        for row in rows:
            require(0<row['lapse_lower_bound_finite_expansion']<=row['lapse_center'], 'lapse gate')
            require(row['strong_constraint_sample_error']<1e-6 and row['strong_lapse_sample_error']<1e-6,
                    'reported strong residual gate')
            require(row['mass_surface_volume_gap']<1e-6, 'reported mass gate')
    require(data['max_refinement_difference']<1e-7,'reported refinement gate')
    record = data['reference_profile']
    with mp.workdps(65):
        a = [mp.mpf(str(x)) for x in record['zeta_coefficients']]
        b = [mp.mpf(str(x)) for x in record['lapse_coefficients']]
        scale = mp.mpf(str(record['map_scale']))
        eps, sigma = mp.mpf(str(record['epsilon'])),mp.mpf(str(record['sigma_over_ell']))
        require(len(a)==len(b)==record['modes'], 'coefficient dimensions')
        def profile(r,coefs):
            u=scale/mp.sqrt(scale**2+r*r)
            x=2*u-1
            t0,t1=mp.mpf(1),x
            value=coefs[0]*t0
            if len(coefs)>1:
                value+=coefs[1]*t1
            for c in coefs[2:]:
                t0,t1=t1,2*x*t1-t0
                value+=c*t1
            return u*value
        zeta=lambda r:profile(r,a)
        lapse=lambda r:1+profile(r,b)
        require(abs(zeta(0)-mp.mpf(str(record['zeta_center'])))<mp.mpf('1e-12'),'center metric')
        require(abs(lapse(0)-mp.mpf(str(record['lapse_center'])))<mp.mpf('1e-12'),'center lapse')
        lower=1-sum(abs(x) for x in b)
        require(lower>0,'independent global finite-expansion lapse bound')
        mass=scale*sum((-1)**j*x for j,x in enumerate(a))
        require(abs(mass/eps-mp.mpf(str(record['adm_mass_over_rest'])))<mp.mpf('1e-7'),
                'independent ADM mass mismatch')
        norm=max(1,16*mp.pi*eps/(2*mp.pi*sigma**2)**mp.mpf('1.5'))
        rows=[]
        for point in ('.05','.3','1','3','10'):
            r=mp.mpf(point)*sigma
            zj=[mp.diff(zeta,r,j) for j in range(7)]
            nj=[mp.diff(lapse,r,j) for j in range(7)]
            density=eps*mp.exp(-r*r/(2*sigma*sigma))/(2*mp.pi*sigma*sigma)**mp.mpf('1.5')
            hc=(equations[0](r,*zj)-16*mp.pi*density)/norm
            lc=equations[1](r,*zj,*nj)/norm
            require(abs(hc)<mp.mpf('1e-6'), 'independent full Hamiltonian residual')
            require(abs(lc)<mp.mpf('1e-6'), 'independent full Euler lapse residual')
            rows.append(dict(r_over_ell=mp.nstr(r,12),hamiltonian_error=mp.nstr(hc,20),
                             lapse_error=mp.nstr(lc,20)))
        mean=4*mp.pi*mp.quad(lambda r:r*r*mp.exp(-r*r/(2*sigma*sigma))*lapse(r),
                           [0,sigma,3*sigma,8*sigma,mp.inf])/(2*mp.pi*sigma*sigma)**mp.mpf('1.5')
        require(abs(mean-mp.mpf(str(record['mean_lapse'])))<mp.mpf('1e-10'),'independent mean lapse')
        require(abs(mean-mp.mpf(str(record['d_adm_d_rest'])))<mp.mpf('1e-10'),'mass-clock identity')
        return dict(epsilon=mp.nstr(eps,12),sample_checks=rows,
                    lapse_bound=mp.nstr(lower,30),adm_mass_over_rest=mp.nstr(mass/eps,30),
                    mean_lapse=mp.nstr(mean,30),evaluation_dps=65,
                    note='one stored reference profile checked independently; coefficients remain double precision')


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--evidence',type=Path)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    base=Path(__file__).resolve().parents[2]
    path=args.evidence or base/'research/relational_qg_R4/results.json'
    data=json.loads(path.read_text(encoding='utf-8'))
    numerical=base/'src/numerical/relational_qg_r4_initial_data.py'
    require(data['source_sha256']==hashlib.sha256(numerical.read_bytes()).hexdigest(),'stale numerical evidence')
    result=dict(verified=True,kinetic=matrix_control(),profile=verify_profile(data,invariant_equations()),
                evidence_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                verifier_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                full_evolution_solved=False,generic_stability_proved=False,
                environment=dict(python=platform.python_version(),sympy=sp.__version__,mpmath=mp.__version__))
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':
    main()
