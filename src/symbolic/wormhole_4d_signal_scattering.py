"""4D spherical thin-shell throat: partial waves, finite source, receiver test.

Metric: ds^2=-dt^2+dx^2+(b+|x|)^2 dOmega^2, minimal scalar.
The one-throat scattering block has two exterior sides. Putting both mouths
in one exterior and adding a time shift requires a DIFFERENT global gluing.
No stationary scattering formula here is a post-CTC initial-value solution.
Sources: Visser 1989 doi:10.1103/PhysRevD.39.3182; MTY 1988
10.1103/PhysRevLett.61.1446. The explicit matching below is rederived.
"""
from __future__ import annotations

import platform
import sympy as s
import mpmath as mp


def p_jost(angular_l: int, z):
    if not isinstance(angular_l, int) or angular_l < 0:
        raise ValueError("angular_l must be a nonnegative integer")
    return sum(s.I**k*s.factorial(angular_l+k)/(
        s.factorial(k)*s.factorial(angular_l-k)*(2*z)**k)
        for k in range(angular_l+1))


def exact_checks() -> None:
    t, x, b, q = s.symbols("t x b q", real=True, positive=True)
    r = s.Function("r")(x)
    chi = s.Function("chi")(t, x)
    ell = s.symbols("ell", real=True)
    field = chi/r
    wave = -s.diff(field,t,2)+s.diff(field,x,2)+2*s.diff(r,x)/r*s.diff(field,x)-ell*(ell+1)/r**2*field
    expected = -s.diff(chi,t,2)+s.diff(chi,x,2)-(s.diff(r,x,2)/r+ell*(ell+1)/r**2)*chi
    assert s.simplify(r*wave-expected) == 0
    # For r=b+|x|, r''/r=2 delta(x)/b. Thus u is continuous and [u']=2u/b.
    for angular_l in range(5):
        P = p_jost(angular_l,q)
        D = (s.I*q-1)*P+q*s.diff(P,q)
        trans = s.cancel(s.I*q/(P*D))
        refl = s.cancel(trans-s.conjugate(P)/P)
        assert s.simplify(trans*s.conjugate(trans)+refl*s.conjugate(refl)-1) == 0
        # Jost solution solves the full 4D partial-wave exterior equation.
        R = s.symbols("R", positive=True)
        f = s.exp(s.I*q*(R-1))*p_jost(angular_l,q*R)
        assert s.simplify(s.diff(f,R,2)+(q*q-angular_l*(angular_l+1)/R**2)*f) == 0
        if angular_l == 0:
            assert s.simplify(trans*s.conjugate(trans)-q*q/(1+q*q)) == 0
        if angular_l == 1:
            assert s.simplify(trans*s.conjugate(trans)-q**6/((q*q+1)*(q**4+4))) == 0
    print("EXACT 4D: radial operator retains the sphere's centrifugal and r''/r terms.")
    print("Thin shell gives [u_x]=2u/b, NOT an arbitrarily transparent boundary.")
    print("EXACT flux conservation for l=0..4; eta_0=q^2/(1+q^2).")
    # Laplace domain kernel: h(t)=delta(t)-exp(-t)theta(t), time in b/c units.
    p = s.symbols("p", positive=True)
    assert s.simplify(1-1/(p+1)-p/(p+1)) == 0
    tau, v = s.symbols("tau v", real=True)
    z = s.integrate(s.exp(-(tau-v))*s.sin(s.pi*v)**2,(v,0,tau))
    assert s.simplify(s.diff(z,tau)+z-s.sin(s.pi*tau)**2) == 0
    assert s.simplify(z.subs(tau,0)) == 0
    # Required Israel layer cannot be replaced by a no-jump scalar boundary.
    strength = s.symbols("strength", real=True)
    delta_trans = 2*s.I*q/(2*s.I*q-strength)
    assert s.simplify(delta_trans.subs(strength,0)) == 1
    assert s.simplify((delta_trans*s.conjugate(delta_trans)).subs({strength:2,q:1})) == s.Rational(1,2)
    print("FINITE-SOURCE control: impulse response has zero support before t=0; packet peaks are not fronts.")


