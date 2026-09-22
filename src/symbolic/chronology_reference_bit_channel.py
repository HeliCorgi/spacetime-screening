#!/usr/bin/env python3
"""Receiver-inclusive CTC diagnostic, NOT a physical Taub-NUT channel.

Exact rational/complex arithmetic. Three registers D,S,C: a receiver pointer,
sender carrier and putative returning qubit. A retained classical flag R is
represented by its two explicit diagonal blocks (equivalent to a 16x16 state).
The same local circuit and return noise are used in every comparison.

This tests the difference between setting-by-setting Deutsch fixed points,
a single labeled-mixture product prescription, and an initially correlated
prescription. Their different recorded-bit statistics must not be conflated.
See notes/chronology-operational-channel-test.md for assumptions/references.
"""
from __future__ import annotations

from functools import lru_cache
import platform
import sympy as sp

I2 = sp.eye(2)
P = [sp.diag(1, 0), sp.diag(0, 1)]
X = sp.Matrix([[0, 1], [1, 0]])
Z = P[0] - P[1]


def partial_trace(a: sp.Matrix, keep: int) -> sp.Matrix:
    """Keep one of the three qubits in tensor order D,S,C."""
    if a.shape != (8, 8) or keep not in (0, 1, 2):
        raise ValueError('Expected an 8x8 matrix and keep=0,1,2')
    out = sp.zeros(2)
    for i in range(8):
        bi = [(i >> (2-k)) & 1 for k in range(3)]
        for j in range(8):
            bj = [(j >> (2-k)) & 1 for k in range(3)]
            if all(bi[k] == bj[k] for k in range(3) if k != keep):
                out[bi[keep], bj[keep]] += a[i, j]
    return sp.simplify(out)


@lru_cache(maxsize=None)
def circuit(c: sp.Expr, s: sp.Expr) -> sp.Matrix:
    """Read C into D BEFORE partial-SWAP encoding between S and C."""
    if sp.simplify(c*c + s*s - 1) != 0:
        raise ValueError('Partial-SWAP coefficients must obey c^2+s^2=1')
    read, swap = sp.zeros(8), sp.zeros(8)
    for d in (0, 1):
        for a in (0, 1):
            for b in (0, 1):
                j = 4*d + 2*a + b
                read[4*(d ^ b) + 2*a + b, j] = 1
                swap[4*d + 2*b + a, j] = 1
    u = (c*sp.eye(8) - sp.I*s*swap) * read
    assert sp.simplify(u.H*u - sp.eye(8)) == sp.zeros(8)
    return u


def evolve(b: int, tau: sp.Matrix, c: sp.Expr, s: sp.Expr) -> sp.Matrix:
    u = circuit(c, s)
    initial = sp.kronecker_product(P[0], P[b], tau)
    return sp.simplify(u*initial*u.H)


def noise(a: sp.Matrix, eta: sp.Expr) -> sp.Matrix:
    """Linear extension is required: includes tr(a), not a hardcoded 1."""
    return sp.simplify(eta*a + (1-eta)*sp.trace(a)*I2/2)


def loop_map(b: int, tau: sp.Matrix, c: sp.Expr,
             s: sp.Expr, eta: sp.Expr) -> sp.Matrix:
    return noise(partial_trace(evolve(b, tau, c, s), 2), eta)


def tv(p0: list, p1: list) -> sp.Expr:
    return sp.simplify(sum(abs(a-b) for a, b in zip(p0, p1))/2)


