"""4D RN interior two-input scattering and non-equilibrium preparation diagnostics.

Standalone: python src/symbolic/sa_two_input_state_v5.py [--output result.json]
No full SA covariance, outside source, or past receiver law is supplied here.
The exact interior scattering theorem is imported from Kehle--Shlapentokh-Rothman
(2019), arXiv:1804.05438, Prop. 3.3 / Thms. 3--5. See the associated v5 note.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import time

import mpmath as mp
import sympy as sp

BASE_SHA = "7724b58b6f571d01c35f6a1ef411aee9d79d62dd"
PRECISIONS = (50, 80)
# A finite-cutoff numerical check, not a mode sum or a complete quantum state.
SCATTERING_CASES = (("0.02", 0), ("0.2", 0), ("2", 0), ("0.2", 1))


def require(ok: bool, message: str) -> None:
    if not ok:
        raise AssertionError(message)


def conv(a, b, n):
    return [sum((a[j] * b[k-j] for j in range(k+1)), mp.mpf(0)) for k in range(n+1)]


def potential_series(center, rp, rm, order):
    """Taylor coefficients for r(s)^4/d^2 and x(1-x), x'=x(1-x)."""
    d = rp-rm
    x = [1/(1+mp.exp(-center))]
    for n in range(order):
        x.append((x[n]-sum((x[j]*x[n-j] for j in range(n+1)), mp.mpf(0)))/(n+1))
    r = [-d*v for v in x]
    r[0] += rp
    r2 = conv(r, r, order)
    r4 = conv(r2, r2, order)
    x2 = conv(x, x, order)
    return [v/d**2 for v in r4], [x[k]-x2[k] for k in range(order+1)]


def taylor_step(y, dy, q, step, order):
    coeff = [y, dy]
    for n in range(order-1):
        coeff.append(-sum((q[j]*coeff[n-j] for j in range(n+1)), mp.mpc(0))/((n+1)*(n+2)))
    out = coeff[-1]
    dout = order*coeff[-1]
    for n in range(order-1, -1, -1):
        out = out*step+coeff[n]
        if n > 0:
            dout = dout*step+n*coeff[n]
    return out, dout


def scattering(dps, half_width=100, step="1", order=120):
    """Propagate the actual neutral 4D l-mode equation between RN horizons.

    phi_ss + [(omega*r^2/d)^2 + l(l+1)*x(1-x)] phi = 0.
    Horizon bases are exp(+-i nu*s)/r_h, so their conserved fluxes coincide.
    Their phases differ by harmless fixed constants from some tortoise conventions.
    """
    with mp.workdps(dps):
        M = mp.mpf(1)
        Q = mp.mpf("0.99")
        delta = mp.sqrt(M*M-Q*Q)
        rp, rm = M+delta, M-delta
        d = rp-rm
        kp, km = d/(2*rp**2), d/(2*rm**2)
        h = mp.mpf(step)
        count = int(2*half_width/h)
        require(mp.almosteq(count*h, 2*half_width), "nonintegral mesh")
        vectors = []
        for wnorm, ell in SCATTERING_CASES:
            w = mp.mpf(wnorm)*kp
            nu = w*rp**2/d
            y = mp.exp(1j*nu*half_width)/rp
            vectors.append([y, -1j*nu*y, w, ell])
        for i in range(count):
            center = -mp.mpf(half_width)+i*h
            a, b = potential_series(center, rp, rm, order-2)
            for vec in vectors:
                w, ell = vec[2:]
                q = [w*w*a[j]+ell*(ell+1)*b[j] for j in range(order-1)]
                vec[0], vec[1] = taylor_step(vec[0], vec[1], q, h, order)
        results = []
        for (wnorm, ell), (phi, phis, w, _) in zip(SCATTERING_CASES, vectors):
            num = w*rm**2/d
            u, us = rm*phi, rm*phis
            T = (u+1j*us/num)*mp.exp(1j*num*half_width)/2
            R = (u-1j*us/num)*mp.exp(-1j*num*half_width)/2
            flux_error = abs(abs(T)**2-abs(R)**2-1)
            require(flux_error < mp.mpf("1e-42"), "pseudo-unitary flux failed")
            # Inverse source for the normalized outgoing target (1,0).
            ia, ib = mp.conj(T), -R
            o1, o2 = T*ia+mp.conj(R)*ib, R*ia+mp.conj(T)*ib
            require(abs(o1-1)+abs(o2) < mp.mpf("1e-42"), "inverse failed")
            # Analytic truncation bound; Taylor roundoff is NOT included in this bound.
            C = 4*w*w*rp**3/d+ell*(ell+1)
            IL = C/(w*rp**2/d)*mp.exp(-half_width)
            IR = C/(w*rm**2/d)*mp.exp(-half_width)
            tail_bound = (abs(T)+abs(R))*mp.expm1(IL+IR)
            results.append({
                "omega_over_kappa_plus": wnorm, "ell": ell,
                "T_re": mp.nstr(T.real, 48), "T_im": mp.nstr(T.imag, 48),
                "R_re": mp.nstr(R.real, 48), "R_im": mp.nstr(R.imag, 48),
                "T_squared": mp.nstr(abs(T)**2, 45),
                "R_squared": mp.nstr(abs(R)**2, 45),
                "inverse_spectral_energy_factor": mp.nstr(abs(T)**2+abs(R)**2, 45),
                "flux_error": mp.nstr(flux_error, 8),
                "analytic_endpoint_error_bound_excluding_ode_error": mp.nstr(tail_bound, 12),
            })
        return {"dps": dps, "Q_over_M": "0.99", "half_width": half_width,
                "step": step, "taylor_order": order, "cases": results}


