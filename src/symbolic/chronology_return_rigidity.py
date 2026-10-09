#!/usr/bin/env python3
"""Exact finite checks accompanying the return-germ rigidity argument.

The microlocal/Poincare theorem is proved in the accompanying note, NOT by
these finite symbolic checks. No nonlinear SCEE or formation solution is claimed.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import platform
import sys
from typing import Any

import sympy as s

PARENT = "27e78fe8ab10566c2f54d787ba8e15e1ce0aa65a"


def matrix_strings(m: s.Matrix) -> list[list[str]]:
    return [[str(s.simplify(m[i, j])) for j in range(m.cols)] for i in range(m.rows)]


def hamiltonian_checks() -> dict[str, Any]:
    t, psi, x, z = s.symbols("t psi x z", real=True)
    pt, pp, px, pz = s.symbols("p_t p_psi p_x p_z", real=True)
    gamma = s.symbols("gamma", positive=True)
    F = s.Function("F")(t, x, psi)
    q = s.Matrix([t, psi, x, z])
    p = s.Matrix([pt, pp, px, pz])
    g = s.Matrix([[0, -1, 0, 0], [-1, F, 0, 0],
                  [0, 0, 1, 0], [0, 0, 0, 1]])
    H = (p.T * g.inv() * p)[0] / 2
    assert s.simplify(H + F * pt**2 / 2 + pt * pp - (px**2 + pz**2) / 2) == 0
    psi_dot = s.diff(H, pp)
    pt_dot = -s.diff(H, t)
    log_rate = s.simplify(pt_dot / (pt * psi_dot))
    assert log_rate == -s.diff(F, t) / 2
    assert s.simplify(log_rate.subs(F, -gamma*t).doit()) == gamma/2

    # Existing zero-boost crossing: F=-t^3; no new formation candidate.
    H3 = H.subs(F, -t**3)
    X = s.Matrix([s.diff(H3, a) for a in p] + [-s.diff(H3, a) for a in q])
    state = list(q) + list(p)
    orbit = {t: 0, x: 0, z: 0, pt: -1, pp: 0, px: 0, pz: 0}
    vector_at_orbit = X.subs(orbit)
    assert vector_at_orbit == s.Matrix([0, 1, 0, 0, 0, 0, 0, 0])
    A = X.jacobian(state).subs(orbit)
    # Tangent variations in x,p_x obey delta x'=delta p_x, delta p_x'=0.
    block = A.extract([2, 6], [2, 6])
    assert block == s.Matrix([[0, 1], [0, 0]])
    for row in [2, 6]:
        assert all(A[row, col] == 0 for col in range(8) if col not in [2, 6])
    ell = s.symbols("ell", positive=True)
    transfer = (ell * block).exp()
    assert transfer == s.Matrix([[1, ell], [0, 1]])
    J = s.Matrix([[0, 1], [-1, 0]])
    assert s.simplify(transfer.T * J * transfer - J) == s.zeros(2)
    # dpsi/dlambda=1 on the reference orbit and its linear screen variation
    # has no first-order timing correction. This block is a Poincare block.
    assert A[1, 2] == 0 and A[1, 6] == 0
    assert A[4, 2] == 0 and A[4, 6] == 0
    return {
        "general_H": str(H),
        "log_abs_p_t_per_psi": "-F_t/2",
        "affine_front_multiplier": "exp(gamma*ell/2)",
        "zero_boost_reference_H_flow": matrix_strings(vector_at_orbit),
        "zero_boost_multiplier": "1",
        "zero_boost_screen_generator": matrix_strings(block),
        "zero_boost_screen_return": matrix_strings(transfer),
        "screen_return_at_ell_1": matrix_strings(transfer.subs(ell, 1)),
        "screen_return_is_identity": False,
        "screen_return_is_symplectic": True,
        "meaning": "exact first-variation calculation, not a PDE existence proof",
    }


def refocusing_controls() -> dict[str, Any]:
    a, L = s.symbols("a L", positive=True)
    J = s.Matrix([[0, 1], [-1, 0]])
    transfer = s.Matrix([[s.cos(L/a), a*s.sin(L/a)],
                         [-s.sin(L/a)/a, s.cos(L/a)]])
    assert s.simplify(transfer.T * J * transfer - J) == s.zeros(2)
    round_return = s.simplify(transfer.subs(L, 2*s.pi*a))
    assert round_return == s.eye(2)

    # Purely canonical-map countercontrol: not claimed to be a constructed
    # Lorentzian metric. Identity of D(Pi) at one point is not identity of Pi.
    u, v = s.symbols("u v", real=True)
    Pi = s.Matrix([u, v+u**3])
    D = Pi.jacobian([u, v])
    assert s.simplify(D.T*J*D-J) == s.zeros(2)
    assert D.subs(u, 0) == s.eye(2)
    assert Pi[1] - v == u**3
    return {
        "ESU_screen_return": matrix_strings(round_return),
        "ESU_null_flow_period": "2*pi*a / E for null covector energy E>0",
        "ESU_WF_geometry_control": "passes necessary return-germ test",
        "first_jet_countercontrol": {
            "map": "(u,v)->(u,v+u^3)",
            "derivative_at_origin": matrix_strings(D.subs(u, 0)),
            "identity_germ": False,
            "spacetime_realization_claimed": False,
        },
    }


def spectral_counterexample() -> dict[str, Any]:
    # Same temporal ESU quotient, same null flow; change only a smooth
    # lower-order term to m^2*a^2=1/2. Temporal n and spatial j are integers.
    n, j = s.symbols("n j", integer=True)
    numerator = 2*n**2 - 2*j**2 - 1
    parity = s.Poly(numerator, n, j, modulus=2)
    assert parity == s.Poly(1, n, j, modulus=2)
    assert s.simplify((n**2-j**2).subs(n, j)) == 0
    return {
        "geometry": "(R/(2*pi*a)Z) x round S3_a",
        "field": "Box-R/6-m^2, ordinary periodic real scalar",
        "mass_squared_times_a_squared": "1/2",
        "eigenvalue_times_a_squared": "n^2-j^2-1/2",
        "twice_eigenvalue_mod_2": 1,
        "all_mode_gap_lower_bound": "1/2",
        "nonzero_periodic_distributional_KG_solution": False,
        "Hadamard_state": False,
        "massless_control_has_infinite_kernel": True,
        "proof_scope": "Fourier completeness plus odd integer numerator; not a finite mode truncation",
    }


def build_report() -> dict[str, Any]:
    return {
        "schema": "chronology-return-rigidity-v1",
        "parent_sha": PARENT,
        "python": platform.python_version(),
        "sympy": s.__version__,
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "checks": {
            "hamiltonian": hamiltonian_checks(),
            "refocusing": refocusing_controls(),
            "spectral": spectral_counterexample(),
        },
        "analytic_result": {
            "name": "local null-return germ rigidity and chronology-boundary obstruction",
            "dimension_minimum_for_chronology_corollary": 3,
            "requires_whole_ray_tube": True,
            "requires_local_Hadamard_WF_equality": True,
            "requires_PxW_smooth_on_tube_times_U": True,
            "uses_positivity": False,
            "uses_Einstein_equation": False,
            "uses_compact_generation": False,
            "germ_identity_sufficient_for_state": False,
            "WF_theorem_machine_proved": False,
        },
        "implemented_checks": "passed",
        "formation_solution_found": False,
        "universal_formation_no_go": False,
        "RSET_or_SCEE_solved_here": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Optional JSON evidence path")
    args = parser.parse_args()
    try:
        text = json.dumps(build_report(), indent=2, ensure_ascii=False) + "\n"
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(text, encoding="utf-8")
        sys.stdout.write(text)
        return 0
    except (OSError, AssertionError, ValueError) as exc:
        print(f"check failed: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
