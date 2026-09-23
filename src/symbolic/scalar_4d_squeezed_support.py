"""3+1D normal scalar: local Ellis stress match is not a supported wormhole.

Analytic construction and independent checks; no finite-dimensional CCR cutoff.
References and limitations: notes/four-dimensional-source-completion.md.
The packet state has spatial tails. The oscillator control is a comparison,
not a local preparation of the whole four-dimensional field.
"""
from __future__ import annotations

import platform
import sympy as sp
import mpmath as mp


def exact_checks() -> None:
    t, x, y, z = sp.symbols('t x y z', real=True)
    a = sp.symbols('a', positive=True)
    coords = (t, x, y, z)
    sign = (-1, 1, 1, 1)
    den = (a + sp.I*t)**2 + x*x + y*y + z*z
    seed = a/(sp.pi*den)
    packet = -sp.sqrt(2)*a*sp.diff(seed, x)
    box = sum(sign[i]*sp.diff(seed, coords[i], 2) for i in range(4))
    assert sp.factor(box) == 0
    assert sp.simplify(packet-2*sp.sqrt(2)*a*a*x/(sp.pi*den**2)) == 0
    assert sp.diff(sp.factor(box), x) == 0  # Box commutes with partial_x.
    k = sp.symbols('k', positive=True)
    density = 8*a**4*k**3*sp.exp(-2*a*k)/3
    assert sp.integrate(density, (k, 0, sp.oo)) == 1
    assert sp.integrate(k*density, (k, 0, sp.oo)) == 2/a

    # General polarization identity for conservation, not a pointwise sample.
    u = sp.symbols('u0:4'); v = sp.symbols('v0:4')
    hu = sp.MutableDenseMatrix(4, 4, lambda i,j: sp.Symbol(f'U{min(i,j)}{max(i,j)}'))
    hv = sp.MutableDenseMatrix(4, 4, lambda i,j: sp.Symbol(f'V{min(i,j)}{max(i,j)}'))
    for j in range(4):
        div = sum(sign[i]*(hu[i,i]*v[j]+u[i]*hv[i,j]
                           +hv[i,i]*u[j]+v[i]*hu[i,j])/2 for i in range(4))
        div -= sum(sign[i]*(hu[j,i]*v[i]+u[i]*hv[j,i])/2 for i in range(4))
        expected = (sum(sign[i]*hu[i,i] for i in range(4))*v[j]
                    +sum(sign[i]*hv[i,i] for i in range(4))*u[j])/2
        assert sp.expand(div-expected) == 0

    origin = {t:0,x:0,y:0,z:0}
    grad = sp.Matrix([sp.diff(packet,c).subs(origin) for c in coords])
    assert grad == sp.Matrix([0,2*sp.sqrt(2)/(sp.pi*a*a),0,0])
    n, m = sp.symbols('n m', real=True)
    eta = sp.diag(*sign)
    stress = 2*(n+m)*(grad*grad.T-eta*(grad.T*eta*grad)[0]/2)
    assert (stress-8*(n+m)/(sp.pi**2*a**4)*sp.diag(1,1,-1,-1)).applyfunc(sp.simplify) == sp.zeros(4)
    r = sp.symbols('r', positive=True)
    assert sp.simplify((sp.cosh(2*r)-1-sp.sinh(2*r))-(sp.exp(-2*r)-1)) == 0

    # A four-dimensional field on the complete 4D ray (t,x,y,z)=(s,s,0,0).
    ray = sp.simplify(packet.subs({x:t,y:0,z:0}))
    deriv = sp.diff(ray,t)
    expected_mod = 8/(sp.pi**2*(a*a+4*t*t)**2)
    assert sp.simplify(sp.expand_complex(deriv*sp.conjugate(deriv))-expected_mod) == 0
    assert sp.integrate(expected_mod,(t,-sp.oo,sp.oo)) == 2/(sp.pi*a**3)
    # deriv**2 has poles only in the upper half-plane and decays as t^-4.
    # Closing below gives zero anomalous full-ray integral.

    # Positive-frequency quarter-cycle control of one selected oscillator.
    w0,w1 = sp.symbols('w0 w1', positive=True)
    M = sp.Matrix([[0,1/w1],[-w1,0]])
    J = sp.Matrix([[0,1],[-1,0]])
    assert M*J*M.T == J
    Vin = sp.diag(1/(2*w0),w0/2)
    Vout = M*Vin*M.T
    assert Vout.det() == sp.Rational(1,4)
    work = (Vout[1,1]+w0*w0*Vout[0,0])/2-w0/2
    assert sp.factor(work) == (w0-w1)**2*(w0+w1)**2/(4*w0*w1*w1)
    print('EXACT: continuum d^3k norm, mean frequency, Box_4 and tensor conservation.')
    print('EXACT: squeezed dipole has diag(-A,-A,A,A) at one event, with positive total energy.')
    print('FULL-RAY ANEC = 4*sinh(r)^2/(pi*a^3)>0; local stress matching is not throat support.')
    print('CONTROL: a positive oscillator Hamiltonian prepares the covariance with positive work.')


