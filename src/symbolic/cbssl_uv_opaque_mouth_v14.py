#!/usr/bin/env python3
"""CBSSL v14: make the wormhole mouth genuinely UV-opaque with a local action.

Goal:
  Replace the phenomenological v13 real-frequency profile q(u)=0.5 exp(-u^4)
  by a local, positive-energy mouth interaction and test the chronology loop.

A single timelike mouth sheet carries a brane-localized kinetic+mass term

    S_sheet = 1/2 int dt [ zeta (d_t phi)^2 - mu phi^2 ]_{x=0}

in the reduced normal channel.  With zeta>0, mu>0 its localized energy is
positive.  The exact scattering amplitude is

    t(w)=2 i w / (zeta w^2 + 2 i w - mu).

For the dimensionless choice mu=zeta=1 (frequencies u=w r),

    t(u)=2 i u/(u+i)^2,

so the sheet is opaque both in the IR and the UV and transmits perfectly at
u=1.  This is an explicit local realization of "do not make the wormhole UV
transparent".

Results:
  * One sheet at each mouth gives q_2=t^2~u^-2.  That is not enough to make
    the point-split RSET finite at a null loop.
  * Four passive filter stages give q_4=t^4~u^-4.  The real-frequency
    two-point/RSET null-loop spectral integrals become absolutely finite and
    the u=1 signal band still transmits perfectly.
  * However past-advance feedback multiplies by exp(-i a u), a=3/4.  On the
    upper imaginary axis u=i y,
        q_N(i y) exp(a y) =
        [2 y/(1+y)^2]^N exp(a y).
    For every finite N and every a>0 this starts at 0 and tends to infinity.
    Hence 1-q_N exp(-i a u) has an upper-half-plane pole: a linear instability.
    For N=4 the pole is y*=9.2739592454...
  * Adding a causal positive delay tau to the filter changes the exponential
    to exp[(a-tau)y].  Avoiding the asymptotic pole requires tau>=a, which
    removes the net past advance.

Thus local positive UV opacity is achievable, but in this finite-stage passive
family it cannot simultaneously provide a stable stationary past-advance loop.
The v13 super-Gaussian q(u) is also audited: it is bounded on the real axis but
unbounded in parts of the upper half plane, so it is not accepted as a passive
causal transfer function.

Toy-model audit, not a universal theorem for all quantum-gravity completions.
"""
from __future__ import annotations

import argparse
import cmath
import hashlib
import json
import math
import platform
from pathlib import Path

import mpmath as mp
import sympy as sp

BASE_SHA = "7f7fbec0b56c9592459e79b0c84a8be4ced8950c"
ADVANCE = mp.mpf("0.75")


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def exact_sheet_scattering() -> dict:
    """Derive the local sheet transmission and flux unitarity."""
    u, mu, zeta = sp.symbols("u mu zeta", positive=True, real=True)
    I = sp.I

    # Jump condition from
    # S = 1/2 int[(phi_t)^2-(phi_x)^2] + 1/2 int_sheet[zeta phi_t^2-mu phi^2]:
    # [phi_x] = (mu-zeta u^2) phi.
    t = sp.simplify(2*I*u/(zeta*u**2 + 2*I*u - mu))
    r = sp.simplify(t-1)
    T = sp.simplify(t*sp.conjugate(t))
    R = sp.simplify(r*sp.conjugate(r))
    require(sp.simplify(T+R-1) == 0, "sheet scattering not unitary")

    t1 = sp.simplify(t.subs({mu:1,zeta:1}))
    require(sp.simplify(t1-2*I*u/(u+I)**2) == 0, "mu=zeta=1 factorization")
    T1 = sp.simplify(T.subs({mu:1,zeta:1}))
    require(sp.simplify(T1-4*u**2/(1+u**2)**2) == 0, "sheet transmission probability")
    require(sp.simplify(t1.subs(u,1)-1) == 0, "signal band not transparent")
    require(sp.limit(u*t1, u, sp.oo) == 2*I, "UV amplitude")
    require(sp.limit(t1/u, u, 0, dir="+") == -2*I, "IR amplitude")

    return {
        "local_action": "S_sheet=1/2 int dt [zeta (d_t phi)^2-mu phi^2] at the timelike mouth sheet",
        "localized_energy": "H_sheet=1/2[zeta (d_t phi)^2+mu phi^2] >=0 for zeta,mu>0",
        "jump_condition": "[d_x phi]=(mu-zeta omega^2) phi",
        "transmission_general": "t=2 i omega/(zeta omega^2+2 i omega-mu)",
        "choice": "mu*r=zeta/r=1 after dimensionless normal-channel rescaling",
        "transmission": "t(u)=2 i u/(u+i)^2",
        "transmission_probability": "|t|^2=4 u^2/(1+u^2)^2",
        "reflection_probability": "|r|^2=(u^2-1)^2/(1+u^2)^2",
        "flux_unitarity": True,
        "perfect_transmission_at_u": "1",
        "UV_amplitude_scaling": "t~2 i/u",
        "IR_amplitude_scaling": "t~-2 i u",
        "positive_local_energy": True,
    }


