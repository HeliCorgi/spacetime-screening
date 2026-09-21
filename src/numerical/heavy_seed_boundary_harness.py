#!/usr/bin/env python3
"""Offline heavy-seed boundary harness for Spacetime Screening.

Primary source:
Chon et al., Nature 657, 621-625 (2026)
DOI 10.1038/s41586-026-10985-8
arXiv:2601.04955

This file intentionally does NOT pretend that Fig. 1 source data are public.
The Nature data-availability statement says inputs/configuration/initial
conditions are public, while full simulation outputs are available from the
corresponding author on reasonable request.

Instead, this harness uses only source-stated anchor points and qualitative
accretion-rate phases from data/heavy_seed_source_envelope.csv.

The goal is to define a clean interface:

    cosmological outer feeding history
        -> inner closure(M, mdot, state)
        -> luminosity / radiative efficiency / feedback observables

No screened-BH closure is assumed here.  The baseline closure reproduces
Eq. (4) of Chon et al.; alternative closures can be injected as callables.
"""

from __future__ import annotations

from dataclasses import dataclass
import csv
import math
from pathlib import Path
from typing import Callable, Iterable


# Cosmology used in the paper.
OMEGA_M = 0.31
OMEGA_L = 0.69
H0_KM_S_MPC = 68.0
MPC_M = 3.085677581491367e22
SEC_PER_YR = 365.25 * 24.0 * 3600.0

# Eddington luminosity in erg/s per solar mass.
L_EDD_PER_MSUN = 1.26e38


def cosmic_age_gyr(z: float) -> float:
    """Age in Gyr for flat matter+Lambda cosmology, neglecting radiation.

    Adequate here as a bookkeeping conversion for z~8-14 anchors.
    """
    if z < 0:
        raise ValueError("redshift must be nonnegative")
    H0 = H0_KM_S_MPC * 1000.0 / MPC_M
    pref = 2.0 / (3.0 * H0 * math.sqrt(OMEGA_L))
    arg = math.sqrt(OMEGA_L / OMEGA_M) / (1.0 + z) ** 1.5
    return pref * math.asinh(arg) / SEC_PER_YR / 1e9


def chon_slim_disk_l_over_ledd(mdot_edd: float) -> float:
    """Eq. (4) of Chon et al. in dimensionless form.

    mdot_edd = Mdot_acc / Mdot_Edd.
    For mdot<=2, the stated epsilon_r=0.1 definition gives L/L_Edd=mdot.
    For mdot>2, use the paper's logarithmic slim-disk branch.
    """
    if mdot_edd < 0:
        raise ValueError("mdot_edd must be nonnegative")
    if mdot_edd <= 2.0:
        return mdot_edd
    return 2.0 * (1.0 + math.log(mdot_edd / 2.0))


@dataclass(frozen=True)
class InnerBoundaryOutput:
    l_over_ledd: float
    epsilon_relative_to_chon: float = 1.0
    wind_mass_fraction: float = 0.0
    kinetic_fraction: float = 0.0


Closure = Callable[[float, float, str], InnerBoundaryOutput]


def chon_baseline_closure(
    mass_msun: float,
    mdot_edd: float,
    state: str,
) -> InnerBoundaryOutput:
    del mass_msun, state
    return InnerBoundaryOutput(
        l_over_ledd=chon_slim_disk_l_over_ledd(mdot_edd),
    )


def rescaled_test_closure(
    mass_msun: float,
    mdot_edd: float,
    state: str,
    *,
    luminosity_factor: float = 1.0,
    wind_mass_fraction: float = 0.0,
    kinetic_fraction: float = 0.0,
) -> InnerBoundaryOutput:
    """Model-agnostic placeholder for a future screened-BH inner solution.

    The parameters are deliberately phenomenological.  They are not claims
    about spacetime screening; they only expose the interface needed for
    sensitivity tests before a real strong-field accretion model exists.
    """
    del mass_msun, state
    if luminosity_factor < 0:
        raise ValueError("luminosity_factor must be nonnegative")
    if not (0 <= wind_mass_fraction < 1):
        raise ValueError("wind_mass_fraction must lie in [0,1)")
    if kinetic_fraction < 0:
        raise ValueError("kinetic_fraction must be nonnegative")
    return InnerBoundaryOutput(
        l_over_ledd=(
            luminosity_factor
            * chon_slim_disk_l_over_ledd(mdot_edd)
        ),
        epsilon_relative_to_chon=luminosity_factor,
        wind_mass_fraction=wind_mass_fraction,
        kinetic_fraction=kinetic_fraction,
    )


# Operational numeric interpretations for prose-only ranges.
# These are NOT claimed to be digitized Fig. 1 data.
DESCRIPTOR_BOUNDS = {
    "several_to_few_tens": (3.0, 30.0),
    "0.1_to_1": (0.1, 1.0),
    "lt_0.01": (0.0, 0.01),
}


