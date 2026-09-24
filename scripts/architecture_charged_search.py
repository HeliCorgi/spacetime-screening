"""Generate validated v3 records and reports; unknown channels remain unknown."""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import platform
import sys
import architecture_search as protocol

ROOT=Path(__file__).resolve().parents[1]
CONFIG='architecture/charged-source-handle-v3.json'
IDS={'rn-smooth-conformal-source','mp-same-exterior-handle'}
# Explicit extension for one new scoped obstruction; no A requirement is changed.
protocol.VERDICTS['specified_conformal_trace_tail_mismatch']='C'
FILES=[CONFIG,'architecture/requirements.lock','docs/4d-past-signalling-protocol.txt',
       'scripts/architecture_charged_models.py','scripts/architecture_charged_search.py',
       'scripts/architecture_charged_verify.py','scripts/test_architecture_charged_search.py',
       'scripts/architecture_search.py','.github/workflows/architecture-charged-completion.yml']

def write(path,value):
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(value,indent=2,ensure_ascii=False,allow_nan=False)+'\n',encoding='utf-8')

def validate(bundle,root=ROOT):
    protocol.validate_bundle(bundle,root)
    protocol.require({r['candidate_id'] for r in bundle['candidates']}==IDS,'Unexpected v3 candidate set')
    for r in bundle['candidates']:
        expected=18 if r['candidate_id']=='rn-smooth-conformal-source' else 19
        protocol.require(r['calculation']['tested']==expected,'Missing v3 computation points')

def report(bundle):
    lines=['# 四次元の支持源と同一外部ハンドル：v3', '',
           '分類: '+json.dumps(bundle['counts'])+'。異なる二模型の診断であり、同じ完成装置ではありません。',
           'Checkout: `'+str(bundle['provenance']['checkout_sha'])+'`',
           '独立研究者の査読: 未実施。Aは自動承認しません。','']
    for row in bundle['candidates']:
        lines += ['## '+row['candidate_id']+' — '+row['status'],'',row['title'],'']
        for key,value in row.items():
            if key in ('candidate_id','status','title'):continue
            lines += ['### '+key,'']
            if isinstance(value,str):lines += [value,'']
            else:lines += ['```json',json.dumps(value,indent=2,ensure_ascii=False,allow_nan=False),'```','']
    return '\n'.join(lines)+'\n'

def run(output,root=ROOT):
    import mpmath, sympy
    from architecture_charged_models import exact_checks,all_experiments
    config=protocol.load_json(root/CONFIG)
    protocol.require(config['precision_dps']==[50,80],'Do not weaken precision')
    protocol.require(protocol.sha256(root/config['protocol_file'])==config['protocol_sha256'],'Protocol changed')
    exact=exact_checks();lo=all_experiments(50);hi=all_experiments(80)
    protocol.compare_precision(lo,hi)
    rows=[]
    for template in config['candidates']:
        row=copy.deepcopy(template);calc=hi[row['candidate_id']];calc['tested']=len(calc['trials'])
        row['status']=protocol.VERDICTS[calc['verdict']];row['calculation']=calc
        row['numerical_error_budget']={'precision_dps':[50,80],'agreement_relative':'1e-40',
            'independent_check_relative':'1e-39','approximation_error':'No numerical bound for model changes, stability, geometry formation or quantum-source completion.',
            'exact':'Symbolic identities and asymptotic coefficient contradiction; finite point sampling is not the proof.',
            'sampling':'37 deterministic diagnostics; not random samples of natural possibilities.'}
        rows.append(row)
    bundle={'schema_version':1,'batch_id':config['batch_id'],'candidates':rows,
        'counts':{s:sum(r['status']==s for r in rows) for s in ('A','B','C')},'exact_checks':exact,
        'provenance':{'source_base_sha':config['source_base_sha'],'checkout_sha':protocol.git_sha(root),
            'execution':'GitHub Actions' if os.getenv('GITHUB_ACTIONS')=='true' else 'local',
            'github_run_id':os.getenv('GITHUB_RUN_ID'),'python':platform.python_version(),'sympy':sympy.__version__,'mpmath':mpmath.__version__,
            'file_sha256':{p:protocol.sha256(root/p) for p in FILES}},
        'coverage':{'not_assessed_now':['Full RSET on a new background','Source/control fabrication','Dynamical time-holonomy preparation','Stability of charged handle','Past detector probabilities']}}
    validate(bundle,root);write(output/'candidates.json',bundle)
    (output/'report.md').write_text(report(bundle),encoding='utf-8')
    return bundle

def finalize(records,verification,output,gate=False,root=ROOT):
    bundle=protocol.load_json(records);validate(bundle,root);proof=protocol.load_json(verification)
    protocol.require(proof['records_sha256']==protocol.sha256(records),'Stale verification')
    checks=proof.get('candidates',[])
    protocol.require(len(checks)==len(IDS) and {c['candidate_id'] for c in checks}==IDS,'Incomplete verification coverage')
    byid={r['candidate_id']:r for r in bundle['candidates']}
    for c in checks:
        protocol.require(c.get('passed') is True and c['checked']==byid[c['candidate_id']]['calculation']['tested'],'Failed or incomplete verification')
    protocol.require(proof.get('checks',{}).get('MP_bulk_Einstein_Maxwell')=='direct 4D tensor identity','Missing geometry verification')
    for r in bundle['candidates']:
        r['verification']['computational']='passed_same_author_separate_implementation'
        r['verification']['independent_task']=proof
    validate(bundle,root);write(output/'candidates.json',bundle)
    (output/'report.md').write_text(report(bundle),encoding='utf-8')
    if gate and bundle['counts']['A']:
        raise protocol.RecordError('A requires human scientific review; output saved but clearance blocked')
    return bundle

if __name__=='__main__':
    parser=argparse.ArgumentParser();sub=parser.add_subparsers(dest='command',required=True)
    r=sub.add_parser('run');r.add_argument('--output',type=Path,required=True)
    f=sub.add_parser('finalize');f.add_argument('--records',type=Path,required=True);f.add_argument('--verification',type=Path,required=True);f.add_argument('--output',type=Path,required=True);f.add_argument('--gate',action='store_true')
    args=parser.parse_args()
    try:
        out=run(args.output) if args.command=='run' else finalize(args.records,args.verification,args.output,args.gate)
        print(json.dumps({'counts':out['counts'],'points':sum(r['calculation']['tested'] for r in out['candidates']),'external_peer_review':'not_performed'}))
    except (ValueError,KeyError,OSError) as exc:
        print('ERROR (not a physical C): '+str(exc),file=sys.stderr);sys.exit(1)
