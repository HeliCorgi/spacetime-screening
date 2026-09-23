#!/usr/bin/env python3
"""Relative-mode encoding and two explicit MMP/Roman-ring assembly tests.

Finite-dimensional matrices here describe the FLAVOR transformation, not a
Fock cutoff. Ideal readout numbers are forward-channel controls only. The
network tests do not identify a 4D van Vleck factor with a confined 2D
Landau-level Casimir source, or forbid arbitrary multi-mouth geometries.
"""
from __future__ import annotations

from fractions import Fraction
from itertools import product
import platform
import sympy as sp
import mpmath as mp


def zero(expression: sp.Expr) -> None:
    assert sp.simplify(sp.trigsimp(sp.expand(expression))) == 0, expression


def flavor_checks() -> None:
    for n in (2, 3, 5, 8):
        singlet = sp.ones(n, 1)/sp.sqrt(n)
        rows = [list(singlet)]
        # Helmert basis: exactly orthonormal, with N-1 zero-sum directions.
        for k in range(1, n):
            rows.append([1/sp.sqrt(k*(k+1)) if i<k else
                         -k/sp.sqrt(k*(k+1)) if i==k else 0 for i in range(n)])
        U=sp.Matrix(rows)
        assert (U*U.T-sp.eye(n)).applyfunc(sp.simplify)==sp.zeros(n)
        mass=singlet*singlet.T
        assert (U*mass*U.T-sp.diag(1,*([0]*(n-1)))).applyfunc(sp.simplify)==sp.zeros(n)
        relative=U[1,:].T
        assert sp.simplify(sum(relative))==0
        assert mass*relative==sp.zeros(n,1)
        zero((relative.T*relative)[0]-1)
    tau, x, amplitude=sp.symbols('tau x amplitude', real=True)
    pulse=sp.Function('pulse')
    plus=amplitude*pulse(tau-x)
    minus=-plus
    zero(sp.diff(plus,tau,2)-sp.diff(plus,x,2))
    zero(sp.diff(plus,tau)**2+sp.diff(plus,x)**2
         -sp.diff(minus,tau)**2-sp.diff(minus,x)**2)
    # Nonnegative classical null energy: the copropagating projection is zero,
    # NOT strictly positive. It cannot supply the extra negative focusing term.
    zero((sp.diff(plus,tau)+sp.diff(plus,x))**2)
    antiparallel=amplitude*pulse(tau+x)
    zero((sp.diff(antiparallel,tau)+sp.diff(antiparallel,x))**2
         -4*sp.diff(antiparallel,tau)**2)
    print('EXACT: singlet-only mass matrix; N-1 orthogonal neutral relative modes.')
    print('EXACT: opposite-sign collective pulses have equal quadratic stress and zero total vector current.')
    print('A copropagating coherent signal adds zero to its own null projection; it does not add negative support.')


def timing_checks() -> None:
    # All admissible independent pairs have w_i=tau_i-Delta_i>d_i>=0.
    # Exhaustive finite tests complement, not replace, the general sum proof.
    tested=0
    for n in (1,2,3,4):
        for margins in product((Fraction(1,100),Fraction(1,3),Fraction(2)), repeat=n):
            own=[Fraction(i+1,5) for i in range(n)]
            transit=[own[i]+margins[i] for i in range(n)]
            connectors=[Fraction(1,20) for _ in range(n)]
            assert sum(transit)+sum(connectors)>0
            tested+=1
    # A clock relabeling changes individual edge delays, not any cycle sum.
    delays=[Fraction(7,3),Fraction(4,5),Fraction(2,7)]
    clocks=[Fraction(8),Fraction(-11),Fraction(5,2)]
    relabeled=[delays[i]+clocks[(i+1)%3]-clocks[i] for i in range(3)]
    assert min(relabeled)<0  # A negative display-time difference is not a CTC.
    assert sum(relabeled)==sum(delays)>0
    # Genuine Roman-ring kinematic control: each isolated wormhole is non-CTC,
    # but a combined ring can be CTC if we DROP the derived no-shortcut gate.
    # Mouth positions: A1=0,B1=100,A2=101,B2=1; two external links of length 1.
    own_roundtrips=[Fraction(-2)+100, Fraction(-2)+100]
    assert min(own_roundtrips)>0
    assert Fraction(-2)+1-2+1 == -2
    print(f'PASS {tested} positive-delay assembled-ring controls and clock-gauge invariance.')
    print('NEGATIVE CONTROL: isolated non-CTC arms alone do NOT rule out a Roman ring.')


