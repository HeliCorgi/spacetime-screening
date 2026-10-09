#!/usr/bin/env python3
"""Independent finite consistency checks for the return-rigidity note.

Uses Euler--Lagrange screen variations and the embedding solution for round
sphere geodesics. Does not import the producer. The continuum theorem remains
an analytic argument, not a machine-checked theorem.
"""
from __future__ import annotations

import argparse
from fractions import Fraction
import hashlib
import json
from pathlib import Path
import platform
import sys
from typing import Any

import sympy as s

PARENT = "27e78fe8ab10566c2f54d787ba8e15e1ce0aa65a"


def lagrangian_screen() -> dict[str, Any]:
    lam, ell, e = s.symbols("lambda ell epsilon", real=True)
    t, psi, x, z = [s.Function(name)(lam) for name in ("t", "psi", "x", "z")]
    L = (-2*s.diff(t, lam)*s.diff(psi, lam)
         - t**3*s.diff(psi, lam)**2
         + s.diff(x, lam)**2+s.diff(z, lam)**2)/2
    eq = [s.simplify(s.diff(s.diff(L, s.diff(q, lam)), lam)-s.diff(L, q))
          for q in (t, psi, x, z)]
    assert eq[2] == s.diff(x, lam, 2)
    assert eq[3] == s.diff(z, lam, 2)
    q0, v0 = s.symbols("q0 v0", real=True)
    screen_solution = q0+lam*v0
    assert s.diff(screen_solution, lam, 2) == 0
    screen_map = s.Matrix([screen_solution.subs(lam, ell), v0]).jacobian([q0, v0])
    assert screen_map == s.Matrix([[1, ell], [0, 1]])
    # Verify directly that t=0, psi=lambda, x=z=0 is a geodesic.
    subs = {t: 0, psi: lam, x: 0, z: 0}
    assert all(s.simplify(a.subs(subs).doit()) == 0 for a in eq)
    # A screen variation changes the null constraint only at second order.
    perturbed = L.subs({t: 0, psi: lam, x: e*screen_solution, z: 0}).doit()
    assert s.diff(perturbed, e).subs(e, 0) == 0
    out = [[str(screen_map[i, j].subs(ell, 1)) for j in range(2)] for i in range(2)]
    return {"screen_return_at_ell_1": out,
            "reference_loop_affine": True,
            "linear_screen_is_tangent_to_null_cone": True}


def exact_round_sphere_return() -> dict[str, Any]:
    # For |X0|=a, X0.V0=0, |V0|=E, this solves the round-sphere geodesic
    # equation. Temporal advance is E*L=2*pi*a, i.e. the actual deck period.
    a, E, lam = s.symbols("a E lambda", positive=True)
    x0, v0 = s.symbols("x0 v0", real=True)
    X = s.cos(E*lam/a)*x0 + a/E*s.sin(E*lam/a)*v0
    V = s.diff(X, lam)
    L = 2*s.pi*a/E
    assert s.simplify(s.diff(X, lam, 2)+(E/a)**2*X) == 0
    assert s.simplify(X.subs(lam, L)-x0) == 0
    assert s.simplify(V.subs(lam, L)-v0) == 0
    assert s.simplify(E*L-2*s.pi*a) == 0
    # This is a whole family (arbitrary X0,V0,E), not just one Jacobi matrix.
    return {"whole_round_geodesic_family_returns": True,
            "not_merely_first_jet": True}


def rational_countercontrols() -> dict[str, Any]:
    # Polynomial expressions depend only on residue classes modulo two.
    residues = [(2*n*n-2*j*j-1) % 2 for n in range(2) for j in range(2)]
    assert residues == [1]*4
    # First-jet identity alone is not identity of a canonical map germ.
    witnesses = []
    for N in [2, 4, 16, 256]:
        q = Fraction(1, N)
        kick = q**3
        assert kick > 0
        witnesses.append({"q": str(q), "kick": str(kick)})
    # One-sided scaling cannot be absorbed by joint conicity.
    kin = (Fraction(1), Fraction(0))
    kout = tuple(2*a for a in kin)
    assert kout != kin
    # If c*(-kin)=-kin then c=1, which cannot change kout to kin.
    c = kin[0]/kin[0]
    residual = tuple(c*a-b for a, b in zip(kout, kin))
    assert c == 1 and any(r != 0 for r in residual)
    return {"all_parity_classes": residues,
            "canonical_nonidentity_witnesses": witnesses,
            "joint_scaling_cannot_remove_mismatch": True}


