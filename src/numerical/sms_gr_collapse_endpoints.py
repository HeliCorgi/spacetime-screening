#!/usr/bin/env python3
"""Dimensionless GR endpoint observables for rotating SMS collapse.

Published benchmarks:
- Shibata & Shapiro (2002): a uniformly rotating mass-shedding SMS collapses
  to a BH containing ~90% of the mass, dimensionless spin ~0.75, with ~10%
  remaining in a disk.
- Fujibayashi et al. (2025): rotating SMS-core collapse forms a BH; rapidly
  rotating cases produce shock-driven ejecta saturating at ~1% of the core
  mass, mean velocity ~0.2c, and kinetic/explosion energy up to ~1e-4 Mc^2.

This script converts those dimensionless scales for representative heavy-seed
masses.  It is a benchmark calculator, not a new collapse simulation.
"""

from __future__ import annotations

G = 6.67430e-8          # cgs
C = 2.99792458e10       # cm/s
MSUN = 1.98847e33       # g

SHIBATA_BH_MASS_FRACTION = 0.90
SHIBATA_BH_SPIN = 0.75
SHIBATA_DISK_FRACTION = 0.10

FUJIBAYASHI_EJECTA_FRACTION = 0.01
FUJIBAYASHI_EJECTA_V_OVER_C = 0.20
FUJIBAYASHI_ENERGY_FRACTION = 1e-4


def mass_energy_erg(m_msun: float) -> float:
    return m_msun * MSUN * C**2


def gravitational_time_s(m_msun: float) -> float:
    return G * m_msun * MSUN / C**3


def main() -> None:
    print("== Rotating SMS GR endpoint benchmark ==")
    for mass in (1e5, 3e5, 1e6):
        e0 = mass_energy_erg(mass)
        tg = gravitational_time_s(mass)

        print(f"M={mass:.3g} Msun")
        print(
            f"  Shibata-Shapiro: M_BH~"
            f"{SHIBATA_BH_MASS_FRACTION*mass:.3g} Msun, "
            f"a_BH~{SHIBATA_BH_SPIN:.2f}, "
            f"M_disk~{SHIBATA_DISK_FRACTION*mass:.3g} Msun"
        )
        print(
            f"  Fujibayashi-scale: M_ej~"
            f"{FUJIBAYASHI_EJECTA_FRACTION*mass:.3g} Msun, "
            f"v_ej~{FUJIBAYASHI_EJECTA_V_OVER_C:.2f}c, "
            f"E~{FUJIBAYASHI_ENERGY_FRACTION*e0:.3e} erg"
        )
        print(f"  t_g={tg:.6g} s")
        print()

        assert 0 < tg
        assert (
            SHIBATA_BH_MASS_FRACTION
            + SHIBATA_DISK_FRACTION
            == 1.0
        )

    e_1e6 = FUJIBAYASHI_ENERGY_FRACTION * mass_energy_erg(1e6)
    assert 1e56 < e_1e6 < 2e56

    print(
        "Screened-collapse comparison vector:"
        " {t_AH, M_AH/M, a, M_disk/M, M_ej/M, E_ej/(Mc^2)}."
    )
    print(
        "If no apparent horizon forms, replace horizon observables by "
        "{R_min, K_max, M_core/M}."
    )
    print("All rotating-SMS endpoint assertions passed.")


if __name__ == "__main__":
    main()
