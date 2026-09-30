#!/usr/bin/env python3
"""Independent verifier for CBSSL v14 local UV-opaque mouth audit."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import platform
from pathlib import Path

import mpmath as mp

BASE_SHA = "7f7fbec0b56c9592459e79b0c84a8be4ced8950c"
ADVANCE = mp.mpf("0.75")


def req(ok, message):
    if not ok:
        raise AssertionError(message)


def t_stage(u):
    return 2j*u/(u+1j)**2


def scattering_control():
    with mp.workdps(60):
        rows = []
        for u_s in ("0.1","0.5","1","2","10"):
            u = mp.mpf(u_s)
            t = t_stage(u)
            r = t-1
            flux = abs(t)**2+abs(r)**2
            req(abs(flux-1) < mp.mpf("1e-50"), "flux")
            rows.append({
                "u":u_s,
                "|t|^2":mp.nstr(abs(t)**2,30),
                "|r|^2":mp.nstr(abs(r)**2,30),
                "sum":mp.nstr(flux,20),
            })
        req(abs(t_stage(mp.mpf(1))-1) < mp.mpf("1e-50"), "u=1 resonance")
        return {
            "rows":rows,
            "UV_check_u_abs_t_at_1e5": mp.nstr(mp.mpf("1e5")*abs(t_stage(mp.mpf("1e5"))),30),
            "IR_check_abs_t_over_u_at_1e-8": mp.nstr(abs(t_stage(mp.mpf("1e-8")))/mp.mpf("1e-8"),30),
        }


def integrability_control():
    with mp.workdps(70):
        i0 = mp.quad(lambda u:(2*u/(1+u*u))**4,[0,1,mp.inf])
        i2 = mp.quad(lambda u:u*u*(2*u/(1+u*u))**4,[0,1,mp.inf])
        req(abs(i0-mp.pi/2)<mp.mpf("1e-55"),"i0")
        req(abs(i2-5*mp.pi/2)<mp.mpf("1e-55"),"i2")

        # N=2 RSET asymptote.
        u = mp.mpf("1e8")
        n2_asym = u*u*abs(t_stage(u)**2)
        req(abs(n2_asym-4) < mp.mpf("1e-6"),"N2 asymptote")
        return {
            "N2_u2_abs_q_limit":"4",
            "N2_RSET_integral_finite":False,
            "N4_phi2_abs_integral":mp.nstr(i0,40),
            "N4_RSET_abs_integral":mp.nstr(i2,40),
            "N4_RSET_integral_finite":True,
        }


def bisection_root(N, lo, hi):
    def f(y):
        return N*mp.log(2*y/(1+y)**2)+ADVANCE*y
    flo=f(lo); fhi=f(hi)
    req(flo*fhi<0,"bad bracket")
    for _ in range(300):
        mid=(lo+hi)/2
        fm=f(mid)
        if flo*fm<=0:
            hi=mid; fhi=fm
        else:
            lo=mid; flo=fm
    return (lo+hi)/2


def feedback_control():
    with mp.workdps(70):
        brackets={2:(mp.mpf("1"),mp.mpf("4")),
                  4:(mp.mpf("5"),mp.mpf("12")),
                  6:(mp.mpf("10"),mp.mpf("25"))}
        roots={}
        for N,(lo,hi) in brackets.items():
            y=bisection_root(N,lo,hi)
            gain=(2*y/(1+y)**2)**N*mp.e**(ADVANCE*y)
            req(abs(gain-1)<mp.mpf("1e-55"),"pole gain")
            roots[str(N)]=mp.nstr(y,40)
        req(abs(mp.mpf(roots["4"])-mp.mpf("9.273959245421"))<mp.mpf("1e-12"),"N4 root")

        # Demonstrate positive delay tradeoff.
        delay_rows=[]
        for tau_s in ("0.5","0.74","0.75","0.8"):
            tau=mp.mpf(tau_s)
            net=ADVANCE-tau
            delay_rows.append({
                "tau_over_r":tau_s,
                "net_advance_over_r":mp.nstr(net,20),
                "asymptotic_exponential_growth":bool(net>0),
            })
        return {
            "roots_y":roots,
            "N4_growth_time_over_r":mp.nstr(1/mp.mpf(roots["4"]),30),
            "finite_N_pole_reason":"exp(a y) beats every inverse power y^-N for a>0",
            "delay_rows":delay_rows,
        }


def supergaussian_control():
    with mp.workdps(50):
        R=mp.mpf(2)
        upper=mp.mpf("0.5")*mp.e**(R**4)
        req(upper>mp.mpf("1e6"),"supergaussian upper-plane growth")
        return {
            "q_real_profile":"0.5 exp(-u^4)",
            "upper_ray":"u=R exp(i*pi/4)",
            "R":"2",
            "|q|":mp.nstr(upper,30),
            "passive_Hinf":False,
        }


def evidence(path:Path):
    data=json.loads(path.read_text(encoding="utf-8"))
    src=Path(__file__).with_name("cbssl_uv_opaque_mouth_v14.py")
    req(data["base_sha"]==BASE_SHA,"base")
    req(data["code_sha256"]==hashlib.sha256(src.read_bytes()).hexdigest(),"stale evidence")
    req(data["classification"]=={"A":0,"B":0,"C":3},"classification")
    req(data["local_sheet"]["positive_local_energy"] is True,"positive sheet")
    req(data["null_loop_integrability"]["natural_two_mouth_filter"]["null_RSET_absolute_integral"].startswith("diverges"),"N2")
    req(data["null_loop_integrability"]["engineered_four_stage_filter"]["real_axis_RSET_finite"] is True,"N4 real axis")
    req(data["feedback_instability"]["stability"] is False,"instability")
    req(data["v13_causality_audit"]["passive_causal_H_infinity_transfer_accepted"] is False,"v13 causal audit")
    req(all(c["status"]=="C" for c in data["candidates"]),"candidate status")
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--evidence",type=Path)
    p.add_argument("--output",type=Path)
    a=p.parse_args()

    out={
        "verified":True,
        "classification":{"A":0,"B":0,"C":3},
        "scattering":scattering_control(),
        "integrability":integrability_control(),
        "feedback":feedback_control(),
        "supergaussian":supergaussian_control(),
        "environment":{"python":platform.python_version(),"mpmath":mp.__version__},
        "verifier_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    if a.evidence:
        out["evidence_sha256"]=evidence(a.evidence)
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")

    print(json.dumps({
        "verified":True,
        "local_UV_opacity":True,
        "N2_RSET":"DIVERGES",
        "N4_real_axis_RSET":"FINITE",
        "N4_feedback":"UNSTABLE",
        "N4_upper_pole":out["feedback"]["roots_y"]["4"],
    },ensure_ascii=False))


if __name__=="__main__":
    main()