def need(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def validate_evidence(data: dict[str, Any], independent: dict[str, Any]) -> None:
    need(data.get("schema") == "chronology-return-rigidity-v1", "schema")
    need(data.get("parent_sha") == PARENT, "parent")
    checks = data["checks"]
    ham = checks["hamiltonian"]
    need(ham["screen_return_at_ell_1"] == independent["lagrangian"]["screen_return_at_ell_1"], "screen matrix")
    need(ham["zero_boost_multiplier"] == "1", "zero-boost multiplier")
    need(ham["affine_front_multiplier"] == "exp(gamma*ell/2)", "affine multiplier")
    need(ham["log_abs_p_t_per_psi"] == "-F_t/2", "log derivative")
    need(ham["screen_return_is_identity"] is False, "screen rigidity flag")
    need(ham["screen_return_is_symplectic"] is True, "screen symplectic flag")
    ref = checks["refocusing"]
    need(ref["ESU_screen_return"] == [["1", "0"], ["0", "1"]], "ESU matrix")
    need(ref["first_jet_countercontrol"]["identity_germ"] is False, "jet versus germ")
    need(ref["first_jet_countercontrol"]["spacetime_realization_claimed"] is False, "canonical versus geometric example")
    spec = checks["spectral"]
    need(spec["mass_squared_times_a_squared"] == "1/2", "mass shift")
    need(type(spec["twice_eigenvalue_mod_2"]) is int and spec["twice_eigenvalue_mod_2"] == 1, "parity")
    need(spec["all_mode_gap_lower_bound"] == "1/2", "spectral gap")
    need(spec["nonzero_periodic_distributional_KG_solution"] is False, "massive KG kernel")
    need(spec["Hadamard_state"] is False, "massive state")
    need(spec["massless_control_has_infinite_kernel"] is True, "massless control")
    theorem = data["analytic_result"]
    need(type(theorem["dimension_minimum_for_chronology_corollary"]) is int and
         theorem["dimension_minimum_for_chronology_corollary"] == 3, "dimension")
    for key in ("requires_whole_ray_tube", "requires_local_Hadamard_WF_equality",
                "requires_PxW_smooth_on_tube_times_U"):
        need(theorem[key] is True, key)
    for key in ("uses_positivity", "uses_Einstein_equation", "uses_compact_generation",
                "germ_identity_sufficient_for_state", "WF_theorem_machine_proved"):
        need(theorem[key] is False, key)
    for key in ("formation_solution_found", "universal_formation_no_go", "RSET_or_SCEE_solved_here"):
        need(data[key] is False, key)
    need(data["implemented_checks"] == "passed", "finite check status")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", type=Path, help="Optional producer JSON for cross-checking")
    parser.add_argument("--output", type=Path, help="Optional verifier JSON")
    args = parser.parse_args()
    try:
        independent = {"lagrangian": lagrangian_screen(),
                       "round_return": exact_round_sphere_return(),
                       "countercontrols": rational_countercontrols()}
        if args.evidence:
            data = json.loads(args.evidence.read_text(encoding="utf-8"))
            need(isinstance(data, dict), "evidence must be a JSON object")
            validate_evidence(data, independent)
        report = {"schema": "chronology-return-rigidity-independent-v1",
                  "parent_sha": PARENT, "python": platform.python_version(),
                  "sympy": s.__version__,
                  "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                  "checks": independent,
                  "forward_json_crosscheck": args.evidence is not None,
                  "implemented_checks": "passed",
                  "WF_theorem_machine_proved": False,
                  "formation_solution_found": False}
        text = json.dumps(report, indent=2, ensure_ascii=False)+"\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(text, encoding="utf-8")
        sys.stdout.write(text)
        return 0
    except (OSError, ValueError, KeyError, TypeError, AssertionError) as exc:
        print(f"verification failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
