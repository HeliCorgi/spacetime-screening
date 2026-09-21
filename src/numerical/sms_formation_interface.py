#!/usr/bin/env python3
"""Formation-gate interface for cosmological SMS accretion histories.

This module deliberately separates three levels:

1. Constant-accretion GR instability threshold:
   piecewise log-log interpolation of Saio et al. (2024) Table 1.

2. Constant-accretion post-GRI fate:
   exact discrete Pop III outcomes from Nagele & Umeda (2024).
   NO interpolation of fate labels.

3. Variable accretion history:
   requires a real stellar-evolution/stability solver.  The interface refuses
   to collapse a variable history to a single "effective mdot" automatically.

This policy is motivated by Woods et al. (2021), who showed that realistic
cosmological variable accretion histories produce structurally diverse SMSs
and direct-collapse masses around 1--2e5 Msun in their models.

The module is plumbing, not a replacement for stellar evolution.
"""

from __future__ import annotations

from dataclasses import dataclass
import csv
from pathlib import Path
from typing import Sequence

from sms_gri_benchmark import GRIPoint, load_points, loglog_interpolate


@dataclass(frozen=True)
class AccretionSample:
    time_yr: float
    mdot_msun_per_yr: float


@dataclass(frozen=True)
class ConstantRateAssessment:
    mdot: float
    mcrit_gr: float
    post_gri_fate_if_tabulated: str | None


def load_fates(path: Path) -> dict[float, str]:
    with path.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    return {
        float(r["mdot_msun_per_yr"]): r["outcome"]
        for r in rows
        if float(r["metallicity_zsun"]) == 0.0
    }


def assess_constant_rate(
    mdot: float,
    gri_points: list[GRIPoint],
    fates: dict[float, str],
) -> ConstantRateAssessment:
    mcrit = loglog_interpolate(gri_points, mdot)
    return ConstantRateAssessment(
        mdot=mdot,
        mcrit_gr=mcrit,
        post_gri_fate_if_tabulated=fates.get(mdot),
    )


def assess_variable_history(
    history: Sequence[AccretionSample],
) -> None:
    """Refuse a fake effective-rate collapse closure.

    A variable history changes entropy, core fraction, burning stage and
    thermal relaxation; these are not encoded by a time-averaged mdot alone.
    """
    if len(history) < 2:
        raise ValueError("variable history requires at least two samples")
    if any(s.mdot_msun_per_yr < 0 for s in history):
        raise ValueError("accretion rates must be nonnegative")
    if any(b.time_yr <= a.time_yr for a, b in zip(history, history[1:])):
        raise ValueError("history times must be strictly increasing")

    raise NotImplementedError(
        "Variable accretion histories require a stellar-evolution + "
        "relativistic-stability solver; do not replace them by a single "
        "effective mdot."
    )


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    gri_points = load_points(root / "data" / "sms_gri_gr_benchmark.csv")
    fates = load_fates(root / "data" / "sms_post_gri_fates.csv")

    print("== Constant-rate formation-gate examples ==")
    for mdot in (0.1, 0.3, 1.0, 10.0, 100.0):
        a = assess_constant_rate(mdot, gri_points, fates)
        fate = a.post_gri_fate_if_tabulated or "not tabulated"
        print(
            f"mdot={mdot:g}: "
            f"Mcrit_GR~{a.mcrit_gr:.6g} Msun; "
            f"post-GRI fate={fate}"
        )

    # Exact source rows.
    assert assess_constant_rate(
        1.0, gri_points, fates
    ).post_gri_fate_if_tabulated == "pulsation"
    assert assess_constant_rate(
        100.0, gri_points, fates
    ).post_gri_fate_if_tabulated == "collapse"

    # A variable history must not silently reduce to an average.
    history = [
        AccretionSample(0.0, 0.2),
        AccretionSample(1e5, 1.0),
        AccretionSample(2e5, 0.05),
    ]
    try:
        assess_variable_history(history)
    except NotImplementedError:
        pass
    else:
        raise AssertionError("variable history must require a real solver")

    print()
    print(
        "Variable-accretion histories intentionally return no fate. "
        "Use a stellar-evolution/stability solver before coupling to the "
        "screened-collapse stage."
    )
    print("All SMS formation-interface assertions passed.")


if __name__ == "__main__":
    main()
