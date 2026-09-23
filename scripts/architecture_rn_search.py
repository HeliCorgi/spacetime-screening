"""A-directed RN continuation using the unchanged protocol record validator.

No A claim or automated merging. The old first batch stays byte-for-byte intact.
Generation and separate verification are joined only after hash/coverage checks.
"""
from __future__ import annotations
import argparse
import copy
import json
import os
from pathlib import Path
import platform
import mpmath
import sympy
from architecture_search import (load_json,sha256,validate_bundle,validate_record,require,
                                compare_precision,write_json,render,git_sha,require_human_review_for_a)
from architecture_rn_models import geometry_checks,certify_box,rational_sweep,numeric_diagnostics,seam_diagnostic

ROOT=Path(__file__).resolve().parents[1]
FILES=['architecture/rn-a-target-v2.json','architecture/requirements.lock','docs/4d-past-signalling-protocol.txt',
       'scripts/architecture_rn_models.py','scripts/architecture_rn_search.py','scripts/architecture_rn_verify.py',
       'scripts/test_architecture_rn_search.py','scripts/architecture_search.py','.github/workflows/architecture-rn-search.yml']
IDS={'rn-causal-slope-support','rn-single-seam-offset'}


def report(bundle):
    text=render(bundle)
    return text.replace('— 初回バッチ','— A-directed RN継続',1).replace('固定した初回バッチ','固定したRN継続バッチ',1)


def generate(output):
    cfg=load_json(ROOT/'architecture/rn-a-target-v2.json')
    require(cfg['precision_dps']==[50,80],'Do not lower precision')
    require(sha256(ROOT/cfg['protocol_file'])==cfg['protocol_sha256'],'Protocol bytes changed')
    require({r['candidate_id'] for r in cfg['candidates']}==IDS,'Expected two specified candidates')
    checks=geometry_checks();cert=certify_box();rows,counts,witness=rational_sweep()
    p50=numeric_diagnostics(50);p80=numeric_diagnostics(80);compare_precision(p50,p80)
    support={'tested':counts['tested'],'trials':rows,'stable':counts['stable'],'outside':counts['outside'],
             'invalid_exterior':counts['invalid_exterior'],'witness':witness,'certificate':cert,
             'near_extremal':p80,'checks':checks,'verdict':'conditional_radial_stability','probability_law_computed':False}
    results={'rn-causal-slope-support':support,'rn-single-seam-offset':seam_diagnostic()}
    records=[]
    for template in cfg['candidates']:
        r=copy.deepcopy(template);r['calculation']=results[r['candidate_id']]
        r['numerical_error_budget']={'precision_dps':[50,80],'agreement_relative':'1e-40',
           'exact_parts':'Fraction grid and rational interval certificate; the verifier uses a different Bernstein certificate.',
           'numerical_parts':'Optical integrals and nonlinear EOS differentiation compared at 50/80 dps, not certified rounding intervals.',
           'model_error':'Zero-thickness idealization and missing source/nonradial/dynamical effects are NOT estimated by decimal precision.',
           'sampling':'Finite deterministic parameter set; stable fraction is not a probability of physical realizability.'}
        validate_record(r);records.append(r)
    bundle={'schema_version':1,'batch_id':cfg['batch_id'],'counts':{k:sum(r['status']==k for r in records) for k in ('A','B','C')},
            'coverage':cfg['coverage'],'provenance':{'source_base_sha':cfg['source_base_sha'],'checkout_sha':git_sha(ROOT),
             'execution':'GitHub Actions' if os.getenv('GITHUB_ACTIONS')=='true' else 'local','github_run_id':os.getenv('GITHUB_RUN_ID'),
             'python':platform.python_version(),'sympy':sympy.__version__,'mpmath':mpmath.__version__,
             'file_sha256':{p:sha256(ROOT/p) for p in FILES}},'candidates':records}
    validate_bundle(bundle,ROOT);output.mkdir(parents=True,exist_ok=True)
    write_json(output/'candidates.json',bundle);(output/'report.md').write_text(report(bundle),encoding='utf-8')
    print(json.dumps({'counts':bundle['counts'],'RN_grid':counts,'additional_clock_controls':15,'verification':'pending'}))
    return bundle


def finalize(raw,verification,output,gate):
    b=load_json(raw);validate_bundle(b,ROOT);v=load_json(verification)
    require(v.get('input_sha256')==sha256(raw),'Stale raw/verification pairing')
    require(v.get('verification_program_sha256')==sha256(ROOT/'scripts/architecture_rn_verify.py'),'Verifier changed')
    require(set(v.get('candidates',{}))==IDS=={r['candidate_id'] for r in b['candidates']},'Missing/unknown candidate task')
    for r in b['candidates']:
        require(v['candidates'][r['candidate_id']].get('software_check')=='passed','Failed verification')
        r['verification'].update(computational='passed',independent_task='architecture_rn_verify.py, separate CI job; same author, not independent peer review')
    b['verification_artifact_sha256']=sha256(verification)
    validate_bundle(b,ROOT);output.mkdir(parents=True,exist_ok=True)
    write_json(output/'candidates.json',b);(output/'report.md').write_text(report(b),encoding='utf-8')
    # Retain all outputs before blocking A clearance.
    if gate:require_human_review_for_a(b)
    print('Verified RN continuation: '+json.dumps(b['counts'])+'; external peer review not performed')
    return b


if __name__=='__main__':
    p=argparse.ArgumentParser();sub=p.add_subparsers(dest='command',required=True)
    q=sub.add_parser('run');q.add_argument('--output',type=Path,required=True)
    q=sub.add_parser('finalize');q.add_argument('--records',type=Path,required=True);q.add_argument('--verification',type=Path,required=True);q.add_argument('--output',type=Path,required=True);q.add_argument('--gate',action='store_true')
    args=p.parse_args()
    if args.command=='run':generate(args.output)
    else:finalize(args.records,args.verification,args.output,args.gate)
