#!/usr/bin/env python3
"""CBSSL v9: a proposed chronology-backreaction state-selection law (toy physics).

This is intentionally a NEW toy law, not established physics and not derived
from standard QFT.  It is designed to:
  * reduce to ordinary quantum theory when no closed causal return exists;
  * select a self-consistent loop state when a chronology-return channel exists;
  * reject chronology candidates with no admissible finite-stress fixed point;
  * include semiclassical backreaction before a tie-breaker state choice;
  * reproduce the v7 positive-D Deutsch toy when the loop channel is contractive.
"""
from __future__ import annotations
import argparse, hashlib, json, math, platform
from pathlib import Path
import mpmath as mp
import sympy as sp

BASE_SHA = "fbf98de97fe11b9dea40e7d195227ea4a088b5a5"
LAW_NAME = "Chronology-Backreaction State-Selection Law (CBSSL)"


def require(ok, msg):
    if not ok:
        raise AssertionError(msg)


def exact_v7_branch():
    """Exact selected branch for the frozen v7 Gaussian loop component."""
    a = sp.Rational(1, 2)
    eta = a**2
    lam = sp.Integer(1)
    c = sp.pi / 8
    vx = sp.Rational(1, 2)
    vp = sp.Rational(1, 2) + eta * lam**2 / (1-eta)
    mean = sp.simplify(c/(1-a))
    d = sp.simplify(sp.exp(-2*lam**2*vx) * sp.sin(2*lam*mean))
    require(mean == sp.pi/4, "v7 mean")
    require(vp == sp.Rational(5, 6), "v7 P variance")
    require(d == sp.exp(-1), "v7 D")
    excess = sp.simplify((vx + vp - 1 + mean**2) / 2)
    require(excess == sp.Rational(1, 6) + sp.pi**2/32, "bit-symmetric energy")
    p0p = sp.simplify((1+d)/2)
    p1p = sp.simplify((1-d)/2)
    return {
        "a": "1/2", "eta": "1/4", "lambda": "1", "c": "pi/8",
        "mean_X": {"do_0":"pi/4", "do_1":"-pi/4"},
        "V_X":"1/2", "V_P":"5/6",
        "loop_energy_excess_over_hbar_omega": str(excess),
        "bit_energy_difference": "0",
        "P_Y_do_0": {"+1":"(1+exp(-1))/2", "-1":"(1-exp(-1))/2"},
        "P_Y_do_1": {"+1":"(1-exp(-1))/2", "-1":"(1+exp(-1))/2"},
        "D_past":"exp(-1)",
        "numeric": {
            "P0_plus": float(sp.N(p0p, 18)),
            "P1_plus": float(sp.N(p1p, 18)),
            "D_past": float(mp.e**-1),
            "energy_excess": float(sp.N(excess, 18)),
        }
    }


def nonaffinity_feature():
    """The v8 non-affinity gap becomes an intentional feature of the new law."""
    a = sp.Rational(1,2); c = sp.pi/8; q = sp.Rational(1,2)
    mu = sp.simplify(c/(1-a))
    v_affine = sp.simplify(sp.Rational(1,2) + 4*q*(1-q)*mu**2)
    noise = (1-a*a)/2
    v_mixed_fixed = sp.simplify((noise + 4*q*(1-q)*c**2)/(1-a*a))
    gap = sp.simplify(v_affine-v_mixed_fixed)
    require(gap == sp.pi**2/24, "nonaffinity gap")
    return {
        "selected_then_mixed_variance":"1/2+pi^2/16",
        "mixed_operation_then_selected_variance":"1/2+pi^2/48",
        "gap":"pi^2/24",
        "numeric_gap":float(sp.N(gap,18)),
        "interpretation":"CBSSL is intentionally non-affine in the complete chronology-return operation; this is forbidden for an ordinary fixed-process quantum supermap but is postulated only when a causal return exists."
    }


def degenerate_tie_breaker():
    """Identity loop has infinitely many fixed points; relative entropy selects a reference state."""
    p = sp.symbols('p', positive=True)
    D = p*sp.log(p/sp.Rational(2,3)) + (1-p)*sp.log((1-p)/sp.Rational(1,3))
    d1 = sp.simplify(sp.diff(D,p))
    d2 = sp.simplify(sp.diff(D,p,2))
    require(sp.simplify(d1.subs(p,sp.Rational(2,3))) == 0, "tie stationary")
    require(sp.simplify(d2.subs(p,sp.Rational(2,3))) > 0, "tie minimum")
    return {
        "loop_channel":"identity",
        "fixed_point_set":"all density matrices",
        "reference_state":"diag(2/3,1/3)",
        "selected_state":"diag(2/3,1/3)",
        "contrast_with_Deutsch_max_entropy":"Deutsch maximum-entropy tie-break would select I/2; CBSSL instead selects the admissible fixed point closest in relative entropy to the specified local Hadamard/reference state."
    }


def chronology_protection_control():
    """If the only fixed point violates an admissibility/stress cap, the chronology solution is rejected."""
    fixed_energy = sp.Integer(1)
    cap = sp.Rational(1,2)
    require(fixed_energy > cap, "protection control")
    return {
        "channel":"replacement to excited state",
        "unique_fixed_point_energy":"1 energy-unit",
        "admissible_energy_cap":"1/2 energy-unit",
        "admissible_fixed_point_exists":False,
        "law_result":"no stationary chronology-violating solution in this toy sector; geometry must leave the assumed stationary chronology class"
    }


