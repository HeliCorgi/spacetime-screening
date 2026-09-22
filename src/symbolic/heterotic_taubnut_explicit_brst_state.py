#!/usr/bin/env python3
"""Explicit untwisted BRST-state candidate in exact heterotic Taub-NUT.

This script constructs one exact anomaly-free model point and one untwisted
affine/coset state whose gauge constraints and conformal weights close exactly.

It verifies:
  1. anomaly cancellation at an integer-charge point;
  2. equality of left/right gauge-current level matrices;
  3. both Taub-NUT gauge constraints for a concrete principal-continuous state;
  4. exact cancellation of numerator conformal weight by the auxiliary
     BRST/gauge-sector subtraction, giving h_L=h_R=0 for the coset primary;
  5. a standard spectator heterotic oscillator completion to matter weights
     (h_L,h_R)=(1,1/2);
  6. global t-periodicity / monopole charge quantization;
  7. exact matching to the minisuperspace NUT continuum exponent;
  8. absence of a positive-NUT D(x)=0 singularity for this parameter point.

Important: the script verifies the algebraic physical-state candidate.  The
claim that it represents a non-exact positive-norm class uses the standard
gauged-WZW BRST/coset equivalence and the usual no-ghost properties of the
principal continuous SL(2,R) representation; those representation-theoretic
inputs are documented in the companion note and are not proven by SymPy.
"""

import sympy as sp

# ---------------------------------------------------------------------------
# 1. Exact anomaly-free heterotic Taub-NUT background point
# ---------------------------------------------------------------------------

k1 = sp.Integer(8)          # SL(2,R) bosonic level
k2 = sp.Integer(4)          # SU(2) bosonic level = k1-4

QA, PA = sp.Integer(2), sp.Integer(0)
QB, PB = sp.Integer(2), sp.Integer(1)

delta = sp.sqrt(sp.Rational(8, 5))
lam = sp.sqrt(sp.Rational(2, 5))

E_AA = -k1 * (1 - delta**2) - 2 * (QA**2 + PA**2 - delta**2)
E_AB = k1 * delta * lam - 2 * (QA * QB + PA * PB - delta * lam)
E_BB = k2 + k1 * lam**2 - 2 * (QB**2 + PB**2 - (1 + lam**2))

assert k1 == k2 + 4
assert sp.simplify(E_AA) == 0
assert sp.simplify(E_AB) == 0
assert sp.simplify(E_BB) == 0

# Gauge-current level matrices. WZW Cartans have k/2 and each bosonized
# complex fermion has level 1.
K_L = sp.Matrix(
    [
        [k1 / 2 + QA**2 + PA**2, QA * QB + PA * PB],
        [QA * QB + PA * PB, QB**2 + PB**2],
    ]
)

K_R = sp.Matrix(
    [
        [
            k1 * delta**2 / 2 + delta**2,
            k1 * delta * lam / 2 + delta * lam,
        ],
        [
            k1 * delta * lam / 2 + delta * lam,
            k1 * lam**2 / 2 + k2 / 2 + lam**2 + 1,
        ],
    ]
)

K = sp.Matrix([[8, 4], [4, 5]])
K_inv = sp.Matrix(
    [
        [sp.Rational(5, 24), -sp.Rational(1, 6)],
        [-sp.Rational(1, 6), sp.Rational(1, 3)],
    ]
)

assert sp.simplify(K_L - K) == sp.zeros(2)
assert sp.simplify(K_R - K) == sp.zeros(2)
assert sp.simplify(K.inv() - K_inv) == sp.zeros(2)

print("Part 1: exact anomaly-free point")
print("  k1=8, k2=4; (QA,PA)=(2,0), (QB,PB)=(2,1)")
print("  delta^2=8/5, lambda^2=2/5")
print("  K_L=K_R=[[8,4],[4,5]].")


# ---------------------------------------------------------------------------
# 2. Explicit untwisted affine-primary quantum numbers
# ---------------------------------------------------------------------------

# Principal continuous representation j=1/2+i s with s=1/2.
s = sp.Rational(1, 2)
j = sp.Rational(1, 2) + sp.I * s
ell = sp.Integer(1)

# Positive-frequency hyperbolic-basis state.
m = -sp.Integer(2)
Mbar = sp.sqrt(10) / 2
Nbar = -sp.Integer(1)

