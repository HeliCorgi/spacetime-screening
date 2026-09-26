#!/usr/bin/env python3
"""SA v6: close the #25 two-input channel with an ordinary forward record path.

This is a scoped obstruction, not a universal chronology-protection theorem.
It composes:
  * the #25 KSR two-input inverse scattering law,
  * a common Gaussian free-field seed plus bit-antisymmetric coherent displacement,
  * a finite Ramsey receiver,
  * ordinary forward storage of the receiver bit, and
  * admissible copy / NOT local controllers at the future sender.

For a fixed operation-independent linear process, normalization of both closed
experiments forces the backward binary distinguishability d to vanish.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import platform

import mpmath as mp
import sympy as sp

BASE_SHA = "82274b96f69fd9c6fceb5166fdf07672429d650d"


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def exact_model() -> dict:
    lam, V, s, d, q = sp.symbols("lambda V s d q", real=True)
    # #25 two-port inverse scattering. Tc,Rc denote complex conjugates.
    T, R, Tc, Rc, g = sp.symbols("T R Tc Rc g", commutative=True)
    S = sp.Matrix([[T, Rc], [R, Tc]])
    inverse_target = sp.Matrix([Tc * g, -R * g])
    det = T * Tc - R * Rc
    inv_out = S * inverse_target
    require(sp.simplify(inv_out[0]-det*g) == 0 and sp.simplify(inv_out[1]) == 0, "KSR inverse target algebra")

    # Common Gaussian seed; bit b changes only the coherent mean +/-s.
    d_receiver = sp.exp(-2 * lam**2 * V) * sp.sin(2 * lam * s)
    # Binary receiver record r=0 means sigma_y=+1; r=1 means sigma_y=-1.
    K = sp.Matrix([
        [(1 + d) / 2, (1 - d) / 2],
        [(1 - d) / 2, (1 + d) / 2],
    ])
    require(all(sp.simplify(sum(K[r, b] for r in range(2)) - 1) == 0 for b in range(2)),
            "open do(b) columns not normalized")
    # Open-intervention total-variation distinguishability is |d|.
    diff = [sp.simplify(K[r, 0] - K[r, 1]) for r in range(2)]
    require(diff == [d, -d], "binary intervention difference")

    # Close the experiment: past record r is stored and carried forward.
    # The future lab is allowed to implement b=r (copy) or b=1-r (NOT).
    z_copy = sp.expand(sum(K[r, r] for r in range(2)))
    z_not = sp.expand(sum(K[r, 1-r] for r in range(2)))
    require(z_copy == 1 + d and z_not == 1 - d, "feedback normalization weights")
    require(sp.solve([z_copy - 1, z_not - 1], [d], dict=True) == [{d: 0}],
            "closed normalization did not force d=0")

    # A stochastic local choice q*copy + (1-q)*NOT must remain affine.
    z_mix = sp.expand(q * z_copy + (1-q) * z_not)
    require(sp.simplify(z_mix-(1 + (2*q - 1)*d)) == 0, "mixed local controller total")
    posterior_copy_if_renormalized = sp.simplify(q * z_copy / z_mix)
    require(sp.simplify(posterior_copy_if_renormalized - q) != 0,
            "operation-dependent renormalization did not retroselect controller")

    # Nearest input-independent binary kernel is d->0. Column TV correction = |d|/2.
    # We store the signed algebraic displacement; absolute value is stated in the note.
    correction_signed = sp.simplify((K[0, 0] - sp.Rational(1, 2)))
    require(correction_signed == d/2, "column correction")

    return {
        "ramsey_parameter": str(d_receiver),
        "open_kernel": [[str(sp.simplify(K[r, b])) for b in range(2)] for r in range(2)],
        "open_D_past": "Abs(d)",
        "feedback_totals": {"copy": str(z_copy), "not": str(z_not), "mixture": str(z_mix)},
        "closed_consistency_solution": {"d": "0"},
        "closed_probabilities": {
            "P_Y_do_0": {"+1": "1/2", "-1": "1/2"},
            "P_Y_do_1": {"+1": "1/2", "-1": "1/2"},
            "D_past": "0",
        },
        "minimum_column_TV_change_to_fixed_no_signal_kernel": "Abs(d)/2",
        "renormalized_copy_fraction": str(posterior_copy_if_renormalized),
        "KSR_inverse": {
            "input_A": "(-1)^b * conjugate(T) * g",
            "input_B": "(-1)^(b+1) * R * g",
            "output_1": "(-1)^b * g when |T|^2-|R|^2=1",
            "output_2": "0",
        },
    }


def q99_low_frequency() -> dict:
    with mp.workdps(80):
        q = mp.mpf("0.99")
        delta = mp.sqrt(1-q*q)
        rp, rm = 1+delta, 1-delta
        a = rm/rp
        T = (a + 1/a)/2
        R = (a - 1/a)/2
        C = T*T + R*R
        frac = R*R/C
        require(abs(T*T-R*R-1) < mp.mpf("1e-70"), "low-frequency pseudo-unitarity")
        return {
            "Q_over_M": "0.99",
            "T0": mp.nstr(T, 50),
            "R0": mp.nstr(R, 50),
            "two_input_energy_factor": mp.nstr(C, 50),
            "second_input_energy_fraction": mp.nstr(frac, 50),
            "interpretation": "#25 inverse-control cost, not a probability. The closed-loop C proof below does not depend on this number.",
        }


def numerical_control() -> dict:
    with mp.workdps(80):
        lam = mp.mpf(1)
        V = mp.mpf("0.5")
        s = mp.mpf("0.2")
        d = mp.exp(-2*lam*lam*V) * mp.sin(2*lam*s)
        p0 = [(1+d)/2, (1-d)/2]
        p1 = [(1-d)/2, (1+d)/2]
        tv = mp.mpf("0.5") * sum(abs(a-b) for a,b in zip(p0,p1))
        require(abs(tv-abs(d)) < mp.mpf("1e-70"), "TV control")
        zc, zn = 1+d, 1-d
        return {
            "ONLY_A_CONTROL_EXAMPLE_not_SA_data": True,
            "lambda": "1", "V": "0.5", "s": "0.2",
            "d": mp.nstr(d, 50),
            "P0": [mp.nstr(x, 50) for x in p0],
            "P1": [mp.nstr(x, 50) for x in p1],
            "D": mp.nstr(tv, 50),
            "Z_copy": mp.nstr(zc, 50),
            "Z_NOT": mp.nstr(zn, 50),
            "normalization_defect_magnitude": mp.nstr(abs(d), 50),
        }


def candidate_record() -> dict:
    return {
        "candidate_id": "sa-two-input-closed-operational-v6",
        "status": "C",
        "dimension": 4,
        "geometry": "Prescribed Schein-Aichelburg same-exterior handle; #25 propagation uses the 4D RN inter-horizon block and fixed shell/time identifications.",
        "matter_content": "Neutral real massless minimally-coupled scalar signal field; classical Maxwell/shell background; finite Ramsey qubit; ordinary classical memory from receiver to sender.",
        "quantum_state": "A single operation-independent centered Gaussian seed with finite receiver variance V_eff, displaced coherently by the two-input sign-controlled signal. The C result is independent of the numerical value of V_eff.",
        "sender_intervention": "External do(b) controls the sign of both #25 inverse-scattering inputs: F_A=(-1)^b conjugate(T) g and F_B=-(-1)^b R g. For the closure test the same future lab may alternatively apply copy or NOT to the stored earlier receiver bit.",
        "scattering": "[G1,G2]^T=[[T,R*],[R,T*]][F_A,F_B]^T; |T|^2-|R|^2=1; target G1=(-1)^b g,G2=0.",
        "receiver": "Finite proper-time Ramsey qubit, initially |+x>, U=exp[-i lambda sigma_z Phi(F)], measured in sigma_y with all outcomes kept.",
        "measurement": "Y in {+1,-1}; r=(1-Y)/2 is stored and transported ordinarily forward to the future sender.",
        "P_Y_do_0": {"+1": "1/2", "-1": "1/2"},
        "P_Y_do_1": {"+1": "1/2", "-1": "1/2"},
        "distinguishability": {"metric": "total_variation", "value": 0, "computed": True},
        "obstruction": "Before operational closure the Ramsey law has d=exp(-2 lambda^2 V_eff) sin(2 lambda s_F) and D=|d|. Closing the same fixed linear channel with ordinary forward memory gives total weights 1+d (copy) and 1-d (NOT). Normalization for both admissible local operations forces d=0. Per-operation renormalization is future-operation-dependent postselection and violates the intervention criterion.",
        "quantification": {
            "if_open_model_claims_D": "normalization defect of copy and NOT is exactly D in opposite directions",
            "minimum_max_column_TV_change_to_operation_independent_no_signal_kernel": "D/2",
            "operation_mixture": "Z(q)=1+(2q-1)d; renormalization changes the chosen copy probability to q(1+d)/Z(q)",
        },
        "scope": "C for #25 when embedded in one operation-independent linear quantum/process model that permits ordinary forward record transport and standard local CPTP copy/NOT controllers. Does not rule out theories with operation-dependent global boundary conditions, nonlinear/postselected final-state rules, or restricted local operations; those are different B candidates and fail the current protocol assumptions unless independently derived.",
        "literature": [
            {"title": "Traversable Wormholes in Geometries of Charged Shells", "authors": "F. Schein; P. C. Aichelburg", "year": 1996, "url": "https://arxiv.org/abs/gr-qc/9606069"},
            {"title": "A scattering theory for linear waves on the interior of Reissner-Nordstrom black holes", "authors": "C. Kehle; Y. Shlapentokh-Rothman", "year": 2019, "url": "https://arxiv.org/abs/1804.05438"},
            {"title": "Quantum correlations with no causal order", "authors": "O. Oreshkov; F. Costa; C. Brukner", "year": 2012, "url": "https://arxiv.org/abs/1105.4464"},
            {"title": "Channel capacity of relativistic quantum communication with rapid interaction", "authors": "E. Tjoa; K. Gallock-Yoshimura", "year": 2022, "url": "https://arxiv.org/abs/2202.12301"},
        ],
        "verification": {"computational": "forward exact algebra plus independent process-matrix verifier required", "human_review_for_A": True},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {
        "base_sha": BASE_SHA,
        "environment": {"python": platform.python_version(), "sympy": sp.__version__, "mpmath": mp.__version__},
        "exact": exact_model(),
        "q99_low_frequency": q99_low_frequency(),
        "numerical_control": numerical_control(),
        "classification": {"A": 0, "B": 0, "C": 1},
        "candidate": candidate_record(),
        "code_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"passed": True, "classification": result["classification"], "closed_D_past": 0,
                      "second_input_energy_fraction_q99": result["q99_low_frequency"]["second_input_energy_fraction"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
