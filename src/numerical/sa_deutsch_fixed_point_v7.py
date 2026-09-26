#!/usr/bin/env python3
"""SA v7: explicit Deutsch fixed-point toy completion on top of frozen SA v5.

The SA v5 two-input map is treated as a completed signal component.  This file
adds a *hypothesized* Deutsch fixed-point rule and a standard pure-loss segment,
then computes explicit do(0)/do(1) receiver probabilities.  It is a B candidate,
not a derivation of Deutsch dynamics from 3+1D semiclassical QFT.
"""
from __future__ import annotations
import argparse, json, math, hashlib, platform
from pathlib import Path
import mpmath as mp
import sympy as sp

BASE_SHA = "fbc4e2bf567e00e021f94216f470198f5ce41880"
A = sp.Rational(1,2)          # attenuation amplitude; eta=A^2=1/4
ETA = A**2
LAMBDA = sp.Integer(1)
C = sp.pi/8                   # x-quadrature displacement per loop pass


def require(ok, msg):
    if not ok:
        raise AssertionError(msg)


def exact_results():
    # X,P convention: [X,P]=i; vacuum variances are 1/2.
    mean = sp.simplify(C/(1-A))
    vx = sp.Rational(1,2)
    # Receiver is QND in X.  Tracing its |+x> probe adds random +/-lambda P kicks,
    # then the eta attenuator damps them before the next pass.
    vp = sp.simplify(sp.Rational(1,2) + ETA*LAMBDA**2/(1-ETA))
    require(mean == sp.pi/4, "fixed mean")
    require(vp == sp.Rational(5,6), "P variance")
    require(sp.simplify(vx*vp-sp.Rational(1,4)) > 0, "uncertainty")

    d = sp.simplify(sp.exp(-2*LAMBDA**2*vx)*sp.sin(2*LAMBDA*mean))
    require(d == sp.exp(-1), "chosen signal should give exp(-1)")
    p0 = [sp.simplify((1+d)/2), sp.simplify((1-d)/2)]
    p1 = [p0[1], p0[0]]

    # Induced record kernel, rows y=+1,-1; columns b=0,1.
    K = sp.Matrix([[p0[0], p1[0]],[p0[1], p1[1]]])
    uniform = sp.Matrix([sp.Rational(1,2), sp.Rational(1,2)])
    Xbit = sp.Matrix([[0,1],[1,0]])
    require(sp.simplify(K*uniform-uniform) == sp.zeros(2,1), "copy Deutsch fixed point")
    require(sp.simplify(K*Xbit*uniform-uniform) == sp.zeros(2,1), "NOT Deutsch fixed point")
    require(K.eigenvals()[d] == 1, "copy nontrivial eigenvalue")
    require((K*Xbit).eigenvals()[-d] == 1, "NOT nontrivial eigenvalue")

    return {
        "parameters": {"attenuation_amplitude":"1/2","eta":"1/4","lambda":"1","c":"pi/8"},
        "fixed_point_x_mean": {"do_0":"pi/4","do_1":"-pi/4"},
        "fixed_point_variances": {"V_X":"1/2","V_P":"5/6"},
        "exact_receiver_contrast": "exp(-1)",
        "P_Y_do_0": {"+1":"(1+exp(-1))/2","-1":"(1-exp(-1))/2"},
        "P_Y_do_1": {"+1":"(1-exp(-1))/2","-1":"(1+exp(-1))/2"},
        "D_past": "exp(-1)",
        "copy_record_fixed_point": {"+1":"1/2","-1":"1/2","subleading_eigenvalue":"exp(-1)"},
        "not_record_fixed_point": {"+1":"1/2","-1":"1/2","subleading_eigenvalue":"-exp(-1)"},
        "fixed_point_characteristic_function": (
            "chi_b(kx,kp)=exp[i(-1)^b*pi*kx/4] exp[-(kx^2+kp^2)/4] "
            "prod_{n>=1} cos(2^{-n} kp)"
        ),
    }


def dagger(M):
    return M.T.conjugate()


def tr(M):
    return sum(M[i,i] for i in range(M.rows))


def frob(M):
    return mp.sqrt(sum(abs(M[i,j])**2 for i in range(M.rows) for j in range(M.cols)))


