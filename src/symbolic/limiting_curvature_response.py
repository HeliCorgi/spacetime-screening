#!/usr/bin/env python3
"""Limiting-curvature asymptotics for the Hayward QTG response.

For source variable s and curvature response
    psi(s)=s/(1+ell^2 s),

the large-s derivatives scale as
    psi'  ~ 1/(ell^4 s^2),
    psi'' ~ -2/(ell^4 s^3).

This corresponds to beta=2 in the sufficient inverse-response falloff
criterion discussed for quasitopological limiting curvature in 2026.
"""

from __future__ import annotations

import sympy as sp


s,ell=sp.symbols("s ell", positive=True, finite=True)


def main():
    psi=sp.factor(s/(1+ell**2*s))
    d1=sp.factor(sp.diff(psi,s))
    d2=sp.factor(sp.diff(psi,s,2))
    d3=sp.factor(sp.diff(psi,s,3))

    assert sp.simplify(d1-1/(1+ell**2*s)**2)==0
    assert sp.simplify(d2+2*ell**2/(1+ell**2*s)**3)==0
    assert sp.simplify(d3-6*ell**4/(1+ell**2*s)**4)==0

    # Extract asymptotic coefficients.
    c1=sp.simplify(sp.limit(s**2*d1,s,sp.oo))
    c2=sp.simplify(sp.limit(s**3*d2,s,sp.oo))
    c3=sp.simplify(sp.limit(s**4*d3,s,sp.oo))

    assert sp.simplify(c1-1/ell**4)==0
    assert sp.simplify(c2+2/ell**4)==0
    assert sp.simplify(c3-6/ell**4)==0

    # Saturation gap.
    gap=sp.factor(1/ell**2-psi)
    assert sp.simplify(
        gap-1/(ell**2*(1+ell**2*s))
    )==0

    gap_coeff=sp.simplify(sp.limit(s*gap,s,sp.oo))
    assert sp.simplify(gap_coeff-1/ell**4)==0

    # Logarithmic response exponent:
    # beta_eff = - d log(psi') / d log(s)
    beta_eff=sp.factor(-s*sp.diff(sp.log(d1),s))
    assert sp.simplify(
        beta_eff-2*ell**2*s/(1+ell**2*s)
    )==0
    assert sp.limit(beta_eff,s,0)==0
    assert sp.limit(beta_eff,s,sp.oo)==2

    print("== Hayward inverse curvature response ==")
    print(f"psi(s) = {psi}")
    print(f"psi'(s) = {d1}")
    print(f"psi''(s) = {d2}")
    print(f"psi'''(s) = {d3}")
    print()
    print("== Large-source asymptotics ==")
    print(f"s^2 psi' -> {c1}")
    print(f"s^3 psi'' -> {c2}")
    print(f"s^4 psi''' -> {c3}")
    print(f"s (1/ell^2-psi) -> {gap_coeff}")
    print()
    print(f"beta_eff(s) = {beta_eff}")
    print(f"beta_eff -> {sp.limit(beta_eff,s,sp.oo)}")
    print()
    print("The asymptotic inverse-response exponent is beta=2 > 1.")
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
