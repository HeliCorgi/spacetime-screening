#!/usr/bin/env python3
"""Explicit, normalized negative-energy states and preparation work in a chiral CFT.

The states are smooth circle-diffeomorphism images of the NS vacuum. For a
free complex chiral fermion, symmetric point splitting independently gives
the stress. The preparation is an ideal stress-tensor Hamiltonian control in
the 2D model, not an engineered 4D MMP device. All outcomes are retained.
"""
from __future__ import annotations

import platform
import sympy as sp
import mpmath as mp


def symbolic_checks() -> None:
    x = sp.symbols('x', real=True)
    a, k, L, cc = sp.symbols('a k L c', positive=True)
    F = x - a * sp.sin(k*x) / k
    d1, d2, d3 = (sp.diff(F, x, n) for n in (1, 2, 3))
    schwarz = sp.factor(d3/d1 - sp.Rational(3, 2)*(d2/d1)**2)
    expected = (a*k**2*sp.cos(k*x)/(1-a*sp.cos(k*x))
                - sp.Rational(3, 2)*(a*k*sp.sin(k*x)/(1-a*sp.cos(k*x)))**2)
    assert sp.simplify(schwarz-expected) == 0
    stress = -sp.pi*cc*d1**2/(12*L**2)-cc*schwarz/(24*sp.pi)
    assert sp.simplify(stress.subs(x, 0) + sp.pi*cc*(1-a)**2/(12*L**2)
                       + cc*a*k**2/(24*sp.pi*(1-a))) == 0
    assert sp.simplify(stress.subs(a, 0)+sp.pi*cc/(12*L**2)) == 0
    # The circle integral of a Schwarzian is -1/2 integral (F''/F')^2.
    assert sp.simplify(schwarz-sp.diff(d2/d1, x)+sp.Rational(1, 2)*(d2/d1)**2) == 0
    q = (1-a**2)**(-sp.Rational(1, 2))-1-a**2/2
    assert sp.simplify(sp.diff(q, a)-a*((1-a**2)**(-sp.Rational(3, 2))-1)) == 0

    # Independent free-fermion point splitting, with the common phase removed:
    # K= sqrt(F'(x+h/2)F'(x-h/2))/(2 L sin(pi*(F(x+h/2)-F(x-h/2))/L)).
    h = sp.symbols('h')
    p = sp.symbols('p', positive=True)
    q2, r = sp.symbols('q2 r', real=True)
    num = sp.sqrt((p+q2*h/2+r*h*h/8)*(p-q2*h/2+r*h*h/8))
    den = 2*L*sp.sin(sp.pi*(p*h+r*h**3/24)/L)
    coeff = sp.expand(sp.series(num/den, h, 0, 2).removeO()).coeff(h, 1)
    target = (r/p-sp.Rational(3, 2)*(q2/p)**2)/(24*sp.pi)+sp.pi*p**2/(12*L**2)
    assert sp.simplify(coeff-target) == 0
    print('EXACT: smooth diffeomorphism vacuum has T=-pi*c*Fprime^2/(12 L^2)-c*Schwarzian/(24 pi).')
    print('EXACT: free-fermion point splitting reproduces this stress, not a prescribed negative tensor.')
    print('WORK: W=pi*c/(12 L) * [m^2*(1/sqrt(1-a^2)-1)-a^2/2] >= 0 for integer m>=1.')
    print('PREPARATION: circle diffeomorphism isotopy gives a stress-tensor Hamiltonian control; no 4D hardware claimed.')


