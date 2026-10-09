#!/usr/bin/env python3
"""Spatial causality and reset audit of the fixed linear R1 shear system.

Exact algebra and rational stencil checks are separated from numerical mode
convergence. No nonlinear Einstein evolution or universal compiler is certified.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path

import mpmath as mp
import sympy as sp

PARENT = "d679f9585cc89518981ce03f6075bab8fb5256fd"


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def algebra() -> dict:
    w, Q, k, mu, tau = sp.symbols("w Q k mu tau", positive=True)
    lam = sp.symbols("lambda")
    C = sp.Matrix([[0, 0, 0, 1/w], [0, 0, -1, 0],
                   [0, -1, 0, 0], [mu/tau, 0, 0, 0]])
    R = sp.Matrix([[0, Q/w, 0, 0], [-2*Q, 0, 0, 0],
                   [0, 0, 0, 0], [0, 0, 0, -1/tau]])
    H = sp.diag(2*w, 1, 1, 2*tau/mu)
    require(H*C == C.T*H, "spatial symmetrizer")
    require(H*R + R.T*H == sp.diag(0, 0, 0, -4/mu), "local dissipation")
    require(sp.factor((lam*sp.eye(4)-C).det()) ==
            (lam-1)*(lam+1)*(lam**2*tau*w-mu)/(tau*w), "principal cone")

    v, E, B, P = z = sp.Matrix(sp.symbols("v E B P", real=True))
    zy = sp.Matrix(sp.symbols("v_y E_y B_y P_y", real=True))
    q = (z.T*H*z)[0]/2
    flux = (z.T*H*C*z)[0]/2
    qdot = (z.T*H*(-C*zy + R*z))[0]
    flux_y = (z.T*H*C*zy)[0]
    require(sp.expand(qdot+flux_y+2*P**2/mu) == 0, "local flux law")
    for sign in (-1, 1):
        squares = (E-sign*B)**2/2 + w*(v+sign*P/w)**2 + (tau/mu-1/w)*P**2
        require(sp.expand(q+sign*flux-squares) == 0, "cone sum of squares")

    # Sine v,E and cosine B,P must give the EXISTING modal generator.
    A = sp.Matrix([[0, Q/w, 0, k/w], [-2*Q, 0, -k, 0],
                   [0, k, 0, 0], [-mu*k/tau, 0, 0, -1/tau]])
    y = sp.symbols("y", real=True)
    profiles = sp.diag(sp.sin(k*y), sp.sin(k*y), sp.cos(k*y), sp.cos(k*y))
    require(sp.simplify(-C*sp.diff(profiles*z, y)+R*profiles*z-profiles*A*z)
            == sp.zeros(4, 1), "PDE to fixed R1 mode")
    A5 = A.row_join(sp.zeros(4, 1)).col_join(sp.Matrix([[1, 0, 0, 0, 0]]))
    J = sp.Matrix([[w*k, 0, -Q, tau*k*k, mu*k**3]])
    require(sp.simplify(J*A5) == sp.zeros(1, 5), "displacement invariant")

    polynomial = sp.Poly(sp.expand(tau*w*(lam*sp.eye(4)-A).det()), lam)
    a4, a3, a2, a1, a0 = polynomial.all_coeffs()
    delta2 = sp.factor(a3*a2-a4*a1)
    delta3 = sp.factor(a3*a2*a1-a4*a1*a1-a3*a3*a0)
    require(delta2 == mu*w*k**2, "Hurwitz minor 2")
    require(delta3 == 2*mu*w*Q**2*k**2, "Hurwitz minor 3")
    require(a0 == mu*k**4, "strict k != 0 requirement")

    # Derive the spatial invariant independently with local derivative jets.
    vt_y, Bt, Pt_yy, dt_yyy = Q*zy[1]/w-sp.Symbol("P_yy")/w, zy[1], \
        (-sp.Symbol("P_yy")-mu*sp.Symbol("v_yyy"))/tau, sp.Symbol("v_yyy")
    require(sp.expand(w*vt_y-Q*Bt-tau*Pt_yy-mu*dt_yyy) == 0,
            "local third-derivative invariant")

    # Nonzero retained displacement at an almost-reset endpoint needs a residue.
    radius = sp.Rational(1, 10**6)
    bound = (1+1+sp.Rational(1, 100))*radius/sp.Rational(1, 1000)
    require(bound == sp.Rational(201, 100000), "quantitative reset bound")
    require(bound < sp.Rational(3, 5), "requested reset and d>=0.6 are incompatible")
    # Cauchy-Schwarz lower bound on remaining modal wave/storage energy.
    denominator = 2*w*k**2+4*Q**2+2*mu*tau*k**4
    d = sp.symbols("d", real=True)
    energy_floor = mu**2*k**6*d**2/denominator
    require(sp.simplify(denominator -
            ((w*k)**2/(w/2)+Q**2/sp.Rational(1,4)+(tau*k*k)**2/(tau/(2*mu)))) == 0,
            "remaining modal energy bound")

    # An initially localized electric perturbation can satisfy the same initial
    # GR constraints, but this does not solve its nonlinear subsequent evolution.
    e0, eps, chi, G = sp.symbols("e0 epsilon chi G", positive=True)
    density = 2*(e0-eps**2*chi**2/4)+eps**2*chi**2/2
    require(sp.expand(density-2*e0) == 0, "localized initial compensation")
    require(sp.expand(6*(16*sp.pi*G*e0/3)-16*sp.pi*G*density) == 0,
            "localized Hamiltonian constraint")

    # Wrong current sign breaks closed-system energy conservation.
    wrong = R.copy(); wrong[1, 0] = 2*Q
    require(sp.simplify(H*wrong+wrong.T*H-sp.diag(0,0,0,-4/mu)) != sp.zeros(4),
            "wrong-current negative control")
    require((q+flux).subs({w:1,mu:2,tau:1,v:1,P:-1,E:0,B:0}) < 0,
            "superluminal transverse coefficients rejected by cone test")
    require(J[4].subs(mu,0) == 0, "no division by viscosity in the inviscid control")
    require(sp.factor(polynomial.as_expr().subs(Q, 0)) ==
            (k*k+lam*lam)*(k*k*mu+lam*lam*tau*w+lam*w), "Q=0 undamped Maxwell control")
    require(sp.simplify(polynomial.as_expr().subs({k:0, lam:0})) == 0,
            "zero mode not strictly damped")
    return {
        "equations": "w*v_t=Q*E-P_y; E_t=B_y-2Q*v; B_t=E_y; tau*P_t=-P-mu*v_y",
        "H": str(H), "flux": str(sp.expand(flux)),
        "energy_law": "q_t + flux_y = -2*P^2/mu",
        "cone_condition": "w,mu,tau>0 and mu<=tau*w; transverse sector only",
        "modal_invariant_coefficients": [str(c) for c in J],
        "benchmark_normalized_invariant": ["1000", "0", "-1000", "10", "1"],
        "hurwitz_delta2": str(delta2), "hurwitz_delta3": str(delta3),
        "spatial_invariant": "w*v_y-Q*B-tau*P_yy-mu*d_yyy",
        "reset_radius": str(radius), "reset_displacement_bound": str(bound),
        "retained_target": "3/5", "remaining_energy_floor": str(energy_floor),
        "asymptotic_scope": "fixed k,Q,w,mu,tau>0, initial (v,E,B,P,d)=(0,1,0,0,0): d(t)->0 in this linear model",
        "nonlinear_R1_certified": False,
    }


def exact_local_stencil() -> dict:
    """A rational, local light-cone stencil with separate numerical dissipation."""
    C = sp.Matrix([[0,0,0,1], [0,0,-1,0], [0,-1,0,0], [sp.Rational(1,10),0,0,0]])
    R = sp.Matrix([[0,1,0,0], [-2,0,0,0], [0,0,0,0], [0,0,0,-100]])
    H = sp.diag(2,1,1,20)
    h = sp.Rational(1,8)
    delta = h/2
    S = (sp.eye(4)-delta*R/2).inv()*(sp.eye(4)+delta*R/2)
    left, right = (sp.eye(4)+C)/2, (sp.eye(4)-C)/2
    N, center = 33, 16
    state = [sp.zeros(4,1) for _ in range(N)]
    state[center][1] = 1  # Deliberately a grid impulse, not smooth continuum data.
    def energy(u: list) -> sp.Rational:
        return sp.expand(h*sum((x.T*H*x)[0]/2 for x in u))
    def source(u: list) -> tuple[list, sp.Rational]:
        out = [S*x for x in u]
        heat = h*sum(2*delta*1000*((x[3]+y[3])/2)**2 for x,y in zip(u,out))
        require(energy(u)-energy(out)-heat == 0, "exact local source heat")
        return out, heat
    initial = energy(state)
    heat_total = sp.S.Zero
    diffusion_total = sp.S.Zero
    rows = []
    for step in range(1,7):
        state, heat = source(state); heat_total += heat
        before = energy(state)
        state = [left*state[(j-1)%N]+right*state[(j+1)%N] for j in range(N)]
        loss = before-energy(state)
        require(loss >= 0, "transport is H-contracting")
        diffusion_total += loss
        state, heat = source(state); heat_total += heat
        for j, value in enumerate(state):
            if abs(j-center) > step:
                require(value == sp.zeros(4,1), "outside discrete light cone exactly zero")
        balance = energy(state)+heat_total+diffusion_total-initial
        require(balance == 0, "field+physical heat+NUMERICAL diffusion balance")
        rows.append({"step":step, "time":str(step*h), "cone_radius_cells":step,
                     "balance":"0", "outside_cone":"exactly zero"})
    return {"grid_cells":N, "dx_dt":str(h), "steps":rows,
            "initial_energy":str(initial), "heat":str(heat_total),
            "numerical_diffusion":str(diffusion_total),
            "scope":"rational grid support and stability, not a smooth nonlinear GR simulation"}


def acausal_midpoint_control() -> dict:
    """An energy-exact centered midpoint update is not a local causal stencil."""
    N = 9
    D = sp.zeros(N)
    for j in range(N):
        D[j,(j+1)%N] = -sp.Rational(1,2)
        D[j,(j-1)%N] = sp.Rational(1,2)
    dt = sp.Rational(1,4)
    M = (sp.eye(N)-dt*D/2).inv()*(sp.eye(N)+dt*D/2)
    require(M.T*M == sp.eye(N), "centered midpoint exact quadratic norm")
    initial = sp.eye(N)[:,0]
    after = M*initial
    require(after[3] != 0, "spacelike numerical leakage must be detected")
    return {"grid_cells":N, "dx":"1", "dt":str(dt),
            "distance_three_cell_amplitude":str(after[3]),
            "exact_energy_residual":"0", "causal_stencil":False,
            "scope":"discretization negative control; not a failure of continuum Maxwell causality"}


def numerical_diagnostics() -> dict:
    with mp.workdps(70):
        mu, tau = mp.mpf(1)/1000, mp.mpf(1)/100
        A = mp.matrix([[0,1,0,1,0], [-2,0,-1,0,0], [0,1,0,0,0],
                       [-mu/tau,0,0,-1/tau,0], [1,0,0,0,0]])
        initial = mp.matrix([0,1,0,0,0])
        T = mp.pi/mp.sqrt(3)
        modal = []
        for label,t in [("pi/sqrt(3)",T),("2*pi/sqrt(3)",2*T),
                        ("1000",mp.mpf(1000)),("10000",mp.mpf(10000)),
                        ("60000",mp.mpf(60000))]:
            z = mp.expm(A*t)*initial
            residue = z[0]-z[2]+tau*z[3]+mu*z[4]
            require(abs(residue) < mp.mpf("1e-50"), "augmented exponential invariant")
            modal.append({"time":label, "v":mp.nstr(z[0],30), "B":mp.nstr(z[2],30),
                          "P":mp.nstr(z[3],30), "d":mp.nstr(z[4],30),
                          "invariant_residual":mp.nstr(abs(residue),8)})
        require(mp.mpf("0.6662") < mp.mpf(modal[0]["d"]) < mp.mpf("0.6663"),
                "unchanged first gate benchmark")

        # Convergence of the local scheme, not a spatial Fourier ODE masquerading
        # as a causal support test. The exact stencil was checked separately.
        wave = mp.pi/4  # L=8, one sine period; physical time T=1.
        A4 = mp.matrix([[0,1,0,wave],[-2,0,-wave,0],[0,wave,0,0],
                        [-mu*wave/tau,0,0,-1/tau]])
        R = mp.matrix([[0,1,0,0],[-2,0,0,0],[0,0,0,0],[0,0,0,-1/tau]])
        ref = mp.expm(A4)*mp.matrix([0,1,0,0])
        convergence = []
        errors = []
        for N in (64,128,256,512):
            h = mp.mpf(8)/N
            S = (mp.eye(4)-h*R/4)**-1*(mp.eye(4)+h*R/4)
            c, sn = mp.cos(wave*h), mp.sin(wave*h)
            transport = mp.matrix([[c,0,0,sn],[0,c,-sn,0],[0,sn,c,0],[-mu*sn/tau,0,0,c]])
            end = (S*transport*S)**(N//8)*mp.matrix([0,1,0,0])
            error = max(abs(end[j]-ref[j]) for j in range(4))
            errors.append(error)
            convergence.append({"cells":N, "steps":N//8, "max_error":mp.nstr(error,18)})
        ratios = [errors[j]/errors[j+1] for j in range(3)]
        require(all(mp.mpf("1.5") < r < mp.mpf("2.2") for r in ratios),
                "expected first-order local scheme convergence")
        return {"modal_samples":modal, "local_scheme_convergence":convergence,
                "error_ratios":[mp.nstr(x,12) for x in ratios],
                "scope":"numerical linear diagnostics; asymptotic statement is proved algebraically, not from samples"}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {"schema":"r1-causal-reset-v1", "parent_sha":PARENT,
              "python":platform.python_version(), "sympy":sp.__version__, "mpmath":mp.__version__,
              "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "algebra":algebra(), "local_stencil":exact_local_stencil(),
              "negative_midpoint":acausal_midpoint_control(), "diagnostics":numerical_diagnostics(),
              "status":"all implemented checks passed; universal embedding remains D",
              "not_certified":["nonlinear Einstein gate", "finite-time physical preparation",
                               "controller/latch/reset construction", "all-time nonlinear stability",
                               "universal computation", "CTC/Hadamard/RSET/SCEE"]}
    text = json.dumps(result, indent=2, ensure_ascii=False)+"\n"
    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    print(text, end="")


if __name__ == "__main__":
    main()
