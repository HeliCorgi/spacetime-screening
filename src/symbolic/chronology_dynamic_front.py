#!/usr/bin/env python3
"""Geometry and certified bounds for a dynamic drift-front; not an SCEE solver.

The no-Hadamard conclusion is an analytic argument in the companion note.
No finite sample is promoted to a wavefront-set or state-existence proof.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import platform
from pathlib import Path
from fractions import Fraction as Q
import sympy as sp
import mpmath as mp

PARENT = "7410fa94786ffe43c74ade1e4dc00ee2ce355127"


def curvature(g: sp.Matrix, x: tuple) -> tuple:
    n = len(x)
    inv = g.inv()
    ch = [[[sp.simplify(sum(inv[a, d] *
              (sp.diff(g[d, c], x[b]) + sp.diff(g[d, b], x[c])
               - sp.diff(g[b, c], x[d])) for d in range(n)) / 2)
            for c in range(n)] for b in range(n)] for a in range(n)]
    ric = sp.Matrix(n, n, lambda a, b: sp.simplify(sum(
        sp.diff(ch[c][a][b], x[c]) - sp.diff(ch[c][a][c], x[b])
        + sum(ch[c][c][d]*ch[d][a][b] - ch[c][b][d]*ch[d][a][c]
              for d in range(n)) for c in range(n))))
    scal = sp.simplify(sp.trace(inv * ric))
    return inv, ch, ric, scal, sp.simplify(ric - scal*g/2)


def geometry() -> dict:
    t, psi, r, z = x = sp.symbols("t psi r z", real=True)
    f, q = sp.Function("f")(r), sp.Function("q")(t)
    F = f-q
    g = sp.Matrix([[0,-1,0,0],[-1,F,0,0],[0,0,1,0],[0,0,0,1]])
    inv, ch, ric, scal, ein = curvature(g, x)
    target = sp.diag(0, -sp.diff(f,r,2)/2, sp.diff(q,t,2)/2,
                     sp.diff(q,t,2)/2)
    assert ein == target and sp.simplify(g.det()+1) == 0
    assert sp.simplify(scal+sp.diff(q,t,2)) == 0
    mixed = inv * ein
    for nu in range(4):
        div = sum(sp.diff(mixed[mu,nu],x[mu])
                  +sum(ch[mu][mu][a]*mixed[a,nu]
                       -ch[a][mu][nu]*mixed[mu,a] for a in range(4))
                  for mu in range(4))
        assert sp.simplify(div) == 0
    # Initial constraints at q=t. K convention: K=-Lie_N(h)/2.
    f1, f2 = sp.diff(f,r), sp.diff(f,r,2)
    A = f-t
    h = sp.diag(A,1,1)
    K = sp.Matrix([[sp.sqrt(A)/2,f1/(2*sp.sqrt(A)),0],
                   [f1/(2*sp.sqrt(A)),0,0],[0,0,0]])
    R3 = -f2/A+f1*f1/(2*A*A)
    hc = sp.simplify(R3 + sp.trace(h.inv()*K)**2
                     - sp.trace(h.inv()*K*h.inv()*K))
    assert sp.simplify(hc+f2/A) == 0
    hinv = h.inv()
    hx = (psi,r,z)
    hch = [[[sp.simplify(sum(hinv[i,l]*(sp.diff(h[l,k],hx[j])
              +sp.diff(h[l,j],hx[k])-sp.diff(h[j,k],hx[l]))
              for l in range(3))/2) for k in range(3)]
              for j in range(3)] for i in range(3)]
    S = hinv*K-sp.eye(3)*sp.trace(hinv*K)
    momentum = []
    for i in range(3):
        expr = sum(sp.diff(S[j,i],hx[j]) + sum(
            hch[j][j][l]*S[l,i]-hch[l][j][i]*S[j,l]
            for l in range(3)) for j in range(3))
        momentum.append(sp.simplify(expr))
    assert sp.simplify(momentum[0]-f2/(2*sp.sqrt(A))) == 0
    assert momentum[1:] == [0,0]
    # The source is DIAGNOSED, not manufactured by defining physical T=G/8piG.
    u = sp.symbols("u", positive=True)
    signed = sp.integrate((1-2*u)/sp.sqrt(1+u),(u,0,1))
    absolute = (sp.integrate((1-2*u)/sp.sqrt(1+u),(u,0,sp.Rational(1,2)))
                -sp.integrate((1-2*u)/sp.sqrt(1+u),(u,sp.Rational(1,2),1)))
    assert sp.simplify(signed-(-14+10*sp.sqrt(2))/3) == 0
    assert sp.simplify(absolute-(4*sp.sqrt(6)-(14+10*sp.sqrt(2))/3)) == 0
    return {"metric":str(g), "determinant":"-1", "inverse_tt":str(inv[0,0]),
            "Einstein_tensor":str(ein), "scalar_curvature":str(scal),
            "div_Einstein":"0 in all four components",
            "Hamiltonian_lhs":str(hc), "momentum_lhs":[str(v) for v in momentum],
            "required_rho_at_q_t":"-f''/(16*pi*G*(f-t))",
            "initial_absolute_budget_factor":str(sp.simplify(absolute)),
            "initial_signed_energy_factor":str(sp.simplify(-signed)),
            "budget_convention":"Lambda=0 Einstein-tensor diagnostic, not actual RSET or a prepared source",
            "switch_pressure":"q''/(16*pi*G), uniform on both noncompact ends"}


def equations_and_repairs() -> dict:
    F, Ft, Fr, pt, pp, pr, pz = sp.symbols("F Ft Fr pt pp pr pz", real=True)
    H = -pt*pp-F*pt**2/2+(pr**2+pz**2)/2
    assert sp.diff(H,pt) == -pp-F*pt
    assert -sp.diff(H,F)*Fr == Fr*pt**2/2
    # Hamiltonian: psi_dot=-p_t; d log|p_t|/d psi=-F_t/2.
    assert sp.simplify((Ft*pt**2/2)/(-pt)/pt+Ft/2) == 0
    a,b,R,Rd = sp.symbols("a b R Rd", positive=True)
    C = b*b-a*a*R*R
    wall = sp.Matrix([[1+Rd*Rd,b,0],[b,C,0],[0,0,1]])
    assert sp.simplify(wall.det()-((1+Rd*Rd)*C-b*b)) == 0
    material = sp.Matrix([1,-1/b,0])
    assert sp.simplify((material.T*wall*material)[0]-(Rd**2-a*a*R*R/(b*b))) == 0
    # Moving Grant wall at R=b/a, with theta of period 1.
    Fdot = -2*a*a*R*Rd
    kappa = sp.simplify(-Fdot/(2*b)).subs(R,b/a)
    assert sp.simplify(kappa-a*Rd) == 0
    # Smooth, positive conformal factors only reparameterize null Hamilton flow.
    O, p = sp.symbols("Omega p", positive=True)
    dO, dH = sp.symbols("dOmega dH")
    conf = dH/O**2-2*H*dO/O**3
    assert sp.simplify(conf.subs(pp,(-F*pt**2+pr**2+pz**2)/(2*pt))-dH/O**2) == 0
    return {"Hamiltonian":str(H), "log_covector_derivative":"-F_t/2",
            "radial_covector_derivative":"F_r*p_t^2/2",
            "front_equations":["r''+r'/2=f'(r)/2", "t'+t/2=(f(r)+r'^2)/2"],
            "return_p_t_multiplier":"exp(1/2)",
            "Grant_wall_determinant":str(sp.factor(wall.det())),
            "Grant_material_norm":str(sp.simplify((material.T*wall*material)[0])),
            "Grant_wall_kappa_at_crossing":"a*R_dot",
            "front_wall_kappa_at_crossing":"(f'(R)*R_dot-q')/2",
            "conformal_repair":"same null cotangent orbits; multiplier not removed",
            "smooth_potential_repair":"lower order; same characteristic set and propagation",
            "echo_repair":"canceling integral F_t does not cancel a strictly negative radial kick"}


def exp_half_bounds(n: int = 70) -> tuple[Q,Q]:
    term = Q(1); value = Q(1)
    for j in range(1,n+1):
        term /= 2*j
        value += term
    first = term/(2*(n+1))
    return value, value+first/(1-Q(1,2*(n+2)))


def certificate() -> dict:
    lo,hi = exp_half_bounds()
    assert Q(8,5)<lo<hi<Q(5,3)
    dr = Q(1,442368)
    dv = Q(5,221184)
    err = dr/4+Q(1,5308416)+dv*(Q(1,6)+dv)
    def center(e: Q) -> Q:
        return Q(7,16)+e/(64*(e-1)**2)
    # center is decreasing for e>1.
    tl,th = center(hi)-err,center(lo)+err
    assert Q(49,100)<tl<th<Q(51,100)
    assert hi-lo<Q(1,10**100)
    # Dirichlet inverse norm <=1/6, source derivative Lipschitz <=1/8.
    contraction = Q(1,48)
    assert contraction<1
    jlower=Q(17,24)
    detlower=Q(17,64)
    assert jlower*Q(3,8)==detlower
    return {"method":"analytic maximum principle + contraction; exp series uses rational tail",
            "exp_half":[str(lo),str(hi)],
            "r_range":["0","1/48"], "Dirichlet_inverse_bound":"1/6",
            "contraction":str(contraction),
            "r_minus_first_iterate_bound":str(dr),
            "rprime_minus_first_iterate_bound":str(dv),
            "t0_error_bound":str(err), "t0_interval":[str(tl),str(th)],
            "t_entire_curve_range":["95/192","313/576"],
            "shooting_r_derivative_lower":str(jlower),
            "shooting_2by2_abs_det_lower":str(detlower),
            "metric_perturbation_scope":"an open C2 neighborhood exists; no numerical radius claimed"}


def numerical_bvp(steps: int) -> dict:
    # Independent of the certificate: RK4 + shooting, for diagnostics only.
    with mp.workdps(45):
        dt = mp.mpf(1)/steps
        def rhs(y):
            r,v,j,h,s = y
            f=1/(1+mp.exp(r)); fp=-f*(1-f); fpp=f*(1-f)*(1-2*f)
            return mp.matrix([v,(fp-v)/2,h,(fpp*j-h)/2,(f+v*v-s)/2])
        def evolve(v0):
            y=mp.matrix([0,v0,0,1,0])
            for _ in range(steps):
                k1=rhs(y); k2=rhs(y+dt*k1/2); k3=rhs(y+dt*k2/2); k4=rhs(y+dt*k3)
                y += dt*(k1+2*k2+2*k3+k4)/6
            return y
        v0=mp.mpf('0.0677')
        for _ in range(7):
            y=evolve(v0)
            v0-=y[0]/y[2]
        y=evolve(v0)
        t0=y[4]/(1-mp.exp(-mp.mpf(1)/2))
        return {"steps":steps,"rprime0":mp.nstr(v0,30),"rprime1":mp.nstr(y[1],30),
                "t0":mp.nstr(t0,30),"radial_return_residual":mp.nstr(y[0],8),
                "shooting_r_derivative":mp.nstr(y[2],25),
                "endpoint_radial_covector_change":mp.nstr(mp.exp(mp.mpf(1)/2)*y[1]-v0,25)}


def build() -> dict:
    geom=geometry(); eq=equations_and_repairs(); cert=certificate()
    rows=[numerical_bvp(n) for n in (64,128,256)]
    tl,th=map(Q,cert["t0_interval"])
    for row in rows:
        assert tl<Q(row["t0"])<th
        assert Q(row["endpoint_radial_covector_change"])<0
    changes=[Q(rows[i+1]["t0"])-Q(rows[i]["t0"]) for i in (0,1)]
    assert changes[0]>0 and changes[1]>0 and 15<changes[0]/changes[1]<17
    return {"schema":"chronology-dynamic-front-v1","parent_sha":PARENT,
            "python":platform.python_version(),"sympy":sp.__version__,"mpmath":mp.__version__,
            "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "geometry":geom,"equations_and_repairs":eq,"certificate":cert,"diagnostics":rows,
            "implemented_checks":"passed", "formation_geometry_constructed":True,
            "standard_global_Hadamard_bisolution_excluded":True,
            "physical_formation_solution_found":False,"universal_no_go":False,
            "not_certified":["physical source realization","finite preparation","initial total RSET energy",
                             "self-consistent SCEE evolution","interacting/UV theories","numerical C2 stability radius"]}


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args(); out=build(); text=json.dumps(out,indent=2,ensure_ascii=False)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding="utf-8")
    print(text,end="")

if __name__ == "__main__":
    main()
