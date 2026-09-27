#!/usr/bin/env python3
"""Independent verifier for CBSSL v11 helical global-RSET gate."""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp
import sympy as sp

BASE_SHA = "3e64a86e8f65b8a1dc3ec5e71159a9b9f3332551"


def req(ok, msg):
    if not ok:
        raise AssertionError(msg)


def independent_flat_cylinder():
    """Verify standard periodic-scalar Casimir data without forward code."""
    with mp.workdps(80):
        a = mp.mpf(4)
        n_phi = 19999
        n_c = 1999
        phi = mp.fsum(2 / (4 * mp.pi**2 * (n * a)**2) for n in range(1, n_phi + 1))
        phi_exact = 1 / (12 * a * a)
        phi_tail = 1 / (2 * mp.pi**2 * a * a * n_phi)
        req(abs(phi - phi_exact) < phi_tail, "phi image convergence")

        C = mp.fsum(1 / (mp.pi**2 * n**4 * a**4) for n in range(1, n_c + 1))
        C_exact = mp.pi**2 / (90 * a**4)
        C_tail = 1 / (3 * mp.pi**2 * a**4 * n_c**3)
        req(abs(C - C_exact) < C_tail, "Casimir convergence")

        # Covariant tensor in an orthonormal frame whose x direction is compact:
        # C*diag(-1,-3,1,1).  Contract with eta^{ab}.
        diag = (-C_exact, -3*C_exact, C_exact, C_exact)
        trace = -diag[0] + diag[1] + diag[2] + diag[3]
        req(abs(trace) < mp.mpf("1e-70"), "trace")
        invariant = sum(v*v for v in diag)
        req(abs(invariant - 12*C_exact**2) < mp.mpf("1e-70"), "invariant")

        return {
            "a": mp.nstr(a, 20),
            "phi2_partial": mp.nstr(phi, 35),
            "phi2_exact": mp.nstr(phi_exact, 35),
            "phi2_tail_bound": mp.nstr(phi_tail, 12),
            "C_partial": mp.nstr(C, 35),
            "C_exact": mp.nstr(C_exact, 35),
            "C_tail_bound": mp.nstr(C_tail, 12),
            "trace": mp.nstr(trace, 12),
            "TmnTmn": mp.nstr(invariant, 35),
        }


def causal_domain_gate():
    """The Hadamard cylinder branch and one-null past advance do not overlap."""
    L, D = sp.symbols("L Delta", positive=True, real=True)
    a2 = sp.factor(L**2 - D**2)
    req(sp.factor(a2 - (L-D)*(L+D)) == 0, "factorization")

    controls = []
    for beta in (sp.Rational(1, 2), sp.Integer(1), sp.Integer(2)):
        aa = sp.simplify(a2.subs({L: 1, D: beta}))
        advance = sp.simplify((D-L).subs({L: 1, D: beta}))
        controls.append({
            "Delta_over_L": str(beta),
            "a_squared_over_L2": str(aa),
            "past_advance_over_L": str(advance),
        })
    req(controls[0]["a_squared_over_L2"] == "3/4", "spacelike control")
    req(controls[1]["a_squared_over_L2"] == "0", "null control")
    req(controls[2]["a_squared_over_L2"] == "-3", "timelike control")
    req(controls[2]["past_advance_over_L"] == "1", "past advance control")

    return {
        "Hadamard_image_domain": "Delta<L",
        "one_null_past_advance_domain": "Delta>L",
        "overlap": False,
        "null_boundary": "Delta=L",
        "controls": controls,
    }


