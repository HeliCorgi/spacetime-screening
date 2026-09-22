#!/usr/bin/env python3
"""EGKR Nappi--Witten reflection benchmark, NOT heterotic Taub--NUT.

Primary input: hep-th/0204189v2, eqs. (2.44), (3.31), (4.19), (4.25),
and footnote 19 (nu(k)=1). Compare complex coefficients, not only their
moduli. The script reproduces published formulae; it does not independently
solve the NW radial ODE or construct a string BRST Hilbert space.

Run with no arguments for assertions, or --json PATH to save the results.
Dependencies: mpmath (no network or external files).
"""
from __future__ import annotations

import argparse
import json
import platform
from pathlib import Path
from typing import Any

import mpmath as mp


def reflection(s: Any, m: Any, mprime: Any, k: Any | None = None) -> Any:
    """Formula (2.44), or (4.25) when k is provided; source j convention."""
    s, m, mprime = map(mp.mpf, (s, m, mprime))
    if s <= 0:
        raise ValueError("This benchmark excludes the s=0 threshold.")
    j = -mp.mpf('0.5') + 1j * s
    numerator = mp.gamma(-2*j-1)*mp.gamma(j+1+1j*m)*mp.gamma(j+1-1j*mprime)
    denominator = mp.gamma(2*j+1)*mp.gamma(-j+1j*m)*mp.gamma(-j-1j*mprime)
    if k is not None:
        k = mp.mpf(k)
        if k <= 0:
            raise ValueError("k must be positive.")
        numerator *= mp.gamma(1-(2*j+1)/k)
        denominator *= mp.gamma(1+(2*j+1)/k)
    return numerator / denominator


def reflection_probability(s: Any, m: Any, mprime: Any) -> Any:
    """Independent real expression (3.31), for s and omega_minus > 0."""
    op, om = (m+mprime)/2, (m-mprime)/2
    return (mp.cosh(2*mp.pi*op)+mp.cosh(2*mp.pi*(s-om))) / (
        mp.cosh(2*mp.pi*op)+mp.cosh(2*mp.pi*(s+om)))


def close(a: Any, b: Any, tolerance: Any, label: str) -> Any:
    err = abs(a-b)/max(mp.mpf(1), abs(a), abs(b))
    if err >= tolerance:
        raise AssertionError(f"{label}: residual {err}")
    return err


