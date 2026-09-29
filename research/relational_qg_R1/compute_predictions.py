from __future__ import annotations
import json,sys,platform,hashlib
from pathlib import Path
import numpy as np
import scipy
from scipy.special import erf
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.linalg import eigh_tridiagonal
import sympy as sp

ROOT=Path(__file__).resolve().parent

def kernel(r: float, ell: float=1.0)->float:
    if ell<=0 or r<0: raise ValueError('ell>0, r>=0 required')
    if r==0: return 1/(np.sqrt(np.pi)*ell)
    return float(erf(r/(2*ell))/r)

def force_ratio(x: float)->float:
    return float(erf(x/2)-x/np.sqrt(np.pi)*np.exp(-x*x/4))

def phase_difference(d:float)->float:
    return 2*kernel(3*d)-kernel(4*d)-kernel(2*d)

def pure_negativity(amplitudes:np.ndarray)->float:
    rho=np.outer(amplitudes,amplitudes.conj())
    pt=rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
    return float(-np.linalg.eigvalsh(pt).clip(max=0).sum())

def original_control():
    q=np.linspace(-2,2,81)
    deg=np.r_[1.,np.full(79,2.),1.]
    es=[]; vecs=[]
    for E in [0,.1,.2]:
        e,v=eigh_tridiagonal(8*deg+.5*q*q+E*np.exp(-q),np.full(80,-8.))
        es.append(e);vecs.append(v)
    diff=float(es[2][0]-2*es[1][0]+es[0][0]); tstar=float(np.pi/abs(diff))
    seed=vecs[0][:,0]
    records=[]
    for t in [0.,50.,100.,200.,tstar]:
        psi=[v @ (np.exp(-1j*e*t)*(v.T@seed)) for e,v in zip(es,vecs)]
        mat=np.stack([psi[0],psi[1],psi[1],psi[2]])/2
        rho=mat @ mat.conj().T
        pt=rho.reshape(2,2,2,2).transpose(0,3,2,1).reshape(4,4)
        records.append({'t':t,'negativity':float(-np.linalg.eigvalsh(pt).clip(max=0).sum()),
                        'purity':float(np.trace(rho@rho).real),'trace_error':float(abs(np.trace(rho)-1))})
    return {'scope':'Anchored 81-state submodel, not the unpinned original uniform q mode',
            'energies':[float(e[0]) for e in es], 'interaction_shift':diff,
            'adiabatic_pi_phase_time':tstar,'quench_dynamics':records,
            'uniform_massless_vacuum_E0_ratio':[{'q':x,'ratio':float(np.exp(-2*x))} for x in [-2,-1,0,1,2]]}

def tensor_bootstrap():
    a,b,c,d=sp.symbols('a b c d');eta=sp.diag(-1,1,1,1)
    fields=sp.symbols('h0:10'); pairs=[(i,j) for i in range(4) for j in range(i,4)]
    H=sp.zeros(4)
    for z,(i,j) in zip(fields,pairs):H[i,j]=z;H[j,i]=z
    Hu=eta*H*eta; tr=sp.trace(eta*H)
    p=sp.Matrix(sp.symbols('p0:4',real=True));p2=(p.T*eta*p)[0];v=Hu*p
    L=(-a*p2*sum(H[i,j]*Hu[i,j] for i in range(4) for j in range(4))
       +b*(v.T*eta*v)[0]+c*(p.T*v)[0]*tr+d*p2*tr**2)
    K=sp.hessian(L,fields)
    R=sp.Matrix(10,4,lambda r,z:p[pairs[r][0]]*(1 if pairs[r][1]==z else 0)+p[pairs[r][1]]*(1 if pairs[r][0]==z else 0))
    equations=[]
    for entry in K*R:equations.extend(sp.Poly(sp.expand(entry),*p).coeffs())
    sol=sp.linsolve(equations,[a,b,c,d])
    Kf=K.subs({a:1,b:2,c:-2,d:1})
    assert (Kf*R).applyfunc(sp.expand)==sp.zeros(10,4)
    poles=[]
    for ps in [[1,0,0,1],[5,3,4,0],[3,1,2,2]]:
        subs=dict(zip(p,ps));rank=Kf.subs(subs).rank();gr=R.subs(subs).rank()
        dof=10-rank-gr;assert dof==2
        poles.append({'p_cov':ps,'field_kernel_dimension':10-rank,'gauge_rank':gr,'physical_polarizations':dof})
    tensor_basis=[]
    for i in range(3):
        e=np.zeros((3,3));e[i,i]=1;tensor_basis.append(e)
    for i,j in [(0,1),(0,2),(1,2)]:
        e=np.zeros((3,3));e[i,j]=e[j,i]=1/np.sqrt(2);tensor_basis.append(e)
    tt_checks=[]
    for kv in [[0,0,1],[1,2,3],[3,-4,2]]:
        k=np.asarray(kv,dtype=float);k/=np.linalg.norm(k)
        P=np.eye(3)-np.outer(k,k)
        def proj(e):return P@e@P-.5*P*np.trace(P@e)
        mat=np.array([[np.sum(e*proj(f)) for f in tensor_basis] for e in tensor_basis])
        eig=np.linalg.eigvalsh(mat)
        assert np.sum(eig>.5)==2
        tt_checks.append({'direction':kv,'eigenvalues':eig.tolist(),'projector_error':float(np.max(abs(mat@mat-mat)))})
    return {'coefficient_solution':str(sol),'exact_gauge_null_identity':True,
            'null_momentum_counts':poles,'TT_projector_checks':tt_checks,
            'scope':'Linearized, flat-background, two-derivative sector; not emergent from the original graph Hamiltonian'}

