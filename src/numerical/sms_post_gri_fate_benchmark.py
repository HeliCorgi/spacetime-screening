#!/usr/bin/env python3
"""Post-GRI fate benchmark for rapidly accreting Pop III supermassive stars.

Primary source:
Nagele & Umeda, Phys. Rev. D 110, L061301 (2024),
arXiv:2408.08352.

The source performs 1D GR hydrodynamics after the radial GR instability.
For the Pop III (Z=0) models, Table I gives non-monotonic outcomes:
collapse to a BH at some accretion rates and thermonuclear pulsations at
others.

This benchmark deliberately does NOT interpolate the outcome in accretion
rate.  The source outcomes are non-monotonic and depend on stellar structure,
core fraction, nuclear burning, and numerical/network details.

The purpose is to prevent an invalid closure:
    GRI onset -> automatic BH particle.
"""

from __future__ import annotations

import csv
from pathlib import Path


def load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    rows = load(root / "data" / "sms_post_gri_fates.csv")

    assert len(rows) == 7
    assert all(float(r["metallicity_zsun"]) == 0.0 for r in rows)

    outcomes = {
        float(r["mdot_msun_per_yr"]): r["outcome"]
        for r in rows
    }

    expected = {
        0.1: "collapse",
        1.0: "pulsation",
        10.0: "pulsation",
        50.0: "pulsation",
        90.0: "collapse",
        100.0: "collapse",
        200.0: "pulsation",
    }
    assert outcomes == expected

    print("== Pop III post-GRI hydrodynamic fate benchmark ==")
    for r in rows:
        print(
            f"mdot={float(r['mdot_msun_per_yr']):g} Msun/yr, "
            f"M_GRI={float(r['m_gri_msun']):.6g} Msun, "
            f"M_core={float(r['m_core_gri_msun']):.6g} Msun "
            f"-> {r['outcome']}"
        )

    print()
    print("Important non-monotonicity:")
    print("  0.1 Msun/yr -> collapse")
    print("  1--50 Msun/yr -> pulsation in the tabulated Pop III models")
    print("  90--100 Msun/yr -> collapse")
    print("  200 Msun/yr -> pulsation")
    print()

    # Nature heavy-seed simulations quote accretion rates around the
    # ~1 Msun/yr scale for the protostellar growth phase.
    one = next(
        r for r in rows
        if float(r["mdot_msun_per_yr"]) == 1.0
    )
    assert one["outcome"] == "pulsation"
    assert float(one["m_gri_msun"]) == 93560.0

    # Nuclear burning is dynamically relevant for pulsating models.
    assert float(one["e_nuc_1e54_erg"]) > 1.0

    print(
        "At the exact 1 Msun/yr source model, GRI onset does NOT immediately "
        "produce a BH: the GR hydrodynamic outcome is a pulsation."
    )
    print()
    print(
        "Therefore a cosmological heavy-seed closure must distinguish "
        "GRI onset from post-GRI fate.  Do not interpolate the discrete fate "
        "labels without a stellar/hydrodynamic model."
    )
    print("All post-GRI fate assertions passed.")


if __name__ == "__main__":
    main()
