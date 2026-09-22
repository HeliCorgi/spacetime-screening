#!/usr/bin/env python3
"""Conditional interaction/backreaction diagnostics, not a full string amplitude.

Source metric/dilaton: Johnson--Svendsen, hep-th/0405141, eqs. (72)-(79).
See notes/heterotic-taubnut-interactions-backreaction-return.md.

The tests below establish algebraic facts in explicitly stated models:
* free spectator-current Wick selection rules;
* the regular ingoing metric and two counter-streaming null sources;
* the associated invariant stress and center-of-mass growth;
* finite dilaton coupling and local Misner boost holonomy;
* proper acceleration of a fixed-radius chronology orbit.
They do not establish a BRST physical state, a genus-one answer, a dynamically
formed singular barrier, or operational signalling to the past.
"""
from __future__ import annotations

from functools import lru_cache
import math
import sympy as sp


def zero(expr: sp.Expr) -> None:
    """Algebraic equality, not structural comparison of expressions."""
    assert sp.simplify(expr) == 0, expr


@lru_cache(None)
def wick(labels: tuple[int, ...]) -> sp.Expr:
    """Gaussian chiral current with <J_i J_j> = 1/(z_i-z_j)^2."""
    if not labels:
        return sp.Integer(1)
    if len(labels) % 2:
        return sp.Integer(0)
    first, rest = labels[0], labels[1:]
    return sum(
        (z[first] - z[other]) ** -2 * wick(rest[:i] + rest[i + 1:])
        for i, other in enumerate(rest)
    )


z = sp.symbols('z0:4')
assert wick((0, 1, 2)) == 0
four = wick((0, 1, 2, 3))
expected = (
    1 / ((z[0]-z[1])**2 * (z[2]-z[3])**2)
    + 1 / ((z[0]-z[2])**2 * (z[1]-z[3])**2)
    + 1 / ((z[0]-z[3])**2 * (z[1]-z[2])**2)
)
zero(four - expected)
assert four.subs(dict(zip(z, (0, 1, 2, 4)))) == sp.Rational(49, 144)
print('PASS spectator: identical-Y zero-momentum cubic factor vanishes; quartic factor does not.')

# L2 is the positive length squared prefactor (k-2)*alpha_prime.
p, D, L2 = sp.symbols('p D L2', positive=True)
g_static = L2 * sp.diag(1/p, -p/D)  # coordinates (x,t)
# v=t+r*, r*prime=sqrt(D)/p; transform to (x,v).
jac = sp.Matrix([[1, 0], [-sp.sqrt(D)/p, 1]])
g_ef = sp.simplify(jac.T * g_static * jac)
g_ef_expected = L2 * sp.Matrix([[0, 1/sp.sqrt(D)], [1/sp.sqrt(D), -p/D]])
assert sp.simplify(g_ef - g_ef_expected) == sp.zeros(2)
gi = sp.simplify(g_ef.inv())
zero(g_ef.det() + L2**2/D)

# Null covectors for ingoing v and outgoing u=v-2r*.
in_cov = sp.Matrix([0, 1])
out_cov = sp.Matrix([-2*sp.sqrt(D)/p, 1])
zero((in_cov.T*gi*in_cov)[0])
zero((out_cov.T*gi*out_cov)[0])
cross = sp.simplify((in_cov.T*gi*out_cov)[0])
zero(cross + 2*D/(L2*p))

rho_i, rho_o = sp.symbols('rho_i rho_o', nonnegative=True)
stress = rho_i*in_cov*in_cov.T + rho_o*out_cov*out_cov.T
stress2 = sp.simplify(sp.trace(gi*stress*gi*stress))
zero(stress2 - 8*rho_i*rho_o*D**2/(L2**2*p**2))
assert stress2.subs(rho_o, 0) == 0
# Vanishing invariant of pure null radiation is NOT zero stress or no backreaction.
assert stress.subs(rho_o, 0) != sp.zeros(2)

