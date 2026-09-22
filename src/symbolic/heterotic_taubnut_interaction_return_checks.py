#!/usr/bin/env python3
"""Scoped interaction/backreaction/return checks for the Taub-NUT audit.

This script DOES NOT prove a full heterotic BRST spectrum, a string S-matrix,
or a time machine. It verifies specified algebra, a scalar radial problem,
a neutral-spectator selection rule, and local causal/backreaction diagnostics.
Dependencies: SymPy and mpmath. No network, no external files, no CI dispatch.
Run: python heterotic_taubnut_interaction_return_checks.py [--json OUTPUT]
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sympy as sp
import mpmath as mp


def main() -> dict:
    report: dict = {"scope": "conditional scalar/CFT-factor/local-geometry diagnostics",
                    "full_string_BRST_proved": False,
                    "interacting_coset_amplitude_computed": False,
                    "operational_past_return_proved": False}
    mp.mp.dps = 80
    # 1. Retain the genuinely checked anomaly/weight arithmetic, not its
    #    unproved interpretation as a complete physical state.
    k1, k2 = sp.Integer(8), sp.Integer(4)
    delta, lam = sp.sqrt(sp.Rational(8, 5)), sp.sqrt(sp.Rational(2, 5))
    QA, PA, QB, PB = map(sp.Integer, (2, 0, 2, 1))
    anomalies = [-k1*(1-delta**2)-2*(QA**2+PA**2-delta**2),
                 k1*delta*lam-2*(QA*QB+PA*PB-delta*lam),
                 k2+k1*lam**2-2*(QB**2+PB**2-1-lam**2)]
    assert all(sp.simplify(e) == 0 for e in anomalies)
    j, ell = sp.Rational(1, 2)+sp.I/2, sp.Integer(1)
    omega = sp.sqrt(10)/2
    JL = sp.Matrix([-2, 0])
    K = sp.Matrix([[8, 4], [4, 5]])
    h_num = -j*(j-1)/(k1-2)+ell*(ell+1)/(k2+2)
    assert sp.simplify(h_num-(JL.T*K.inv()*JL)[0]/2) == 0
    assert sp.simplify(-2+delta*omega) == 0
    assert sp.simplify(lam*omega-1) == 0
    report["anomaly_and_assumed_weight_arithmetic"] = "PASS (conditional conventions)"

    # 2. Independent numerical reproduction including ODE residual and
    #    Wronskian, not just the closed-form number.
    om = mp.sqrt(10)/2
    de = mp.sqrt(mp.mpf(8)/5)
    la = mp.sqrt(mp.mpf(2)/5)
    ap, am = om*(1+de)/2, om*(de-1)/2
    a = mp.mpf('.5')-1j*(om+mp.mpf('.5'))
    b = mp.mpf('.5')-1j*(om-mp.mpf('.5'))
    c = 1-1j*(om+2)
    A = mp.gamma(c)*mp.gamma(1j)/(mp.gamma(b)*mp.gamma(c-a))
    B = mp.gamma(c)*mp.gamma(-1j)/(mp.gamma(a)*mp.gamma(c-b))
    transmission, reflection = (om+2)/abs(B)**2, abs(A/B)**2
    assert abs(transmission+reflection-1) < mp.mpf('1e-70')
    def radial(u):
        return u**(-1j*ap)*(1+u)**(1j*am)*mp.hyp2f1(a,b,c,-u)
    def Dm(x):
        return (x+de)**2-mp.mpf('.4')*(x*x-1)
    errors, currents = [], []
    for u in map(mp.mpf, ('0.01','0.1','1','10')):
        R = radial(u)
        dR, ddR = mp.diff(radial,u), mp.diff(radial,u,2)
        potential = om**2*Dm(1+2*u)/(4*u*(1+u))-1
        terms = (u*(1+u)*ddR, (1+2*u)*dR, potential*R)
        residual = abs(sum(terms))/(1+sum(map(abs,terms)))
        flux = 2*u*(1+u)*mp.im(mp.conj(R)*dR)
        assert residual < mp.mpf('1e-65')
        assert abs(flux+(om+2)) < mp.mpf('1e-65')
        errors.append(mp.nstr(residual,8)); currents.append(mp.nstr(flux,25))
    report["scalar_radial_problem"] = {
        "T":mp.nstr(transmission,55), "R":mp.nstr(reflection,55),
        "R_plus_T_minus_1":mp.nstr(transmission+reflection-1,8),
        "relative_ODE_residuals":errors, "flux_samples":currents,
        "interpretation":"exterior radial flux ratio; NOT a string/past-return probability"}

    # 3. Free spectator J=i dY, <JJ>=1/z^2, zero Y momenta.
    #    Wick pairing makes an odd correlator zero. For 4 points it is not zero.
    z1,z2,z3,z4,z,W = sp.symbols('z1 z2 z3 z4 z W')
    def wick(points):
        if len(points)%2: return sp.Integer(0)
        if not points: return sp.Integer(1)
        return sum(wick(points[1:n]+points[n+1:])/(points[0]-points[n])**2
                   for n in range(1,len(points)))
    assert wick([z1,z2,z3]) == 0
    J4 = sp.simplify(sp.limit(W**2*wick([0,z,1,W]),W,sp.oo))
    expected = 1/z**2+1+1/(1-z)**2
    assert sp.simplify(J4-expected) == 0
    assert J4.subs(z,sp.Rational(1,2)) == 9
    report["spectator_selection"] = {
        "self_three_point":"zero for this specific zero-momentum J polarization",
        "four_current_factor":str(J4),
        "four_current_factor_at_z_half":9,
        "full_four_string_amplitude":"NOT computed; other coset/ghost/picture factors required"}

    # 4. Exact local coupling and acceleration of the fixed-x time-circle.
    x,y,L2 = sp.symbols('x y L2', positive=True)
    p=x*x-1
    D=(x+delta)**2-sp.Rational(2,5)*p
    d=1+delta
    assert sp.simplify(D.subs(x,1)-d*d) == 0
    assert sp.simplify(sp.diff(D,x)-(6*x+4*sp.sqrt(10))/5) == 0
    acc2=p/(4*L2)*(sp.diff(p,x)/p-sp.diff(D,x)/D)**2
    assert sp.simplify(sp.limit(y*acc2.subs(x,1+y),y,0)-1/(2*L2)) == 0
    report["coupling"] = {"g_s_horizon_over_g_s0":mp.nstr(1/mp.sqrt(1+de),30),
        "monotonicity":"D'>0 for x>=1, hence g_s decreases along positive NUT x",
        "holding_acceleration":"a^2 ~ 1/[2 L^2 (x-1)]; finite at fixed x>1"}

    # 5. Horizon-regular outgoing EF coframe u=t-r*(x), chi=du-lambda cos theta dphi.
    #    In this coframe only the radial/time 2x2 transformation is needed.
    P,DD,LL = sp.symbols('P DD LL', positive=True)
    old = LL*sp.diag(1/P, -P/DD)
    jac = sp.Matrix([[1,0],[sp.sqrt(DD)/P,1]])  # dt=du+sqrt(D)/p dx
    ef=sp.simplify(jac.T*old*jac)
    expected_ef=LL*sp.Matrix([[0,-1/sp.sqrt(DD)],[-1/sp.sqrt(DD),-P/DD]])
    assert sp.simplify(ef-expected_ef) == sp.zeros(2)
    horizon = ef.subs(P,0)
    assert sp.simplify(horizon.det()+LL**2/DD) == 0
    qx,qu=sp.symbols('qx qu', real=True)
    inner=(sp.Matrix([qx,qu]).T*horizon*sp.Matrix([0,1]))[0]
    assert sp.simplify(inner+LL*qx/sp.sqrt(DD)) == 0
    report["one_way_horizon"] = {
        "g_q_future_null_generator":"-L^2 q^x / d at x=1",
        "conclusion":"future causal crossing has q^x>=0 for this Taub->NUT interface",
        "scope":"no reverse future crossing through THIS interface; not a global all-extension no-go"}

    # 6. Local Misner/Rindler limit in physical length R and boost time eta=t/d.
    rad,eta=sp.symbols('rad eta', positive=True)
    U=-rad*sp.exp(-eta); V=rad*sp.exp(eta)
    J=sp.Matrix([[sp.diff(U,rad),sp.diff(U,eta)],
                 [sp.diff(V,rad),sp.diff(V,eta)]])
    flatnull=sp.Matrix([[0,-sp.Rational(1,2)],[-sp.Rational(1,2),0]])
    assert sp.simplify(J.T*flatnull*J-sp.diag(1,-rad**2)) == sp.zeros(2)
    boost=4*mp.pi*la/(1+de)
    report["local_boost"]={"b":mp.nstr(boost,35),"exp_b":mp.nstr(mp.exp(boost),35),
        "meaning":"local quotient boost; NOT a required physical circuit gain for every state"}

    # 7. Conditional blueshift stress in a regular horizon chart.
    #    zeta=-U>0, a stationary branch chi=zeta^(i Omega) is singular at U=0.
    zeta,Omega,Cout=sp.symbols('zeta Omega Cout', positive=True)
    chi=Cout*sp.exp(sp.I*Omega*sp.log(zeta))
    density=sp.simplify(sp.diff(chi,zeta)*sp.conjugate(sp.diff(chi,zeta)))
    assert sp.simplify(density-Cout**2*Omega**2/zeta**2) == 0
    # A regular ingoing V branch has no U derivative, so the singular coefficient
    # is NOT inevitable. This explicitly avoids proving an invalid universal no-go.
    vv=sp.symbols('vv',positive=True)
    regular=sp.exp(-sp.I*Omega*sp.log(vv))
    assert sp.diff(regular,zeta) == 0
    tU,tV=sp.symbols('tU tV',positive=True)
    streams=sp.diag(tU/zeta**2,tV/vv**2)
    inv=flatnull.inv()
    invariant=sp.simplify(sp.trace(streams*inv*streams*inv))
    assert sp.simplify(invariant-8*tU*tV/(zeta**2*vv**2)) == 0
    report["conditional_backreaction"]={
        "singular_branch_derivative_squared":str(density),
        "two_null_stream_invariant":str(invariant),
        "regular_branch_U_derivative":0,
        "epsilon_scaling":"epsilon(U)=epsilon0*(U0/U)^2, for a nonzero stationary singular branch",
        "scope":"local EFT diagnostic, not a full string-loop/backreacted solution"}

    # 8. Coordinate periodicity is not an information-return observable.
    #    A simple grade check also catches an old unsupported descendant formula.
    kk,ww=sp.symbols('kk ww', integer=True, positive=True)
    grade=kk*ww  # [L0,K^+_-1]=K^+_-1
    claimed=kk*ww**2
    assert (grade-claimed).subs({kk:4,ww:2}) == -8
    cutoff=sp.symbols('cutoff',positive=True)
    norm=sp.integrate(1/x,(x,1,cutoff))
    assert sp.simplify(norm-sp.log(cutoff)) == 0
    report["scope_checks"]={
        "old_simple_descendant_formula":"grade k*w != k*w^2 for w>1; old symbolic CI did not check it",
        "individual_asymptotic_radial_mode_L2_integral":str(norm),
        "caution":"generalized mode is not an already constructed finite-norm physical packet"}
    print(json.dumps(report,indent=2,ensure_ascii=False))
    print('PASS: all explicitly implemented diagnostics; no full-string/time-travel theorem claimed.')
    return report

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--json',type=Path,help='Optional report path')
    args=parser.parse_args()
    result=main()
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True)
        args.json.write_text(json.dumps(result,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
