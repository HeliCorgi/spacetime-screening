"""4D continuation: smooth RN source audit and a same-exterior MP handle.

These are TWO different models, never a completed semiclassical channel.
Units c=hbar=G=1 in the numerical records. Sources in the accompanying note.
"""
from __future__ import annotations
import mpmath as mp
import sympy as sp


def exact_checks() -> dict:
    r, a, e, M, z, v, w = sp.symbols('r a e M z v w', positive=True)
    f = 1-2*M/r+z/r**2
    fr, frr = sp.diff(f,r), sp.diff(f,r,2)
    # Entries are 8*pi*G times orthonormal covariant stress components.
    rho = (1-f*v*v-2*f*r*w-fr*r*v*v)/r**2
    pr = (-1+f*v*v+fr*r*v*v)/r**2
    pt = (frr*v*v+fr*w)/2 + fr*v*v/r + f*w/r
    scalar = sp.factor(rho-pr-2*pt)
    expected = 2*(1-v*v)/r**2-(fr+4*f/r)*w
    assert sp.simplify(scalar-expected)==0
    assert sp.simplify(rho+pr+2*f*w/r)==0
    assert all(sp.simplify(q.subs({v:1,w:0})-s*z/r**4)==0
               for q,s in ((rho,1),(pr,-1),(pt,1)))
    # T_ren required after subtracting the classical Maxwell tensor.
    source = [rho-z/r**4, pr+z/r**4, pt-z/r**4]
    derivative = lambda q: sp.diff(q,r)*v+sp.diff(q,v)*w+sp.diff(q,w)*sp.Symbol('wprime')
    ward = derivative(source[1])+fr*v/(2*f)*(source[0]+source[1])+2*v/r*(source[1]-source[2])
    assert sp.simplify(ward)==0
    # On x>0 use s=sqrt(x^2+e^2)=r-a+e: r'^2=1-e^2/s^2, r''=e^2/s^3.
    s=r-a+e
    R=sp.factor(expected.subs({v:sp.sqrt(1-e**2/s**2),w:e**2/s**3}))
    assert sp.limit(r**4*R,r,sp.oo)==-2*e**2
    # A state-independent trace test, not a replacement for the complete RSET.
    u=sp.symbols('u',positive=True)
    X=sp.sqrt(1-e**2/s**2)
    Dx=lambda q: sp.diff(q,r)*X
    boxR=sp.factor(Dx(r**2*f*Dx(R))/r**2)
    assert sp.limit(r**6*boxR,r,sp.oo)==-24*e**2
    # Curvature from four independent orthonormal sections.
    A=(frr*X**2+fr*e**2/s**3)/2
    B=fr*X**2/(2*r)
    C=-(f*e**2/s**3+fr*X**2/2)/r
    D=(1-f*X**2)/r**2
    K=4*(A*A+2*B*B+2*C*C+D*D)
    Ric2=(A+2*B)**2+(-A+2*C)**2+2*(-B+C+D)**2
    W2=K-2*Ric2+R**2/3; Euler=K-4*Ric2+R**2
    assert sp.limit(r**6*W2,r,sp.oo)==48*M**2
    assert sp.limit(r**6*Euler,r,sp.oo)==48*M**2
    assert sp.limit(r**4*W2,r,sp.oo)==0
    # Explicit ansatz relaxation: a logarithmic lapse tail removes the r^-4 trace term.
    L=sp.symbols('L',positive=True)
    deltaf=2*e**2*sp.log(r/L)/r**2
    dR=-(sp.diff(deltaf,r,2)*X**2+sp.diff(deltaf,r)*e**2/s**3
         +4*(deltaf*e**2/s**3+sp.diff(deltaf,r)*X**2)/r+2*deltaf*X**2/r**2)
    assert sp.limit(r**4*(R+dR),r,sp.oo)==0
    # MP junction identities. U is angle-dependent; do not replace it by an average.
    U,Un,Ut,Unt,b = sp.symbols('U Un Ut Unt b', positive=True)
    kt=-Un/U**2; ka=1/(U*b)+Un/U**2
    sigma=-ka/(2*sp.pi); pressure=(kt+ka)/(4*sp.pi)
    charge=-Un/(2*sp.pi*U**2)
    assert sp.simplify(pressure-1/(4*sp.pi*U*b))==0
    assert sp.simplify(sigma+2*pressure-charge)==0
    Dth=lambda q: sp.diff(q,U)*Ut+sp.diff(q,Un)*Unt
    force=Dth(pressure)-(sigma+pressure)*Ut/U
    assert sp.simplify(force-Un*Ut/(2*sp.pi*U**3))==0
    return {'rn_full_stress_and_ward':'exact', 'RN_r4_R':'-2*epsilon^2',
            'RN_r6_boxR':'-24*epsilon^2', 'RN_r6_Weyl2':'48*M^2',
            'RN_r6_Euler':'48*M^2', 'log_lapse_tail_cancels_r4_trace':True,
            'MP_Israel_Maxwell_tangential_Ward':'exact'}


def rn_components(x, a, e, M, q2):
    s=mp.sqrt(x*x+e*e); r=a+s-e
    v=x/s; w=e*e/s**3
    f=1-2*M/r+q2/r**2; fr=2*M/r**2-2*q2/r**3; frr=-4*M/r**3+6*q2/r**4
    rho=(1-f*v*v-2*f*r*w-fr*r*v*v)/r**2
    pr=(-1+f*v*v+fr*r*v*v)/r**2
    pt=(frr*v*v+fr*w)/2+fr*v*v/r+f*w/r
    A=(frr*v*v+fr*w)/2; B=fr*v*v/(2*r)
    C=-(f*w+fr*v*v/2)/r; D=(1-f*v*v)/r**2
    R=-2*A-4*B+4*C+2*D
    K=4*(A*A+2*B*B+2*C*C+D*D)
    Ric2=(A+2*B)**2+(-A+2*C)**2+2*(-B+C+D)**2
    return r,f,rho-q2/r**4,pr+q2/r**4,pt-q2/r**4,R,K-2*Ric2+R*R/3,K-4*Ric2+R*R


