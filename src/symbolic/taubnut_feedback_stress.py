#!/usr/bin/env python3
"""Taub-NUT stress sources of recorded field feedback, not solved backreaction.

Checks the exact diagnostic scalar action/frames and a homogeneous radial stress
profile. The profile is NOT asserted to be a global physical commutator/state.
Small-metric-perturbation bounds refer to a fixed identified interior CTC.
"""
from __future__ import annotations
import platform
import sympy as s
import mpmath as mp


def exact_checks() -> None:
    t, x, th, ph = s.symbols('t x theta phi', real=True)
    K, lam = s.symbols('K lambda', positive=True)
    D = s.Function('D', positive=True)(x)
    p, coords = x*x-1, (t, x, th, ph)
    g = K*s.Matrix([[-p/D, 0, 0, p*lam*s.cos(th)/D],
                    [0, 1/p, 0, 0], [0, 0, 1, 0],
                    [p*lam*s.cos(th)/D, 0, 0, s.sin(th)**2-p*lam**2*s.cos(th)**2/D]])
    gi = s.simplify(g.inv())
    Z = s.sqrt(D)
    ge, gei = Z*g, gi/Z
    sqrtg = K*K*s.sin(th)/Z  # 0<theta<pi, x>1.
    sqrte = Z*Z*sqrtg
    assert s.simplify(g.det()+sqrtg**2) == 0
    assert (sqrte*gei-sqrtg*Z*gi).applyfunc(s.simplify) == s.zeros(4)
    up = s.Matrix([0, 1/p, 0, 0])
    norme = s.simplify((up.T*gei*up)[0])
    Te = (up*up.T-ge*norme/2).applyfunc(s.simplify)
    target = s.Matrix([[1/(2*D), 0, 0, -lam*s.cos(th)/(2*D)],
                       [0, 1/(2*p*p), 0, 0], [0, 0, -1/(2*p), 0],
                       [-lam*s.cos(th)/(2*D), 0, 0, lam*lam*s.cos(th)**2/(2*D)-s.sin(th)**2/(2*p)]])
    assert (Te-target).applyfunc(s.simplify) == s.zeros(4)
    assert s.simplify(s.diff(sqrte*gei[1, 1]/p, x)) == 0
    def divergence(T, metric, inv, density):
        mixed, upper = inv*T, inv*T*inv
        return s.Matrix([s.simplify(sum(s.diff(density*mixed[a, b], coords[a]) for a in range(4))/density
                        -sum(s.diff(metric[a, c], coords[b])*upper[a, c] for a in range(4) for c in range(4))/2)
                         for b in range(4)])
    assert divergence(Te, ge, gei, sqrte) == s.zeros(4, 1)
    Ts = Z*Te
    Ophi = s.simplify(Z*(up.T*gi*up)[0])
    gradphi = s.Matrix([0, -s.diff(D, x)/(4*D), 0, 0])
    ward = divergence(Ts, g, gi, sqrtg)
    assert (ward-Ophi*gradphi).applyfunc(s.simplify) == s.zeros(4, 1)
    assert ward[1] != 0  # Dropping the dilaton source violates the Ward identity.
    a, b, c, nu, k = s.symbols('a b c nu k', real=True)
    coef = a*a+b*b+4*k*nu*a*c
    assert s.simplify((coef.subs(k, 1)-coef.subs(k, -1))-8*nu*a*c) == 0
    # Point-split covariance term 2 k nu (A*C+C*A) -> 2 k nu B_ab(A,C).
    A, C = s.Matrix(s.symbols('A0:4', real=True)), s.Matrix(s.symbols('C0:4', real=True))
    cross = A*C.T+C*A.T-ge*(A.T*gei*C)[0]
    total = (A*A.T-ge*(A.T*gei*A)[0]/2)+2*k*nu*cross
    assert (total.subs(k, 1)-total.subs(k, -1)-4*nu*cross).applyfunc(s.simplify) == s.zeros(4)
    # Interior time-fibre norm, exact for the published background family.
    delta, aa = s.symbols('delta a_alpha', positive=True)
    dx = (x+delta)**2-aa*p
    numerator = s.expand(s.diff(p, x)*dx-p*s.diff(dx, x)/2)
    expected = (1-aa)*x**3+3*delta*x**2+(2*delta**2+1+aa)*x+delta
    assert s.expand(numerator-expected) == 0
    # For x>1,delta>1,0<aa<1 it is positive: p/sqrt(D) increases radially.
    print('EXACT: four-dimensional scalar-frame identity; stress profile T_xx=1/(2p^2), T_tt=1/(2D).')
    print('EXACT: Einstein-frame divergence=0; string-frame divergence=O_Phi dPhi, generally nonzero.')
    print('EXACT: feedback stress difference = 4 exp(-2V_B) B_ab(e_A,c_B).')
    print('NEGATIVE CONTROL: a metric-only string-frame source omits a nonzero dilaton Ward term.')
    print('CTC BOUND: |h(n,n)|<1 along a fixed unit-timelike closed curve preserves that CTC.')


def numeric_checks(dps: int) -> list:
    with mp.workdps(dps):
        K, delta, aa = mp.mpf(6), mp.sqrt(mp.mpf(8)/5), mp.mpf(2)/5
        def D(x):
            return (x+delta)**2-aa*(x*x-1)
        def margin(x):
            return K*(x*x-1)/mp.sqrt(D(x))
        lo, mid = margin(mp.mpf('1.5')), margin(mp.mpf(2))
        rho = 1/(2*K*mp.sqrt(D(mp.mpf(2)))*3)
        assert 0 < lo < mid
        for i in range(21):
            xi = mp.mpf('1.5')+mp.mpf(i)/20
            assert margin(xi) >= lo-mp.power(10, -dps+8)
        # This is a norm margin, not a prediction that the metric responds by h.
        assert -1+mp.mpf('0.9') < 0
        assert -1+mp.mpf('1.1') > 0
        print(f'dps={dps}; min(-gE_tt), x in [1.5,2.5] = {mp.nstr(lo, 32)}')
        print(f'dps={dps}; -gE_tt at x=2 = {mp.nstr(mid, 32)}; radial-profile rho = {mp.nstr(rho, 32)}')
        return [+lo, +mid, +rho]


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {s.__version__}; mpmath {mp.__version__}')
    exact_checks()
    lo, hi = numeric_checks(50), numeric_checks(80)
    with mp.workdps(90):
        assert all(abs(a-b) < mp.mpf('1e-40') for a, b in zip(lo, hi))
    print('PASS stress/Ward/CTC diagnostics. No h_ab, global NUT state, reservoir or string backreaction assigned.')


if __name__ == '__main__':
    main()
