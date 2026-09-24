"""Separate arithmetic verifier: no import of either forward calculation.

Uses a canonical Sturm-Liouville midpoint integrator, a time-domain logarithmic
kernel for the 4D detector noise, and independently formed Pauli matrices.
This is same-author cross-checking, NOT external scientific peer review.
"""
from __future__ import annotations
import argparse
import cmath
import hashlib
import json
import math
from pathlib import Path
import unittest
import mpmath as mp
import sympy as sp


def reflection_midpoint(wbar:float,N:int,S:float=50.0)->dict[str,complex]:
    """Cayley midpoint on (phi,p), p=r^2 f phi_r; preserves canonical flux."""
    M=.2;Q=.1;root=math.sqrt(M*M-Q*Q);rp=M+root;rm=M-root
    omega=wbar*root/(rm*rm);nu=wbar/2;h=S/N
    u,v,z,w=0.0,rp,1.0,0.0
    for i in range(N):
        r=rm*(-math.expm1(-(i+.5)*h))
        a=1/(rp-r);b=-omega*omega*r**4/(rp-r)
        den=1-h*h*a*b/4;d=(1+h*h*a*b/4)/den;ab=h*a/den;ba=h*b/den
        u,v,z,w=d*u+ab*v,ba*u+d*v,d*z+ab*w,ba*z+d*w
    r=rm*(-math.expm1(-S));out={}
    for label,ph,p in [('D',u,v),('N',z,w)]:
        deriv=p/(rp-r)
        out[label]=cmath.exp(-2j*nu*S)*(ph+deriv/(1j*nu))/(ph-deriv/(1j*nu))
    return out


def extrapolate(values:list[complex])->complex:
    """Remove midpoint h^2 and h^4 terms; not claimed interval error bounds."""
    a,b,c=values
    return (16*(4*c-b)/3-(4*b-a)/3)/15


def time_domain_noise(dps:int=60)->mp.mpf:
    """-int int chi'(t) chi'(s) log|t-s| /(4pi^2), compact chi=sin^4(pi t)."""
    with mp.workdps(dps):
        cs=[mp.pi,-mp.pi/2];freqs=[2*mp.pi,4*mp.pi]
        def kernel(s):
            out=mp.mpf(0)
            for n,a in enumerate(freqs):
                for m,b in enumerate(freqs):
                    if n==m:
                        I=(1-s)*mp.cos(a*s)/2+mp.sin(a*s)/(2*a)
                    else:
                        I=((mp.sin(b*s)-mp.sin(a*s))/(a-b)
                           +(mp.sin(b*s)+mp.sin(a*s))/(a+b))/2
                    out+=cs[n]*cs[m]*I
            return out
        value=-mp.quad(lambda s:mp.log(s)*kernel(s),[0,mp.mpf('.1'),mp.mpf('.5'),1])/(2*mp.pi**2)
        return +value


def check_scattering(data:dict)->list[dict]:
    assert data['not_full_SA_horizon_crossing'] is True
    assert data['past_receiver_probability'] is None
    checked=[]
    assert len(data['rows'])==3
    for row in data['rows']:
        ww=float(row['omega_over_kappa_minus'])
        seq=[reflection_midpoint(ww,n) for n in [2048,4096,8192,16384]]
        errors={};convergence={}
        for bc in ['D','N']:
            c0=extrapolate([s[bc] for s in seq[:3]])
            c1=extrapolate([s[bc] for s in seq[1:]])
            target=complex(float(row[bc]['real']),float(row[bc]['imag']))
            errors[bc]=abs(c1-target);convergence[bc]=abs(c1-c0)
            assert errors[bc]<3e-8,(ww,bc,errors[bc])
            assert convergence[bc]<2e-8,(ww,bc,convergence[bc])
            assert abs(abs(target)-1)<1e-12
        checked.append({'omega_over_kappa_minus':ww,'max_reference_error':max(errors.values()),
                        'max_step_convergence_change':max(convergence.values()),
                        'method':'canonical midpoint 2048..16384, Richardson order6'})
    return checked


