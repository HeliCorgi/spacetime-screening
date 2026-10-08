#!/usr/bin/env python3
"""Eternal ESU time-quotient control: thermal state and mean SCEE algebra.

This is NOT formation from causal initial data.  State positivity, Hadamard
regularity and descent are analytic arguments in the note, not sample tests.
Renormalization: the standard conformal-scalar ESU Casimir prescription;
matched renormalized curvature-squared gravitational coefficients are zero.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import platform
from pathlib import Path
import mpmath as mp
import sympy as sp

PARENT="c6e6cda08ad73e457d135bcb9652a2355add9a9b"


def exact_checks() -> dict:
    a,G,Lam,S=sp.symbols("a G Lambda S",positive=True)
    rho=S/(2*sp.pi**2*a**4)
    a2=sp.Rational(3,2)/Lam
    required=9*sp.pi/(16*G*Lam)
    Et=3/a**2-Lam-8*sp.pi*G*rho
    Es=-1/a**2+Lam-8*sp.pi*G*rho/3
    sub={a**2:a2,S:required}
    assert sp.simplify(Et.subs(sub)) == 0
    assert sp.simplify(Es.subs(sub)) == 0
    # Invariants of R x S3: trace anomaly vanishes for a massless conformal scalar.
    R=6/a**2; Ric2=12/a**4; Riem2=12/a**4
    assert sp.simplify(Riem2-2*Ric2+R**2/3) == 0
    assert sp.simplify(Riem2-4*Ric2+R**2) == 0
    s,chi=sp.symbols("s chi",real=True)
    W=1/(8*sp.pi**2*a*a*(sp.cos(s)-sp.cos(chi)))
    assert sp.trigsimp(W.subs(s,s+2*sp.pi)-W) == 0
    # For r != 0, radial conformal KG operator on the ESU.
    op=-sp.diff(W,s,2)+sp.diff(W,chi,2)+2*sp.cot(chi)*sp.diff(W,chi)-W
    assert sp.trigsimp(op) == 0
    # Incorrect periods need not descend even for the lowest frequency.
    assert sp.exp(-sp.I*sp.pi) != 1
    # Lambda=0 cannot balance the two static radiation equations.
    assert sp.simplify((-Et+3*Es).subs(Lam,0)) == -6/a**2
    trace_requirement=sp.simplify(-Et+3*Es)
    assert trace_requirement == 4*Lam-6/a**2
    return {"fixed_couplings":"G=1, Lambda=1/100000000; curvature-squared coefficients=0 in stated prescription",
            "a_squared":"3/(2*Lambda)","S_required":"9*pi/(16*G*Lambda)",
            "temporal_period":"2*pi*a","inverse_temperature":"beta=a*b, b independent of real-time period",
            "vacuum_S":"1/240","rho":"S/(2*pi^2*a^4)","pressure":"rho/3",
            "Einstein_residuals":["0","0"],"trace_anomaly_invariants":"C^2=Euler=Box R=0",
            "KG_off_singularities":"0", "vacuum_two_point_periodicity":"exact",
            "Lambda_zero_control":"no static solution with finite a and this source",
            "period_pi_a_control":"lowest positive-frequency mode does not descend"}


def positive_thermal_sum_interval(b: str, terms: int=8000):
    """Directed arbitrary-precision interval sum, plus a positive analytic tail."""
    iv=mp.iv
    bI=iv.mpf(b)
    q=iv.exp(-bI)
    power=q
    total=iv.mpf(1)/240
    for j in range(1,terms+1):
        total += j**3*power/(1-power)
        power *= q
    m=terms+1
    # sum_{j=m}^infty j^3 q^j, divided by 1-q^m.
    geometric=(m**3/(1-q)+3*m*m*q/(1-q)**2
               +3*m*q*(1+q)/(1-q)**3+q*(1+4*q+q*q)/(1-q)**4)
    tail=power*geometric/(1-power)
    return total,tail


def lo(x):
    return mp.mpf(x._mpi_[0])


def hi(x):
    return mp.mpf(x._mpi_[1])


def thermal_certificate() -> dict:
    with mp.workdps(80):
        mp.iv.dps=60
        Lam=mp.mpf(1)/10**8
        a=mp.sqrt(3/(2*Lam))
        target=9*mp.pi/(16*Lam)
        # A bracket seed only.  The finite sums + tails below certify it;
        # a high-temperature asymptotic is NOT used as the final equation.
        seed=(mp.pi**4/(15*target))**mp.mpf('0.25')
        blo=mp.nstr(seed-mp.mpf('1e-24'),40)
        bhi=mp.nstr(seed+mp.mpf('1e-24'),40)
        Sl,Tl=positive_thermal_sum_interval(blo)
        Sh,Th=positive_thermal_sum_interval(bhi)
        targetI=9*mp.iv.pi*10**8/16
        assert lo(Sl) > hi(targetI)
        assert hi(Sh+Th) < lo(targetI)
        assert max(hi(Tl),hi(Th)) < mp.mpf('1e-30')
        # Independent rearrangement: sum over occupation multiplicity first.
        q=mp.exp(-seed); qp=q; alternative=mp.mpf(1)/240
        for m in range(1,8001):
            alternative += qp*(1+4*qp+qp*qp)/(1-qp)**4
            qp*=q
        alt_tail=qp*(1+4*qp+qp*qp)/(1-qp)**4/(1-q)
        Sd,Td=positive_thermal_sum_interval(mp.nstr(seed,75))
        assert lo(Sd)-alt_tail-mp.mpf('1e-55') <= alternative <= hi(Sd+Td)+mp.mpf('1e-55')
        rho=Lam/(8*mp.pi)
        beta=a*seed
        energy=2*mp.pi**2*a**3*rho
        return {"terms_each_sum":8000,"interval_dps":60,"G":"1","Lambda":"1/100000000",
                "b_lower":blo,"b_upper":bhi,
                "S_required":mp.nstr(target,40),
                "low_endpoint_positive_margin":mp.nstr(lo(Sl)-hi(targetI),12),
                "high_endpoint_negative_margin":mp.nstr(lo(targetI)-hi(Sh+Th),12),
                "series_tail_upper":mp.nstr(max(hi(Tl),hi(Th)),14),
                "independent_Lambert_sum_difference":mp.nstr(abs(alternative-target),14),
                "a":mp.nstr(a,30),"beta_approx":mp.nstr(beta,30),
                "rho":mp.nstr(rho,30),"slice_energy":mp.nstr(energy,30),
                "real_time_period_approx":mp.nstr(2*mp.pi*a,30),
                "meaning":"monotonic exact spectral sum has one root in this b bracket"}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    data={"schema":"chronology-esu-control-v1","parent_sha":PARENT,
          "python":platform.python_version(),"sympy":sp.__version__,"mpmath":mp.__version__,
          "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          "exact":exact_checks(),"thermal_root":thermal_certificate(),
          "implemented_checks":"passed","eternal_mean_field_control":True,
          "causal_initial_state":False,"formation_solution_found":False,
          "not_certified":["physical preparation", "nonlinear stability",
                           "small stress fluctuations", "all-loop quantum gravity"]}
    text=json.dumps(data,indent=2,ensure_ascii=False)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding="utf-8")
    print(text,end="")

if __name__ == "__main__":
    main()
