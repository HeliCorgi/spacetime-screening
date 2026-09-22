#!/usr/bin/env python3
"""Receiver-event audit on the existing heterotic Taub-NUT geometry.

This reproduces fixed-background kinematics, not a physical message channel.
A receiver inside NUT is not chronal. The short laboratory arc B->A and the
long carrier arc A->B are distinct future timelike arcs of the same circle.
An unwrapped proper-time label is used only on each arc, not as a global
single-valued clock on the quotient. No full backreaction is computed.
"""
from __future__ import annotations

import platform
import sympy as sp


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}')
    x = sp.symbols('x', real=True)
    K = sp.Integer(6)  # (k-2)*alpha_prime with k=8, alpha_prime=1
    delta = sp.sqrt(sp.Rational(8, 5))
    lam = sp.sqrt(sp.Rational(2, 5))
    p = x*x - 1
    D = sp.expand((x+delta)**2 - sp.Rational(2, 5)*p)
    assert sp.simplify(D - (3*x*x/sp.Integer(5) + 2*delta*x + 2)) == 0
    # All three terms in this polynomial are positive for x>1.
    gtt = -K*p/D
    scale = sp.sqrt(-gtt.subs(x, 2))
    period = 4*sp.pi*lam
    loop = sp.simplify(period*scale)
    lab_arc, return_arc = sp.simplify(loop/4), sp.simplify(3*loop/4)
    assert sp.simplify(lab_arc+return_arc-loop) == 0
    assert gtt.subs(x, 2).is_negative is True
    assert (period/4).is_positive is True
    assert (period-period/4).is_positive is True
    accel2 = sp.factor(p/(4*K)*(sp.diff(p, x)/p-sp.diff(D, x)/D)**2)
    assert accel2.subs(x, 2).is_nonnegative is True

    # Unit future timelike tangents on both arcs, with t increasing.
    arc_norm = sp.simplify(gtt.subs(x, 2)*(1/scale)**2)
    assert arc_norm == -1
    # B has t=0; A has t=period/4. They are NOT the same quotient event.
    assert sp.simplify((period/4)/period) == sp.Rational(1, 4)

    # Local outgoing horizon chart (q,x), q=t-r_star, n=d/dq future.
    q_metric = sp.Matrix([[-K*p/D, -K/sp.sqrt(D)], [-K/sp.sqrt(D), 0]])
    assert sp.simplify(q_metric.det()+K*K/D) == 0
    d = 1+delta
    assert sp.simplify(D.subs(x, 1)-d*d) == 0
    vq, vx = sp.symbols('v_q v_x', real=True)
    inner = sp.simplify((sp.Matrix([vq, vx]).T*q_metric*sp.Matrix([1, 0]))[0])
    at_horizon = sp.simplify(inner.subs(x, 1))
    assert sp.simplify(sp.sqrtdenest(at_horizon+K*vx/d)) == 0
    # Future causal inner products with n are <=0, hence v_x>=0 there.
    # This local calculation does not classify every global extension.

    for n in (2, 3, 4):
        omega = n/(2*lam)
        observed_frequency = omega/scale
        assert sp.simplify(observed_frequency*loop-2*sp.pi*n) == 0
    # A global phase change of a single state is not a bit encoding.
    ket = sp.Matrix([1, 2])/sp.sqrt(5)
    phase = (3+4*sp.I)/5
    assert sp.simplify((phase*ket)*(phase*ket).H-ket*ket.H) == sp.zeros(2)

    print('B:t=0, A:t=L/4 at x=2 and fixed angles; L=4*pi*lambda.')
    print(f'Full proper loop length: {sp.N(loop, 35)} [alpha_prime=1]')
    print(f'B->A laboratory proper duration: {sp.N(lab_arc, 35)}')
    print(f'A->B returning-arc proper duration: {sp.N(return_arc, 35)}')
    print(f'Static carrier acceleration squared: {sp.N(accel2.subs(x, 2), 35)}')
    print('Both arcs are future timelike: B<<A and A<<B; B is not chronal.')
    print('Horizon inner product: g(v,n)=-K*v_x/(1+delta).')
    print('Periodic phase is not a global clock or a distinguishable message.')
    print('PASS geometric checks; physical_Taub_NUT_channel_certified=False')


if __name__ == '__main__':
    main()
