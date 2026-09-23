#!/usr/bin/env python3
"""Feedback-normalization audit, not a universal chronology-protection theorem.

Reproduce the one-party process constraint (Oreshkov--Costa--Brukner,
arXiv:1105.4464, Appendix C, Eq. 19) and apply it to the repository's
field/probe binary channel. The crucial assumption is an operation-independent
linear process for ALL forward laboratory instruments. CTC geometry alone
does not imply that assumption. No unavailable Taub-NUT kernel is assigned.
"""
from __future__ import annotations

from itertools import product
import platform
import sympy as sp

I2 = sp.eye(2)
X = sp.Matrix([[0, 1], [1, 0]])
Y = sp.Matrix([[0, -sp.I], [sp.I, 0]])
Z = sp.diag(1, -1)
PAULI = [I2, X, Y, Z]


def ptr_out(m: sp.Matrix) -> sp.Matrix:
    """Trace the output factor in input x output, both qubits."""
    if m.shape != (4, 4):
        raise ValueError('Expected a 4x4 two-qubit operator')
    return sp.Matrix(2, 2, lambda i, j: sum(m[2*i+k, 2*j+k] for k in range(2)))


def exact_zero(m: sp.Matrix) -> bool:
    return all(sp.simplify(v) == 0 for v in m)


def classical_checks() -> None:
    u, v, d, r, q = sp.symbols('u v d r q', real=True)
    # Columns: sent bit. Rows: received bit. This is NOT a joint state.
    kernel = sp.Matrix([[u, v], [1-u, 1-v]])
    maps = list(product(range(2), repeat=2))
    totals = {f: sp.expand(sum(kernel[y, f[y]] for y in range(2))) for f in maps}
    assert totals[(0, 0)] == totals[(1, 1)] == 1
    assert sp.expand(totals[(0, 1)] - (1+u-v)) == 0
    assert sp.expand(totals[(1, 0)] - (1-u+v)) == 0
    assert sp.solve([t-1 for t in totals.values()], [u], dict=True) == [{u: v}]

    symmetric = sp.Matrix([[(1+d)/2, (1-d)/2], [(1-d)/2, (1+d)/2]])
    forward = sp.Matrix(2, 2, lambda b, y: (1+r*(-1)**(b+y))/2)
    assert sp.expand(sum(symmetric[y, b]*forward[b, y]
                         for y in range(2) for b in range(2))) == 1+d*r
    # One normalization per fixed operation is not affine coarse-graining.
    z_mix = q*(1+d)+(1-q)*(1-d)
    copied_gate_weight = q*(1+d)/z_mix
    assert sp.simplify(copied_gate_weight.subs(q, sp.Rational(1, 2))-(1+d)/2) == 0
    assert sp.simplify(copied_gate_weight-q) != 0

    # Finite-alphabet check: all deterministic feedback maps plus column sums.
    # General proof (all sizes) is in the note; these are exact finite controls.
    for ny, nb in [(2, 2), (3, 2), (2, 3), (3, 3)]:
        coeffs = sp.symbols(f'k0:{ny*nb}')
        k = sp.Matrix(ny, nb, coeffs)
        equations = [sum(k[y, b] for y in range(ny))-1 for b in range(nb)]
        equations += [sum(k[y, f[y]] for y in range(ny))-1
                      for f in product(range(nb), repeat=ny)]
        a, rhs = sp.linear_eq_to_matrix(equations, coeffs)
        assert a.rank() == ny*nb-ny+1
        solution = next(iter(sp.linsolve((a, rhs), coeffs)))
        solved = k.subs(dict(zip(coeffs, solution)))
        assert all(sp.simplify(solved[y, b]-solved[y, 0]) == 0
                   for y in range(ny) for b in range(nb))
        print(f'Exact feedback constraints: {ny} outputs x {nb} inputs; rank={a.rank()}')

    # The closest binary input-independent kernel in maximum column TV is
    # obtained by replacing u,v with their mean: correction size |u-v|/2.
    midpoint = (u+v)/2
    assert sp.expand((u-midpoint)-(u-v)/2) == 0
    assert sp.expand((v-midpoint)+(u-v)/2) == 0
    print('Restoring one fixed no-signal kernel costs max-column TV at least |u-v|/2.')

    # Fixed example, rational throughout. A noisy positive channel is NOT enough.
    example = symmetric.subs(d, sp.Rational(1, 3))
    assert all(e >= 0 for e in example)
    assert sum(example[y, y] for y in range(2)) == sp.Rational(4, 3)
    assert sum(example[y, 1-y] for y in range(2)) == sp.Rational(2, 3)
    no_signal = symmetric.subs(d, 0)
    assert all(sum(no_signal[y, f[y]] for y in range(2)) == 1 for f in maps)
    print('Binary totals: constants=1; copy=1+d; flip=1-d; noisy feedback=1+d*r')
    print('Positive control d=0: every feedback is normalized; d=1/3: totals 4/3, 2/3')


