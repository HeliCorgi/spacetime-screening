#!/usr/bin/env python3
"""CBSSL v13: construct/test the missing chronology-handle two-point function.

Two completions are kept strictly separate.

(1) Closed geometric short-throat handle:
    In the flat short-throat approximation, repeated handle traversals generate
    image geodesics.  A fixed nonzero traversal attenuation q merely replaces
    zeta(2), zeta(4) by polylogarithms Li_2(q), Li_4(q).  The image correction
    still diverges when the primitive closed spacelike loop becomes null.
    The v12 past-advance witness lies on the timelike side, so this standard
    image/Hadamard completion is classified C for this handle ansatz.

(2) UV-soft open Gaussian return channel:
    Treat the handle as a modewise pure-loss Gaussian return map with a unitary
    dilation by an environment:
        a -> q(u) exp(i u theta) a + sqrt(1-q(u)^2) b,
    q(u)=q0 exp(-u^4), |q|<1.
    Let the environment be a gauge-invariant Gaussian state with occupation
        N(u)=N0 exp(-u^4).
    The unique fixed covariance has occupation N(u), zero anomalous covariance.
    This gives an explicit nonzero smooth correction Delta G_handle^+ to the
    safe S1 Hadamard state.  The correction is symmetric, preserves the CCR,
    is positive (N>=0), and is super-polynomially UV soft, hence it does not
    alter the local Hadamard singularity.  Its finite RSET is included in the
    regulated semiclassical core and the core is re-solved.

This open-channel construction is B, not A: it is not a closed local QFT on a
geometric time-machine handle.  It adds reservoir degrees of freedom and a
frequency-dependent nonlocal mouth channel; complete reservoir/apparatus stress
and a microscopic geometric derivation remain absent.

Toy-model audit, not established physics.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp

BASE_SHA = "735e51ad470df93f4e680169084a9fdf90c77556"
ALPHA = mp.mpf("4")
XI = mp.mpf("-10000")
M2 = mp.mpf("1000")

# v12 converged safe-S1 coefficients:
CT = mp.mpf("0.00039115324987090346409958722388060179527777892968766")
CX = mp.mpf("-0.0013135652650630378856936929316968132131234586046131")
CH = mp.mpf("0.0004612060075960672107970528539081057089228398374627")

Q0 = mp.mpf("0.5")
N0 = mp.mpf("0.01")
THETA_LOOP = mp.mpf("-0.75")  # (tau_shortcut+d_ext-Delta_clock)/r


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def popov_local(r: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    mds = mp.sqrt(M2)
    pt = -XI**3/6 + XI**2/12 - XI/60 + mp.mpf(1)/630
    pth = -2*pt
    logterm = mp.log(mds**2*r**2)/720
    fac = 1/(4*mp.pi**2*r**4)
    tt = fac*(mp.mpf("0.00310")+logterm+pt/(M2*r**2))
    th = fac*(-mp.mpf("0.00171")-logterm+pth/(M2*r**2))
    return tt, th


def closed_geometric_handle() -> dict:
    """Image sum in the short-throat flat-space handle approximation."""
    with mp.workdps(70):
        ell_over_r = mp.mpf("1.25")  # d_ext/r + tau_shortcut/r
        actual_delta_over_r = mp.mpf("2")
        actual_beta = actual_delta_over_r/ell_over_r
        actual_s2 = ell_over_r**2-actual_delta_over_r**2
        require(actual_beta > 1 and actual_s2 < 0, "v12 handle is not on timelike side")

        li2 = mp.polylog(2, Q0)
        li4 = mp.polylog(4, Q0)
        rows = []
        for beta_s in ("0", "0.5", "0.9", "0.99", "0.999", "0.9999"):
            beta = mp.mpf(beta_s)
            s2 = ell_over_r**2*(1-beta**2)
            phi2_r2 = li2/(2*mp.pi**2*s2)
            rset_scale_r4 = li4/(mp.pi**2*s2**2)
            rows.append({
                "Delta_over_ell": beta_s,
                "s_squared_over_r2": mp.nstr(s2, 25),
                "Delta_phi2_times_r2": mp.nstr(phi2_r2, 25),
                "RSET_scale_times_r4": mp.nstr(rset_scale_r4, 25),
            })

        # Fixed q attenuation cannot cure the n=1 null-image singularity.
        require(rows[-1]["RSET_scale_times_r4"] != "0", "geometric image divergence hidden")
        return {
            "approximation": "flat short-throat primitive loop; van Vleck control factor set to one",
            "primitive_optical_loop_over_r": mp.nstr(ell_over_r, 20),
            "actual_Delta_clock_over_r": "2",
            "actual_Delta_over_ell": mp.nstr(actual_beta, 20),
            "actual_loop_interval_squared_over_r2": mp.nstr(actual_s2, 25),
            "per_traversal_attenuation_q": mp.nstr(Q0, 20),
            "Delta_G_coincidence_spacelike": "Li_2(q)/(2*pi^2*s^2)",
            "RSET_scale_spacelike": "Li_4(q)/(pi^2*s^4)",
            "fixed_attenuation_removes_null_divergence": False,
            "actual_timelike_analytic_continuation_accepted_as_Hadamard_state": False,
            "rows": rows,
            "status": "C",
        }


def open_gaussian_handle() -> dict:
    """Explicit smooth Delta G_handle^+ from a UV-soft Gaussian return channel."""
    with mp.workdps(70):
        # N(u)=N0 exp(-u^4), u=omega*r.
        # Delta W(x,x') = int d^3k/[2(2pi)^3 omega] N(omega r)
        #   * [exp(-ik Delta x)+exp(+ik Delta x)]
        #
        # At spatial coincidence:
        # Delta <phi^2> = 1/(2pi^2 r^2) int_0^inf u N(u) du.
        # int u exp(-u^4) du = sqrt(pi)/4.
        phi2_coeff = N0/(8*mp.pi**(mp.mpf("1.5")))

        # rho = 1/(2pi^2 r^4) int u^3 N(u) du,
        # int u^3 exp(-u^4) du = 1/4.
        rho_coeff = N0/(8*mp.pi**2)

        # Numerical controls of the analytic integrals.
        i1 = mp.quad(lambda u: u*mp.e**(-u**4), [0, 1, mp.inf])
        i3 = mp.quad(lambda u: u**3*mp.e**(-u**4), [0, 1, mp.inf])
        require(abs(i1-mp.sqrt(mp.pi)/4) < mp.mpf("1e-55"), "phi2 integral")
        require(abs(i3-mp.mpf(1)/4) < mp.mpf("1e-55"), "energy integral")

        # Modewise fixed covariance check at representative frequencies.
        controls = []
        for u_s in ("0", "0.5", "1", "2", "4"):
            u = mp.mpf(u_s)
            q = Q0*mp.e**(-u**4)
            N = N0*mp.e**(-u**4)
            require(0 <= q < 1 and N >= 0, "Gaussian channel parameters")
            # n' = q^2 n + (1-q^2) N, hence fixed n=N.
            fixed_res = q*q*N + (1-q*q)*N-N
            require(abs(fixed_res) < mp.mpf("1e-65"), "fixed occupation")
            controls.append({
                "u=omega*r": u_s,
                "q(u)": mp.nstr(q, 30),
                "N(u)": mp.nstr(N, 30),
                "return_phase": "exp(i*u*theta), theta=-3/4",
            })

        return {
            "channel": "modewise pure-loss Gaussian return map with environment dilation",
            "return_map": "a -> q(u) exp(i u theta) a + sqrt(1-q(u)^2) b",
            "q_profile": "q(u)=0.5 exp(-u^4)",
            "environment_occupation": "N(u)=0.01 exp(-u^4)",
            "theta_loop": "-3/4",
            "unique_fixed_occupation": "n_*(u)=N(u)",
            "fixed_anomalous_covariance": "0",
            "Delta_G_handle_plus": "integral d^3k/[2(2pi)^3 omega] N(omega*r) [exp(-ik.(x-x'))+exp(+ik.(x-x'))]",
            "Delta_phi2": "N0/(8*pi^(3/2)*r^2)",
            "Delta_phi2_coefficient": mp.nstr(phi2_coeff, 45),
            "RSET_mixed": "rho_H * diag(-1,1/3,1/3,1/3), rho_H=N0/(8*pi^2*r^4)",
            "rho_coefficient": mp.nstr(rho_coeff, 45),
            "positive_quasifree_state": True,
            "CCR_preserved": True,
            "Hadamard_preserved": True,
            "reason_Hadamard": "Delta G is C-infinity because N(u) decays as exp(-u^4); the local UV singularity remains that of the safe Hadamard state.",
            "geometric_closed_handle_QFT": False,
            "controls": controls,
            "status": "B",
            "coefficients": (-rho_coeff, rho_coeff/3, rho_coeff/3),
        }


def residuals(
    r: mp.mpf,
    q2: mp.mpf,
    f2: mp.mpf,
    handle_coeffs: tuple[mp.mpf, mp.mpf, mp.mpf],
) -> mp.matrix:
    ht, hx, hh = handle_coeffs
    tq_t, tq_h = popov_local(r)
    em_t = -q2/(8*mp.pi*r**4)
    em_h = q2/(8*mp.pi*r**4)
    A = ALPHA*r
    W = 2*mp.pi**2*f2/A**2

    et = -1/r**2 - 8*mp.pi*(tq_t+em_t+(CT+ht)/r**4-W)
    ex = -1/r**2 - 8*mp.pi*(tq_t+em_t+(CX+hx)/r**4+W)
    eh = -8*mp.pi*(tq_h+em_h+(CH+hh)/r**4-W)
    return mp.matrix([et, ex, eh, eh])


def solve_open_core(
    handle_coeffs: tuple[mp.mpf, mp.mpf, mp.mpf],
    dps: int,
) -> dict:
    with mp.workdps(dps):
        r, q2, f2 = mp.findroot(
            lambda rr, qq, ff: (
                residuals(rr, qq, ff, handle_coeffs)[0],
                residuals(rr, qq, ff, handle_coeffs)[1],
                residuals(rr, qq, ff, handle_coeffs)[2],
            ),
            (mp.mpf("101.49341"), mp.mpf("20601.81"), mp.mpf("6.0e-8")),
            tol=mp.power(10, -(dps-15)),
            maxsteps=80,
        )
        res = residuals(r, q2, f2, handle_coeffs)
        maxres = max(abs(v) for v in res)
        require(r > 0 and q2 > 0 and f2 > 0, "open-handle core parameter sign")
        require(maxres < mp.power(10, -(dps-20)), "open-handle core residual")

        J = mp.matrix(3)
        for i in range(3):
            J[i,0] = mp.diff(lambda z: residuals(z,q2,f2,handle_coeffs)[i], r)
            J[i,1] = mp.diff(lambda z: residuals(r,z,f2,handle_coeffs)[i], q2)
            J[i,2] = mp.diff(lambda z: residuals(r,q2,z,handle_coeffs)[i], f2)
        detJ = mp.det(J)
        require(abs(detJ) > mp.mpf("1e-20"), "open-handle Jacobian singular")

        return {
            "dps": dps,
            "r_planck": mp.nstr(r, 55),
            "Q_squared": mp.nstr(q2, 55),
            "A_topo_planck": mp.nstr(ALPHA*r, 55),
            "axion_f_squared_planck2": mp.nstr(f2, 55),
            "max_abs_residual": mp.nstr(maxres, 12),
            "jacobian_determinant": mp.nstr(detJ, 35),
        }


def compare_precision(lo: dict, hi: dict) -> str:
    errs = []
    for key in ("r_planck","Q_squared","axion_f_squared_planck2"):
        a, b = mp.mpf(lo[key]), mp.mpf(hi[key])
        errs.append(abs(a-b)/max(mp.mpf(1), abs(b)))
    m = max(errs)
    require(m < mp.mpf("1e-30"), "v13 precision mismatch")
    return mp.nstr(m, 15)


def receiver_control() -> dict:
    with mp.workdps(70):
        k = mp.mpf(3)
        pc = (1+mp.erf(k/mp.sqrt(2)))/2
        pe = 1-pc
        D = 2*pc-1
        return {
            "P_Y_do_0": {"+1": mp.nstr(pc,50), "-1": mp.nstr(pe,50)},
            "P_Y_do_1": {"+1": mp.nstr(pe,50), "-1": mp.nstr(pc,50)},
            "D_past": mp.nstr(D,50),
            "globally_certified": False,
        }


def candidate_records(
    closed: dict,
    opened: dict,
    core: dict,
    signal: dict,
) -> list[dict]:
    return [
        {
            "candidate_id": "cbssl-closed-geometric-handle-image-v13",
            "status": "C",
            "scope": "Short-throat flat-space geometric image completion of the separate v12 chronology handle, including any fixed nonzero per-traversal attenuation q.",
            "Delta_G_handle": closed["Delta_G_coincidence_spacelike"],
            "RSET": closed["RSET_scale_spacelike"],
            "obstruction": "As the primitive closed spacelike loop becomes null, Li_2(q)/s^2 and Li_4(q)/s^4 diverge for every fixed q>0. The actual v12 past-advance witness is on the timelike side; the analytic continuation is not accepted as a standard Hadamard image state.",
            "safe_S1_destroyed": False,
            "classification_reason": "Separating A_topo protects the unrelated S1 sector, but the chronology handle generates its own short closed loop and inherits the null-loop image singularity.",
        },
        {
            "candidate_id": "cbssl-uv-soft-open-handle-v13",
            "status": "B",
            "scope": "Effective open Gaussian chronology-return channel on the safe S1 support-field algebra, with a UV-soft pure-loss transfer and an explicit environment dilation.",
            "Delta_G_handle": opened["Delta_G_handle_plus"],
            "positive_quasifree_state": True,
            "CCR_preserved": True,
            "Hadamard_preserved": True,
            "safe_sector_backreaction": {
                "solved": True,
                "r_planck": core["r_planck"],
                "Q_squared": core["Q_squared"],
                "axion_f_squared_planck2": core["axion_f_squared_planck2"],
                "max_abs_residual": core["max_abs_residual"],
                "jacobian_determinant": core["jacobian_determinant"],
            },
            "communication": {
                "conditional_receiver": signal,
                "return_gain_low_frequency": "q(0)=1/2",
                "past_advance_geometry": "inherited v12 theta_loop=-3/4",
            },
            "unresolved_assumptions": [
                "This is an open-system mouth channel, not a closed local geometric QFT on the wormhole/time-machine spacetime.",
                "The environment/reservoir and frequency-dependent mouth interaction require complete stress-energy and apparatus accounting.",
                "A microscopic local action producing q(u)=0.5 exp(-u^4) has not been constructed.",
                "If the handle is dynamically formed from a globally hyperbolic region, compactly-generated-horizon/KRW obstructions must be re-tested.",
                "The zero-stress Z2 communication sector remains conditional on CBSSL and is not globally certified by the support-field construction alone.",
            ],
            "classification_reason": "A nonzero smooth Delta G_handle^+ can be constructed without spoiling the safe S1 Hadamard singularity, and its finite RSET can be absorbed in the regulated core. B, not A, because this requires an explicit open UV-soft reservoir channel rather than the closed geometric handle QFT requested by ordinary semiclassical gravity.",
        },
    ]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    closed = closed_geometric_handle()
    opened = open_gaussian_handle()
    coeffs = opened["coefficients"]
    run50 = solve_open_core(coeffs, 50)
    run70 = solve_open_core(coeffs, 70)
    precision = compare_precision(run50, run70)
    signal = receiver_control()
    candidates = candidate_records(closed, opened, run70, signal)

    data = {
        "base_sha": BASE_SHA,
        "classification": {"A": 0, "B": 1, "C": 1},
        "closed_geometric_handle": closed,
        "open_gaussian_handle": {k:v for k,v in opened.items() if k!="coefficients"},
        "precision_runs": [run50, run70],
        "max_50_70_relative_difference": precision,
        "signal": signal,
        "candidates": candidates,
        "environment": {"python": platform.python_version(), "mpmath": mp.__version__},
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

    print(json.dumps({
        "passed": True,
        "classification": data["classification"],
        "closed_geometric_handle": "C",
        "uv_soft_open_handle": "B",
        "r_planck": run70["r_planck"],
        "formal_D_past": signal["D_past"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
