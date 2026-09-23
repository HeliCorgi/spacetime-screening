"""3+1D semiclassical initial data for a normal squeezed dipole packet.

First order in G, not an exact nonlinear spacetime or laboratory preparation.
Flat-space packet stress, conformally flat time-symmetric R^3 initial geometry,
and all initial Einstein equations through the initial acceleration.
Independent entrypoint: no imports from other repository scripts.
References and domain: notes/four-dimensional-source-completion.md.
"""
from __future__ import annotations

import platform
import sympy as sp
import mpmath as mp


def potentials(s, n, m, atan, pi):
    """Dimensionless delta psi = (lP/a)^2 [U0+U2 P2(cos theta)]."""
    D = 1+s*s
    u0 = (2*n/pi*(atan(s)/s+(9*s**4+24*s*s+11)/(9*D**3))
          +8*m*(1-11*s*s)/(45*pi*D**4))
    u2 = (2*n/(3*pi*s**3)*atan(s)
          +2*n*(3*s**4-8*s*s-3)/(9*pi*s*s*D**3)
          -2*m/(15*pi*s**3)*atan(s)
          +2*m*(-3*s**6-91*s**4+11*s*s+3)/(45*pi*s*s*D**4))
    return u0, u2


def densities(s, n, m, pi):
    D = 1+s*s
    common = 8/pi**2
    r0 = common*((n+m)/D**4 + 8*s*s*((n+m)*s*s+n-3*m)/(3*D**6))
    r2 = common*16*s*s*((n+m)*s*s+n-3*m)/(3*D**6)
    return r0, r2


def exact_checks() -> None:
    s = sp.symbols('s', positive=True)
    n, m = sp.symbols('n m', real=True)
    rhos = densities(s, n, m, sp.pi)
    us = potentials(s, n, m, sp.atan, sp.pi)
    for l, rho, u in zip((0, 2), rhos, us):
        residual = sp.diff(u,s,2)+2*sp.diff(u,s)/s-l*(l+1)*u/s**2+2*sp.pi*rho
        assert sp.simplify(residual) == 0
    assert sp.limit(us[0],s,0) == (200*n+8*m)/(45*sp.pi)
    assert sp.limit(us[1],s,0) == 0
    assert sp.limit(s*us[0],s,sp.oo) == n
    assert sp.limit(s*us[1],s,sp.oo) == 0
    assert sp.simplify(sp.limit(s*us[0],s,sp.oo)-n) == 0

    # Density multipoles from the actual dipole derivatives at t=0.
    angle = sp.symbols('angle', real=True)
    D = 1+s*s
    source = 8/sp.pi**2*((n+m)/D**4
             +8*s*s*angle**2*((n+m)*s*s+n-3*m)/D**6)
    assert sp.simplify(source-rhos[0]-rhos[1]*(3*angle**2-1)/2) == 0
    # Coefficients are linear in angle^2; the endpoint bounds establish the
    # radial envelope in all directions, not just the sampled values below.
    q2 = sp.symbols('q2', nonnegative=True)
    normal = (1+q2)**2+8*q2*(1+q2)
    anomalous = (1+q2)**2+8*q2*(q2-3)
    assert sp.expand(9*(1+q2)**2-normal) == 8+8*q2
    assert sp.expand(9*(1+q2)**2-anomalous) == 8+40*q2
    assert sp.expand(9*(1+q2)**2+anomalous
                     -18*(q2-sp.Rational(1,9))**2-sp.Rational(88,9)) == 0

    # Full initial Einstein equations: lapse=1, shift=0, K_ij=0.
    # h_ij=4 u delta_ij, dot h_ij=0. H denotes the Hessian of u.
    G, rho = sp.symbols('G rho', real=True)
    H = sp.Matrix(3,3,lambda i,j:sp.Symbol(f'H{min(i,j)}{max(i,j)}'))
    P = sp.Matrix(3,3,lambda i,j:sp.Symbol(f'P{min(i,j)}{max(i,j)}'))
    lap = sp.trace(H); stress_trace = sp.trace(P)
    acceleration = 4*H + 16*sp.pi*G*P - 8*sp.pi*G*stress_trace*sp.eye(3)
    ric3 = -2*H-2*lap*sp.eye(3)
    ric00 = -sp.trace(acceleration)/2
    ricij = ric3+acceleration/2
    scalar4 = -ric00+sp.trace(ricij)
    e00 = ric00+scalar4/2
    eij = ricij-scalar4*sp.eye(3)/2
    constraint = {H[2,2]:-2*sp.pi*G*rho-H[0,0]-H[1,1]}
    assert sp.expand((e00-8*sp.pi*G*rho).subs(constraint)) == 0
    assert (eij-8*sp.pi*G*P).applyfunc(lambda e:sp.expand(e.subs(constraint))) == sp.zeros(3)
    # G_0i=T_0i=0: spatial derivatives are real, the time derivative imaginary.
    print('EXACT 3+1D: Hamiltonian and momentum constraints; all initial Einstein components including acceleration.')
    print('EXACT: regular l=0,2 Newton potentials; ADM energy=2*n/a>0; no spatial topology change.')
    integral = sp.integrate(s/(1+s*s)**4,(s,0,sp.oo))
    assert integral == sp.Rational(1,6)
    assert sp.simplify(sp.Rational(1,2)*4*sp.pi*72/sp.pi**2*integral) == 24/sp.pi
    print('BOUND: sup|delta psi| <= (24/pi)*(n+|m|)*(lP/a)^2 from a positive radial envelope.')


