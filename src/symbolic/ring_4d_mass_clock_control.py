"""Reproduce a conditional 4D clock-control route, not an engineered time machine.

Frolov--Krtous--Zelnikov, arXiv:2305.03887v1, equations (2.8), (4.12),
(5.35), (6.1)--(6.9). Weak fields, distant mouths, pre-existing negative
conical-defect ring. This is NOT the spherical scattering geometry.
"""
from __future__ import annotations

import platform
import sympy as s
import mpmath as mp


def exact_checks() -> None:
    chi, th, ph = s.symbols("chi theta phi", real=True)
    a, mass = s.symbols("a m", positive=True)
    # Three independent spatial coordinates; time adds the fourth dimension.
    X = a*s.cosh(chi)*s.sin(th)*s.cos(ph)
    Y = a*s.cosh(chi)*s.sin(th)*s.sin(ph)
    Z = a*s.sinh(chi)*s.cos(th)
    jac = s.Matrix([X,Y,Z]).jacobian([chi,th,ph])
    g3 = s.simplify(s.trigsimp(jac.T*jac))
    scale = s.sinh(chi)**2+s.cos(th)**2
    target = a*a*s.diag(scale,scale,s.cosh(chi)**2*s.sin(th)**2)
    assert s.simplify(s.trigsimp(g3-target)) == s.zeros(3)
    potential = mass*(s.atan(s.sinh(chi))-s.pi/2)
    assert s.simplify(s.diff(potential,chi)-mass/s.cosh(chi)) == 0
    assert s.simplify(s.diff(s.cosh(chi)*s.diff(potential,chi),chi)) == 0
    # Source-free oblate Laplacian outside the shell; inside potential is constant.
    t0, t2, A, B, hol = s.symbols("t0 t2 A B I", real=True)
    t1 = t0+A
    t3 = t2+B
    relation = s.solve(t1-s.exp(hol)*t2,t0)[0]
    assert s.simplify((t3-t0).subs(t0,relation)-(A+B-(s.exp(hol)-1)*t2)) == 0
    print("EXACT: 3D oblate spatial metric plus time, shell exterior harmonic potential, and clock matching.")
    print("PUBLISHED weak-field relation: I_C=(GM/ac^2)[arctan(a/R)-a/L+omitted distant-mouth corrections].")
    print("Conditional round trip: t3-t0=Bopt-(exp(I_C)-1)*t2; not independent clock relabeling.")


def numerical(dps: int) -> tuple:
    with mp.workdps(dps):
        c=mp.mpf(299792458)
        G=mp.mpf("6.67430e-11")
        a,R,L=mp.mpf(1),mp.mpf(10),mp.mpf(1000)
        # Bopt is approximated as L/c, as in the paper's leading timescale.
        Bopt=L/c
        line_energy=-c**4/(4*G)  # J/m, also tension in N for a Nambu--Goto sign.
        ring_energy=2*mp.pi*a*line_energy
        out=[line_energy,ring_energy]
        for M in (mp.mpf("1e3"),mp.mpf("1e12"),mp.mpf("1e20")):
            m=G*M/(a*c*c)
            I=m*(mp.atan(a/R)-a/L)
            assert 0<I<mp.mpf("1e-6")
            # Rigorous arctan remainder only; NOT a bound on omitted metric orders.
            lower=m*(a/R-(a/R)**3/3-a/L)
            upper=m*(a/R-a/L)
            assert lower<I<upper
            onset=Bopt/mp.expm1(I)
            leading=R*L*c/(G*M)
            assert abs(onset/leading-1)<mp.mpf(".02")
            assert Bopt-mp.expm1(I)*(onset/2)>0
            assert Bopt-mp.expm1(I)*(2*onset)<0
            out.extend((I,onset))
            print(f"dps={dps}; M={mp.nstr(M,8)} kg; I_C={mp.nstr(I,12)}; formal onset={mp.nstr(onset,12)} s")
        print(f"  required negative ring energy per length={mp.nstr(line_energy,12)} J/m; radius1m ideal ring={mp.nstr(ring_energy,12)} J")
        return tuple(out)


def main() -> None:
    print(f"Python {platform.python_version()}; SymPy {s.__version__}; mpmath {mp.__version__}")
    exact_checks()
    a,b=numerical(50),numerical(80)
    with mp.workdps(85):
        assert all(abs(x-y)<mp.mpf("1e-43")*max(abs(y),mp.mpf("1e-80")) for x,y in zip(a,b))
    print("PASS published conditional clock-control equations and nominal SI scaling checks.")
    print("The ring's negative source, formation, quantum backreaction and past-record probabilities are NOT constructed.")
    print("Do NOT combine this ring's clock result with a spherical throat's transmission as one solved device.")


if __name__ == "__main__":
    main()
