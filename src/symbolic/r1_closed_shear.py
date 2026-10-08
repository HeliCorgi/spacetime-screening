#!/usr/bin/env python3
"""Closed Maxwell/pair-fluid shear: exact identities and linear diagnostics.

Scope: constraint-satisfying initial data, inviscid first variation on a
radiation FLRW background, and a positive-viscosity *linear* relaxation sector.
This is NOT a nonlinear viscous Einstein solver or a certified nonlinear gate.
No prescribed external current, new dependency, or weakened legacy test is used.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
from pathlib import Path
from typing import Any

import mpmath as mp
import sympy as sp

PARENT = "0ab94331d8aef62148acac1d89e3235979e6ea83"


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def check_constraints() -> dict[str, Any]:
    eps, y, k, e0, GN = sp.symbols("epsilon y k e0 G", positive=True)
    electric = eps * sp.sin(k*y)
    each = e0-electric**2/4
    rho = 2*each+electric**2/2
    H2 = 16*sp.pi*GN*e0/3
    require(sp.simplify(rho-2*e0) == 0, "constant total normal energy")
    require(sp.simplify(6*H2-16*sp.pi*GN*rho) == 0, "Hamiltonian constraint")
    # Initially fluid velocities and magnetic field vanish. K=-H h is constant.
    x = sp.symbols("x", real=True)
    require(sp.diff(electric, x) == 0, "Maxwell electric Gauss constraint")
    require(sp.simplify(-sp.diff(electric,y)+eps*k*sp.cos(k*y)) == 0,
            "non-potential electric field")
    # An uncompensated electric field violates the SAME fixed-H constraint.
    bad = sp.simplify(6*H2-16*sp.pi*GN*(2*e0+electric**2/2))
    require(sp.simplify(bad+8*sp.pi*GN*electric**2) == 0 and bad != 0,
            "uncompensated-source negative control")
    require(sp.simplify((each.subs({e0:sp.Rational(3,4),eps:1,
                                  y:sp.pi/2,k:1}))) > 0,
            "strictly positive fluid density control")
    require(each.subs({e0:sp.Rational(3,4),eps:2,y:sp.pi/2,k:1}) < 0,
            "reject over-energetic initial electric field")
    return {"each_fluid_energy": str(each), "rho_total": str(rho.expand().simplify()),
            "H_squared": str(H2), "Hamiltonian": "0", "momentum": "0",
            "Gauss_E": "0", "Gauss_B": "0", "net_charge": "0",
            "strict_positivity_condition": "epsilon^2 < 4 e0",
            "initial_slice_energy": "2 e0 L^3 (includes Maxwell and both fluids)",
            "uncompensated_residual": str(bad)}


def check_background_and_principal_parts() -> dict[str, Any]:
    eta, H, e0, GN = sp.symbols("eta H e0 G", positive=True)
    a = 1+H*eta
    rho = 2*e0/a**4
    hubble = sp.diff(a,eta)/a**2
    constraint = (3*hubble**2-8*sp.pi*GN*rho).subs(H**2,16*sp.pi*GN*e0/3)
    require(sp.simplify(constraint) == 0, "radiation FLRW Friedmann equation")
    require(sp.diff(a,eta,2) == 0, "radiation acceleration equation in conformal time")
    # Lorentz-force scaling in the transverse radiation Euler equation.
    # w=a^-4 w0, n=a^-3 n0, E_phys=a^-2 E, d/dt=a^-1 d/deta.
    require(sp.simplify(a**(-3)*a**(-2)/(a**(-4)*a**(-1))-1) == 0,
            "conformal transverse force scaling")
    lam, nx, ny, nz = sp.symbols("lambda nx ny nz", real=True)
    cs = sp.sqrt(sp.Rational(1,3))
    principal = sp.Matrix([[0,cs*nx,cs*ny,cs*nz],
                           [cs*nx,0,0,0], [cs*ny,0,0,0], [cs*nz,0,0,0]])
    require(principal == principal.T, "rest-frame Euler principal symmetry")
    expected = lam**2*(lam**2-(nx**2+ny**2+nz**2)/3)
    require(sp.factor((lam*sp.eye(4)-principal).det()-expected) == 0,
            "Euler sound and transport characteristics")
    require(sp.simplify(-1/a**2) < 0, "background time covector timelike")
    # Charge conjugation plus opposite velocities cancels first-order T^{0x}.
    w, v = sp.symbols("w v")
    require(w*v+w*(-v) == 0, "first order total momentum cancellation")
    return {"background": "g0=a^2(-deta^2+dx^2+dy^2+dz^2), a=1+H0 eta",
            "H0_squared": "16 pi G e0/3", "fluid_sound_speed_squared": "1/3",
            "Euler_characteristic_polynomial": str(expected),
            "Maxwell_and_gravity_characteristics": "null; derived in note, not kernel formalized",
            "metric_first_variation": "0 for the symmetric initial family",
            "nonlinear_Einstein_evolution_executed": False}


def check_linear_modes() -> dict[str, Any]:
    t = sp.symbols("eta", real=True)
    k, Q, w, E0 = sp.symbols("k Q w E0", positive=True)
    om = sp.sqrt(k*k+2*Q*Q/w)
    v = Q*E0/(w*om)*sp.sin(om*t)
    E = E0*sp.cos(om*t)
    B = k*E0/om*sp.sin(om*t)
    d = Q*E0/(w*om**2)*(1-sp.cos(om*t))
    for residual in [sp.diff(v,t)-Q*E/w, sp.diff(E,t)+k*B+2*Q*v,
                     sp.diff(B,t)-k*E, sp.diff(d,t)-v]:
        require(sp.simplify(residual) == 0, "closed modal equation")
    energy = (E**2+B**2)/4+w*v**2/2
    require(sp.simplify(energy-E0**2/4) == 0, "positive closed wave energy")
    end = sp.pi/om
    require(sp.simplify(v.subs(t,end)) == 0, "inviscid endpoint velocity")
    require(sp.simplify(d.subs(t,end)-2*Q*E0/(w*om**2)) == 0, "nonzero shear displacement")
    # A frozen prescribed E is not Maxwell's dynamical solution.
    frozen_defect = -2*Q*(Q*E0*t/w)-k*(k*E0*t)
    require(frozen_defect != 0, "frozen-driver negative control")
    return {"Omega_squared": str(om**2), "v": str(v), "E": str(E), "B": str(B),
            "displacement": str(d), "wave_energy": "E0^2/4 per coordinate volume, times epsilon^2",
            "gate_end": "pi/Omega", "endpoint_displacement": "2 epsilon Q E0/(w Omega^2) sin(k y)",
            "frozen_E_Maxwell_defect": str(frozen_defect),
            "scope": "exact first variation, not exact finite-amplitude solution"}


def check_relaxation() -> dict[str, Any]:
    v,E,B,p,k,Q,w,mu,tau = sp.symbols("v E B p k Q w mu tau", real=True)
    state = sp.Matrix([v,E,B,p])
    rhs = sp.Matrix([Q*E/w+k*p/w, -k*B-2*Q*v, k*E, -(p+mu*k*v)/tau])
    energy = (E**2+B**2)/4+w*v**2/2+tau*p**2/(2*mu)
    denergy = sum(sp.diff(energy,state[i])*rhs[i] for i in range(4))
    require(sp.simplify(denergy+p**2/mu) == 0, "relaxation dissipation with dynamic driver")
    values = {w:1, Q:1, k:1, mu:sp.Rational(1,1000), tau:sp.Rational(1,100)}
    ct = sp.simplify((mu/(tau*w)).subs(values))
    cl = sp.Rational(1,3)+sp.Rational(4,3)*ct
    require(ct == sp.Rational(1,10) and cl == sp.Rational(7,15), "strict linear causal speeds")
    require(0 < ct < 1 and 0 < cl < 1, "linear causal margins")
    bad = sp.Rational(1,3)+sp.Rational(4,3)*sp.Rational(1,1000)/sp.Rational(1,10000)
    require(bad > 1, "reject too-short relaxation at fixed viscosity")
    # The loss must heat a thermodynamic variable; an isentropic EOS is insufficient.
    strain, ds, n, temperature = sp.symbols("strain ds n temperature", real=True)
    production = sp.simplify(-(-2*mu*strain)*strain)
    require(production == 2*mu*strain**2 and production != 0,
            "isentropic-viscous-completion negative control")
    return {"matrix": str(rhs.jacobian(state).subs(values)),
            "energy": str(energy), "d_energy": "-p^2/mu",
            "c_transverse_squared": str(ct), "c_longitudinal_squared": str(cl),
            "mu": "1/1000", "tau": "1/100", "w": "1", "Q": "1", "k": "1",
            "nonlinear_viscous_causality_proved": False,
            "isentropic_completion_defect": str(production),
            "thermodynamic_requirement": "n Temperature D entropy = -pi:sigma; include relaxation entropy storage"}


def check_exact_entropy_completion() -> dict[str, Any]:
    """Contracted nonlinear original-IS entropy identity; not hyperbolicity."""
    e,n,theta,c,K,mu,tau,temp = sp.symbols("e n theta pi_sigma pi_squared mu tau Temperature", real=True)
    de = -sp.Rational(4,3)*e*theta-c
    dn = -n*theta
    log_coefficient_rate = sp.simplify(dn/n-2*de/e)
    require(sp.simplify(log_coefficient_rate-sp.Rational(5,3)*theta-2*c/e)==0,
            "nonlinear coefficient derivative from thermodynamics")
    b = tau/(4*mu*temp)
    dK = -2*K/tau-4*mu*c/tau-(theta+log_coefficient_rate)*K
    divergence = -c/temp-b*dK-b*(theta+log_coefficient_rate)*K
    require(sp.simplify(divergence-K/(2*mu*temp))==0, "exact entropy production")
    # Deleting the cubic pi*(pi:sigma) term spoils this exact entropy identity.
    truncated_dK = -2*K/tau-4*mu*c/tau-sp.Rational(8,3)*theta*K
    defect = sp.factor(-c/temp-b*truncated_dK-b*(theta+log_coefficient_rate)*K-K/(2*mu*temp))
    require(sp.simplify(defect+tau*K*c/(2*mu*temp*e))==0 and defect!=0,
            "omitted nonlinear entropy-term negative control")
    return {"EOS":"e=kappa n^(4/3) exp(s-s0), p=e/3, Temperature=e/n",
            "transport":"tau=tau0 (e/e0)^(-1/4), mu=mu0 (e/e0)^(3/4)",
            "constitutive_equation":"tau Delta D pi + pi = -2 mu sigma -(4/3) tau theta pi -(tau/e)(pi:sigma) pi",
            "entropy_current":"[n s - tau pi:pi/(4 mu Temperature)] u",
            "entropy_divergence":"pi:pi/(2 mu Temperature) >= 0",
            "truncated_entropy_defect":str(defect),
            "scope":"covariant candidate specified, entropy algebra checked; nonlinear principal estimates pending"}


def check_nonlinear_rest_symbol() -> dict[str, Any]:
    """A finite-matrix lemma for the specified entropy-completed shear law.

    This does not replace a common-gauge nonlinear Einstein-matter estimate.
    Normalize w=1, hence e=3/4, and rotate the wave direction to (1,0,0).
    """
    p,q,r,s,t,alpha = sp.symbols("p q r s t alpha", real=True, nonzero=True)
    pi=sp.Matrix([[p,q,r],[q,s,t],[r,t,-p-s]])
    I=sp.eye(3); direction=sp.Matrix([1,0,0]); M=I+pi
    velocity=sp.Matrix(sp.symbols("v0:3", real=True))
    theta=(direction.T*velocity)[0]
    sigma=(direction*velocity.T+velocity*direction.T)/2-I*theta/3
    contraction=sp.trace(pi*sigma)
    stress_rate=2*alpha*sigma+sp.Rational(4,3)*pi*theta+sp.Rational(4,3)*pi*contraction
    energy_rate=theta+contraction
    B=sp.Matrix([energy_rate,stress_rate[0,0],stress_rate[1,1],
                 stress_rate[0,1],stress_rate[0,2],stress_rate[1,2]]).jacobian(velocity)
    D=sp.Matrix([[sp.Rational(1,3),1,0,0,0,0],[0,0,0,1,0,0],[0,0,0,0,1,0]])
    A=sp.simplify(D*B)
    pn=pi*direction
    target=alpha*I+(1+alpha)/3*direction*direction.T+direction*pn.T/3+sp.Rational(4,3)*pn*direction.T+sp.Rational(4,3)*pn*pn.T
    require(sp.simplify(A-target)==sp.zeros(3), "derive acoustic block from constitutive tensor")
    # H = M - (3/(4 alpha)) M n n^T M, L=M^-1 A. Verify H L without an inverse.
    HL=sp.simplify((I-sp.Rational(3,4)/alpha*M*direction*direction.T)*A)
    require(sp.simplify(HL-HL.T)==sp.zeros(3), "indefinite acoustic symmetrizer identity")
    delta=sp.Rational(1,1000); a=sp.Rational(1,10); c=3/(4*a)
    lambdaL=sp.Rational(7,15); radius=(lambdaL-a)/3
    defect=sp.simplify(((sp.Rational(5,3)+lambdaL)*delta+sp.Rational(4,3)*delta**2)/(1-delta))
    proj=sp.simplify(defect/(radius-defect))
    Hdef=sp.simplify(delta+c*(2*delta+delta**2))
    positive=sp.simplify(1-c*proj**2-Hdef)
    negative=sp.simplify(1-c+c*proj**2+Hdef)
    require(0<defect<radius and a-defect>0 and lambdaL+defect<1,
            "strictly causal separated acoustic clusters")
    require(positive>sp.Rational(98,100) and negative<-sp.Rational(648,100),
            "definite signatures on spectral subspaces")
    require((1+4*delta)/3<1 and delta**2/a<sp.Rational(1,2),
            "dominant-energy and entropy-density tube margins")
    return {"normalized_stress_condition":"operator_norm(pi/w) <= 1/1000",
            "alpha":"1/10", "acoustic_defect_bound":str(defect),
            "projector_difference_bound":str(proj), "H_difference_bound":str(Hdef),
            "transverse_signature_lower":str(positive), "longitudinal_signature_upper":str(negative),
            "speed_squared_lower":str(a-defect),"speed_squared_upper":str(lambdaL+defect),
            "identity":"H L = L^T H; positive symmetrizer via separated definite clusters",
            "DEC_pressure_over_energy_upper":str((1+4*delta)/3),
            "entropy_storage_over_n_upper":str(delta**2/a),
            "scope":"frozen rest-frame principal-symbol lemma; common-slice coupled PDE certification not claimed"}


def numeric_diagnostics(dps: int) -> dict[str, Any]:
    """mpmath values are diagnostics; uniform bounds have a separate exact proof."""
    with mp.workdps(dps):
        mu, tau = mp.mpf(1)/1000, mp.mpf(1)/100
        mat = mp.matrix([[0,1,0,1,0],[-2,0,-1,0,0],[0,1,0,0,0],
                         [-mu/tau,0,0,-1/tau,0],[1,0,0,0,0]])
        om = mp.sqrt(3); T = mp.pi/om
        step = mp.expm(mat*T/256)
        z = mp.matrix([0,1,0,0,0])
        max_v = mp.mpf(0); max_dt = mp.mpf(0)
        for j in range(257):
            t = T*j/256
            vr = mp.sin(om*t)/om
            dvr = mp.cos(om*t)
            max_v = max(max_v,abs(z[0]-vr)*om)
            max_dt = max(max_dt,abs(z[1]+z[3]-dvr))
            if j < 256:
                z = step*z
        direct = mp.expm(mat*T)*mp.matrix([0,1,0,0,0])
        require(max(abs(direct[i]-z[i]) for i in range(5)) < mp.mpf(10)**(-dps+10),
                "semigroup/direct expm agreement")
        Qend = (z[1]**2+z[2]**2)/4+z[0]**2/2+tau*z[3]**2/(2*mu)
        loss = mp.mpf(1)/4-Qend
        require(loss>0, "positive wave-energy transfer to heat")
        require(max_v < mp.mpf(13)/5000 and max_dt < mp.mpf(13)/5000,
                "sample checks consistent with separate uniform bound")
        require(abs(z[4]-mp.mpf(2)/3)/(mp.mpf(2)/3) < mp.mpf(9)/5000,
                "displacement diagnostic")
        return {"dps":dps, "T":mp.nstr(T,35),
                "endpoint_order":"v,E,B,pi_xy,displacement",
                "endpoint":[mp.nstr(value,35) for value in z],
                "sample_relative_v_error":mp.nstr(max_v,25),
                "sample_scaled_dt_error":mp.nstr(max_dt,25),
                "wave_energy_to_heat":mp.nstr(loss,25),
                "relative_displacement_error":mp.nstr(abs(z[4]-mp.mpf(2)/3)/(mp.mpf(2)/3),25),
                "samples_are_not_uniform_proof":True}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    low, high = numeric_diagnostics(50), numeric_diagnostics(80)
    with mp.workdps(45):
        require(max(abs(mp.mpf(a)-mp.mpf(b)) for a,b in zip(low["endpoint"],high["endpoint"]))
                < mp.mpf("1e-33"), "50/80 digit agreement")
    result = {"schema":"r1-closed-shear-v1", "parent_sha":PARENT,
              "python":platform.python_version(), "sympy":sp.__version__,
              "mpmath":mp.__version__,
              "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "constraints":check_constraints(),
              "background":check_background_and_principal_parts(),
              "inviscid_modes":check_linear_modes(), "relaxation":check_relaxation(),
              "entropy_completion":check_exact_entropy_completion(),
              "nonlinear_rest_symbol":check_nonlinear_rest_symbol(), "diagnostics":high,
              "uniform_linear_bounds":{"relative_scaled_C1":"13/5000", "relative_displacement":"9/5000",
                                       "method":"energy contraction + relaxation integral, proved in note and rational checker"},
              "status":"all implemented checks passed; full R1 remains partial",
              "not_certified":["a concrete nonlinear Einstein-fluid amplitude threshold",
                               "nonlinear positive-viscosity closed-source completion",
                               "a nonlinear GR evolution simulation", "persistent stored gate or arbitrary pulse",
                               "universal computation", "Hadamard/RSET/SCEE", "CTC"]}
    text = json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding="utf-8")
    print(text,end="")


if __name__ == "__main__":
    main()