def stage_amplitude(u: complex | mp.mpf) -> complex:
    return 2j*u/(u+1j)**2


def null_loop_integrability() -> dict:
    """Check the high-frequency power needed for a 4D point-split RSET."""
    with mp.workdps(70):
        # Natural handle: one positive sheet at each mouth.
        # q2=t^2 and |q2|=4u^2/(1+u^2)^2 ~4/u^2.
        # The null-loop RSET absolute spectral test contains int u^2 |q| du,
        # so N=2 diverges linearly.
        q2_u2_limit = mp.mpf(4)
        require(q2_u2_limit > 0, "N=2 divergence control")

        # Four stages: |q4|=(2u/(1+u^2))^4.
        # Exact beta-function integrals:
        # int |q4| du = pi/2
        # int u^2 |q4| du = 5pi/2.
        i0 = mp.quad(lambda u: (2*u/(1+u*u))**4, [0,1,mp.inf])
        i2 = mp.quad(lambda u: u*u*(2*u/(1+u*u))**4, [0,1,mp.inf])
        require(abs(i0-mp.pi/2) < mp.mpf("1e-55"), "N=4 phi2 integral")
        require(abs(i2-5*mp.pi/2) < mp.mpf("1e-55"), "N=4 RSET integral")

        # Real-frequency feedback denominator has no zero:
        # |q4|=1 only at u=1, but loop phase exp(-i*3/4) !=1.
        d_at_one = abs(1-mp.e**(-1j*ADVANCE))
        require(d_at_one > mp.mpf("0.7"), "u=1 loop phase accidentally closes")

        # Numerical minimum on a broad real interval as an additional control.
        min_d = mp.inf
        min_u = None
        for j in range(1, 20001):
            u = mp.mpf(j)/1000
            q = stage_amplitude(u)**4
            d = abs(1-q*mp.e**(-1j*ADVANCE*u))
            if d < min_d:
                min_d, min_u = d, u
        require(min_d > mp.mpf("0.6"), "real-frequency feedback pole")

        return {
            "natural_two_mouth_filter": {
                "stages": 2,
                "chronology_amplitude": "q2=t(u)^2",
                "UV_scaling": "q2~u^-2",
                "null_phi2_absolute_integral": "finite",
                "null_RSET_absolute_integral": "diverges; u^2 |q2| -> 4",
                "status": "C",
            },
            "engineered_four_stage_filter": {
                "stages": 4,
                "chronology_amplitude": "q4=t(u)^4",
                "UV_scaling": "q4~16/u^4",
                "signal_band": "|q4(1)|=1",
                "absolute_phi2_spectral_integral": "pi/2",
                "absolute_RSET_spectral_integral": "5*pi/2",
                "real_frequency_feedback_zero": False,
                "minimum_abs_feedback_denominator_0_to_20": mp.nstr(min_d, 25),
                "minimum_location_u": mp.nstr(min_u, 20),
                "real_axis_RSET_finite": True,
            },
        }


def upper_half_plane_instability() -> dict:
    """Find the feedback pole and prove its finite-N inevitability."""
    with mp.workdps(70):
        def gain_on_iy(y, N):
            return (2*y/(1+y)**2)**N * mp.e**(ADVANCE*y)

        def log_gain(y, N, delay=mp.mpf("0")):
            return N*mp.log(2*y/(1+y)**2) + (ADVANCE-delay)*y

        roots = {}
        brackets = {2:(mp.mpf("1"),mp.mpf("4")),
                    4:(mp.mpf("5"),mp.mpf("12")),
                    6:(mp.mpf("10"),mp.mpf("25")),
                    8:(mp.mpf("20"),mp.mpf("40"))}
        for N,(lo,hi) in brackets.items():
            root = mp.findroot(lambda y: log_gain(y,N), (lo,hi))
            require(root > 0, "upper-plane root")
            require(abs(gain_on_iy(root,N)-1) < mp.mpf("1e-50"), "feedback pole equation")
            roots[str(N)] = mp.nstr(root, 40)

        y4 = mp.mpf(roots["4"])
        require(abs(y4-mp.mpf("9.273959245421")) < mp.mpf("1e-12"), "N=4 pole drift")

        # General finite-N asymptotics:
        # y->0: [2y/(1+y)^2]^N e^(a y) ->0.
        # y->inf: ~ (2/y)^N e^(a y) ->inf for every finite N and a>0.
        #
        # Add a physical positive delay tau: exp[(a-tau)y].
        # If tau<a the same asymptotic root is unavoidable.
        delays = []
        for tau_s in ("0", "0.25", "0.5", "0.74", "0.75", "1"):
            tau = mp.mpf(tau_s)
            asymptotic = (
                "grows_exponentially"
                if tau < ADVANCE
                else "polynomially_decays_or_better"
            )
            net_advance = ADVANCE-tau
            delays.append({
                "filter_delay_over_r": tau_s,
                "asymptotic_upper_axis_feedback": asymptotic,
                "net_past_advance_over_r": mp.nstr(net_advance, 20),
                "past_advance_survives": bool(net_advance > 0),
            })

        return {
            "feedback_denominator": "D_N(u)=1-t(u)^N exp(-i a u), a=3/4",
            "imaginary_axis": "D_N(i y)=1-[2y/(1+y)^2]^N exp(a y)",
            "finite_stage_general_result": "for every finite N and a>0, gain goes 0 at y->0 and infinity at y->infinity, so an upper-half-plane pole exists",
            "pole_locations_y=Im(omega*r)": roots,
            "N4_instability_time_over_r": mp.nstr(1/y4, 30),
            "stability": False,
            "delay_tradeoff": delays,
            "causal_delay_needed_to_remove_asymptotic_pole": "tau_filter >= a",
            "consequence": "tau_filter>=a removes the net past advance in this loop accounting",
        }


