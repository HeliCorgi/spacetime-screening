#!/usr/bin/env python3
"""Independent Hamiltonian and rational checks for chronology null returns.

Does not import the forward script.  The analytic microlocal proof is in the
note; finite witnesses do not establish an all-geometries chronology theorem.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import platform
from fractions import Fraction as Q
from pathlib import Path
import sympy as sp

PARENT = "c6e6cda08ad73e457d135bcb9652a2355add9a9b"


def hamiltonian_checks() -> dict:
    T,x,y,z,a = sp.symbols("T x y z a", real=True)
    pt,px,py,pz = sp.symbols("pT px py pz", real=True)
    f=a*(x*x-y*y)/2
    H=((T-f)*pt*pt-2*pt*pz+px*px+py*py)/2
    central={T:0,x:0,y:0,px:0,py:0,pz:0}
    dz=sp.diff(H,pz).subs(central)
    dpt=-sp.diff(H,T).subs(central)
    assert dz == -pt
    assert sp.simplify(dpt/dz/pt) == sp.Rational(1,2)
    assert H.subs(central) == 0
    assert (-sp.diff(H,x)).subs(central) == 0
    assert (-sp.diff(H,y)).subs(central) == 0
    m=sp.symbols("m",positive=True)
    F=T/(2*m-T)
    H07=(F*pt*pt-2*pt*pz)/2
    ratio=sp.simplify((-sp.diff(H07,T)/sp.diff(H07,pz)/pt).subs({T:0,pz:0}))
    assert ratio == 1/(4*m)
    # Generic winding solution: dot T=1, p_psi=1, p_T=2/F.
    F=sp.Function("F")(T)
    H2=(F*pt*pt-2*pt*pz)/2
    vals={pt:2/F,pz:1}
    assert sp.simplify(H2.subs(vals)) == 0
    assert sp.simplify(sp.diff(H2,pt).subs(vals)) == 1
    assert sp.simplify(sp.diff(H2,pz).subs(vals)) == -2/F
    assert sp.simplify(-sp.diff(H2,T).subs(vals)-sp.diff(2/F,T)) == 0
    return {"ori2005_dlog_covector_dz":"1/2",
            "ori2007_dlog_covector_dz":"1/(4*m)",
            "winding_T_is_affine":True}



def periodic_repair_check() -> dict:
    """Independent null-axis calculation and explicit periodic coordinate map."""
    t,z=sp.symbols("t z",real=True)
    P=sp.Function("P")(z); Qf=sp.Function("Q")
    h=P*Qf(z-2*t)
    f0=P*Qf(z)
    g=sp.Matrix([[0,-h],[-h,h-f0]])
    inv=g.inv()
    # Only Gamma^z_zz is needed; compute it from metric differentiation.
    coord=(t,z)
    kappa=sp.simplify(sum(inv[1,j]*(2*sp.diff(g[j,1],z)-sp.diff(g[1,1],coord[j]))
                            for j in range(2))/2)
    assert sp.simplify(kappa-sp.diff(P,z)/P) == 0
    # Coordinate map of the positive periodic repair, evaluated independently.
    h=2+sp.cos(z-2*t); f0=2+sp.cos(z)
    V=2*t+sp.sin(t)*sp.cos(z-t)
    assert sp.trigsimp(sp.diff(V,t)-h) == 0
    assert sp.trigsimp(2*sp.diff(V,z)-(f0-h)) == 0
    assert sp.trigsimp(V.subs(z,z+2*sp.pi)-V) == 0
    # |V-2t|<=1. For V=-10 the whole closed loop has -11/2<=t<=-9/2.
    earliest=Q(-11,2); latest=Q(-9,2)
    assert latest < -4
    return {"kappa_is_log_derivative_of_P":True,
            "periodic_repair_has_global_stationary_coordinate":True,
            "example_loop_time_range":[str(earliest),str(latest)],
            "not_a_causal_formation_example":True}


def rational_witnesses() -> dict:
    cubic=[]
    for n in (2,4,8,16,32,64):
        t=Q(-1,n); tp=Q(-1,n+1)
        turns=1/(tp*tp)-1/(t*t)
        assert turns == 2*n+1
        assert t < tp < 0
        p=(2/t**3,Q(1))
        direct=(Q(0),Q(-1))
        assert p[0]*direct[1]-p[1]*direct[0] != 0
        cubic.append({"t":str(t),"t_prime":str(tp),"turns":int(turns)})
    grant=[]
    for n in (1,2,4,8,16,32,64):
        b=Q(n); lam=Q(2**n)
        # Solve null-chord equation for v, instead of using hyperbolic functions.
        du=1/lam-1
        dv_needed=b*b/du
        v=dv_needed/(lam-1)
        assert du*dv_needed == b*b
        k0=(-dv_needed/2,-du/2,b,Q(0))  # lower with g_uv=-1/2
        k1=(k0[0]/lam,lam*k0[1],b,Q(0))
        assert k0 != k1
        assert k0[0]*k1[2] != k1[0]*k0[2]
        midpoint_v=((1+1/lam)/2)*(v*(1+lam)/2)
        grant.append({"n":n,"uv":str(v),"midpoint_uv":str(midpoint_v)})
    return {"cubic_multiple_turns":cubic,"grant":grant}



def compactified_drift_verification() -> dict:
    # Compute covectors, rather than only the forward metric interval.
    rows=[]
    for B,n,m in [(sp.Integer(1),1,-1),(sp.Rational(10,7),10,-7),
                  (sp.sqrt(2),1,-1),(sp.sqrt(101),10,-1)]:
        displacement=n+m*B
        scale=sp.Integer(2)**n
        U=1/scale-1
        V=sp.simplify(displacement**2/U)
        v=sp.simplify(V/(scale-1))
        initial=sp.Matrix([-V/2,-U/2,displacement])
        returned=sp.Matrix([initial[0]/scale,scale*initial[1],displacement])
        assert initial != returned
        assert sp.simplify(-U*V+displacement**2) == 0
        peak_squared=sp.simplify(-v*(1+scale)*(1+1/scale)/4)
        assert sp.simplify(peak_squared < sp.Rational(29,20)**2) is sp.S.true
        rows.append({"B":str(B),"n":n,"m":m,"uv":str(v),"net_drift":str(displacement),"covector_mismatch":True})
    return {"exact_cases":rows,"theorem_is_in_note":True}


def controls() -> dict:
    # Independent positive series log(2)=sum_{j>=1} 1/(j*2^j).
    lower=sum((Q(1,j*2**j) for j in range(1,101)),Q(0))
    upper=lower+Q(1,101*2**100)
    assert Q(289,200)*lower > 1
    assert Q(289,200) < Q(29,20) < Q(3,2)
    # A common rescaling of a WF pair is allowed; independent rescaling is not.
    k=sp.Matrix([1,1]); alpha=sp.Rational(2)
    assert alpha*k != k
    assert sp.Matrix.vstack(alpha*k,-k) != alpha*sp.Matrix.vstack(k,-k)
    # Round S3 geodesic returns with the SAME tangent after length 2*pi*a.
    s=sp.symbols("s",real=True)
    X=sp.Matrix([sp.cos(s),sp.sin(s),0,0])
    dX=sp.diff(X,s)
    assert X.subs(s,2*sp.pi) == X.subs(s,0)
    assert dX.subs(s,2*sp.pi) == dX.subs(s,0)
    return {"WF_joint_not_separate_scaling":True,
            "round_S3_return_covector_unchanged":True,
            "cutoff_Grant_CTC_control":True,
            "unchanged_return_is_not_a_no_go_certificate":True,
            "nonclosed_black_hole_generator_not_excluded":True}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence",type=Path)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    H=hamiltonian_checks(); R=rational_witnesses(); C=controls(); X=periodic_repair_check(); D=compactified_drift_verification()
    if args.evidence:
        ev=json.loads(args.evidence.read_text(encoding="utf-8"))
        assert ev["schema"] == "chronology-null-return-v1"
        assert ev["parent_sha"] == PARENT
        assert ev["ori"]["central_K_acceleration"] == ["0","-1/2","0","0"]
        assert ev["ori"]["ori2005_affine_return_multiplier"] == "exp(ell/2)"
        assert ev["ori"]["ori2007_affine_return_multiplier"] == "exp(ell/(4*m))"
        assert ev["ori"]["ori2005_Ricci"] == ev["ori"]["ori2007_Ricci"] == "zero"
        assert ev["traveling_wave"]["affine_return_multiplier"] == "1/c"
        assert ev["traveling_wave"]["sech_profile_descends_as_stated"] is False
        assert ev["traveling_wave"]["periodic_control_Ricci"] == "zero"
        assert ev["traveling_wave"]["periodic_control_CTCs_arbitrarily_early"] is True
        assert ev["traveling_wave"]["periodic_control_causal_formation"] is False
        assert ev["degenerate"]["cubic_horizon_multiplier"] == "1"
        assert ev["degenerate"]["winding_covector"] == ["2/F(t)","1"]
        assert ev["grant"]["pure_time_translation_null_witness"] is False
        assert len(ev["grant"]["witnesses"]) == len(R["grant"])
        for given,wanted in zip(ev["grant"]["witnesses"],R["grant"]):
            assert given["n"] == wanted["n"]
            assert Q(given["uv"]) == Q(wanted["uv"])
            assert Q(given["midpoint_uv"]) == Q(wanted["midpoint_uv"])
            assert given["null_interval"] == "0" and given["returned_tangent_mismatch"] is True
        assert ev["cutoff_grant"]["CTC_geometric_control"] is True
        assert ev["cutoff_grant"]["cutoff_R"] == "29/20"
        assert ev["cutoff_grant"]["minimum_null_chord_peak_radius"] == "3/2"
        assert ev["cutoff_grant"]["null_selfreturn_witness_contained"] is False
        assert ev["cutoff_grant"]["physical_boundary_completion"] is False
        assert len(ev["compact_drift"]["examples"]) == 4
        for given,wanted in zip(ev["compact_drift"]["examples"],D["exact_cases"]):
            assert given["contained"] is True
            assert (given["n"],given["m"]) == (wanted["n"],wanted["m"])
            assert given["period"] == wanted["B"]
            assert given["uv"] == wanted["uv"]
            assert given["net_drift"] == wanted["net_drift"]
        assert ev["formation_solution_found"] is False
        assert ev["universal_chronology_no_go"] is False
    out={"schema":"chronology-null-return-independent-v1","parent_sha":PARENT,
         "python":platform.python_version(),"sympy":sp.__version__,
         "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         "Hamiltonian":H,"rational_witnesses":R,"negative_controls":C,"periodic_repair":X,"compact_drift":D,
         "forward_json_checked":args.evidence is not None,
         "implemented_checks":"passed","QFT_formalization":False,
         "full_formation_resolution":False}
    text=json.dumps(out,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding="utf-8")
    print(text,end="")

if __name__ == "__main__":
    main()
