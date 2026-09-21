#!/usr/bin/env python3
"""Sensitivity layer connecting the heavy-seed outer benchmark to an inner closure.

This script combines:
- heavy_seed_boundary_harness.py
- heavy_seed_sed_adapter.py

It does not assume a specific spacetime-screening accretion solution.
Instead it reports how a generic change in inner radiative transfer would
propagate into the ionizing feedback variable Q_H used by the outer
radiation-hydrodynamic problem.

The example parameters are deliberately labelled as interface tests, not
predictions.
"""

from __future__ import annotations

import math

from heavy_seed_boundary_harness import (
    evaluate_phase,
    rescaled_test_closure,
)
from heavy_seed_sed_adapter import ionizing_outputs


PHASES = [
    # mass, source descriptor, state
    (6e5, "several_to_few_tens", "early_super_eddington"),
    (1e7, "lt_0.01", "z10_low_state"),
    (3e7, "0.1_to_1", "z8_central_growth"),
]


def phase_feedback(
    mass_msun: float,
    descriptor: str,
    state: str,
    *,
    luminosity_factor: float = 1.0,
    wind_mass_fraction: float = 0.0,
) -> dict[str, float]:
    phase = evaluate_phase(
        mass_msun,
        descriptor,
        state,
        closure=lambda m, md, s: rescaled_test_closure(
            m,
            md,
            s,
            luminosity_factor=luminosity_factor,
            wind_mass_fraction=wind_mass_fraction,
        ),
    )

    q_lo = ionizing_outputs(phase["lbol_lo_erg_s"])["q_h_s^-1"]
    q_hi = ionizing_outputs(phase["lbol_hi_erg_s"])["q_h_s^-1"]

    return {
        **phase,
        "q_h_lo_s^-1": q_lo,
        "q_h_hi_s^-1": q_hi,
        # Pure bookkeeping placeholder: fraction of supplied mass not
        # immediately assigned to a wind at the inner boundary.
        "retained_supply_fraction": 1.0 - wind_mass_fraction,
    }


def main() -> None:
    print("== Heavy-seed feedback sensitivity interface ==")
    print(
        "Example only: compare the Chon-et-al. baseline with a closure "
        "that emits 50% of the baseline luminosity and assigns 30% of the "
        "inner supply to winds."
    )
    print()

    for mass, descriptor, state in PHASES:
        base = phase_feedback(mass, descriptor, state)
        test = phase_feedback(
            mass,
            descriptor,
            state,
            luminosity_factor=0.5,
            wind_mass_fraction=0.3,
        )

        q_ratio_lo = (
            test["q_h_lo_s^-1"] / base["q_h_lo_s^-1"]
            if base["q_h_lo_s^-1"] > 0 else float("nan")
        )
        q_ratio_hi = (
            test["q_h_hi_s^-1"] / base["q_h_hi_s^-1"]
            if base["q_h_hi_s^-1"] > 0 else float("nan")
        )

        print(state)
        print(f"  M = {mass:.3g} Msun")
        print(
            "  baseline Q_H range = "
            f"[{base['q_h_lo_s^-1']:.3e}, "
            f"{base['q_h_hi_s^-1']:.3e}] s^-1"
        )
        print(
            "  test Q_H range     = "
            f"[{test['q_h_lo_s^-1']:.3e}, "
            f"{test['q_h_hi_s^-1']:.3e}] s^-1"
        )
        print(
            "  retained inner supply fraction = "
            f"{test['retained_supply_fraction']:.2f}"
        )
        print()

        # Same SED shape means Q_H scales exactly with L_bol.
        if base["q_h_lo_s^-1"] > 0:
            assert math.isclose(q_ratio_lo, 0.5, rel_tol=1e-12)
        if base["q_h_hi_s^-1"] > 0:
            assert math.isclose(q_ratio_hi, 0.5, rel_tol=1e-12)
        assert math.isclose(
            test["retained_supply_fraction"],
            0.7,
            rel_tol=1e-12,
        )

    print(
        "Interpretation: once a genuine screened-BH inner solution supplies "
        "its luminosity, spectrum and outflow closure, this interface maps "
        "those outputs directly onto the cosmological feedback variables."
    )
    print("All feedback-sensitivity assertions passed.")


if __name__ == "__main__":
    main()
