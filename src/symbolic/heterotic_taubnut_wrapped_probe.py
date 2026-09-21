#!/usr/bin/env python3
"""Exact heterotic Taub-NUT wrapped-string horizon diagnostic.

Source conventions follow Johnson & Svendsen (2004), exact string-frame metric:

    ds^2 = (k-2) {
        dx^2/(x^2-1)
        - (x^2-1)/D(x) (dt + 2 lambda A_phi^M dphi)^2
        + dtheta^2 + sin^2(theta) dphi^2
    },

    D(x) = (x+delta)^2 - 4/(k+2) (x^2-1),

with exact dilaton

    Phi-Phi0 = -(1/4) log D(x),

and periodic fiber coordinate t ~ t + 4 pi lambda.

At fixed angular coordinates take the diagnostic closed-string embedding

    x=x(tau),
    t=2 lambda w sigma,
    0 <= sigma < 2 pi,

with integer winding w.

This script verifies:
- the embedding closes under the exact target-space periodicity;
- the induced determinant is
      det h = -(k-2)^2 (2 lambda w)^2 xdot^2 / D(x);
- the apparent (x^2-1) factor cancels exactly;
- at x=1, D=(1+delta)^2 > 0 for delta>=1, so the Nambu-Goto
  area density is finite for finite xdot;
- the exact dilaton/string coupling is also finite at x=1.

This is a REPRODUCED HERE / diagnostic result only.  It does not impose
heterotic BRST/Virasoro constraints, normalizability, interaction consistency,
or establish operational CTC traversal.
"""

from __future__ import annotations

import sympy as sp

x, k, delta, lam, w, xdot = sp.symbols(
    "x k delta lambda w xdot",
    real=True,
)
pi = sp.pi

D = sp.factor((x + delta) ** 2 - sp.Rational(4, 1) / (k + 2) * (x**2 - 1))

g_xx = sp.factor((k - 2) / (x**2 - 1))
g_tt = sp.factor(-(k - 2) * (x**2 - 1) / D)

dt_dsigma = 2 * lam * w

h_tautau = sp.factor(g_xx * xdot**2)
h_sigmasigma = sp.factor(g_tt * dt_dsigma**2)
h_tausigma = sp.Integer(0)

det_h = sp.factor(h_tautau * h_sigmasigma - h_tausigma**2)
expected_det = sp.factor(
    -(k - 2) ** 2 * (2 * lam * w) ** 2 * xdot**2 / D
)

assert sp.simplify(det_h - expected_det) == 0

# Target-space closure: sigma -> sigma+2pi shifts t by one integer multiple
# of the exact period 4 pi lambda.
delta_t = sp.simplify(dt_dsigma * 2 * pi)
target_period = 4 * pi * lam
assert sp.simplify(delta_t - w * target_period) == 0

D_plus = sp.factor(D.subs(x, 1))
D_minus = sp.factor(D.subs(x, -1))
assert D_plus == (1 + delta) ** 2
assert D_minus == (delta - 1) ** 2

det_plus = sp.factor(expected_det.subs(x, 1))
assert det_plus == -4 * lam**2 * w**2 * xdot**2 * (k - 2) ** 2 / (delta + 1) ** 2

# Exact dilaton: Phi-Phi0 = -1/4 log D.
# Thus exp(Phi-Phi0) = D^{-1/4}.  At x=1 and delta>=1 this is finite.
gs_ratio_fourth_power = sp.factor(1 / D)
gs_plus_fourth_power = sp.factor(gs_ratio_fourth_power.subs(x, 1))
assert gs_plus_fourth_power == 1 / (delta + 1) ** 2

# Near-horizon cancellation check by x=1+eps.
eps = sp.symbols("eps", real=True)
near = sp.factor(expected_det.subs(x, 1 + eps))
near_limit = sp.factor(sp.limit(near, eps, 0))
assert sp.simplify(near_limit - det_plus) == 0

# Causal character of the periodic fiber:
# for D>0 and k>2, sign(g_tt) = -sign(x^2-1).
# Taub: |x|<1 -> spacelike fiber; NUT x>1 -> timelike fiber.
gtt_plus_side = sp.factor(g_tt.subs(x, 1 + eps))


def main() -> None:
    print("== Exact heterotic Taub-NUT wrapped-probe diagnostic ==")
    print(f"D(x) = {D}")
    print(f"g_xx = {g_xx}")
    print(f"g_tt = {g_tt}")
    print()
    print(f"t(sigma+2pi)-t(sigma) = {delta_t}")
    print(f"target period = {target_period}")
    print()
    print(f"det h = {det_h}")
    print(f"D(1) = {D_plus}")
    print(f"lim_(x->1) det h = {near_limit}")
    print(f"[exp(Phi-Phi0)]^4 at x=1 = {gs_plus_fourth_power}")
    print()
    print("Conclusion:")
    print("The exact chronology horizon x=1 is not an automatic local")
    print("Nambu-Goto area-density singularity for this fixed-angle winding")
    print("diagnostic.  The x^2-1 factors cancel, and the exact dilaton is")
    print("finite there.  Full heterotic physical-state constraints remain")
    print("to be imposed before interpreting this as string traversal.")
    print("All wrapped-probe assertions passed.")


if __name__ == "__main__":
    main()