def check_precision(dps: int) -> dict[str, Any]:
    with mp.workdps(dps):
        tol = mp.mpf(10)**(-dps+12)
        # An allowed set under the displayed NW N=0, zero-internal-momentum
        # constraints, NOT a new claim about the Taub--NUT state.
        k, jp, m, mprime = 10, mp.mpf(3), mp.mpf(3), mp.mpf(-2)
        s = mp.sqrt(3)/2
        j = -mp.mpf('0.5') + 1j*s
        shell = -j*(j+1)-m*m+jp*(jp+1)-mprime*mprime
        assert abs(m) <= jp <= mp.mpf(k)/2-1 and abs(mprime) <= jp
        assert (jp-m) == int(jp-m) and (jp-mprime) == int(jp-mprime)
        close(shell, 0, tol, "NW equation (4.19)")
        r0, rk = reflection(s,m,mprime), reflection(s,m,mprime,k)
        f = mp.gamma(1-2j*s/k)/mp.gamma(1+2j*s/k)
        close(rk/r0, f, tol, "ratio of independently evaluated formulae")
        close(abs(f), 1, tol, "unit modulus finite-level factor")
        prob = reflection_probability(s,m,mprime)
        close(abs(r0)**2, prob, tol, "semiclassical rate eq. (3.31)")
        close(abs(rk)**2, prob, tol, "exact rate eq. (3.31)")
        if abs(rk/r0-1) < mp.mpf('0.01'):
            raise AssertionError("Benchmark must distinguish the COMPLEX amplitudes.")

        phase = -2*mp.im(mp.loggamma(1+2j*s/k))
        derivative = -4/mp.mpf(k)*mp.re(mp.digamma(1+2j*s/k))
        by_diff = mp.diff(lambda u: -2*mp.im(mp.loggamma(1+2j*u/k)), s)
        close(derivative, by_diff, tol, "phase derivative")
        # The alternative repository spin convention has the same Casimir.
        j_repo = j+1
        close(-j*(j+1), -j_repo*(j_repo-1), tol, "Casimir convention")

        # Enumerate the displayed lowest-oscillator NW constraints. This is
        # not a full spectrum enumeration (no descendants/other pictures).
        count = 0
        max_error = mp.mpf(0)
        for kk in (8,10):
            for twospin in range(kk-1):
                jj = mp.mpf(twospin)/2
                for tm in range(-twospin,twospin+1,2):
                    for tp in range(-twospin,twospin+1,2):
                        mm, pp = mp.mpf(tm)/2, mp.mpf(tp)/2
                        s2 = mm*mm+pp*pp-jj*(jj+1)-mp.mpf('0.25')
                        if s2 <= 0 or mm <= pp:
                            continue
                        ss = mp.sqrt(s2)
                        semi = reflection(ss,mm,pp)
                        exact = reflection(ss,mm,pp,kk)
                        expected = reflection_probability(ss,mm,pp)
                        for calculated in (abs(semi)**2, abs(exact)**2):
                            max_error = max(max_error,close(calculated,expected,tol,"enumerated rate"))
                        count += 1

        k_limit = []
        previous = mp.inf
        for kk in (10,20,40,100,1000,10000):
            ph = -2*mp.im(mp.loggamma(1+2j*s/kk))
            deviation = abs(reflection(s,m,mprime,kk)/r0-1)
            assert deviation < previous
            previous = deviation
            approximate = 4*mp.euler*s/kk-16*mp.zeta(3)*s**3/(3*kk**3)
            k_limit.append({"k_NW":kk,"phase_rad":mp.nstr(ph,25),
                            "complex_ratio_error_from_one":mp.nstr(deviation,25),
                            "phase_cubic_expansion_error":mp.nstr(abs(ph-approximate),15)})
        # Derivative of phase is not interpreted as a physical time delay.
        def complex_dict(z: Any) -> dict[str,str]:
            return {"re":mp.nstr(mp.re(z),30),"im":mp.nstr(mp.im(z),30)}
        return {"dps":dps,"scope":"Published NW coefficient formulae; not a Taub--NUT amplitude",
                "parameters":{"k_NW":k,"j_SU2":"3","m":"3","mprime":"-2","s":"sqrt(3)/2"},
                "R_semiclassical":complex_dict(r0),"R_exact":complex_dict(rk),
                "exact_over_semiclassical":complex_dict(f),
                "reflection_probability":mp.nstr(prob,30),
                "finite_level_phase_rad":mp.nstr(phase,30),
                "d_phase_d_s":mp.nstr(derivative,30),
                "allowed_lowest_oscillator_cases_checked":count,
                "max_enumerated_rate_residual":mp.nstr(max_error,10),
                "large_k_comparison":k_limit}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--json',type=Path)
    args = ap.parse_args()
    low, high = check_precision(45), check_precision(80)
    with mp.workdps(50):
        for key in ('reflection_probability','finite_level_phase_rad','d_phase_d_s'):
            close(mp.mpf(low[key]),mp.mpf(high[key]),mp.mpf('1e-28'),f"precision repeat {key}")
    result = {"status":"PASS","python":platform.python_version(),"mpmath":mp.__version__,
              "runs":[low,high],"not_calculated":["Taub--NUT BRST spectrum","Taub--NUT exact amplitude",
              "operational past signalling","independent NW ODE integration"]}
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True)
        args.json.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PASS: NW semiclassical/exact COMPLEX reflection benchmark (45/80 digits)')
    print('Reflection probability =',high['reflection_probability'])
    print('Finite-level phase [rad] =',high['finite_level_phase_rad'])
    print('This does not change any Taub--NUT physical-state or signalling gate.')

if __name__ == '__main__':
    main()