omega_i, omega_o = sp.symbols('omega_i omega_o', positive=True)
s_cm = sp.simplify(-2*omega_i*omega_o*cross)
zero(s_cm - 4*omega_i*omega_o*D/(L2*p))
# Check that the null-coframe contraction survives the full angular fibration.
# eta=dt+connection*dphi. These are local coframe elements; no globally exact
# eikonal or conserved four-dimensional source is asserted by this check.
connection, sin2 = sp.symbols('connection sin2', real=True, nonzero=True)
g4 = L2 * sp.Matrix([
    [1/p, 0, 0, 0],
    [0, -p/D, 0, -p*connection/D],
    [0, 0, 1, 0],
    [0, -p*connection/D, 0, sin2-p*connection**2/D],
])
gi4 = sp.simplify(g4.inv())
l4 = sp.Matrix([sp.sqrt(D)/p, 1, 0, connection])
n4 = sp.Matrix([-sp.sqrt(D)/p, 1, 0, connection])
zero((l4.T*gi4*l4)[0])
zero((n4.T*gi4*n4)[0])
zero((l4.T*gi4*n4)[0]-cross)
# At an ingoing future horizon, xi=d_v is future null. For future causal U,
# g(U,xi)<=0 gives U^x<=0. The retarded chart has the opposite cross sign.
Ux, Uv = sp.symbols('U_x U_v', real=True)
xi = sp.Matrix([0, 1])
U = sp.Matrix([Ux, Uv])
zero((U.T*g_ef*xi)[0].subs(p, 0)-L2*Ux/sp.sqrt(D))

print('PASS local geometry: EF metric regular; two-beam invariant and s_cm derived.')

x, delta, lam, k = sp.symbols('x delta lambda k', positive=True)
pm = x**2-1
Dm = (x+delta)**2 - sp.Integer(4)*pm/(k+2)
D1 = (1+delta)**2
st = stress2.subs({p: pm, D: Dm})
zero(sp.limit((x-1)**2*st, x, 1, dir='+') - 2*rho_i*rho_o*D1**2/L2**2)
zero(sp.limit((x-1)*s_cm.subs({p:pm,D:Dm}), x, 1, dir='+') - 2*omega_i*omega_o*D1/L2)
# Finite invariant for a nonzero regular incoming coefficient requires the
# outgoing null-fluid coefficient to vanish at least quadratically in y.
rho0 = sp.symbols('rho0', positive=True)
zero(sp.limit(st.subs(rho_o, rho0*(x-1)**2), x, 1, dir='+') - 2*rho_i*rho0*D1**2/L2**2)
print('PASS conditional near-horizon source: T_ab T^ab ~ (x-1)^(-2) if both coefficients stay nonzero.')

# Differentiating the *given* dilaton does not solve the backreacted equations.
g0 = sp.symbols('g0', positive=True)
gs = g0*Dm**(-sp.Rational(1,4))
zero(sp.diff(gs, x) + g0*sp.diff(Dm,x)/(4*Dm**sp.Rational(5,4)))
zero(sp.diff(Dm,x) - (2*(k-2)*x/(k+2)+2*delta))
# For k>2,delta>=1,x>=1 the last derivative is positive: gs maximum is at x=1.
gh = g0/sp.sqrt(1+delta)
zero(gs.subs(x,1)**4-gh**4)

# Proper-acceleration invariant of the static t-orbit, calculated in string frame.
acc2 = sp.factor(pm*(sp.diff(pm,x)/pm-sp.diff(Dm,x)/Dm)**2/(4*L2))
period_tau2 = (4*sp.pi*lam)**2*L2*pm/Dm
zero(sp.limit((x-1)*acc2, x, 1, dir='+')-1/(2*L2))
boost = 4*sp.pi*lam/(1+delta)
zero(sp.limit(acc2*period_tau2, x, 1, dir='+')-boost**2)

values = {k:8, delta:sp.sqrt(sp.Rational(8,5)), lam:sp.sqrt(sp.Rational(2,5))}
beta = float(boost.subs(values).evalf())
print(f'boost rapidity beta = {beta:.15f}; exp(beta) = {math.exp(beta):.15f}')
print(f'gs(horizon)/g0 = {float((gh/g0).subs(values)):.15f}')
# This recurrence is a declared toy, NOT the exact gauge/orbifold image sum.
for eps0 in (1e-6, 1e-12, 1e-24):
    first = math.ceil(math.log(1/eps0)/beta)
    assert eps0*math.exp((first-1)*beta) < 1 <= eps0*math.exp(first*beta)
    print(f'conditional boost-overlap toy: eps0={eps0:g}, first n with eps_n>=1: {first}')

# Periodicity of an eigenfunction only gives the same spacetime point/phase.
N = sp.symbols('N', integer=True)
zero(sp.exp(-2*sp.pi*sp.I*N)-1)
# Equal spectral weights need not identify two states: a literal counterexample.
H = sp.zeros(2)
e0, e1 = sp.eye(2).col(0), sp.eye(2).col(1)
assert H*e0 == H*e1 and e0 != e1 and (e0.T*e1)[0] == 0
print('PASS logical checks: a periodic phase is not signalling; equal weights are not state equality.')
print('OK: all explicitly scoped interaction/backreaction assertions passed.')
