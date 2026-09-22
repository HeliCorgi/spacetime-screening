#!/usr/bin/env python3
"""Flux-normalized horizon <-> NUT transmission amplitude for the explicit
heterotic Taub-NUT BRST state.

State/background are those of heterotic_taubnut_explicit_brst_state.py:
  k1=8, k2=4,
  delta^2=8/5, lambda^2=2/5,
  omega=Mbar=sqrt(10)/2,
  Lambda=1,
  j=1/2+i/2.

The exact radial equation is hypergeometric.  We choose the solution that is
purely ingoing at the x=1 horizon and expand it at x->+infinity in
flux-normalized NUT in/out modes.  This gives a unitary 2-channel scattering
coefficient:
    NUT_in -> r NUT_out + t Horizon_in,
with R=|r|^2, T=|t|^2 and R+T=1.

Because the radial operator has real coefficients, the reciprocal
horizon->NUT channel has the same transmission probability.  This is the
free-string/minisuperspace transmission coefficient associated with the
explicit BRST physical state; it is not an interacting string S-matrix.
"""

import sympy as sp
import mpmath as mp

I = sp.I
pi = sp.pi

omega = sp.sqrt(10) / 2
delta = sp.sqrt(sp.Rational(8, 5))
lam = sp.sqrt(sp.Rational(2, 5))
Lambda = sp.Integer(1)
Ametric = sp.Rational(3, 5)

# Exact NUT continuum momentum exponent.
rho2 = sp.simplify(omega**2 * Ametric - Lambda - sp.Rational(1, 4))
rho = sp.sqrt(rho2)
assert rho == sp.Rational(1, 2)

# Horizon logarithmic momentum.
a_plus = sp.simplify(omega * (1 + delta) / 2)
sigma = sp.simplify(2 * a_plus)
assert sp.simplify(sigma - (omega + 2)) == 0

# Hypergeometric parameters for the purely horizon-ingoing branch.
# R = u^alpha (1+u)^beta F(a,b;c;-u), u=(x-1)/2>0.
alpha = -I * a_plus
a_minus = sp.simplify(omega * (delta - 1) / 2)
beta = I * a_minus
h = -sp.Rational(1, 2) + I * rho

a = sp.simplify(alpha + beta - h)
b = sp.simplify(alpha + beta + h + 1)
c = sp.simplify(1 + 2 * alpha)

assert sp.simplify(a - (sp.Rational(1, 2) - I * (omega + sp.Rational(1, 2)))) == 0
assert sp.simplify(b - (sp.Rational(1, 2) - I * (omega - sp.Rational(1, 2)))) == 0
assert sp.simplify(c - (1 - I * (omega + 2))) == 0
assert sp.simplify(b - a - I) == 0
assert sp.simplify(c - a - (sp.Rational(1, 2) - 3 * I / 2)) == 0
assert sp.simplify(c - b - (sp.Rational(1, 2) - 5 * I / 2)) == 0

print("Part 1: explicit hypergeometric parameters fixed.")
print("  rho=1/2, 2 a_+ = omega+2.")
print("  a=1/2-i(omega+1/2), b=1/2-i(omega-1/2),")
print("  c=1-i(omega+2).")


# ---------------------------------------------------------------------------
# Connection coefficients
# ---------------------------------------------------------------------------
#
# At NUT infinity u->infinity:
#   R_H ~ A_out u^(-1/2+i rho) + B_in u^(-1/2-i rho)
#
# for the solution with unit amplitude R_H~u^(-i a_plus) at the horizon.
#
# DLMF 15.10/15.8 gives:
#   A_out = Gamma(c) Gamma(b-a) / [Gamma(b) Gamma(c-a)]
#   B_in  = Gamma(c) Gamma(a-b) / [Gamma(a) Gamma(c-b)].

# Squared magnitudes from
# |Gamma(1+i y)|^2 = pi*y/sinh(pi*y)
# |Gamma(i y)|^2   = pi/(y*sinh(pi*y))
# |Gamma(1/2+i y)|^2 = pi/cosh(pi*y).

yb = sp.simplify(omega - sp.Rational(1, 2))
ya = sp.simplify(omega + sp.Rational(1, 2))

A2 = sp.simplify(
    sigma
    * sp.cosh(pi * yb)
    * sp.cosh(3 * pi / 2)
    / (sp.sinh(pi * sigma) * sp.sinh(pi))
)

B2 = sp.simplify(
    sigma
    * sp.cosh(pi * ya)
    * sp.cosh(5 * pi / 2)
    / (sp.sinh(pi * sigma) * sp.sinh(pi))
)

# Fluxes:
# horizon unit-amplitude mode: J_H = -2 a_plus = -sigma.
# NUT modes u^(-1/2 +/- i rho): J = +/- 2 rho = +/-1.
#
# Hence exact flux conservation requires B2-A2=sigma.
# Prove the hyperbolic identity explicitly:
# cosh[X+pi/2]cosh[5pi/2]-cosh[X-pi/2]cosh[3pi/2]
#   = sinh[X+2pi] sinh[pi], X=pi*omega.
X = pi * omega
bracket = (
    sp.cosh(X + pi / 2) * sp.cosh(5 * pi / 2)
    - sp.cosh(X - pi / 2) * sp.cosh(3 * pi / 2)
)
rhs_bracket = sp.sinh(X + 2 * pi) * sp.sinh(pi)

