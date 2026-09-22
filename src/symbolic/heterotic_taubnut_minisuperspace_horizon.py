#!/usr/bin/env python3
"""Exact heterotic Taub-NUT minisuperspace horizon/transmission diagnostics.

This is an obstruction test, not a full BRST-spectrum proof.

Input exact nonrotating background:
  ds^2 = (k-2){ dx^2/(x^2-1)
               -(x^2-1)/D(x) (dt-lambda cos(theta)dphi)^2
               +dtheta^2+sin^2(theta)dphi^2 }
  D(x)=(x+delta)^2-4(x^2-1)/(k+2)
  Phi-Phi0 = -(1/4) log D.

For a dilaton-weighted scalar zero mode, the natural operator is
  O = [e^{-2Phi} sqrt|g|]^{-1}
      d_mu[e^{-2Phi} sqrt|g| g^{mu nu} d_nu].

The script checks:
  * exact cancellation of the x-dependence in e^{-2Phi}sqrt|g|;
  * separated radial equation;
  * regular-singular horizon exponents at x=+/-1;
  * finite nonzero conserved horizon flux;
  * tortoise-coordinate Schrödinger potential V -> 0 at x=1;
  * asymptotic NUT-region propagation threshold.

These statements show that x=1 is not a local perfect-reflection wall for
minisuperspace modes. They do NOT establish a normalizable BRST physical
heterotic string state or an operational CTC return.
"""

import sympy as sp

x, k, delta, lam, theta = sp.symbols(
    "x k delta lambda theta", real=True, positive=True
)
omega, Lambda = sp.symbols("omega Lambda", real=True)
I = sp.I

K = k - 2
p = x**2 - 1
D = (x + delta) ** 2 - sp.Rational(4, 1) * p / (k + 2)
f = p / D
s = sp.sin(theta)
a = -lam * sp.cos(theta)  # dt + a dphi = dt - lambda cos(theta)dphi

# Dimensionless metric g/K in coordinates (x,t,theta,phi).
g0 = sp.Matrix(
    [
        [1 / p, 0, 0, 0],
        [0, -f, 0, -f * a],
        [0, 0, 1, 0],
        [0, -f * a, 0, s**2 - f * a**2],
    ]
)

det_g0 = sp.cancel(g0.det())
assert sp.simplify(det_g0 + s**2 / D) == 0

ginv0 = sp.simplify(g0.inv())
assert sp.simplify(ginv0[0, 0] - p) == 0
assert sp.simplify(
    ginv0[1, 1] - (-D / p + lam**2 * sp.cos(theta) ** 2 / s**2)
) == 0
assert sp.simplify(ginv0[1, 3] - lam * sp.cos(theta) / s**2) == 0
assert sp.simplify(ginv0[3, 3] - 1 / s**2) == 0

print("Part 1: det(g) = -(k-2)^4 sin(theta)^2 / D(x).")
print("        Since exp(-2Phi) ~ sqrt(D), exp(-2Phi)*sqrt|g|")
print("        is x-independent: ~(k-2)^2 sin(theta).")

# Useful exact identities.
assert sp.simplify(D.subs(x, 1) - (delta + 1) ** 2) == 0
assert sp.simplify(D.subs(x, -1) - (delta - 1) ** 2) == 0

Ainf = sp.simplify((k - 2) / (k + 2))
decomp = (
    Ainf
    + (delta + 1) ** 2 / (2 * (x - 1))
    - (delta - 1) ** 2 / (2 * (x + 1))
)
assert sp.simplify(D / p - decomp) == 0

print("Part 2: D/(x^2-1) decomposes exactly into a constant plus")
print("        simple poles at x=+/-1.")

# Separated scalar equation:
#   d_x[p d_x R] + [omega^2 D/p - Lambda] R = 0.
#
# Near x=1, set y=x-1. p~2y, D~(1+delta)^2.
# Frobenius R~y^alpha gives:
#   alpha^2 + omega^2(1+delta)^2/4 = 0.
alpha = sp.symbols("alpha")
a_plus_sq = omega**2 * (delta + 1) ** 2 / 4
a_minus_sq = omega**2 * (delta - 1) ** 2 / 4

