#!/usr/bin/env python3
"""Binary field measurement -> recorded feedback: exact back-action checks.

Local Weyl-field calculation, not an assumed Deutsch process. The no-fixed-state
result additionally requires a return map preserving the sender observable A.
The oscillator integrals and attenuator are controls, NOT Taub-NUT predictions.
"""
from __future__ import annotations
import platform
import sympy as s
import mpmath as mp


def exact_checks() -> None:
    a, b, c, v, w, delta, z = s.symbols('a b c v w delta z', real=True)
    va, cab = s.symbols('V_A C_AB', real=True)
    H = s.Matrix([[va, cab, 0], [cab, v, c], [0, c, w]])
    Om = s.Matrix([[0, delta, a], [-delta, 0, b], [-a, -b, 0]])
    # H_AC is immaterial: the A coefficients cancel in every word below.
    def ex(word):
        vs = [s.Matrix(x) for x in word]
        q = sum(vs, s.zeros(3, 1))
        phase = sum((vs[i].T*Om*vs[j])[0]
                    for i in range(len(vs)) for j in range(i+1, len(vs)))
        return s.exp(s.expand(-s.I*phase/2-(q.T*H*q)[0]/2))
    nu = s.exp(-2*v)
    records = {}
    for y in (1, -1):
        # M_y = [W(-B) - i y W(B)]/2, receiver initially |+x>, Y readout.
        terms = ((s.Rational(1, 2), -1), (-s.I*y/2, 1))
        for r in (1, -1):
            val = sum(s.conjugate(ci)*cj*ex([(0, -bi, 0), (-r, 0, 0),
                       (0, 0, 1), (r, 0, 0), (0, bj, 0)])
                      for ci, bi in terms for cj, bj in terms)
            target = s.exp(s.I*r*a-w/2)*(s.cos(b)+s.I*y*nu*s.sinh(2*c))/2
            assert s.simplify(s.expand(val-target.rewrite(s.exp))) == 0
            assert s.simplify(target.subs({a: 0, b: 0, c: 0, w: 0})) == s.Rational(1, 2)
            records[y, r] = target
    for k in (1, -1):
        chi = s.exp(-w/2)*(s.cos(a)*s.cos(b)-k*nu*s.sin(a)*s.sinh(2*c))
        assert s.simplify(s.expand_complex(sum(records[y, k*y] for y in (1, -1))-chi)) == 0
        scaled = chi.subs({a: z*a, b: z*b, c: z*c, w: z**2*w}, simultaneous=True)
        m2 = s.simplify(-s.diff(scaled, z, 2).subs(z, 0))
        assert s.simplify(m2-(w+a*a+b*b+4*k*nu*a*c)) == 0
        m4 = s.simplify(s.diff(scaled, z, 4).subs(z, 0))
        cumulant = s.simplify(m4-3*m2**2)
        # A positive canonical Gaussian example: A=P, B=Q, h=Q, variance=1/2.
        value = cumulant.subs({a: -1, b: 0, c: s.Rational(1, 2), v: s.Rational(1, 2), w: s.Rational(1, 2)})
        assert value != 0
        # Square completion and Cauchy bound; v>=0, c^2<=v*w required physically.
        assert s.expand((a+2*k*nu*c)**2+w+b*b-4*nu**2*c*c-m2) == 0
    for r in (1, -1):
        assert s.simplify(sum(records[y, r] for y in (1, -1))-
                          s.exp(s.I*r*a-w/2)*s.cos(b)) == 0
    # Exact state-independent operator identity, NOT iterated Gaussian closure:
    # f(y) is arbitrary; feedback exp(i f(y) A) commutes with every W(z A).
    # Summing the receiver outcomes leaves (Ad_W(B)+Ad_W(-B))/2.
    rp, rm = s.symbols('r_plus r_minus', real=True)
    coeffs = {}
    om2 = s.Matrix([[0, delta], [-delta, 0]])
    for y, r in ((1, rp), (-1, rm)):
        terms = ((s.Rational(1, 2), -1), (-s.I*y/2, 1))
        for ci, bi in terms:
            for cj, bj in terms:
                vs = [s.Matrix(q) for q in ((0, -bi), (-r, 0), (z, 0), (r, 0), (0, bj))]
                phase = s.expand(sum((vs[i].T*om2*vs[j])[0] for i in range(5) for j in range(i+1, 5)))
                key = tuple(sum(vs, s.zeros(2, 1)))
                coeffs[key] = coeffs.get(key, 0)+s.conjugate(ci)*cj*s.exp(-s.I*phase/2)
    assert s.simplify(coeffs[z, 0]-s.cos(z*delta)) == 0
    assert all(s.simplify(value) == 0 for key, value in coeffs.items() if key != (z, 0))
    # z=0 is also the state-independent completeness sum N_y^dagger N_y=1.
    assert s.cos(z*delta).subs(z, 0) == 1
    vin = s.symbols('V_in', real=True)
    out = s.cos(z*delta)*s.exp(-vin*z*z/2)
    assert s.simplify(-s.diff(out, z, 2).subs(z, 0)-vin-delta**2) == 0
    for n in (1, 2, 5, 17):
        assert s.simplify(-s.diff(s.cos(z*delta)**n*s.exp(-vin*z*z/2), z, 2).subs(z, 0)
                          -vin-n*delta**2) == 0
    # A regular invariant chi cannot equal cos(z*delta)*chi for nonzero delta:
    # z_n=1/(n*delta) ->0 has cos(z_n*delta)!=1, forcing chi(z_n)=0.
    # Continuity and chi(0)=1 contradict this. This last step is proved in note.
    eta, ve = s.symbols('eta V_env', real=True)
    vstar = ve+eta*delta**2/(1-eta)
    assert s.factor(eta*(vstar+delta**2)+(1-eta)*ve-vstar) == 0
    J = s.Matrix([[0, 1], [-1, 0]])
    # Single-mode attenuator CP criterion Y+i(Omega-X Omega X^T)/2 >=0.
    cp = (1-eta)*(ve*s.eye(2)+s.I*J/2)
    assert s.factor(cp.det()-(1-eta)**2*(ve**2-s.Rational(1, 4))) == 0
    assert min(cp.subs({eta: s.Rational(1, 2), ve: 0}).eigenvals()) < 0
    print('EXACT: recorded Kraus maps are normalized for constants/copy/NOT; flag marginal unchanged.')
    print('EXACT: chi_k(h)=exp(-V_h/2)[cos(a)cos(b)-k exp(-2V_B)sin(a)sinh(2C_Bh)].')
    print('EXACT: V_k=V_h+a^2+b^2+4k exp(-2V_B)a C_Bh; generally non-Gaussian.')
    print('STATE-INDEPENDENT: E_f^*(W(z A))=cos(z Delta_AB) W(z A), for every f.')
    print('CONDITIONAL NO-GO: A-preserving return and Delta_AB!=0 admit no regular invariant state.')
    print('LOSS CONTROL: Vstar=V_env+eta Delta_AB^2/(1-eta); missing vacuum noise is not CP.')


