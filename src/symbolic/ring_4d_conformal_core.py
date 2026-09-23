"""4D smooth negative-cone core: Einstein trace vs conformal quantum matter.

All four dimensions are retained; a straight-core diagnostic, NOT a finite
FKZ ring solution. No 2D QEI is used. Duff, hep-th/9308075, Eqs. (21),(30),(31);
FKZ negative conical source: arXiv:2305.03887. Domain in the accompanying note.
"""
from __future__ import annotations

import platform
import sympy as sp
import mpmath as mp


def exact_checks() -> None:
    t,z,r,phi=sp.symbols('t z r phi',real=True)
    coords=(t,z,r,phi)
    S=sp.Function('S')(r)
    g=sp.diag(-1,1,1,S*S);gi=sp.diag(-1,1,1,1/(S*S))
    Gamma=[[[sp.simplify(sum(gi[i,k]*(sp.diff(g[k,j],coords[l])+sp.diff(g[k,l],coords[j])
                        -sp.diff(g[j,l],coords[k])) for k in range(4))/2)
             for l in range(4)] for j in range(4)] for i in range(4)]
    Riem={}
    for i in range(4):
        for j in range(4):
            for k in range(4):
                for l in range(4):
                    value=sp.diff(Gamma[i][j][l],coords[k])-sp.diff(Gamma[i][j][k],coords[l])
                    value+=sum(Gamma[i][a][k]*Gamma[a][j][l]-Gamma[i][a][l]*Gamma[a][j][k] for a in range(4))
                    value=sp.simplify(value)
                    if value != 0: Riem[i,j,k,l]=value
    Ric=sp.Matrix(4,4,lambda j,l:sp.simplify(sum(Riem.get((i,j,i,l),0) for i in range(4))))
    R=sp.simplify(sum(gi[i,i]*Ric[i,i] for i in range(4)))
    assert sp.simplify(R+2*sp.diff(S,r,2)/S) == 0
    Einstein=(Ric-g*R/2).applyfunc(sp.simplify)
    expected=sp.diag(-sp.diff(S,r,2)/S,sp.diff(S,r,2)/S,0,0)
    assert (Einstein-expected).applyfunc(sp.simplify) == sp.zeros(4)
    ric2=sp.simplify(sum(gi[i,i]*gi[j,j]*Ric[i,j]**2 for i in range(4) for j in range(4)))
    riem2=sp.simplify(sum(g[i,i]*gi[j,j]*gi[k,k]*gi[l,l]*v*v
                            for (i,j,k,l),v in Riem.items()))
    assert sp.simplify(ric2-R**2/2) == 0
    assert sp.simplify(riem2-R**2) == 0
    assert sp.simplify(riem2-4*ric2+R**2) == 0  # Euler density.
    assert sp.simplify(riem2-2*ric2+R**2/3-R**2/3) == 0  # Weyl^2=R^2/3.
    mix=gi*Einstein
    for j in range(4):
        divergence=sum(sp.diff(mix[i,j],coords[i]) for i in range(4))
        divergence+=sum(Gamma[i][i][k]*mix[k,j]-Gamma[k][i][j]*mix[i,k]
                        for i in range(4) for k in range(4))
        assert sp.simplify(divergence) == 0

    eps,s=sp.symbols('eps s',positive=True)
    profile=r+s*(r-eps*sp.atan(r/eps))
    Spr=sp.diff(profile,r);Spp=sp.diff(profile,r,2)
    assert sp.simplify(Spp-2*s*r*eps**2/(r*r+eps**2)**2) == 0
    assert Spr.subs(r,0) == 1
    assert sp.limit(Spr,r,sp.oo) == 1+s
    RR=sp.factor(-2*Spp/profile)
    assert sp.limit(RR,r,0) == -4*s/eps**2
    G=sp.symbols('G',positive=True)
    assert sp.integrate(-Spp/(4*G),(r,0,sp.oo)) == -s/(4*G)
    assert sp.limit(profile*sp.diff(RR,r),r,0) == 0
    assert sp.limit(profile*sp.diff(RR,r),r,sp.oo) == 0
    lapR=sp.factor(sp.diff(profile*sp.diff(RR,r),r)/profile)
    assert sp.limit(r**4*RR,r,sp.oo) == -4*s*eps**2/(1+s)
    assert sp.limit(r**4*RR**2,r,sp.oo) == 0
    assert sp.limit(r**4*lapR,r,sp.oo) == 0
    # c_W is the anomaly coefficient, not light speed: scalar 1/120,
    # Dirac 1/20, Maxwell 1/10. Integrated Box R vanishes in this domain.
    cw=sp.symbols('cw',positive=True)
    ratio=sp.simplify((1/(8*sp.pi*G))/(cw/(48*sp.pi**2)))
    assert ratio == 6*sp.pi/(cw*G)
    print('EXACT 4D: all Einstein components, Bianchi identity, Riemann/Ricci/Weyl/Euler contractions.')
    print('CORE: mu=-s/(4G), negative angle deficit=-2*pi*s; thickness does not dilute its integrated source.')
    print('ANOMALY NECESSARY CONDITION: sup(-R)*lP^2 >= 6*pi/c_W for S_doubleprime>=0.')
    print('The integrated Box R term vanishes; finite curvature-squared counterterms cannot remove this bound.')
    print('PROFILE CONTROL: its R~r^-4 tail cannot match conformal trace terms ~r^-6 or faster at any thickness.')


