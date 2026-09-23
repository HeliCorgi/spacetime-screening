#!/usr/bin/env python3
"""Closed versus refreshed reservoirs for the existing field/probe instrument.

Analytic scope: density-operator fixed points of an outcome-blind unitary
return on field+retained reservoir, for either fixed sender setting. The
infinite-dimensional no-go is proved in the companion note, not inferred
from finite matrices. A fresh-bath countermodel has normal fixed states.
None of these maps is asserted to be the global NUT completion.
"""
from __future__ import annotations

import platform
import sympy as sp
import mpmath as mp


def symbolic_checks() -> None:
    I = sp.I
    # Independent finite-matrix check of the Hilbert-Schmidt identity.
    # It is valid in finite dimension too, but the no-go is NOT: finite
    # translations have invariant density operators. Preserve that control.
    Z = sp.diag(1, -1)
    X = sp.Matrix([[0, 1], [1, 0]])
    eye = sp.eye(2)
    Bminus = sp.kronecker_product((3*eye-4*I*Z)/5, eye)
    Bplus = Bminus.conjugate().T
    H = sp.Matrix([[1, 1], [1, -1]])/sp.sqrt(2)
    CNOT = sp.Matrix([[1, 0, 0, 0], [0, 1, 0, 0],
                      [0, 0, 0, 1], [0, 0, 1, 0]])
    returns = [sp.eye(4), sp.kronecker_product(H, eye),
               CNOT*sp.kronecker_product(H, H)]
    source = sp.kronecker_product((3*eye+4*I*X)/5, eye)
    raw = sp.Matrix([[1, 0, 0, 0], [I, 2, 0, 0],
                     [1, 1, 2, 0], [0, -I, 1, 1]])
    expand = lambda M: M.applyfunc(sp.expand)
    rho = expand(raw*raw.conjugate().T)
    rho /= sp.trace(rho)
    hs2 = lambda M: sp.simplify(sp.trace(expand(M).conjugate().T*expand(M)))
    for U in returns:
        assert (U.conjugate().T*U-sp.eye(4)).applyfunc(sp.simplify) == sp.zeros(4)
        Vminus = expand(U*source*Bminus)
        Vplus = expand(U*source*Bplus)
        A = expand(Vminus*rho*Vminus.conjugate().T)
        B = expand(Vplus*rho*Vplus.conjugate().T)
        out = (A+B)/2
        assert sp.simplify(hs2(rho)-hs2(out)-hs2(A-B)/4) == 0
        assert sp.simplify(sp.trace(out)-1) == 0
        # Kraus record sum is the same random-unitary map for fixed sending.
        via_record = sp.zeros(4)
        complete = sp.zeros(4)
        for y in (1, -1):
            M = (Bminus-I*y*Bplus)/2
            complete += M.conjugate().T*M
            N = expand(U*source*M)
            via_record += expand(N*rho*N.conjugate().T)
        assert (complete-sp.eye(4)).applyfunc(sp.simplify) == sp.zeros(4)
        assert (via_record-out).applyfunc(sp.simplify) == sp.zeros(4)
    print('EXACT: purity loss = one quarter of the squared HS distance of the two unitary branches.')
    print('This includes arbitrary initial field-bath correlations; return must not access the receiver record.')

    # Weyl commutator: conjugation by exp(2iB) translates the A distribution.
    s, dc = sp.symbols('s Delta_AB', real=True)
    vecs = [sp.Matrix(v) for v in ((0, -2), (s, 0), (0, 2))]
    Om = sp.Matrix([[0, dc], [-dc, 0]])
    phase = sum((vecs[i].T*Om*vecs[j])[0]
                for i in range(3) for j in range(i+1, 3))
    assert sp.simplify(phase-4*s*dc) == 0
    # Bminus/Bplus equality at a fixed point forces invariance under exp(2iB).
    # A continuous characteristic function cannot obey chi(s)=exp(-2is dc)chi(s)
    # with chi(0)=1 when dc!=0 (proof and assumptions in the note).
    print('WEYL: exp(-2iB) exp(isA) exp(2iB)=exp(-2is Delta_AB) exp(isA).')
    print('CONDITIONAL NO-GO: no invariant trace-class density operator for Delta_AB!=0.')

    # Deliberate finite-cutoff false-positive: identity/d is always invariant
    # under a random-unitary channel. Its oscillator energy grows with d.
    for d in (2, 4, 8, 16):
        Hosc = sp.diag(*[sp.Rational(2*j+1, 2) for j in range(d)])
        assert sp.trace(Hosc*sp.eye(d)/d) == sp.Rational(d, 2)
    for U in returns:
        zero = sp.eye(4)/4
        branches = [U*V*zero*V.conjugate().T*U.conjugate().T for V in (Bminus, Bplus)]
        assert (sum(branches, sp.zeros(4))/2-zero).applyfunc(sp.simplify) == sp.zeros(4)
    print('NEGATIVE CONTROL: truncated maximally mixed fixed states have energy d/2, not a bosonic stationary limit.')

    # Reused two-mode bath, all four feedback controls: the common commuting
    # P sector is closed under real beam-splitter mixing.
    eta, noise, ve = sp.symbols('eta beta2 Venv', positive=True)
    vv, ww, cross = sp.symbols('V W C', real=True)
    c, d = sp.symbols('c d', real=True)
    rot = sp.Matrix([[c, d], [-d, c]])
    V = sp.Matrix([[vv, cross], [cross, ww]])
    kicked = V+sp.diag(noise, 0)
    updated = rot*kicked*rot.T
    assert sp.expand(sp.trace(updated)-(c*c+d*d)*(sp.trace(V)+noise)) == 0
    # With a product fresh bath, compute the bath output and correlations too.
    rot_eta = rot.subs({c: sp.sqrt(eta), d: sp.sqrt(1-eta)})
    fresh = rot_eta*sp.diag(vv+noise, ve)*rot_eta.T
    vstar = ve+eta*noise/(1-eta)
    assert sp.simplify(fresh[0, 0].subs(vv, vstar)-vstar) == 0
    assert sp.simplify(fresh[1, 1].subs(vv, vstar)-(ve+noise)) == 0
    assert sp.simplify(fresh[0, 1].subs(vv, vstar)+sp.sqrt(eta)*sp.sqrt(1-eta)*noise/(1-eta)) == 0
    # Complete positivity needs the environment vacuum noise as well.
    Omega = sp.Matrix([[0, 1], [-1, 0]])
    cp = (1-eta)*ve*sp.eye(2)+sp.I*(1-eta)*Omega/2
    assert sp.factor(cp.det()-(1-eta)**2*(ve**2-sp.Rational(1, 4))) == 0
    invalid = cp.subs({eta: sp.Rational(1, 4), ve: 0})
    assert min(invalid.eigenvals()) == -sp.Rational(3, 8)
    # eta=1/4 is a 60-degree mode-space rotation. Six reuses are exact.
    O = sp.Matrix([[sp.Rational(1, 2), sp.sqrt(3)/2],
                   [-sp.sqrt(3)/2, sp.Rational(1, 2)]])
    C = sp.eye(2)/2
    kick = sp.Rational(9, 25)
    for n in range(1, 7):
        C = (O*(C+sp.diag(kick, 0))*O.T).applyfunc(sp.simplify)
        assert sp.simplify(sp.trace(C)-1-n*kick) == 0
    assert C == sp.Rational(79, 50)*sp.eye(2)
    print('REUSED BATH: total P variance increases by beta^2 each turn; after 6 turns V_P=1.58 I.')
    print('FRESH BATH: V_P*=0.62, bath output variance=0.86 for eta=1/4,beta=3/5,Venv=1/2.')
    print('These are P-quadrature budgets, NOT a lower bound on total heat for arbitrary feedback.')

    # Fresh-bath FULL one-mode fixed-state existence via a Lyapunov bound.
    # Do not assume the feedback state remains Gaussian.
    alpha, beta, energy, eps = sp.symbols('alpha beta E epsilon', positive=True)
    boundA = (1+eta)/2
    boundB = eta*(alpha**2+beta**2)/2+eta**2*alpha**2/(1-eta)+(1-eta)*ve
    choice = (1-eta)/(2*eta)
    before = eta*((1+eps)*energy+(alpha**2+beta**2+alpha**2/eps)/2)+(1-eta)*ve
    assert sp.simplify(before.subs(eps, choice)-boundA*energy-boundB) == 0
    # An elementary pointwise inequality controls both copy and NOT.
    q, f = sp.symbols('q f', real=True)
    slack = eps*q*q+alpha**2/eps+2*alpha*q*f
    assert sp.expand(slack-((sp.sqrt(eps)*q+alpha*f/sp.sqrt(eps))**2
                           +alpha**2*(1-f*f)/eps)) == 0
    print('FRESH-BATH EXISTENCE: energy obeys E_next <= a E+b, a=(1+eta)/2<1.')
    print('The analytic compactness/Cesaro argument yields at least one normal finite-energy fixed state for each control.')