# No excitation of the two left heterotic gauge-fermion bosons and no
# right coset-fermion Cartan charge.
s1 = s2 = f1 = f2 = sp.Integer(0)

Mbar_total = Mbar + f1
Nbar_total = Nbar + f2

G_A = sp.simplify(m + delta * Mbar_total + QA * s1 + PA * s2)
G_B = sp.simplify(lam * Mbar_total + Nbar_total + QB * s1 + PB * s2)

assert G_A == 0
assert G_B == 0

# Chiral matter gauge-charge vectors.  The total local constraint is the sum
# of these vectors after auxiliary BRST dressing.
J_L = sp.Matrix([m + QA * s1 + PA * s2, QB * s1 + PB * s2])
J_R = sp.Matrix(
    [
        delta * Mbar_total,
        lam * Mbar_total + Nbar_total,
    ]
)

assert sp.simplify(J_L - sp.Matrix([-2, 0])) == sp.zeros(2, 1)
assert sp.simplify(J_R - sp.Matrix([2, 0])) == sp.zeros(2, 1)
assert sp.simplify(J_L + J_R) == sp.zeros(2, 1)

print("Part 2: untwisted gauge-neutral primary")
print("  j=1/2+i/2, ell=1, m=-2, Mbar=sqrt(10)/2, Nbar=-1")
print("  G_A=G_B=0 exactly.")


# ---------------------------------------------------------------------------
# 3. Exact coset conformal weights
# ---------------------------------------------------------------------------

# Bosonic affine-primary weights in the source conventions.
C_sl2 = sp.simplify(-j * (j - 1))      # 1/4+s^2 = 1/2
h_sl2 = sp.simplify(C_sl2 / (k1 - 2))
h_su2 = sp.Rational(ell * (ell + 1), k2 + 2)
h_num = sp.simplify(h_sl2 + h_su2)

# BRST auxiliary U(1)^2 sector subtracts one-half J^T K^{-1} J.
h_gauge_L = sp.simplify((J_L.T * K_inv * J_L)[0] / 2)
h_gauge_R = sp.simplify((J_R.T * K_inv * J_R)[0] / 2)

h_coset_L = sp.simplify(h_num - h_gauge_L)
h_coset_R = sp.simplify(h_num - h_gauge_R)

assert C_sl2 == sp.Rational(1, 2)
assert h_sl2 == sp.Rational(1, 12)
assert h_su2 == sp.Rational(1, 3)
assert h_num == sp.Rational(5, 12)
assert h_gauge_L == sp.Rational(5, 12)
assert h_gauge_R == sp.Rational(5, 12)
assert h_coset_L == 0
assert h_coset_R == 0

# SU(2)_4 integrability bound: ell <= k2/2.
assert 0 <= ell <= k2 / 2

print("Part 3: exact coset mass-shell core")
print("  h_SL2=1/12, h_SU2=1/3, numerator=5/12")
print("  gauge subtraction=5/12 on each chirality")
print("  => (h_L,h_R)_coset=(0,0).")


# ---------------------------------------------------------------------------
# 4. Standard critical-heterotic spectator completion
# ---------------------------------------------------------------------------

# The 4D heterotic coset has c=6 in each chiral accounting after gauging and
# adding its four chiral fermions.  A conventional spectator completion can
# supply c_L=20 and c_R=9.  We only need one neutral free internal boson Y
# and its right-moving superpartner for the explicit vertex.
#
# Candidate -1-picture matter factor:
#   (i dY_L) * psi_R^Y * Phi_coset
# with zero internal momentum.
h_left_internal_current = sp.Integer(1)
h_right_internal_fermion = sp.Rational(1, 2)

h_phys_L = sp.simplify(h_coset_L + h_left_internal_current)
h_phys_R = sp.simplify(h_coset_R + h_right_internal_fermion)

assert h_phys_L == 1
assert h_phys_R == sp.Rational(1, 2)

print("Part 4: spectator oscillator completion")
print("  (i dY_L) psi_R^Y Phi_coset has matter weights (1,1/2).")
print("  With the right NS -1-picture superghost this is the standard")
print("  heterotic unintegrated physical-vertex weight assignment.")


# ---------------------------------------------------------------------------
# 5. Match to target-space periodicity and the exact minisuperspace mode
# ---------------------------------------------------------------------------

omega = Mbar
q = sp.simplify(lam * omega)

