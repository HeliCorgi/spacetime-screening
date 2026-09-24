"""Independent v5 checks: Cayley/Richardson propagation and Legendre KKT pulses.

Does not import the forward model. Optional evidence is checked against current
source hashes; a report is never cleared from a missing or unverified evidence file.
"""
from __future__ import annotations
import argparse
import cmath
import copy
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import time
import unittest
import mpmath as mp
import sympy as sp

BASE_SHA="7724b58b6f571d01c35f6a1ef411aee9d79d62dd"
CASES=((.02,0),(.2,0),(2.,0),(.2,1))
GOLD=[(1.0405752066665466+.0018788018000565417j,-.28774426729989844-.0018781004697837662j),
      (1.0374783535519129+.018065000501122212j,-.27637837841060494-.017397421619826036j),
      (.99787266818191794+.07135902114546692j,-.028694276245708377+.004313967324200453j),
      (-.98605270495696248-.32286939924149892j,.27511464593870609+.029266320396136503j)]
MINIMUM_KEYS="candidate_id status geometry matter_content quantum_state dimension topology assumptions boundary_conditions symmetries approximation_order stress_energy backreaction support_accounting stability causal_structure sender_intervention receiver_observable P_Y_do_0 P_Y_do_1 distinguishability obstructions unresolved_assumptions literature code verification scope".split()


def check(ok, message):
    if not ok: raise AssertionError(message)


def validated_covariance(Sigma):
    check(Sigma.rows==Sigma.cols, "covariance not square")
    check(Sigma==Sigma.T, "covariance not symmetric")
    check(all(v>=0 for v in Sigma.eigenvals()), "negative covariance")
    return Sigma


def validate_record(r):
    check(all(k in r for k in MINIMUM_KEYS),"missing protocol field")
    check(type(r['dimension']) is int and r['dimension']==4,"wrong dimension")
    check(r['dimension_split']=={'space':3,'time':1},"wrong split")
    # This extension contains a conditional B only. It cannot approve any A.
    check(r['status']=='B',"unexpected classification; human/scientific review required")
    check(bool(r['unresolved_assumptions']),"missing unresolved assumptions")
    check(r['verification']['human_review_for_A'] is True,"human gate disabled")
    for key in ('P_Y_do_0','P_Y_do_1'):
        p=r[key]
        check(p['computed'] is False and p['distribution'] is None and p['reason'],"invented probability")
    d=r['distinguishability']
    check(d['computed'] is False and d['value'] is None and d['error_bound'] is None,"invented distinguishability")
    check(r['support_accounting']['complete'] is False,"invented apparatus")
    check(r['stress_energy']['renormalized'] is False,"difference promoted to full RSET")
    check(isinstance(r.get('assumption_changes'),list) and bool(r['assumption_changes']),"assumption changes omitted")
    check(set(r['stages'])==set('1234567'),"stage omitted")
    check(r['calculation']['tested']==len(r['calculation']['trials'])>0,"wrong count")
    return True


def cayley(wnorm, ell, nsteps, halfwidth=40):
    """Second-order symplectic midpoint of the original radial Sturm equation."""
    d=2*math.sqrt(1-.99**2); rp=1+d/2; rm=1-d/2
    kp=d/(2*rp*rp); w=wnorm*kp
    nuplus=w*rp*rp/d; numinus=w*rm*rm/d
    h=2*halfwidth/nsteps
    phi=cmath.exp(1j*nuplus*halfwidth)/rp; pi=-1j*nuplus*phi
    for i in range(nsteps):
        s=-halfwidth+(i+.5)*h
        # Reconstruct Delta and dr/ds directly, not a Taylor-series potential.
        if s>=0:
            e=math.exp(-s); x=1/(1+e); xm=e/(1+e)
        else:
            e=math.exp(s); x=e/(1+e); xm=1/(1+e)
        r=rm+d*xm
        q=w*w*r**4/(d*d)+ell*(ell+1)*x*xm
        z=h*h*q/4; den=1+z
        phi,pi=((1-z)*phi+h*pi)/den,(-h*q*phi+(1-z)*pi)/den
    u,us=rm*phi,rm*pi
    return ((u+1j*us/numinus)*cmath.exp(1j*numinus*halfwidth)/2,
            (u-1j*us/numinus)*cmath.exp(-1j*numinus*halfwidth)/2)


