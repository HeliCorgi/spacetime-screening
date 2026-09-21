#!/usr/bin/env python3
"""Model-independent matching scale for SMS collapse into a screened regime.

Use the Schwarzschild exterior Kretschmann scalar only as a curvature-scale
diagnostic:

    K(r) = 48 M_geo^2 / r^6.

At r_s=2 M_geo,
    K_h = 3/(4 M_geo^4).

Therefore
    K(r)/K_h = (r_s/r)^6 = C^6,
where C=r_s/r is the compactness.

If a high-curvature completion becomes relevant when
    K/K_h = eta,
then
    r_act/r_s = eta^(-1/6).

This provides a clean GR -> strong-field matching radius without assuming a
specific screened interior.

The SMS GRI benchmark starts at C~1e-5--1e-4, i.e. thousands to tens of
thousands of Schwarzschild radii.
"""

from __future__ import annotations

import csv
import math
from pathlib import Path


def activation_radius_over_rs(eta: float) -> float:
    if not (0.0 < eta <= 1.0):
        raise ValueError("eta must lie in (0,1]")
    return eta ** (-1.0 / 6.0)


def compactness_at_activation(eta: float) -> float:
    return eta ** (1.0 / 6.0)


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    path = root / "data" / "sms_gri_gr_benchmark.csv"

    with path.open(newline="", encoding="utf-8") as fh:
        rows = [
            r for r in csv.DictReader(fh)
            if r["status"] == "gri"
        ]

    print("== GR instability starting radii ==")
    for row in rows:
        comp = float(row["compactness_2gm_rc2"])
        r_over_rs = 1.0 / comp
        print(
            f"mdot={float(row['mdot_msun_per_yr']):g} Msun/yr: "
            f"R_GRI/r_s={r_over_rs:.6g}"
        )
        assert r_over_rs > 5000.0

    print()
    print("== Curvature-trigger matching radii ==")
    for eta in (1.0, 1e-3, 1e-6, 1e-12, 1e-18, 1e-24):
        rr = activation_radius_over_rs(eta)
        cc = compactness_at_activation(eta)
        print(
            f"K/K_h={eta:.0e}: "
            f"r_act/r_s={rr:.6g}, C_act={cc:.6g}"
        )

    assert math.isclose(
        activation_radius_over_rs(1e-6),
        10.0,
        rel_tol=1e-12,
    )
    assert math.isclose(
        activation_radius_over_rs(1e-12),
        100.0,
        rel_tol=1e-12,
    )
    assert math.isclose(
        activation_radius_over_rs(1e-24),
        1e4,
        rel_tol=1e-12,
    )

    # Chon/Saio-relevant 1 Msun/yr GRI model.
    c_gri = 2.9e-5
    eta_gri = c_gri**6
    assert 5e-28 < eta_gri < 7e-28

    print()
    print(
        "For the 1 Msun/yr GRI model, the surface curvature-scale ratio "
        f"is only K/K_h~{eta_gri:.3e}."
    )
    print(
        "Hence a high-curvature theory with eta_act >> 1e-27 can use GR "
        "for a substantial part of the collapse before switching to the "
        "strong-field solver."
    )
    print("All SMS screening-activation assertions passed.")


if __name__ == "__main__":
    main()
