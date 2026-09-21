#!/usr/bin/env python3
"""Scale separation between the 2026 heavy-seed simulation and screened-BH physics.

Reference:
Chon et al., Nature 657, 621-625 (2026), DOI 10.1038/s41586-026-10985-8.

The paper's BH accretion zoom reaches ~500 au around a ~10^6 Msun heavy seed;
the cosmological sink radius is typically of order a parsec.  This script
compares those scales with the Schwarzschild radius and with the leading
analytic 4D GQTG asymptotic correction.

For a cubic GQTG-compatible exterior,
    delta f_3 ~ -(27/4) lambda_3 M_geo^2 / r^6,
with lambda_3=ell^4.

The relative correction to the Schwarzschild potential 2M/r is then
    |delta f_3|/(2M/r)
      ~ (27/8) (ell/r)^4 (M/r).

This is parametrically tiny at the AREPO sink/accretion scales whenever
ell is horizon-scale or smaller.
"""

from __future__ import annotations
import math

G = 6.67430e-11
c = 299_792_458.0
MSUN = 1.98847e30
AU = 1.495978707e11
PC = 3.085677581491367e16

def mgeo(m_msun: float) -> float:
    return G * m_msun * MSUN / c**2

def rs(m_msun: float) -> float:
    return 2.0 * mgeo(m_msun)

def cubic_relative_correction(m_msun: float, r_m: float, ell_over_M: float) -> float:
    M = mgeo(m_msun)
    ell = ell_over_M * M
    return (27.0 / 8.0) * (ell / r_m)**4 * (M / r_m)

def main():
    masses = [6e5, 1e6, 3e7]
    radii = {
        "500 au": 500 * AU,
        "5000 au": 5000 * AU,
        "1 pc": PC,
        "10 pc": 10 * PC,
    }

    print("== Heavy-seed simulation scale separation ==")
    for mass in masses:
        print(f"M = {mass:.3g} Msun")
        print(f"  r_s = {rs(mass)/AU:.6g} au")
        for name, radius in radii.items():
            print(f"  {name}: r/r_s = {radius/rs(mass):.6g}")
        print()

    # Fiducial ~10^6 Msun seed, 500 au high-resolution accretion run.
    mass = 1e6
    radius = 500 * AU

    assert radius / rs(mass) > 2.0e4
    assert PC / rs(mass) > 1.0e7

    eps_ell_M = cubic_relative_correction(mass, radius, 1.0)
    eps_ell_10M = cubic_relative_correction(mass, radius, 10.0)

    print("== Cubic GQTG-compatible exterior estimate ==")
    print(f"At M=1e6 Msun, r=500 au:")
    print(f"  ell=M:   |delta f|/(2M/r) ~ {eps_ell_M:.3e}")
    print(f"  ell=10M: |delta f|/(2M/r) ~ {eps_ell_10M:.3e}")
    print()

    assert eps_ell_M < 1e-20
    assert eps_ell_10M < 1e-16

    # ell needed for a 1% correction at 500 au.
    M = mgeo(mass)
    target = 0.01
    ell = (
        target * radius**5 / ((27.0 / 8.0) * M)
    )**0.25

    print("ell required for a 1% cubic correction at 500 au:")
    print(f"  ell/M = {ell/M:.6g}")
    print(f"  ell = {ell/AU:.6g} au")
    print(f"  ell/r = {ell/radius:.6g}")
    print()

    assert ell > radius

    print(
        "Conclusion: for any horizon-scale or microscopic screening length, "
        "the published simulation's resolved gas dynamics are effectively "
        "insensitive to the screened interior.  The simulation is therefore "
        "best used as an external feeding/formation boundary condition."
    )
    print("All scale-separation assertions passed.")

if __name__ == "__main__":
    main()
