#!/usr/bin/env python3
"""Strong-field / cosmological timescale separation for the heavy-seed benchmark.

Primary source:
Chon et al., Nature 657, 621-625 (2026)
DOI 10.1038/s41586-026-10985-8.

The source states that the initial super-Eddington phase lasts less than
~1 Myr and that the BH-accretion zoom resolves scales down to ~500 au.

For comparison, the intrinsic gravitational time of a black hole is

    t_g = G M / c^3.

For M~10^6 Msun this is only a few seconds.  This enormous separation
supports treating the unresolved strong-field region as a sequence of
quasi-stationary inner solutions labelled by slowly varying outer data
(M, Mdot, angular momentum, radiation environment).

This is an approximation criterion, not a proof of adiabaticity for every
possible internal degree of freedom.
"""

from __future__ import annotations

import math

G = 6.67430e-11
C = 299_792_458.0
MSUN = 1.98847e30
AU = 1.495978707e11
SEC_PER_YR = 365.25 * 24.0 * 3600.0


def t_g_seconds(m_msun: float) -> float:
    return G * m_msun * MSUN / C**3


def kepler_dynamical_time_seconds(m_msun: float, r_au: float) -> float:
    """sqrt(r^3/GM), i.e. orbital period divided by 2 pi."""
    r = r_au * AU
    return math.sqrt(r**3 / (G * m_msun * MSUN))


def main() -> None:
    masses = [6e5, 1e6, 3e7]

    print("== Heavy-seed timescale separation ==")
    for mass in masses:
        tg = t_g_seconds(mass)
        tdyn_500 = kepler_dynamical_time_seconds(mass, 500.0)
        ratio_myr = 1e6 * SEC_PER_YR / tg

        print(f"M={mass:.3g} Msun")
        print(f"  t_g = {tg:.6g} s")
        print(
            "  t_dyn(500 au) = "
            f"{tdyn_500/SEC_PER_YR:.6g} yr"
        )
        print(f"  1 Myr / t_g = {ratio_myr:.6e}")
        print()

        assert ratio_myr > 1e11

    tg_1e6 = t_g_seconds(1e6)
    assert 4.8 < tg_1e6 < 5.1

    # The resolved 500-au flow evolves on years, still vastly slower than
    # the horizon-scale gravitational time.
    tdyn = kepler_dynamical_time_seconds(1e6, 500.0)
    assert tdyn / tg_1e6 > 1e7

    print(
        "Conclusion: a first-pass coupling can treat the strong-field inner "
        "solution as quasi-stationary relative to both the resolved 500-au "
        "flow and the Myr-scale cosmological feeding history."
    )
    print("All timescale-separation assertions passed.")


if __name__ == "__main__":
    main()
