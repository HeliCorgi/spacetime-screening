"""Generate/validate protocol records; stage failures are not physical C results.

Run: python scripts/architecture_search.py run --output /tmp/architecture-out
Then run architecture_verify.py and `finalize`. No GitHub write/merge operation exists.
"""
from __future__ import annotations
import argparse
import copy
from decimal import Decimal, InvalidOperation
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import subprocess
import sys
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = '''candidate_id status geometry matter_content quantum_state dimension topology assumptions boundary_conditions symmetries approximation_order stress_energy backreaction support_accounting stability causal_structure sender_intervention receiver_observable P_Y_do_0 P_Y_do_1 distinguishability obstructions unresolved_assumptions literature code verification scope'''.split()
TEXT = '''candidate_id geometry matter_content quantum_state topology boundary_conditions approximation_order stability causal_structure receiver_observable scope'''.split()
EVIDENCE_KEYS = '''global_stress_matching semiclassical_self_consistency apparatus_complete stability_appropriate initial_boundary_consistency finite_receiver_record intervention_not_correlation renormalized_source_supplied'''.split()
IDS = {'flat-local-source','rotating-global-time','schwarzschild-eos-0-to-1','schwarzschild-eos-4','fkz-mass-controlled-ring','finite-casimir-cell-line','thin-collar-qei-window'}
VERDICTS = {
 'retarded_local_source_no_past_dependence':'C',
 'global_time_obstruction':'C',
 'radial_instability_on_stated_domain':'C',
 'conditional_radial_stability':'B',
 'conditional_classical_past_path':'B',
 'independent_cells_cannot_supply_negative_total_line_energy':'C',
 'thin_layer_not_excluded_by_this_necessary_diagnostic':'B'}

