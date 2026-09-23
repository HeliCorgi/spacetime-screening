"""A normalized finite-energy negative-energy state of a genuine 3+1D field.

Canonical free scalar conventions follow Fewster--Eveson gr-qc/9805024.
This packet is an explicit calculation here, not a source supplied by that paper.
No local laboratory preparation or curved-wormhole completion is asserted.
"""
from __future__ import annotations

import platform
import sympy as s
import mpmath as mp


def exact_checks() -> None:
    t, r = s.symbols("t r", real=True)
    a, k = s.symbols("a k", positive=True)
    n, m = s.symbols("n m", real=True)
    # [a(k),a^dagger(p)]=delta^3(k-p). All transverse directions are integrated.
    f2 = a*a/s.pi/k*s.exp(-2*a*k)
    assert s.integrate(4*s.pi*k*k*f2, (k, 0, s.oo)) == 1
    assert s.simplify(s.integrate(4*s.pi*k**3*f2, (k, 0, s.oo))-1/a) == 0
    u = a/(s.pi*((a+s.I*t)**2+r*r))
    assert s.cancel(-s.diff(u, t, 2)+s.diff(u, r, 2)+2*s.diff(u, r)/r) == 0
    ub = s.conjugate(u)
    ut, ur, bt, br = s.diff(u, t), s.diff(u, r), s.diff(ub, t), s.diff(ub, r)
    rho = n*(ut*bt+ur*br)+m*(ut**2+bt**2+ur**2+br**2)/2
    t0r = n*(bt*ur+br*ut)+m*(ut*ur+bt*br)
    pr = rho
    pt = n*(ut*bt-ur*br)+m*(ut**2+bt**2-ur**2-br**2)/2
    # Prove the full 4D bilinear identity before substituting rational solutions.
    # This avoids expanding huge denominators, without weakening the identity.
    U, V = s.Function("U")(t, r), s.Function("V")(t, r)
    Ut, Ur, Vt, Vr = s.diff(U, t), s.diff(U, r), s.diff(V, t), s.diff(V, r)
    R, F, P = Ut*Vt+Ur*Vr, Ut*Vr+Vt*Ur, Ut*Vt-Ur*Vr
    LU = s.diff(U,t,2)-s.diff(U,r,2)-2*Ur/r
    LV = s.diff(V,t,2)-s.diff(V,r,2)-2*Vr/r
    assert s.expand(s.diff(R,t)-s.diff(F,r)-2*F/r-Ut*LV-Vt*LU) == 0
    assert s.expand(-s.diff(F,t)+s.diff(R,r)+2*(R-P)/r+Ur*LV+Vr*LU) == 0
    rho0 = 4*a*a*((n+m)*r*r+(n-m)*a*a)/(s.pi**2*(a*a+r*r)**4)
    assert s.cancel(rho.subs(t, 0)-rho0) == 0
    assert s.simplify(s.integrate(4*s.pi*r*r*rho0, (r, 0, s.oo))-n/a) == 0
    at_center = 4*(n-m)/(s.pi**2*a**4)
    assert s.simplify(rho.subs({r: 0, t: 0})-at_center) == 0
    assert s.simplify(pt.subs({r: 0, t: 0})-at_center) == 0
    z = s.symbols("z", real=True)
    nz, mz = 2*z*z/(1+z*z), s.sqrt(2)*z/(1+z*z)
    zopt = s.sqrt(3)-s.sqrt(2)
    assert s.simplify((nz-mz).subs(z, zopt)-(1-s.sqrt(s.Rational(3, 2)))) == 0
    assert s.simplify(s.diff(nz-mz, z).subs(z, zopt)) == 0
    # Compact sampler used for the curved-space DIAGNOSTIC in the other script.
    y = s.symbols("y", real=True)
    h = 2/s.sqrt(3)*s.cos(s.pi*y/2)**2
    assert s.integrate(h*h, (y, -1, 1)) == 1
    assert s.simplify(s.integrate(s.diff(h, y, 2)**2, (y, -1, 1))) == s.pi**4/3
    print("EXACT 4D: d^3k normalization, positive-frequency wave equation, full tensor conservation, energy=n/a.")
    print("STATE: (|0>+zeta|2_f>)/sqrt(1+zeta^2), zeta=sqrt(3)-sqrt(2) gives negative central density.")
    print("TENSOR CONTROL: at the packet center pr=pt=rho<0, not the Ellis target pt=-rho>0.")


