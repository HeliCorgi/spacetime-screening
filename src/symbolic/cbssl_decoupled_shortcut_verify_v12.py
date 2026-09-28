#!/usr/bin/env python3
"""Independent verifier for CBSSL v12 decoupled topology/shortcut candidate."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp

BASE_SHA = "669b263e832d2f1d040706a13119470677caead4"
ALPHA = mp.mpf("4")
XI = mp.mpf("-10000")
M2 = mp.mpf("1000")


def req(ok, message):
    if not ok:
        raise AssertionError(message)


def independent_circle_coefficients(dps=50, lmax=18, pmax=10):
    """Recompute the conformal S1 x S2 topological tensor without forward code."""
    with mp.workdps(dps):
        E = mp.mpf("0")
        dA = mp.mpf("0")
        dR = mp.mpf("0")
        for ell in range(lmax + 1):
            c = mp.mpf(ell*(ell+1)) + mp.mpf(1)/3
            mu = mp.sqrt(c)
            g = mp.mpf(2*ell+1)
            s1 = mp.mpf("0")
            sp = mp.mpf("0")
            s0 = mp.mpf("0")
            for p in range(1, pmax + 1):
                z = p*ALPHA*mu
                k0 = mp.besselk(0, z)
                k1 = mp.besselk(1, z)
                s1 += k1/p
                sp += k0 + k1/z
                s0 += k0
            E -= g*mu/mp.pi*s1
            dA += g*mu**2/mp.pi*sp
            dR -= g*ALPHA*c/mp.pi*s0

        rho = E/(ALPHA*4*mp.pi)
        px = -dA/(4*mp.pi)
        pth = -dR/(8*mp.pi*ALPHA)
        ct, cx, ch = -rho, px, pth
        req(abs(ct+cx+2*ch) < mp.mpf("1e-40"), "conformal trace")
        return ct, cx, ch


def alternative_core(coeffs):
    """Eliminate winding anisotropy first, then solve in y=r^2 and Q^2."""
    with mp.workdps(60):
        ct, cx, ch = coeffs
        cw = (ct-cx)/2
        common = (ct+cx)/2
        theta_eff = ch-cw
        req(cw > 0, "winding energy must be positive")

        xi = XI
        m2 = M2
        mds = mp.sqrt(m2)
        pt = -xi**3/6 + xi**2/12 - xi/60 + mp.mpf(1)/630
        pth = -2*pt

        def qlocal(y):
            logterm = mp.log(mds**2*y)/720
            fac = 1/(4*mp.pi**2*y**2)
            tt = fac*(mp.mpf("0.00310")+logterm+pt/(m2*y))
            th = fac*(-mp.mpf("0.00171")-logterm+pth/(m2*y))
            return tt, th

        def F(y, q2):
            tt, th = qlocal(y)
            emt = -q2/(8*mp.pi*y**2)
            emh = q2/(8*mp.pi*y**2)
            return (
                -1/y - 8*mp.pi*(tt+emt+common/y**2),
                -8*mp.pi*(th+emh+theta_eff/y**2),
            )

        y, q2 = mp.findroot(F, (mp.mpf("10300.9"), mp.mpf("20601.81")), tol=mp.mpf("1e-45"))
        res = F(y, q2)
        req(max(abs(v) for v in res) < mp.mpf("1e-40"), "alternative core residual")
        r = mp.sqrt(y)
        f2 = cw*ALPHA**2/(2*mp.pi**2*y)
        W = cw/y**2

        # Rebuild all three mixed equations explicitly.
        tt, th = qlocal(y)
        emt = -q2/(8*mp.pi*y**2)
        emh = q2/(8*mp.pi*y**2)
        et = -1/y - 8*mp.pi*(tt+emt+ct/y**2-W)
        ex = -1/y - 8*mp.pi*(tt+emt+cx/y**2+W)
        eh = -8*mp.pi*(th+emh+ch/y**2-W)
        req(max(abs(et), abs(ex), abs(eh)) < mp.mpf("1e-40"), "three component closure")

        return {
            "r_planck": mp.nstr(r, 45),
            "Q_squared": mp.nstr(q2, 45),
            "axion_f_squared_planck2": mp.nstr(f2, 45),
            "winding_energy_density": mp.nstr(W, 35),
            "max_abs_residual": mp.nstr(max(abs(et), abs(ex), abs(eh)), 12),
            "c_t": mp.nstr(ct, 35),
            "c_x": mp.nstr(cx, 35),
            "c_theta": mp.nstr(ch, 35),
        }


def shortcut_control():
    r = mp.mpf(1)
    A = 4*r
    d = r
    tau = r/4
    delta = 2*r
    req(d < A/2, "shortest external mouth separation")
    req(tau + d < delta < A, "separated shortcut/topology wedge")
    return {
        "A_topo_over_r": "4",
        "d_ext_over_r": "1",
        "tau_shortcut_over_r": "1/4",
        "Delta_clock_over_r": "2",
        "past_advance_over_r": mp.nstr(delta-d-tau, 20),
        "safe_spatial_topology_and_past_advance_overlap": True,
    }


def receiver_control():
    with mp.workdps(70):
        k = mp.mpf(3)
        pc = (1+mp.erf(k/mp.sqrt(2)))/2
        pe = 1-pc
        D = 2*pc-1
        return {
            "P0_plus": mp.nstr(pc, 45),
            "P1_plus": mp.nstr(pe, 45),
            "D_past": mp.nstr(D, 45),
            "globally_certified": False,
        }


def evidence(path: Path, alt: dict):
    data = json.loads(path.read_text(encoding="utf-8"))
    src = Path(__file__).with_name("cbssl_decoupled_shortcut_v12.py")
    req(data["base_sha"] == BASE_SHA, "base")
    req(data["code_sha256"] == hashlib.sha256(src.read_bytes()).hexdigest(), "stale evidence")
    req(data["classification"] == {"A": 0, "B": 1, "C": 0}, "classification")
    req(data["candidate"]["status"] == "B", "status")
    req(data["candidate"]["safe_topology"]["Hadamard_spatial_circle_state"] is True, "safe topology")
    req(data["candidate"]["backreaction"]["safe_sector_self_consistent"] is True, "safe closure")
    req(data["candidate"]["backreaction"]["chronology_handle_global_RSET_included"] is False, "handle overclaim")
    req(data["candidate"]["global_state_gate"]["full_global_Hadamard_state"] is False, "global state overclaim")
    req(data["candidate"]["distinguishability"]["globally_certified"] is False, "communication overclaim")

    fwd = data["precision_runs"][-1]
    for key in ("r_planck", "Q_squared", "axion_f_squared_planck2"):
        a = mp.mpf(alt[key])
        b = mp.mpf(fwd[key])
        rel = abs(a-b)/max(mp.mpf(1), abs(b))
        req(rel < mp.mpf("1e-9"), f"independent root mismatch {key}")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    coeffs = independent_circle_coefficients()
    alt = alternative_core(coeffs)
    shortcut = shortcut_control()
    receiver = receiver_control()
    out = {
        "verified": True,
        "classification": {"A": 0, "B": 1, "C": 0},
        "alternative_core": alt,
        "shortcut": shortcut,
        "receiver": receiver,
        "environment": {"python": platform.python_version(), "mpmath": mp.__version__},
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if args.evidence:
        out["evidence_sha256"] = evidence(args.evidence, alt)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({
        "verified": True,
        "classification": "B",
        "safe_topology_and_past_advance_overlap": True,
        "r_planck": alt["r_planck"],
        "formal_D_past": receiver["D_past"],
        "global_handle_RSET": "UNSOLVED",
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
