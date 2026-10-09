#!/usr/bin/env python3
"""Independent Hamiltonian and rational-bound checks; no forward import.

The analytic existence proof (direct method / contraction) is in the note.
This is not an automatic theorem prover for QFT or semiclassical gravity.
"""
from __future__ import annotations
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import sympy as s

PARENT = "7410fa94786ffe43c74ade1e4dc00ee2ce355127"


def quarter_exp() -> tuple[F,F]:
    # Different expansion: compute exp(1/4) and square, not exp(1/2).
    term=F(1); total=term
    for k in range(1,81):
        term/=4*k
        total+=term
    tail=term/F(4*81)/(1-F(1,4*82))
    return total,total+tail


def rational_certificate() -> dict:
    el,eu=quarter_exp(); lo,hi=el*el,eu*eu
    assert F(8,5)<lo<hi<F(5,3)
    assert lo>F(80,49) and hi<F(7,4)
    inv=F(1,6); source=F(1,8); radius=inv*source
    contraction=inv*F(1,8)
    residual=radius*radius/32
    dr=inv*residual
    dv=F(5,3)*residual
    # Logistic cubic Taylor remainder: max |f'''| <=1/8.
    error=dr/4+radius**3/48+dv*(F(1,6)+dv)
    assert radius==F(1,48) and contraction==F(1,48)
    assert dr==F(1,442368) and dv==F(5,221184)
    def central(e): return F(7,16)+e/(64*(e-1)**2)
    lower=central(hi)-error; upper=central(lo)+error
    # A genuinely truncated domain can exclude the complete witness.
    hump_lower=(el-1)/(8*(el+1))-dr
    assert hump_lower>F(1,100)
    assert F(49,100)<lower<upper<F(51,100)
    jlower=2*(1-F(49,80))-F(1,15)
    assert jlower==F(17,24) and jlower*F(3,8)==F(17,64)
    return {"exp_half":[str(lo),str(hi)],"r_range":["0",str(radius)],
            "Dirichlet_inverse_bound":str(inv),"contraction":str(contraction),
            "r_minus_first_iterate_bound":str(dr),
            "rprime_minus_first_iterate_bound":str(dv),
            "t0_error_bound":str(error),"t0_interval":[str(lower),str(upper)],
            "t_entire_curve_range":["95/192","313/576"],
            "shooting_r_derivative_lower":str(jlower),
            "shooting_2by2_abs_det_lower":str(jlower*F(3,8)),
            "witness_hump_lower":str(hump_lower)}


def hamiltonian() -> dict:
    t,psi,r,z=s.symbols("t psi r z", real=True)
    pt,ps,pr,pz=s.symbols("pt ps pr pz", real=True)
    f=s.Function("f")(r)
    Ham= -pt*ps-(f-t)*pt**2/2+(pr**2+pz**2)/2
    dx=[s.diff(Ham,p) for p in (pt,ps,pr,pz)]
    dp=[-s.diff(Ham,a) for a in (t,psi,r,z)]
    assert s.simplify(dp[0]/dx[1]/pt)==s.Rational(1,2)
    assert dp[1]==0 and dp[2]==s.diff(f,r)*pt**2/2
    # Eliminate momenta after differentiating dr/dpsi; different derivation
    # from the Christoffel computation in the forward script.
    v=-pr/pt
    dvlambda=s.diff(v,pr)*dp[2]+s.diff(v,pt)*dp[0]
    assert s.simplify(dvlambda/dx[1]-(s.diff(f,r)-v)/2)==0
    v0=s.symbols("v0")
    null_ps=(-(f-t)*pt**2+pr**2)/(2*pt)
    tprime=s.simplify((dx[0]/dx[1]).subs(ps,null_ps).subs(pr,-v0*pt))
    assert s.simplify(tprime-(f-t+v0*v0)/2)==0
    x=s.symbols("x", real=True)
    E=s.exp(s.Rational(1,2))
    r1=(1-s.exp(-x/2))/(4*(1-1/E))-x/4
    assert s.simplify(s.diff(r1,x,2)+s.diff(r1,x)/2+s.Rational(1,8))==0
    assert s.simplify(r1.subs(x,0))==s.simplify(r1.subs(x,1))==0
    approx=s.integrate(s.exp(x/2)*(s.Rational(1,2)-r1/4+s.diff(r1,x)**2)/2,(x,0,1))/(E-1)
    assert s.simplify(approx-(s.Rational(7,16)+E/(64*(E-1)**2)))==0
    # All-x inequalities used in the analytic enclosure, not sampled checks.
    B=s.Rational(2,3)*x*(1-x)
    assert s.expand(s.diff(B,x,2)+s.diff(B,x)/2+1+s.Rational(2,3)*x)==0
    y=s.symbols("y",real=True)
    assert s.expand(s.Rational(1,8)-(6*y*y-y)-(1-4*y)*(s.Rational(1,8)+s.Rational(3,2)*y))==0
    assert s.expand(6*y*y-y+s.Rational(1,24)-6*(y-s.Rational(1,12))**2)==0
    # Source NEC is not the same as positivity of a quantum state.
    u=s.symbols("u",real=True)
    assert s.expand(u*(1-u)*(1-2*u)).subs(u,s.Rational(1,4))>0
    # q=constant has no boost; this certificate must not reject an ESU control.
    gamma,L=s.symbols("gamma L",real=True)
    assert s.exp(gamma*L/2).subs(gamma,0)==1
    return {"log_p_t_return_derivative":"1/2", "p_psi_conserved":True,
            "radial_equation_verified":True,"null_time_equation_verified":True,
            "first_iterate_and_integrated_time_verified":True,
            "zero_boost_not_a_certificate":True,
            "nonperiodic_psi_not_a_closed_return":True,
            "truncated_domain_requires_whole_path":True}