def quadrature_checks(dps: int) -> list:
    results = []
    with mp.workdps(dps):
        # Infinite-dimensional Schrodinger representation [Q,P]=i.
        # A=alpha P, B=beta Q, h=u Q+v P; no finite oscillator cutoff.
        alpha, beta = mp.mpf('0.7'), mp.mpf('0.6')
        def psi(x):
            return mp.exp(-x*x/2)/mp.root(mp.pi, 4)
        # Gaussian tail bounds permit finite integration without lowering precision.
        L = mp.sqrt((dps+30)*mp.log(10))
        R = L+abs(alpha)+1
        bounds = [-R, -8, -4, 0, 4, 8, R]
        t0 = mp.erfc(L)
        t2 = L*mp.exp(-L*L)/mp.sqrt(mp.pi)+t0/2
        tail_bound = 8*(t2+(alpha**2+beta**2+1)*t0)
        assert tail_bound < mp.power(10, -dps-20)
        def integrate(fn):
            return mp.quad(fn, bounds, method='gauss-legendre')
        for kind in ('fixed0', 'fixed1', 'copy', 'NOT'):
            def r_of(y):
                return {'fixed0': 1, 'fixed1': -1, 'copy': y, 'NOT': -y}[kind]
            def outpsi(x, y):
                q = x+r_of(y)*alpha
                return (mp.exp(-1j*beta*q)-1j*y*mp.exp(1j*beta*q))*psi(q)/2
            def derivative(x, y):
                q = x+r_of(y)*alpha
                em, ep = mp.exp(-1j*beta*q), mp.exp(1j*beta*q)
                return ((-1j*beta-q)*em+(y*beta+1j*y*q)*ep)*psi(q)/2
            for u, vv in ((mp.mpf('0.4'), mp.mpf('0.3')), (mp.mpf('1'), mp.mpf('0'))):
                chi = mp.mpc(0)
                for y in (1, -1):
                    # W(uQ+vP) psi(x)=exp[iu(x+v/2)] psi(x+v).
                    chi += integrate(lambda x: mp.conj(outpsi(x, y))*mp.exp(1j*u*(x+vv/2))*outpsi(x+vv, y))
                a, b, c = -alpha*u, beta*vv, beta*u/2
                w, nu = (u*u+vv*vv)/2, mp.exp(-beta*beta)
                if kind in ('copy', 'NOT'):
                    k = 1 if kind == 'copy' else -1
                    target = mp.exp(-w/2)*(mp.cos(a)*mp.cos(b)-k*nu*mp.sin(a)*mp.sinh(2*c))
                else:
                    target = mp.exp(-w/2+1j*r_of(1)*a)*mp.cos(b)
                assert abs(chi-target) < mp.power(10, -dps+9)
                results.append(+chi)
            norm, moment_q2, moment_p2 = mp.mpf(0), mp.mpf(0), mp.mpf(0)
            for y in (1, -1):
                branch_norm = integrate(lambda x: abs(outpsi(x, y))**2)
                assert abs(branch_norm-mp.mpf('0.5')) < mp.power(10, -dps+9)
                norm += branch_norm
                moment_q2 += integrate(lambda x: x*x*abs(outpsi(x, y))**2)
                moment_p2 += integrate(lambda x: abs(derivative(x, y))**2)
            target_q = mp.mpf('0.5')+alpha**2
            if kind in ('copy', 'NOT'):
                target_q -= (1 if kind == 'copy' else -1)*2*mp.exp(-beta**2)*alpha*beta
            assert abs(norm-1) < mp.power(10, -dps+9)
            assert abs(moment_q2-target_q) < mp.power(10, -dps+9)
            assert abs(moment_p2-(mp.mpf('0.5')+beta**2)) < mp.power(10, -dps+9)
            results += [+moment_q2, +moment_p2]
            print(f'dps={dps}; {kind}: <Q^2>={mp.nstr(moment_q2, 30)}, <P^2>={mp.nstr(moment_p2, 20)}')
        # Controlled attenuator marginal: exact finite-N recurrence plus rigorous
        # product-tail bound |prod_{j>N}cos(x_j)-1| <= sum x_j^2/2.
        eta, delta, ve, z = mp.mpf('0.5'), mp.mpf('0.2'), mp.mpf('0.5'), mp.mpf('0.7')
        n = 4*dps
        product = mp.exp(-ve*z*z/2)*mp.fprod(mp.cos(delta*eta**(mp.mpf(j)/2)*z) for j in range(1, n+1))
        shifted = mp.exp(-ve*eta*z*z/2)*mp.fprod(mp.cos(delta*eta**(mp.mpf(j+1)/2)*z) for j in range(1, n+1))
        rhs = mp.exp(-(1-eta)*ve*z*z/2)*mp.cos(mp.sqrt(eta)*delta*z)*shifted
        tail = delta**2*z*z*eta**(n+1)/(2*(1-eta))
        assert abs(product-rhs) <= 2*tail+mp.power(10, -dps+8)
        results.append(+product)
        print(f'dps={dps}; attenuated marginal variance={ve+eta*delta**2/(1-eta)}; tail_bound={mp.nstr(tail, 8)}')
    return results


def main() -> None:
    print(f'Python {platform.python_version()}; SymPy {s.__version__}; mpmath {mp.__version__}')
    exact_checks()
    lo, hi = quadrature_checks(50), quadrature_checks(80)
    with mp.workdps(90):
        assert all(abs(a-b) < mp.mpf('1e-40') for a, b in zip(lo, hi))
    print('PASS algebra and independent wavefunction integrals. Not a global NUT state or full backreaction solution.')


if __name__ == '__main__':
    main()
