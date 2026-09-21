#!/usr/bin/env python3
"""Curvature/compactness separation at the SMS GR-instability threshold.

Source benchmark:
Saio et al., A&A 689, A169 (2024), arXiv:2406.18040.

Their Table 1 gives the surface compactness
    C = 2GM/(R c^2)
at the onset of the GR radial instability.  The values are only
~1e-5--1.7e-4.

For scale comparison, evaluate the exterior Schwarzschild Kretschmann scalar
at the stellar surface,
    K(R)=48 M_geo^2/R^6,
and at r=2M_geo,
    K(2M)=3/(4 M_geo^4).

Their ratio is exactly
    K(R)/K(2M)=C^6.

Likewise a one-curvature/tidal scale M/R^3 relative to its r=2M value scales
as C^3.

These are scale-separation diagnostics.  They do not replace the stellar
interior curvature profile and do not prove that every modified-gravity model
has Delta Mcrit=0.  They show that a theory designed to switch on only at
near-horizon local curvature is far from its trigger scale when the GRI first
appears.
"""

from __future__ import annotations

import csv
from pathlib import Path


def load(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    rows = load(root / "data" / "sms_gri_gr_benchmark.csv")

    gri = [r for r in rows if r["status"] == "gri"]
    assert gri

    print("== SMS GRI compactness / curvature separation ==")
    for row in gri:
        mdot = float(row["mdot_msun_per_yr"])
        comp = float(row["compactness_2gm_rc2"])
        k_ratio = comp**6
        tidal_ratio = comp**3

        print(
            f"mdot={mdot:g} Msun/yr: "
            f"C=2GM/(Rc^2)={comp:.3e}, "
            f"tidal ratio~C^3={tidal_ratio:.3e}, "
            f"K(R)/K(2M)=C^6={k_ratio:.3e}"
        )

        assert 0 < comp < 2e-4
        assert tidal_ratio < 1e-11
        assert k_ratio < 3e-23

    # Chon-relevant ~1 Msun/yr anchor.
    one = next(r for r in gri if float(r["mdot_msun_per_yr"]) == 1.0)
    c1 = float(one["compactness_2gm_rc2"])
    assert c1 == 2.9e-5
    assert 5e-28 < c1**6 < 7e-28

    cmin = min(float(r["compactness_2gm_rc2"]) for r in gri)
    cmax = max(float(r["compactness_2gm_rc2"]) for r in gri)

    print()
    print(f"GRI compactness range: {cmin:.3e} -- {cmax:.3e}")
    print(
        "The onset of collapse is therefore deeply separated from "
        "near-horizon local-curvature scales."
    )
    print()
    print(
        "Interpretation for Spacetime Screening: a genuinely high-curvature "
        "screening mechanism should leave the initial GRI threshold nearly "
        "GR-like unless it also modifies weak/post-Newtonian stellar gravity. "
        "The more direct QG test is the nonlinear collapse AFTER the GRI."
    )
    print("All SMS curvature-separation assertions passed.")


if __name__ == "__main__":
    main()