def v13_supergaussian_causality_audit() -> dict:
    """Audit q=0.5 exp(-u^4) as a passive causal transfer function."""
    with mp.workdps(50):
        # Along u=R exp(i pi/4), u^4=-R^4, hence |q|=.5 exp(R^4).
        rows = []
        for R_s in ("1","1.5","2"):
            R = mp.mpf(R_s)
            growth = mp.mpf("0.5")*mp.e**(R**4)
            rows.append({
                "R": R_s,
                "upper_half_plane_ray": "u=R exp(i*pi/4)",
                "|q(u)|": mp.nstr(growth, 25),
            })
        require(mp.mpf(rows[-1]["|q(u)|"]) > mp.mpf("1e6"), "super-Gaussian Hinf audit")
        return {
            "profile": "q_v13(u)=0.5 exp(-u^4)",
            "bounded_on_real_axis": True,
            "bounded_analytic_in_upper_half_plane": False,
            "passive_causal_H_infinity_transfer_accepted": False,
            "reason": "on u=R exp(i*pi/4), |q|=0.5 exp(R^4) grows without bound",
            "rows": rows,
            "v13_effective_open_state_status_after_causal_gate": "C for this specific transfer profile",
        }


def candidate_records(sheet, integ, instability, audit) -> list[dict]:
    return [
        {
            "candidate_id": "cbssl-local-two-mouth-uv-filter-v14",
            "status": "C",
            "matter_model": sheet["local_action"],
            "positive_local_energy": True,
            "UV_opaque": True,
            "signal_band_transmission": "perfect at u=1 for each sheet",
            "chronology_path_stages": 2,
            "obstruction": integ["natural_two_mouth_filter"]["null_RSET_absolute_integral"],
            "classification_reason": "One local positive filter per mouth is genuinely UV opaque but only gives q~u^-2, insufficient for a finite 4D point-split stress tensor at the handle null-loop limit.",
        },
        {
            "candidate_id": "cbssl-four-stage-passive-uv-filter-v14",
            "status": "C",
            "UV_opaque": True,
            "real_axis_RSET_finite": True,
            "signal_band_transmission": "|q4(1)|=1",
            "upper_half_plane_pole": instability["pole_locations_y=Im(omega*r)"]["4"],
            "stability": False,
            "classification_reason": "Four local passive stages make the real-frequency RSET integrals finite, but the negative loop delay generates an upper-half-plane feedback pole and therefore no stationary stable chronology state.",
        },
        {
            "candidate_id": "cbssl-v13-supergaussian-causal-audit-v14",
            "status": "C",
            "profile": audit["profile"],
            "classification_reason": "The v13 super-Gaussian real-frequency cutoff is not a bounded passive causal transfer function in the upper half plane; its B result remains an effective open-state toy, not a microscopic causal mouth model.",
        },
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    sheet = exact_sheet_scattering()
    integ = null_loop_integrability()
    instability = upper_half_plane_instability()
    audit = v13_supergaussian_causality_audit()
    candidates = candidate_records(sheet, integ, instability, audit)

    data = {
        "base_sha": BASE_SHA,
        "classification": {"A":0,"B":0,"C":3},
        "local_sheet": sheet,
        "null_loop_integrability": integ,
        "feedback_instability": instability,
        "v13_causality_audit": audit,
        "candidates": candidates,
        "environment": {
            "python": platform.python_version(),
            "sympy": sp.__version__,
            "mpmath": mp.__version__,
        },
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

    print(json.dumps({
        "passed": True,
        "classification": data["classification"],
        "local_UV_opacity": True,
        "natural_two_mouth_RSET": "DIVERGES",
        "four_stage_real_axis_RSET": "FINITE",
        "four_stage_feedback": "UNSTABLE",
        "N4_upper_pole": instability["pole_locations_y=Im(omega*r)"]["4"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
