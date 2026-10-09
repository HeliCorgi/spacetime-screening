#!/usr/bin/env python3
"""Finite-resource audit controls, not a relativistic universal compiler.

The four-mode system is the LINEAR conformal-time model of PR #40 R1.
Adding a diagnostic heat ledger does not construct nonlinear GR evolution.
All exact checks, including expected-failure controls, run without --output.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform

import mpmath as mp
import sympy as sp

PR_PARENT = "c074780bf48f6b9acda92a94c1b74b28f96f362c"
MATH_SOURCE = "fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb"


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def expected_failure(check, message: str) -> None:
    try:
        check()
    except (AssertionError, ValueError):
        return
    raise AssertionError("Negative control was accepted: " + message)


def parameters(w: F, mu: F, tau: F) -> None:
    if min(w, mu, tau) <= 0:
        raise ValueError("w, viscosity, and relaxation time must be positive")


def linear_model() -> dict:
    w, mu, tau, k, Q = sp.symbols("w mu tau k Q", positive=True)
    A = sp.Matrix([[0, Q/w, 0, k/w], [-2*Q, 0, -k, 0],
                   [0, k, 0, 0], [-mu*k/tau, 0, 0, -1/tau]])
    H = sp.diag(w, sp.Rational(1, 2), sp.Rational(1, 2), tau/mu)
    loss = sp.diag(0, 0, 0, -2/mu)
    require(sp.simplify(H*A + A.T*H - loss) == sp.zeros(4),
            "continuous wave-energy identity")
    # The wrong current sign fails without modifying any physical threshold.
    wrong = A.copy()
    wrong[1, 0] = 2*Q
    expected_failure(lambda: require(sp.simplify(H*wrong + wrong.T*H - loss)
                                     == sp.zeros(4), "wrong current"),
                     "Maxwell current with wrong sign")
    z = sp.Matrix(sp.symbols("v E B P"))
    qdot = sp.simplify((z.T*H*A*z)[0])
    require(sp.simplify(qdot + z[3]**2/mu) == 0, "heat compensation")
    expected_failure(lambda: require(qdot == 0, "missing heat"),
                     "calling wave energy total conserved energy")
    expected_failure(lambda: parameters(F(1), F(-1), F(1)), "negative viscosity")
    expected_failure(lambda: parameters(F(1), F(1), F(0)), "zero relaxation")
    return {"A": str(A), "H": str(H), "HA_plus_ATH": str(loss),
            "wave_energy_derivative": "-P^2/mu",
            "diagnostic_heat_derivative": "P^2/mu",
            "meaning": "quadratic conformal-mode ledger, not full matter slice energy"}


def fraction_matrix(M: sp.Matrix) -> list[list[F]]:
    return [[F(int(M[i, j].p), int(M[i, j].q)) for j in range(M.cols)]
            for i in range(M.rows)]


def matvec(M: list[list[F]], z: list[F]) -> list[F]:
    return [sum((a*b for a, b in zip(row, z)), F(0)) for row in M]


def wave_energy(z: list[F], w: F, mu: F, tau: F) -> F:
    v, E, B, P = z
    return w*v*v/2 + (E*E+B*B)/4 + tau*P*P/(2*mu)


def mp_fraction(x: F):
    return mp.mpf(x.numerator)/x.denominator


def midpoint_experiment() -> dict:
    w, mu, tau = F(1), F(1, 1000), F(1, 100)
    parameters(w, mu, tau)
    A = sp.Matrix([[0, 1, 0, 1], [-2, 0, -1, 0],
                   [0, 1, 0, 0], [-sp.Rational(1, 10), 0, 0, -100]])
    z0 = [F(0), F(1), F(0), F(0)]
    initial = wave_energy(z0, w, mu, tau)
    require(initial == F(1, 4), "initial modal energy")
    T = F(2)  # Deliberately not the earlier gate time pi/sqrt(3).
    rows = []
    with mp.workdps(80):
        Am = mp.matrix([[mp.mpf(str(A[i, j])) for j in range(4)] for i in range(4)])
        reference = mp.expm(mp_fraction(T)*Am)*mp.matrix([0, 1, 0, 0])
        errors = []
        for n in (32, 64, 128, 256):
            h = T/n
            hs = sp.Rational(h.numerator, h.denominator)
            R = fraction_matrix((sp.eye(4)-hs*A/2).inv()*(sp.eye(4)+hs*A/2))
            z = z0[:]
            heat = F(0)
            for _ in range(n):
                next_z = matvec(R, z)
                Pmid = (z[3]+next_z[3])/2
                heat_step = h*Pmid*Pmid/mu
                require(heat_step >= 0, "nonnegative heat")
                require(wave_energy(next_z, w, mu, tau)-wave_energy(z, w, mu, tau)
                        == -heat_step, "exact midpoint dissipative identity")
                heat += heat_step
                z = next_z
                require(wave_energy(z, w, mu, tau)+heat == initial,
                        "exact rational wave-plus-heat balance")
            require(heat > 0, "nontrivial viscous heat")
            error = max(abs(mp_fraction(z[i])-reference[i]) for i in range(4))
            errors.append(error)
            rows.append({"steps": n, "endpoint_max_error": mp.nstr(error, 18),
                         "heat": mp.nstr(mp_fraction(heat), 18),
                         "exact_balance_residual": "0", "every_step_checked": True})
        ratios = [errors[i]/errors[i+1] for i in range(len(errors)-1)]
        require(all(3 < r < 5 for r in ratios), "second-order convergence control")
        require(errors[-1] < mp.mpf("0.00003"), "predeclared linear endpoint tolerance")
        reference_out = [mp.nstr(x, 30) for x in reference]
        ratios_out = [mp.nstr(r, 12) for r in ratios]
    return {"parameters": {"w": "1", "mu": "1/1000", "tau": "1/100", "k": "1", "Q": "1"},
            "T": "2", "rows": rows, "error_ratios": ratios_out,
            "reference": reference_out,
            "scope": "exact discrete balance plus numerical linear convergence; no nonlinear PDE error bound"}


def causal_and_energy_conditions() -> dict:
    alpha = F(1, 10)
    cT2, cL2 = alpha, F(1, 3)+4*alpha/3
    require(cT2 == F(1, 10) and cL2 == F(7, 15) < 1,
            "equilibrium characteristic speeds")
    delta = F(1, 1000)
    pressure_ratio = (1+4*delta)/3
    require(pressure_ratio == F(251, 750) < 1, "type-I DEC sufficient bound")
    # The equilibrium stress is independent of transport coefficients.
    # Thus DEC alone cannot validate the characteristic cone.
    bad_alpha = F(2)
    bad_cL2 = F(1, 3)+4*bad_alpha/3
    expected_failure(lambda: require(bad_cL2 <= 1, "superluminal longitudinal mode"),
                     "DEC as a replacement for causality")
    nu, tau, z = sp.symbols("nu tau z", positive=True)
    lam = (-1+sp.sqrt(1-4*tau*nu*z))/(2*tau)
    require(sp.simplify(sp.limit(lam, tau, 0, dir="+")+nu*z) == 0,
            "telegraph slow-root diffusion limit")
    return {"cT_squared": str(cT2), "cL_squared": str(cL2),
            "DEC_pressure_ratio_bound": str(pressure_ratio),
            "DEC_counterexample_alpha": str(bad_alpha), "counterexample_cL_squared": str(bad_cL2),
            "telegraph_signal_speed_squared": "nu/tau",
            "singular_limit": "tau -> 0 at fixed nu makes the signal speed unbounded",
            "scope": "equilibrium cone and type-I algebra; not nonlinear tube invariance"}


def resource_and_precision_controls() -> dict:
    B, cost = F(1), F(1, 16)
    require(16*cost <= B < 17*cost, "fixed-budget count")
    expected_failure(lambda: require(17*cost <= B, "seventeenth gate"),
                     "positive-cost gate beyond budget")
    # Infinite repetitions are not excluded by a finite budget without a floor.
    for N in (1, 8, 32, 128):
        spent = sum((F(1, 2**j) for j in range(1, N+1)), F(0))
        require(spent == 1-F(1, 2**N) < 1, "summable-cost negative control")
    radius = F(1, 10**6)
    # Two otherwise identical radix words differing at digit n are separated
    # by 2*8^-n; the midpoint belongs to both allowed error balls.
    n = 1
    while F(2, 8**n) > 2*radius:
        n += 1
    gap = F(2, 8**n)
    require(gap/2 <= radius, "overlap of encoding-error balls")
    expected_failure(lambda: require(gap > 2*radius, "uniform radix margin"),
                     "fixed-error all-length direct radix coding")
    return {"budget": str(B), "cost_floor": str(cost), "maximum_count": 16,
            "summable_cost": "sum_(j=1)^N 2^-j = 1-2^-N < 1",
            "noise_radius": str(radius), "first_overlap_digit": n, "gap": str(gap),
            "scope": "conditional resource and encoding obstructions, not a no-go for every computation"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {"schema": "family376-finite-resource-v1", "pr_parent": PR_PARENT,
              "math_source": MATH_SOURCE, "python": platform.python_version(),
              "sympy": sp.__version__, "mpmath": mp.__version__,
              "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "checks": {"linear_energy": linear_model(), "midpoint": midpoint_experiment(),
                         "causality_DEC": causal_and_energy_conditions(),
                         "resources_precision": resource_and_precision_controls()},
              "status": "all implemented checks passed",
              "embedding_classification": "D",
              "not_proved": ["finite-time physical preparation", "nonlinear Einstein-matter gate",
                             "all-time robust universal compiler", "CTC or semiclassical solution"]}
    text = json.dumps(result, ensure_ascii=False, indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