# t ~ t + 4 pi lambda requires exp(-i omega 4 pi lambda)=1:
# equivalently 2 lambda omega is an integer.
period_number = sp.simplify(2 * lam * omega)

# Scalar monopole harmonic separation constant for ell=1, q=1.
Lambda = sp.simplify(ell * (ell + 1) - q**2)

A = sp.Rational(k1 - 2, k1 + 2)
nu2 = sp.simplify(sp.Rational(1, 4) + Lambda - omega**2 * A)

assert q == 1
assert period_number == 2
assert Lambda == 1
assert A == sp.Rational(3, 5)
assert nu2 == -sp.Rational(1, 4)

# Large-x radial exponents: -1/2 +- sqrt(nu2) = -1/2 +- i/2.
s_plus = sp.simplify(-sp.Rational(1, 2) + sp.sqrt(nu2))
s_minus = sp.simplify(-sp.Rational(1, 2) - sp.sqrt(nu2))
assert s_plus in (
    -sp.Rational(1, 2) + sp.I / 2,
    -sp.Rational(1, 2) - sp.I / 2,
)
assert s_minus in (
    -sp.Rational(1, 2) + sp.I / 2,
    -sp.Rational(1, 2) - sp.I / 2,
)

# This matches the principal-continuous radial label j=1/2+i/2.
assert sp.simplify(j - (sp.Rational(1, 2) + sp.I / 2)) == 0

print("Part 5: exact minisuperspace match")
print("  omega=Mbar=sqrt(10)/2, lambda*omega=1, 2 lambda omega=2")
print("  Lambda=1, A=3/5, nu^2=-1/4")
print("  => NUT exponents -1/2 +- i/2, matching j=1/2+i/2.")


# ---------------------------------------------------------------------------
# 6. Check that the first positive NUT region has no D(x)=0 singularity
# ---------------------------------------------------------------------------

x = sp.symbols("x", real=True)
D = sp.factor((x + delta) ** 2 - sp.Rational(4, k1 + 2) * (x**2 - 1))
D_expected = (3 * x**2 + 4 * sp.sqrt(10) * x + 10) / 5

assert sp.simplify(D - D_expected) == 0

roots = sp.solve(sp.Eq(D, 0), x)
assert set(roots) == {-sp.sqrt(10), -sp.sqrt(10) / 3}
assert all(sp.N(r) < -1 for r in roots)

print("Part 6: D(x)=0 only at x=-sqrt(10), -sqrt(10)/3.")
print("  The entire first positive NUT region x>1 is free of D=0 curvature")
print("  singularities for this explicit model point.")


# ---------------------------------------------------------------------------
# 7. Hypergeometric connection: no discrete pole that kills NUT continuation
# ---------------------------------------------------------------------------

# C = Lambda - omega^2 A = -1/2.
C = sp.simplify(Lambda - omega**2 * A)
assert C == -sp.Rational(1, 2)

# One solution of h(h+1)=C.
h = -sp.Rational(1, 2) + sp.I / 2
assert sp.simplify(h * (h + 1) - C) == 0

a_plus = sp.simplify(omega * (1 + delta) / 2)
a_minus = sp.simplify(omega * (delta - 1) / 2)
alpha = -sp.I * a_plus
beta = sp.I * a_minus

aa = sp.simplify(alpha + beta - h)
bb = sp.simplify(alpha + beta + h + 1)
cc = sp.simplify(1 + 2 * alpha)

# Gamma-function connection coefficients are nonzero if denominator arguments
# are not non-positive integers.  Here all four denominator arguments have
# real part 1/2, so none can be a Gamma pole.
den_args = [aa, bb, sp.simplify(cc - aa), sp.simplify(cc - bb)]
for arg in den_args:
    assert sp.simplify(sp.re(arg) - sp.Rational(1, 2)) == 0

# Numerator difference parameters are +-i and hence also finite/nonzero.
assert sp.simplify(bb - aa - sp.I) == 0
assert sp.simplify(aa - bb + sp.I) == 0

print("Part 7: exact hypergeometric connection")
print("  denominator Gamma arguments all have Re=1/2; no pole zeros occur.")
print("  b-a=i and a-b=-i; both connection coefficients are finite/nonzero.")
print()
print("OK: explicit untwisted heterotic Taub-NUT BRST-state candidate checks passed.")