def horizon_blowup():
    """Independent scaling check of the unregularized horizon divergence."""
    with mp.workdps(80):
        rows = []
        previous = None
        for a2_s in ("1e-1", "1e-2", "1e-3", "1e-4"):
            a2 = mp.mpf(a2_s)
            phi = 1/(12*a2)
            C = mp.pi**2/(90*a2**2)
            inv = 12*C*C
            if previous is not None:
                ratio = inv/previous
                req(abs(ratio-mp.mpf("1e4")) < mp.mpf("1e-70"), "a^-8 invariant scaling")
            else:
                ratio = None
            rows.append({
                "a_squared": a2_s,
                "phi2": mp.nstr(phi, 25),
                "C": mp.nstr(C, 25),
                "TmnTmn": mp.nstr(inv, 25),
                "ratio_to_previous_invariant": None if ratio is None else mp.nstr(ratio, 12),
            })
            previous = inv
        return {
            "finite_at_a_squared_zero": False,
            "phi2_scaling": "a^-2",
            "RSET_scaling": "a^-4",
            "invariant_scaling": "a^-8",
            "rows": rows,
        }


def sa_local_geometry_control():
    U, rho, D, alpha = sp.symbols("U rho Delta alpha", positive=True, real=True)
    ell2 = sp.simplify(U**2*rho**2*alpha**2 - D**2/U**2)
    rho_h = sp.simplify(D/(alpha*U**2))
    req(sp.simplify(ell2.subs(rho, rho_h)) == 0, "SA helical norm")
    with mp.workdps(60):
        threshold = 2*mp.pi*mp.mpf(2)**2*mp.mpf(1)
        req(abs(threshold-8*mp.pi) < mp.mpf("1e-50"), "SA threshold")
        return {
            "ell_squared": "U^2 rho^2 alpha^2-Delta^2/U^2",
            "rho_h": "Delta/(alpha U^2)",
            "U0_2_rho1_alpha2pi_Delta_critical": mp.nstr(threshold, 30),
        }


def formal_receiver_control():
    with mp.workdps(80):
        k = mp.mpf(3)
        pc = (1+mp.erf(k/mp.sqrt(2)))/2
        pe = 1-pc
        d = 2*pc-1
        req(d > 0, "formal receiver")
        return {
            "P0_plus": mp.nstr(pc, 50),
            "P1_plus": mp.nstr(pe, 50),
            "D_past": mp.nstr(d, 50),
            "globally_certified": False,
        }


def verify_evidence(path: Path):
    data = json.loads(path.read_text(encoding="utf-8"))
    src = Path(__file__).with_name("cbssl_global_rset_v11.py")
    req(data["base_sha"] == BASE_SHA, "base SHA")
    req(data["code_sha256"] == hashlib.sha256(src.read_bytes()).hexdigest(), "stale forward evidence")
    req(data["classification"] == {"A": 0, "B": 0, "C": 1}, "classification")
    req(data["candidate"]["status"] == "C", "candidate status")
    req(data["flat_helical_control"]["conditions_overlap"] is False, "causal overlap")
    req(data["chronology_horizon"]["finite_on_horizon"] is False, "horizon finite")
    req(data["v10_gate"]["spacelike_Hadamard_image_state_available"] is False, "v10 state gate")
    req(data["v10_gate"]["global_self_consistent_solution_found"] is False, "v10 backreaction gate")
    req(data["v10_gate"]["formal_local_signal_only"]["globally_certified_probability"] is False, "communication certification")
    req(data["sa_extension"]["full_SA_mode_sum_completed"] is False, "SA overclaim")
    req(len(data["physics_sacrifices"]) >= 6, "physics sacrifice accounting")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    out = {
        "verified": True,
        "base_sha": BASE_SHA,
        "classification": {"A": 0, "B": 0, "C": 1},
        "flat_cylinder": independent_flat_cylinder(),
        "causal_gate": causal_domain_gate(),
        "horizon": horizon_blowup(),
        "sa_local_geometry": sa_local_geometry_control(),
        "formal_receiver": formal_receiver_control(),
        "environment": {"python": platform.python_version(), "sympy": sp.__version__, "mpmath": mp.__version__},
        "verifier_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if args.evidence:
        out["evidence_sha256"] = verify_evidence(args.evidence)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({
        "verified": True,
        "classification": "C",
        "safe_state_and_past_advance_overlap": False,
        "formal_D_past": out["formal_receiver"]["D_past"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