def audit_case(c: sp.Expr, s: sp.Expr, eta: sp.Expr,
               p0: sp.Expr) -> tuple:
    g, drive = eta*c*c, eta*s*s
    if g == 1:
        raise ValueError('Degenerate identity loop has no unique fixed point')
    zeta = sp.cancel(drive/(1-g))
    assert 0 <= zeta <= 1 and 0 <= g < 1
    tau = [(I2 + (-1)**b*zeta*Z)/2 for b in (0, 1)]
    p = [p0, 1-p0]
    tau_bar = sp.simplify(sum((p[b]*tau[b] for b in (0, 1)), sp.zeros(2)))

    # Exact Choi matrices from all matrix units, not just density inputs.
    for b in (0, 1):
        choi = sp.zeros(4)
        for i in (0, 1):
            for j in (0, 1):
                e = sp.zeros(2)
                e[i, j] = 1
                out = loop_map(b, e, c, s, eta)
                expected = eta*(c*c*sp.diag(e[0, 0], e[1, 1])
                                 + s*s*sp.trace(e)*P[b])
                expected += (1-eta)*sp.trace(e)*I2/2
                assert sp.simplify(out-expected) == sp.zeros(2)
                assert sp.trace(out) == sp.trace(e)
                choi += sp.kronecker_product(e, out)
        assert choi == sp.diag(*choi.diagonal())
        assert all(v >= (1-eta)/2 for v in choi.diagonal())
        assert loop_map(b, tau[b], c, s, eta) == tau[b]
        assert min(tau[b].diagonal()) >= 0 and sp.trace(tau[b]) == 1

    deterministic = []
    for b in (0, 1):
        d = partial_trace(evolve(b, tau[b], c, s), 0)
        deterministic.append(list(d.diagonal()))
    assert tv(*deterministic) == zeta

    # Product prescription: rho_RS tensor tau_bar, with R retained.
    # Blocks are unnormalized; tracing their sum gives the full loop state.
    product_blocks = [p[b]*evolve(b, tau_bar, c, s) for b in (0, 1)]
    returned = noise(sum((partial_trace(a, 2) for a in product_blocks), sp.zeros(2)), eta)
    assert sp.simplify(returned-tau_bar) == sp.zeros(2)
    joint_product = sp.Matrix([[partial_trace(product_blocks[b], 0)[y, y]
                                for y in (0, 1)] for b in (0, 1)])
    for b in (0, 1):
        for y in (0, 1):
            assert sp.simplify(joint_product[b, y]-p[b]*tau_bar[y, y]) == 0
    assert sum(joint_product) == 1
    conditional = [[joint_product[b, y]/p[b] for y in (0, 1)] for b in (0, 1)]
    assert tv(*conditional) == 0

    # Correlated alternative: sum_b p_b |bb><bb|_RS tensor tau_b.
    # Same input marginals, different correlations, NOT the product prescription.
    correlated_blocks = [p[b]*evolve(b, tau[b], c, s) for b in (0, 1)]
    joint_correlated = sp.Matrix([[partial_trace(correlated_blocks[b], 0)[y, y]
                                  for y in (0, 1)] for b in (0, 1)])
    for b in (0, 1):
        assert noise(partial_trace(correlated_blocks[b], 2), eta) == p[b]*tau[b]
    assert sp.simplify(sum((noise(partial_trace(a, 2), eta) for a in correlated_blocks),
                          sp.zeros(2))-tau_bar) == sp.zeros(2)
    correlated_cond = [[joint_correlated[b, y]/p[b] for y in (0, 1)] for b in (0, 1)]
    assert tv(*correlated_cond) == zeta
    assert sum(joint_correlated) == 1
    if zeta > 0:
        assert joint_correlated != joint_product  # linearity-trap negative control

    return g, zeta, joint_product, joint_correlated


def postselection_control() -> None:
    """Ordinary time-ordered QM: filtering later data fakes an earlier bit."""
    bell = sp.Matrix([1, 0, 0, 1])/sp.sqrt(2)
    rho = bell*bell.H
    unconditional, selected = [], []
    for b in (0, 1):
        joint = sp.zeros(2)
        for y in (0, 1):
            for a in (0, 1):
                k = sp.kronecker_product(P[y], P[a]*(X**b))
                joint[y, a] = sp.trace(k*rho*k.H)
        unconditional.append([sum(joint[y, a] for a in (0, 1)) for y in (0, 1)])
        success = sum(joint[y, 0] for y in (0, 1))
        assert success == sp.Rational(1, 2)
        selected.append([joint[y, 0]/success for y in (0, 1)])
    assert tv(*unconditional) == 0
    assert tv(*selected) == 1


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}')
    count = 0
    for c, s in [(sp.Integer(1), sp.Integer(0)), (sp.Integer(0), sp.Integer(1)),
                 (sp.Rational(3, 5), sp.Rational(4, 5)),
                 (sp.Rational(5, 13), sp.Rational(12, 13))]:
        for eta in [sp.Integer(0), sp.Rational(1, 4), sp.Rational(3, 4), sp.Integer(1)]:
            if eta*c*c == 1:
                continue
            for p in [sp.Rational(1, 2), sp.Rational(1, 3)]:
                audit_case(c, s, eta, p)
                count += 1
    postselection_control()
    g, zeta, product, correlated = audit_case(sp.Rational(3, 5), sp.Rational(4, 5),
                                            sp.Rational(3, 4), sp.Rational(1, 2))
    assert g == sp.Rational(27, 100) and zeta == sp.Rational(48, 73)
    assert product == sp.ones(2)/4
    assert correlated == sp.Matrix([[121, 25], [25, 121]])/292
    print(f'Exact circuit/Choi/fixed-point/reference checks: {count} parameter cases')
    print(f'Example: contraction={g}; setting-wise difference={zeta}')
    print(f'Retained-bit product prescription joint P(b,y)={product}; Delta=0')
    print(f'Correlated alternative joint P(b,y)={correlated}; Delta={zeta}')
    print('Both have identical input marginals and satisfy marginal loop consistency.')
    print('Later postselection: conditional Delta=1, unconditional Delta=0.')
    print('PASS diagnostic assertions; physical_Taub_NUT_channel_certified=False')
    print('No CTC hardware, full string state, or physical backwards signal is established.')


if __name__ == '__main__':
    main()
