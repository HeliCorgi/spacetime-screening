#!/usr/bin/env python3
"""v8: stress-tensor route audit and Deutsch-from-standard-QFT no-go diagnostic.

This script does not claim a universal no-go for quantum gravity.
It quantifies:
  * the scale matching required for a one-scale 4D vacuum RSET to support a
    zero-tidal wormhole throat;
  * the finite positive signal-mode energy of the v7 Deutsch toy;
  * an exact convex-linearity failure of the Deutsch fixed-point selector,
    showing that it cannot equal any operation-independent linear quantum
    supermap on the same pair of local operations.
"""
from __future__ import annotations
import argparse, json, math, platform, hashlib
from pathlib import Path
import sympy as sp
import mpmath as mp

BASE_SHA = "6a408e42abef6355699d276c1bc45547198954ae"

def require(ok, msg):
    if not ok:
        raise AssertionError(msg)

def exact_deutsch_nonaffinity():
    a = sp.Rational(1,2)
    c = sp.pi/8
    q = sp.Rational(1,2)
    vvac = sp.Rational(1,2)
    # Deterministic x -> a x +/- c plus vacuum loss noise.
    noise = (1-a**2)*vvac
    mu = sp.simplify(c/(1-a))
    # Each deterministic fixed point retains vacuum X variance.
    v_det = vvac
    # Affine mixture of the two selected Deutsch fixed-point states.
    v_affine = sp.simplify(v_det + 4*q*(1-q)*mu**2)
    # Fixed point after first mixing the two local operations into one CPTP map.
    # Random displacement variance per loop = 4q(1-q)c^2.
    v_channel_mixed = sp.simplify((noise + 4*q*(1-q)*c**2)/(1-a**2))
    gap = sp.simplify(v_affine-v_channel_mixed)
    require(mu == sp.pi/4, "v7 mean changed")
    require(v_affine == sp.Rational(1,2)+sp.pi**2/16, "affine mixture variance")
    require(v_channel_mixed == sp.Rational(1,2)+sp.pi**2/48, "mixed channel fixed variance")
    require(gap == sp.pi**2/24 and gap > 0, "Deutsch selector should be non-affine")

    # General symbolic gap, useful for scope.
    aa, cc, qq = sp.symbols("a c q", positive=True)
    gen_gap = sp.factor(
        4*qq*(1-qq)*cc**2 *
        (1/(1-aa)**2 - 1/(1-aa**2))
    )
    require(sp.simplify(gen_gap - 8*aa*qq*(1-qq)*cc**2/((1-aa)**2*(1+aa))) == 0,
            "general non-affinity gap")

    return {
        "a":"1/2","c":"pi/8","q":"1/2",
        "deterministic_fixed_mean_abs":"pi/4",
        "fixed_selector_affine_mixture_variance":"1/2+pi^2/16",
        "fixed_point_of_mixed_channel_variance":"1/2+pi^2/48",
        "nonaffinity_variance_gap":"pi^2/24",
        "numeric_gap":float(sp.N(gap,20)),
        "general_gap":"8*a*q*(1-q)*c^2/((1-a)^2*(1+a))",
        "interpretation":"Deutsch fixed-point selection is not affine in the inserted operation. A fixed-state, operation-independent standard quantum supermap is affine, so it cannot reproduce this selector for all local operations."
    }

def stress_scale():
    G=mp.mpf("6.67430e-11")
    c=mp.mpf("299792458")
    hb=mp.mpf("1.054571817e-34")
    lp=mp.sqrt(hb*G/c**3)
    b=mp.mpf(1)
    # Zero-tidal b(r)=b0 throat: tau_required = c^4/(8 pi G b0^2).
    # A one-scale vacuum RSET from N species: tau_quantum = N*C*hbar*c/b0^4.
    # Match -> N*C = b0^2/(8 pi lp^2).
    nc = b*b/(8*mp.pi*lp**2)
    rows=[]
    for cdim in ["1","0.01","0.001","0.0001"]:
        C=mp.mpf(cdim)
        rows.append({"dimensionless_RSET_coefficient_C":cdim,
                     "required_species_N_at_1m":mp.nstr(nc/C,14)})
    # v7 selected oscillator mode energy in units hbar*omega.
    E = sp.simplify(sp.Rational(1,2)*(sp.Rational(1,2)+sp.Rational(5,6)+sp.pi**2/16))
    Eex=sp.simplify(E-sp.Rational(1,2))
    return {
        "planck_length_m":mp.nstr(lp,16),
        "zero_tidal_1m_required_product_N_times_C":mp.nstr(nc,16),
        "examples":rows,
        "v7_loop_mode_energy_over_hbar_omega":str(E),
        "v7_loop_mode_excess_over_vacuum":str(Eex),
        "v7_signal_support_comment":"For a minimally coupled coherent scalar displacement, the classical null contraction is (k.grad phi)^2 >= 0; the signal mode is not itself the exotic throat support."
    }