def numerical(dps: int) -> tuple:
    with mp.workdps(dps):
        a = mp.mpf(1)
        z = mp.sqrt(3)-mp.sqrt(2)
        n = 2*z*z/(1+z*z)
        m = mp.sqrt(2)*z/(1+z*z)
        # Independent momentum integral, not substitution into the position formula.
        for t, r in ((mp.mpf(".2"), mp.mpf(".3")), (mp.mpf(".4"), mp.mpf(".7"))):
            numeric_u = a/mp.pi*mp.quad(
                lambda k: k*mp.exp(-(a+1j*t)*k)*mp.sin(k*r)/(k*r), [0, 1, mp.inf])
            analytic_u = a/(mp.pi*((a+1j*t)**2+r*r))
            assert abs(numeric_u-analytic_u) < mp.mpf(10)**(-(dps-8))
        def rho(t, r):
            den = (a+1j*t)**2+r*r
            ut = -2j*a*(a+1j*t)/(mp.pi*den**2)
            ur = -2*a*r/(mp.pi*den**2)
            return n*(abs(ut)**2+abs(ur)**2)+m*mp.re(ut**2+ur**2)
        for t in (mp.mpf(0), mp.mpf(".5")):
            energy = 4*mp.pi*mp.quad(lambda r: r*r*rho(t, r), [0, 1, mp.inf])
            assert abs(energy-n/a) < mp.mpf(10)**(-(dps-8))
        results = [rho(0, 0), n/a]
        print(f"dps={dps}; a=1: rho_center={mp.nstr(results[0], 32)}; total_energy={mp.nstr(n, 32)}")
        for width in (mp.mpf(".25"), mp.mpf(".5"), mp.mpf(1), mp.mpf(2)):
            # Gaussian timelike sampler, exact Minkowski theorem, not null-line QEI.
            w = lambda t: mp.exp(-(t/width)**2)/(mp.sqrt(mp.pi)*width)
            average = 2*mp.quad(lambda t: w(t)*rho(t, 0), [0, 1, mp.inf])
            bound = -mp.mpf(3)/(64*mp.pi**2*width**4)
            assert average >= bound
            # Optimize the entire vacuum+two-particle family for this time average.
            A = 2*mp.quad(lambda t: w(t)*4*a*a/(mp.pi**2*(a*a+t*t)**3), [0, 1, mp.inf])
            B = 2*mp.quad(lambda t: w(t)*4*a*a/mp.pi**2*mp.re((a+1j*t)**-6), [0, 1, mp.inf])
            family_min = A-mp.sqrt(A*A+B*B/2)
            assert family_min >= bound
            assert average >= family_min-mp.mpf(10)**(-(dps-8))
            results.extend((average, family_min))
            print(f"  width/a={width}; rho_avg={mp.nstr(average, 24)}; family_min={mp.nstr(family_min, 24)}; QEI={mp.nstr(bound, 24)}")
        # Spherical-wave compensation is retained, never clipped to the negative core.
        assert rho(0, 0) < 0 and rho(0, 2) > 0 and n/a > 0
        return tuple(results)


def main() -> None:
    print(f"Python {platform.python_version()}; SymPy {s.__version__}; mpmath {mp.__version__}")
    exact_checks()
    a, b = numerical(50), numerical(80)
    with mp.workdps(85):
        assert all(abs(x-y) < mp.mpf("1e-42") for x, y in zip(a, b))
    print("PASS 4D negative-state and timelike-QEI checks, independent d^3k and spatial-energy integrals.")
    print("This is a Minkowski-state candidate, NOT a self-consistent wormhole source or laboratory preparation.")


if __name__ == "__main__":
    main()
