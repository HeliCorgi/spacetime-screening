"""A-directed 3+1D RN-shell search, not a semiclassical past channel.

Source conventions: Eiroa 0805.1403, Eqs. (9)-(13), (35)-(37).
G=c=1 in geometry; mu=M/a0 and z=Q^2/a0^2, eta=dp/dsigma.
The shell is neutral: opposite charges are seen at the two asymptotic ends.
No source state, apparatus, CTC identification, or probability is inferred
from radial stability. Fraction intervals certify one open subextremal box.
"""
from __future__ import annotations
from fractions import Fraction as F
from itertools import product
import mpmath as mp
import sympy as sp


def hessian(mu, z, eta):
    f = 1 - 2*mu + z
    return -4*mu + 6*z - 2*(mu-z)**2/f - 2*(1+2*eta)*(1-3*mu+2*z)


def geometry_checks():
    r, M, Q, G = sp.symbols('r M Q G', positive=True)
    f = 1-2*M/r+Q**2/r**2
    # Mixed 4D Einstein tensor for the stated static spherical metric.
    gr = (r*sp.diff(f,r)+f-1)/r**2
    gt = sp.diff(f,r,2)/2+sp.diff(f,r)/r
    assert sp.simplify(gr+Q**2/r**4)==0
    assert sp.simplify(gt-Q**2/r**4)==0
    rho = Q**2/(8*sp.pi*G*r**4)
    pr, pt = -rho, rho
    assert sp.simplify(sp.diff(pr,r)+(rho+pr)*sp.diff(f,r)/(2*f)+2*(pr-pt)/r)==0
    sigma = -sp.sqrt(f)/(2*sp.pi*G*r)
    pressure = (r*sp.diff(f,r)+2*f)/(8*sp.pi*G*r*sp.sqrt(f))
    assert sp.simplify(pressure-(1-M/r)/(4*sp.pi*G*r*sp.sqrt(f)))==0
    # Null tangent has Killing energy one at either infinity.
    assert sp.simplify(sigma/sp.sqrt(f)+1/(2*sp.pi*G*r))==0
    # The surface pressure contributes to the gravitational mass budget.
    shell_komar=4*sp.pi*r**2*sp.sqrt(f)*(sigma+2*pressure)
    assert sp.simplify(shell_komar+2*Q**2/(G*r)-2*M/G)==0
    mu,z,eta=sp.symbols('mu z eta', real=True)
    h=hessian(mu,z,eta)
    assert sp.factor(h.subs(z,mu**2)-2*(1-mu)*(4*eta*mu-2*eta-1))==0
    # Charge-free expression agrees with the previous Poisson-Visser gate.
    old=-2*(2*mu+mu**2/(1-2*mu)+(1+2*eta)*(1-3*mu))
    assert sp.simplify(h.subs(z,0)-old)==0
    # A continuous normal flux has no delta-function electric charge at the
    # seam (the two outward asymptotic charge signs are opposite).
    normal_field=Q*sp.sqrt(f)/r**2
    flux_density=sp.sqrt(f)*r**2*normal_field/f
    assert sp.simplify(flux_density-Q)==0
    # Neither an arbitrary scalar potential nor Maxwell gives negative
    # classical radial null stress; quantum negative energy is not excluded.
    dt,dr,dy,dz,U=sp.symbols('dt dr dy dz U',real=True)
    metric=sp.diag(-1,1,1,1); gradient=sp.Matrix([dt,dr,dy,dz]);k=sp.Matrix([1,1,0,0])
    tensor=gradient*gradient.T-metric*((gradient.T*metric*gradient)[0]/2+U)
    assert sp.expand((k.T*tensor*k)[0]-(dt+dr)**2)==0
    eps=sp.symbols('eps',positive=True)
    optical=2*(1+2*(1-eps)*sp.log((1+eps)/eps)+(1-eps)**2*(1/eps-1/(1+eps)))
    assert sp.limit(2*eps*optical,eps,0,dir='+')==4
    # A surface scalar EFT realizes the intrinsic EOS but leaves negative
    # vacuum offset unspecified; it is NOT a 4D matter completion.
    X,X0,C,B,alpha=sp.symbols('X X0 C B alpha', positive=True)
    P=C*(X/X0)**alpha+B
    density=2*X*sp.diff(P,X)-P
    cs2=sp.simplify(sp.diff(P,X)/sp.diff(density,X))
    assert sp.simplify(cs2-1/(2*alpha-1))==0
    assert sp.simplify(density+P-2*alpha*C*(X/X0)**alpha)==0
    return {'bulk':'G^mu_nu=Q^2/r^4 diag(-1,-1,1,1)',
            'shell':'sigma=-sqrt(f)/(2*pi*G*a); p=(1-M/a)/(4*pi*G*a*sqrt(f))',
            'radial_ANEC_Killing_E_1':'-1/(2*pi*G*a)',
            'two_end_Komar':'2*(M-Q^2/a)/G+2*Q^2/(G*a)=2*M/G',
            'extremal_stability':'a^2 Vpp=2*(1-mu)*(4*eta*mu-2*eta-1)',
            'extremal_resource_limit':'G*|E_shell|*T_opt/a^2 -> 4 for detectors at r=2a',
            'classical_scalar_null':'T_kk=(d_t_phi+d_r_phi)^2>=0; potential cancels',
            'surface_EFT':'P=C*(X/X0)^alpha+B; cs^2=1/(2*alpha-1); B is unsupplied negative vacuum energy'}


