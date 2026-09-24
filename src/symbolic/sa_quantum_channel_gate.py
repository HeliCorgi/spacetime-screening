"""4D Schein--Aichelburg scalar junction and finite-pulse channel audit.

References and scope: notes/sa-quantum-channel-gate.md.
Kehle--Shlapentokh-Rothman Theorem 5 supplies the analytic scattering-tail
result; this script verifies its specialization, not that theorem itself.
No global two-shell Wightman function or past probability is manufactured.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
import mpmath as mp
import sympy as s

BASE = '2304cbc39b638491d20cb9ece2f44b05bb216426'


def exact_checks() -> dict:
    t,x,y,z,r,th,ph=s.symbols('t x y z r th ph', real=True)
    U=s.Function('U')(x,y,z); P=s.Function('P')(t,x,y,z)
    inv=s.diag(-U**2,U**-2,U**-2,U**-2); coords=(t,x,y,z)
    box=sum(s.diff(U**2*inv[i,i]*s.diff(P,coords[i]),coords[i]) for i in range(4))/U**2
    assert s.simplify(box+U**2*s.diff(P,t,2)-sum(s.diff(P,c,2) for c in (x,y,z))/U**2)==0
    m,e=s.symbols('m e',positive=True); f=1-2*m/r+e**2/r**2
    u=s.Function('u')(t,r); pot0=f*s.diff(f,r)/r
    for ell in (0,1,2):
        angular=s.legendre(ell,s.cos(th)); field=u/r*angular
        boxrn=-s.diff(field,t,2)/f+s.diff(r*r*f*s.diff(field,r),r)/r**2+s.diff(s.sin(th)*s.diff(field,th),th)/(r*r*s.sin(th))
        reduced=-s.diff(u,t,2)+f*s.diff(f*s.diff(u,r),r)-(pot0+f*ell*(ell+1)/r**2)*u
        assert s.simplify(s.trigsimp(r*f*boxrn-angular*reduced))==0
    # Same proper clock and same oriented scalar KG flux, with no shell coupling.
    U0,fa,wm=s.symbols('U0 fa wm',positive=True)
    wrn=U0*s.sqrt(fa)*wm
    assert s.simplify(wrn/s.sqrt(fa)-U0*wm)==0
    drout=s.symbols('drout'); drin=drout/(U0*s.sqrt(fa))
    assert s.simplify(s.sqrt(fa)*drin-drout/U0)==0
    # Regular radial endpoint for phi despite singular metric; two L2 branches.
    D=r*r*f; w=r*r/f
    assert s.limit(D,r,0)==e**2 and s.limit(w/r**4,r,0)==1/e**2
    V=f*s.diff(f,r)/r
    assert s.limit(r**6*V,r,0)==-2*e**4
    alpha=s.symbols('alpha'); assert s.solve(alpha*(alpha-1)+s.Rational(2,9),alpha)==[s.Rational(1,3),s.Rational(2,3)]
    # Boundary Wronskian depends on c0,c1; a real Robin relation nulls it.
    a,b,c,d,beta=s.symbols('a b c d beta',real=True)
    boundary=e**2*(a*d-b*c)
    assert s.simplify(boundary.subs({b:beta*a/e**2,d:beta*c/e**2}))==0
    # Imported zero-frequency coefficients, independently checking constraints.
    rp,rm=s.symbols('rp rm',positive=True)
    T=(rm/rp+rp/rm)/2; R=(rm/rp-rp/rm)/2
    assert s.simplify(T*T-R*R)==1 and s.simplify(T+R-rm/rp)==0
    # Pulse moment polynomial: compact support makes all boundary terms vanish.
    nu=s.symbols('nu')
    for n in range(1,6):
        Q=s.prod(1-nu/s.Integer(j) for j in range(1,n+1))
        assert Q.subs(nu,0)==1
        assert all(Q.subs(nu,j)==0 for j in range(1,n+1))
    # Same DEC lower bound for 1/2 <= e/m < 1, R=m1=1,d=3,m=1/5,A=2.
    grad=s.Rational(216151,345600)
    margin=grad-s.Rational(21,100)-s.Rational(1,179)
    assert margin==s.Rational(1014173,2474496)>0
    return {'4d_wave_operators':True,'shell_clock_and_kg_flux':True,
            'origin_boundary_not_fixed_by_shells':True,'zero_frequency_flux_identity':True,
            'moment_cancellations_N_1_to_5':True,'DEC_margin_coefficient':str(margin),
            'scattering_tail_theorem':'imported KSR Theorem 5; not numerically reproved',
            'global_quantum_state_constructed':False}


def calculations(dps: int) -> dict:
    with mp.workdps(dps):
        def h(v):
            return mp.exp(-1/(1-v*v)) if abs(v)<1 else mp.mpf(0)
        def hp(v):
            return -2*v/(1-v*v)**2*h(v) if abs(v)<1 else mp.mpf(0)
        def hpp(v):
            if abs(v)>=1: return mp.mpf(0)
            a=1-v*v
            return (4*v*v/a**4-2/a**2-8*v*v/a**3)*h(v)
        cut=[-1,-mp.mpf(3)/4,-mp.mpf(1)/4,0,mp.mpf(1)/4,mp.mpf(3)/4,1]
        integrate=lambda fn:mp.quad(fn,cut)
        area=integrate(h); moment=integrate(lambda v:mp.exp(v)*h(v))
        shaped=integrate(lambda v:mp.exp(v)*(hp(v)+h(v)))
        assert abs(shaped)<mp.mpf('1e-45')
        assert abs(integrate(lambda v:hp(v)+h(v))-area)<mp.mpf('1e-45')
        E0=integrate(lambda v:hp(v)**2); E1=integrate(lambda v:(hpp(v)+hp(v))**2)
        assert E0>0 and E1>E0
        second=integrate(lambda v:mp.exp(2*v)*(hp(v)+h(v)))
        assert abs(second+integrate(lambda v:mp.exp(2*v)*h(v)))<mp.mpf('1e-45')
        rows=[]
        for qtext in ('.5','.99','.999'):
            q=mp.mpf(qtext); M=mp.mpf(1)/5; Q=M*q; d=mp.sqrt(M*M-Q*Q)
            rp=M+d; rm=M-d; kp=d/rp**2; km=d/rm**2; p=kp/km
            fA=1-M+Q*Q/4; clock=2*mp.sqrt(fA)
            assert mp.mpf(179)/200<mp.sqrt(fA)<mp.mpf(9)/10
            assert rp!=3*rm  # ell=0 avoids the KSR first-pole exceptional case.
            assert 0<p<1
            T0=(rm/rp+rp/rm)/2; R0=(rm/rp-rp/rm)/2
            assert abs(T0*T0-R0*R0-1)<mp.mpf('1e-45')
            rows.append({'charge_ratio':q,'r_plus':rp,'r_minus':rm,'kappa_plus':kp,'kappa_minus':km,
                'p':p,'uncancelled_signal_stress_power':2*p-2,
                'second_outer_pole_stress_power':4*p-2,
                'T_zero':T0,'R_zero':R0,'MP_clock_duration_of_prescribed_horizon_bump':2*clock/kp,
                'potentially_dangerous_outer_pole_slots':int(mp.ceil(1/p)-1)})
        near=rows[1]; sensitivity=[]
        for X in ('1e-3','1e-6','1e-12'):
            xv=mp.mpf(X)
            sensitivity.append({'abs_Vbar':xv,'unit_prefactor_derivative_tolerance':xv**(1-near['p'])})
        def encode(v):
            if isinstance(v,dict):return {k:encode(val) for k,val in v.items()}
            if isinstance(v,list):return [encode(val) for val in v]
            if isinstance(v,mp.mpf):return mp.nstr(v,46)
            return v
        return encode({'area':area,'uncancelled_Laplace_moment':moment,
            'shaped_first_moment_exact':'0','E0_shape_integral':E0,'E1_shape_integral':E1,
            'equal_area_horizon_energy_ratio':E1/E0,'shaped_second_Laplace_moment':second,
            'geometry_rows':rows,'near_extremal_sensitivity':sensitivity,
            'critical_charge_ratio_for_two_p_greater_one':mp.sqrt(1-(3-2*mp.sqrt(2))**2),
            'past_probability':None,'past_probability_computed':False})


def compare(a, b):
    if isinstance(a,dict):
        assert a.keys()==b.keys()
        for k in a: compare(a[k],b[k])
    elif isinstance(a,list):
        assert len(a)==len(b)
        for x,y in zip(a,b):compare(x,y)
    elif isinstance(a,str):
        with mp.workdps(90):
            try: x,y=mp.mpf(a),mp.mpf(b)
            except ValueError: assert a==b; return
            assert abs(x-y)<=mp.mpf('1e-40')*max(1,abs(x),abs(y)),(a,b)
    else: assert a==b


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    exact=exact_checks(); low=calculations(50);high=calculations(80);compare(low,high)
    result={'source_base_sha':BASE,'python':platform.python_version(),'sympy':s.__version__,'mpmath':mp.__version__,
        'precision_dps':[50,80],'code_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'exact':exact,'calculations':high,'status':'diagnostics_passed_not_A'}
    text=json.dumps(result,indent=2,ensure_ascii=False,allow_nan=False)
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(text+'\n',encoding='utf-8')
    print(text)
    print('PASS 4D junction, pulse moments and 50/80-digit checks. No complete past receiver probability.')


if __name__=='__main__': main()