def state_data(dps: int) -> list[mp.mpf]:
    with mp.workdps(dps):
        tau, L, cc = mp.mpf(1), mp.mpf(9)/4, mp.mpf(1)
        ell = tau/mp.pi
        tvac = -mp.pi*cc/(12*L**2)
        deficit = mp.mpf(17)/1944
        results = []
        for m, a_str in ((1, '0'), (1, '0.3'), (2, '0.1'), (1, '0.9')):
            a = mp.mpf(a_str)
            assert 0 <= a < 1 and m >= 1
            wave = 2*mp.pi*m/L
            def fp(v):
                return 1-a*mp.cos(wave*(v-tau))
            def fpp(v):
                return a*wave*mp.sin(wave*(v-tau))
            def fppp(v):
                return a*wave**2*mp.cos(wave*(v-tau))
            def T(v):
                S = fppp(v)/fp(v)-mp.mpf('1.5')*(fpp(v)/fp(v))**2
                return tvac*fp(v)**2-cc*S/(24*mp.pi)
            grid = [L*j/24 for j in range(25)]
            E = mp.quad(T, grid)
            W_num = E-L*tvac
            W_exact = mp.pi*cc/(12*L)*(m*m*(1/mp.sqrt(1-a*a)-1)-a*a/2)
            tol = mp.power(10, -dps+8)
            assert abs(W_num-W_exact) < tol
            assert W_num >= -tol
            assert fp(tau) == 1-a
            # Proper-circle monodromy: F(v+L)=F(v)+L, F'>0.
            for vv in (mp.mpf(0), mp.mpf('0.37'), tau):
                def F(v):
                    return v-a*mp.sin(wave*(v-tau))/wave
                assert abs(F(vv+L)-F(vv)-L) < tol
                assert fp(vv) > 0
            I = cc/24 + 2*ell*mp.quad(lambda v: mp.sin(v/(2*ell))**2*T(v),
                                       [tau*j/12 for j in range(25)])
            added = I-deficit
            A = cc/12+cc*tau/(6*(L-2*tau))+2*tau*E/mp.pi
            finite_bound = cc**2/(576*A)
            assert I >= finite_bound-tol and finite_bound > 0
            assert added >= -deficit-tol
            if a > 0:
                assert T(tau) < tvac  # Genuine negative pulse relative to Casimir vacuum.
            if m == 2 and a_str == '0.1':
                assert added < 0  # It helps, but does not supply enough.
            if m == 1 and a_str == '0.9':
                assert added > 0  # Stronger point negativity can worsen the full average.
            # A positive sampling function h supplies an independent circle-QEI test.
            # Its sharp infimum is checked in all of these non-vacuum states.
            hfun = lambda v: 1+mp.mpf('0.4')*mp.cos(2*mp.pi*v/L)
            dh = lambda v: -mp.mpf('0.4')*2*mp.pi/L*mp.sin(2*mp.pi*v/L)
            J = mp.quad(lambda v: 1/hfun(v), grid)
            sharp = -mp.pi*cc/(12*J)-cc/(48*mp.pi)*mp.quad(lambda v: dh(v)**2/hfun(v), grid)
            # h is in the global conformal span, so the vacuum saturates this bound.
            assert abs(sharp-L*tvac) < tol
            assert mp.quad(lambda v: hfun(v)*T(v), grid) >= sharp-tol
            results.extend((+I, +added, +T(tau), +W_exact, +finite_bound))
            print(f'dps={dps}; m={m}, a={a}; '
                  f'Tcenter={mp.nstr(T(tau), 30)}; I={mp.nstr(I, 30)}; '
                  f'Iextra={mp.nstr(added, 30)}; work={mp.nstr(W_exact, 30)}')

            # The two-point subtraction is independently evaluated with guard digits.
            # Epsilon truncation is O(epsilon^2); these checks are not interval proofs.
            with mp.workdps(2*dps+40):
                l_hi = mp.mpf(9)/4
                a_hi = mp.mpf(a_str)
                k_hi = 2*mp.pi*m/l_hi
                epsilon = mp.power(10, -(dps//2))
                def F_hi(v):
                    return v-a_hi*mp.sin(k_hi*(v-1))/k_hi
                def Fp_hi(v):
                    return 1-a_hi*mp.cos(k_hi*(v-1))
                for vv in (mp.mpf(1), mp.mpf('0.43')):
                    vp, vm = vv+epsilon/2, vv-epsilon/2
                    kernel = mp.sqrt(Fp_hi(vp)*Fp_hi(vm))/(2*l_hi*mp.sin(mp.pi*(F_hi(vp)-F_hi(vm))/l_hi))
                    split_T = -(kernel-1/(2*mp.pi*epsilon))/epsilon
                    z = k_hi*(vv-1)
                    prime = Fp_hi(vv)
                    S = a_hi*k_hi**2*mp.cos(z)/prime-mp.mpf('1.5')*(a_hi*k_hi*mp.sin(z)/prime)**2
                    exact_T = -mp.pi*prime**2/(12*l_hi**2)-S/(24*mp.pi)
                    assert abs(split_T-exact_T) < mp.power(10, -dps+8)
        return results


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}; mpmath {mp.__version__}')
    symbolic_checks()
    low, high = state_data(50), state_data(80)
    with mp.workdps(100):
        assert len(low) == len(high)
        assert all(abs(a-b) < mp.mpf('1e-40') for a, b in zip(low, high))
    print('PASS normalized-state stress, finite preparation work, 50/80-digit averages and point splitting.')
    print('Negative local energy is achieved in the CFT; the required negative total JT null integral is not.')
    print('No apparatus stress, higher-mode completion, boundary redesign or full MMP evolution was computed.')


if __name__ == '__main__':
    main()