def gaussian_predictions():
    rows=[]
    for x in [.1,.5,1.,2.,3.,4.,6.,10.]:
        calc,err=quad(lambda k: (2/np.pi)*np.exp(-k*k)*np.sinc(k*x/np.pi),0,np.inf,epsabs=2e-12,epsrel=2e-12)
        exact=kernel(x)
        assert abs(calc-exact)<2e-11
        lens_num,le=quad(lambda z:4*x*force_ratio(np.sqrt(x*x+z*z))/(x*x+z*z)**1.5,
                         0,np.inf,epsabs=1e-11,epsrel=1e-11)
        lens_exact=4/x*(-np.expm1(-x*x/4))
        assert abs(lens_num-lens_exact)<2e-10
        rows.append({'r_over_ell':x,'ell_times_kernel':exact,'force_over_Newton':force_ratio(x),
                     'potential_Fourier_error':abs(calc-exact),'b_over_ell':x,
                     'lensing_over_point_GR':float(-np.expm1(-x*x/4)),
                     'lensing_integral_error':abs(lens_num-lens_exact)})
    return {'kernel':'erf(r/(2 ell))/r','center_kernel':'1/(sqrt(pi) ell)',
            'center_force':'G m1 m2 r/(6 sqrt(pi) ell^3) + O(r^3)',
            'rows':rows,
            'radiation':[{'omega_ell_over_c':y,'power_ratio':float(np.exp(-y*y))} for y in [.01,.1,.5,1.,2.,3.]],
            'scope':'Leading order G, GM/(c^2 ell)<<1; source-to-probe interaction includes two identical form-factor vertices'}

def quantum_phase():
    ds=[.1,.25,.5,.75,1.,1.5,2.,4.]
    dstar=brentq(phase_difference,.1,2.,xtol=1e-14)
    rows=[]
    tau=10.
    for d in ds+[dstar]:
        v=np.array([kernel(3*d),kernel(4*d),kernel(2*d),kernel(3*d)])
        amps=np.exp(1j*tau*v)/2
        neg=pure_negativity(amps)
        diff=phase_difference(d)
        formula=abs(np.sin(tau*diff/2))/2
        assert abs(neg-formula)<2e-14
        rows.append({'d_over_ell':d,'ell_DeltaK':diff,'point_Newton_ell_DeltaK':-1/(12*d),
                     'tau':tau,'negativity':neg,'negativity_formula':formula})
    return {'geometry':'A0=0,A1=d; B0=3d,B1=4d; sharply localized, static held packets',
            'DeltaK':'2 K(3d)-K(4d)-K(2d)',
            'phase':'chi=(G mA mB t/hbar) DeltaK',
            'small_d':'DeltaK=d^2/(6 sqrt(pi) ell^3)+O(d^4/ell^5)',
            'large_d':'DeltaK=-1/(12d)+exponentially small terms',
            'phase_zero_d_over_ell':dstar,'phase_zero_ell_DeltaK':phase_difference(dstar),
            'rows':rows,'scope':'Leading quasistatic order G; packet overlap, traps, radiation, and laboratory decoherence omitted'}

def stable_operator_control():
    from scipy.linalg import expm
    n=17;L=np.zeros((n,n))
    for i in range(n):
        j=(i+1)%n
        L[i,i]+=1;L[j,j]+=1;L[i,j]-=1;L[j,i]-=1
    F=expm(-.5*L)
    perm=np.random.default_rng(12026).permutation(n)
    Fp=expm(-.5*L[np.ix_(perm,perm)])
    vals=np.linalg.eigvalsh(F)
    assert np.min(vals)>0 and np.max(vals)<1+1e-12
    assert np.max(abs(F@np.ones(n)-1))<1e-12
    assert np.max(abs(Fp-F[np.ix_(perm,perm)]))<1e-12
    return {'n_sites':n,'spectral_min':float(vals.min()),'spectral_max':float(vals.max()),
            'constant_mode_error':float(np.max(abs(F@np.ones(n)-1))),
            'relabel_covariance_error':float(np.max(abs(Fp-F[np.ix_(perm,perm)]))),
            'point_pair_lower_bound':'H_two_body >= -G mA mB/(sqrt(pi) ell)',
            'important_limit':'Smoothing does not remove the k=0 cosmological/vacuum mode'}

if __name__=='__main__':
    result={'original_control':original_control(),'tensor_bootstrap':tensor_bootstrap(),
            'gaussian_predictions':gaussian_predictions(),'quantum_phase':quantum_phase(),
            'spatial_operator':stable_operator_control(),
            'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__,'sympy':sp.__version__},
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    p=ROOT/'results.json';p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print('wrote',p)
    print('tensor solution',result['tensor_bootstrap']['coefficient_solution'])
    print('phase zero d/ell',result['quantum_phase']['phase_zero_d_over_ell'])
    for row in result['quantum_phase']['rows']:print(row)
    print('Gaussian force/lensing rows:')
    for row in result['gaussian_predictions']['rows']:print(row)
