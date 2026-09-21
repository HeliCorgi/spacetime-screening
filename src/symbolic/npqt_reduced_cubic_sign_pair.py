#!/usr/bin/env python3
"""Match the aligned NPQT sign pair to the published 2D reduced cubic density.

Source: Bueno--Cano--Hennigar--Murcia, arXiv:2509.19016.

For a general spherical metric the source defines

    Omega = 2 psi/3 + R2/3 + 2 B/3,
    Theta = psi/2 - R2/4,

where
    B = Box(phi)/phi,

and the four-dimensional Ricci scalar is

    R4 = R2 - 4 B + 2 psi.

Solving at fixed (Omega, Theta, R4) gives

    psi = Omega/2 + Theta + R4/12,
    R2  = Omega - 2 Theta + R4/6,
    B   = Omega/2 - R4/6.

On the aligned Ricci stratum the 2D Hessian is pure trace,
    nabla_mu nabla_nu phi = (B phi/2) gamma_mu_nu,
so
    t_phi / phi^2 = -B^2/4.

The published cubic spherical density is

    Z3_2d =
      6 psi^3
      + 12 psi^2 B
      + 3 psi^2 R2
      - 24 psi t_phi/phi^2.

Substitution gives

    Z3_2d(+Theta)-Z3_2d(-Theta)
      = 27 Omega^2 Theta.

For the spherical Weyl normalization used in the repository,
    W2 = 3 Omega^2
(equivalently Omega=4q),
so the difference is exactly

    9 W2 Theta,

matching the independent full four-dimensional cubic-density sign-pair gate.

This isolates the remaining escape route: only equivalence of the reduced
action up to a 2D boundary/total-derivative term can evade the pointwise
density obstruction while preserving spherical equations.
"""

from __future__ import annotations

import sympy as sp

Omega, Theta, R4 = sp.symbols("Omega Theta R4", real=True)

psi = sp.factor(Omega / 2 + Theta + R4 / 12)
R2 = sp.factor(Omega - 2 * Theta + R4 / 6)
B = sp.factor(Omega / 2 - R4 / 6)

assert sp.simplify(
    (2 * psi / 3 + R2 / 3 + 2 * B / 3) - Omega
) == 0
assert sp.simplify(psi / 2 - R2 / 4 - Theta) == 0
assert sp.simplify(R2 - 4 * B + 2 * psi - R4) == 0

t_over_phi2 = -B**2 / 4

Z3red = sp.factor(
    6 * psi**3
    + 12 * psi**2 * B
    + 3 * psi**2 * R2
    - 24 * psi * t_over_phi2
)

Zplus = sp.factor(Z3red)
Zminus = sp.factor(Z3red.subs(Theta, -Theta))
difference = sp.factor(Zplus - Zminus)

assert difference == 27 * Omega**2 * Theta

W2 = 3 * Omega**2
assert sp.simplify(difference - 9 * W2 * Theta) == 0

q = sp.symbols("q", real=True)
assert sp.simplify(W2.subs(Omega, 4 * q) - 48 * q**2) == 0

def main() -> None:
    print("== NPQT reduced cubic sign-pair check ==")
    print(f"psi   = {psi}")
    print(f"R2    = {R2}")
    print(f"B     = {B}")
    print(f"t/phi^2 = {t_over_phi2}")
    print()
    print(f"Z3_2d = {Z3red}")
    print(f"Delta Z3_2d = {difference}")
    print(f"W2 = {W2}")
    print("Delta Z3_2d = 9 W2 Theta.")
    print()
    print("Conclusion: the sign-pair distinction is present in the published")
    print("2D spherical reduction itself, not only in one 4D rational chart.")
    print("All reduced-density assertions passed.")

if __name__ == "__main__":
    main()