def alternate_scattering():
    rows=[]
    for (w,l),gold in zip(CASES,GOLD):
        table=[]
        for j,n in enumerate((1000,2000,4000,8000)):
            t,r=cayley(w,l,n)
            row=[(t,r)]
            for k in range(1,j+1):
                fac=4**k
                row.append(tuple((fac*row[k-1][a]-table[j-1][k-1][a])/(fac-1) for a in (0,1)))
            table.append(row)
        t,r=table[-1][-1]
        err=max(abs(t-gold[0]),abs(r-gold[1]))
        flux=abs(abs(t)**2-abs(r)**2-1)
        check(err<1e-9,"independent ODE mismatch")
        check(flux<2e-9,"independent flux mismatch")
        rows.append({'omega_over_kappa_plus':str(w),'ell':l,'T':[t.real,t.imag],
                     'R':[r.real,r.imag],'reference_difference':err,'flux_error':flux,
                     'finest_steps':8000,'Richardson_levels':4,'cutoff':40})
    return rows


def legendre_kkt(degree=8,dps=70):
    """Different basis and saddle-point solve; integrals use z=tanh(t)."""
    with mp.workdps(dps):
        z=sp.symbols('z')
        # Numerical evaluation of independently generated Legendre polynomials.
        polys=[];ders=[]
        for j in range(degree+1):
            expr=sp.legendre(j,z)
            polys.append(sp.lambdify(z,expr,'mpmath'))
            ders.append(sp.lambdify(z,sp.diff(expr,z),'mpmath'))
        def integrate(fun):
            def at(t):
                zz=mp.tanh(t); jac=1/mp.cosh(t)**2
                return fun(zz)*jac
            return mp.quad(at,[-5,-2,-1,0,1,2,5])
        def h(zz):return mp.exp(-1/(1-zz*zz))
        def hp(zz):return -2*zz*h(zz)/(1-zz*zz)**2
        K=mp.matrix(degree+1); B=mp.matrix(2,degree+1)
        for i in range(degree+1):
            B[0,i]=integrate(lambda zz,i=i:h(zz)*polys[i](zz)) if i%2==0 else mp.mpf(0)
            B[1,i]=integrate(lambda zz,i=i:mp.exp(zz)*h(zz)*polys[i](zz))
            for j in range(i,degree+1):
                if (i+j)%2:
                    val=mp.mpf(0)
                else:
                    val=integrate(lambda zz,i=i,j=j:(hp(zz)*polys[i](zz)+h(zz)*ders[i](zz))*(hp(zz)*polys[j](zz)+h(zz)*ders[j](zz)))
                K[i,j]=val;K[j,i]=val
        A=B[0,0]
        kkt=mp.matrix(degree+3); rhs=mp.matrix(degree+3,1)
        for i in range(degree+1):
            for j in range(degree+1): kkt[i,j]=K[i,j]
            for j in range(2):kkt[i,degree+1+j]=B[j,i];kkt[degree+1+j,i]=B[j,i]
        rhs[degree+1]=A
        sol=mp.lu_solve(kkt,rhs); c=sol[:degree+1,:]
        energy=(c.T*K*c)[0]
        check(abs(energy-mp.mpf('7.13604938033695241286726205077233466503141502'))<mp.mpf('1e-40'),"independent optimized energy")
        check(mp.norm(B*c-mp.matrix([A,0]),p=mp.inf)<mp.mpf('1e-50'),"independent constraints")
        # Exact Green-representer lower bound in a different formulation.
        g0=lambda zz:(1-zz*zz)/2
        g1=lambda zz:mp.cosh(1)+zz*mp.sinh(1)-mp.exp(zz)
        # Unlike bump-weighted integrals, these representers do not have a
        # superexponentially small tanh-coordinate tail. Integrate their full
        # compact z domain rather than truncate t at +/-5.
        a=mp.quad(g0,[-1,0,1]); b=mp.quad(g1,[-1,0,1])
        c1=mp.quad(lambda zz:mp.exp(zz)*g1(zz),[-1,0,1])
        lower=A*A*c1/(a*c1-b*b)
        check(lower<energy,"variational lower bound")
        check(abs(lower-mp.mpf("4.8558982225195451276728617381933410509147254"))<mp.mpf("1e-40"),"independent full-domain lower bound")
        # Gaussian preparation average of the finite Ramsey law.
        var=mp.mpf('.03'); mean=mp.mpf('.2'); base=mp.mpf('.5')
        numerical=mp.quad(lambda t:mp.exp(-t*t/2)/mp.sqrt(2*mp.pi)*mp.sin(2*(mean+mp.sqrt(var)*t)),[-mp.inf,0,mp.inf])*mp.exp(-2*base)
        analytic=mp.exp(-2*(base+var))*mp.sin(2*mean)
        check(abs(numerical-analytic)<mp.mpf('1e-50'),"independent Gaussian receiver integral")
        return {'dps':dps,'degree':degree,'energy':mp.nstr(energy,52),
                'H01_infimum':mp.nstr(lower,52),'constraints_passed':True,
                'Ramsey_average_verified':True,
                'interpretation':'Mathematical/state-control checks, not numerical SA receiver probabilities.'}