def numerical_checks(dps: int) -> tuple:
    with mp.workdps(dps):
        alpha, beta = mp.mpf('0.7'), mp.mpf('0.6')
        eta, ve = mp.mpf('0.25'), mp.mpf('0.5')
        c = mp.sqrt(eta)
        vp = ve+eta*beta*beta/(1-eta)
        mu = -alpha*c/(1-c)
        N = 180 if dps == 80 else 120

        def chi(s, t, r=1):
            phase = mp.exp(1j*r*mu*s-ve*(s*s+t*t)/2)
            return phase*mp.fprod(mp.cos(beta*c**j*t) for j in range(1, N+1))

        maxres = mp.mpf(0)
        for s, t in ((mp.mpf('0.2'), mp.mpf('0.3')),
                     (mp.mpf('-0.7'), mp.mpf('1.1')),
                     (mp.mpf('0'), mp.mpf('0'))):
            for r in (1, -1):
                rhs = mp.exp(-(1-eta)*ve*(s*s+t*t)/2)*mp.exp(-1j*r*alpha*c*s)*mp.cos(beta*c*t)*chi(c*s, c*t, r)
                residual = abs(chi(s, t, r)-rhs)
                tail = beta*beta*t*t*eta**(N+1)/(2*(1-eta))
                assert residual < tail+mp.power(10, -dps+8)
                assert abs(chi(-s, -t, r)-mp.conj(chi(s, t, r))) < mp.power(10, -dps+8)
                maxres = max(maxres, residual)
        qmean = mp.diff(lambda s: chi(s, 0), 0)/1j
        q2 = -mp.diff(lambda s: chi(s, 0), 0, 2)
        p2 = -mp.diff(lambda t: chi(0, t), 0, 2)
        assert abs(qmean-mu) < mp.power(10, -dps+8)
        assert abs(q2-(ve+mu*mu)) < mp.power(10, -dps+8)
        assert abs(p2-vp) < mp.power(10, -dps+8)
        E = mp.re((q2+p2)/2)
        Ebound = eta*(alpha*alpha+beta*beta)/(1-eta)+2*eta*eta*alpha*alpha/(1-eta)**2+2*ve
        assert E < Ebound
        separate_D = mp.exp(-2*beta*beta*ve)*abs(mp.sin(2*beta*mu))
        # With one independent retained setting flag and a common incoming
        # field state, pre-feedback Y is independent of that flag, for any state.
        for qf, py in ((mp.mpf('0.3'), mp.mpf('0.7')),
                       (mp.mpf('0.5'), mp.mpf('0.5'))):
            joint = [[qf*py, qf*(1-py)], [(1-qf)*py, (1-qf)*(1-py)]]
            assert abs(sum(map(sum, joint))-1) < mp.power(10, -dps+8)
            assert abs(joint[0][0]/qf-joint[1][0]/(1-qf)) < mp.power(10, -dps+8)
        print(f'dps={dps}; fresh-bath full-state <H>={mp.nstr(E, 32)}; V_P={mp.nstr(vp, 32)}; bound={mp.nstr(Ebound, 32)}')
        print(f'dps={dps}; separately selected fixed-state readout distance={mp.nstr(separate_D, 32)}; independent retained-flag distance=0')
        print(f'dps={dps}; full two-quadrature characteristic-function residual={mp.nstr(maxres, 5)}')
        return +E, +vp, +separate_D


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}; mpmath {mp.__version__}')
    symbolic_checks()
    low, high = numerical_checks(50), numerical_checks(80)
    with mp.workdps(90):
        for a, b in zip(low, high):
            assert abs(a-b) < mp.mpf('1e-40')
    print('PASS reservoir algebra and 50/80-digit fixed-state checks.')
    print('Closed density-operator return is rejected under explicit assumptions; fresh-bath mathematical escape survives.')
    print('No physical NUT reservoir, apparatus stress, global quantum state or backward communication is certified.')


if __name__ == '__main__':
    main()
