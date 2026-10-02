#!/usr/bin/env python3
"""A scoped auxiliary-volume bounce candidate, NOT a complete QG theory.

Framework action: De Felice, Doll & Mukohyama, arXiv:2004.12549.
Scalar quadratic coefficients: Ganz et al., arXiv:2212.13561v2,
Eqs. (33)-(40). Their published bounce is not the potential tested here.

Chosen potential: V(phi)=(phi**2-mu**2*cos(phi/mu)**2)/3.
We verify background equations, an anisotropic stiff family, and the
signs of the published scalar quadratic action specialized to this model.
The full Dirac reduction, quantum loops, UV completion, nonlinear
inhomogeneous stability, and observational compatibility are NOT verified.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import platform
import sympy as sp


def zero(expr, label):
    result = sp.simplify(sp.trigsimp(expr))
    if result != 0:
        raise AssertionError(f'{label}: {result}')


def action_reduction():
    # ADM convention K_ij=(dot gamma_ij-D_i N_j-D_j N_i)/(2N).
    a,ad,N,M,phi,lam,V,shear2,cd = sp.symbols(
        'a ad N M phi lam V shear2 cd', positive=True, real=True)
    L = M**2*(-3*a*ad**2/N + a**3*shear2/(2*N)
              -N*a**3*V-sp.Rational(3,4)*N*a**3*lam**2
              -lam*(3*a*a*ad+N*a**3*phi)) + a**3*cd**2/(2*N)
    lam_star = -2*ad/(a*N)-sp.Rational(2,3)*phi
    zero(sp.diff(L,lam).subs(lam,lam_star),'lambda equation')
    expected = M**2*a**3*(shear2/(2*N)+2*phi*ad/a
                            +N*(phi**2/3-V))+a**3*cd**2/(2*N)
    zero(L.subs(lam,lam_star)-expected,'reduced homogeneous action')
    return {
        'lambda_eliminated':str(lam_star),
        'L_reduced':'M^2 a^3 [shear_dot_squared/(2N)+2 phi adot/a+N(phi^2/3-V)] + a^3 chidot^2/(2N)',
        'full_Dirac_reduction_recomputed':False,
    }


def homogeneous_family():
    x,mu,M,w,ph = sp.symbols('x mu M w ph', positive=True, real=True)
    V=(ph**2-mu**2*sp.cos(ph/mu)**2)/3
    rho_c=M**2*mu**2/3
    phi=mu*sp.atan(x)
    a=(1+x*x)**(1/(3*(1+w)))
    H=mu*x/(3*(1+x*x))
    rho=rho_c/(1+x*x)
    dxdt=mu*(1+w)/2
    zero(dxdt*sp.diff(a,x)/a-H,'scale-factor derivative')
    zero(V.subs(ph,phi)-phi**2/3+rho/M**2,'density constraint')
    zero(sp.diff(V,ph).subs(ph,phi)/2-phi/3-H,'H constraint')
    zero(dxdt*sp.diff(phi,x)-3*(1+w)*rho/(2*M**2),'phi dynamics')
    zero(dxdt*sp.diff(rho,x)+3*H*(1+w)*rho,'matter conservation')
    zero(3*M**2*H**2-rho*(1-rho/rho_c),'modified Friedmann')
    zero(dxdt*sp.diff(H,x)+(1+w)*rho*(1-2*rho/rho_c)/(2*M**2),
         'acceleration including bounce')
    # The fundamental homogeneous equations remain regular at H=0.
    Hdot0=sp.simplify((dxdt*sp.diff(H,x)).subs(x,0))
    assert Hdot0 == mu**2*(w+1)/6
    return {
        'potential':str(V), 'rho_c':str(rho_c),
        'a':'a_b [1+(mu*(1+w)*t/2)^2]^(1/[3(1+w)])',
        'rho':'rho_c/[1+(mu*(1+w)*t/2)^2]',
        'phi':'mu atan(mu*(1+w)*t/2)',
        'Hdot_at_bounce':str(Hdot0),
        'positive_density_dust_background':True,
        'stiff_scalar_background':True,
        'all_symbolic_residuals_zero':True,
    }


def bianchi_stiff():
    # mu=M=a_b=1; all dimensions restored in the report.
    x,d1,d2=sp.symbols('x d1 d2',real=True)
    ds=[d1,d2,-d1-d2]
    D2=sp.expand(sum(d*d for d in ds))
    a=(1+x*x)**sp.Rational(1,6)
    phi=sp.atan(x)
    H=x/(3*(1+x*x))
    betadot=[d/sp.sqrt(1+x*x) for d in ds]
    chidot=sp.sqrt(sp.Rational(2,3)-D2)/sp.sqrt(1+x*x)
    shear2=sum(q*q for q in betadot)
    W=1/(3*(1+x*x))
    zero(W-(shear2+chidot**2)/2,'lapse constraint, anisotropic family')
    zero(2*sp.diff(phi,x)-3*W-sp.Rational(3,2)*(shear2+chidot**2),
         'scale-factor Euler equation')
    zero(2*H-sp.sin(2*phi)/3,'auxiliary equation, anisotropic family')
    zero(sp.diff(a**3*chidot,x),'scalar field equation')
    for i in range(3):
        zero(sp.diff(a**3*betadot[i],x),f'shear equation {i}')
    Ricci=sp.factor(6*(sp.diff(H,x)+2*H*H))
    Kretsch=sp.factor(12*((sp.diff(H,x)+H*H)**2+H**4))
    zero(Ricci-2*(3-x*x)/(3*(1+x*x)**2),'isotropic Ricci')
    zero(Kretsch-4*(9-12*x*x+5*x**4)/(27*(1+x*x)**4),'isotropic Riemann squared')
    # For |d| constraints, 1.5 d_i^2 <= sum d_j^2 < 2/3,
    # so |d_i|<2/3. Both asymptotic directional exponents exceed -1/3.
    samples=[]
    for values in [(sp.Rational(0),sp.Rational(0)),
                   (sp.Rational(1,5),-sp.Rational(1,10)),
                   (sp.Rational(1,2),-sp.Rational(1,4))]:
        params={d1:values[0],d2:values[1]}
        f=sp.simplify(sp.Rational(3,2)*D2.subs(params))
        assert 0 <= f < 1
        samples.append({'d':[str(q.subs(params)) for q in ds],
                        'constant_shear_fraction':str(f)})
    return {
        'beta_i':'d_i asinh(mu*t), sum d_i=0',
        'chi':'chi0+M sqrt(2/3-sum d_i^2) asinh(mu*t)',
        'allowed_anisotropy':'sum d_i^2<2/3; positive canonical matter density',
        'shear_fraction':'(3/2) sum d_i^2; constant, not an isotropization mechanism',
        'isotropic_R_over_mu2':str(Ricci),
        'isotropic_K_over_mu4':str(Kretsch),
        'causal_geodesic_completeness_argument':
            'Every a_i is positive and smooth at finite t; a_i~|t|^(1/3 +/- d_i), and |d_i|<2/3. For conserved spatial momenta, proper/affine length has asymptotic integrand bounded below by a positive multiple of |t|^p with p>-1/3>-1.',
        'all_symbolic_residuals_zero':True,
        'samples':samples,
        'generic_inhomogeneous_stability':False,
    }


def scalar_quadratic():
    # Substitute the chosen stiff background into the published reduced
    # quadratic action. This is NOT a rederivation of that constraint reduction.
    x,q=sp.symbols('x q',real=True)
    w=sp.Integer(1); cs2=sp.Integer(1)
    H=x/(3*(1+x*x)); rho=1/(3*(1+x*x))
    alpha=sp.factor(rho/H**2)
    eps=sp.factor(-sp.diff(H,x)/H**2)
    eta=sp.factor(sp.diff(eps,x)/(eps*H))
    A1=(1+w)**3*alpha*(12*cs2+(1+w)*alpha-2*eps)/4
    A2=3*(1+w)**4*alpha**2*(6*cs2+(1+w)*alpha-2*eps)/8
    B1=cs2*(1+w)**2*((1+w)**2*alpha**2+6*(1+w)*alpha*(1+3*cs2-eps)+4*eps*eta)/4
    B2=(1+w)**3*alpha*(-(1+w)**2*alpha**2+2*(1+w)*alpha*(6*cs2+9*cs2**2+(2-3*cs2)*eps)+4*eps*(-(1+3*cs2)*eps+3*cs2*(1+3*cs2+eta)))/8
    cr=sp.factor((cs2**2*(1+w)**2*q**4+B1*H**2*q*q+B2*H**4)/(cs2*(1+w)**2*q**4+A1*H**2*q*q+A2*H**4))
    Z=sp.factor(alpha*(1+w)*(q*q+sp.Rational(3,2)*(1+w)*alpha*H**2)/(cs2*(q*q+sp.Rational(3,2)*(1+w)*alpha*H**2)+(1+w)*alpha*H**2*((1+w)*alpha/2-eps)/2))
    num=3*q**4*x*x*(1+x*x)**3+6*q*q*(1+x*x)**2*(x*x+3)+3*x**4+13*x*x+2
    den=3*(1+x*x)*(q*q*(1+x*x)+1)*(q*q*x*x*(1+x*x)+x*x+2)
    Ztarget=6*(1+x*x)*(q*q*(1+x*x)+1)/(q*q*x*x*(1+x*x)+x*x+2)
    zero(cr-num/den,'scalar gradient rational expression')
    zero(Z-Ztarget,'scalar kinetic rational expression')
    # Polynomial certificate, valid for all real x and real q, not a scan.
    for poly in (num,den,sp.fraction(Ztarget)[0],sp.fraction(Ztarget)[1]):
        terms=sp.Poly(sp.expand(poly),x,q).terms()
        assert all(c>0 and all(e%2==0 for e in powers) for powers,c in terms)
        assert sp.Poly(sp.expand(poly),x,q).coeff_monomial(1)>0
    rows=[]
    for xx in (0,1,2):
        for qq in (sp.Rational(1,10),1,10):
            rows.append({'mu_t':xx,'k_over_a_mu':str(qq),
                         'Z':str(sp.N(Z.subs({x:xx,q:qq}),18)),
                         'c_R_squared':str(sp.N(cr.subs({x:xx,q:qq}),18))})
    # A leading high-frequency boundary-layer control only: NOT a complete
    # Hadamard propagation or high-frequency particle-production calculation.
    u=sp.symbols('u',real=True)
    wave=sp.exp(-sp.I*u)*(u+sp.I)/sp.sqrt(u*u+2)
    omega2=1+(2*u*u+10)/(u*u+2)**2
    zero(sp.diff(wave,u,2)+omega2*wave,'leading UV boundary-layer solution')
    return {
        'source':'arXiv:2212.13561v2 Eqs. 33-40, specialized to canonical stiff matter',
        'variables':'x=mu*t; q=k/(a*mu); Z=z^2/a^2; k!=0 physical scalar modes',
        'Z':str(sp.factor(Ztarget)),
        'c_R_squared':str(sp.factor(num/den)),
        'Z_positive_all_finite_x_q':True,
        'c_R_squared_positive_all_finite_x_q':True,
        'homogeneous_limits_removable_in_reduced_coefficients':True,
        'c_R_squared_at_bounce':str(sp.factor(cr.subs(x,0))),
        'strict_metric_microcausality_proved':False,
        'strong_coupling_control':False,
        'all_perturbations_bounded_for_all_times_proved':False,
        'full_quantum_Hadamard_completion':False,
        'leading_UV_boundary_layer_solution':str(wave),
        'rows':rows,
    }


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    args=p.parse_args()
    result={
        'name':'B1 auxiliary-volume candidate (a specified VCDM potential)',
        'framework_is_existing_research':True,
        'potential_selected_by_inverse_design_not_derived_from_quantum_gravity':True,
        'action_check':action_reduction(),
        'homogeneous_family':homogeneous_family(),
        'anisotropic_stiff_family':bianchi_stiff(),
        'linear_scalar_check':scalar_quadratic(),
        'all_implemented_symbolic_checks_passed':True,
        'full_quantum_gravity_claim':False,
        'generic_singularity_resolution_claim':False,
        'observational_fit_performed':False,
        'environment':{'python':platform.python_version(),'sympy':sp.__version__},
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    text=json.dumps(result,ensure_ascii=False,indent=2)+'\n'
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(text,encoding='utf-8')
    print(text)

if __name__=='__main__':
    main()