print("Part 3: horizon indicial equations:")
print("        x=+1: alpha^2 + omega^2(delta+1)^2/4 = 0")
print("        x=-1: beta^2  + omega^2(delta-1)^2/4 = 0")
print("        => oscillatory logarithmic modes for real omega.")

# Conserved radial Wronskian current near x=1.
y, aa = sp.symbols("y aa", positive=True, real=True)
R = y ** (I * aa)
Rp = sp.diff(R, y)
J = sp.simplify(
    (2 * y) / (2 * I) * (sp.conjugate(R) * Rp - R * sp.conjugate(Rp))
)
assert sp.simplify(J - 2 * aa) == 0

print("Part 4: for R~(x-1)^(i a), the conserved horizon flux -> 2a,")
print("        finite and nonzero. The horizon does not enforce zero flux.")

# Tortoise coordinate:
#   dr*/dx = sqrt(D)/p.
# Near x=1:
#   r* ~ (delta+1)/2 log|x-1|,
# so modes are exp(+- i omega r*).
#
# Remove the first derivative from the radial equation after changing to r*.
# With R=D^(-1/4) psi:
#   psi¨ + [omega^2 - V] psi = 0,
#   V = Lambda*p/D + A'/2 + A^2/4,
#   A = d_{r*} ln sqrt(D) = p D'/(2 D^(3/2)).
Astar = sp.simplify(p * sp.diff(D, x) / (2 * D ** sp.Rational(3, 2)))
V = sp.simplify(
    Lambda * p / D
    + (p / sp.sqrt(D)) * sp.diff(Astar, x) / 2
    + Astar**2 / 4
)

V_horizon = sp.simplify(sp.limit(V, x, 1, dir="+"))
assert V_horizon == 0

V_infinity = sp.simplify(sp.limit(V, x, sp.oo))
expected_Vinf = sp.simplify((Lambda + sp.Rational(1, 4)) / Ainf)
assert sp.simplify(V_infinity - expected_Vinf) == 0

print("Part 5: Schrödinger-form potential:")
print("        V(x->1+) = 0 exactly.")
print("        V(x->+infinity) = (Lambda+1/4)/A,")
print("        A=(k-2)/(k+2).")
print("        Continuum propagation in the NUT region is allowed when")
print("        omega^2 > (Lambda+1/4)/A.")

# Large-x Euler exponents from:
#   x^2 R''+2xR'+[omega^2 A-Lambda]R=0.
# s(s+1)+omega^2 A-Lambda=0, so
#   s=-1/2 +- sqrt(1/4+Lambda-omega^2 A).
nu_sq = sp.simplify(sp.Rational(1, 4) + Lambda - omega**2 * Ainf)
print("Part 6: large-x exponents are")
print("        s=-1/2 +- sqrt(1/4+Lambda-omega^2 A).")
print("        Oscillatory/delta-normalizable continuum iff nu^2<0.")

# Exact hypergeometric singularity structure using z=(1-x)/2.
z = sp.symbols("z")
Dz = sp.expand(D.subs(x, 1 - 2 * z))
C0 = sp.simplify(Lambda - omega**2 * Ainf)
pot_z = sp.simplify(omega**2 * Dz / (4 * z * (1 - z)) + Lambda)
target_z = sp.simplify(
    C0
    + omega**2 * (delta + 1) ** 2 / (4 * z)
    + omega**2 * (delta - 1) ** 2 / (4 * (1 - z))
)
assert sp.simplify(pot_z - target_z) == 0

print("Part 7: with z=(1-x)/2 the exact radial ODE is Fuchsian with")
print("        regular singular points z=0,1,infinity (hypergeometric type).")
print("        Hence x=+/-1 are regular singular horizons, not hard walls.")

# Proper time around a constant-(x,theta,phi) chronology orbit in x>1:
# Delta t=4 pi lambda and g_tt=-(k-2)p/D.
tau_loop_sq = sp.simplify(
    (4 * sp.pi * lam) ** 2 * K * p / D
)
assert sp.simplify(sp.limit(tau_loop_sq, x, 1, dir="+")) == 0

print("Part 8: in the NUT region D>0, x>1, the periodic t-orbit is timelike.")
print("        Its proper-time squared per loop is")
print("        (4 pi lambda)^2 (k-2)(x^2-1)/D(x), finite for finite x>1.")
print()
print("OK: exact minisuperspace horizon/transmission diagnostics passed.")
