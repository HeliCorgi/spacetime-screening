#!/usr/bin/env python3
"""Derive a retained-bit/receiver distribution from free-field Weyl couplings.

This is a specialization of the field-mediated detector framework, not a
Deutsch or postselection prescription. It is conditional on a positive field
state, a valid commutator and an allowed interaction ordering. Those inputs
are NOT supplied for the complete Taub-NUT chronology-violating region here.
"""
from __future__ import annotations

import platform
import sympy as sp
import mpmath as mp


def symbolic_checks() -> None:
    delta, va, vb, cov = sp.symbols('Delta V_A V_B C', real=True)
    H = sp.Matrix([[va, cov], [cov, vb]])
    Omega = sp.Matrix([[0, delta], [-delta, 0]])

    def expectation(word: list[tuple]) -> sp.Expr:
        vectors = [sp.Matrix(v) for v in word]
        total = sum(vectors, sp.zeros(2, 1))
        phase = sum((vectors[i].T*Omega*vectors[j])[0]
                    for i in range(len(vectors)) for j in range(i+1, len(vectors)))
        return sp.exp(sp.expand(-sp.I*phase/2-(total.T*H*total)[0]/2))

    # Weyl self-inverse and a sign-sensitive commutator check.
    assert expectation([(1, 0), (-1, 0)]) == 1
    group_comm = expectation([(1, 0), (0, 1), (-1, 0), (0, -1)])
    assert sp.simplify(group_comm-sp.exp(-sp.I*delta)) == 0
    Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    I2 = sp.eye(2)
    nu = sp.exp(-2*vb)
    z = (1, -1)
    states, early = [], []
    p0 = sp.symbols('p_0', real=True)
    joint = sp.zeros(2)
    for bit in (0, 1):
        r = (-1)**bit
        # U_A=exp(i*r*Phi_A), U_B=exp(-i*Z_B*Phi_B), B starts in |+x>.
        # Trace cyclicity gives U_A^dagger W_B(z_j-z_i) U_A.
        rho = sp.Matrix(2, 2, lambda i, j:
                        expectation([(-r, 0), (0, z[j]), (0, -z[i]), (r, 0)])/2)
        expected = sp.Matrix([[1, nu*sp.exp(-2*sp.I*r*delta)],
                              [nu*sp.exp(2*sp.I*r*delta), 1]])/2
        assert (rho-expected).applyfunc(sp.simplify) == sp.zeros(2)
        assert (rho-rho.conjugate().T).applyfunc(sp.simplify) == sp.zeros(2)
        assert sp.trace(rho) == 1
        assert sp.simplify(rho.det()-(1-nu**2)/4) == 0
        weight = p0 if bit == 0 else 1-p0
        for j, outcome in enumerate((1, -1)):
            prob = sp.simplify(sp.trace((I2+outcome*Y)/2*rho).rewrite(sp.sin))
            target = (1+outcome*r*nu*sp.sin(2*delta))/2
            assert sp.simplify(prob-target) == 0
            joint[bit, j] = weight*target
        assert sp.simplify(sum(joint[bit, j] for j in range(2))-weight) == 0
        states.append(rho)
        # An actual earlier readout: U_A acts later on the field only.
        old = sp.Matrix(2, 2, lambda i, j:
                        expectation([(0, z[j]), (-r, 0), (r, 0), (0, -z[i])])/2)
        early.append(old)
    assert sp.simplify(sum(joint)) == 1
    difference = states[0]-states[1]
    assert (difference**2-nu**2*sp.sin(2*delta)**2*I2).applyfunc(lambda x: sp.simplify(sp.expand_complex(x))) == sp.zeros(2)
    assert (early[0]-early[1]).applyfunc(sp.simplify) == sp.zeros(2)
    assert sp.simplify(sp.trace(Y*early[0])) == 0

    # The two-point function must be positive, not just a formal solution.
    W = H+sp.I*Omega/2
    assert sp.simplify(W.det()-(va*vb-cov**2-delta**2/4)) == 0
    invalid = W.subs({va: 0, vb: 0, cov: 0, delta: 1})
    assert invalid.eigenvals() == {sp.Rational(-1, 2): 1, sp.Rational(1, 2): 1}
    print('EXACT P(R=b,Y=y)=p_b*(1+y*(-1)^b*exp(-2V_B)*sin(2Delta))/2.')
    print('EXACT D=exp(-2V_B)*abs(sin(2Delta)); positive normalized joint state.')
    print('EXACT true earlier readout is unchanged by the later field-only unitary.')
    print('NEGATIVE CONTROL: zero covariance with nonzero commutator has negative eigenvalue.')
    print('A nonzero timelike commutator alone is not evidence of backwards signalling.')


def quadrature_checks(dps: int) -> list[tuple]:
    with mp.workdps(dps):
        results = []
        # Independent infinite-dimensional representation, not a Fock cutoff:
        # Phi_A=-Delta*P, Phi_B=Q, [Q,P]=i. Sender translates a Gaussian.
        for delta, vb in ((mp.mpf('0'), mp.mpf('0.5')),
                          (mp.mpf('0.2'), mp.mpf('0.5')),
                          (mp.pi/4, mp.mpf('0.5')),
                          (mp.pi/2, mp.mpf('0.5')),
                          (mp.mpf('0.2'), mp.mpf('2'))):
            target_nu = mp.exp(-2*vb)
            probs = []
            for r in (1, -1):
                def density(q):
                    return mp.exp(-(q-r*delta)**2/(2*vb))/mp.sqrt(2*mp.pi*vb)
                bounds = [-mp.inf, r*delta-4*mp.sqrt(vb), r*delta,
                          r*delta+4*mp.sqrt(vb), mp.inf]
                norm = mp.quad(density, bounds)
                coherence = mp.quad(lambda q: density(q)*mp.exp(-2j*q), bounds)
                assert abs(norm-1) < mp.power(10, -dps+8)
                assert abs(coherence-target_nu*mp.exp(-2j*r*delta)) < mp.power(10, -dps+8)
                p_plus = (1-mp.im(coherence))/2
                assert 0 <= p_plus <= 1
                probs.append(p_plus)
            distance = abs(probs[0]-probs[1])
            target = target_nu*abs(mp.sin(2*delta))
            assert abs(distance-target) < mp.power(10, -dps+8)
            results.append((+distance, +(1+distance)/2))
            print(f'dps={dps}; Delta={mp.nstr(delta, 8)}; V_B={vb}; '
                  f'D={mp.nstr(distance, 35)}; Pguess={mp.nstr((1+distance)/2, 35)}')
        return results


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}; mpmath {mp.__version__}')
    symbolic_checks()
    low, high = quadrature_checks(50), quadrature_checks(80)
    with mp.workdps(90):
        for a, b in zip(low, high):
            for x, y in zip(a, b):
                assert abs(x-y) < mp.mpf('1e-40')
    print('PASS exact field/detector algebra and 50/80-digit independent integrals.')
    print('Comparison values are NOT Taub-NUT probabilities. No missing kernel is set to zero.')


if __name__ == '__main__':
    main()