def exact_algebra():
    T, R, Tc, Rc = sp.symbols("T R Tc Rc")
    S = sp.Matrix([[T, Rc], [R, Tc]])
    Sinv = sp.Matrix([[Tc, -Rc], [-R, T]])
    det = T*Tc-R*Rc
    require(S*Sinv == det*sp.eye(2), "inverse identity")
    p = sp.diag(1, -1)
    Sadj = sp.Matrix([[Tc, Rc], [R, T]])
    require(Sadj*p*S == det*p, "indefinite flux identity")
    # Full 4D spherical reduction. Delta = (r-rp)(r-rm).
    x, d, r, omega, ell = sp.symbols("x d r omega ell", nonzero=True)
    delta = -d*d*x*(1-x)
    r_s = -d*x*(1-x)
    # Multiplying the radial Sturm equation by -x(1-x) gives our oscillator q.
    q_from_sturm = sp.simplify(-x*(1-x)*(omega**2*r**4/delta-ell*(ell+1)))
    q = omega**2*r**4/d**2+ell*(ell+1)*x*(1-x)
    require(sp.simplify(q-q_from_sturm) == 0, "4D radial reduction")
    require(sp.simplify(delta/r_s-d)==0, "radial Sturm momentum")
    # A covariance with support in the moment kernel can be nonzero PSD.
    v = sp.Matrix([1, -1]); L = sp.Matrix([1, 1])
    Sigma = v*v.T
    require((L.T*Sigma*L)[0] == 0 and Sigma != sp.zeros(2), "kernel covariance")
    require(Sigma.eigenvals() == {sp.Integer(0): 1, sp.Integer(2): 1}, "PSD kernel")
    bad = sp.diag(1,-1)
    require((L.T*bad*L)[0] == 0 and min(bad.eigenvals()) < 0,
            "negative covariance false cancellation control")
    return {"checks": ["4D scalar Sturm reduction", "exact inverse scattering algebra",
                        "indefinite flux, not a probability", "nonzero PSD moment-kernel covariance",
                        "indefinite covariance false positive rejected"],
            "all_passed": True}