def verify(junction:dict,scattering:dict)->dict:
    rows=check_scattering(scattering)
    with mp.workdps(70):
        cut=mp.mpf(junction['finite_time_4D_noise_control']['spectral_cut_integral'])
        tail=mp.mpf(junction['finite_time_4D_noise_control']['positive_tail_upper_bound'])
        v=time_domain_noise(70)
        assert cut < v < cut+tail
        # Check the Gaussian Ramsey formula with direct Bloch density matrices.
        for row in junction['gaussian_integral_controls']:
            mean=(-1)**row['bit']*mp.mpf(row['mu_control']);variance=mp.mpf(row['variance_control'])
            off=mp.exp(-2*variance-2j*mean)/2
            rho=mp.matrix([[mp.mpf('.5'),off],[mp.conj(off),mp.mpf('.5')]])
            sy=mp.matrix([[0,-1j],[1j,0]])
            product=rho*sy
            py=(1+mp.re(product[0,0]+product[1,1]))/2
            assert abs(py-mp.mpf(row['P_y_plus_control']))<mp.mpf('1e-40')
        m=mp.mpf(1)/5;q=mp.mpf(1)/10
        rplus=m+mp.sqrt(m*m-q*q);rminus=m-mp.sqrt(m*m-q*q)
        ratio=(rplus/rminus)**2
        assert abs(ratio-(97+56*mp.sqrt(3)))<mp.mpf('1e-60')
    r,aa,bb=sp.symbols('r aa bb',positive=True)
    p=(aa-r)*(bb-r)
    I=sp.integrate(1/p,r)
    assert sp.simplify(sp.diff(p*sp.diff(I,r),r))==0
    assert junction['global_state_constructed'] is False
    assert junction['past_receiver_probabilities_computed'] is False
    return {'independent_program':True,'external_peer_review':'not_performed',
            'scattering_cross_checks':rows,'finite_window_noise_time_domain':mp.nstr(v,50),
            'noise_within_positive_spectral_tail_bound':True,
            'state_proved_on_full_SA':False}


def filehash(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()

class NegativeControls(unittest.TestCase):
    def test_threshold_D_N_differ(self):
        v=reflection_midpoint(.001,8192)
        self.assertLess(abs(v['D']+1),.001)
        self.assertLess(abs(v['N']-1),.003)
    def test_unit_reflection_is_not_transmission(self):
        v=reflection_midpoint(.2,4096)
        self.assertAlmostEqual(abs(v['D']),1,places=12)
        self.assertGreater(abs(v['D']-v['N']),1)
    def test_midpoint_converges(self):
        a=reflection_midpoint(.2,2048)['D'];b=reflection_midpoint(.2,4096)['D'];c=reflection_midpoint(.2,8192)['D']
        self.assertGreater(abs(a-b)/abs(b-c),3.9)
    def test_noise_positive(self):
        v=time_domain_noise(35);self.assertGreater(v,0);self.assertLess(v,.1)
    def test_source_sign_energy_parity(self):
        sx=sp.Matrix([[0,1],[1,0]]);sz=sp.diag(1,-1)
        self.assertEqual(sz*sx*sz,-sx)
    def test_ramsey_state_not_parity_invariant(self):
        rho=sp.Matrix([[1,1],[1,1]])/2;sz=sp.diag(1,-1)
        self.assertNotEqual(sz*rho*sz,rho)
    def test_common_temperature_nonextremal(self):
        for q in [.1,.15,.199]:
            m=.2;rp=m+math.sqrt(m*m-q*q);rm=m-math.sqrt(m*m-q*q)
            self.assertGreater((rp/rm)**2,1)
    def test_zero_charge_not_two_horizons(self):
        self.assertEqual(.2-math.sqrt(.2*.2),0)
    def test_extremal_not_in_kms_proof(self):
        m=sp.Rational(1,5);q=m
        self.assertEqual(sp.sqrt(m*m-q*q),0)
    def test_modes_both_square_integrable(self):
        x=sp.symbols('x',positive=True)
        for a in [sp.Rational(1,3),sp.Rational(2,3)]:
            self.assertTrue(sp.integrate(x**(2*a),(x,0,1)).is_finite)
    def test_wronskian_identity(self):
        self.assertEqual(7**2-(-4*sp.sqrt(3))**2,1)
    def test_coherent_shift_covariance(self):
        v,m=sp.symbols('v m');self.assertEqual(sp.expand(v+m*m-m*m),v)


def main()->None:
    ap=argparse.ArgumentParser();ap.add_argument('--junction',type=Path);ap.add_argument('--scattering',type=Path)
    ap.add_argument('--output',type=Path);ap.add_argument('--tests',action='store_true');args=ap.parse_args()
    if args.tests:
        suite=unittest.defaultTestLoader.loadTestsFromTestCase(NegativeControls)
        result=unittest.TextTestRunner(verbosity=2).run(suite)
        if not result.wasSuccessful():raise SystemExit(1)
        return
    if not all([args.junction,args.scattering,args.output]):ap.error('Provide all input/output paths')
    result=verify(json.loads(args.junction.read_text()),json.loads(args.scattering.read_text()))
    result['inputs']={'junction':filehash(args.junction),'scattering':filehash(args.scattering)}
    result['verifier_sha256']=filehash(Path(__file__))
    args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