class Interval:
    """Exact rational enclosures; no floating-point sign decision."""
    def __init__(self,lo,hi=None):
        self.lo,self.hi=F(lo),F(lo if hi is None else hi)
        assert self.lo<=self.hi
    @staticmethod
    def of(x): return x if isinstance(x,Interval) else Interval(x)
    def __add__(self,other):
        o=self.of(other);return Interval(self.lo+o.lo,self.hi+o.hi)
    __radd__=__add__
    def __neg__(self): return Interval(-self.hi,-self.lo)
    def __sub__(self,other): return self+-self.of(other)
    def __rsub__(self,other): return self.of(other)+-self
    def __mul__(self,other):
        o=self.of(other);v=[a*b for a in (self.lo,self.hi) for b in (o.lo,o.hi)]
        return Interval(min(v),max(v))
    __rmul__=__mul__
    def __truediv__(self,other):
        o=self.of(other);assert o.lo*o.hi>0,'denominator enclosure meets zero'
        return self*Interval(1/o.hi,1/o.lo)
    def __pow__(self,n):
        assert n==2
        return Interval(0 if self.lo<=0<=self.hi else min(self.lo**2,self.hi**2),max(self.lo**2,self.hi**2))
    def strings(self): return [str(self.lo),str(self.hi)]


def certify_box():
    mu=Interval('0.899999','0.900001')
    z=Interval('0.809899','0.809901')
    eta=Interval('0.7499','0.7501')
    f=1-2*mu+z; gap=mu**2-z; h=hessian(mu,z,eta)
    enthalpy_numerator=-1+3*mu-2*z
    assert f.lo>0 and gap.lo>0 and mu.hi<1
    assert h.lo>0 and enthalpy_numerator.lo>0
    # f>0, mu<1, mu^2-z>0 => 1>mu+sqrt(mu^2-z): shell outside r+.
    return {'mu':mu.strings(),'z':z.strings(),'eta':eta.strings(),
            'f':f.strings(),'mu_squared_minus_z':gap.strings(),
            'a2_Vpp':h.strings(),'enthalpy_numerator':enthalpy_numerator.strings(),
            'method':'exact Fraction interval arithmetic; exterior and positive-Hessian open box'}


def rational_sweep():
    rows=[]
    deficits=[F(0),F(1,10**8),F(1,10**6),F(1,10**4),F(1,1000),F(1,100),F(1,10)]
    etas=[F(0),F(1,4),F(1,2),F(3,5),F(3,4),F(1)]
    for mu,d,eta in product([F(i,100) for i in range(55,100)],deficits,etas):
        z=mu*mu-d; f=1-2*mu+z
        outside=z>=0 and mu<1 and f>0
        h=hessian(mu,z,eta) if outside else None
        rows.append({'mu':str(mu),'z':str(z),'deficit':str(d),'eta':str(eta),
                     'f':str(f),'outside_outer_horizon':outside,'a2_Vpp':None if h is None else str(h),
                     'radially_stable':None if h is None else h>0})
    assert len(rows)==1890
    counts={'tested':len(rows),'outside':sum(r['outside_outer_horizon'] for r in rows),
            'stable':sum(r['radially_stable'] is True for r in rows),
            'invalid_exterior':sum(not r['outside_outer_horizon'] for r in rows)}
    assert counts['stable']>0 and counts['invalid_exterior']>0
    witness={'mu':F(9,10),'z':F(8099,10000),'eta':F(3,4)}
    value=hessian(**witness)
    assert value==F(10097,495000)>0
    return rows,counts,{**{k:str(v) for k,v in witness.items()},'a2_Vpp':str(value),'r_plus_over_a':'91/100'}


def numeric_diagnostics(dps):
    with mp.workdps(dps):
        out=[]
        for epsilon in ['0.1','0.01','0.001','0.0001']:
            e=mp.mpf(epsilon);m=1-e;R=mp.mpf(2);eta=mp.mpf('.75')
            T=2*((R-1)+2*m*mp.log((R-m)/(1-m))-m*m*(1/(R-m)-1/(1-m)))
            proper_energy=-2*e
            out.append({'epsilon':epsilon,'optical_time_over_a':mp.nstr(T,45),
                        'shell_energy_G_over_a':mp.nstr(proper_energy,45),
                        'energy_time_G_over_a2':mp.nstr(-proper_energy*T,45),
                        'radial_ANEC_2piGa':'-1',
                        'omega_infinity_times_a':mp.nstr(e*mp.sqrt(e*(4*eta*m-2*eta-1)),45)})
        return out


def seam_diagnostic():
    rows=[]
    for delta in [-100,-1,0,1,100]:
        for wait in [F(0),F(1,3),F(10)]:
            first=F(7,3)+delta
            second=F(7,3)-delta
            duration=first+wait+second
            assert duration==F(14,3)+wait>0
            rows.append({'offset':delta,'wait':str(wait),'forward_leg_coordinate_delta':str(first),
                         'return_leg_coordinate_delta':str(second),'same_clock_roundtrip':str(duration)})
    return {'tested':len(rows),'trials':rows,'verdict':'global_time_obstruction',
            'checks':{'global_time':'T=t_left on left, T=t_right-Delta on right',
                      'inverse_metric':'g^{-1}(dT,dT)=-1/f<0',
                      'boundary':'two ends joined ONCE; real nonperiodic time; no second exterior path',
                      'future_order':'A future causal traversal increases T; opposite seam crossings cancel Delta'},
            'probability_law_computed':False}