def pulse_and_state(dps, degrees=(2, 4, 6, 8)):
    """Finite smooth waveforms; an explicit conditional Gaussian state deformation."""
    with mp.workdps(dps):
        zero = mp.mpf(0)
        def h(z):
            return mp.exp(-1/(1-z*z)) if abs(z)<1 else zero
        def hp(z):
            return -2*z*h(z)/(1-z*z)**2 if abs(z)<1 else zero
        def hpp(z):
            return h(z)*(4*z*z/(1-z*z)**4-2/(1-z*z)**2-8*z*z/(1-z*z)**3) if abs(z)<1 else zero
        panels = [-1, -mp.mpf(".75"), -mp.mpf(".5"), 0, mp.mpf(".5"), mp.mpf(".75"), 1]
        integ = lambda f: mp.quad(f, panels)
        area = integ(h)
        E0 = integ(lambda z: hp(z)**2)
        Eold = integ(lambda z:(hp(z)+hpp(z))**2)
        require(abs(integ(lambda z:mp.exp(z)*(h(z)+hp(z)))) < mp.mpf("1e-44"), "first moment")
        # A second independently noisy but constrained profile: (1+d/dz)(z*h).
        nfun = lambda z:z*h(z)+h(z)+z*hp(z)
        require(abs(integ(lambda z:mp.exp(z)*nfun(z))) < mp.mpf("1e-44"), "noise first moment")
        require(abs(integ(nfun)) < mp.mpf("1e-44"), "noise zero area")
        # Sharp H_0^1 infimum for fixed area and one forbidden exponential moment.
        g0 = lambda z:(1-z*z)/2
        g1 = lambda z:mp.cosh(1)+z*mp.sinh(1)-mp.exp(z)
        G = mp.matrix([[mp.mpf(2)/3, 2/mp.e], [2/mp.e, 1-mp.exp(-2)]])
        require(abs(G[0,1]-integ(g1)) < mp.mpf("1e-44"), "Gram 01")
        require(abs(G[1,1]-integ(lambda z:mp.exp(z)*g1(z))) < mp.mpf("1e-44"), "Gram 11")
        lam = mp.lu_solve(G, mp.matrix([area, 0]))
        Emin = area*lam[0]
        # C-infinity compact bumps times polynomials: feasible, not just an H1 minimizer.
        degree=max(degrees)
        B = [integ(lambda z,j=j:h(z)*z**j) if j%2==0 else zero for j in range(degree+1)]
        C = [integ(lambda z,j=j:mp.exp(z)*h(z)*z**j) for j in range(degree+1)]
        moments = {}
        for n in range(0,2*degree+3,2):
            for power in (0,2,4):
                moments[n,power] = integ(lambda z,n=n,power=power: h(z)**2*z**n/(1-z*z)**power if abs(z)<1 else zero)
        def moment(n,power):
            return zero if n%2 else moments[n,power]
        K=mp.matrix(degree+1)
        for i in range(degree+1):
            for j in range(degree+1):
                n=i+j
                K[i,j] = (i*j*moment(n-2,0) if i*j else zero)-2*(i+j)*moment(n,2)+4*moment(n+2,4)
        rows=[]
        prev=mp.inf
        for degree in degrees:
            kk=K[:degree+1,:degree+1]
            aa=mp.matrix([[B[j] for j in range(degree+1)], [C[j] for j in range(degree+1)]])
            # Cholesky is an independent positivity check on the energy metric.
            mp.cholesky(kk)
            W=kk**-1*aa.T
            mult=mp.lu_solve(aa*W,mp.matrix([area,0]))
            coeff=W*mult
            energy=(coeff.T*kk*coeff)[0]
            residual=mp.norm(aa*coeff-mp.matrix([area,0]),p=mp.inf)
            require(residual<mp.mpf("1e-42"), "smooth-basis constraints")
            require(Emin < energy < prev, "variational bounds or monotonicity")
            prev=energy
            poly=lambda z:sum((coeff[j]*z**j for j in range(degree+1)),zero)
            polyd=lambda z:sum((j*coeff[j]*z**(j-1) for j in range(1,degree+1)),zero)
            Echeck=integ(lambda z:(hp(z)*poly(z)+h(z)*polyd(z))**2)
            require(abs(energy-Echeck)<mp.mpf("1e-40"), "direct energy")
            rows.append({"degree":degree,"energy":mp.nstr(energy,45),
                         "ratio_to_original_bump_energy":mp.nstr(energy/E0,45),
                         "ratio_to_old_cancelled_pulse_energy":mp.nstr(energy/Eold,45),
                         "constraint_residual":mp.nstr(residual,8),
                         "coefficients":[mp.nstr(v,48) for v in coeff]})
        # Explicit regular finite-spectrum control examples only, NOT SA probabilities.
        # Average the quantum Gaussian characteristic function over classical preparation noise.
        Vbase=mp.mpf(".5"); msignal=mp.mpf(".2"); vprep=mp.mpf(".03")
        char=mp.exp(-2*(Vbase+vprep))*mp.sin(2*msignal)
        positive_probs=[(1+y*sign*char)/2 for sign in (1,-1) for y in (1,-1)]
        require(min(positive_probs)>0 and all(mp.almosteq(sum(positive_probs[i:i+2]),1) for i in (0,2)), "normalized meter control")
        for delta in [mp.mpf(".001"),mp.mpf("-.001")]:
            q=1+delta
            actual=integ(lambda z:mp.exp(q*z)*(h(z)+hp(z)))
            expected=-delta*integ(lambda z:mp.exp(q*z)*h(z))
            require(abs(actual-expected)<mp.mpf("1e-44"), "calibration mismatch")
        return {"dps":dps,"area":mp.nstr(area,45),"original_energy":mp.nstr(E0,45),
                "old_cancelled_energy":mp.nstr(Eold,45),
                "old_ratio":mp.nstr(Eold/E0,45),
                "H01_infimum_energy":mp.nstr(Emin,45),
                "H01_infimum_ratio_to_original":mp.nstr(Emin/E0,45),
                "H01_infimum_not_smooth_feasible":True,
                "smooth_feasible_optimizations":rows,
                "moment_and_noise_kernel_checks":True,
                "calibration_checks":True,
                "meter_normalization_control_only":True}


