#!/usr/bin/env python3
"""R3: a specified nonlinear preferred-foliation Hamiltonian candidate.

The trace constraint is a NEW assumption, not derived from the R1 graph.
Two gravitational modes are counted only on the regular second-class branch.
Finite-order A_m replaces R1's exponential; the Gaussian limit is a static
comparison, not a proved nonlinear or quantum continuum limit.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import platform
from pathlib import Path
import mpmath as mp
import sympy as sp

BASE_SHA = '7e25b4db8a81b6287c9f07e593a1c0f2310132de'
ORDERS = (2, 4, 8, 16, 32)


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def text(x):
    return mp.nstr(x, 42)


def matching_and_constraints():
    k, b, c, z, h, rho, msq, a = sp.symbols('k b c z h rho M2 A', positive=True)
    # k points along z; scalar gamma_ij=e^(2z)delta_ij.
    ric_s = sp.diag(k*k*z, k*k*z, 2*k*k*z)
    r_s = sp.trace(ric_s)
    coeff = sp.expand(-sp.trace(ric_s*ric_s)+c*r_s*r_s)
    chosen = sp.solve(sp.Eq(coeff, 2*k**4*z*z), c)[0]
    require(chosen == sp.Rational(1,2), 'scalar/tensor matching coefficient')
    ric_tt = sp.diag(k*k*h/2, -k*k*h/2, 0)
    require(sp.trace(ric_tt*ric_tt) == k**4*h*h/2, 'TT curvature norm')
    # V^(2)_scalar=2 A k^2 z^2 +4 A k^2 n z;
    # H^(1)=-2 M2 A k^2 z+rho. Static matter has no spatial stress.
    lapse, zz = sp.symbols('n zz')
    stat = msq/2*(2*a*k*k*zz*zz+4*a*k*k*lapse*zz)-rho*lapse
    solution = sp.solve([sp.diff(stat,lapse),sp.diff(stat,zz)],[lapse,zz])
    require(sp.simplify(solution[lapse]+solution[zz]) == 0, 'Phi=Psi')
    # C=pi generates delta z=epsilon/2, hence {H,C}=-M2 A k^2.
    dirac_symbol = -msq*a*k*k
    b1,b2,q = sp.symbols('b1 b2 q', real=True)
    block = sp.Matrix([[0,q,b1,0],[-q,0,0,b2],[-b1,0,0,0],[0,-b2,0,0]])
    require(sp.factor(block.det()) == b1*b1*b2*b2, 'Dirac block determinant')
    # Canonical TT oscillator: inverse A in H, A in reduced L.
    p,qd = sp.symbols('p qdot')
    ham = 2*p*p/(msq*a)+msq*a*k*k*h*h/8
    ps = sp.solve(sp.Eq(qd,sp.diff(ham,p)),p)[0]
    lag = sp.simplify((p*qd-ham).subs(p,ps))
    require(sp.simplify(lag-msq*a*(qd*qd-k*k*h*h)/8)==0,'TT Legendre transform')
    # Explicit conformal integration at ell=0 checks the EH bulk coefficient.
    x,e = sp.symbols('x e', real=True)
    f=sp.cos(x)+sp.sin(2*x)/3
    eh2=-4*f*sp.diff(f,x,2)-2*sp.diff(f,x)**2
    require(sp.integrate(sp.expand_trig(eh2-2*sp.diff(f,x)**2),(x,0,2*sp.pi))==0,'conformal EH integral')
    return {
        'curvature_coefficient': str(chosen),
        'static_lapse': str(solution[lapse]),
        'static_conformal_factor': str(solution[zz]),
        'flat_Dirac_symbol': str(dirac_symbol),
        'Dirac_block_determinant': str(sp.factor(block.det())),
        'regular_branch_gravitational_dof': (12-2*3-2)//2,
        'TT_reduced_action': 'M2/8 integral [hdot A hdot - dh A dh]',
        'two_modes_scope': 'Requires invertible {H,pi}, boundary conditions, and pi=0. No global rank or nonlinear well-posedness theorem is claimed.',
        'ordinary_GR_limit': 'ell=0: ADM GR restricted to maximal slicing where that slicing exists',
        'full_GR_refoliation_algebra_proved': False,
    }


def polynomials():
    y=sp.symbols('y')
    f=sp.Integer(1); total=0; result={}
    for j in range(1,max(ORDERS)+1):
        total=sp.expand(total+f)
        if j in ORDERS:
            cs=sp.Poly(total,y).all_coeffs()
            result[j]=[mp.mpf(int(v.p))/int(v.q) for v in cs]
        f=sp.expand(((2*j-2+y)*f-y*sp.diff(f,y))/(2*j))
    return result


def kernel(m, r, polys):
    if r < 0:
        r=-r
    if not r:
        return mp.sqrt(m)*mp.gamma(m-mp.mpf('.5'))/(mp.sqrt(mp.pi)*mp.gamma(m))
    y=mp.sqrt(m)*r
    return (1-mp.exp(-y)*mp.polyval(polys[m],y))/r


def hierarchy():
    ps=polynomials(); rows=[]
    for m in ORDERS:
        fun=lambda d:2*kernel(m,3*d,ps)-kernel(m,4*d,ps)-kernel(m,2*d,ps)
        root=mp.findroot(fun,(mp.mpf('.2'),mp.mpf('.9')),solver='anderson')
        require(root>mp.mpf('.1') and abs(fun(root))<mp.mpf('1e-40'),'nontrivial phase root')
        freq2=mp.power(m,mp.mpf('1.5'))*mp.gamma(m-mp.mpf('1.5'))/(6*mp.sqrt(mp.pi)*mp.gamma(m))
        binding=mp.quad(lambda k:mp.exp(-k*k)/(1+k*k/m)**m,[0,1,mp.inf])/mp.pi
        rows.append({'order':m,'point_probe_node':text(root),'center_kernel':text(kernel(m,mp.mpf(0),ps)),
                     'Omega0_squared_ell3_over_GM':text(freq2),'gaussian_sigma1_binding_magnitude':text(binding)})
    gauss=lambda r:mp.erf(r/2)/r
    rinf=mp.findroot(lambda d:2*gauss(3*d)-gauss(4*d)-gauss(2*d),('.5','.8'))
    return {'A_m':'(1+ell^2 L/m)^m','B_m':'(A_m-1)/L, polynomially extended at L=0',
            'rows':rows,'Gaussian_point_probe_node':text(rinf),
            'Gaussian_Omega0_squared_ell3_over_GM':text(1/(6*mp.sqrt(mp.pi))),
            'point_probe_node_is_apparatus_independent':False,
            'nonlinear_m_to_infinity_limit_proved':False}


def inverse_operator_variation():
    L=mp.matrix([[2,-1,0],[-1,3,-1],[0,-1,2]])
    dL=mp.matrix([[1,mp.mpf('.2'),0],[mp.mpf('.2'),-mp.mpf('.3'),mp.mpf('.1')],[0,mp.mpf('.1'),mp.mpf('.4')]])
    p=mp.matrix([1,mp.mpf('.3'),mp.mpf('-.7')]); m=2
    Q=mp.eye(3)+L/m; A=Q**m; inv=A**-1
    dA=(dL*Q+Q*dL)/m
    dinv=-inv*dA*inv
    analytic=(p.T*dinv*p)[0]
    step=mp.mpf('1e-12')
    def energy(e):
        qq=mp.eye(3)+(L+e*dL)/m
        return (p.T*(qq**m)**-1*p)[0]
    numerical=(energy(step)-energy(-step))/(2*step)
    require(abs(analytic-numerical)<mp.mpf('1e-23'),'Frechet derivative')
    require(abs(analytic)>mp.mpf('.01'),'frozen-operator negative control')
    return {'dA_inverse':'-A_inverse (dA) A_inverse','analytic_energy_derivative':text(analytic),
            'finite_difference_energy_derivative':text(numerical),'error':text(abs(analytic-numerical)),
            'naively_freezing_A_is_accepted':False,
            'scope':'Noncommuting finite-matrix test of the operator variation, not a full curved-space field-equation solve'}


def p2_and_binding():
    r,s=sp.symbols('r s',positive=True)
    kap=(1-sp.exp(-r/s)*(1+r/(2*s)))/r
    lap=lambda f:sp.diff(f,r,2)+2*sp.diff(f,r)/r
    Le=lambda f:-lap(f)
    require(sp.simplify(Le(kap)+2*s*s*Le(Le(kap))+s**4*Le(Le(Le(kap))))==0,'P2 radial Green equation away from source')
    density=sp.simplify(-lap(kap)/(4*sp.pi))
    require(sp.simplify(density-sp.exp(-r/s)/(8*sp.pi*s**3))==0,'P2 effective density')
    require(sp.integrate(4*sp.pi*r*r*density,(r,0,sp.oo))==1,'P2 density normalization')
    aa=1/mp.sqrt(2)
    def k2(x):
        return (1-mp.exp(-x/aa)*(1+x/(2*aa)))/x if x else 1/(2*aa)
    # Smooth coordinate rest-density rho=M Gaussian(sigma). Not a stationary dust star.
    sigma=mp.mpf(1)
    pair=mp.quad(lambda x:4*mp.pi*x*x*mp.exp(-x*x/(4*sigma*sigma))*k2(x)/(4*mp.pi*sigma*sigma)**mp.mpf('1.5'),[0,1,mp.inf])/2
    field=mp.quad(lambda k:mp.exp(-sigma*sigma*k*k)/(1+k*k/2)**2,[0,1,mp.inf])/mp.pi
    require(abs(pair-field)<mp.mpf('1e-40'),'ADM binding equals pair energy')
    # 16 pi G M_ADM +2 Igrad =16 pi G Mrest; Igrad=4 pi G int rho zeta1.
    return {'kernel':'[1-exp(-sqrt(2)r/ell)(1+r/(sqrt(2)ell))]/r',
            'effective_density':'exp(-r/a)/(8 pi a^3), a=ell/sqrt(2)',
            'center_kernel_ell':text(1/(2*aa)),
            'Omega0_squared_ell3_over_GM':text(1/(6*aa**3)),
            'binding_mass_formula':'M_ADM=M_rest-(G/2) int rho(x)rho(y)K_m(|x-y|) dxdy +O(G^2), c=1',
            'binding_coefficient_pair_space':text(pair),'binding_coefficient_field_space':text(field),
            'mass_ratio_example_epsilon_0p01_through_first_correction':text(1-mp.mpf('.01')*pair),
            'binding_scope':'Time-symmetric, smooth, weak asymptotically-flat initial data; integrated constraint through quadratic metric order. No full nonlinear initial-data solution is asserted.'}


def domain_failures():
    t=sp.symbols('t',positive=True)
    scale=t**sp.Rational(2,3)
    H=sp.diff(scale,t)/scale
    R4=sp.simplify(6*(sp.diff(H,t)+2*H*H))
    kretsch=sp.simplify(12*((sp.diff(scale,t,2)/scale)**2+H**4))
    require(R4==4/(3*t*t) and kretsch==80/(27*t**4),'CMC FLRW counterexample')
    return {'maximal_trace_constraint_on_homogeneous_positive_density_flat_slice':'pi=0 gives p=0 and R3=0, so H=rho cannot vanish; not a cosmological branch',
            'optional_CMC_replacement':'C=pi-sqrt(gamma)*<pi/sqrt(gamma)>; global mode must be retained, not counted as a propagating scalar',
            'CMC_extension_has_been_fully_analyzed':False,
            'homogeneous_CMC_control':'If this extension is used, L=R3=0 leaves the GR flat-FLRW equations unchanged',
            'dust_FLRW_R4':str(R4),'dust_FLRW_Kretschmann':str(kretsch),
            'generic_singularity_resolution':False,
            'strict_metric_microcausality':False,
            'radiatively_protected_coefficients':False,
            'complete_quantum_gravity':False}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    with mp.workdps(55):
        data={'base_sha':BASE_SHA,'model':'R3_m nonlinear Hamiltonian candidate with preferred foliation and second-class trace constraint',
              'new_assumptions':['pi=0 on the asymptotically-flat branch','finite polynomial A_m for a specified m','specified nonlinear curvature operator ordering'],
              'matching':matching_and_constraints(),'hierarchy':hierarchy(),
              'operator_variation':inverse_operator_variation(),'P2_binding':p2_and_binding(),
              'limits':domain_failures(),'all_implemented_assertions_passed':True,
              'environment':{'python':platform.python_version(),'sympy':sp.__version__,'mpmath':mp.__version__},
              'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'passed':True,'dof_on_regular_branch':data['matching']['regular_branch_gravitational_dof'],
                      'P2_node':data['hierarchy']['rows'][0]['point_probe_node'],
                      'P2_binding':data['P2_binding']['binding_coefficient_pair_space'],
                      'global_nonlinear_wellposedness':False,'complete_QG':False}))


if __name__=='__main__':
    main()
