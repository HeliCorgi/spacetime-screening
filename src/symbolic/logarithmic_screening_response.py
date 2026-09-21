#!/usr/bin/env python3
"""Dimensionless logarithmic screening response for the Hayward relation.

For the spherical response
    psi(s) = s/(1 + ell^2 s),

define the dimensionless logarithmic response ("screening elasticity")
    S_log = d ln psi / d ln s
          = (s/psi) dpsi/ds.

For Hayward,
    S_log = 1/(1+ell^2 s)
          = 1-ell^2 psi
          = r^3/(r^3+2 M ell^2).

Thus the radial function previously called a diagnostic G_eff/G is exactly
the fractional logarithmic curvature response to a fractional source change.

GR: S_log = 1.
Deep screened regime: S_log -> 0.
"""

from __future__ import annotations

import sympy as sp


s,ell,M,r=sp.symbols(
    "s ell M r", positive=True, finite=True
)

psi=sp.factor(s/(1+ell**2*s))
dpsi=sp.factor(sp.diff(psi,s))

Slog=sp.factor(s*dpsi/psi)
Sigma=sp.factor(1-ell**2*psi)

source=2*M/r**3
Slog_r=sp.factor(Slog.subs(s,source))

# A second dimensionless measure: incremental vs secant response.
# psi/s is the average response from 0 to s; dpsi/ds is incremental.
incremental_ratio=sp.factor(
    dpsi/(psi/s)
)


def main():
    expected=sp.factor(1/(1+ell**2*s))
    assert sp.simplify(Slog-expected)==0
    assert sp.simplify(Sigma-expected)==0
    assert sp.simplify(incremental_ratio-Slog)==0

    expected_r=sp.factor(
        r**3/(r**3+2*M*ell**2)
    )
    assert sp.simplify(Slog_r-expected_r)==0

    assert sp.limit(Slog,s,0)==1
    assert sp.limit(Slog,s,sp.oo)==0

    # Relation to beta_eff defined previously.
    beta_eff=sp.factor(
        -s*sp.diff(sp.log(dpsi),s)
    )
    relation=sp.factor(2*(1-Slog))
    assert sp.simplify(beta_eff-relation)==0

    # Response flow with log source:
    # dS/dlns = s dS/ds = -S(1-S)
    flow=sp.factor(s*sp.diff(Slog,s))
    expected_flow=sp.factor(-Slog*(1-Slog))
    assert sp.simplify(flow-expected_flow)==0

    # psi saturation can be reconstructed from S.
    # ell^2 psi = 1-S
    assert sp.simplify(ell**2*psi-(1-Slog))==0

    print("== Dimensionless logarithmic screening ==")
    print(f"psi(s) = {psi}")
    print(f"dpsi/ds = {dpsi}")
    print(f"S_log = d ln(psi)/d ln(s) = {Slog}")
    print(f"1-ell^2 psi = {Sigma}")
    print()
    print("S_log = incremental response / average response")
    print(f"= {incremental_ratio}")
    print()
    print("On the Hayward solution:")
    print(f"S_log(r) = {Slog_r}")
    print()
    print("Limits:")
    print(f"S_log(s->0) = {sp.limit(Slog,s,0)}")
    print(f"S_log(s->infty) = {sp.limit(Slog,s,sp.oo)}")
    print()
    print("Response-flow identity:")
    print(f"dS_log/d ln s = {flow}")
    print("= -S_log(1-S_log)")
    print()
    print(f"beta_eff = {beta_eff} = 2(1-S_log)")
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
