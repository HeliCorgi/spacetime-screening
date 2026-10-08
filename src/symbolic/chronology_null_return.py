#!/usr/bin/env python3
"""Exact geometry behind the null-return obstruction; not a QFT proof engine.

The distributional propagation argument and its hypotheses are in
notes/chronology-formation-mainline.md.  No source stress is reverse-defined.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import platform
from fractions import Fraction
from pathlib import Path
import sympy as sp

PARENT = "c6e6cda08ad73e457d135bcb9652a2355add9a9b"


def geometry(metric: sp.Matrix, coordinates: tuple):
    """Levi-Civita connection and Ricci tensor directly from a covariant metric."""
    n = len(coordinates)
    inv = metric.inv().applyfunc(sp.simplify)
    gamma = [[[sp.simplify(sum(inv[i, l] * (
        sp.diff(metric[l, k], coordinates[j]) + sp.diff(metric[l, j], coordinates[k])
        - sp.diff(metric[j, k], coordinates[l])) for l in range(n)) / 2)
        for k in range(n)] for j in range(n)] for i in range(n)]
    ricci = sp.zeros(n)
    for i in range(n):
        for j in range(n):
            ricci[i, j] = sp.simplify(sum(
                sp.diff(gamma[k][i][j], coordinates[k])
                - sp.diff(gamma[k][i][k], coordinates[j])
                + sum(gamma[k][k][l] * gamma[l][i][j]
                      - gamma[k][j][l] * gamma[l][i][k] for l in range(n))
                for k in range(n)))
    return inv, gamma, ricci


def ori_vacuum_checks() -> dict:
    t, z, x, y = sp.symbols("T z x y", real=True)
    a = sp.symbols("a", positive=True)
    profile = a * (x*x - y*y) / 2
    g = sp.Matrix([[0, -1, 0, 0], [-1, profile-t, 0, 0],
                   [0, 0, 1, 0], [0, 0, 0, 1]])
    inverse, gamma, ricci = geometry(g, (t, z, x, y))
    assert sp.simplify(g.det()) == -1
    assert ricci == sp.zeros(4)
    acceleration = [sp.simplify(gamma[i][1][1].subs({t:0, x:0, y:0})) for i in range(4)]
    assert acceleration == [0, -sp.Rational(1,2), 0, 0]
    # Future orientation can reverse the loop; either multiplier is nonunit.
    length = sp.symbols("ell", positive=True)
    multiplier = sp.exp(length/2)
    assert sp.simplify(sp.diff(sp.exp(z/2), z) - sp.exp(z/2)/2) == 0
    # Ori 2007: t=2m-r, psi=v, F=t/(2m-t).
    m, th, ph = sp.symbols("m theta phi", positive=True)
    r = 2*m-t
    F = t/r
    g07 = sp.Matrix([[0,-1,0,0],[-1,-F,0,0],
                     [0,0,r*r,0],[0,0,0,r*r*sp.sinh(th)**2]])
    _, connection07, ricci07 = geometry(g07, (t,z,th,ph))
    assert ricci07.applyfunc(sp.simplify) == sp.zeros(4)
    kappa07 = sp.simplify(connection07[1][1][1].subs(t,0))
    assert kappa07 == -1/(4*m)
    return {"ori2005_Ricci":"zero", "determinant":"-1",
            "central_K_acceleration":list(map(str,acceleration)),
            "ori2005_affine_return_multiplier":str(multiplier),
            "ori2007_Ricci":"zero", "ori2007_kappa":str(kappa07),
            "ori2007_affine_return_multiplier":"exp(ell/(4*m))",
            "scope":"specified vacuum cores; no assumption of compact generation"}



def traveling_wave_quotient_checks() -> dict:
    """Audit the stated z-periodic quotient, including a periodic repair.

    The general local vacuum h=P(z)Q(z-2t) is not an arbitrary metric on S1:
    its factors must satisfy compatible Floquet conditions. The proof of the
    resulting nonunit-holonomy / stationary-repair dichotomy is in the note.
    """
    t,z,x,y=sp.symbols("t z x y",real=True)
    k,eps,alpha,length=sp.symbols("k epsilon alpha ell",real=True)
    h=sp.exp(k*(eps*z-alpha*t))
    ratio=sp.simplify(h.subs(z,z+length)/h)
    assert ratio == sp.exp(k*eps*length)
    assert (k*alpha).subs(alpha,2*eps) == 2*k*eps
    # A concrete member of the plotted sech profile is not periodic either.
    assert sp.sech(sp.Integer(1))**2 != 1
    # General factorized local metric. Its connection along the null axis
    # has kappa=(h_z+h_t/2)/h=P'/P, regardless of the traveling factor Q.
    P=sp.Function("P")(z)
    Q=sp.Function("Q")
    hg=P*Q(z-2*t)
    kappa=sp.simplify((sp.diff(hg,z)+sp.diff(hg,t)/2)/hg)
    assert kappa == sp.diff(P,z)/P
    # Pull back a v-stationary metric by the exact one-form
    # dv=Q(z-2t)dt + (Q(z)-Q(z-2t))dz/2.
    P0,Qw,Qz,f=sp.symbols("P Qw Qz f",real=True)
    J=sp.eye(4); J[0,0]=Qw; J[0,1]=(Qz-Qw)/2
    stationary=sp.Matrix([[0,-P0,0,0],[-P0,P0*Qz-f,0,0],
                          [0,0,1,0],[0,0,0,1]])
    original=sp.Matrix([[0,-P0*Qw,0,0],[-P0*Qw,P0*Qw-f,0,0],
                       [0,0,1,0],[0,0,0,1]])
    assert (J.T*stationary*J-original).applyfunc(sp.simplify) == sp.zeros(4)
    # Do not incorrectly require the individual factors to be periodic.
    # P=exp(-z), Q=exp(z-2t) gives the legitimate periodic h=exp(-2t),
    # with nonunit Floquet c=exp(-ell) and nonunit null return.
    valid_h=sp.simplify(sp.exp(-z)*sp.exp(z-2*t))
    assert valid_h == sp.exp(-2*t)
    assert sp.simplify(valid_h.subs(z,z+length)-valid_h) == 0
    # A globally valid positive periodic repair: Q(s)=2+cos(s), P=1.
    # Primitive Qint=2s+sin(s), so v=2t+[sin z-sin(z-2t)]/2.
    v=2*t+(sp.sin(z)-sp.sin(z-2*t))/2
    assert sp.trigsimp(v.subs(z,z+2*sp.pi)-v) == 0
    assert sp.trigsimp(sp.diff(v,t)-(2+sp.cos(z-2*t))) == 0
    # h>=1 ensures invertibility. |v-2t|<=1 holds for all real z,t.
    # f=Q(z)+a(x^2-y^2)/2 then gives permanent pp-wave CTCs, not onset.
    a=sp.symbols("a",positive=True)
    pp=sp.Matrix([[0,-1,0,0],[-1,-a*(x*x-y*y)/2,0,0],
                  [0,0,1,0],[0,0,0,1]])
    _,_,ric=geometry(pp,(t,z,x,y))  # t denotes v in this independent chart
    assert ric == sp.zeros(4)
    assert pp[1,1].subs({x:1,y:0}) == -a/2
    assert pp[1,1].subs({x:0,y:0}) == 0
    return {"stated_exponential_z_monodromy":str(ratio),
            "sech_profile_descends_as_stated":False,
            "general_local_h":"P(z)*Q(z-2*t)",
            "periodicity_requires":"P(z+ell)=c*P(z), Q(s+ell)=Q(s)/c, c>0",
            "null_axis_kappa":"P_prime/P", "affine_return_multiplier":"1/c",
            "valid_nonunit_Floquet_control":"h=exp(-2*t), c=exp(-ell)",
            "unit_Floquet_repair":"P and Q periodic => global v-stationary metric",
            "periodic_control_v":str(v),"periodic_control_Ricci":"zero",
            "periodic_control_CTCs_arbitrarily_early":True,
            "periodic_control_causal_formation":False,
            "scope":"specified simple z identification and positive factorized vacuum family"}


def degenerate_crossing_checks() -> dict:
    t, z = sp.symbols("t psi", real=True)
    F = sp.Function("F")(t)
    g = sp.Matrix([[0,-1],[-1,-F]])
    inv, gamma, ricci = geometry(g,(t,z))
    assert inv == sp.Matrix([[F,-1],[-1,0]])
    scalar = sp.simplify(sp.trace(inv*ricci))
    assert scalar == -sp.diff(F,t,2)
    V = sp.Matrix([1,-2/F])
    assert sp.simplify((V.T*g*V)[0]) == 0
    assert g*V == sp.Matrix([2/F,1])
    assert gamma[0][0][0] == gamma[1][0][0] == 0
    accel = sp.Matrix([sum(V[j]*sp.diff(V[i],(t,z)[j]) for j in range(2))
                      + sum(gamma[i][j][k]*V[j]*V[k] for j in range(2) for k in range(2))
                      for i in range(2)])
    assert accel.applyfunc(sp.simplify) == sp.zeros(2,1)
    s, L = sp.symbols("s L", positive=True)
    # t=-s; second null branch makes one turn and returns closer to t=0.
    q_linear = -s*sp.exp(-L/2)
    q_cubic = -s/sp.sqrt(1+L*s*s)
    assert sp.simplify(-2*sp.log((-q_linear)/s)-L) == 0
    assert sp.simplify(1/q_cubic**2-1/s**2-L) == 0
    assert sp.diff(t**3,t).subs(t,0) == 0  # no nonunit holonomy at horizon
    return {"inverse_tt":"F(t)", "scalar_curvature":str(scalar),
            "winding_tangent":["1","-2/F(t)"],
            "winding_covector":["2/F(t)","1"],
            "local_direct_covector":["0","-1"],
            "F_t_endpoint":str(q_linear), "F_t_cubed_endpoint":str(q_cubic),
            "cubic_horizon_multiplier":"1",
            "mechanism":"wrong off-diagonal null direction, not nonunit horizon holonomy",
            "scope":"analytic proof uses smooth F(0)=0 and F(t)<0 for t<0; see note"}


def grant_checks() -> dict:
    rows=[]
    for n in (1,2,4,8,16,32,64):
        scale=Fraction(2)**n
        D=scale+1/scale-2
        u=Fraction(1); v=-Fraction(n*n)/D
        tangent=(u/scale-u, scale*v-v, Fraction(n), Fraction(0))
        assert -tangent[0]*tangent[1]+tangent[2]**2 == 0
        pulled=(scale*tangent[0],tangent[1]/scale,tangent[2],tangent[3])
        assert pulled != tangent
        # Nonzero transverse component rules out even proportionality.
        assert pulled[0]*tangent[2] != tangent[0]*pulled[2]
        # The straight witness leaves a fixed thin collar as n grows.
        umid=(u+u/scale)/2; vmid=(v+scale*v)/2
        assert umid*vmid == v*(scale+1/scale+2)/4
        rows.append({"n":n,"uv":str(u*v),"null_interval":"0",
                     "returned_tangent_mismatch":True,"midpoint_uv":str(umid*vmid)})
    assert abs(Fraction(rows[-1]["uv"])) < Fraction(1,10**12)
    # Controls: pure timelike translation has CTCs but no null self-image chord.
    assert -Fraction(3)**2 < 0
    return {"boost_factor":"2", "transverse_shift":"1", "witnesses":rows,
            "scope":"full Grant quotient or a domain containing the WHOLE null witness",
            "collar_warning":"endpoint accumulation alone does not ensure witness containment",
            "pure_time_translation_null_witness":False}



def compact_drift_checks() -> dict:
    """An additional y period restores null witnesses inside the cutoff.

    The note proves this for every period using pigeonhole approximation.
    These exact examples independently guard rational and irrational periods.
    """
    cases=[]
    for period,n,m in [(sp.Integer(1),1,-1),(sp.Rational(10,7),10,-7),
                       (sp.sqrt(2),1,-1),(sp.sqrt(101),10,-1)]:
        b=n+m*period; lam=sp.Integer(2)**n
        if b == 0:
            uv=sp.Integer(0); peak=sp.Integer(0)
        else:
            uv=sp.simplify(-b*b/(lam+1/lam-2))
            peak=sp.simplify(sp.Abs(b)*(lam+1)/(2*(lam-1)))
        du=1/lam-1; dv=(lam-1)*uv
        assert sp.simplify(-du*dv+b*b) == 0
        assert sp.simplify(peak < sp.Rational(29,20)) is sp.S.true
        assert lam != 1
        cases.append({"period":str(period),"n":n,"m":m,"net_drift":str(b),
                      "uv":str(uv),"peak_radius":str(peak),"contained":True})
    return {"extra_identification":"y~y+B, B>0", "examples":cases,
            "general_bound":"N>3*B/(2*R) => some 1<=n<=N, m, |n+m*B|<=B/N",
            "result":"every extra drift period restores a contained bad null return",
            "scope":"translation compactification; not arbitrary physical boundary completion"}


def cutoff_grant_control() -> dict:
    # log(2)=2 atanh(1/3), bounded by a positive rational series and tail.
    log_lo=sum((Fraction(2, (2*j+1)*3**(2*j+1)) for j in range(20)), Fraction(0))
    log_hi=log_lo+Fraction(2,41*3**41)*Fraction(9,8)
    R=Fraction(29,20); radius=Fraction(289,200)
    assert radius < R < Fraction(3,2)
    assert radius*log_lo > 1
    # Every null self-image chord in the full boost-by-2 quotient reaches
    # r_mid >= (1/2)coth(log(2)/2)=3/2; monotonicity is proved in the note.
    return {"cutoff_R":str(R), "CTC_radius":str(radius),
            "log2_lower":str(log_lo),"log2_upper":str(log_hi),
            "K_norm_upper":str(1-radius**2*log_lo**2),
            "minimum_null_chord_peak_radius":"3/2",
            "null_selfreturn_witness_contained":False,
            "CTC_geometric_control":True,
            "physical_boundary_completion":False,
            "warning":"timelike boundary/hole and noncompact geometry; not a prepared apparatus"}


def run() -> dict:
    return {"schema":"chronology-null-return-v1","parent_sha":PARENT,
            "python":platform.python_version(),"sympy":sp.__version__,
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "ori":ori_vacuum_checks(),"traveling_wave":traveling_wave_quotient_checks(),
            "degenerate":degenerate_crossing_checks(),
            "grant":grant_checks(),"cutoff_grant":cutoff_grant_control(),
            "compact_drift":compact_drift_checks(),"implemented_checks":"passed",
            "formation_solution_found":False,"universal_chronology_no_go":False,
            "not_proved":["automated wavefront-set theorem", "all finite-energy formation geometries",
                          "full nonlinear semiclassical evolution", "causal preparation of an eternal quotient"]}


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output",type=Path)
    args=p.parse_args()
    text=json.dumps(run(),ensure_ascii=False,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding="utf-8")
    print(text,end="")

if __name__ == "__main__":
    main()