def numerical_checks(dps: int) -> tuple[mp.mpf,...]:
    with mp.workdps(dps):
        s=mp.mpf(1)
        f=lambda u:(1+s)*u-s*mp.atan(u)
        fpp=lambda u:2*s*u/(1+u*u)**2
        integrand=lambda u:fpp(u)**2/f(u) if u else mp.mpf(0)
        Q=mp.quad(integrand,[0,1,4,mp.inf])
        def compact(v: mp.mpf) -> mp.mpf:
            u=mp.tan(v)
            return integrand(u)*(1+u*u)
        Q2=mp.quad(compact,[0,mp.pi/4,mp.atan(4),mp.pi/2])
        assert abs(Q-Q2)<mp.mpf(10)**(-dps+7)
        totalR=mp.quad(lambda u:-4*mp.pi*fpp(u),[0,1,mp.inf])
        assert abs(totalR+4*mp.pi*s)<mp.mpf(10)**(-dps+7)
        cw=mp.mpf(1)/10
        eps_over_lp=mp.sqrt(cw*Q/(3*mp.pi*s))
        bound=6*mp.pi/cw
        peak=4*s/eps_over_lp**2
        assert peak>bound
        print(f'dps={dps}; s=1: Q={mp.nstr(Q,35)}, integral R dA={mp.nstr(totalR,30)}')
        print(f'  Maxwell integrated-trace thickness eps/lP={mp.nstr(eps_over_lp,25)} (necessary, NOT a solution)')
        print(f'  peak curvature |R(0)|*lP^2={mp.nstr(peak,25)}; shape-independent lower bound={mp.nstr(bound,25)}')
        for ss in (mp.mpf('.25'),mp.mpf('.5'),mp.mpf(1),mp.mpf(2)):
            integ=mp.quad(lambda u:2*ss*u/(1+u*u)**2,[0,1,mp.inf])
            assert abs(integ-ss)<mp.mpf(10)**(-dps+7)
        return tuple(+v for v in (Q,totalR,eps_over_lp,peak,bound))


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}; mpmath {mp.__version__}')
    exact_checks()
    low=numerical_checks(50);high=numerical_checks(80)
    with mp.workdps(80):
        for a,b in zip(low,high):
            assert abs(a-b)<mp.mpf('1e-40')*max(1,abs(b))
    print('PASS. Boundary-free conformal matter only; not massive/minimal scalars, supporting walls, or finite toroidal geometry.')
    print('Trace consistency is NECESSARY, never sufficient; no semiclassical solution is certified by a scalar trace.')


if __name__ == '__main__':
    main()
