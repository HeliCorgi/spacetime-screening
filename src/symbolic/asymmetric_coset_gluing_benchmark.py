#!/usr/bin/env python3
"""Compact asymmetric-coset control for Quella--Schomerus (2003).

Model: (SU(2)_k x SU(2)_k)/U(1), epsilon_L(h)=(1,h),
epsilon_R(h)=(h,1), the p=q=1 example of hep-th/0212119v3, sec. 4.2.
Use sec. 2.3 eqs. (7)-(8): intersect allowed labels and identification groups,
then glue the conjugate right sector. This is a COMPACT control, not a
Lorentzian heterotic Taub--NUT Hilbert-space construction or a BRST proof.

The SU(2)/U(1) characters are labelled by (ell,m), ell=twice spin,
m modulo 2k, ell-m even, with (ell,m)~(k-ell,m+k). The common identification
group of the ASYMMETRIC product coset is trivial even though each chiral
coset has an order-two identification. We test the complete finite modular
matrices rather than comparing a truncated q expansion.
"""
from __future__ import annotations

import argparse
import json
import platform
from collections import Counter
from fractions import Fraction
from pathlib import Path
from typing import Any

import mpmath as mp


def pf_rep(k: int, ell: int, m: int) -> tuple[int,int]:
    m %= 2*k
    if not 0 <= ell <= k or (ell-m) % 2:
        raise ValueError('Not an allowed parafermion label')
    return min((ell,m),(k-ell,(m+k)%(2*k)))


def h_su(k: int, ell: int) -> Fraction:
    return Fraction(ell*(ell+2),4*(k+2))


def h_pf(k: int, label: tuple[int,int]) -> Fraction:
    ell,m = label
    return h_su(k,ell)-Fraction(m*m,4*k)


def finite_data(k: int) -> dict[str,Any]:
    if k < 2:
        raise ValueError('This benchmark uses k>=2.')
    universe = [(l1,l2,m) for l1 in range(k+1) for l2 in range(k+1) for m in range(2*k)]
    allowed_L = {a for a in universe if (a[1]-a[2])%2 == 0}
    allowed_R = {a for a in universe if (a[0]-a[2])%2 == 0}
    allowed = sorted(allowed_L & allowed_R)
    # Store simple-current actions as their shifts in the PARENT product and H.
    # Their intersection, NOT the group they jointly generate, implements (8).
    id_L = {(0,0,0),(0,k,k)}
    id_R = {(0,0,0),(k,0,k)}
    common_id = id_L & id_R
    assert common_id == {(0,0,0)}
    pf_labels = sorted({pf_rep(k,l,m) for l in range(k+1) for m in range(2*k) if (l-m)%2 == 0})
    assert len(pf_labels) == k*(k+1)//2
    chiral = [(l,pf) for l in range(k+1) for pf in pf_labels]
    index = {label:i for i,label in enumerate(chiral)}
    # Write both chiral algebras in the order SU(2) x parafermion.
    # The SU(2) factors swap sides; right U(1) charge is conjugated.
    def pair(label: tuple[int,int,int]) -> tuple[int,int]:
        l1,l2,m = label
        return index[(l1,pf_rep(k,l2,m))], index[(l2,pf_rep(k,l1,-m))]
    entries = Counter(pair(a) for a in allowed)
    M = [[0 for _ in chiral] for _ in chiral]
    for (i,j),multiplicity in entries.items():
        M[i][j] = multiplicity
        # An EXACT rational T-phase check (central charges agree).
        hL = h_su(k,chiral[i][0])+h_pf(k,chiral[i][1])
        hR = h_su(k,chiral[j][0])+h_pf(k,chiral[j][1])
        assert (hL-hR).denominator == 1
    vac = index[(0,pf_rep(k,0,0))]
    assert M[vac][vac] == 1
    # The common action is free. Individual chiral identifications can still
    # give multiplicities in the left/right-pair matrix; do not delete them.
    return dict(allowed=allowed,all_L_count=len(allowed_L),all_R_count=len(allowed_R),
                pf_labels=pf_labels,chiral=chiral,index=index,pair=pair,M=M,
                common_id_order=len(common_id),max_multiplicity=max(entries.values()),
                nonzero_pairs=len(entries))


