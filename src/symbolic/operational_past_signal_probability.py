#!/usr/bin/env python3
"""Operational signal controls, not a Taub-NUT probability calculation.

1. Exact three-qubit noisy postselected teleportation: an earlier receiver's
   unconditional bit is independent of the later encoding, even when a
   selected future Bell outcome displays perfect/partial correlation.
2. A finite-noise Gaussian readout can communicate without preserving a
   pure state; verify the total variation by an independent density integral.
3. A coherent classical source changes the mean, not connected covariance.

The elementary Bell example is NOT a reproduction of the optimized 2026
Ji--Lloyd--Wilde retrocausal-capacity theorem and does not exclude a new
physical law enforcing a final-state projection. That resource must be derived.
"""
from __future__ import annotations

import platform
import mpmath as mp
import sympy as sp


def ket(a: int, b: int) -> sp.Matrix:
    out = sp.zeros(4, 1)
    out[2*a+b] = 1
    return out


def exact_bell_controls() -> None:
    vis = sp.symbols('v', real=True)
    basis = [sp.Matrix([1, 0]), sp.Matrix([0, 1])]
    bells = [(ket(0, 0)+ket(1, 1))/sp.sqrt(2),
             (ket(0, 0)-ket(1, 1))/sp.sqrt(2),
             (ket(0, 1)+ket(1, 0))/sp.sqrt(2),
             (ket(0, 1)-ket(1, 0))/sp.sqrt(2)]
    projectors = [b*b.H for b in bells]
    assert sum(projectors, sp.zeros(4)) == sp.eye(4)
    rhoBC = vis*projectors[0]+(1-vis)*sp.eye(4)/4
    assert sp.trace(rhoBC) == 1
    # For 0<=v<=1 the eigenvalues (1+3v)/4, (1-v)/4 (x3) are nonnegative.
    z = sp.symbols('z')
    assert sp.factor(rhoBC.charpoly(z).as_expr()
                     -(z-(1+3*vis)/4)*(z-(1-vis)/4)**3) == 0
    outputs: dict[int, sp.Matrix] = {}
    conditioned: dict[int, sp.Matrix] = {}
    for bit in (0, 1):
        # Register order B,C,M. Measuring B first commutes with the later CM
        # Bell instrument. The formula keeps B's earlier classical record.
        rho = sp.kronecker_product(rhoBC, basis[bit]*basis[bit].H)
        joint = sp.zeros(2, 4)
        for y in (0, 1):
            effectB = basis[y]*basis[y].H
            for h in range(4):
                joint[y, h] = sp.simplify(sp.trace(
                    sp.kronecker_product(effectB, projectors[h])*rho))
        assert sp.simplify(sum(joint)-1) == 0
        for h in range(4):
            assert sp.simplify(sum(joint[y, h] for y in (0, 1))-sp.Rational(1,4)) == 0
        outputs[bit] = joint*sp.ones(4, 1)
        assert outputs[bit] == sp.Matrix([sp.Rational(1,2)]*2)
        conditioned[bit] = 4*joint[:, 0]
        expected = sp.Matrix([(1+vis*(-1)**(y+bit))/2 for y in (0, 1)])
        assert conditioned[bit] == expected
        for v0 in (0, sp.Rational(1,5), sp.Rational(4,5), 1):
            vals = joint.subs(vis, v0)
            assert all(a >= 0 for a in vals)
        print(f'bit={bit}; joint P(earlier y, later Bell h) = {joint.tolist()}')
    assert outputs[0] == outputs[1]
    assert (conditioned[0]-conditioned[1]) == sp.Matrix([vis, -vis])
    # Negative control: deleting all h!=0 outcomes would falsely certify a
    # backwards bit for v=1, despite the complete ensemble being unchanged.
    assert conditioned[0].subs(vis, 1) != conditioned[1].subs(vis, 1)
    print('EXACT: D_unconditional=0; D_future-postselected=v; P(h=0)=1/4 for both bits.')
    print('Message-independent herald probability alone does NOT remove the selection bias.')


def coherent_covariance_control() -> None:
    W, mu, mup, f, fp = sp.symbols('W mu mup f fp', commutative=True)
    shifted_W = W+f*mup+fp*mu+f*fp
    shifted_connected = sp.expand(shifted_W-(mu+f)*(mup+fp))
    assert sp.simplify(shifted_connected-(W-mu*mup)) == 0
    print('EXACT: c-number source displacement leaves the connected two-point covariance unchanged.')


def gaussian_controls(dps: int) -> list[mp.mpf]:
    with mp.workdps(dps):
        results = []
        # Means -a,+a; variance V; includes no response and a noisy positive control.
        for astr, vstr in [('0', '1'), ('0.3', '1'), ('1', '1'), ('1', '4')]:
            a, var = mp.mpf(astr), mp.mpf(vstr)
            scale = mp.sqrt(2*mp.pi*var)
            pdf0 = lambda y: mp.exp(-(y+a)**2/(2*var))/scale
            pdf1 = lambda y: mp.exp(-(y-a)**2/(2*var))/scale
            # At y>0 pdf1>=pdf0, symmetry supplies the other half of TV.
            integ = mp.quad(lambda y: pdf1(y)-pdf0(y), [0, 1, 4, mp.inf])
            closed = mp.erf(a/mp.sqrt(2*var))
            assert abs(integ-closed) < mp.power(10, -dps+10)
            assert 0 <= closed < 1
            success = (1+closed)/2
            if a == 0:
                assert integ == 0 and success == mp.mpf('0.5')
            else:
                assert success > mp.mpf('0.5')
            results.append(+closed)
            print(f'dps={dps}; means=+/-{a}; variance={var}; TV={mp.nstr(closed,40)}; '
                  f'P_guess={mp.nstr(success,40)}')
        # TV approximation errors eps0,eps1 do not require exact state preservation.
        eps0, eps1 = mp.mpf('0.01'), mp.mpf('0.02')
        assert results[2]-eps0-eps1 > 0
        # An unknown response is not a measured zero or a positive witness.
        taub_nut_past_response = None
        assert taub_nut_past_response is None
        return results


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {sp.__version__}; mpmath {mp.__version__}')
    exact_bell_controls()
    coherent_covariance_control()
    lo, hi = gaussian_controls(50), gaussian_controls(80)
    with mp.workdps(80):
        assert max(abs(a-b) for a, b in zip(lo, hi)) < mp.mpf('1e-40')
    print('PASS operational probability controls; Taub-NUT past receiver distribution NOT computed.')
    print('A noise model or postselected model is not a physical realization of a backward channel.')


if __name__ == '__main__':
    main()