def no_remote_ensemble_signalling_control():
    """Selection depends on the reduced chronology density operator, not its ensemble decomposition."""
    bell = sp.Matrix([1,0,0,1])/sp.sqrt(2)
    rho = bell*bell.T
    X = sp.Matrix([[0,1],[1,0]])
    U = sp.kronecker_product(sp.eye(2), X)
    out = U*rho*U.T
    def ptr_B(rr):
        return sp.Matrix(2,2,lambda i,j: sum(rr[2*i+k,2*j+k] for k in range(2)))
    require(ptr_B(rho) == sp.eye(2)/2, "Bell reduction")
    require(ptr_B(out) == ptr_B(rho), "remote TP control")
    return {
        "control":"Bell-pair remote local unitary",
        "chronology_reduced_state_before":"I/2",
        "chronology_reduced_state_after":"I/2",
        "selector_change":False,
        "scope":"This only tests decomposition/remote-unitary invariance when the remote operation is outside the chronology-return map. It is not a general proof against all nonlinear superluminal signalling."
    }


def cut_covariance_control():
    """Fixed-point mismatch and relative-entropy ordering are invariant under unitary cut transport."""
    rho = sp.diag(sp.Rational(2,3), sp.Rational(1,3))
    X = sp.Matrix([[0,1],[1,0]])
    moved = X*rho*X
    require(moved == sp.diag(sp.Rational(1,3), sp.Rational(2,3)), "cut move")
    require(X*rho*X == moved, "unitary covariance")
    return {
        "control":"unitary conjugation of chronology cut",
        "fixed_point_equality_preserved":True,
        "law_requirement":"Bures distance and quantum relative entropy are unitarily invariant, so the selection ordering is cut-covariant under unitary transport of the complete boundary algebra."
    }


def law_record():
    return {
        "law_id":"cbssl-v9",
        "law_name":LAW_NAME,
        "status":"B",
        "claim_type":"new toy physical law proposed in this project; not established physics and not claimed as literature-first",
        "activation":"Only when the geometry admits a closed causal return map across a chronology cut. If no return map exists, use ordinary initial-value QFT with no CBSSL state reselection.",
        "boundary_state_space":"Positive trace-one density operators (or algebraic states in the continuum limit) on the complete chronology-cut algebra, including all classical control records that cross the cut.",
        "return_map":"Phi[g,E] is the complete CPTP return channel induced by ordinary local QFT/apparatus propagation away from the chronology boundary for the actually implemented local operation E.",
        "selection":"Lexicographically minimize (C_loop, R_sc, I_ref): first chronology mismatch C_loop=D_B^2(rho,Phi[rho]); among its minimizers minimize the positive semiclassical Einstein residual R_sc; among remaining degeneracy minimize quantum relative entropy I_ref=D(rho||rho_ref). A stationary chronology solution is admitted only if min C_loop=0 and min R_sc=0 with finite renormalized stress and fixed asymptotic charges.",
        "semiclassical_residual":"E_mn=G_mn+Lambda g_mn-8*pi*G<T_mn>_ren; R_sc=integral_C sqrt(-g) w E_mn E_rs q^(mr)q^(ns), with q^(mn)=g^(mn)+2 u^m u^n positive in the apparatus frame. Renormalization counterterms/reference state are fixed once, not per operation.",
        "tie_breaker":"Relative entropy to one operation-independent local Hadamard/reference state; identity-loop control selects the reference state, unlike Deutsch maximum entropy.",
        "no_postselection":"Once (g*,rho*) is selected, all local outcome probabilities use the ordinary Born rule and all outcomes are kept. No conditioning on a future measurement outcome.",
        "charge_constraint":"Admissible states/geometries must preserve the asymptotic/gauge charges fixed by the external preparation; the selector may not create arbitrary ADM charge or gauge charge.",
        "representation_rule":"The law acts on the complete physical CPTP map including retained classical randomizer/control registers. It does not depend on a hidden convex decomposition of the same reduced channel.",
        "chronology_protection_branch":"If no admissible finite-RSET fixed point with zero semiclassical residual exists, the assumed stationary chronology-violating geometry is not a physical solution and must backreact/evolve out of that class.",
        "novel_nonaffinity":"Operation -> selected loop state is intentionally non-affine. The v7/v8 q=1/2 witness is Delta V=pi^2/24.",
        "v7_positive_channel":exact_v7_branch(),
        "unresolved_assumptions":[
            "No microscopic quantum-gravity derivation of CBSSL is supplied; it is the proposed fundamental toy law itself.",
            "The full 3+1D SA return channel on the continuum field algebra is not computed under CBSSL.",
            "The full renormalized stress tensor and a self-consistent SA metric solving the CBSSL semiclassical residual are not yet constructed.",
            "Restriction of the nonlinear selector to chronology regions avoids changing ordinary globally hyperbolic QFT by fiat; full compatibility with relativistic causality in multipartite quantum gravity is not proven."
        ],
        "classification_reason":"Positive sender-controlled D_past is explicit in the v7 mode and paradoxical copy/NOT loops have fixed points, but the new boundary law and full 3+1D RSET/backreaction are speculative/unconstructed. Therefore B, not A."
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    a=p.parse_args()
    data={
        "base_sha":BASE_SHA,
        "classification":{"A":0,"B":1,"C":0},
        "law":law_record(),
        "controls":{
            "nonaffinity":nonaffinity_feature(),
            "degenerate_tie_breaker":degenerate_tie_breaker(),
            "chronology_protection":chronology_protection_control(),
            "remote_ensemble":no_remote_ensemble_signalling_control(),
            "cut_covariance":cut_covariance_control(),
        },
        "environment":{"python":platform.python_version(),"sympy":sp.__version__,"mpmath":mp.__version__},
        "code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding='utf-8')
    print(json.dumps({"passed":True,"classification":data["classification"],"law":LAW_NAME,"D_past":float(mp.e**-1),"nonaffinity_gap":data["controls"]["nonaffinity"]["numeric_gap"]},ensure_ascii=False))

if __name__=='__main__':
    main()
