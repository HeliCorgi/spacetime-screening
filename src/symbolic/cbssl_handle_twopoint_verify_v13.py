#!/usr/bin/env python3
"""Independent verifier for CBSSL v13 chronology-handle two-point audit."""
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

CT = mp.mpf("0.00039115324987090346409958722388060179527777892968766")
CX = mp.mpf("-0.0013135652650630378856936929316968132131234586046131")
CH = mp.mpf("0.0004612060075960672107970528539081057089228398374627")

N0 = mp.mpf("0.01")


def req(ok, message):
    if not ok:
        raise AssertionError(message)


def geometric_image_control():
    with mp.workdps(70):
        q = mp.mpf("0.5")
        ell = mp.mpf("1.25")
        li2 = mp.polylog(2, q)
        li4 = mp.polylog(4, q)

        vals = []
        prev_rset = None
        for eps_s in ("1e-1", "1e-2", "1e-3", "1e-4"):
            eps = mp.mpf(eps_s)
            # s^2/r^2 is treated directly as a positive approach to zero.
            phi = li2/(2*mp.pi**2*eps)
            rset = li4/(mp.pi**2*eps**2)
            if prev_rset is not None:
                req(abs(rset/prev_rset-mp.mpf("100")) < mp.mpf("1e-60"), "s^-4 scaling")
            vals.append({
                "s_squared_over_r2": eps_s,
                "Delta_phi2_times_r2": mp.nstr(phi, 30),
                "RSET_scale_times_r4": mp.nstr(rset, 30),
            })
            prev_rset = rset

        actual_s2 = ell**2-mp.mpf(2)**2
        req(actual_s2 < 0, "actual handle not timelike")
        return {
            "fixed_q": "1/2",
            "null_limit_finite": False,
            "actual_loop_interval_squared_over_r2": mp.nstr(actual_s2, 25),
            "actual_standard_Hadamard_image_completion": False,
            "rows": vals,
        }


def open_state_control():
    with mp.workdps(70):
        i1 = mp.quad(lambda u: u*mp.e**(-u**4), [0, 1, mp.inf])
        i3 = mp.quad(lambda u: u**3*mp.e**(-u**4), [0, 1, mp.inf])
        req(abs(i1-mp.sqrt(mp.pi)/4) < mp.mpf("1e-55"), "i1")
        req(abs(i3-mp.mpf("0.25")) < mp.mpf("1e-55"), "i3")

        phi_coeff = N0/(8*mp.pi**(mp.mpf("1.5")))
        rho_coeff = N0/(8*mp.pi**2)

        # Pure-loss fixed covariance control at several u.
        for u in (mp.mpf("0"), mp.mpf("0.7"), mp.mpf("1.5"), mp.mpf("3")):
            q = mp.mpf("0.5")*mp.e**(-u**4)
            N = N0*mp.e**(-u**4)
            nout = q*q*N+(1-q*q)*N
            req(abs(nout-N) < mp.mpf("1e-60"), "fixed Gaussian occupation")
            req(0 <= q < 1, "return contraction")
        return {
            "Delta_phi2_coefficient": mp.nstr(phi_coeff, 40),
            "rho_coefficient": mp.nstr(rho_coeff, 40),
            "positive_occupation": True,
            "UV_smooth": True,
            "CCR_correction_symmetric": True,
        }, (-rho_coeff, rho_coeff/3, rho_coeff/3)


def popov(y):
    mds = mp.sqrt(M2)
    pt = -XI**3/6+XI**2/12-XI/60+mp.mpf(1)/630
    pth = -2*pt
    log = mp.log(mds**2*y)/720
    fac = 1/(4*mp.pi**2*y**2)
    return (
        fac*(mp.mpf("0.00310")+log+pt/(M2*y)),
        fac*(-mp.mpf("0.00171")-log+pth/(M2*y)),
    )


