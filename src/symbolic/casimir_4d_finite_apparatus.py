"""Finite Casimir source completion: forces, supports and negative line energy.

4D Maxwell vacuum + ordinary DEC material in the local-flat parallel-plate
regime; not a no-go for every Casimir geometry or positive-ADM-mass wormhole.
Costa & Matsas, arXiv:2112.08881v3, Eqs. (12)-(22).
Additional applications and boundaries: accompanying research note.
"""
from __future__ import annotations

import platform
import sympy as sp
import mpmath as mp


def exact_checks() -> None:
    u,A,d,S,kappa = sp.symbols('u A d S kappa', positive=True)
    force=3*u*A
    rho_strut=kappa*force/S
    vacuum_energy=-u*A*d
    strut_energy=sp.simplify(rho_strut*S*d)
    total=sp.factor(vacuum_energy+strut_energy)
    assert total == A*d*u*(3*kappa-1)
    assert total.subs(kappa,1) == 2*A*d*u
    assert sp.diff(strut_energy,S) == 0
    # DEC requires kappa>=1. Thinner struts do not lower the energy bound.
    z=sp.symbols('z',real=True)
    slab=sp.Heaviside(z)-sp.Heaviside(z-d)
    field_pzz=-3*u*slab
    material_pzz=3*u*slab
    assert sp.diff(field_pzz+material_pzz,z) == 0
    assert sp.diff(field_pzz,z) != 0
    Q=sp.symbols('Q',positive=True)
    eps_f,eps_e=sp.symbols('eps_f eps_e',nonnegative=True)
    robust=3*Q*(1-eps_f)-Q*(1+eps_e)
    assert sp.expand(robust-Q*(2-3*eps_f-eps_e)) == 0
    assert robust.subs({eps_f:sp.Rational(1,10),eps_e:sp.Rational(1,10)}) == 8*Q/5
    for fraction in (sp.Rational(1,1000),sp.Rational(1,10),sp.Integer(1)):
        assert sp.simplify(strut_energy.subs(S,fraction*A)-kappa*force*d) == 0
    assert total.subs(kappa,sp.Rational(1,4)) < 0
    assert rho_strut.subs(kappa,sp.Rational(1,4))-force/S < 0

    # Vacuum normals transverse to a prospective string tangent z.
    ux,uy=sp.symbols('ux uy',nonnegative=True)
    U=ux+uy
    field=sp.diag(-U,-3*ux+uy,ux-3*uy,U)
    target=sp.diag(-Q,0,0,Q)
    apparatus=target-field
    assert sp.expand(apparatus[1,1]+apparatus[2,2]) == 2*U
    assert sp.expand(apparatus[1,1]+apparatus[2,2]-2*apparatus[0,0]) == 2*Q
    # DEC gives p_x+p_y <= 2 rho: contradiction by 2Q>0.
    # Negative control: arbitrary normals do NOT obey that theorem.
    weights=(3*Q/4,3*Q/4,Q/2)
    UU=sum(weights)
    arbitrary=sp.diag(-UU,*(UU-4*w for w in weights))
    ordinary=sp.diag(Q,Q,Q,Q)  # algebraic DEC saturation, not a built material.
    assert arbitrary+ordinary == target
    c,s=sp.symbols('c s',real=True)
    P=U*sp.eye(3)-4*U*sp.Matrix([c,s,0])*sp.Matrix([[c,s,0]])
    assert sp.expand(P[0,0]+P[1,1]+2*U).subs(s**2,1-c**2).expand() == 0
    print('EXACT: finite-area force balance + DEC imply E_struts>=3|E_Cas|, E_all>=2|E_Cas|.')
    print('EXACT: support area cancels; dropping supports violates distributional conservation.')
    print('EXACT: transverse Casimir-vacuum normals + pointwise DEC cannot match a negative pure-string tensor.')
    print('NEGATIVE CONTROL: unrestricted orientations can match algebraically; no universal material theorem claimed.')


def numerical_checks(dps: int) -> tuple[mp.mpf,...]:
    with mp.workdps(dps):
        hbar=mp.mpf('1.054571817e-34');c=mp.mpf('299792458');G=mp.mpf('6.67430e-11')
        A=mp.mpf('1e-4');d=mp.mpf('1e-6')
        u=mp.pi**2*hbar*c/(720*d**4)
        E=u*A*d;F=3*u*A
        for frac in ('1','0.01','0.000001'):
            S=mp.mpf(frac)*A
            minimum=(F/S)*S*d
            assert abs(minimum-3*E)<mp.mpf(10)**(-dps+5)*E
        mu=-c**4/(4*G)
        radius=mp.mpf(1);ring=2*mp.pi*radius*mu
        replacement_min=2*abs(ring)
        print(f'dps={dps}; area=1cm^2, gap=1um: E_Cas={mp.nstr(-E,24)} J, force={mp.nstr(F,24)} N')
        print(f'  E_struts>={mp.nstr(3*E,24)} J; E_all>={mp.nstr(2*E,24)} J (plates omitted only from lower bound)')
        print(f'  FKZ target 1m-ring line integral={mp.nstr(ring,12)} J; algebraic cell sum={mp.nstr(replacement_min,12)} J')
        return tuple(+v for v in (E,F,mu,ring,replacement_min))


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}; mpmath {mp.__version__}')
    exact_checks()
    low=numerical_checks(50);high=numerical_checks(80)
    with mp.workdps(80):
        for a,b in zip(low,high):
            assert abs(a-b)<mp.mpf('1e-40')*abs(b)
    print('PASS restricted finite-apparatus checks. Edge/curvature corrections and a full ring assembly are not solved.')
    print('The large ring cell sum is algebraic, NOT a solved strongly self-gravitating device.')
    print('Positive total energy does NOT by itself exclude a wormhole with a negative local pocket.')


if __name__ == '__main__':
    main()
