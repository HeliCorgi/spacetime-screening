#!/usr/bin/env python3
"""R4_2: repair a nonuniform-lapse kinetic ordering; exact geometry checks.

A positive A^-1 and positive N do not imply positive {N,A^-1}/2.
This is an off-shell kinetic guarantee counterexample, not an on-shell ghost
proof. The replacement S N S, S=A^-1/2, is positive on the tracefree sector
whenever N>0 and A has the stated positive self-adjoint realization.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import platform
from pathlib import Path
import sympy as sp

BASE_SHA = '39fa44951a83d44d3bdae88ee6a0ab9b6ad5af34'


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def ordering():
    # p_yy=-p_zz depends only on x: transverse and tracefree. Fourier basis
    # sqrt(2)cos(x), sqrt(2)cos(5x); N=1+(1/2)cos(4x) remains positive.
    Ainv = sp.diag(sp.Rational(4,9), sp.Rational(4,729))
    N = sp.Matrix([[1,sp.Rational(1,4)],[sp.Rational(1,4),1]])
    S = sp.diag(sp.Rational(2,3), sp.Rational(2,27))
    old = (N*Ainv+Ainv*N)/2
    new = S*N*S
    require(old.det() == -sp.Rational(385,531441), 'old ordering counterexample')
    require(new.det() == sp.Rational(5,2187), 'new ordering determinant')
    comm = S*N-N*S
    require(old-new == (S*comm-comm*S)/2, 'double commutator correction')
    require(S*S == Ainv, 'flat ordering equality')
    return dict(physical_test='nonzero transverse tracefree Fourier modes 1 and 5',
        lapse='1+cos(4x)/2', lapse_range=['1/2','3/2'],
        old_matrix=str(old), repaired_matrix=str(new),
        old_determinant=str(old.det()), repaired_determinant=str(new.det()),
        old_eigenvalues=[str(x.evalf(24)) for x in sorted(old.eigenvals(),key=float)],
        repaired_eigenvalues=[str(x.evalf(24)) for x in sorted(new.eigenvals(),key=float)],
        repaired_ordering='S N S',
        positivity_scope='tracefree kinetic quadratic form, N>0; not full interacting energy or stability',
        initial_p_zero_constraints_unchanged=True,
        on_shell_ghost_proved=False)


def radial_identity():
    r = sp.symbols('r',positive=True)
    z, n = sp.symbols('z0:9'), sp.symbols('n0:7')
    def dr(f):
        return (sp.diff(f,r)+sum(sp.diff(f,z[j])*z[j+1] for j in range(8))
                +sum(sp.diff(f,n[j])*n[j+1] for j in range(6)))
    def lap(f):
        return sp.exp(-2*z[0])*(dr(dr(f))+(2/r+z[1])*dr(f))
    E = sp.exp(z[0])
    A = E**-2*(-2*z[2]-2*z[1]/r)
    B = E**-2*(-z[2]-3*z[1]/r-z[1]**2)
    R = A+2*B
    LA = lap(A)-4*E**-2*(1/r+z[1])**2*(A-B)
    LB = lap(B)+2*E**-2*(1/r+z[1])**2*(A-B)
    V = (R-lap(R)+lap(lap(R))/4-A*A-2*B*B+(A*LA+2*B*LB)/4
         +R*R/2-R*lap(R)/8)
    full = r*r*E**3*n[0]*V
    W = r*r*(E*(4*n[1]*z[1]+2*n[0]*z[1]**2+n[1]*dr(R))
        +E**3*lap(n[0])*lap(R)/4
        +E**3*n[0]*(-A*A-2*B*B+R*R/2)
        -E*(n[0]*(dr(A)**2+2*dr(B)**2+4*(1/r+z[1])**2*(A-B)**2)
             +n[1]*(A*dr(A)+2*B*dr(B)))/4
        +E*(n[0]*dr(R)**2+n[1]*R*dr(R))/8)
    boundary = (-4*r*r*n[0]*E*z[1]-r*r*E*n[0]*dr(R)
        +r*r*E*(n[0]*dr(lap(R))-n[1]*lap(R))/4
        +r*r*E*n[0]*(A*dr(A)+2*B*dr(B))/4-r*r*E*n[0]*R*dr(R)/8)
    require(sp.expand(full-W-dr(boundary)) == 0, 'weak action misses boundary/operator variation')
    require(sp.simplify(sp.diff(E**3*V,z[6])+E**-3)==0, 'sixth-order radial principal part')
    # Curvature contractions from a diagonal Ricci tensor in an orthonormal
    # radial frame. The contracted product rule is independently checked.
    ric2 = A*A+2*B*B
    grad2 = E**-2*(dr(A)**2+2*dr(B)**2+4*(1/r+z[1])**2*(A-B)**2)
    require(sp.expand((lap(ric2)/2-grad2)-(A*LA+2*B*LB))==0,
            'tensor Laplacian/product rule')
    # The ADM boundary is not dropped: zeta~M/r gives boundary~4M for N_inf=1.
    mass = sp.symbols('mass')
    asym = {z[j]:sp.diff(mass/r,r,j) for j in range(9)}
    asym.update({n[0]:1,**{n[j]:0 for j in range(1,7)}})
    require(sp.limit(boundary.subs(asym),r,sp.oo)==4*mass, 'ADM surface contribution')
    return dict(weak_strong_identity=True, tensor_rough_laplacian_identity=True,
        radial_principal_coefficient='-exp(-3*zeta) d_r^6 delta_zeta',
        general_time_symmetric_principal_symbol='-M_P^2 sqrt(gamma) ell^4 (gamma^ij k_i k_j)^3/4',
        principal_elliptic_for_positive_spatial_metric=True,
        global_invertibility_proved=False, asymptotic_boundary='4 M_ADM in G=1 units')


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path)
    a=p.parse_args()
    out=dict(base_sha=BASE_SHA,ordering=ordering(),radial_action=radial_identity(),
        implemented_checks_passed=True, full_quantum_gravity=False,
        environment=dict(python=platform.python_version(),sympy=sp.__version__),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    if a.output:
        a.output.parent.mkdir(parents=True,exist_ok=True)
        a.output.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(passed=True,old_kinetic_positive=False,repaired_tracefree_kinetic_positive=True,
                         weak_strong_identity=True,full_quantum_gravity=False)))

if __name__=='__main__':
    main()