def numerical_checks(dps: int) -> tuple[mp.mpf,...]:
    with mp.workdps(dps):
        sq=mp.mpf('.5'); n=mp.sinh(sq)**2; m=-mp.sinh(sq)*mp.cosh(sq)
        records=[]
        for r in (mp.mpf('.25'),mp.mpf(1),mp.mpf(3),mp.mpf(10)):
            U=potentials(r,n,m,mp.atan,mp.pi)
            for i,l in enumerate((0,2)):
                def f(x):
                    return densities(x,n,m,mp.pi)[i]
                inner=mp.quad(lambda x:x**(l+2)*f(x),[0,r])
                outer=mp.quad(lambda x:x**(1-l)*f(x),[r,2*r,mp.inf])
                result=2*mp.pi/(2*l+1)*(inner/r**(l+1)+r**l*outer)
                assert abs(result-U[i])<mp.mpf(10)**(-dps+9)
                records.append(+result)
            for costheta in (mp.mpf(-1),mp.mpf(0),mp.mpf('.7'),mp.mpf(1)):
                value=U[0]+U[1]*(3*costheta**2-1)/2
                assert abs(value)<24*(n+abs(m))/mp.pi
        G=mp.mpf('6.67430e-11');c=mp.mpf('299792458');hbar=mp.mpf('1.054571817e-34')
        lp=mp.sqrt(hbar*G/c**3);b=mp.mpf(1)
        a=(32*(1-mp.exp(-2*sq))/mp.pi)**mp.mpf('.25')*mp.sqrt(lp*b)
        amplitude_bound=24*(n+abs(m))/mp.pi*lp**2/a**2
        central=(200*n+8*m)/(45*mp.pi)*lp**2/a**2
        energy=2*n*hbar*c/a
        assert amplitude_bound<mp.mpf('1e-30')
        print(f'dps={dps}; 1m point-match, squeeze=.5: a={mp.nstr(a,15)}m')
        print(f'  all-space |delta psi| upper={mp.nstr(amplitude_bound,25)}, delta psi(origin)={mp.nstr(central,25)}')
        print(f'  ADM leading energy={mp.nstr(energy,15)}J; this is a tiny R^3 perturbation, not a wormhole.')
        return tuple(records)+(+amplitude_bound,+central,+energy)


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}; mpmath {mp.__version__}')
    exact_checks()
    low=numerical_checks(50);high=numerical_checks(80)
    with mp.workdps(80):
        for a,b in zip(low,high):
            assert abs(a-b)<mp.mpf('1e-40')*max(abs(b),mp.mpf('1e-60'))
    print('PASS independent Green integrals and local initial Einstein checks.')
    print('Order-G initial data only: no full evolution, fluctuation control, local pump or backward receiver law.')


if __name__ == '__main__':
    main()