def quantum_checks() -> None:
    coeffs = sp.symbols('w0:16', real=True)
    basis = [sp.kronecker_product(a, b) for a in PAULI for b in PAULI]
    w = sum((a*b for a, b in zip(coeffs, basis)), sp.zeros(4))
    m0 = sp.eye(4)/2
    assert ptr_out(m0) == I2
    equations = [sp.trace(w*m0)-1]
    # A full-dimensional collection of genuinely CPTP Choi operators.
    # We use the FULL transpose of the standard Choi operator (OCB convention).
    for i in range(4):
        for j in range(1, 4):
            direction = sp.kronecker_product(PAULI[i], PAULI[j])
            assert ptr_out(direction) == sp.zeros(2)
            assert direction*direction == sp.eye(4)
            for sign in [-1, 1]:
                m = m0 + sign*direction/4
                assert m.is_hermitian and ptr_out(m) == I2
                assert all(e >= 0 for e in m.eigenvals())
                equations.append(sp.trace(w*m)-1)
    a, b = sp.linear_eq_to_matrix(equations, coeffs)
    assert a.rank() == 13
    solution = next(iter(sp.linsolve((a, b), coeffs)))
    assert solution[0] == sp.Rational(1, 2)
    assert all(solution[4*i+j] == 0 for i in range(4) for j in range(1, 4))
    w_solved = w.subs(dict(zip(coeffs, solution)))
    rho = I2/2 + coeffs[4]*X + coeffs[8]*Y + coeffs[12]*Z
    assert exact_zero(w_solved-sp.kronecker_product(rho, I2))
    assert sp.trace(rho) == 1
    print('Quantum normalization rank=13/16; W=rho_input tensor I_output')

    # Apply to the actual algebraic receiver state derived in the preceding note.
    nu, phase = sp.symbols('nu phase', real=True)
    w_field = (sp.kronecker_product(I2, I2)
               + nu*sp.cos(phase)*sp.kronecker_product(X, I2)
               + nu*sp.sin(phase)*sp.kronecker_product(Y, Z))/2
    effects = [(I2+Y)/2, (I2-Y)/2]  # received bit 0 corresponds to Y=+1
    projectors = [sp.diag(1, 0), sp.diag(0, 1)]
    for f in maps_for_qubits():
        m = sum((sp.kronecker_product(effects[y], projectors[f[y]])
                 for y in range(2)), sp.zeros(4))
        assert m.is_hermitian and ptr_out(m) == I2
        assert all(e >= 0 for e in m.eigenvals())
        total = sp.simplify(sp.trace(w_field*m))
        expected = 1 if f[0] == f[1] else 1 + (1 if f == (0, 1) else -1)*nu*sp.sin(phase)
        assert sp.simplify(total-expected) == 0
    # Positive, trace-preserving backward channel with visible normalization defect.
    w_example = w_field.subs({nu: sp.Rational(1, 2), phase: sp.pi/2})
    assert w_example.eigenvals() == {sp.Rational(1, 4): 2, sp.Rational(3, 4): 2}
    # Physical trace-preservation of backward channel is trace over INPUT of W.
    tr_input = sp.Matrix(2, 2, lambda i, j: sum(w_example[2*k+i, 2*k+j] for k in range(2)))
    assert tr_input == I2
    print('Field-probe specialization: d=exp(-2 V_B)*sin(2 Delta_AB)')
    print('Positive backward Choi does not imply validity for all forward feedback.')


def maps_for_qubits() -> list[tuple[int, int]]:
    return [(0, 0), (0, 1), (1, 0), (1, 1)]


if __name__ == '__main__':
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}')
    classical_checks()
    quantum_checks()
    print('PASS exact conditional normalization checks; no universal physical NO claimed.')
    print('Escape requires changing the operation-independent/composable/linear assumptions.')