def fock_model(N, dps=30):
    """Pure-mpmath truncated Fock check of the full receiver+loss+feedback maps."""
    with mp.workdps(dps):
        eta=mp.mpf('0.25'); lam=mp.mpf(1); c=mp.pi/8
        a=mp.matrix(N,N)
        for n in range(1,N):
            a[n-1,n]=mp.sqrt(n)
        adag=dagger(a)
        X=(a+adag)/mp.sqrt(2)
        Uminus=mp.expm(-1j*lam*X); Uplus=mp.expm(1j*lam*X)
        Mplus=(Uminus-1j*Uplus)/2
        Mminus=(Uminus+1j*Uplus)/2
        comp=dagger(Mplus)*Mplus+dagger(Mminus)*Mminus
        require(frob(comp-mp.eye(N)) < mp.mpf('1e-24'), "receiver Kraus completeness")
        beta=c/mp.sqrt(2)
        Dplus=mp.expm(beta*adag-beta*a); Dminus=dagger(Dplus)
        Ks=[]
        for k in range(N):
            K=mp.matrix(N,N)
            for n in range(k,N):
                K[n-k,n]=mp.sqrt(math.comb(n,k))*(1-eta)**(mp.mpf(k)/2)*eta**(mp.mpf(n-k)/2)
            Ks.append(K)

        def loss(rho):
            out=mp.matrix(N,N)
            for K in Ks:
                out += K*rho*dagger(K)
            return out

        def apply(rho, mode):
            if mode in (0,1):
                pre=Mplus*rho*dagger(Mplus)+Mminus*rho*dagger(Mminus)
                mid=loss(pre); D=(Dplus,Dminus)[mode]
                return D*mid*dagger(D)
            out=mp.matrix(N,N)
            Ds=(Dplus,Dminus) if mode=='copy' else (Dminus,Dplus)
            for M,D in zip((Mplus,Mminus),Ds):
                out += D*loss(M*rho*dagger(M))*dagger(D)
            return out

        rows={}
        for mode in (0,1,'copy','not'):
            rho=mp.matrix(N,N); rho[0,0]=1
            err=mp.inf
            for it in range(100):
                new=apply(rho,mode)
                new=new/tr(new).real
                err=frob(new-rho); rho=new
                if err < mp.mpf('1e-14'):
                    break
            probs=[tr(M*rho*dagger(M)).real for M in (Mplus,Mminus)]
            rows[str(mode)]={
                "iterations":it+1,
                "frobenius_step":mp.nstr(err,10),
                "P_plus":mp.nstr(probs[0],30),
                "P_minus":mp.nstr(probs[1],30),
                "trace":mp.nstr(tr(rho).real,30),
            }
        exact=(1+mp.e**-1)/2
        require(abs(mp.mpf(rows['0']['P_plus'])-exact) < mp.mpf('5e-5'), "Fock do(0) mismatch")
        require(abs(mp.mpf(rows['1']['P_plus'])-(1-exact)) < mp.mpf('5e-5'), "Fock do(1) mismatch")
        require(abs(mp.mpf(rows['copy']['P_plus'])-mp.mpf('.5')) < mp.mpf('1e-12'), "copy fixed point")
        require(abs(mp.mpf(rows['not']['P_plus'])-mp.mpf('.5')) < mp.mpf('1e-12'), "NOT fixed point")
        return {"cutoff":N,"dps":dps,"rows":rows}