def shared_loop_checks() -> None:
    # All channels in this intentionally restricted sewing travel the SAME
    # transparent, antiperiodic loop through all n distinct AdS2 throats.
    # For each throat: gate_i=4*tau_i^2/(C+Delta_loop)^2-1 must be positive.
    # Since min tau_i <= sum(tau_i)/n <= C/n, n>=2 is impossible for Delta>=0.
    tested=0
    for n in (2,3,4):
        for lengths in product((Fraction(1),Fraction(2),Fraction(5)),repeat=n):
            for extra,shift in ((Fraction(0),Fraction(0)),(Fraction(1),Fraction(1,2))):
                C=sum(lengths)+extra
                gates=[4*t*t/(C+shift)**2-1 for t in lengths]
                shortest=min(range(n),key=lambda i:lengths[i])
                assert gates[shortest] <= Fraction(4,n*n)-1 <= 0
                tested+=1
    assert Fraction(4)*Fraction(1)**2/Fraction(5,2)**2-1 == -Fraction(9,25)
    print(f'PASS {tested} shared-loop sewing controls; one throat must fail its gate for n>=2.')
    print('This is NOT a theorem against branched/multi-cycle, actively supported or full multi-mouth solutions.')


def van_vleck_checks() -> None:
    # Visser 1997 thin-throat geometric-optics factor; distinct from the
    # channel support calculation and from a physical transmission probability.
    z=sp.symbols('z',positive=True)
    for n in (2,3,4,8):
        U=sp.chebyshevu(n-1,z)
        assert sp.Poly(U,z).LC()==2**(n-1)
        exact=sp.Rational(n*n)/U.subs(z,11)**2  # d/R=10
        assert exact>0
    eps=sp.symbols('eps',positive=True)
    # Strip the positive prefactor Delta_vV/(N^4*d^4).
    interval=2*eps-eps**2
    shape=(1+4*(1-eps)**2/interval)/interval**2
    zero(sp.limit(eps**3*shape,eps,0,dir='+')-sp.Rational(1,2))
    print('EXACT: finite-N van Vleck factor remains positive; the displayed near-null stress proxy scales eps^-3.')
    print('Small 4D focusing coefficients are not multipliers for the 2D supporting Casimir energy.')


def numerical_checks(dps: int) -> list[mp.mpf]:
    with mp.workdps(dps):
        out=[]
        target_error=mp.mpf('0.01')
        for eta in (mp.mpf(1),mp.mpf('0.9'),mp.mpf('0.5')):
            n=-mp.log(4*target_error*(1-target_error))/(4*eta)
            overlap=mp.exp(-2*eta*n)
            distance=mp.sqrt(1-overlap**2)
            err=(1-distance)/2
            assert abs(err-target_error)<mp.power(10,-dps+8)
            # Independent 2D support representation for the two coherent states.
            a=mp.matrix([1,0]); b=mp.matrix([overlap,mp.sqrt(1-overlap**2)])
            diff=a*a.T-b*b.T
            ev=mp.eigsy(diff,eigvals_only=True)
            assert abs((abs(ev[0])+abs(ev[1]))/2-distance)<mp.power(10,-dps+8)
            out.append(+n)
            print(f'dps={dps}; ideal FORWARD-channel eta={eta}; n for Helstrom error .01={mp.nstr(n,34)}')
        for n in (2,4,8):
            ratio=mp.mpf(10)
            # Independently evaluate U_{n-1}(cosh a)=sinh(n a)/sinh(a).
            a=mp.acosh(1+ratio)
            u=mp.sinh(n*a)/mp.sinh(a)
            factor=(n/u)**2
            # Independent three-term recursion.
            u0,u1=mp.mpf(1),2*(1+ratio)
            for degree in range(2,n):
                u0,u1=u1,2*(1+ratio)*u1-u0
            assert abs(factor-(n/u1)**2)<mp.power(10,-dps+8)
            out.append(+factor)
            print(f'dps={dps}; N={n},d/R=10; thin-throat Delta_vV={mp.nstr(factor,34)}')
        return out


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}; mpmath {mp.__version__}')
    flavor_checks()
    timing_checks()
    shared_loop_checks()
    van_vleck_checks()
    low, high=numerical_checks(50),numerical_checks(80)
    with mp.workdps(90):
        assert max(abs(x-y) for x,y in zip(low,high))<mp.mpf('1e-40')
    print('PASS relative-mode and restricted ring tests.')
    print('No backward receiver probability, physical eta, full network metric or natural likelihood was assigned.')


if __name__ == '__main__':
    main()