class RecordError(ValueError):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RecordError(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical_sha(value: Any) -> str:
    return hashlib.sha256(json.dumps(value,sort_keys=True,ensure_ascii=False,allow_nan=False).encode()).hexdigest()


def load_json(path: Path) -> Any:
    def reject_constant(value: str) -> None:
        raise RecordError('Non-finite JSON value: '+value)
    def unique_pairs(pairs: list[tuple[str,Any]]) -> dict:
        result={}
        for key,value in pairs:
            require(key not in result, 'Duplicate JSON key: '+key)
            result[key]=value
        return result
    return json.loads(path.read_text(encoding='utf-8'),parse_constant=reject_constant,object_pairs_hook=unique_pairs)


def finite_decimal(value: Any, name: str) -> Decimal:
    require(isinstance(value,str),name+' must be a decimal string')
    try:
        d=Decimal(value)
    except InvalidOperation as exc:
        raise RecordError(name+' is not numeric') from exc
    require(d.is_finite(),name+' is not finite')
    return d


def local_path(name: str, root: Path) -> Path:
    require(isinstance(name,str) and bool(name),'Invalid path')
    p=(root/name).resolve()
    require(p.is_relative_to(root.resolve()),'Path escapes repository: '+name)
    require(p.is_file(),'Missing file: '+name)
    return p


def validate_record(r: dict[str,Any]) -> None:
    require(isinstance(r,dict),'Candidate must be an object')
    require(all(k in r for k in REQUIRED),'Missing required fields: '+','.join(k for k in REQUIRED if k not in r))
    for key in TEXT:
        require(isinstance(r[key],str) and bool(r[key].strip()),'Empty/nontext '+key)
    require(bool(re.fullmatch(r'[a-z0-9][a-z0-9-]*',r['candidate_id'])),'Invalid candidate ID')
    require(r['status'] in ('A','B','C'),'Exactly one status A/B/C required')
    require(type(r['dimension']) is int and r['dimension']==4,'Only explicit 3+1D candidates belong in this batch')
    require(r.get('dimension_split')=={'space':3,'time':1},'Wrong spacetime dimension split')
    for key in ('assumptions','symmetries','literature','code','obstructions','unresolved_assumptions'):
        require(isinstance(r[key],list),'List required: '+key)
    require(bool(r['assumptions']) and bool(r['code']) and bool(r['literature']),'Assumptions/code/literature cannot be empty')
    for key in ('assumptions','symmetries','code','obstructions','unresolved_assumptions'):
        require(all(isinstance(x,str) and x.strip() for x in r[key]),'Invalid list entry: '+key)
    for key in ('stress_energy','backreaction','support_accounting','sender_intervention','distinguishability','verification'):
        require(isinstance(r[key],dict) and bool(r[key]),'Structured object required: '+key)
    for key in ('kind','formula','renormalized','full_tensor_matched'):
        require(key in r['stress_energy'],'Missing source field '+key)
    for flag in ('renormalized','full_tensor_matched'):
        require(type(r['stress_energy'][flag]) is bool,'Source evidence flag must be Boolean: '+flag)
    for key in ('kind','formula'):
        require(isinstance(r['stress_energy'][key],str) and bool(r['stress_energy'][key].strip()),'Source description required: '+key)
    for key in ('complete','details'):
        require(key in r['support_accounting'],'Missing support field '+key)
    require(type(r['support_accounting']['complete']) is bool,'Support completeness must be a Boolean')
    require('level' in r['backreaction'] and 'details' in r['backreaction'],'Backreaction level/details required')
    for flag in ('same_preparation','uses_postselection','future_boundary_condition_is_input'):
        require(type(r['sender_intervention'].get(flag)) is bool,'Missing explicit intervention flag: '+flag)
    require(isinstance(r.get('assumption_changes'),list),'Assumption changes must be explicitly recorded, even when empty')
    for change in r['assumption_changes']:
        require(isinstance(change,dict) and all(isinstance(change.get(k),str) and change[k].strip() for k in ('field','old','new','reason')),'Incomplete assumption-change record')
    stages=r.get('stages',{})
    require(set(stages)==set('1234567'),'All seven stages need an explicit state')
    for stage in stages.values():
        require(isinstance(stage,dict) and stage.get('state') in ('completed','partial','not_reached'),'Invalid stage state')
        require(isinstance(stage.get('name'),str) and bool(stage['name']),'Stage name required')
    for item in r['literature']:
        require(isinstance(item,dict),'Literature object required')
        for key in ('title','authors','year','url','used_for','checked_on'):
            require(key in item and bool(item[key]),'Incomplete source metadata: '+key)
        require(item['url'].startswith('https://'),'Source URL must use https')
        require(isinstance(item['year'],int) and item['year']<=2026,'Invalid source year')
    for pkey in ('P_Y_do_0','P_Y_do_1'):
        p=r[pkey]
        require(isinstance(p,dict) and type(p.get('computed')) is bool,'Probability computed flag required')
        if not p['computed']:
            require(p.get('distribution') is None and bool(p.get('reason')),'Unknown probability must be null with reason, not zero')
        else:
            d=p.get('distribution')
            require(isinstance(d,dict) and bool(d.get('family')),'Explicit computed distribution required')
            if d['family']=='normal':
                finite_decimal(d.get('mean'),'mean')
                require(finite_decimal(d.get('variance'),'variance')>0,'Positive variance required')
            else:
                raise RecordError('New distribution family requires an explicit validation implementation')
    dist=r['distinguishability']
    require(dist.get('metric')=='total_variation','Specify the distinguishability metric')
    both=all(r[k]['computed'] for k in ('P_Y_do_0','P_Y_do_1'))
    require(type(dist.get('computed')) is bool and dist['computed']==both,'Probability/distinguishability mismatch')
    if both:
        value=finite_decimal(dist.get('value'),'D')
        error=finite_decimal(dist.get('error_bound'),'D error')
        require(0<=value<=1 and error>=0,'Invalid D or numerical error budget')
        d0,d1=r['P_Y_do_0']['distribution'],r['P_Y_do_1']['distribution']
        if d0==d1:
            require(value==0,'Identical distributions cannot certify a nonzero D')
    else:
        require(dist.get('value') is None and dist.get('error_bound') is None,'No fabricated zero/error for an unknown channel')
    require(bool(r.get('calculation')) and r['calculation'].get('tested',0)>0,'A candidate needs an actual calculation, not an empty template')
    calc=r['calculation']
    require(type(calc['tested']) is int and isinstance(calc.get('trials'),list) and len(calc['trials'])==calc['tested'],'Calculation point count must match its records')
    require(isinstance(r.get('numerical_error_budget'),dict) and bool(r['numerical_error_budget']),'Numerical error budget required')
    if r['status'] in ('B','C'):
        require(VERDICTS.get(calc.get('verdict'))==r['status'],'Status contradicts registered scoped verdict')
    if r['status']=='C':
        require(bool(r['obstructions']),'C requires a scoped demonstrated obstruction')
    if r['status']=='B':
        require(bool(r['unresolved_assumptions']),'B requires its explicit unresolved assumptions')
    if r['status']=='A':
        require(r.get('candidate_kind')=='channel','A cannot be a component-only result')
        require(both and dist.get('receiver_precedes_sender') is True,'A needs an actual past receiver experiment')
        require(value>error,'A needs D larger than its error bound')
        require(not r['obstructions'] and not r['unresolved_assumptions'],'A cannot retain unresolved physical assumptions')
        evidence=r.get('construction_evidence',{})
        require(all(evidence.get(k) is True for k in EVIDENCE_KEYS),'A lacks complete physical construction evidence')
        require(r['support_accounting']['complete'] is True,'A lacks complete apparatus accounting')
        require(r['stress_energy']['renormalized'] is True,'A lacks renormalized quantum source')
        sender=r['sender_intervention']
        require(sender.get('same_preparation') is True and sender.get('uses_postselection') is False and sender.get('future_boundary_condition_is_input') is False,'A has a hidden intervention/selection/boundary assumption')
    require(r['verification'].get('human_review_for_A') is True,'Human review rule cannot be disabled')


def validate_bundle(bundle: dict, root: Path | None = None) -> None:
    require(isinstance(bundle,dict) and bundle.get('schema_version')==1,'Unknown record schema')
    rows=bundle.get('candidates')
    require(isinstance(rows,list) and len(rows)>0,'Empty search is not success')
    ids=[r.get('candidate_id') for r in rows]
    require(len(set(ids))==len(ids),'Duplicate candidate IDs')
    for r in rows: validate_record(r)
    require(bundle.get('counts')=={s:sum(r['status']==s for r in rows) for s in ('A','B','C')},'Stale classification counts')
    provenance=bundle.get('provenance',{})
    require(re.fullmatch('[0-9a-f]{40}',str(provenance.get('source_base_sha',''))) is not None,'Source base SHA missing')
    checkout=provenance.get('checkout_sha')
    require(checkout is None or re.fullmatch('[0-9a-f]{40}',checkout) is not None,'Invalid checkout SHA')
    require(bool(provenance.get('file_sha256')),'No code/input provenance')
    if root is not None:
        for path,expected in provenance['file_sha256'].items():
            require(sha256(local_path(path,root))==expected,'Input/code hash mismatch: '+path)
        for r in rows:
            for path in r['code']: local_path(path,root)
    require(bundle.get('coverage',{}).get('not_assessed_now') is not None,'Search coverage must be explicit')


def compare_precision(a: Any,b: Any) -> None:
    import mpmath as mp
    if isinstance(a,dict):
        require(isinstance(b,dict) and set(a)==set(b),'Precision runs changed keys')
        for key in a: compare_precision(a[key],b[key])
    elif isinstance(a,list):
        require(isinstance(b,list) and len(a)==len(b),'Precision runs changed trial count')
        for x,y in zip(a,b): compare_precision(x,y)
    elif isinstance(a,str) and isinstance(b,str):
        try:
            with mp.workdps(90):
                x,y=mp.mpf(a),mp.mpf(b)
                require(abs(x-y)<=mp.mpf('1e-40')*max(abs(x),abs(y),mp.mpf('1e-100')),'50/80-digit numerical mismatch')
        except (ValueError,ZeroDivisionError):
            require(a==b,'Precision runs changed text')
    else:
        require(a==b,'Precision runs changed logical result')


def git_sha(root: Path) -> str | None:
    p=subprocess.run(['git','rev-parse','HEAD'],cwd=root,capture_output=True,text=True,check=False)
    return p.stdout.strip() if p.returncode==0 else None


def run_batch(root: Path, output: Path) -> dict:
    import mpmath
    import sympy
    from architecture_models import all_experiments
    config_path=root/'architecture/batch-v1.json'
    config=load_json(config_path)
    require(config.get('precision_dps')==[50,80],'Changing precision requires a reviewed protocol update')
    require(sha256(root/config['protocol_file'])==config['protocol_sha256'],'Uploaded protocol changed without an explicit version update')
    require({r['candidate_id'] for r in config['candidates']}==IDS,'This fixed first batch needs all seven audited families')
    first=all_experiments(50); results=all_experiments(80)
    compare_precision(first,results)
    rows=[]
    for template in config['candidates']:
        row=copy.deepcopy(template); calc=results[row['candidate_id']]
        require(calc['verdict'] in VERDICTS,'Unreviewed verdict; do not default an unknown outcome to B or C')
        row['status']=VERDICTS[calc['verdict']]
        row['calculation']=calc
        row['numerical_error_budget']={
            'precision_dps':[50,80], 'agreement_relative':'1e-40','absolute_floor':'1e-140',
            'roundoff':'Independent precision rerun, NOT rigorous interval certification.',
            'approximation_error':'Not numerically certified; stated individually in approximation_order and scope.',
            'sampling':'Deterministic parameter sweep, not statistical evidence or a success probability.'}
        if row['candidate_id']=='flat-local-source':
            for k in ('P_Y_do_0','P_Y_do_1'):
                row[k]={'computed':True,'distribution':{'family':'normal','mean':'0','variance':'1'},'reason':'Past t=-1, source starts at 0; normalized full-outcome meter model, no postselection.'}
            row['distinguishability'].update(computed=True,value='0',error_bound='0',receiver_precedes_sender=True,
                interpretation='Exactly identical past distributions in this explicitly retarded G^0 protocol. Future contrast is not the target.')
        validate_record(row); rows.append(row)
    paths=['architecture/batch-v1.json','architecture/requirements.lock',config['protocol_file'],
           'scripts/architecture_models.py','scripts/architecture_search.py','scripts/architecture_verify.py','scripts/test_architecture_search.py',
           '.github/workflows/architecture-search.yml']
    bundle={'schema_version':1,'batch_id':config['batch_id'],
            'counts':{s:sum(r['status']==s for r in rows) for s in ('A','B','C')},
            'coverage':config['coverage'],
            'provenance':{'source_base_sha':config['source_base_sha'],'checkout_sha':git_sha(root),
                          'execution':'GitHub Actions' if os.getenv('GITHUB_ACTIONS')=='true' else 'local',
                          'github_run_id':os.getenv('GITHUB_RUN_ID'),
                          'python':platform.python_version(),'sympy':sympy.__version__,'mpmath':mpmath.__version__,
                          'file_sha256':{p:sha256(root/p) for p in paths}},
            'candidates':rows}
    validate_bundle(bundle,root)
    output.mkdir(parents=True,exist_ok=True)
    write_json(output/'candidates.json',bundle)
    (output/'report.md').write_text(render(bundle),encoding='utf-8')
    print(json.dumps({'counts':bundle['counts'],'trials':sum(r['calculation']['tested'] for r in rows),'verification':'pending'},ensure_ascii=False))
    return bundle


def write_json(path: Path,obj: Any) -> None:
    text=json.dumps(obj,ensure_ascii=False,indent=2,allow_nan=False)+'\n'
    path.parent.mkdir(parents=True,exist_ok=True)
    temp=path.with_suffix(path.suffix+'.tmp');temp.write_text(text,encoding='utf-8');temp.replace(path)


def render(bundle: dict) -> str:
    validate_bundle(bundle)
    counts=bundle['counts']; p=bundle['provenance']
    lines=['# 4D Past-Signalling Architecture Search — 初回バッチ', '',
           f"**A={counts['A']} / B={counts['B']} / C={counts['C']}**。候補・部分構成の分類で、自然界の確率ではありません。",'',
           'A: 完成した構成候補（人間の審査必須）。B: 明記した仮定を要する条件付きの部分候補。C: 明記した範囲の障害。',
           '局所一致、必要条件の通過、古典的経路、未来側の受信差はAになりません。', '',
           f"実行: {p['execution']} / Python {p['python']} / SymPy {p['sympy']} / mpmath {p['mpmath']}",
           f"読取基点: `{p['source_base_sha']}`。実行checkout SHA: `{p['checkout_sha'] or '未取得（ローカル全repo checkoutなし）'}`。",'',
           '| 候補 | 分類 | 計算点数 | 反証用の別実装 |', '|---|---|---:|---|']
    for r in bundle['candidates']:
        lines.append(f"| {r['candidate_id']} — {r['title']} | {r['status']} | {r['calculation']['tested']} | {r['verification']['computational']} |")
    lines += ['', '## 探索の範囲', '固定した初回バッチの再現可能な探索です。全モデル空間の網羅や無期限の自律研究ではありません。',
              '文献選定は出典付きで固定し、Actions内でオンライン文献を自動採用しません。', '', '### 未探索（候補B/Cとして水増ししない）']
    for entry in bundle['coverage']['not_assessed_now']:
        lines.append(f"- **{entry['class']}**: {entry['reason']}")
    for r in bundle['candidates']:
        lines += ['',f"## {r['candidate_id']} — {r['status']}",r['title'],'',
                  f"**適用範囲:** {r['scope']}",'',f"**分類の直接根拠:** `{r['calculation']['verdict']}`",'',
                  '| Stage | 作業 | 状態 |','|---|---|---|']
        for k,s in r['stages'].items(): lines.append(f"| {k} | {s['name']} | {s['state']} |")
        for key in REQUIRED:
            if key in ('candidate_id','status','dimension','scope','literature'):continue
            value=r[key]
            if isinstance(value,(dict,list)):
                text=json.dumps(value,ensure_ascii=False,indent=2)
                lines += ['',f'### {key}','```json',text,'```']
            else: lines += ['',f'### {key}',str(value)]
        lines += ['', '### Assumption changes', '```json',json.dumps(r['assumption_changes'],ensure_ascii=False,indent=2),'```',
                  '', '### 数値・モデル誤差', '```json',json.dumps(r['numerical_error_budget'],ensure_ascii=False,indent=2),'```','', '### 一次資料']
        for ref in r['literature']:
            lines.append(f"- {ref['authors']} ({ref['year']}), [{ref['title']}]({ref['url']}). {ref['used_for']}")
    lines += ['', '## 検証の限界', '別実装の計算検証は、同じ作成者による別プログラムです。独立研究者の査読・別AI研究員による検証ではありません。',
              'CI成功は、実装されたチェックの成功だけを表します。自動マージ機能はありません。Aの主張は必ず人間へエスカレーションします。','']
    return '\n'.join(lines)


def require_human_review_for_a(bundle: dict) -> None:
    require(not any(r.get('status')=='A' for r in bundle['candidates']),
            'A CLAIM: automatic clearance is blocked. Independent physical and human review is mandatory; artifacts retained.')


def collect_verifications(raw: Path, directory: Path, output: Path, root: Path=ROOT) -> dict:
    """Join separate tasks; stale, duplicate, missing or failing results stop the pipeline."""
    b=load_json(raw);validate_bundle(b,root)
    files=sorted(directory.glob('*.json'))
    require(bool(files),'No verification artifacts')
    input_hash=sha256(raw); program_hash=sha256(root/'scripts/architecture_verify.py')
    combined={}; executions=[]
    for path in files:
        v=load_json(path)
        require(v.get('input_sha256')==input_hash,'Stale per-candidate verification')
        require(v.get('verification_program_sha256')==program_hash,'Different verifier program')
        require(isinstance(v.get('candidates'),dict) and bool(v['candidates']),'Empty verification task')
        for cid,result in v['candidates'].items():
            require(cid not in combined,'Duplicate verification task '+cid)
            require(result.get('software_check')=='passed','Failed verification task '+cid)
            combined[cid]=result
        executions.append({'file':path.name,'sha256':sha256(path),'execution':v.get('execution'),
                           'python':v.get('python')})
    require(set(combined)=={r['candidate_id'] for r in b['candidates']},'Missing/unknown verification task')
    merged={'input_sha256':input_hash,'verification_program_sha256':program_hash,
            'candidates':combined,'task_artifacts':executions,'external_peer_review':'not_performed'}
    write_json(output,merged)
    print(f'Collected {len(combined)} candidate checks from {len(files)} task artifacts.')
    return merged


def finalize(raw: Path, verification: Path, output: Path, root: Path=ROOT, gate: bool=False) -> dict:
    b=load_json(raw);validate_bundle(b,root)
    v=load_json(verification)
    require(v.get('input_sha256')==sha256(raw),'Verifier checked another/stale artifact')
    require(v.get('verification_program_sha256')==sha256(root/'scripts/architecture_verify.py'),'Verifier program hash mismatch')
    expected={r['candidate_id'] for r in b['candidates']}
    require(set(v.get('candidates',{}))==expected,'Every candidate, including every B/A, needs its own verification result')
    for r in b['candidates']:
        result=v['candidates'][r['candidate_id']]
        require(result.get('software_check')=='passed','Verifier failure must not be hidden')
        r['verification'].update(computational='cross_checked',independent_task=result,
                                 verifier_artifact_sha256=sha256(verification))
    validate_bundle(b,root)
    output.mkdir(parents=True,exist_ok=True)
    write_json(output/'candidates.json',b)
    write_json(output/'verification.json',v)
    (output/'report.md').write_text(render(b),encoding='utf-8')
    if gate:
        require_human_review_for_a(b)
    print('Final report:',json.dumps(b['counts']),'; external peer review: not performed')
    return b


def main() -> None:
    p=argparse.ArgumentParser(description=__doc__)
    sub=p.add_subparsers(dest='command',required=True)
    r=sub.add_parser('run');r.add_argument('--output',type=Path,required=True)
    v=sub.add_parser('validate');v.add_argument('--records',type=Path,required=True)
    c=sub.add_parser('collect');c.add_argument('--records',type=Path,required=True);c.add_argument('--directory',type=Path,required=True);c.add_argument('--output',type=Path,required=True)
    f=sub.add_parser('finalize');f.add_argument('--records',type=Path,required=True);f.add_argument('--verification',type=Path,required=True);f.add_argument('--output',type=Path,required=True);f.add_argument('--gate',action='store_true')
    args=p.parse_args()
    try:
        if args.command=='run': run_batch(ROOT,args.output)
        elif args.command=='validate':validate_bundle(load_json(args.records),ROOT);print('Records valid')
        elif args.command=='collect':collect_verifications(args.records,args.directory,args.output)
        else:finalize(args.records,args.verification,args.output,gate=args.gate)
    except (RecordError,ValueError,OSError,AssertionError) as exc:
        print(f'FAILED: {type(exc).__name__}: {exc}',file=sys.stderr)
        raise SystemExit(1) from exc

if __name__=='__main__': main()