def candidate_record(exact, fock_runs):
    dnum=mp.e**-1
    return {
      "candidate_id":"sa-deutsch-fixed-point-v7",
      "status":"B",
      "dimension":4,
      "dimension_split":{"space":3,"time":1},
      "geometry":"Frozen SA v5 same-exterior MP/shell/RN signal component plus an explicit effective loop mode and ordinary forward pure-loss segment.",
      "matter_content":"SA v5 classical background and scalar signal; one smeared bosonic loop mode; finite Ramsey qubit receiver; vacuum environment for a standard eta=1/4 attenuator.",
      "quantum_state":"For each selected future operation, impose Deutsch self-consistency rho*=Phi_operation(rho*). For do(b) the exact loop fixed point is specified by the displayed characteristic function; this rule is postulated, not derived from SA QFT.",
      "topology":"SA same-exterior handle retained as prescribed background; the additional fixed-point rule is a nonstandard global quantum law.",
      "assumptions":["SA v5 is frozen as a completed signal part","Deutsch operation-dependent fixed-point law","pure-loss amplitude 1/2 on the ordinary forward segment","future sender controls both v5 ports","no postselection"],
      "boundary_conditions":"No future final-state projection. The loop state is selected by rho=Phi_E(rho) separately for the actually chosen local operation E.",
      "symmetries":["Single selected wavepacket mode for the fixed-point toy; not a spherical replacement of the full MP exterior."],
      "approximation_order":"Exact one-mode CPTP/fixed-point algebra and finite-Fock verification on top of the frozen linear SA signal component; not a full 3+1D semiclassical derivation of the Deutsch law.",
      "stress_energy":{"kind":"finite-mode toy only","renormalized":False,"full_tensor_matched":False,"details":"Finite mode energy is bounded; the full SA renormalized stress tensor for this operation-dependent state is not computed."},
      "backreaction":{"level":"not_solved","details":"No semiclassical Einstein solution selects or supports the Deutsch fixed point."},
      "support_accounting":{"complete":False,"details":"SA formation and the physical mechanism enforcing the fixed-point law are unsupplied."},
      "stability":"The eta=1/4 effective loop is contractive for fixed do(b); copy/NOT feedback fixed points were numerically iterated in truncated Fock space. This is not full spacetime stability.",
      "causal_structure":"Future do(b) drives the two frozen SA ports; the candidate backward field reaches the earlier finite receiver; its ordinary record can return forward. Deutsch consistency replaces the v6 operation-independent process law.",
      "sender_intervention":{"description":"do(b) chooses the common sign of the two frozen SA v5 inverse-scattering inputs, producing an x displacement (-1)^b*pi/8 per loop pass.","same_preparation":True,"uses_postselection":False,"future_boundary_condition_is_input":False},
      "receiver_observable":"Finite Ramsey qubit with U=exp(-i sigma_z X), measured in sigma_y; all Y=+/-1 results retained.",
      "P_Y_do_0":{"computed":True,"distribution":{"+1":"(1+e^-1)/2","-1":"(1-e^-1)/2"},"numeric":{"+1":float((1+dnum)/2),"-1":float((1-dnum)/2)}},
      "P_Y_do_1":{"computed":True,"distribution":{"+1":"(1-e^-1)/2","-1":"(1+e^-1)/2"},"numeric":{"+1":float((1-dnum)/2),"-1":float((1+dnum)/2)}},
      "distinguishability":{"metric":"total_variation","computed":True,"value":"e^-1","numeric":float(dnum),"receiver_precedes_sender":True},
      "obstructions":[],
      "unresolved_assumptions":["Derive the operation-dependent Deutsch fixed-point selection rule from the full 3+1D SA quantum field theory rather than postulate it.","Compute the corresponding full renormalized stress tensor and semiclassical backreaction."],
      "literature":[
        {"authors":"D. Deutsch","title":"Quantum mechanics near closed timelike lines","year":1991,"url":"https://doi.org/10.1103/PhysRevD.44.3197","used_for":"Fixed-point CTC prescription; not a derivation from SA."},
        {"authors":"H. D. Politzer","title":"Path integrals, density matrices, and information flow with closed timelike curves","year":1994,"url":"https://doi.org/10.1103/PhysRevD.49.3981","used_for":"Inequivalent CTC quantum prescriptions and nonlinearity/coherence caveat."},
        {"authors":"S. Aaronson; J. Watrous","title":"Closed Timelike Curves Make Quantum and Classical Computing Equivalent","year":2009,"url":"https://arxiv.org/abs/0808.2669","used_for":"Modern statement of Deutsch causal consistency as a fixed point of the evolution map."}
      ],
      "code":["src/numerical/sa_deutsch_fixed_point_v7.py","src/symbolic/sa_deutsch_fixed_point_verify_v7.py"],
      "verification":{"computational":"exact algebra plus finite-Fock iteration","external_peer_review":"not_performed","human_review_for_A":True},
      "scope":"Positive D_past in an explicit Deutsch-rule toy completion. B, not A, because the fixed-point law and its full 3+1D RSET/backreaction are not derived from the SA semiclassical theory.",
      "calculation":{"exact":exact,"fock_runs":fock_runs}
    }


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    exact=exact_results()
    # Exact algebra is primary; two finite cutoffs check the full feedback channel.
    fock_runs=[fock_model(10,30), fock_model(14,30)]
    rec=candidate_record(exact,fock_runs)
    result={"base_sha":BASE_SHA,"environment":{"python":platform.python_version(),"sympy":sp.__version__,"mpmath":mp.__version__},"classification":{"A":0,"B":1,"C":0},"candidate":rec,"code_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding='utf-8')
    print(json.dumps({"passed":True,"classification":result["classification"],"D_past":float(mp.e**-1),"P0_plus":float((1+mp.e**-1)/2),"copy_fixed_P_plus":fock_runs[-1]["rows"]["copy"]["P_plus"],"fock_cutoffs":[r["cutoff"] for r in fock_runs]},ensure_ascii=False))

if __name__=='__main__':
    main()
