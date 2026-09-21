#!/usr/bin/env python3
"""GR instability benchmark for rapidly accreting primordial SMSs.

Primary numerical benchmark:
Saio, Nandal, Ekstrom & Meynet (2024), arXiv:2406.18040.

Their Table 1 gives the mass at which the fundamental relativistic radial
pulsation mode becomes unstable for constant accretion rates.  This script
loads those source values and supplies a log-log interpolation ONLY within
the tabulated GRI range 0.05--1000 Msun/yr.

The interpolation is a repository convenience, not a result of the source.

The Spacetime Screening observable is defined as

    Delta M_crit(mdot) = M_crit,screened - M_crit,GR,

or equivalently as a shift of the fundamental-mode eigenvalue.

No nonzero screening shift is assumed in this file.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
import math
from pathlib import Path


@dataclass(frozen=True)
class GRIPoint:
    mdot: float
    mcrit: float


def load_points(path: Path) -> list[GRIPoint]:
    points: list[GRIPoint] = []
    with path.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            if row["status"] != "gri":
                continue
            points.append(
                GRIPoint(
                    mdot=float(row["mdot_msun_per_yr"]),
                    mcrit=float(row["mcrit_msun"]),
                )
            )
    points.sort(key=lambda p: p.mdot)
    return points


def loglog_interpolate(points: list[GRIPoint], mdot: float) -> float:
    """Piecewise log-log interpolation of the tabulated GR benchmark."""
    if mdot <= 0:
        raise ValueError("mdot must be positive")
    if len(points) < 2:
        raise ValueError("need at least two benchmark points")
    if mdot < points[0].mdot or mdot > points[-1].mdot:
        raise ValueError("do not extrapolate beyond the source GRI table")

    for a, b in zip(points, points[1:]):
        if a.mdot <= mdot <= b.mdot:
            if mdot == a.mdot:
                return a.mcrit
            if mdot == b.mdot:
                return b.mcrit
            x = (
                math.log(mdot / a.mdot)
                / math.log(b.mdot / a.mdot)
            )
            return math.exp(
                math.log(a.mcrit)
                + x * math.log(b.mcrit / a.mcrit)
            )

    # Exact final endpoint.
    return points[-1].mcrit


def fractional_screening_shift(
    mcrit_gr: float,
    delta_mcrit: float,
) -> float:
    return delta_mcrit / mcrit_gr


def main() -> None:
    root = Path(__file__).resolve().parents[2]
    path = root / "data" / "sms_gri_gr_benchmark.csv"
    points = load_points(path)

    expected = [
        (0.05, 8.2e4),
        (0.1, 1.06e5),
        (1.0, 2.16e5),
        (10.0, 4.56e5),
        (100.0, 7.08e5),
        (1000.0, 1.06e6),
    ]
    assert [(p.mdot, p.mcrit) for p in points] == expected

    print("== GR SMS instability benchmark ==")
    for p in points:
        print(
            f"mdot={p.mdot:g} Msun/yr -> "
            f"Mcrit={p.mcrit:.6g} Msun"
        )

    # Reproduce exact table nodes.
    for p in points:
        assert math.isclose(
            loglog_interpolate(points, p.mdot),
            p.mcrit,
            rel_tol=1e-14,
        )

    print()
    print("Operational interpolation in the Chon-relevant range:")
    for mdot in (0.1, 0.3, 0.5, 1.0):
        mcrit = loglog_interpolate(points, mdot)
        print(
            f"mdot={mdot:g} Msun/yr -> "
            f"Mcrit,GR~{mcrit:.6g} Msun"
        )

    m03 = loglog_interpolate(points, 0.3)
    assert 1.06e5 < m03 < 2.16e5

    print()
    print(
        "Screening observable: Delta Mcrit(mdot) = "
        "Mcrit_screened - Mcrit_GR."
    )
    print(
        "This benchmark sets Delta Mcrit=0 by construction; a nonzero "
        "value requires a modified stellar-equilibrium + radial-mode solve."
    )
    print("All SMS GRI benchmark assertions passed.")


if __name__ == "__main__":
    main()