def numerical(dps: int) -> tuple:
    with mp.workdps(dps):
        out=[]
        for angular_l,qstr in ((0,".2"),(0,"1"),(0,"5"),(1,"1"),(2,"1"),(2,"5")):
            q=mp.mpf(qstr)
            def f(r):
                z=q*r
                h=mp.sqrt(mp.pi/(2*z))*(mp.besselj(angular_l+mp.mpf(".5"),z)
                        +1j*mp.bessely(angular_l+mp.mpf(".5"),z))
                return (1j)**(angular_l+1)*z*h*mp.exp(-1j*q)
            F, Fp=f(1),mp.diff(f,mp.mpf(1))
            # Independent two-sided matching, using spherical Bessel functions.
            refl,trans=mp.lu_solve(mp.matrix([[F,-F],[Fp,Fp-2*F]]),
                                  mp.matrix([-mp.conj(F),-mp.conj(Fp)]))
            P=sum((1j)**k*mp.factorial(angular_l+k)/(
                mp.factorial(k)*mp.factorial(angular_l-k)*(2*q)**k)
                for k in range(angular_l+1))
            Pp=sum(-k*(1j)**k*mp.factorial(angular_l+k)/(
                mp.factorial(k)*mp.factorial(angular_l-k)*2**k*q**(k+1))
                for k in range(1,angular_l+1))
            explicit=1j*q/(P*((1j*q-1)*P+q*Pp))
            assert abs(trans-explicit)<mp.mpf(10)**(-(dps-8))
            assert abs(abs(trans)**2+abs(refl)**2-1)<mp.mpf(10)**(-(dps-8))
            eta=abs(trans)**2
            # Ideal monochromatic/narrowband limit, not a finite-time past receiver.
            n_for_helstrom=mp.log(1/(4*mp.mpf(".01")*mp.mpf(".99")))/(4*eta)
            out.extend((eta,n_for_helstrom))
            print(f"dps={dps}; l={angular_l}, q={q}; eta={mp.nstr(eta,28)}; ideal N_1percent={mp.nstr(n_for_helstrom,24)}")
        # Explicit sign-modulated finite source with a causal transmitted waveform.
        def profile(t):
            return mp.sin(mp.pi*t)**2 if 0<t<1 else mp.mpf(0)
        def response(t):
            if t<=0:
                return mp.mpf(0)
            return profile(t)-mp.quad(lambda v: mp.exp(-(t-v))*profile(v),[0,min(t,1)])
        assert response(-1)==response(0)==0
        y= response(mp.mpf(".5"))
        assert y>0
        # Exact filter equation y'=f'-y, away from the switch endpoints.
        for at in (mp.mpf(".2"),mp.mpf(".5"),mp.mpf(".8"),mp.mpf("1.3")):
            assert abs(mp.diff(response,at)-(mp.diff(profile,at)-response(at))) < mp.mpf(10)**(-(dps-8))
        out.append(y)
        print(f"  finite source response at t=.5 b/c: {mp.nstr(y,28)} (opposite sign for the other bit)")
        # Actual quadrature readout of a normalized transmitted coherent mode:
        # means +/-sqrt(2*N*eta), variance 1/2; all results retained.
        occupation, efficiency=mp.mpf(2),mp.mpf(".5")
        mu=mp.sqrt(2*occupation*efficiency)
        p_wrong=mp.quad(lambda y: mp.exp(-(y-mu)**2)/mp.sqrt(mp.pi),[-mp.inf,0])
        assert abs(p_wrong-mp.erfc(mp.sqrt(2*occupation*efficiency))/2)<mp.mpf(10)**(-(dps-8))
        out.append(p_wrong)
        print(f"  FORWARD mode readout N=2,eta=.5: homodyne error={mp.nstr(p_wrong,28)}")
        return tuple(out)


def main() -> None:
    print(f"Python {platform.python_version()}; SymPy {s.__version__}; mpmath {mp.__version__}")
    exact_checks()
    a,b=numerical(50),numerical(80)
    with mp.workdps(85):
        assert all(abs(x-y)<mp.mpf("1e-42")*max(1,abs(y)) for x,y in zip(a,b))
    print("PASS 4D angular scattering, finite causal source and unconditional forward receiver statistics.")
    print("A physical time holonomy Delta is an EXTRA global input, not a clock label or computed device.")
    print("Past arrival requires Delta>tau_throat+d_external/c+tau_read. No post-CTC joint law is supplied.")


if __name__ == "__main__":
    main()