def descriptor_bounds(descriptor: str) -> tuple[float, float] | None:
    if not descriptor:
        return None
    try:
        return DESCRIPTOR_BOUNDS[descriptor]
    except KeyError as exc:
        raise ValueError(f"unknown descriptor: {descriptor}") from exc


def lbol_erg_s(mass_msun: float, l_over_ledd: float) -> float:
    return mass_msun * L_EDD_PER_MSUN * l_over_ledd


def load_source_envelope(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def evaluate_phase(
    mass_msun: float,
    descriptor: str,
    state: str,
    closure: Closure = chon_baseline_closure,
) -> dict[str, float]:
    bounds = descriptor_bounds(descriptor)
    if bounds is None:
        raise ValueError("phase requires an Eddington descriptor")
    lo, hi = bounds
    out_lo = closure(mass_msun, lo, state)
    out_hi = closure(mass_msun, hi, state)
    return {
        "mdot_lo": lo,
        "mdot_hi": hi,
        "l_over_ledd_lo": out_lo.l_over_ledd,
        "l_over_ledd_hi": out_hi.l_over_ledd,
        "lbol_lo_erg_s": lbol_erg_s(mass_msun, out_lo.l_over_ledd),
        "lbol_hi_erg_s": lbol_erg_s(mass_msun, out_hi.l_over_ledd),
    }


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    source_path = root / "data" / "heavy_seed_source_envelope.csv"
    rows = load_source_envelope(source_path)

    print("== Source-stated redshift anchors ==")
    anchors = []
    for row in rows:
        if row["z"]:
            z = float(row["z"])
            age = cosmic_age_gyr(z)
            anchors.append((z, age, row["event"], row["mass_msun"]))
            print(
                f"z={z:4.1f} age={age:.4f} Gyr "
                f"event={row['event']} mass={row['mass_msun'] or 'n/a'}"
            )

    # Cosmic time increases as redshift decreases.
    anchors_sorted = sorted(anchors, reverse=True)
    ages = [x[1] for x in anchors_sorted]
    assert all(b > a for a, b in zip(ages, ages[1:]))

    # Explicit source anchors.
    t14 = cosmic_age_gyr(14.0)
    t10 = cosmic_age_gyr(10.0)
    t8 = cosmic_age_gyr(8.0)
    assert 0 < t10 - t14 < 0.3
    assert 0 < t8 - t10 < 0.3

    print()
    print("Elapsed cosmic time:")
    print(f"z=14 -> z=10: {(t10-t14)*1e3:.2f} Myr")
    print(f"z=10 -> z=8:  {(t8-t10)*1e3:.2f} Myr")

    print()
    print("== Chon et al. luminosity envelope ==")

    # Use masses only where the paper supplies an explicit anchor.
    phases = [
        (6e5, "several_to_few_tens", "early_super_eddington"),
        (1e7, "lt_0.01", "z10_low_state"),
        (3e7, "0.1_to_1", "z8_central_growth"),
    ]

    for mass, descriptor, state in phases:
        q = evaluate_phase(mass, descriptor, state)
        print(
            f"{state}: M={mass:.3g} Msun, "
            f"mdot=[{q['mdot_lo']:.3g},{q['mdot_hi']:.3g}], "
            f"L/LEdd=[{q['l_over_ledd_lo']:.3g},"
            f"{q['l_over_ledd_hi']:.3g}], "
            f"Lbol=[{q['lbol_lo_erg_s']:.3e},"
            f"{q['lbol_hi_erg_s']:.3e}] erg/s"
        )

    # Check the slim-disk branch is sublinear at high mdot.
    assert chon_slim_disk_l_over_ledd(30.0) < 30.0
    assert chon_slim_disk_l_over_ledd(2.0) == 2.0
    assert chon_slim_disk_l_over_ledd(0.1) == 0.1

    print()
    print("== Interface sensitivity example (not a screening prediction) ==")
    base = evaluate_phase(
        6e5,
        "several_to_few_tens",
        "early_super_eddington",
    )
    half = evaluate_phase(
        6e5,
        "several_to_few_tens",
        "early_super_eddington",
        closure=lambda m, md, s: rescaled_test_closure(
            m, md, s, luminosity_factor=0.5
        ),
    )
    print(
        "A purely phenomenological 50% luminosity transfer rescales the "
        f"early envelope from L/LEdd <= {base['l_over_ledd_hi']:.3g} "
        f"to <= {half['l_over_ledd_hi']:.3g}."
    )
    print(
        "Replace this placeholder by a screened-BH inner accretion closure "
        "once one is derived."
    )

    assert math.isclose(
        half["l_over_ledd_hi"],
        0.5 * base["l_over_ledd_hi"],
    )

    print()
    print("All heavy-seed boundary-harness assertions passed.")


if __name__ == "__main__":
    main()