class Controls(unittest.TestCase):
    def test_inverse(self):
        a,b=sp.symbols('a b',real=True);S=sp.Matrix([[a,b],[b,a]])
        self.assertEqual(S*sp.Matrix([[a,-b],[-b,a]]),(a*a-b*b)*sp.eye(2))
    def test_inverse_wrong_sign_fails(self):
        S=sp.Matrix([[7,-4*sp.sqrt(3)],[-4*sp.sqrt(3),7]])
        self.assertNotEqual(S*S,sp.eye(2))
    def test_not_probability(self):self.assertEqual(7**2-(4*sp.sqrt(3))**2,1);self.assertGreater(7**2,1)
    def test_noise_mean_not_variance(self):
        S=validated_covariance(sp.eye(2));L=sp.Matrix([1,1]);self.assertEqual((L.T*S*L)[0],2)
    def test_nonzero_noise_kernel(self):
        S=validated_covariance(sp.Matrix([[1,-1],[-1,1]]));self.assertEqual(S*sp.Matrix([1,1]),sp.zeros(2,1))
    def test_bad_covariance(self):
        with self.assertRaises(AssertionError):validated_covariance(sp.diag(1,-1))
    def test_not_symmetric_covariance(self):
        with self.assertRaises(AssertionError):validated_covariance(sp.Matrix([[1,2],[0,1]]))
    def test_classical_covariance_not_quantum_vacuum(self):
        S=sp.diag(1,0);self.assertEqual(S.det(),0);self.assertLess(S.det(),sp.Rational(1,4))
    def test_added_psd_keeps_uncertainty(self):
        self.assertGreaterEqual((sp.eye(2)/2+sp.Matrix([[1,-1],[-1,1]])).det(),sp.Rational(1,4))
    def test_local_unitary_no_partner_change(self):
        bell=sp.Matrix([1,0,0,1])/sp.sqrt(2);rho=bell*bell.T
        X=sp.Matrix([[0,1],[1,0]]);U=sp.kronecker_product(X,sp.eye(2));out=U*rho*U.T
        partial=lambda rr:sp.Matrix(2,2,lambda i,j:sum(rr[2*k+i,2*k+j] for k in range(2)))
        self.assertEqual(partial(rho),partial(out))
    def test_local_tp_nonunitary_no_partner_change(self):
        p=sp.Rational(1,3);K0=sp.diag(1,sp.sqrt(1-p));K1=sp.Matrix([[0,sp.sqrt(p)],[0,0]])
        bell=sp.Matrix([1,0,0,1])/sp.sqrt(2);rho=bell*bell.T
        out=sp.zeros(4)
        for K in (K0,K1):
            L=sp.kronecker_product(K,sp.eye(2));out+=L*rho*L.T
        self.assertEqual(sp.Matrix(2,2,lambda i,j:sum(out[2*k+i,2*k+j] for k in range(2))),sp.eye(2)/2)
    def test_regularized_coordinate_tail(self):
        V,p=sp.symbols('V p',positive=True)
        self.assertEqual(sp.simplify(sp.diff(V**p,V)-p*V**(p-1)),0)
    def test_nonzero_calibration_error(self):
        with mp.workdps(40):
            q=mp.mpf('1.001');H=mp.quad(lambda z:mp.exp(q*z-1/(1-z*z)),[-1,0,1])
            self.assertNotEqual((1-q)*H,0)
    def test_finite_signal_area_not_zero(self):
        self.assertGreater(float(mp.quad(lambda z:mp.exp(-1/(1-z*z)),[-1,0,1])),0)
    def test_finite_moment_cancellation_not_Hadamard(self):
        with mp.workdps(40):
            p=((1-mp.sqrt(1-mp.mpf('.99')**2))/(1+mp.sqrt(1-mp.mpf('.99')**2)))**2
            self.assertGreater(2*p,1);self.assertLess(2*p,2)
    def test_sharp_profile_not_Cinfinity(self):
        # H01 minimizer generally has a nonzero endpoint derivative after zero-extension.
        z=sp.symbols('z');g1=sp.cosh(1)+z*sp.sinh(1)-sp.exp(z)
        self.assertNotEqual(sp.diff(g1,z).subs(z,1),0)
    def test_zero_noise_preserves_seed(self):
        v=sp.symbols('v',positive=True);self.assertEqual(sp.exp(-2*(v+0)),sp.exp(-2*v))