def compare_precision(low, high):
    errors=[]
    for a,b in zip(low["cases"],high["cases"]):
        for key in ("T_re","T_im","R_re","R_im","inverse_spectral_energy_factor"):
            x,y=mp.mpf(a[key]),mp.mpf(b[key])
            err=abs(x-y)/max(1,abs(y))
            require(err<mp.mpf("1e-40"),"scattering precision mismatch")
            errors.append(err)
    return mp.nstr(max(errors),8)


def record():
    """B: an interior construction with all uncomputed global quantities explicit."""
    return {
        "candidate_id":"sa-two-input-non-equilibrium-v5", "status":"B", "dimension":4,
        "dimension_split":{"space":3,"time":1},
        "geometry":"Fixed SA MP/shell/RN setup; new actual propagation is confined to the subextremal RN inter-horizon block.",
        "matter_content":"Neutral, real, massless minimally coupled 4D scalar; classical background Maxwell field and charged shells inherited.",
        "quantum_state":"Conditional positive Gaussian mixtures of coherent solutions over a supplied Hadamard seed W0; the full sewn Lorentzian seed is not supplied.",
        "topology":"SA same-exterior handle remains prescribed; the inter-horizon calculation is not the full handle.",
        "assumptions":["Both characteristic inputs independently controllable for exact quiet-branch inverse design",
                       "KSR degenerate-energy scattering space; not a bound on freely falling energy",
                       "Gaussian classical preparation noise is distinguished from quantum vacuum covariance"],
        "boundary_conditions":"Two outer-horizon traces; target at both inner-horizon branches. Shell/global singular boundary data unresolved.",
        "symmetries":["4D spherical RN block only; no spherical replacement of the MP exterior"],
        "approximation_order":"Exact linear scattering theorem; finite-frequency numerical checks; conditional exact free-field state differences; no full semiclassical solution.",
        "stress_energy":{"kind":"conditional_renormalized_state_difference", "formula":"Delta T=T[u_signal]+sum Sigma_ij T[u_i,u_j]", "renormalized":False,"full_tensor_matched":False,"difference_computed_analytically":True},
        "backreaction":{"level":"leading_local_constraint_diagnostic_only","details":"Nonzero generic noise in the first KSR tail conflicts with a fixed C2 regular extension; complete backreacted geometry not solved."},
        "support_accounting":{"complete":False,"details":"Wave Killing-energy costs computed; two-port apparatus, pumps, background source, finite manufacturing work not supplied."},
        "stability":"Only specified first-tail robustness; not complete horizon regularity or material stability.",
        "causal_structure":"No proof that one exterior sender can access and coordinate both inputs in time; no global past response kernel.",
        "sender_intervention":{"description":"Inverse-design target is prescribed mathematically; the required b-dependent two inputs are solved but not prepared by an exterior apparatus. No postselection is used.", "same_preparation":True,"uses_postselection":False,"future_boundary_condition_is_input":True},
        "receiver_observable":"Conditional finite-time Ramsey record on a legitimate local worldtube; no numerical past record.",
        "P_Y_do_0":{"computed":False,"distribution":None,"reason":"Full SA response and reference covariance not constructed."},
        "P_Y_do_1":{"computed":False,"distribution":None,"reason":"Full SA response and reference covariance not constructed."},
        "distinguishability":{"computed":False,"value":None,"error_bound":None,"metric":"total_variation","receiver_precedes_sender":None},
        "obstructions":["One-sided changes cannot create a nonzero difference on only one outgoing branch while the reflected difference vanishes, by KSR reflection injectivity.",
                        "Mean-tail cancellation does not remove a nonzero preparation covariance in the same tail.",
                        "Taylor's Euclidean construction is not here assumed to provide a uniquely continued whole-SA Lorentzian state."],
        "unresolved_assumptions":["Physical two-port access from the exterior sender","Lorentzian seed, CCR/Hadamard/sewing globally","Full all-mode renormalized stress and backreaction","Finite apparatus and boundary preparation","Actual past distributions"],
        "literature":[{"title":"A scattering theory for linear waves on the interior of Reissner-Nordstrom black holes","authors":"C. Kehle; Y. Shlapentokh-Rothman","year":2019,"url":"https://arxiv.org/abs/1804.05438","used_for":"Prop.3.3; Theorems3--5, exact inverse and reflection injectivity.","checked_on":"2026-09-25"},
                      {"title":"Regular Quantum States on the Cauchy Horizon of a Charged Black Hole","authors":"P. Taylor","year":2020,"url":"https://arxiv.org/abs/1904.05941","used_for":"Section6 caveat on Lorentzian continuation; not a global state import.","checked_on":"2026-09-25"}],
        "code":["src/symbolic/sa_two_input_state_v5.py","src/symbolic/sa_two_input_state_verify_v5.py"],
        "verification":{"computational":"forward_calculations_passed","external_peer_review":"not_performed","human_review_for_A":True},
        "scope":"Intermediate RN control/state-deformation result, NOT a constructed past-signalling channel. A unchanged.",
        "assumption_changes":[
            {"field":"characteristic control", "old":"one outer-horizon input; the other fixed", "new":"two independently adjustable inputs in the inverse-design problem", "reason":"Test complete waveform control rather than cancellation of only one pole."},
            {"field":"state preparation", "old":"coherent mean over an unspecified reference", "new":"explicit Gaussian mixture of coherent solutions, conditional on the same reference", "reason":"Track extra nonstationary covariance and its stress, not only the mean."},
            {"field":"pulse shape", "old":"h+h-prime", "new":"C-infinity bump times degree 2/4/6/8 polynomials at equal support and area", "reason":"Reduce the input energy at a fixed first-tail constraint; not optimize a past receiver law."}
        ],
        "construction_evidence":{k:False for k in ("global_stress_matching","semiclassical_self_consistency","apparatus_complete","stability_appropriate","initial_boundary_consistency","finite_receiver_record","intervention_not_correlation","renormalized_source_supplied")},
        "stages":{
            "1":{"name":"literature","state":"completed"},
            "2":{"name":"classical_geometry","state":"partial"},
            "3":{"name":"quantum_source","state":"partial"},
            "4":{"name":"backreaction","state":"partial"},
            "5":{"name":"support_accounting","state":"partial"},
            "6":{"name":"stability","state":"partial"},
            "7":{"name":"information_channel","state":"not_reached"}
        },
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output",type=Path)
    args=parser.parse_args()
    start=time.monotonic()
    algebra=exact_algebra()
    scatter=[]; pulse=[]
    for dps in PRECISIONS:
        print(f"Calculating {dps}-digit 4D interior scattering",flush=True)
        scatter.append(scattering(dps))
        print(f"Calculating {dps}-digit constrained smooth pulses",flush=True)
        pulse.append(pulse_and_state(dps))
    with mp.workdps(85):
        error=compare_precision(*scatter)
        for key in ("area","original_energy","old_cancelled_energy","H01_infimum_energy"):
            require(abs(mp.mpf(pulse[0][key])-mp.mpf(pulse[1][key]))<mp.mpf("1e-40"),"pulse precision mismatch")
        for a,b in zip(pulse[0]["smooth_feasible_optimizations"],pulse[1]["smooth_feasible_optimizations"]):
            require(abs(mp.mpf(a["energy"])-mp.mpf(b["energy"]))<mp.mpf("1e-40"),"optimizer precision mismatch")
        low=[]
        for qtext in ("0.5","0.9","0.99","0.999"):
            q=mp.mpf(qtext); s=mp.sqrt(1-q*q); rp=1+s;rm=1-s
            T=(rm/rp+rp/rm)/2;R=(rm/rp-rp/rm)/2
            low.append({"Q_over_M":qtext,"T0":mp.nstr(T,40),"R0":mp.nstr(R,40),"spectral_energy_factor_limit":mp.nstr(T*T+R*R,40),"second_input_fraction_limit":mp.nstr(R*R/(T*T+R*R),40),"p":mp.nstr((rm/rp)**2,40)})
    candidate=record()
    trials=([{ "kind":"finite_frequency",**r} for r in scatter[-1]["cases"]]
            +[{"kind":"low_frequency_limit",**r} for r in low]
            +[{"kind":"smooth_pulse",**r} for r in pulse[-1]["smooth_feasible_optimizations"]])
    candidate["calculation"]={"verdict":"conditional_two_input_state_control", "tested":len(trials),"trials":trials}
    candidate["numerical_error_budget"]={
        "precision_comparison":"50/80 digits, threshold 1e-40 relative to max(1,abs(value)); actual difference recorded",
        "infinite_endpoint":"analytic exponential tail bound separate from ODE error",
        "ode_discretization":"Taylor integration cross-checked by Cayley/Richardson; no interval proof of total ODE error",
        "optimization":"implicit exact integrals define coefficients; printed decimals are finite precision and cannot enforce an exact physical pole zero",
        "receiver":"No full-SA response or noise is assigned a numerical value"
    }
    result={"base_sha":BASE_SHA,"code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            "environment":{"python":platform.python_version(),"sympy":sp.__version__,"mpmath":mp.__version__},
            "classification":{"A":0,"B":1,"C":0},
            "interpretation":"One B with restricted obstructions; no new independent apparatus count.",
            "exact_algebra":algebra,"scattering_runs":scatter,"max_50_80_relative_difference":error,
            "low_frequency_limits":low,"pulse_runs":pulse,"candidates":[candidate],
            "elapsed_seconds":round(time.monotonic()-start,3),
            "execution":{"kind":"github_actions" if os.environ.get("GITHUB_ACTIONS")=="true" else "local", "checkout_sha":os.environ.get("GITHUB_SHA"),"run_id":os.environ.get("GITHUB_RUN_ID")},"merging_performed_by_script":False}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"passed":True,"scattering_precision_difference":error,"pulse_energy":pulse[-1]["smooth_feasible_optimizations"][-1]["energy"],"past_probabilities":"uncomputed","elapsed_seconds":result["elapsed_seconds"]},ensure_ascii=False),flush=True)

if __name__ == "__main__":
    main()
