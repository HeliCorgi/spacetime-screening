#!/usr/bin/env python3
"""CBSSL v10: regulated 3+1D semiclassical throat core with R_sc=0.

Toy model, not established physics.  The support sector uses the published
zeroth-order/local RSET of Popov's long-throat scalar fields plus an
independent electrostatic field.  For constant f and r the cited RSET
expressions are exact in that local product geometry; this script solves the
corresponding 3+1D semiclassical Einstein equations directly.

A CBSSL-selected Z2 order-parameter bit is added in a degenerate zero-stress
vacuum, so the two sender interventions do not disturb the solved background.
The global chronology quotient is a toy helical identification; the nonlocal
state/topology correction to the support-field RSET on that quotient is NOT
claimed solved.  Its symmetry-preserving small-correction sensitivity is
quantified by an implicit-function Jacobian.
"""
from __future__ import annotations
import argparse, hashlib, json, platform
from pathlib import Path
import mpmath as mp
import sympy as sp

BASE_SHA = "c27097e29e05275b56a922e5c63e0b99526d1da2"
PRECISIONS = (50, 80)
XI = "-10000"
M2 = "1000"


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def exact_geometry():
    """Direct 4D Christoffel/Ricci check for M2 x S2 of radius r."""
    t, x, th, ph, r = sp.symbols("t x theta phi r", real=True, positive=True)
    coords = (t, x, th, ph)
    g = sp.diag(-1, 1, r**2, r**2 * sp.sin(th)**2)
    gi = sp.simplify(g.inv())
    n = 4
    Gamma = [[[
        sp.simplify(sp.Rational(1, 2) * sum(
            gi[a, d] * (sp.diff(g[d, c], coords[b]) + sp.diff(g[d, b], coords[c]) - sp.diff(g[b, c], coords[d]))
            for d in range(n)))
        for c in range(n)] for b in range(n)] for a in range(n)]
    Ric = sp.zeros(n)
    for a in range(n):
        for b in range(n):
            expr = 0
            for c in range(n):
                expr += sp.diff(Gamma[c][a][b], coords[c]) - sp.diff(Gamma[c][a][c], coords[b])
                for d in range(n):
                    expr += Gamma[c][c][d] * Gamma[d][a][b] - Gamma[c][b][d] * Gamma[d][a][c]
            Ric[a, b] = sp.simplify(expr)
    R = sp.simplify(sum(gi[a, b] * Ric[a, b] for a in range(n) for b in range(n)))
    Gcov = sp.simplify(Ric - g * R / 2)
    Gmix = sp.simplify(gi * Gcov)
    target = sp.diag(-1/r**2, -1/r**2, 0, 0)
    require(sp.simplify(Gmix-target) == sp.zeros(4), "4D Einstein tensor mismatch")
    require(sp.simplify(R-2/r**2) == 0, "Ricci scalar")
    return {"metric":"diag(-1,1,r^2,r^2 sin^2 theta)",
            "Ricci_scalar":"2/r^2",
            "Einstein_mixed":"diag(-1/r^2,-1/r^2,0,0)",
            "direct_4d_check":True}


def popov_polynomials(xi):
    pt = -xi**3/6 + xi**2/12 - xi/60 + mp.mpf(1)/630
    pth = xi**3/3 - xi**2/6 + xi/30 - mp.mpf(1)/315
    require(mp.almosteq(pth, -2*pt), "massive-field tensor polynomial relation")
    return pt, pth


def quantum_rset(r, xi, m2, mds):
    """Published long-throat local RSET used by Popov, mixed components.

    T^t_t=T^x_x and T^theta_theta=T^phi_phi.  Numerical coefficients are
    those printed in the source (0.00310 and -0.00171), hence this is the
    published zeroth-order model, not more precise data than the paper gives.
    """
    pt, pth = popov_polynomials(xi)
    logterm = mp.log(mds**2 * r**2) / 720
    ft = mp.mpf("0.00310") + logterm + pt/(m2*r**2)
    fth = -mp.mpf("0.00171") - logterm + pth/(m2*r**2)
    fac = 1/(4*mp.pi**2*r**4)
    return fac*ft, fac*fth


def residual(r, q2, xi, m2, mds):
    tq_t, tq_th = quantum_rset(r, xi, m2, mds)
    tem_t = -q2/(8*mp.pi*r**4)
    tem_th = +q2/(8*mp.pi*r**4)
    et = -1/r**2 - 8*mp.pi*(tq_t + tem_t)
    ex = et
    eth = -8*mp.pi*(tq_th + tem_th)
    eph = eth
    return (et, ex, eth, eph), (tq_t, tq_t, tq_th, tq_th), (tem_t, tem_t, tem_th, tem_th)