def numerical_checks(dps: int) -> tuple[mp.mpf, ...]:
    with mp.workdps(dps):
        a=mp.mpf(1); sq=mp.mpf('0.5')
        n=mp.sinh(sq)**2; m=-mp.sinh(sq)*mp.cosh(sq)
        def check(v: mp.mpf, target: mp.mpf) -> None:
            assert abs(v-target) < mp.mpf(10)**(-dps+8)*max(1,abs(target))
        check(mp.quad(lambda k:8*a**4*k**3*mp.exp(-2*a*k)/3,[0,1,mp.inf]),1)
        C=2*mp.sqrt(2)*a*a/mp.pi
        dtint=mp.quad(lambda R:4*mp.pi/3*16*a*a*C*C*R**4/(a*a+R*R)**6,[0,1,mp.inf])
        dxint=mp.quad(lambda R:4*mp.pi*C*C*R*R*((a*a+R*R)**-4
                        +R*R/3*(-8*(a*a+R*R)**-5+16*R*R*(a*a+R*R)**-6)),[0,1,mp.inf])
        check(dtint,1/a);check(dxint,1/a)
        energy=n*(dtint+dxint)+m*(dxint-dtint)
        check(energy,2*n/a)
        def derivative(s: mp.mpf) -> mp.mpc:
            return 2*mp.sqrt(2)*a*a/mp.pi*(a*a-2j*a*s)/(a*a+2j*a*s)**3
        raynum=mp.quad(lambda s:2*n*abs(derivative(s))**2+2*m*mp.re(derivative(s)**2),
                       [-mp.inf,-1,0,1,mp.inf])
        check(raynum,4*n/(mp.pi*a**3))
        center=-4*(1-mp.exp(-2*sq))/(mp.pi**2*a**4)
        halfwidth=a*mp.tan(mp.acos(mp.tanh(sq))/8)
        d=lambda tt:2*mp.sqrt(2)*a*a/(mp.pi*(a+1j*tt)**4)
        check(n*abs(d(halfwidth))**2+m*mp.re(d(halfwidth)**2),0)
        # Nominal SI scales: constants are not known to 80 physical digits.
        G=mp.mpf('6.67430e-11');hbar=mp.mpf('1.054571817e-34');c=mp.mpf('299792458')
        lp=mp.sqrt(hbar*G/c**3);b=mp.mpf(1)
        width=(32*(1-mp.exp(-2*sq))/mp.pi)**mp.mpf('.25')*mp.sqrt(lp*b)
        central_duration=2*width*mp.tan(mp.acos(mp.tanh(sq))/8)/c
        weak=2*n*lp*lp/(width*width)
        print(f'dps={dps}; a=1,r=.5: rho_center={mp.nstr(center,32)}, E={mp.nstr(energy,32)}')
        print(f'  full null integral={mp.nstr(raynum,32)}; central negative half-width/a={mp.nstr(halfwidth/a,20)}')
        print(f'  1m POINT-matching width={mp.nstr(width,12)}m; central negative duration={mp.nstr(central_duration,12)}s')
        print(f'  compactness proxy G*E/(c^4*a)={mp.nstr(weak,12)}; not a topology-changing solution')
        return tuple(+v for v in (center,energy,raynum,halfwidth,width,central_duration,weak))


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}; mpmath {mp.__version__}')
    exact_checks()
    low=numerical_checks(50);high=numerical_checks(80)
    with mp.workdps(80):
        for a,b in zip(low,high):
            assert abs(a-b) < mp.mpf('1e-40')*max(abs(b),mp.mpf('1e-60'))
    print('PASS. No full four-dimensional apparatus, curved-space state, or past channel is claimed.')


if __name__ == '__main__':
    main()
