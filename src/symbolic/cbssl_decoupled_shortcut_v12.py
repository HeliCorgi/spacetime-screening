#!/usr/bin/env python3
"""CBSSL v12: decouple a safe spatial topology scale from the causal shortcut.

The v11 simple helical quotient tied the same parameters to:
  * the image-state compactification, and
  * the past-directed causal return.
That forced Delta<L for a Hadamard spatial-cylinder state and Delta>L for
one-null past advance.

v12 separates them:
  * A_topo is a purely spatial S^1 length in a regulated
    R_t x S^1 x S^2 core.  Its scalar topological correction is computed by
    a convergent mode/winding sum.
  * A separate traversable-handle shortcut has mouth separation d_ext,
    traversal time tau_shortcut and clock shift Delta_clock.  Its classical
    loop condition is Delta_clock > d_ext + tau_shortcut.

A new issue appears: the safe S^1 Casimir stress has T^t_t != T^x_x and
therefore does not fit the v10 constant-product Einstein tensor by itself.
The minimal compensator used here is a periodic axion with one spatial
winding around S^1.  Its positive kinetic stress supplies the opposite
t/x anisotropy.  We solve r, Q^2 and the axion scale simultaneously.

This is still B, not A.  The safe S^1 state/RSET and regulated core are
closed, but the separate chronology-handle contribution to the *global*
support-field two-point function/RSET is not constructed.  The handle is
an eternal prescribed shortcut/time shift, not dynamically manufactured.

Toy-model audit, not established physics.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp

BASE_SHA = "669b263e832d2f1d040706a13119470677caead4"
ALPHA = mp.mpf("4")  # A_topo / r
XI = mp.mpf("-10000")
M2 = mp.mpf("1000")
V10_R0 = mp.mpf("101.4933616691277848090930477809412531792577387412069")
V10_Q2 = mp.mpf("20601.822061962252961632375628991644733357093389645794")


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def popov_polynomials(xi: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    pt = -xi**3/6 + xi**2/12 - xi/60 + mp.mpf(1)/630
    pth = -2*pt
    return pt, pth


def local_popov_rset(r: mp.mpf) -> tuple[mp.mpf, mp.mpf]:
    """Same printed local long-throat RSET used in v10."""
    mds = mp.sqrt(M2)
    pt, pth = popov_polynomials(XI)
    logterm = mp.log(mds**2 * r**2) / 720
    ft = mp.mpf("0.00310") + logterm + pt/(M2*r**2)
    fth = -mp.mpf("0.00171") - logterm + pth/(M2*r**2)
    fac = 1/(4*mp.pi**2*r**4)
    return fac*ft, fac*fth


def conformal_circle_coefficients(
    dps: int,
    lmax: int,
    pmax: int,
    alpha: mp.mpf = ALPHA,
) -> dict:
    """Topological RSET of a massless conformal scalar on R x S1 x S2.

    For a sphere radius r and circle A=alpha*r, the angular mode l behaves
    as a 1+1 scalar of mass

        M_l = sqrt(l(l+1)+1/3) / r.

    The periodic-circle topological energy of that 1+1 mode is

        E_l = -(2l+1) M_l/pi * sum_{p>=1} K_1(p A M_l)/p.

    Derivatives of this energy give the compact and angular pressures.
    The returned mixed components scale as c_i/r^4:
        T^t_t = c_t/r^4,
        T^x_x = c_x/r^4,
        T^theta_theta = T^phi_phi = c_h/r^4.
    """
    with mp.workdps(dps):
        ebar = mp.mpf("0")
        deda_bar = mp.mpf("0")
        dedr_bar = mp.mpf("0")
        for ell in range(lmax + 1):
            c = mp.mpf(ell*(ell+1)) + mp.mpf(1)/3
            mu = mp.sqrt(c)
            g = mp.mpf(2*ell + 1)
            sum_k1_over_p = mp.mpf("0")
            sum_pressure = mp.mpf("0")
            sum_k0 = mp.mpf("0")
            for p in range(1, pmax + 1):
                z = mp.mpf(p) * alpha * mu
                k0 = mp.besselk(0, z)
                k1 = mp.besselk(1, z)
                sum_k1_over_p += k1 / p
                sum_pressure += k0 + k1/z
                sum_k0 += k0
            # Evaluate dimensionless coefficients at r=1, A=alpha.
            ebar += -g * mu/mp.pi * sum_k1_over_p
            deda_bar += g * mu**2/mp.pi * sum_pressure
            dedr_bar += -g * alpha * c/mp.pi * sum_k0

        area = 4*mp.pi
        rho = ebar/(alpha*area)
        px = -deda_bar/area
        pth = -dedr_bar/(8*mp.pi*alpha)

        # Mixed t component is -rho.
        ct, cx, ch = -rho, px, pth
        trace = ct + cx + 2*ch
        return {
            "dps": dps,
            "lmax": lmax,
            "pmax": pmax,
            "alpha": mp.nstr(alpha, 20),
            "c_t": mp.nstr(ct, 55),
            "c_x": mp.nstr(cx, 55),
            "c_theta": mp.nstr(ch, 55),
            "mixed_trace_coefficient": mp.nstr(trace, 20),
            "coefficients": (ct, cx, ch),
        }


def coefficient_convergence() -> dict:
    low = conformal_circle_coefficients(45, 20, 12)
    high = conformal_circle_coefficients(65, 24, 15)
    errs = []
    for a, b in zip(low["coefficients"], high["coefficients"]):
        errs.append(abs(a-b)/max(mp.mpf("1e-50"), abs(b)))
    max_rel = max(errs)
    require(max_rel < mp.mpf("1e-9"), "circle mode sum truncation not converged")
    ct, cx, ch = high["coefficients"]
    require(abs(ct + cx + 2*ch) < mp.mpf("1e-45"), "conformal topological trace")
    require(ct > 0 and cx < 0 and ch > 0, "unexpected circle Casimir signs")
    return {
        "low": {k: v for k, v in low.items() if k != "coefficients"},
        "high": {k: v for k, v in high.items() if k != "coefficients"},
        "max_low_high_relative_difference": mp.nstr(max_rel, 15),
        "coefficients": high["coefficients"],
    }


def massive_topology_suppression(r: mp.mpf, alpha: mp.mpf = ALPHA) -> dict:
    """Shortest winding exponent for the v10 massive nonconformal field."""
    with mp.workdps(70):
        m_eff2 = M2 + 2*XI/r**2
        require(m_eff2 > 0, "massive l=0 compact mode tachyonic")
        zmin = alpha*r*mp.sqrt(m_eff2)
        k1 = mp.besselk(1, zmin)
        # Every higher winding has p*zmin and higher l raises the effective mass.
        require(zmin > mp.mpf("1e4"), "massive compactification not exponentially suppressed")
        return {
            "m_eff_l0_squared": mp.nstr(m_eff2, 35),
            "A_times_m_eff_l0": mp.nstr(zmin, 35),
            "log10_K1_shortest_image": mp.nstr(mp.log10(k1), 25),
            "treatment": "O(exp(-A m_eff)) massive topology term is below the retained numerical/model precision and is not promoted to a fake exact zero.",
        }


def residuals(
    r: mp.mpf,
    q2: mp.mpf,
    f2: mp.mpf,
    coeffs: tuple[mp.mpf, mp.mpf, mp.mpf],
    alpha: mp.mpf = ALPHA,
) -> mp.matrix:
    """Einstein residuals with safe S1 Casimir + one axion winding."""
    ct, cx, ch = coeffs
    tq_t, tq_th = local_popov_rset(r)
    tem_t = -q2/(8*mp.pi*r**4)
    tem_th = q2/(8*mp.pi*r**4)

    # theta is a dimensionless periodic axion, L=-f^2 (d theta)^2/2,
    # theta(x+A)=theta(x)+2*pi for winding number one.
    A = alpha*r
    winding_rho = 2*mp.pi**2*f2/A**2
    # Mixed winding stress: diag(-W,+W,-W,-W).
    et = -1/r**2 - 8*mp.pi*(tq_t + tem_t + ct/r**4 - winding_rho)
    ex = -1/r**2 - 8*mp.pi*(tq_t + tem_t + cx/r**4 + winding_rho)
    eth = -8*mp.pi*(tq_th + tem_th + ch/r**4 - winding_rho)
    return mp.matrix([et, ex, eth, eth])


def solve_core(coeffs: tuple[mp.mpf, mp.mpf, mp.mpf], dps: int) -> dict:
    with mp.workdps(dps):
        r, q2, f2 = mp.findroot(
            lambda rr, qq, ff: (
                residuals(rr, qq, ff, coeffs)[0],
                residuals(rr, qq, ff, coeffs)[1],
                residuals(rr, qq, ff, coeffs)[2],
            ),
            (mp.mpf("101.4934"), mp.mpf("20601.81"), mp.mpf("6.7e-8")),
            tol=mp.power(10, -(dps-15)),
            maxsteps=80,
        )
        res = residuals(r, q2, f2, coeffs)
        maxres = max(abs(v) for v in res)
        require(r > 0 and q2 > 0 and f2 > 0, "unphysical solved parameter")
        require(maxres < mp.power(10, -(dps-20)), "v12 core residual")

        ct, cx, ch = coeffs
        A = ALPHA*r
        W = 2*mp.pi**2*f2/A**2
        anisotropy_required = (ct-cx)/(2*r**4)
        require(abs(W-anisotropy_required) < mp.power(10, -(dps-20)), "winding does not cancel t/x anisotropy")

        no_winding_tx_residual_gap = -8*mp.pi*(ct-cx)/r**4
        require(abs(no_winding_tx_residual_gap) > mp.mpf("1e-12"), "anisotropy control accidentally vanished")

        # 3x3 local Jacobian in (r,Q^2,f^2).
        J = mp.matrix(3)
        for i in range(3):
            J[i, 0] = mp.diff(lambda z: residuals(z, q2, f2, coeffs)[i], r)
            J[i, 1] = mp.diff(lambda z: residuals(r, z, f2, coeffs)[i], q2)
            J[i, 2] = mp.diff(lambda z: residuals(r, q2, z, coeffs)[i], f2)
        detJ = mp.det(J)
        require(abs(detJ) > mp.mpf("1e-20"), "v12 3-parameter Jacobian singular")

        return {
            "dps": dps,
            "r_planck": mp.nstr(r, 55),
            "Q_squared": mp.nstr(q2, 55),
            "A_topo_planck": mp.nstr(A, 55),
            "A_topo_over_r": mp.nstr(ALPHA, 20),
            "axion_f_squared_planck2": mp.nstr(f2, 55),
            "axion_f_planck": mp.nstr(mp.sqrt(f2), 45),
            "winding_energy_density": mp.nstr(W, 45),
            "topological_RSET_mixed": [
                mp.nstr(ct/r**4, 45),
                mp.nstr(cx/r**4, 45),
                mp.nstr(ch/r**4, 45),
                mp.nstr(ch/r**4, 45),
            ],
            "winding_T_mixed": [
                mp.nstr(-W, 45),
                mp.nstr(W, 45),
                mp.nstr(-W, 45),
                mp.nstr(-W, 45),
            ],
            "no_winding_t_minus_x_residual": mp.nstr(no_winding_tx_residual_gap, 30),
            "residual_mixed": [mp.nstr(v, 12) for v in res],
            "max_abs_residual": mp.nstr(maxres, 12),
            "jacobian_determinant": mp.nstr(detJ, 35),
        }


def compare_core_precision(lo: dict, hi: dict) -> str:
    errs = []
    for key in ("r_planck", "Q_squared", "axion_f_squared_planck2"):
        a, b = mp.mpf(lo[key]), mp.mpf(hi[key])
        errs.append(abs(a-b)/max(mp.mpf(1), abs(b)))
    maxerr = max(errs)
    require(maxerr < mp.mpf("1e-30"), "50/70-digit v12 solve mismatch")
    return mp.nstr(maxerr, 15)


def shortcut_witness(r: mp.mpf) -> dict:
    """Independent classical handle scale; not the S1 image identification."""
    with mp.workdps(70):
        A_topo = ALPHA*r
        d_ext = r
        tau = r/4
        delta = 2*r
        loop_coordinate_time = tau + d_ext - delta
        past_advance = -loop_coordinate_time
        require(A_topo > 0, "spatial topology")
        require(d_ext < A_topo/2, "mouth separation is not shortest on the circle")
        require(tau < delta < A_topo, "requested separated-scale witness")
        require(delta > d_ext + tau, "shortcut does not generate past advance")
        require(past_advance > 0, "past advance")
        return {
            "model": "eternal prescribed traversable-handle clock shift on a background whose separate x-cycle is purely spatial",
            "A_topo_over_r": "4",
            "d_ext_over_r": "1",
            "tau_shortcut_over_r": "1/4",
            "Delta_clock_over_r": "2",
            "inequality_witness": "tau_shortcut + d_ext < Delta_clock < A_topo",
            "loop_coordinate_time_over_r": "-3/4",
            "past_advance_over_r": "3/4",
            "A_topo_planck": mp.nstr(A_topo, 40),
            "d_ext_planck": mp.nstr(d_ext, 40),
            "tau_shortcut_planck": mp.nstr(tau, 40),
            "Delta_clock_planck": mp.nstr(delta, 40),
            "past_advance_planck": mp.nstr(past_advance, 40),
            "spatial_image_deck_timelike": False,
            "causal_shortcut_is_same_as_image_deck": False,
            "chronology_horizon_formation_modeled": False,
        }


def z2_receiver() -> dict:
    with mp.workdps(80):
        k = mp.mpf(3)
        pc = (1+mp.erf(k/mp.sqrt(2)))/2
        pe = 1-pc
        D = 2*pc-1
        return {
            "P_Y_do_0": {"+1": mp.nstr(pc, 50), "-1": mp.nstr(pe, 50)},
            "P_Y_do_1": {"+1": mp.nstr(pe, 50), "-1": mp.nstr(pc, 50)},
            "D_past": mp.nstr(D, 50),
            "interpretation": "Same zero-local-stress Z2 receiver law as v10, now conditional on a CBSSL loop state for the separate shortcut handle. It is not globally certified until the handle support-field state/RSET is constructed.",
        }


def candidate_record(core: dict, shortcut: dict, signal: dict) -> dict:
    return {
        "candidate_id": "cbssl-decoupled-topology-shortcut-v12",
        "status": "B",
        "dimension": 4,
        "geometry": "Regulated R_t x S1_x x S2 core for the safe support-field topology, plus a separate prescribed traversable-handle causal shortcut/time shift between two worldtubes.",
        "safe_topology": {
            "identification": "x~x+A_topo only; no time shift in the image-state deck transformation",
            "A_topo_over_r": "4",
            "Hadamard_spatial_circle_state": True,
            "topological_RSET_computed": True,
        },
        "anisotropy_compensator": {
            "field": "periodic axion theta with winding number one on S1",
            "stress": "T^mu_nu=diag(-W,+W,-W,-W), W=2*pi^2*f^2/A_topo^2",
            "reason": "The safe S1 Casimir has T^t_t != T^x_x, while the v10 constant product has G^t_t=G^x_x. Winding supplies the missing opposite anisotropy.",
            "solved_f_squared": core["axion_f_squared_planck2"],
        },
        "backreaction": {
            "safe_sector_self_consistent": True,
            "r_planck": core["r_planck"],
            "Q_squared": core["Q_squared"],
            "max_abs_residual": core["max_abs_residual"],
            "jacobian_determinant": core["jacobian_determinant"],
            "chronology_handle_global_RSET_included": False,
        },
        "causal_shortcut": shortcut,
        "sender_intervention": {
            "description": "Same zero-stress Z2 bit operation as v10, with the causal return assigned to the separate handle rather than the spatial S1 image deck.",
            "same_preparation": True,
            "uses_postselection": False,
        },
        "P_Y_do_0": {"computed": True, "conditional": True, "distribution": signal["P_Y_do_0"]},
        "P_Y_do_1": {"computed": True, "conditional": True, "distribution": signal["P_Y_do_1"]},
        "distinguishability": {
            "metric": "total_variation",
            "computed": True,
            "conditional": True,
            "value": signal["D_past"],
            "globally_certified": False,
        },
        "global_state_gate": {
            "safe_S1_support_state": "constructed by mode/winding sum",
            "chronology_handle_support_state": "not_constructed",
            "full_global_Hadamard_state": False,
        },
        "unresolved_assumptions": [
            "Construct the support-field two-point function and nonlocal RSET associated with the separate chronology handle itself; the safe S1 Casimir is not that missing handle term.",
            "Show that the eternal prescribed time-shift handle admits a positive state with the required local Hadamard behavior and CBSSL loop condition.",
            "If the handle/time shift is dynamically formed from a globally hyperbolic region, re-test compact-generation/KRW chronology-horizon obstructions instead of using the eternal-handle assumption.",
            "Construct finite mouths/transition layers and include their complete classical and quantum stress.",
            "Establish nonspherical, time-dependent and stress-fluctuation stability.",
        ],
        "classification_reason": "The v11 algebraic no-overlap is removed: a purely spatial Hadamard topology and an independent past-directed shortcut have a nonempty parameter region, and the safe topology sector can be semiclassically retuned after adding a minimal winding compensator. B, not A, because the causal handle's own global quantum state/RSET and manufactured geometry remain unsolved.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    conv = coefficient_convergence()
    coeffs = conv["coefficients"]
    core50 = solve_core(coeffs, 50)
    core70 = solve_core(coeffs, 70)
    precision = compare_core_precision(core50, core70)
    massive = massive_topology_suppression(mp.mpf(core70["r_planck"]))
    shortcut = shortcut_witness(mp.mpf(core70["r_planck"]))
    signal = z2_receiver()
    candidate = candidate_record(core70, shortcut, signal)

    data = {
        "base_sha": BASE_SHA,
        "classification": {"A": 0, "B": 1, "C": 0},
        "circle_mode_sum": {k: v for k, v in conv.items() if k != "coefficients"},
        "massive_topology_suppression": massive,
        "precision_runs": [core50, core70],
        "max_50_70_relative_difference": precision,
        "shortcut": shortcut,
        "signal": signal,
        "candidate": candidate,
        "environment": {"python": platform.python_version(), "mpmath": mp.__version__},
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({
        "passed": True,
        "classification": data["classification"],
        "r_planck": core70["r_planck"],
        "Q_squared": core70["Q_squared"],
        "axion_f_squared": core70["axion_f_squared_planck2"],
        "past_advance_over_r": shortcut["past_advance_over_r"],
        "formal_D_past": signal["D_past"],
        "global_handle_RSET": "UNSOLVED",
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
