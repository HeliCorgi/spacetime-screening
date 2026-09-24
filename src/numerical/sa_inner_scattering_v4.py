"""4D l=0 RN inner-static-region reflection: explicit boundary dependence.

The radial equation is the partial-wave equation of a 3+1D minimally coupled
massless scalar, not a 2D CFT. It is NOT the full two-shell scattering problem.
Dirichlet and Neumann endpoint extensions are inputs, not physical devices.
No crossing probability or SA quantum state is inferred from |reflection|=1.
"""
from __future__ import annotations
import argparse
import json
import hashlib
from pathlib import Path
import platform
import mpmath as mp

FREQUENCIES=('0.02','0.2','2')


def integrate(freq:str,dps:int,S:int=50) -> dict:
    """Taylor integration in s=-log(1-r/r_minus), regular at r=0.

    Both endpoint branches have finite bulk radial energy. The selected real
    separated boundary conditions have zero Klein-Gordon boundary flux.
    """
    if dps<40 or S<20: raise ValueError('Insufficient precision or horizon range')
    with mp.workdps(dps):
        m=mp.mpf('0.2');q=mp.mpf('0.1')
        d=mp.sqrt(m*m-q*q);rp=m+d;rm=m-d
        k=d/(rm*rm);w=mp.mpf(freq)*k;nu=w/(2*k)
        if w<=0:raise ValueError('Positive frequency required')
        # Explicit power-series propagator for canonical (phi, p=r^2 f phi_r).
        # Coefficients are expanded analytically, avoiding numerical differentiation.
        from math import comb
        P=76 if dps==50 else 96
        step=mp.mpf('0.5');state=[mp.mpf(0),rp,mp.mpf(1),mp.mpf(0)]
        for panel in range(2*S):
            h0=rm*mp.exp(-panel*step);gap=rp-rm
            hs=[h0]
            for n in range(1,P): hs.append(-hs[-1]/n)
            aa=[1/(gap+h0)]
            for n in range(1,P):
                aa.append(-sum(hs[j]*aa[n-j] for j in range(1,n+1))/(gap+h0))
            r4=[]
            for n in range(P):
                r4.append(sum((-1)**j*comb(4,j)*rm**(4-j)*h0**j*(-j)**n
                              for j in range(5))/mp.factorial(n))
            bb=[-w*w*sum(aa[j]*r4[n-j] for j in range(n+1)) for n in range(P)]
            updated=[]
            for offset in (0,2):
                c=[state[offset]];dcoef=[state[offset+1]]
                for n in range(P):
                    c.append(sum(aa[j]*dcoef[n-j] for j in range(n+1))/(n+1))
                    dcoef.append(sum(bb[j]*c[n-j] for j in range(n+1))/(n+1))
                updated.extend([mp.polyval(list(reversed(c)),step),
                                mp.polyval(list(reversed(dcoef)),step)])
            state=updated
        r=rm*(1-mp.exp(-S))
        Y=[state[0],state[1]/(rp-r),state[2],state[3]/(rp-r)];out={}
        for label,i in [('D',0),('N',2)]:
            incoming=(Y[i]-Y[i+1]/(1j*nu))*mp.exp(1j*nu*S)/2
            outgoing=(Y[i]+Y[i+1]/(1j*nu))*mp.exp(-1j*nu*S)/2
            reflect=outgoing/incoming
            assert abs(abs(reflect)-1)<mp.mpf('1e-35')
            out[label]={'real':mp.nstr(mp.re(reflect),48),'imag':mp.nstr(mp.im(reflect),48),
                        'phase_s_radians':mp.nstr(mp.arg(reflect),35)}
        # In (phi,phi_s/nu) the asymptotic generator is a rotation.
        # ||E(s)|| <= C exp(-s); relative amplitude error <= exp(C exp(-S))-1.
        qr=rm/(rp-rm);C=qr+nu*(4+2*qr+qr*qr)
        eps=mp.expm1(C*mp.exp(-S));bound=2*eps/(1-eps)
        r=rm*(1-mp.exp(-S));det=Y[0]*Y[3]-Y[1]*Y[2]
        assert abs(det+rp/(rp-r))<mp.mpf('1e-30'), (freq,dps,mp.nstr(det+rp/(rp-r),20))
        out.update({'omega_over_kappa_minus':freq,'dps':dps,'s_endpoint':S,
                    'remaining_horizon_tail_bound':mp.nstr(bound,20),
                    'wronskian_error':mp.nstr(abs(det+rp/(rp-r)),10)})
        return out


def main()->None:
    parser=argparse.ArgumentParser();parser.add_argument('--output');args=parser.parse_args()
    rows=[]
    for freq in FREQUENCIES:
        lo=integrate(freq,50);hi=integrate(freq,80)
        with mp.workdps(90):
            diff=max(abs(mp.mpf(lo[bc][c])-mp.mpf(hi[bc][c])) for bc in ('D','N') for c in ('real','imag'))
            assert diff<mp.mpf('1e-40'),(freq,diff)
            assert sum((mp.mpf(hi['D'][c])-mp.mpf(hi['N'][c]))**2 for c in ('real','imag'))>mp.mpf('1e-4')
            hi['precision_comparison_difference']=mp.nstr(diff,15)
        rows.append(hi)
    result={'model':'RN 0<r<r_minus, massless minimal 4D l=0 partial wave',
            'm':'.2','charge':'.1','horizon_normalization':'original RN Killing time',
            'boundary_conditions':{'D':'phi(0)=0','N':'r^2 f phi_r(0)=0'},
            'phase_convention':'basis exp(+-i*(omega/(2*kappa_minus))*s)',
            'reflection_is_not_a_probability':True,'not_full_SA_horizon_crossing':True,
            'past_receiver_probability':None,
            'errors':'Tail bound analytic; ODE errors checked by precision and independent convergence, not interval-certified.',
            'runtime':{'python':platform.python_version(),'mpmath':mp.__version__},'rows':rows}
    result['generator_sha256']=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    text=json.dumps(result,indent=2,ensure_ascii=False)
    if args.output:
        Path(args.output).parent.mkdir(parents=True,exist_ok=True);Path(args.output).write_text(text+'\n')
    print(text)

if __name__=='__main__':main()
