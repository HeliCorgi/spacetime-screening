#!/usr/bin/env python3
"""BH SED adapter for the Chon et al. heavy-seed benchmark.

Primary source:
Chon et al., Nature 657, 621-625 (2026)
DOI 10.1038/s41586-026-10985-8
arXiv:2601.04955

The paper models accreting-BH radiation as a double power law:

    F_nu ~ nu^-0.6   from 1 eV to 10 eV
    F_nu ~ nu^-1.5   from 10 eV to 1 keV.

The source passage gives slopes and energy ranges but does not spell out the
relative normalization of the two pieces.  This adapter adopts continuity at
10 eV as an explicit interface assumption.

Given L_bol, the script computes:
- fraction of bolometric power above 13.6 eV;
- mean energy of ionizing photons;
- hydrogen-ionizing photon production rate Q_H.

This is an interface calculation, not a new astrophysical claim.
"""

from __future__ import annotations

from dataclasses import dataclass
import math

EV_TO_ERG = 1.602176634e-12

E_MIN = 1.0
E_BREAK = 10.0
E_ION = 13.6
E_MAX = 1000.0

ALPHA_LOW = -0.6
ALPHA_HIGH = -1.5


def integral_power(lo: float, hi: float, power: float) -> float:
    if lo <= 0 or hi <= lo:
        raise ValueError("require 0 < lo < hi")
    q = power + 1.0
    if abs(q) < 1e-14:
        return math.log(hi / lo)
    return (hi**q - lo**q) / q


# If L_E=A E^alpha_low below the break and B E^alpha_high above it,
# continuity at E_BREAK gives B/A=E_BREAK^(alpha_low-alpha_high).
HIGH_TO_LOW_NORM = E_BREAK ** (ALPHA_LOW - ALPHA_HIGH)


@dataclass(frozen=True)
class SEDSummary:
    ionizing_energy_fraction: float
    mean_ionizing_energy_ev: float
    q_h_per_erg_s: float


def baseline_summary() -> SEDSummary:
    low_energy = integral_power(E_MIN, E_BREAK, ALPHA_LOW)
    high_energy = (
        HIGH_TO_LOW_NORM
        * integral_power(E_BREAK, E_MAX, ALPHA_HIGH)
    )
    total_energy = low_energy + high_energy

    ion_energy = (
        HIGH_TO_LOW_NORM
        * integral_power(E_ION, E_MAX, ALPHA_HIGH)
    )

    # Photon-number integral is integral L_E/E dE.
    ion_number_shape = (
        HIGH_TO_LOW_NORM
        * integral_power(E_ION, E_MAX, ALPHA_HIGH - 1.0)
    )

    frac = ion_energy / total_energy
    mean_ev = ion_energy / ion_number_shape
    q_per_lbol = frac / (mean_ev * EV_TO_ERG)

    return SEDSummary(
        ionizing_energy_fraction=frac,
        mean_ionizing_energy_ev=mean_ev,
        q_h_per_erg_s=q_per_lbol,
    )


def ionizing_outputs(lbol_erg_s: float) -> dict[str, float]:
    if lbol_erg_s < 0:
        raise ValueError("luminosity must be nonnegative")
    s = baseline_summary()
    lion = s.ionizing_energy_fraction * lbol_erg_s
    qh = s.q_h_per_erg_s * lbol_erg_s
    return {
        "l_ion_erg_s": lion,
        "q_h_s^-1": qh,
        "mean_ionizing_energy_ev": s.mean_ionizing_energy_ev,
    }


def main() -> None:
    s = baseline_summary()

    print("== Chon et al. broken-power-law SED adapter ==")
    print("Assumption: the two power-law pieces are continuous at 10 eV.")
    print(f"high/low normalization B/A = {HIGH_TO_LOW_NORM:.9g}")
    print(
        "ionizing energy fraction (>13.6 eV) = "
        f"{s.ionizing_energy_fraction:.9f}"
    )
    print(
        "mean ionizing photon energy = "
        f"{s.mean_ionizing_energy_ev:.6f} eV"
    )
    print(
        "Q_H / L_bol = "
        f"{s.q_h_per_erg_s:.6e} photons erg^-1"
    )
    print()

    # Basic range checks.
    assert 0.0 < s.ionizing_energy_fraction < 1.0
    assert E_ION < s.mean_ionizing_energy_ev < E_MAX

    # Stable reference values for the adopted continuity convention.
    assert math.isclose(
        s.ionizing_energy_fraction,
        0.45842925165406545,
        rel_tol=1e-12,
    )
    assert math.isclose(
        s.mean_ionizing_energy_ev,
        36.099197263496826,
        rel_tol=1e-12,
    )

    example = ionizing_outputs(1e44)
    print("For L_bol=1e44 erg/s:")
    print(f"  L_ion = {example['l_ion_erg_s']:.6e} erg/s")
    print(f"  Q_H   = {example['q_h_s^-1']:.6e} s^-1")

    assert 7.0e53 < example["q_h_s^-1"] < 9.0e53

    print()
    print(
        "Use this adapter only for the paper's baseline spectral shape. "
        "A screened-BH model may replace the spectral transfer function."
    )
    print("All SED-adapter assertions passed.")


if __name__ == "__main__":
    main()
