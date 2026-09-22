#!/usr/bin/env python3
"""Finite NONDERIVATIVE scalar contact overlap, not a string four-point amplitude.

Uses the previously specified radial ODE at k=8, delta^2=8/5, lambda^2=2/5,
omega=sqrt(10)/2, Lambda=1. It checks the ODE by differentiation and the
Wronskian by evaluation, then integrates I4=integral_1^infty |R(x)|^4 dx.
R is normalized to unit incident radial flux in the stated exterior ODE.

Angular/time factors, an actual quartic coupling, BRST two-point measure,
worldsheet conformal blocks, moduli integrals and string backreaction are NOT
included. Finiteness of I4 cannot prove finiteness of a string amplitude.

Run: python src/numerical/heterotic_taubnut_contact_overlap.py [--output FILE]
Requires mpmath (installed as a SymPy dependency).
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import mpmath as mp


def calculate() -> dict:
    mp.mp.dps = 35
    half = mp.mpf('0.5')
    omega = mp.sqrt(10)/2
    delta = mp.sqrt(mp.mpf(8)/5)
    a_plus = omega*(1+delta)/2
    a_minus = omega*(delta-1)/2
    a = half-1j*(omega+half)
    b = half-1j*(omega-half)
    c = 1-1j*(omega+2)
    alpha, beta = -1j*a_plus, 1j*a_minus
    Aout = mp.gamma(c)*mp.gamma(1j)/(mp.gamma(b)*mp.gamma(c-a))
    Bin = mp.gamma(c)*mp.gamma(-1j)/(mp.gamma(a)*mp.gamma(c-b))
    reflect = abs(Aout/Bin)**2
    transmit = (omega+2)/abs(Bin)**2
    assert abs(reflect+transmit-1) < mp.mpf('1e-30')

    def radial(u):
        if u <= 0:
            raise ValueError('This numerical representative is restricted to x>1 (u>0).')
        return mp.exp(alpha*mp.log(u)+beta*mp.log1p(u))*mp.hyp2f1(a,b,c,-u)/Bin

    check_rows = []
    for u in map(mp.mpf, ('0.03', '0.5', '2', '10')):
        x = 1+2*u
        D = (x+delta)**2-mp.mpf(4)*(x*x-1)/10
        R = radial(u)
        Rp = mp.diff(radial,u)
        Rpp = mp.diff(radial,u,2)
        terms = (u*(1+u)*Rpp, (1+2*u)*Rp,
                 (omega**2*D/(4*u*(1+u))-1)*R)
        residual = abs(sum(terms))/max(mp.mpf(1),sum(map(abs,terms)))
        flux = 2*u*(1+u)*mp.im(mp.conj(R)*Rp)
        assert residual < mp.mpf('1e-27')
        assert abs(flux+transmit) < mp.mpf('1e-27')
        check_rows.append({'u':str(u),'relative_ode_residual':mp.nstr(residual,10),
                           'radial_flux':mp.nstr(flux,25)})

    # dx=2du=2exp(r)dr; finite contact with no derivative insertions.
    def log_integrand(r):
        u=mp.exp(r)
        return 2*u*abs(radial(u))**4

    convergence=[]
    for cutoff in (12,20,28):
        knots=sorted(set((-cutoff,-12,-4,0,4,12,cutoff)))
        value=mp.quad(log_integrand,knots)
        convergence.append({'log_u_cutoff':cutoff,'I4_cutoff':mp.nstr(value,28)})
    assert abs(mp.mpf(convergence[-1]['I4_cutoff'])-mp.mpf(convergence[-2]['I4_cutoff'])) < mp.mpf('1e-8')
    assert mp.mpf('0.4547') < mp.mpf(convergence[-1]['I4_cutoff']) < mp.mpf('0.4548')

    # Leading tail estimates, NOT certified numerical error bounds.
    L=mp.mpf(28)
    low_tail_leading=2*mp.exp(-L)/abs(Bin)**4
    upper_tail_envelope_leading=2*(1+abs(Aout/Bin))**4*mp.exp(-L)
    return {
        'scope':'neutral scalar radial contact diagnostic only; no BRST or interaction amplitude claim',
        'mpmath_dps':mp.mp.dps,
        'radial_R':mp.nstr(reflect,30),'radial_T':mp.nstr(transmit,30),
        'ode_flux_checks':check_rows,
        'contact_integral_convergence':convergence,
        'I4_display':'0.45476328 (dimensionless radial factor; 8 displayed decimals)',
        'low_tail_leading_estimate':mp.nstr(low_tail_leading,12),
        'upper_tail_leading_envelope_estimate':mp.nstr(upper_tail_envelope_leading,12),
        'not_computed':['BRST inner product','exact coset four-point function',
                        'worldsheet moduli integral','genus-one tadpoles',
                        'backreacted solution','past-directed signalling probability']
    }


def main() -> None:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output',type=Path)
    args=parser.parse_args()
    result=calculate()
    rendered=json.dumps(result,indent=2,ensure_ascii=False)+'\n'
    print(rendered,end='')
    if args.output:
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(rendered,encoding='utf-8')


if __name__=='__main__':
    main()