def max_abs(M: Any) -> Any:
    return max(abs(M[i,j]) for i in range(M.rows) for j in range(M.cols))


def modular_check(k: int, dps: int) -> dict[str,Any]:
    data = finite_data(k)
    with mp.workdps(dps):
        tol = mp.mpf(10)**(-dps+12)
        def s_su(l: int, r: int) -> Any:
            return mp.sqrt(mp.mpf(2)/(k+2))*mp.sin(mp.pi*(l+1)*(r+1)/(k+2))
        def s_pf(a: tuple[int,int], b: tuple[int,int]) -> Any:
            l,m = a; r,n = b
            return (2/mp.sqrt(k*(k+2))*mp.sin(mp.pi*(l+1)*(r+1)/(k+2))
                    *mp.exp(1j*mp.pi*m*n/k))
        ch = data['chiral']
        S = mp.matrix([[s_su(l,r)*s_pf(a,b) for r,b in ch] for l,a in ch])
        M = mp.matrix(data['M'])
        unitary_residual = max_abs(S.conjugate().T*S-mp.eye(len(ch)))
        # Z = chi^T M conjugate(chi) => S^T M conjugate(S) = M.
        modular_residual = max_abs(S.T*M*S.conjugate()-M)
        if max(unitary_residual,modular_residual) >= tol:
            raise AssertionError(f'Modular test failed at k={k}, dps={dps}')
        output = dict(k=k,dps=dps,allowed_left=data['all_L_count'],allowed_right=data['all_R_count'],
                      allowed_intersection=len(data['allowed']),common_identification_order=1,
                      chiral_dimension=len(ch),nonzero_gluing_entries=data['nonzero_pairs'],
                      largest_gluing_multiplicity=data['max_multiplicity'],vacuum_multiplicity=1,
                      T_invariance='PASS (exact rational weights)',
                      S_unitarity_residual=mp.nstr(unitary_residual,12),
                      S_invariance_residual=mp.nstr(modular_residual,12))
        if k == 4:
            # Adversarial control: quotient by BOTH separate identification
            # operations. This is not the common group in QS (8).
            def wrong_orbit(a: tuple[int,int,int]) -> set[tuple[int,int,int]]:
                l1,l2,m = a
                return {(l1,l2,m),(l1,k-l2,(m+k)%(2*k)),
                        (k-l1,l2,(m+k)%(2*k)),(k-l1,k-l2,m)}
            wrong_reps = sorted({min(wrong_orbit(a)) for a in data['allowed']})
            wrong = mp.zeros(len(ch))
            for a in wrong_reps:
                i,j = data['pair'](a)
                wrong[i,j] += 1
            bad_residual = max_abs(S.T*wrong*S.conjugate()-wrong)
            assert bad_residual > mp.mpf('0.01')
            output['negative_control'] = {'wrong_quotient_representatives':len(wrong_reps),
                    'modular_residual':mp.nstr(bad_residual,20),'status':'WRONG QUOTIENT REJECTED'}
        return output


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--json',type=Path)
    args = ap.parse_args()
    runs = [modular_check(k,dps) for dps in (40,65) for k in (2,3,4)]
    result = {'status':'PASS','python':platform.python_version(),'mpmath':mp.__version__,
              'source':'Quella--Schomerus hep-th/0212119v3 sec.2.3 eqs.(7)-(8), sec.4.2 p=q=1',
              'scope':'Compact rational asymmetric control only; no Taub--NUT BRST certification',
              'runs':runs}
    if args.json:
        args.json.parent.mkdir(parents=True,exist_ok=True)
        args.json.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print('PASS: compact asymmetric state-space gluing control, k=2,3,4; 40/65 digits')
    for item in runs[-3:]:
        print(f"k={item['k']}: {item['allowed_intersection']} allowed triples, "
              f"S residual {item['S_invariance_residual']}, exact T check PASS")
    print('Wrong generated-group quotient rejected. No Taub--NUT gate is promoted.')

if __name__ == '__main__':
    main()