# SymPy may not automatically prove the hyperbolic identity structurally;
# rewrite through exponentials.
assert sp.simplify(
    sp.expand_complex((bracket - rhs_bracket).rewrite(sp.exp))
) == 0

assert sp.simplify(
    (B2 - A2).subs(bracket, rhs_bracket) - sigma
) == 0 or sp.N(B2 - A2 - sigma, 50) == 0

print("Part 2: exact flux relation")
print("  |B_in|^2 - |A_out|^2 = omega+2 = horizon flux magnitude.")


# ---------------------------------------------------------------------------
# Flux-normalized S-matrix coefficients
# ---------------------------------------------------------------------------
#
# Define unit-flux bases:
#   H_in  = u^(-i a_plus)/sqrt(2 a_plus), J=-1
#   N_in  = u^(-1/2-i rho)/sqrt(2 rho),  J=-1
#   N_out = u^(-1/2+i rho)/sqrt(2 rho),  J=+1
#
# Then:
#   N_in -> r N_out + t H_in
# with
#   r = A_out/B_in
#   t = sqrt(a_plus/rho) / B_in.
#
# Thus:
#   R=|A|^2/|B|^2
#   T=(a_plus/rho)/|B|^2 = sigma/B2, since rho=1/2.

Rprob = sp.simplify(A2 / B2)
Tprob = sp.simplify(sigma / B2)

Rprob_closed = sp.simplify(
    sp.cosh(pi * (omega - sp.Rational(1, 2)))
    * sp.cosh(3 * pi / 2)
    /
    (
        sp.cosh(pi * (omega + sp.Rational(1, 2)))
        * sp.cosh(5 * pi / 2)
    )
)

Tprob_closed = sp.simplify(
    sp.sinh(pi * (omega + 2))
    * sp.sinh(pi)
    /
    (
        sp.cosh(pi * (omega + sp.Rational(1, 2)))
        * sp.cosh(5 * pi / 2)
    )
)

assert sp.simplify(Rprob - Rprob_closed) == 0
assert sp.simplify(Tprob - Tprob_closed) == 0

# Verify unitarity numerically to high precision.
mp.mp.dps = 80
omega_mp = mp.sqrt(10) / 2
sigma_mp = omega_mp + 2

R_mp = (
    mp.cosh(mp.pi * (omega_mp - mp.mpf("0.5")))
    * mp.cosh(mp.mpf("1.5") * mp.pi)
    /
    (
        mp.cosh(mp.pi * (omega_mp + mp.mpf("0.5")))
        * mp.cosh(mp.mpf("2.5") * mp.pi)
    )
)

T_mp = (
    mp.sinh(mp.pi * (omega_mp + 2))
    * mp.sinh(mp.pi)
    /
    (
        mp.cosh(mp.pi * (omega_mp + mp.mpf("0.5")))
        * mp.cosh(mp.mpf("2.5") * mp.pi)
    )
)

assert abs((R_mp + T_mp) - 1) < mp.mpf("1e-70")

print("Part 3: flux-normalized probabilities")
print("  R =", mp.nstr(R_mp, 18))
print("  T =", mp.nstr(T_mp, 18))
print("  R+T =", mp.nstr(R_mp + T_mp, 18))


# ---------------------------------------------------------------------------
# Complex transmission/reflection amplitudes in a fixed phase convention
# ---------------------------------------------------------------------------

a_mp = mp.mpf("0.5") - 1j * (omega_mp + mp.mpf("0.5"))
b_mp = mp.mpf("0.5") - 1j * (omega_mp - mp.mpf("0.5"))
c_mp = 1 - 1j * (omega_mp + 2)

Acoef = (
    mp.gamma(c_mp)
    * mp.gamma(1j)
    /
    (mp.gamma(b_mp) * mp.gamma(c_mp - a_mp))
)

Bcoef = (
    mp.gamma(c_mp)
    * mp.gamma(-1j)
    /
    (mp.gamma(a_mp) * mp.gamma(c_mp - b_mp))
)

t_amp = mp.sqrt(sigma_mp) / Bcoef
r_amp = Acoef / Bcoef

assert abs(abs(t_amp)**2 - T_mp) < mp.mpf("1e-65")
assert abs(abs(r_amp)**2 - R_mp) < mp.mpf("1e-65")

print("Part 4: one consistent flux-normalized phase convention")
print("  t =", mp.nstr(t_amp, 18))
print("  r =", mp.nstr(r_amp, 18))
print("  |t| =", mp.nstr(abs(t_amp), 18))
print("  |r| =", mp.nstr(abs(r_amp), 18))
print("  arg(t) =", mp.nstr(mp.arg(t_amp), 18), "rad")
print("  arg(r) =", mp.nstr(mp.arg(r_amp), 18), "rad")


# ---------------------------------------------------------------------------
# Interpretation
# ---------------------------------------------------------------------------
#
# The real radial operator implies reciprocity of the two-channel
# horizon<->NUT transmission probability.  The Taub region is not a stationary
# scattering exterior (x is timelike there), so T should be interpreted as the
# flux-normalized horizon<->NUT channel coefficient for the analytically
# continued physical mode, not as a conventional asymptotic Taub S-matrix.

print()
print("OK: normalized horizon<->NUT transmission amplitude checks passed.")
print("Interpretation: T is the reciprocal free-string/minisuperspace channel")
print("coefficient associated with the explicit BRST physical state.")