def examine_evidence(evidence):
    data=json.loads(evidence.read_text(encoding='utf-8'))
    source=Path(__file__).with_name('sa_two_input_state_v5.py')
    check(source.is_file(),"forward source missing")
    check(data['code_sha256']==hashlib.sha256(source.read_bytes()).hexdigest(),"stale code/evidence hash")
    check(data['base_sha']==BASE_SHA,"wrong base SHA")
    check(data['classification']=={'A':0,'B':1,'C':0},"classification modified")
    check(len(data['candidates'])==1,"candidate count")
    validate_record(data['candidates'][0])
    for index,(w,l) in enumerate(CASES):
        row=data['scattering_runs'][-1]['cases'][index]
        check(row['ell']==l and abs(float(row['omega_over_kappa_plus'])-w)<1e-15,"wrong sample")
        T=complex(float(row['T_re']),float(row['T_im']));R=complex(float(row['R_re']),float(row['R_im']))
        check(max(abs(T-GOLD[index][0]),abs(R-GOLD[index][1]))<1e-12,"changed scattering sample")
    # Mutations of the scientific record must fail, not be relabelled a physical C.
    mutation_checks=0
    for field in MINIMUM_KEYS:
        r=copy.deepcopy(data['candidates'][0]);del r[field]
        try:validate_record(r)
        except (AssertionError,KeyError):mutation_checks+=1
        else:raise AssertionError('missing field accepted: '+field)
    mutations=[lambda r:r.update(status='A'),lambda r:r.update(dimension=2),
               lambda r:r['P_Y_do_0'].update(distribution=0),
               lambda r:r['distinguishability'].update(value='0'),
               lambda r:r['verification'].update(human_review_for_A=False),
               lambda r:r['stress_energy'].update(renormalized=True),
               lambda r:r['support_accounting'].update(complete=True)]
    for mutate in mutations:
        r=copy.deepcopy(data['candidates'][0]);mutate(r)
        try:validate_record(r)
        except (AssertionError,KeyError):mutation_checks+=1
        else:raise AssertionError('invalid record accepted')
    return data,mutation_checks


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--evidence',type=Path)
    parser.add_argument('--output',type=Path)
    parser.add_argument('--report',type=Path)
    args=parser.parse_args();start=time.monotonic()
    tests=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Controls))
    check(tests.wasSuccessful(),'negative/control tests failed')
    print('Independent finite-frequency propagation',flush=True);s=alternate_scattering()
    print('Independent smooth Legendre/KKT optimization',flush=True);p=legendre_kkt()
    out={'verified':True,'verification_kind':'separate numerical implementation by the same author, not independent peer review',
         'environment':{'python':platform.python_version(),'sympy':sp.__version__,'mpmath':mp.__version__},
         'verifier_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'control_tests':tests.testsRun,'scattering':s,'pulses':p,
         'execution':{'kind':'github_actions' if os.environ.get('GITHUB_ACTIONS')=='true' else 'local','checkout_sha':os.environ.get('GITHUB_SHA'),'run_id':os.environ.get('GITHUB_RUN_ID')},'merging_performed_by_script':False}
    if args.evidence:
        data,n=examine_evidence(args.evidence)
        out.update(evidence_sha256=hashlib.sha256(args.evidence.read_bytes()).hexdigest(),mutation_checks=n)
        if args.report:
            text=['# SA v5 — two-input scattering and non-equilibrium preparation','',
                  '**A=0 / B=1 / C=0.** One continued candidate with scoped protocol obstructions; not a count of new devices.','',
                  'Full past probabilities are uncomputed, not zero.','',
                  '## Finite-frequency checks (Q/M=0.99)','',
                  '| omega/kappa+ | ell | |T|²+|R|² | independent complex-amplitude difference |',
                  '|---:|---:|---:|---:|']
            for a,b in zip(data['scattering_runs'][-1]['cases'],s):
                text.append(f"|{a['omega_over_kappa_plus']}|{a['ell']}|{float(a['inverse_spectral_energy_factor']):.12g}|{b['reference_difference']:.3g}|")
            text+=['','These are spectral inverse-control energy factors, not probabilities or finite apparatus energy.',
                   '', '## Smooth first-tail cancellation', '',
                   '| degree | energy / original bump energy | energy / previous shaped pulse |','|---:|---:|---:|']
            for r in data['pulse_runs'][-1]['smooth_feasible_optimizations']:
                text.append(f"|{r['degree']}|{float(r['ratio_to_original_bump_energy']):.12g}|{float(r['ratio_to_old_cancelled_pulse_energy']):.12g}|")
            text+=['','The constraints fix support and area, not receiver error or mean detector signal.',
                   '', '## Protocol candidate record', '', '```json',json.dumps(data['candidates'][0],ensure_ascii=False,indent=2),'```',
                   '',f'Control tests: {tests.testsRun}; record rejection/mutation checks: {n}.',
                   'No full all-mode RSET or independent peer review. This script does not perform merges or certify remote CI status; consult execution provenance.']
            args.report.parent.mkdir(parents=True,exist_ok=True);args.report.write_text('\n'.join(text)+'\n',encoding='utf-8')
    else:
        check(args.report is None,'report requires evidence')
    out['elapsed_seconds']=round(time.monotonic()-start,3)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'verified':True,'max_independent_amplitude_difference':max(r['reference_difference'] for r in s),'elapsed_seconds':out['elapsed_seconds']},ensure_ascii=False))

if __name__=='__main__':main()