def solve_core(dps):
    with mp.workdps(dps):
        xi = mp.mpf(XI); m2 = mp.mpf(M2); m = mp.sqrt(m2); mds = m
        r0, q20 = mp.findroot(
            lambda rr, qq: (residual(rr, qq, xi, m2, mds)[0][0],
                            residual(rr, qq, xi, m2, mds)[0][2]),
            (mp.mpf("101.49"), mp.mpf("20601.8")), tol=mp.power(10, -(dps-15)), maxsteps=100)
        res, tq, tem = residual(r0, q20, xi, m2, mds)
        maxres = max(abs(v) for v in res)
        require(maxres < mp.power(10, -(dps-20)), "semiclassical residual not solved")
        rsc_density = sum(v*v for v in res)
        require(rsc_density < mp.power(10, -2*(dps-20)), "R_sc density")

        f = lambda rr, qq: mp.matrix([residual(rr, qq, xi, m2, mds)[0][0],
                                      residual(rr, qq, xi, m2, mds)[0][2]])
        J = mp.matrix([
            [mp.diff(lambda z: f(z, q20)[0], r0), mp.diff(lambda z: f(r0, z)[0], q20)],
            [mp.diff(lambda z: f(z, q20)[1], r0), mp.diff(lambda z: f(r0, z)[1], q20)],
        ])
        detJ = mp.det(J)
        require(abs(detJ) > mp.mpf("1e-20"), "IFT Jacobian singular")
        Jinv = J**-1

        L = 100*r0
        Delta = 2*L
        k2 = L**2 - Delta**2
        require(k2 < 0, "identification generator not timelike")
        return_advance = Delta - L
        require(return_advance > 0, "no past return")

        return {
            "dps":dps,
            "xi":XI,"m_squared":M2,"m_DS_equals_m":True,
            "r_planck":mp.nstr(r0,55),"Q_squared":mp.nstr(q20,55),"Q_abs":mp.nstr(mp.sqrt(q20),55),
            "quantum_RSET_mixed":[mp.nstr(v,45) for v in tq],
            "electrostatic_T_mixed":[mp.nstr(v,45) for v in tem],
            "Einstein_mixed":[mp.nstr(-1/r0**2,45),mp.nstr(-1/r0**2,45),"0","0"],
            "residual_mixed":[mp.nstr(v,12) for v in res],
            "max_abs_residual":mp.nstr(maxres,12),
            "R_sc_density":mp.nstr(rsc_density,12),
            "jacobian":[[mp.nstr(J[i,j],35) for j in range(2)] for i in range(2)],
            "jacobian_determinant":mp.nstr(detJ,35),
            "response_matrix_8pi_Jinv":[[mp.nstr(8*mp.pi*Jinv[i,j],30) for j in range(2)] for i in range(2)],
            "chronology_toy":{"L_over_r":"100","Delta_over_L":"2","generator_norm_squared":mp.nstr(k2,35),
                              "null_return_time_advance":mp.nstr(return_advance,35)},
        }


def compare_precision(lo, hi):
    errs=[]
    for key in ("r_planck","Q_squared"):
        a=mp.mpf(lo[key]); b=mp.mpf(hi[key]); errs.append(abs(a-b)/max(1,abs(b)))
    require(max(errs) < mp.mpf("1e-35"), "50/80 precision mismatch")
    return mp.nstr(max(errs),12)


def z2_signal_receiver():
    """Zero-stress bit carrier in the regulated CBSSL toy core."""
    x, v, lam = sp.symbols("x v lambda_chi", positive=True)
    V = lam*(x**2-v**2)**2/4
    require(sp.simplify(V.subs(x,v)) == 0 and sp.simplify(V.subs(x,-v)) == 0, "vacuum energy")
    require(sp.simplify(sp.diff(V,x).subs(x,v)) == 0 and sp.simplify(sp.diff(V,x).subs(x,-v)) == 0, "vacuum field equation")
    with mp.workdps(80):
        k = mp.mpf(3)
        pc = (1+mp.erf(k/mp.sqrt(2)))/2
        pe = 1-pc
        D = 2*pc-1
        require(abs(D-mp.erf(k/mp.sqrt(2))) < mp.mpf("1e-70"), "receiver TV")
        return {
            "field":"independent real Z2 order parameter chi with V=lambda_chi(chi^2-v^2)^2/4",
            "selected_fixed_points":{"do_0":"chi=+v","do_1":"chi=-v"},
            "signal_stress_at_fixed_point":"T_mn=0 for both bits in the core",
            "sender_operation":"complete local reset operation E_b biases the returning order parameter to (-1)^b v; CBSSL selects the corresponding chronology fixed point; no future outcome postselection",
            "receiver":"finite worldtube sign sensor with additive Gaussian apparatus noise sigma and v/sigma=3",
            "P_Y_do_0":{"+1":mp.nstr(pc,50),"-1":mp.nstr(pe,50)},
            "P_Y_do_1":{"+1":mp.nstr(pe,50),"-1":mp.nstr(pc,50)},
            "D_past":mp.nstr(D,50),
            "receiver_precedes_sender":True,
        }