def rn_trials(dps: int) -> list[dict]:
    with mp.workdps(dps):
        fmt=lambda x:mp.nstr(x,45)
        a=mp.mpf(1); M=mp.mpf('0.9'); q2=mp.mpf('0.8099')
        rows=[]
        for es in ['0.01','0.03','0.1']:
            e=mp.mpf(es)
            for xs in ['0','0.1','1','10','100']:
                x=mp.mpf(xs)
                r,f,rho,pr,pt,R,W2,E4=rn_components(x,a,e,M,q2)
                assert f>0 and rho+pr<0
                # Neutral real conformal scalar with beta=0 renormalization convention.
                anomaly=(W2/120-E4/360)/(16*mp.pi**2)
                rows.append({'kind':'RN_point','epsilon':es,'x':xs,
                    'r':fmt(r),'f':fmt(f),'eight_pi_G_rho_extra':fmt(rho),
                    'eight_pi_G_pr_extra':fmt(pr),'eight_pi_G_pt_extra':fmt(pt),
                    'R':fmt(R),'minimal_scalar_l0_potential':fmt(f*((2*M/r**2-2*q2/r**3)*(x*x/(x*x+e*e))+f*e*e/(x*x+e*e)**mp.mpf('1.5'))/r),'scalar_anomaly_beta0':fmt(anomaly),
                    'trace_residual_G1':fmt(-R/(8*mp.pi)-anomaly)})
            # E=1 affine radial ANEC: dx/dlambda=+1 for this quasi-global metric.
            # x=e*sinh(t) removes the narrow peak and maps both ends to the real line.
            integ=mp.quad(lambda t: 1/(mp.cosh(t)**2*(a+e*mp.cosh(t)-e)),[0,1,3,mp.inf])
            anec=-integ/(2*mp.pi)
            rows.append({'kind':'RN_ANEC','epsilon':es,'ANEC_G1':fmt(anec),
                         'thin_ANEC_G1':fmt(-1/(2*mp.pi*a))})
        return rows


def mp_boundary(m, a, d, u):
    if m<=0 or a<=0 or d<=2*a or abs(u)>1:
        raise ValueError('Require m>0, a>0, d>2a, |cos(theta)|<=1')
    s=mp.sqrt(d*d+a*a-2*d*a*u)
    U=1+m/a+m/s
    Un=-m/a**2-m*(a-d*u)/s**3
    sigma=-(U+a*Un)/(2*mp.pi*U**2*a)
    pressure=1/(4*mp.pi*U*a)
    charge=-Un/(2*mp.pi*U**2)
    return U,Un,sigma,pressure,charge


def optical_time(m,a,d):
    if m<=0 or a<=0 or d<=2*a:
        raise ValueError('Invalid excised-sphere geometry')
    return d-2*a+4*m*mp.log((d-a)/a)+m*m*(2*(1/a-1/(d-a))+4/d*mp.log((d-a)/a))


def mp_trials(dps: int) -> list[dict]:
    with mp.workdps(dps):
        fmt=lambda x:mp.nstr(x,45)
        m=mp.mpf(1); rows=[]
        for a_s,d_s in [('0.1','10'),('0.2','5'),('0.5','4')]:
            a,d=mp.mpf(a_s),mp.mpf(d_s)
            for u_s in ['-1','-0.5','0','0.5','1']:
                u=mp.mpf(u_s); U,Un,sigma,p,q=mp_boundary(m,a,d,u)
                assert U>0 and Un<0 and sigma<0 and p>0 and q>0
                rows.append({'kind':'MP_boundary','a':a_s,'d':d_s,'u':u_s,
                             'U':fmt(U),'sigma_G1':fmt(sigma),'p_G1':fmt(p),'charge_G1':fmt(q)})
            T=optical_time(m,a,d)
            Uface=mp_boundary(m,a,d,mp.mpf(1))[0]
            # Explicit prescribed holonomy; not generated by human controls.
            delta=T+Uface*mp.mpf(1)
            rows.append({'kind':'MP_return','a':a_s,'d':d_s,'T_axis':fmt(T),
                         'prescribed_Delta':fmt(delta),'proper_return_minus_send':fmt((T-delta)/Uface),
                         'shell_proper_energy_G1':fmt(-2*a*(1+m/d)),
                         'shell_charge_G1':fmt(2*m)})
        a=mp.mpf('.1');d=mp.mpf(10);T=optical_time(m,a,d);Uface=mp_boundary(m,a,d,mp.mpf(1))[0]
        rows.append({'kind':'MP_fixed_witness','m':'1','a':'0.1','d':'10','Delta':'60',
                     'T_axis':fmt(T),'U_face':fmt(Uface),'coordinate_margin':fmt(60-T),
                     'proper_margin':fmt((60-T)/Uface)})
        return rows


def all_experiments(dps: int) -> dict:
    return {'rn-smooth-conformal-source': {'verdict':'specified_conformal_trace_tail_mismatch',
                'trials':rn_trials(dps)},
            'mp-same-exterior-handle': {'verdict':'conditional_classical_past_path',
                'trials':mp_trials(dps)}}