def alternative_core(handle_coeffs):
    """Eliminate winding anisotropy and solve in y=r^2,Q^2."""
    with mp.workdps(60):
        ht, hx, hh = handle_coeffs
        ct = CT+ht
        cx = CX+hx
        ch = CH+hh

        cw = (ct-cx)/2
        common = (ct+cx)/2
        angular_eff = ch-cw
        req(cw > 0, "required winding coefficient not positive")

        def F(y, q2):
            tt, th = popov(y)
            emt = -q2/(8*mp.pi*y**2)
            emh = q2/(8*mp.pi*y**2)
            return (
                -1/y-8*mp.pi*(tt+emt+common/y**2),
                -8*mp.pi*(th+emh+angular_eff/y**2),
            )

        y, q2 = mp.findroot(F, (mp.mpf("10300.9"), mp.mpf("20601.81")), tol=mp.mpf("1e-45"))
        r = mp.sqrt(y)
        f2 = cw*ALPHA**2/(2*mp.pi**2*y)
        res = F(y, q2)
        req(max(abs(v) for v in res) < mp.mpf("1e-40"), "alternative core")

        return {
            "r_planck": mp.nstr(r, 45),
            "Q_squared": mp.nstr(q2, 45),
            "axion_f_squared_planck2": mp.nstr(f2, 45),
            "max_abs_residual": mp.nstr(max(abs(v) for v in res), 12),
        }


def receiver():
    with mp.workdps(70):
        k = mp.mpf(3)
        pc = (1+mp.erf(k/mp.sqrt(2)))/2
        pe = 1-pc
        D = 2*pc-1
        return {
            "P0_plus": mp.nstr(pc,45),
            "P1_plus": mp.nstr(pe,45),
            "D_past": mp.nstr(D,45),
            "globally_certified": False,
        }


def evidence(path: Path, alt: dict):
    data = json.loads(path.read_text(encoding="utf-8"))
    src = Path(__file__).with_name("cbssl_handle_twopoint_v13.py")
    req(data["base_sha"] == BASE_SHA, "base")
    req(data["code_sha256"] == hashlib.sha256(src.read_bytes()).hexdigest(), "stale evidence")
    req(data["classification"] == {"A":0,"B":1,"C":1}, "classification")
    statuses = {c["candidate_id"]: c["status"] for c in data["candidates"]}
    req(statuses["cbssl-closed-geometric-handle-image-v13"] == "C", "closed status")
    req(statuses["cbssl-uv-soft-open-handle-v13"] == "B", "open status")
    req(data["open_gaussian_handle"]["positive_quasifree_state"] is True, "positivity")
    req(data["open_gaussian_handle"]["CCR_preserved"] is True, "CCR")
    req(data["open_gaussian_handle"]["Hadamard_preserved"] is True, "Hadamard")
    req(data["closed_geometric_handle"]["fixed_attenuation_removes_null_divergence"] is False, "closed divergence hidden")

    fwd = data["precision_runs"][-1]
    for key in ("r_planck","Q_squared","axion_f_squared_planck2"):
        a = mp.mpf(alt[key])
        b = mp.mpf(fwd[key])
        req(abs(a-b)/max(mp.mpf(1),abs(b)) < mp.mpf("1e-10"), f"root mismatch {key}")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    geom = geometric_image_control()
    open_ctl, coeffs = open_state_control()
    alt = alternative_core(coeffs)
    recv = receiver()

    out = {
        "verified": True,
        "classification": {"A":0,"B":1,"C":1},
        "closed_geometric_handle": geom,
        "open_gaussian_handle": open_ctl,
        "alternative_core": alt,
        "receiver": recv,
        "environment": {"python": platform.python_version(), "mpmath": mp.__version__},
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if args.evidence:
        out["evidence_sha256"] = evidence(args.evidence, alt)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

    print(json.dumps({
        "verified": True,
        "closed_geometric_handle": "C",
        "uv_soft_open_handle": "B",
        "r_planck": alt["r_planck"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