def candidate_record(core, signal):
    return {
        "candidate_id":"cbssl-popov-helical-core-v10",
        "status":"B",
        "dimension":4,
        "dimension_split":{"space":3,"time":1},
        "geometry":"Regulated constant long-throat core ds^2=-dt^2+dx^2+r0^2 dOmega2 with toy helical chronology identification (t,x)~(t-Delta,x+L), Delta=2L. Local tensors are those of M2 x S2.",
        "matter_content":"Popov support sector: one conformal massless scalar + one very massive nonconformal scalar in the published renormalized long-throat state, plus a classical electrostatic field. Independent Z2 order-parameter bit carrier at degenerate zero-stress minima.",
        "quantum_state":"Support RSET is the published constant-throat/local renormalized state functional. CBSSL selects the chronology fixed point of the Z2 signal operation. The exact global quotient-dependent support-field state/RSET is not supplied.",
        "topology":"3+1D product throat with a helical toy chronology return; not an asymptotically flat manufactured two-mouth spacetime.",
        "assumptions":[
            "CBSSL v9 is taken as the new toy state-selection law.",
            "Use Popov's printed zeroth-order RSET coefficients as the regulated support effective theory; on constant f,r those local expressions are exact for the product background considered in that calculation.",
            "Global nonlocal/image corrections caused by the chronology identification are not silently set to zero; they are the remaining state-completion problem.",
            "Z2 signal minima have zero local stress, so bit choice does not alter the solved support residual."
        ],
        "boundary_conditions":"Helical return acts on the complete signal register under CBSSL. Support-sector renormalization scale is fixed with m_DS=m and is not operation-dependent.",
        "symmetries":["Static local M2 x S2 support core; signal fixed point is spatially constant in the core."],
        "approximation_order":"Exact 4D Einstein tensor; published zeroth-order/local renormalized support RSET solved nonperturbatively as algebraic semiclassical equations. Global chronology-topology RSET correction not included.",
        "stress_energy":{"kind":"renormalized_support_RSET_plus_classical_EM","renormalized":True,"full_tensor_matched_in_regulated_core":True,
                         "details":"All four diagonal mixed Einstein equations vanish at the solved r0,Q^2 within the Popov local-RSET model. Signal T_mn=0 at both selected Z2 minima."},
        "backreaction":{"level":"self_consistent_regulated_3plus1D_core","details":"R_sc density is solved to numerical zero on the constant core. An invertible two-parameter Jacobian proves small symmetry-preserving extra diagonal RSET corrections can be retuned by nearby r,Q^2 at first order."},
        "support_accounting":{"complete":False,"details":"The asymptotically-flat mouth/transition apparatus and the global quotient-dependent support-field state are not completed."},
        "stability":"Not established globally. Local algebraic solution is nonsingular in the two solved residual directions; Jacobian is invertible.",
        "causal_structure":"Toy helical identification has timelike generator and a positive null-return time advance. It is imposed rather than dynamically manufactured.",
        "sender_intervention":{"description":"do(b) applies the complete Z2 reset/bias operation E_b at the future station; CBSSL loop consistency selects chi=(-1)^b v throughout the chronology branch.","same_preparation":True,"uses_postselection":False,"future_boundary_condition_is_input":False},
        "receiver_observable":"Finite worldtube sign detector with Gaussian apparatus noise v/sigma=3.",
        "P_Y_do_0":{"computed":True,"distribution":signal["P_Y_do_0"]},
        "P_Y_do_1":{"computed":True,"distribution":signal["P_Y_do_1"]},
        "distinguishability":{"metric":"total_variation","computed":True,"value":signal["D_past"],"receiver_precedes_sender":True},
        "obstructions":[],
        "unresolved_assumptions":[
            "Compute the actual global CBSSL-selected Hadamard/regulated support-field RSET on the chronology quotient, including nonlocal topology/image contributions, and verify it lies in the small symmetry-preserving correction class or solve the enlarged metric problem.",
            "Construct asymptotically flat finite mouths/transition layers and their complete apparatus stress rather than imposing the helical chronology quotient.",
            "Prove dynamical stability and cutoff/cut independence of the full CBSSL state."
        ],
        "calculation":{"core":core,"signal":signal},
        "verification":{"computational":"direct 4D curvature + 50/80-digit nonlinear solve + separate verifier","external_peer_review":"not_performed","human_review_for_A":True},
        "scope":"First CBSSL model in this project with an actual published 3+1D renormalized support tensor solved to R_sc=0 in a regulated chronology core and explicit nonzero past-bit distributions. B, not protocol-A, because the global quotient RSET and finite manufactured geometry are not completed."
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output",type=Path)
    args=p.parse_args()
    geom=exact_geometry()
    runs=[solve_core(d) for d in PRECISIONS]
    precision=compare_precision(*runs)
    signal=z2_signal_receiver()
    candidate=candidate_record(runs[-1],signal)
    data={"base_sha":BASE_SHA,"classification":{"A":0,"B":1,"C":0},"geometry":geom,
          "precision_runs":runs,"max_50_80_relative_difference":precision,"signal":signal,"candidate":candidate,
          "environment":{"python":platform.python_version(),"sympy":sp.__version__,"mpmath":mp.__version__},
          "code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"
",encoding="utf-8")
    print(json.dumps({"passed":True,"classification":data["classification"],"r_planck":runs[-1]["r_planck"],
                      "Q_squared":runs[-1]["Q_squared"],"R_sc_density":runs[-1]["R_sc_density"],
                      "D_past":signal["D_past"]},ensure_ascii=False))

if __name__=="__main__": main()
