#!/usr/bin/env python3
"""Degeneracy of the explicit 4D covariant lift on single-function metrics.

Based on Borissova & Carballo-Rubio, Phys. Rev. D 113, 124004 (2026).

Their explicit representative lift uses the covariant densities
  H, T, P, K
which reduce on warped-product backgrounds to
  eta, tau, psi, R2D.

The two densities P and K contain the common denominator
  D = I_C2 * I_R2C + 2 I_Rhat2 * I_C3.

Using the warped-product invariant identities, this factorizes as
  D = -(eta^2 - 2 tau) * Omega^3 / 3.

For the single-function static ansatz n(r)=1,
  tau = eta^2/2
identically, so D=0 everywhere on the desired Hayward solution.

The corresponding numerators vanish by the same factor and the reduced
ratios have removable limits:
  P -> psi
  K -> R2D.

Thus the reduced spherical theory is well defined, but the displayed
four-dimensional rational lift is 0/0 on the exact single-function branch.
A generic nonspherical principal-symbol calculation requires a regular
extension/alternative covariant lift before varying off that branch.
"""

from __future__ import annotations

import sympy as sp


R, eta, tau, psi = sp.symbols(
    "R eta tau psi", finite=True
)

rho = R - 4*eta + 2*psi
Omega = R + 2*eta + 2*psi

Sigma = (
    sp.Rational(1,4)*R**2
    - R*psi
    - 2*eta**2
    + 4*tau
    + psi**2
)

IhatR3 = (
    -sp.Rational(3,2)*R*eta**2
    + 3*R*tau
    + 3*eta**2*psi
    - 6*tau*psi
)

IC2 = Omega**2 / 3
IC3 = Omega**3 / 18
IR2C = -Omega * (
    eta**2 - 2*tau + Sigma/3
)

A = eta**2 - 2*tau

D = sp.factor(
    IC2*IR2C + 2*Sigma*IC3
)

NP = sp.factor(
    IhatR3*IC3
)

P_lift = (
    rho/sp.Integer(12)
    + IC3/IC2
    - NP/D
)

NK = sp.factor(
    sp.Rational(1,6)*rho*IC2*IR2C
    + sp.Rational(1,3)*rho*Sigma*IC3
    + 4*Sigma*IC3**2/IC2
    + 2*IhatR3*IC3
    + 2*IC3*IR2C
)

K_lift = NK/D

H_lift = sp.factor(
    -rho/sp.Integer(6) + IC3/IC2
)

T_lift = sp.factor(
    sp.Rational(1,72)*rho**2
    + sp.Rational(1,6)*Sigma
    - sp.Rational(1,6)*rho*IC3/IC2
    + sp.Rational(1,2)*IC3**2/IC2**2
    + sp.Rational(1,12)*IC2*IR2C/IC3
)


def main():
    expected_D = sp.factor(
        -A*Omega**3/3
    )
    expected_NP = sp.factor(
        -A*(R-2*psi)*Omega**3/12
    )
    expected_NK = sp.factor(
        -R*A*Omega**3/3
    )

    assert sp.simplify(D-expected_D)==0
    assert sp.simplify(NP-expected_NP)==0
    assert sp.simplify(NK-expected_NK)==0

    # Cancel the common factor before imposing the single-function condition.
    P_reduced = sp.factor(
        rho/sp.Integer(12)
        + IC3/IC2
        - expected_NP/expected_D
    )
    K_reduced = sp.factor(
        expected_NK/expected_D
    )

    assert sp.simplify(P_reduced-psi)==0
    assert sp.simplify(K_reduced-R)==0
    assert sp.simplify(H_lift-eta)==0
    assert sp.simplify(T_lift-tau)==0

    # Single-function branch: tau = eta^2/2.
    sf = {tau: eta**2/2}
    assert sp.simplify(D.subs(sf))==0
    assert sp.simplify(NP.subs(sf))==0
    assert sp.simplify(NK.subs(sf))==0

    # Off-branch regulator A=delta makes the limiting structure explicit.
    delta = sp.symbols("delta", nonzero=True)
    tau_delta = (eta**2-delta)/2

    D_delta = sp.factor(
        D.subs(tau,tau_delta)
    )
    NP_delta = sp.factor(
        NP.subs(tau,tau_delta)
    )
    NK_delta = sp.factor(
        NK.subs(tau,tau_delta)
    )

    assert sp.simplify(
        D_delta + delta*Omega**3/3
    )==0

    assert sp.simplify(
        NP_delta/D_delta - (R-2*psi)/4
    )==0

    assert sp.simplify(
        NK_delta/D_delta - R
    )==0

    print("== Warped-product invariant identities ==")
    print(f"D = {D}")
    print(f"N_P = {NP}")
    print(f"N_K = {NK}")
    print()

    print("== Single-function branch n=1 ==")
    print("tau = eta^2/2")
    print(f"D -> {sp.simplify(D.subs(sf))}")
    print(f"N_P -> {sp.simplify(NP.subs(sf))}")
    print(f"N_K -> {sp.simplify(NK.subs(sf))}")
    print("Therefore the displayed P and K formulas are 0/0.")
    print()

    print("== Removable spherical limits ==")
    print(f"P -> {P_reduced}")
    print(f"K -> {K_reduced}")
    print(f"H -> {H_lift}")
    print(f"T -> {T_lift}")
    print()

    print("== Off-branch regulator A=delta ==")
    print(f"D(delta) = {D_delta}")
    print(f"N_P/D = {sp.factor(NP_delta/D_delta)}")
    print(f"N_K/D = {sp.factor(NK_delta/D_delta)}")
    print()

    print(
        "Conclusion: the spherical reduction has a finite removable limit, "
        "but the explicit rational 4D lift is indeterminate on the exact "
        "single-function solution before choosing an off-branch extension."
    )
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
