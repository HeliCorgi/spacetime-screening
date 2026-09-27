#!/usr/bin/env python3
"""CBSSL v11: global image-state/RSET gate for a helical chronology quotient.

This script deliberately separates three claims:

1. A globally hyperbolic flat helical quotient with a *spacelike* deck vector.
   There the scalar two-point function is obtained by a convergent image sum,
   point-splitting reproduces the standard periodic-scalar Casimir tensor, and
   the topological correction is Hadamard-smooth at coincidence.
2. The chronology-horizon limit in which the deck vector becomes null.  The
   image correction diverges; this divergence is recorded as a failure, not
   regularized away.
3. The v10 chronology choice Delta=2 L.  Its deck vector is timelike, while a
   past-directed one-null return requires exactly that regime.  The spacelike
   Hadamard image state cannot be analytically continued and counted as a
   global quantum state there.

For the sewn Schein-Aichelburg (SA) geometry we also derive the local norm of
an axial time-helical isometry in the MP exterior and the universal short-loop
image asymptotics.  A full SA mode sum is *not* claimed because the project has
not constructed the required global Hadamard base state and singular-boundary
completion; moreover the helical image state already diverges as its orbit
becomes null.

Toy-model audit, not established new physics.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp
import sympy as sp

BASE_SHA = "3e64a86e8f65b8a1dc3ec5e71159a9b9f3332551"
V10_R0 = mp.mpf("101.4933616691277848090930477809412531792577387412069")
V10_Q2 = mp.mpf("20601.822061962252961632375628991644733357093389645794")


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def exact_flat_helical_control() -> dict:
    """Image sum + point-splitting on R^{1,2} x S^1 in helical coordinates."""
    L, D, n = sp.symbols("L Delta n", positive=True, real=True)
    a2 = sp.factor(L**2 - D**2)
    eta = sp.diag(-1, 1, 1, 1)
    k_up = sp.Matrix([-D, L, 0, 0])
    k_cov = eta * k_up

    y = sp.Matrix(sp.symbols("y0:4", real=True))
    q = sp.expand((y.T * eta * y)[0])
    G = 1 / (4 * sp.pi**2 * q)
    hess = sp.Matrix(4, 4, lambda i, j: sp.diff(G, y[i], y[j]))
    subs = {y[i]: n * k_up[i] for i in range(4)}
    T_one = sp.simplify((-hess).subs(subs))
    e_cov_outer = k_cov * k_cov.T / a2
    T_target = sp.simplify((eta - 4 * e_cov_outer) / (2 * sp.pi**2 * n**4 * a2**2))
    require(sp.simplify(T_one - T_target) == sp.zeros(4), "point-split one-image tensor")

    phi2 = sp.simplify(2 * sp.zeta(2) / (4 * sp.pi**2 * a2))
    C = sp.simplify(2 * sp.zeta(4) / (2 * sp.pi**2 * a2**2))
    require(sp.simplify(phi2 - 1 / (12 * a2)) == 0, "image phi^2 sum")
    require(sp.simplify(C - sp.pi**2 / (90 * a2**2)) == 0, "Casimir coefficient")
    T_cov = sp.simplify(C * (eta - 4 * e_cov_outer))

    trace = sp.simplify(sum(eta[i, j] * T_cov[i, j] for i in range(4) for j in range(4)))
    require(trace == 0, "flat conformal trace")
    T_upup = sp.simplify(eta * T_cov * eta)
    invariant = sp.simplify(sum(T_cov[i, j] * T_upup[i, j] for i in range(4) for j in range(4)))
    require(sp.simplify(invariant - 12 * C**2) == 0, "RSET invariant")

    adapted = sp.diag(-C, -3 * C, C, C)
    require(sp.simplify(-adapted[0, 0] - C) == 0, "Casimir energy density")

    factor = sp.factor(a2)
    require(sp.simplify(factor - (L - D) * (L + D)) == 0, "factorization")

    return {
        "metric": "eta=diag(-1,1,1,1)",
        "identification": "(t,x,y,z)~(t-Delta,x+L,y,z)",
        "deck_norm_squared": "a^2=L^2-Delta^2",
        "valid_image_state_domain": "a^2>0 (spacelike deck vector)",
        "G_quot": "sum_{n in Z} G_M^+(x, gamma^n x')",
        "Delta_G_topo": "sum_{n!=0} G_M^+(x, gamma^n x')",
        "coincident_Delta_phi2": "1/(12 a^2)",
        "point_split_topological_RSET_covariant": "(pi^2/(90 a^4))*(eta_mn-4 e_m e_n), e=k/a",
        "adapted_frame_T_cov": "(pi^2/(90 a^4))*diag(-1,-3,1,1) with compact direction second",
        "adapted_frame_energy_density": "-pi^2/(90 a^4)",
        "trace": "0",
        "trace_anomaly": "0 in flat spacetime",
        "conservation": "partial^mu T_mn=0 (constant tensor)",
        "TmnTmn": "12*(pi^2/(90 a^4))^2",
        "past_advance_condition": "Delta-L>0",
        "hadamard_image_condition": "Delta<L",
        "conditions_overlap": False,
        "point_splitting_derived": True,
    }


def image_sum_convergence() -> dict:
    """Numerical p-series convergence and rigorous integral-test tail bounds."""
    with mp.workdps(80):
        L = mp.mpf(5)
        D = mp.mpf(3)
        a2 = L*L - D*D
        exact_phi2 = 1/(12*a2)
        exact_C = mp.pi**2/(90*a2**2)
        rows = []
        for N in (8, 32, 128, 512):
            s2 = mp.fsum(1/mp.mpf(n)**2 for n in range(1, N+1))
            s4 = mp.fsum(1/mp.mpf(n)**4 for n in range(1, N+1))
            phi = s2/(2*mp.pi**2*a2)
            C = s4/(mp.pi**2*a2**2)
            phi_tail_bound = 1/(2*mp.pi**2*a2*N)
            C_tail_bound = 1/(3*mp.pi**2*a2**2*N**3)
            require(abs(phi-exact_phi2) < phi_tail_bound, "G image tail bound")
            require(abs(C-exact_C) < C_tail_bound, "RSET image tail bound")
            rows.append({
                "N": N,
                "phi2_partial": mp.nstr(phi, 35),
                "phi2_abs_error": mp.nstr(abs(phi-exact_phi2), 12),
                "phi2_tail_bound": mp.nstr(phi_tail_bound, 12),
                "casimir_C_partial": mp.nstr(C, 35),
                "casimir_C_abs_error": mp.nstr(abs(C-exact_C), 12),
                "casimir_C_tail_bound": mp.nstr(C_tail_bound, 12),
            })
        return {
            "control": {"L": "5", "Delta": "3", "a_squared": mp.nstr(a2, 20)},
            "exact_phi2_topo": mp.nstr(exact_phi2, 40),
            "exact_C": mp.nstr(exact_C, 40),
            "G_terms_decay": "n^-2",
            "RSET_terms_decay": "n^-4",
            "rows": rows,
        }


def chronology_horizon_scan() -> dict:
    """Approach a^2=L^2-Delta^2 -> 0+ without hiding the divergence."""
    with mp.workdps(80):
        L = mp.mpf(1)
        rows = []
        for beta_s in ("0", "0.5", "0.9", "0.99", "0.999", "0.9999"):
            beta = mp.mpf(beta_s)
            a2 = L*L*(1-beta*beta)
            phi2 = 1/(12*a2)
            C = mp.pi**2/(90*a2*a2)
            inv = 12*C*C
            rows.append({
                "Delta_over_L": beta_s,
                "a_over_L": mp.nstr(mp.sqrt(a2), 20),
                "phi2_times_L2": mp.nstr(phi2*L*L, 25),
                "Casimir_C_times_L4": mp.nstr(C*L**4, 25),
                "TmnTmn_times_L8": mp.nstr(inv*L**8, 25),
            })
        return {
            "limit": "Delta/L -> 1^-",
            "Delta_phi2_scaling": "(L^2-Delta^2)^-1",
            "adapted_RSET_scaling": "(L^2-Delta^2)^-2 = a^-4",
            "RSET_invariant_scaling": "(L^2-Delta^2)^-4 = a^-8",
            "finite_on_horizon": False,
            "rows": rows,
        }


def v10_timelike_gate() -> dict:
    with mp.workdps(80):
        r0 = +V10_R0
        L = 100*r0
        D = 2*L
        a2 = L*L-D*D
        advance = D-L
        require(a2 < 0 and advance > 0, "v10 chronology regime")

        k = mp.mpf(3)
        pc = (1+mp.erf(k/mp.sqrt(2)))/2
        pe = 1-pc
        formal_D = 2*pc-1

        em_scale = V10_Q2/(8*mp.pi*r0**4)
        a_equal = (mp.pi**2/(90*em_scale))**mp.mpf("0.25")
        require(a_equal > 0, "comparison length")

        return {
            "r0_planck": mp.nstr(r0, 40),
            "L_over_r0": "100",
            "Delta_over_L": "2",
            "deck_norm_squared": mp.nstr(a2, 30),
            "deck_character": "timelike",
            "one_null_past_advance": mp.nstr(advance, 30),
            "spacelike_Hadamard_image_state_available": False,
            "naive_timelike_analytic_continuation_accepted": False,
            "global_RSET_from_tested_image_state": False,
            "semiclassical_backreaction_resolved": False,
            "state_regularity": False,
            "stability": False,
            "global_self_consistent_solution_found": False,
            "formal_local_signal_only": {
                "P_Y_do_0": {"+1": mp.nstr(pc, 50), "-1": mp.nstr(pe, 50)},
                "P_Y_do_1": {"+1": mp.nstr(pe, 50), "-1": mp.nstr(pc, 50)},
                "D_past": mp.nstr(formal_D, 50),
                "globally_certified_probability": False,
            },
            "local_support_EM_scale_planck4": mp.nstr(em_scale, 30),
            "spacelike_side_a_where_Casimir_equals_EM_scale_planck": mp.nstr(a_equal, 30),
            "interpretation": "The v10 D_past remains a formal local signal-sector number, but its Delta>L chronology branch lies beyond the domain of the tested Hadamard image state. It is therefore not a globally admissible communication probability.",
        }


def sa_helical_extension() -> dict:
    """Local SA helical-isometry geometry and universal image asymptotics."""
    U, rho, D, alpha = sp.symbols("U rho Delta alpha", positive=True, real=True)
    ell2 = sp.simplify(-D**2/U**2 + U**2*rho**2*alpha**2)
    rho_h = sp.simplify(D/(alpha*U**2))
    require(sp.simplify(ell2.subs(rho, rho_h)) == 0, "SA local chronology horizon")

    with mp.workdps(50):
        U0 = mp.mpf(2)
        alpha0 = 2*mp.pi
        rho0 = mp.mpf(1)
        Dcrit = alpha0*U0**2*rho0

    return {
        "available_isometry_control": "static time translation + axial rotation in the MP/RN pieces",
        "MP_metric": "ds^2=-U^-2 dT^2+U^2(d rho^2+rho^2 dphi^2+dz^2)",
        "helical_deck": "gamma:(T,phi)->(T-Delta,phi+alpha)",
        "local_deck_norm_squared": "ell^2=U^2 rho^2 alpha^2-Delta^2/U^2",
        "chronology_horizon": "ell^2=0, locally rho_h=Delta/(alpha U^2) when U is treated as fixed over the orbit",
        "v4_shell_local_control": {"U0": "2", "rho": "1", "alpha": "2*pi", "Delta_critical": mp.nstr(Dcrit, 30)},
        "candidate_G_quot": "sum_n G_local^+(x,gamma^n x') on a spacelike-orbit region",
        "candidate_Delta_G_topo": "sum_{n!=0} G_local^+(x,gamma^n x')",
        "universal_short_loop_behavior": {
            "Delta_phi2": "~1/(12 ell^2)",
            "orthonormal_RSET_scale": "~pi^2/(90 ell^4)",
            "as_ell2_to_zero_plus": "diverges",
        },
        "full_SA_base_G_local_constructed": False,
        "full_SA_mode_sum_completed": False,
        "reasons_full_sum_not_claimed": [
            "The existing SA program does not supply a single global positive Hadamard two-point function across both shells, both RN horizons, and the timelike-singularity boundary.",
            "The v10 translational M2 throat deck transformation is not an established global deck isometry of the sewn SA geometry.",
            "For the available axial helical isometry, the image state is singular when the orbit becomes null, before extension into the CTC region.",
        ],
        "KRW_role": "Corroborating theorem for compactly generated Cauchy horizons; this script does not assume without proof that every SA helical horizon satisfies all KRW hypotheses.",
    }


def physics_sacrifices() -> list[dict]:
    return [
        {
            "physics": "global hyperbolicity / ordinary initial-value QFT",
            "sacrifice": "Past advance in the simple quotient needs a timelike deck vector (Delta>L), precisely outside the globally-hyperbolic spatial-cylinder branch used to construct the Hadamard image vacuum.",
            "v11_action": "Do not hide this by analytic continuation; mark the global state/RSET gate failed.",
        },
        {
            "physics": "standard linear quantum dynamics in the chronology sector",
            "sacrifice": "CBSSL is an explicitly new non-affine state-selection law, not derived from standard QFT or a microscopic quantum-gravity theory.",
            "v11_action": "Keep the law hypothesis separate from the independent Hadamard/RSET obstruction.",
        },
        {
            "physics": "full SA quantum state and boundary completion",
            "sacrifice": "The RN timelike singularity needs a boundary/self-adjoint completion and the two nonextremal horizons do not share one two-sided KMS temperature; a global positive Hadamard SA state is still missing.",
            "v11_action": "Do not invent G_local or fill missing mode data with flat-space noise.",
        },
        {
            "physics": "dynamical formation of the topology",
            "sacrifice": "The helical identification/SA handle is imposed as global topology; finite mouth formation, transition layers, and complete apparatus stress are not evolved from ordinary Cauchy data.",
            "v11_action": "Keep this outside the successful backreaction claims.",
        },
        {
            "physics": "controlled semiclassical expansion",
            "sacrifice": "v10 uses r0~101.5 l_P and extreme xi=-10000, while printed RSET coefficients have limited precision; numerical 1e-60 residuals are not physical 60-digit accuracy. Higher-curvature and stress-fluctuation effects are not solved.",
            "v11_action": "Treat the v10 algebraic root as a regulated toy core, not precision quantum gravity.",
        },
        {
            "physics": "dynamical stability / stochastic gravity",
            "sacrifice": "Only expectation-value backreaction in a restricted static ansatz is used; RSET fluctuations, non-spherical modes, and time-dependent instabilities are not controlled.",
            "v11_action": "Record stability as an independent failed/unproved gate rather than infer it from D_past.",
        },
    ]


def candidate_record() -> dict:
    return {
        "candidate_id": "cbssl-global-rset-helical-v11",
        "status": "C",
        "scope_of_C": "The simple v10 helical-quotient completion using a standard Hadamard image state / point-split global RSET. This does not prove a no-go for every CBSSL law, every non-Hadamard/nonstandard QFT prescription, or every possible SA topology.",
        "classification_reason": "For Delta<L the image state is Hadamard and the Casimir tensor is finite but there is no past advance. Delta>L gives the desired one-null past advance but the tested image-vacuum construction is outside its physical domain. At Delta=L the topological two-point function/RSET diverges. Hence no overlap satisfies past advance + global Hadamard image state + finite RSET + semiclassical backreaction in this quotient family.",
        "global_RSET_gate": {
            "hadamard": False,
            "conserved": "true only on spacelike control branch",
            "symmetric": "true only on spacelike control branch",
            "trace_anomaly": "zero on flat control branch; no finite quotient RSET accepted on timelike v10 branch",
            "finite": False,
        },
        "backreaction_gate": "failed before a global solve: the v10 chronology branch has no accepted global image-state RSET, while the chronology-horizon approach diverges rather than remaining a small IFT correction.",
        "communication_gate": "formal D_past>0 survives algebraically in the isolated Z2 signal sector, but it is not globally certified because state regularity and global backreaction fail.",
        "A_gate": False,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    data = {
        "base_sha": BASE_SHA,
        "classification": {"A": 0, "B": 0, "C": 1},
        "flat_helical_control": exact_flat_helical_control(),
        "convergence": image_sum_convergence(),
        "chronology_horizon": chronology_horizon_scan(),
        "v10_gate": v10_timelike_gate(),
        "sa_extension": sa_helical_extension(),
        "physics_sacrifices": physics_sacrifices(),
        "candidate": candidate_record(),
        "environment": {"python": platform.python_version(), "sympy": sp.__version__, "mpmath": mp.__version__},
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "passed": True,
        "classification": data["classification"],
        "flat_image_state": "PASS for Delta<L",
        "chronology_horizon": "DIVERGES",
        "v10_global_state": "FAIL for Delta=2L",
        "formal_D_past": data["v10_gate"]["formal_local_signal_only"]["D_past"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
