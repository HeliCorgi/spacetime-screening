#!/usr/bin/env python3
"""Pure-gravity quasitopological Hayward screening benchmark.

Based on Borissova & Carballo-Rubio,
Phys. Rev. D 113, 124004 (2026), DOI 10.1103/6x2z-qbkh.

For the single-function spherical ansatz define
    psi = (1-f)/r^2.

The Hayward nonpolynomial quasitopological characteristic function is
    H(psi) = 6 psi/(1-ell^2 psi).

The vacuum algebraic equation is
    H(psi) = 12 M/r^3.

Equivalently, with source variable s=2M/r^3,
    h(psi)=psi/(1-ell^2 psi)=s.

This script shows:
- exact recovery of the Hayward metric;
- curvature-response saturation psi -> 1/ell^2;
- vanishing susceptibility dpsi/ds -> 0 at high source;
- the diagnostic screening factor equals 1-ell^2 psi;
- no auxiliary-field cancellation is required at the spherical background level.
"""

from __future__ import annotations

import sympy as sp


r,M,ell,s,psi=sp.symbols(
    "r M ell s psi", positive=True, finite=True
)


def main():
    H=sp.factor(6*psi/(1-ell**2*psi))
    h=sp.factor(H/6)

    # Solve h(psi)=s on the GR-connected branch.
    psi_of_s=sp.solve(sp.Eq(h,s),psi)[0]
    expected=sp.factor(s/(1+ell**2*s))
    assert sp.simplify(psi_of_s-expected)==0

    susceptibility=sp.factor(sp.diff(psi_of_s,s))
    curvature_second=sp.factor(sp.diff(psi_of_s,s,2))

    assert sp.simplify(
        susceptibility-1/(1+ell**2*s)**2
    )==0
    assert sp.simplify(
        curvature_second+2*ell**2/(1+ell**2*s)**3
    )==0

    # Insert the spherical vacuum source s=2M/r^3.
    source=2*M/r**3
    psi_r=sp.factor(psi_of_s.subs(s,source))
    expected_psi_r=sp.factor(
        2*M/(r**3+2*M*ell**2)
    )
    assert sp.simplify(psi_r-expected_psi_r)==0

    f=sp.factor(1-r**2*psi_r)
    expected_f=sp.factor(
        1-2*M*r**2/(r**3+2*M*ell**2)
    )
    assert sp.simplify(f-expected_f)==0

    # Screening factor: distance from the pole in curvature space.
    Sigma=sp.factor(1-ell**2*psi_r)
    expected_sigma=sp.factor(
        r**3/(r**3+2*M*ell**2)
    )
    assert sp.simplify(Sigma-expected_sigma)==0

    # Susceptibility along the solution is Sigma^2.
    susc_r=sp.factor(susceptibility.subs(s,source))
    assert sp.simplify(susc_r-Sigma**2)==0

    # Limits.
    assert sp.limit(psi_of_s,s,0)==0
    assert sp.limit(psi_of_s,s,sp.oo)==1/ell**2
    assert sp.limit(susceptibility,s,0)==1
    assert sp.limit(susceptibility,s,sp.oo)==0
    assert sp.limit(Sigma,r,sp.oo)==1
    assert sp.limit(Sigma,r,0)==0

    # Recover standard Hayward core curvature invariants.
    fp=sp.diff(f,r)
    fpp=sp.diff(f,r,2)
    R=sp.factor(-fpp-4*fp/r+2*(1-f)/r**2)
    Ricci2=sp.factor(
        2*(fpp/2+fp/r)**2
        +2*(fp/r+(f-1)/r**2)**2
    )
    K=sp.factor(
        fpp**2
        +4*(fp/r)**2
        +4*((1-f)/r**2)**2
    )

    assert sp.simplify(sp.limit(R,r,0)-12/ell**2)==0
    assert sp.simplify(
        sp.limit(Ricci2,r,0)-36/ell**4
    )==0
    assert sp.simplify(sp.limit(K,r,0)-24/ell**4)==0

    # Curvature distance to the saturation point.
    gap=sp.factor(1/ell**2-psi_r)
    expected_gap=sp.factor(
        r**3/(ell**2*(r**3+2*M*ell**2))
    )
    assert sp.simplify(gap-expected_gap)==0

    print("== Characteristic function ==")
    print(f"H(psi) = {H}")
    print(f"h(psi) = {h}")
    print()
    print("== Curvature response ==")
    print(f"psi(s) = {psi_of_s}")
    print(f"dpsi/ds = {susceptibility}")
    print(f"d2psi/ds2 = {curvature_second}")
    print("psi -> 1/ell^2 and dpsi/ds -> 0 as s -> infinity")
    print()
    print("== Vacuum spherical solution ==")
    print(f"s(r) = {source}")
    print(f"psi(r) = {psi_r}")
    print(f"f(r) = {f}")
    print()
    print("== Intrinsic screening factor ==")
    print(f"Sigma(r) = 1-ell^2 psi = {Sigma}")
    print(f"dpsi/ds = Sigma^2 = {susc_r}")
    print()
    print("== Center invariants ==")
    print(f"R(0) = {sp.limit(R,r,0)}")
    print(f"Ricci^2(0) = {sp.limit(Ricci2,r,0)}")
    print(f"K(0) = {sp.limit(K,r,0)}")
    print()
    print("All symbolic assertions passed.")


if __name__=="__main__":
    main()