def candidates():
    return [
      {
        "id":"mmp-4d-fermion-casimir",
        "status":"B",
        "stress_status":"strongest explicit semiclassical support candidate",
        "facts":"4D Einstein-Maxwell plus charged massless fermions; negative Casimir-like null stress is inserted into Einstein equations and the throat solution is solved.",
        "blocker":"The published solution is deliberately a long wormhole satisfying the ambient causality bound; changing it into a time machine requires a new dynamical self-consistent solution."
      },
      {
        "id":"jiang-jiang-zero-tidal-rset-2026",
        "status":"B",
        "stress_status":"exact renormalized throat RSET on a prescribed geometry",
        "facts":"Hadamard/pragmatic mode-sum RSET has three (m b0, xi) regions satisfying Morris-Thorne throat conditions.",
        "blocker":"The geometry is prescribed and the paper tests throat conditions; it does not solve the full coupled semiclassical Einstein equation. For a single-scale 1m throat, matching requires N*C=1.523e68."
      },
      {
        "id":"popov-long-throat",
        "status":"B",
        "stress_status":"self-consistent semiclassical long-throat solution in a local/WKB regime",
        "facts":"Vacuum polarization of a nonconformal scalar is used in semiclassical Einstein equations to obtain a long throat.",
        "blocker":"Long-throat/local approximation and macroscopic scale require a large dimensionless parameter; no complete asymptotically-flat time-machine construction or CTC quantum state is supplied."
      },
      {
        "id":"kain-qft-edm",
        "status":"B",
        "stress_status":"static semiclassical QFT wormhole configurations",
        "facts":"Quantized Einstein-Dirac-Maxwell static spherically symmetric wormholes are constructed in semiclassical QFT.",
        "blocker":"Dynamical traversability/stability of the quantum configurations is not established; related EDM evolutions studied by Kain form black holes and trap signals."
      },
      {
        "id":"mehulic-prokopec-2026",
        "status":"B",
        "stress_status":"explicit one-loop RSET/backreaction correction",
        "facts":"Massive minimally coupled scalar one-loop RSET is renormalized and backreaction solved to linear order in hbar.",
        "blocker":"The wormhole is still supported classically by anisotropic matter/negative mouth shells; the paper explicitly leaves fully self-consistent semiclassical solving for future work."
      },
      {
        "id":"deutsch-from-standard-qft",
        "status":"C",
        "stress_status":"not a stress-source candidate",
        "facts":"A fixed initial state plus ordinary linear quantum evolution defines an affine higher-order map of any inserted local CP operation.",
        "blocker":"The explicit v7 Gaussian Deutsch selector is non-affine: at q=1/2 the variance gap is pi^2/24. Thus the exact Deutsch selection law cannot be derived from an operation-independent standard linear QFT process on a fixed background. A nonlinear/operation-dependent boundary law or new quantum-gravity rule is required."
      }
    ]

def record():
    return {
      "batch_id":"stress-deutsch-qft-v8",
      "base_sha":BASE_SHA,
      "classification":{"A":0,"B":5,"C":1},
      "central_result":"Stress-tensor candidates survive as conditional components, but the exact Deutsch operation-dependent fixed-point selector cannot be obtained from an operation-independent standard linear 3+1D QFT supermap. No A completion.",
      "stress_scale":stress_scale(),
      "deutsch_nonaffinity":exact_deutsch_nonaffinity(),
      "candidates":candidates(),
      "next_single_problem":"If one insists on the Deutsch escape, derive a genuinely nonlinear/operation-dependent state-selection law from a specified quantum-gravity boundary functional (not ordinary fixed-state QFT) and compute its renormalized 4D stress tensor. Standard 3+1D QFT is closed by the non-affinity obstruction."
    }

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output",type=Path)
    a=p.parse_args()
    data=record()
    data["environment"]={"python":platform.python_version(),"sympy":sp.__version__,"mpmath":mp.__version__}
    data["code_sha256"]=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({
      "passed":True,
      "classification":data["classification"],
      "N_times_C_1m":data["stress_scale"]["zero_tidal_1m_required_product_N_times_C"],
      "Deutsch_nonaffinity_gap":data["deutsch_nonaffinity"]["numeric_gap"]
    },ensure_ascii=False))
if __name__=="__main__":
    main()
