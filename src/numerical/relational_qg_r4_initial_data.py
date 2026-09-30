#!/usr/bin/env python3
"""R4_2: nonlinear, time-symmetric spherical initial data and lapse.

This is NOT an evolution or generic-stability solver.  Coordinates and lengths
are in ell units, G=c=ell=1. Matter is a coordinate Gaussian rest density at
zero momentum (not a hydrostatic star). The full R3_2 spatial potential is used,
without expansion in source strength. R4 changes only the kinetic ordering to
S N S, S=(1+L/2)^-1; hence these p=0 constraints also apply to R3_2.

A rational Chebyshev Galerkin method on the entire radial half-line solves the
Hamiltonian constraint. Its transpose Jacobian fixes the lapse. Automatic
refinement, independent strong-form residuals, the ADM surface/volume identity,
and lapse bounds are gates, not proofs of continuum existence or stability.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import platform
from pathlib import Path
import numpy as np
import scipy
from numpy.polynomial.chebyshev import Chebyshev
from scipy.optimize import root
from scipy.special import roots_legendre

BASE_SHA = "39fa44951a83d44d3bdae88ee6a0ab9b6ad5af34"


def require(ok, message):
    if not ok:
        raise AssertionError(message)


def basis(r, modes, scale, order=6):
    """Exact chain-rule jets of b_j=u T_j(2u-1), u=scale/sqrt(scale^2+r^2)."""
    r = np.atleast_1d(np.asarray(r, dtype=float))
    den = scale**2 + r*r
    u = scale/np.sqrt(den)
    alpha, beta = 2*r/den, 1/den
    ut = [u]
    binom = [1.]
    for j in range(1, order+1):
        binom.append(binom[-1]*(-.5-j+1)/j)
    for k in range(1, order+1):
        ut.append(u*sum(binom[j]*math.comb(j, k-j)*alpha**(2*j-k)*beta**(k-j)
                        for j in range((k+1)//2, k+1)))
    powers = np.zeros((order+1, order+1, len(u)))
    powers[0, 0] = 1
    for p in range(1, order+1):
        for k in range(p, order+1):
            powers[p, k] = sum(powers[p-1, j]*ut[k-j] for j in range(k))
    out = np.zeros((order+1, modes, len(r)))
    for j in range(modes):
        T = Chebyshev.basis(j)
        t = [T.deriv(k)(2*u-1) for k in range(order+1)]
        f = [u*t[0]] + [(u*2**k*t[k]+k*2**(k-1)*t[k-1])/math.factorial(k)
                        for k in range(1, order+1)]
        for k in range(order+1):
            out[k, j] = math.factorial(k)*sum(f[p]*powers[p, k] for p in range(k+1))
    return out


def weak_coefficients(r, z):
    """W[N]=int r^2 (C0*N+C1*N'+C2*N'') dr; ADM boundary removed."""
    z0, z1, z2, z3, z4 = z[:5]
    e = np.exp(z0)
    c = 2/r+z1
    rb = -4*z2-8*z1/r-2*z1*z1
    rb1 = -4*z3-8*(z2/r-z1/r**2)-4*z1*z2
    rb2 = -4*z4-8*(z3/r-2*z2/r**2+2*z1/r**3)-4*(z2*z2+z1*z3)
    R = rb/e**2
    R1 = (rb1-2*z1*rb)/e**2
    R2 = (rb2-4*z1*rb1+(4*z1*z1-2*z2)*rb)/e**2
    ar, at = -2*z2-2*z1/r, -z2-3*z1/r-z1*z1
    A, B = ar/e**2, at/e**2
    A1 = (-2*z3-2*(z2/r-z1/r**2)-2*z1*ar)/e**2
    B1 = (-z3-3*(z2/r-z1/r**2)-2*z1*z2-2*z1*at)/e**2
    lapR = R2+c*R1
    C0 = (2*e*z1*z1 + e**3*(-A*A-2*B*B+.5*R*R)
          -.25*e*(A1*A1+2*B1*B1+4*(1/r+z1)**2*(A-B)**2)
          +.125*e*R1*R1)
    C1 = (e*(4*z1+R1)+.25/e*c*lapR-.25*e*(A*A1+2*B*B1)
          +.125*e*R*R1)
    C2 = .25/e*lapR
    return C0, C1, C2


def strong_operators():
    """Separate strong constraint and Euler lapse equations; no weak residual reuse."""
    import sympy as sp
    r = sp.symbols('r', positive=True)
    z, n = sp.symbols('z0:9'), sp.symbols('n0:7')
    def dr(f):
        return (sp.diff(f, r)+sum(sp.diff(f, z[j])*z[j+1] for j in range(8))
                +sum(sp.diff(f, n[j])*n[j+1] for j in range(6)))
    def lap(f):
        return sp.exp(-2*z[0])*(dr(dr(f))+(2/r+z[1])*dr(f))
    R = sp.exp(-2*z[0])*(-4*z[2]-8*z[1]/r-2*z[1]**2)
    A = sp.exp(-2*z[0])*(-2*z[2]-2*z[1]/r)
    B = sp.exp(-2*z[0])*(-z[2]-3*z[1]/r-z[1]**2)
    LA = lap(A)-4*sp.exp(-2*z[0])*(1/r+z[1])**2*(A-B)
    LB = lap(B)+2*sp.exp(-2*z[0])*(1/r+z[1])**2*(A-B)
    V = (R-lap(R)+lap(lap(R))/4-A*A-2*B*B+(A*LA+2*B*LB)/4
         +R*R/2-R*lap(R)/8)
    constraint = sp.exp(3*z[0])*V
    # Independently integrate by parts the invariant potential to get the lapse
    # adjoint equation. It is the metric variation, not the constraint equation.
    e, c = sp.exp(z[0]), 2/r+z[1]
    W = r*r*(e*(4*n[1]*z[1]+2*n[0]*z[1]**2+n[1]*dr(R))
        +(n[2]+c*n[1])*(dr(dr(R))+c*dr(R))/(4*e)
        +e**3*n[0]*(-A*A-2*B*B+R*R/2)
        -e*(n[0]*(dr(A)**2+2*dr(B)**2+4*(1/r+z[1])**2*(A-B)**2)
             +n[1]*(A*dr(A)+2*B*dr(B)))/4
        +e*(n[0]*dr(R)**2+n[1]*R*dr(R))/8)
    W = sp.expand(W)
    EL = 0
    for j in range(5):
        term = sp.diff(W, z[j])
        for _ in range(j):
            term = sp.expand(dr(term))
        EL += (-1)**j*term
    EL = sp.expand(EL)
    require(not (set(z[7:]) & EL.free_symbols), 'unexpected high derivative')
    require(sp.simplify(sp.diff(constraint, z[6])+sp.exp(-3*z[0])) == 0,
            'curved radial principal coefficient')
    return (sp.lambdify((r, *z[:7]), constraint, 'numpy', cse=True),
            sp.lambdify((r, *z[:7], *n), EL/r**2, 'numpy', cse=True))


class InitialData:
    def __init__(self, modes=32, quadrature=240, sigma=1., scale=4.):
        if modes < 8 or quadrature < 4*modes or sigma <= 0 or scale <= 0:
            raise ValueError('modes>=8, quadrature>=4*modes, sigma>0, scale>0 required')
        self.modes, self.quadrature, self.sigma, self.scale = modes, quadrature, sigma, scale
        x, w = roots_legendre(quadrature)
        theta = (x+1)*np.pi/4
        self.r = scale*np.tan(theta)
        self.w = w*np.pi/4*scale/np.cos(theta)**2*self.r**2
        self.D = basis(self.r, modes, scale, 4)
        self.tail = scale*(-1.)**np.arange(modes)
        self.rhs = (16*np.pi/(2*np.pi*sigma*sigma)**1.5
                    *(self.D[0] @ (self.w*np.exp(-self.r**2/(2*sigma*sigma)))))
        J0 = self.jacobian(np.zeros(modes))[1:]
        require(np.linalg.norm(J0-J0.T)/np.linalg.norm(J0) < 1e-10, 'flat symmetry')
        values, vectors = np.linalg.eigh((J0+J0.T)/2)
        require(values[0] > 0, 'flat Galerkin operator not positive')
        self.P = (vectors/np.sqrt(values)) @ vectors.T

    def functional(self, a):
        C = weak_coefficients(self.r, np.einsum('kjn,j->kn', self.D, a))
        return np.r_[self.w @ C[0],
                     sum(self.D[j] @ (self.w*C[j]) for j in range(3))]

    def jacobian(self, a):
        columns = []
        for j in range(self.modes):
            perturbed = np.asarray(a, dtype=complex).copy()
            perturbed[j] += 1e-25j
            columns.append(self.functional(perturbed).imag/1e-25)
        return np.array(columns).T

    def solve(self, epsilon, guess=None):
        if not np.isfinite(epsilon) or epsilon <= 0:
            raise ValueError('epsilon must be finite and positive')
        if guess is None:
            guess = np.zeros(self.modes)
        P, src = self.P, epsilon*self.rhs
        sol = root(lambda u: P@(self.functional(P@u)[1:]-src),
                   np.linalg.solve(P, guess),
                   jac=lambda u: P@self.jacobian(P@u)[1:]@P, tol=1e-11)
        require(sol.success, 'nonlinear solver failed: '+str(sol.message))
        a = P@sol.x
        J = self.jacobian(a)
        n = np.linalg.solve(J[1:].T, -J[0])
        res = float(np.max(abs(P@(self.functional(a)[1:]-src))))
        lapse_res = float(np.max(abs(P@(J[1:].T@n+J[0]))))
        mass = epsilon-self.functional(a)[0]/4
        sv = np.linalg.svd(P@J[1:]@P, compute_uv=False)
        require(res < 1e-9 and lapse_res < 1e-9, 'projected constraint/lapse residual')
        require(sv[-1] > 1e-4, 'projected radial branch nearly singular')
        # |u T_j(2u-1)|<=1 on the whole half-line. This is a conservative
        # bound on this finite expansion, not a continuum-error certificate.
        lapse_lower = float(1-np.sum(abs(n)))
        require(lapse_lower > 0, 'positive-lapse bound not established; do not clip')
        mean_lapse = 1+n@self.rhs/4
        a_prime = np.linalg.solve(J[1:], self.rhs)
        mass_prime = 1-J[0]@a_prime/4
        require(abs(mean_lapse-mass_prime) < 1e-10, 'mass-clock sensitivity identity')
        return dict(epsilon=float(epsilon), modes=self.modes, quadrature=self.quadrature,
            sigma_over_ell=self.sigma, map_scale=self.scale,
            zeta_coefficients=a.tolist(), lapse_coefficients=n.tolist(),
            zeta_center=float(np.sum(a)), lapse_center=float(1+np.sum(n)),
            lapse_lower_bound_finite_expansion=lapse_lower,
            adm_mass_over_rest=float(mass/epsilon),
            adm_surface_over_rest=float(self.tail@a/epsilon),
            mass_surface_volume_gap=float(abs(self.tail@a-mass)/epsilon),
            mean_lapse=float(mean_lapse), d_adm_d_rest=float(mass_prime),
            projected_constraint_residual=res, projected_lapse_residual=lapse_res,
            smallest_preconditioned_radial_singular_value=float(sv[-1]))

    def diagnostics(self, record, operators):
        a, n = map(np.asarray, (record['zeta_coefficients'], record['lapse_coefficients']))
        r = np.geomspace(.03*self.sigma, 20*self.sigma, 160)
        D = basis(r, self.modes, self.scale)
        z, N = np.einsum('kjn,j->kn', D, a), np.einsum('kjn,j->kn', D, n)
        N[0] += 1
        rho_peak = 16*np.pi*record['epsilon']/(2*np.pi*self.sigma**2)**1.5
        cr = operators[0](r, *z)-rho_peak*np.exp(-r*r/(2*self.sigma**2))
        lr = operators[1](r, *z, *N)
        norm = max(1., rho_peak)
        ce, le = float(np.max(abs(cr))/norm), float(np.max(abs(lr))/norm)
        require(ce < 1e-6 and le < 1e-6, 'independent strong-form sample residual')
        require(record['mass_surface_volume_gap'] < 1e-6, 'ADM boundary mismatch')
        at0 = basis([0.], self.modes, self.scale, 2)
        z2 = at0[2, :, 0]@a
        record.update(strong_constraint_sample_error=ce, strong_lapse_sample_error=le,
            strong_test_interval_over_ell=[float(r[0]), float(r[-1])], strong_samples=len(r),
            spatial_R_center_ell2=float(-12*np.exp(-2*sum(a))*z2),
            spherical_expansion_factor_sample_min=float(np.min(1+r*z[1])),
            initial_coordinate_acceleration=[dict(r_over_ell=float(r[j]),
                ell_ddot_r_over_c2=float(-N[0,j]*np.exp(-2*z[0,j])*N[1,j]))
                for j in (40, 80, 120)],
            full_evolution_solved=False, generic_stability_proved=False)
        return record


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--epsilon', type=float, nargs='+', default=[.01,.1,.5,1.,2.,4.])
    p.add_argument('--sigma', type=float, default=1.)
    p.add_argument('--modes', type=int, default=32)
    p.add_argument('--quadrature', type=int, default=240)
    p.add_argument('--map-scale', type=float, default=4.)
    p.add_argument('--output', type=Path)
    p.add_argument('--profiles', type=Path, help='optional full finest-grid coefficient records')
    args = p.parse_args()
    epsilons = sorted(set(args.epsilon))
    if not epsilons or min(epsilons) <= 0 or max(epsilons) > 4:
        raise ValueError('this released solver is restricted to 0<epsilon<=4')
    op = strong_operators()
    runs = []
    for modes, nq in ((args.modes,args.quadrature),(args.modes+8,args.quadrature+80)):
        g = InitialData(modes, nq, args.sigma, args.map_scale)
        guess, rows = None, []
        for eps in epsilons:
            rec = g.solve(eps, guess)
            guess = np.asarray(rec['zeta_coefficients'])
            rows.append(g.diagnostics(rec, op))
            print(json.dumps({k:rec[k] for k in ('epsilon','modes','zeta_center',
                'lapse_center','adm_mass_over_rest','mean_lapse','strong_constraint_sample_error')}), flush=True)
        runs.append(rows)
    errors = [abs(a[key]-b[key]) for a,b in zip(*runs) for key in
              ('zeta_center','lapse_center','adm_mass_over_rest','mean_lapse')]
    require(max(errors) < 1e-7, 'refinement failed')
    # A finite-difference first-law check is independent of the transpose solve.
    middle = runs[-1][len(epsilons)//2]
    ep = middle['epsilon']; step = min(1e-3, ep/10)
    vals = []
    for j in (-2,-1,1,2):
        rr = g.solve(ep+j*step, np.asarray(middle['zeta_coefficients']))
        vals.append(rr['epsilon']*rr['adm_mass_over_rest'])
    slope = (vals[0]-8*vals[1]+8*vals[2]-vals[3])/(12*step)
    require(abs(slope-middle['mean_lapse']) < 1e-7, 'independent mass-clock derivative')
    result = dict(model='R4_2', base_sha=BASE_SHA, units='G=c=ell=1',
        source='coordinate Gaussian rest density, zero momenta, asymptotically flat',
        kinetic_ordering='S N S',
        runs=[[{k:v for k,v in rec.items() if k not in ('zeta_coefficients','lapse_coefficients')}
               for rec in rows] for rows in runs], reference_profile=middle,
        max_refinement_difference=max(errors),
        first_law_finite_difference=dict(epsilon=ep, derivative=float(slope),
            mean_lapse=middle['mean_lapse'], error=float(abs(slope-middle['mean_lapse']))),
        implemented_checks_passed=True, full_evolution_solved=False,
        generic_stability_proved=False, full_quantum_gravity=False,
        environment=dict(python=platform.python_version(),numpy=np.__version__,scipy=scipy.__version__),
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    if args.profiles:
        args.profiles.parent.mkdir(parents=True,exist_ok=True)
        args.profiles.write_text(json.dumps(runs[-1],indent=2)+'\n')
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps(dict(passed=True, max_refinement_difference=max(errors),
                         full_evolution_solved=False)))

if __name__ == '__main__':
    main()