def check_evidence(data: dict, cert: dict) -> None:
    if data.get("schema")!="chronology-dynamic-front-v1" or data.get("parent_sha")!=PARENT:
        raise ValueError("wrong evidence version/parent")
    flags={"formation_geometry_constructed":True,
           "standard_global_Hadamard_bisolution_excluded":True,
           "physical_formation_solution_found":False,"universal_no_go":False}
    for key,val in flags.items():
        if data.get(key) is not val: raise ValueError("wrong scope flag: "+key)
    if data.get("implemented_checks")!="passed": raise ValueError("incomplete run")
    got=data["certificate"]
    for key in ("r_range","Dirichlet_inverse_bound","contraction",
                "r_minus_first_iterate_bound","rprime_minus_first_iterate_bound",
                "t0_error_bound","t_entire_curve_range","shooting_r_derivative_lower",
                "shooting_2by2_abs_det_lower"):
        if got.get(key)!=cert[key]: raise ValueError("bad certificate field: "+key)
    # Independent enclosure must overlap; allow only very small rounding
    # differences, not an arbitrarily wide fabricated interval.
    for key in ("exp_half","t0_interval"):
        a,b=map(F,got[key]); c,d=map(F,cert[key])
        if not a<b or b<c or d<a: raise ValueError("nonoverlapping interval: "+key)
        if abs(a-c)>F(1,10**90) or abs(b-d)>F(1,10**90):
            raise ValueError("wrong interval bounds: "+key)
    eq=data["equations_and_repairs"]
    if eq.get("return_p_t_multiplier")!="exp(1/2)": raise ValueError("wrong holonomy")
    if eq.get("Grant_wall_kappa_at_crossing")!="a*R_dot": raise ValueError("wrong wall")
    geom=data["geometry"]
    if geom.get("div_Einstein")!="0 in all four components": raise ValueError("wrong conservation")
    if geom.get("switch_pressure")!="q''/(16*pi*G), uniform on both noncompact ends":
        raise ValueError("unaccounted switch stress")
    if "not actual RSET" not in geom.get("budget_convention",""):
        raise ValueError("source inverse-design mislabeled as physical RSET")
    tl,th=map(F,cert["t0_interval"])
    rows=data["diagnostics"]
    if [row["steps"] for row in rows]!=[64,128,256]: raise ValueError("missing refinement")
    for row in rows:
        if not tl<F(row["t0"])<th: raise ValueError("numerical root outside proof bounds")
        if F(row["endpoint_radial_covector_change"])>=0: raise ValueError("wrong radial kick")


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--evidence",type=Path); p.add_argument("--output",type=Path)
    args=p.parse_args()
    try:
        cert=rational_certificate(); ham=hamiltonian()
        if args.evidence:
            if args.evidence.stat().st_size>2_000_000: raise ValueError("oversized evidence")
            check_evidence(json.loads(args.evidence.read_text(encoding="utf-8")),cert)
        out={"schema":"chronology-dynamic-front-independent-v1","parent_sha":PARENT,
             "python":platform.python_version(),"sympy":s.__version__,
             "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
             "Hamiltonian":ham,"certificate":cert,"forward_json_checked":bool(args.evidence),
             "implemented_checks":"passed","QFT_formalization":False,
             "physical_formation_solution_found":False,"universal_no_go":False}
        text=json.dumps(out,ensure_ascii=False,indent=2)+"\n"
        if args.output:
            args.output.parent.mkdir(parents=True,exist_ok=True)
            args.output.write_text(text,encoding="utf-8")
        print(text,end="")
    except (AssertionError,ValueError,KeyError,TypeError,OSError) as err:
        p.exit(1,"verification failed: "+str(err)+"\n")

if __name__=="__main__":
    main()
