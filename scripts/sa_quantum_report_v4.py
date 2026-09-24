"""Evidence-bound report for the SA quantum-record continuation.

Imports the unchanged repository protocol validator. Only three new scoped B/C
verdict names are registered in memory; A rules and the original file are not
modified. Missing/stale evidence is a software failure, never physical status C.
"""
from __future__ import annotations
import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import platform
import tempfile
import unittest
import mpmath
import sympy
import architecture_search as protocol

ROOT=Path(__file__).resolve().parents[1]
CONFIG='architecture/sa-quantum-record-v4.json'
JUNCTION='src/symbolic/sa_quantum_junction_v4.py'
SCATTERING='src/numerical/sa_inner_scattering_v4.py'
VERIFIER='scripts/sa_quantum_verify_v4.py'
VERDICTS={
 'global_kernels_and_boundary_completion_missing':'B',
 'single_temperature_double_horizon_incompatible':'C',
 'parity_even_readout_has_no_sign_dependence':'C'}
protocol.VERDICTS.update(VERDICTS)
EXPECTED_IDS={'sa-global-ramsey-continuation','sa-single-kms-two-horizons','sa-sign-code-energy-readout'}


def demand(ok:bool, why:str)->None:
    if not ok:raise protocol.RecordError(why)


def digest(path:Path)->str:return hashlib.sha256(path.read_bytes()).hexdigest()


def check_scope(j:dict,s:dict,v:dict)->None:
    demand(j.get('dimension')==4,'Wrong field dimensionality')
    demand(j.get('global_state_constructed') is False,'Full SA state is not constructed in this batch')
    demand(j.get('past_receiver_probabilities_computed') is False,'No full SA receiver probabilities computed')
    demand(j.get('actual_SA_m_h') is None and j.get('actual_SA_V_h') is None,'Control kernels cannot replace SA kernels')
    demand(j['finite_time_4D_noise_control'].get('actual_SA_noise') is False,'Flat control is not SA covariance')
    demand(s.get('not_full_SA_horizon_crossing') is True and s.get('past_receiver_probability') is None,
           'Inner-static reflection is not a global crossing experiment')
    demand(s.get('reflection_is_not_a_probability') is True,'Do not relabel the reflection phase')
    demand([r['omega_over_kappa_minus'] for r in s['rows']]==['0.02','0.2','2'],'Wrong or missing frequency rows')
    demand(v.get('independent_program') is True,'Alternate program verification missing')
    demand(v.get('external_peer_review')=='not_performed','Same-author arithmetic is not peer review')
    demand(v.get('state_proved_on_full_SA') is False,'False global-state promotion')
    demand(v.get('noise_within_positive_spectral_tail_bound') is True,'Noise bound not checked')
    demand(len(v.get('scattering_cross_checks',[]))==3,'Incomplete alternate scattering checks')
    for row in v['scattering_cross_checks']:
        demand(0<=row['max_reference_error']<3e-8,'Scattering alternate program failed')
        demand(0<=row['max_step_convergence_change']<2e-8,'Scattering convergence failed')


def read_evidence(root:Path,evidence:Path)->tuple[dict,dict,dict]:
    jp=evidence/'junction.json';sp=evidence/'scattering.json';vp=evidence/'verification.json'
    j=protocol.load_json(jp);s=protocol.load_json(sp);v=protocol.load_json(vp)
    demand(v.get('inputs')=={'junction':digest(jp),'scattering':digest(sp)},'Stale evidence/proof hashes')
    demand(v.get('verifier_sha256')==digest(root/VERIFIER),'Proof was produced by another verifier version')
    demand(j.get('generator_sha256')==digest(root/JUNCTION),'Junction generator changed after calculation')
    demand(s.get('generator_sha256')==digest(root/SCATTERING),'Scattering generator changed after calculation')
    check_scope(j,s,v)
    return j,s,v


def validate_current(b:dict,root:Path|None=None)->None:
    protocol.validate_bundle(b,root)
    demand({r['candidate_id'] for r in b['candidates']}==EXPECTED_IDS,'Wrong continuation candidate set')
    # These are factual scope constraints of THIS performed calculation, not a
    # global rule forbidding future A research or a lowering of the A gate.
    for r in b['candidates']:
        for key in ['P_Y_do_0','P_Y_do_1']:
            demand(r[key]['computed'] is False and r[key]['distribution'] is None,
                   'No computed full-SA distribution is available in these inputs')
        demand(r['distinguishability']['value'] is None,'Unknown full-SA D is not zero or a local control')
    demand(b['counts']=={'A':0,'B':1,'C':2},'Unexpected status change; requires a new reviewed calculation')


def build(root:Path,evidence:Path)->dict:
    cfg=protocol.load_json(root/CONFIG)
    demand(cfg['precision_dps']==[50,80],'Unreviewed precision change')
    demand(digest(root/cfg['protocol_file'])==cfg['protocol_sha256'],'Original protocol changed')
    j,s,v=read_evidence(root,evidence)
    rows=[]
    for template in cfg['candidates']:
        r=copy.deepcopy(template)
        cid=r['candidate_id']
        verdict=r.pop('verdict')
        demand(verdict in VERDICTS and r['status']==VERDICTS[verdict],'Wrong registered scoped verdict')
        if cid=='sa-global-ramsey-continuation':
            trials=s['rows']
            r['calculated_components']={'junction_and_state_scope':j,'inner_reflection':s,
                'conditional_receiver_law':{'formula':j['finite_ramsey_law'],
                   'actual_full_SA_distribution_computed':False},
                'flat_noise_alternate_control':v['finite_window_noise_time_domain']}
        elif cid=='sa-single-kms-two-horizons':
            trials=[{'temperature_ratio':j['horizon_temperature_ratio'],
               'assumption':'one common inverse temperature; two-sided regularity at both nonextremal bifurcations',
               'required':'beta*kappa_plus=beta*kappa_minus=2*pi',
               'restricted_obstruction':j['common_KMS_both_bifurcate_horizons']}]
        else:
            trials=[{'field_parity':'J0 maps to J1', 'detector_parity':'Z monopole Z=-monopole',
               'energy_readout_invariant':True,'scope':j['sign_code_energy_readout'],
               'numeric_full_SA_probabilities':None}]
        r['calculation']={'tested':len(trials),'trials':trials,'verdict':verdict,
             'interpretation':'Scoped component diagnostics; shared evidence, not independent devices or natural probabilities.'}
        r['numerical_error_budget']={
            'precision_dps':[50,80],
            'scattering_precision_comparison':'All coefficient differences <1e-40; observed maximum 1.44685e-43.',
            'independent_solver':'Double-precision canonical midpoint, Richardson order6; tolerances 3e-8 agreement and 2e-8 step convergence.',
            'scattering_tail':'Analytic bound on s>=50 tail only; ODE errors are not interval-certified.',
            'flat_noise':'Positive spectral tail bound <2.048e-16; alternate logarithmic time-domain integral.',
            'geometry_and_approximation':'No global SA state, CTC propagator, full RSET or backreaction error bound supplied.'}
        r['verification'].update(computational='cross_checked',independent_task={
           'method':'Separate canonical midpoint / independent matrix / static-basis checks',
           'program':VERIFIER,'proof_sha256':digest(evidence/'verification.json'),
           'same_author':True,'external_peer_review':'not_performed'})
        rows.append(r)
    paths=[CONFIG,cfg['protocol_file'],'architecture/requirements.lock','scripts/architecture_search.py',
           JUNCTION,SCATTERING,VERIFIER,'scripts/sa_quantum_report_v4.py',
           'notes/sa-quantum-record-v4.md','.github/workflows/sa-quantum-record-v4.yml']
    b={'schema_version':1,'batch_id':cfg['batch_id'],
       'counts':{status:sum(r['status']==status for r in rows) for status in ['A','B','C']},
       'coverage':{'not_assessed_now':[
          {'class':'Global SA state and physical response','reason':'Singular-endpoint completion, incoming data, mode mixing and global consistency remain.'},
          {'class':'Full horizon-crossing and past receiver experiment','reason':'Actual m_h,V_h and both receiver distributions are uncomputed.'},
          {'class':'Apparatus/semiclassical completion','reason':'No full RSET, state preparation device or coupled backreacted evolution.'}]},
       'provenance':{'source_base_sha':cfg['source_base_sha'],'checkout_sha':protocol.git_sha(root),
          'execution':'GitHub Actions' if os.getenv('GITHUB_ACTIONS')=='true' else 'local',
          'github_run_id':os.getenv('GITHUB_RUN_ID'),'python':platform.python_version(),
          'sympy':sympy.__version__,'mpmath':mpmath.__version__,
          'file_sha256':{p:digest(root/p) for p in paths},
          'evidence_sha256':{p:digest(evidence/p) for p in ['junction.json','scattering.json','verification.json']}},
       'verification':v,'candidates':rows}
    validate_current(b,root)
    return b


def render(b:dict)->str:
    validate_current(b)
    p=b['provenance']
    out=['# 二荷電殻の量子場と有限受信記録 — 検証済みv4報告','',
         '**A=0 / B=1 / C=2。全SA時空の過去向き受信分布は未取得です。**','',
         'Bは全構成の継続、Cは単一平衡状態と符号に鈍感な受信方式の限定的障害です。',
         '内側静的領域の反射は、全地平面通過の透過率でも過去通信確率でもありません。','',
         f"実行: {p['execution']} / Python {p['python']} / SymPy {p['sympy']} / mpmath {p['mpmath']}",
         f"基点: `{p['source_base_sha']}` / checkout: `{p['checkout_sha']}`",'',
         '| 候補 | 分類 | 実際の過去分布 |','|---|---|---|']
    for r in b['candidates']:out.append(f"| {r['candidate_id']} | {r['status']} | 未計算・null |")
    v=b['verification']
    out+=['','## 別実装との照合','```json',json.dumps(v,ensure_ascii=False,indent=2),'```',
          '', '3周波数×2境界条件、8 Gaussian受信対照、1つの有限窓4D真空雑音対照。',
          '証明の共有・再利用があり、候補の計算件数を独立した装置数に合算しません。',
          '別プログラムも同じAIが作成。独立研究者の査読、全SAの物理的完成を意味しません。']
    for r in b['candidates']:
        out+=['',f"## {r['candidate_id']} — {r['status']}",r['title'],'',r['scope'],'',
              '### 七段階','| Stage | 作業 | 状態 |','|---|---|---|']
        for k,s in r['stages'].items():out.append(f"|{k}|{s['name']}|{s['state']}|")
        for key in protocol.REQUIRED:
            if key in ['candidate_id','status','scope','literature']:continue
            out+=['',f'### {key}','```json',json.dumps(r[key],ensure_ascii=False,indent=2),'```']
        for key in ['assumption_changes','calculation','numerical_error_budget','calculated_components']:
            if key in r:out+=['',f'### {key}','```json',json.dumps(r[key],ensure_ascii=False,indent=2),'```']
        out+=['','### 一次文献']
        for s in r['literature']:out.append(f"- {s['authors']} ({s['year']}), [{s['title']}]({s['url']})。{s['used_for']}")
    out+=['','## 入力・コードの出所','```json',json.dumps(p,ensure_ascii=False,indent=2),'```','']
    return '\n'.join(out)


class ReportControls(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.evidence=Path(os.environ['SA_V4_EVIDENCE'])
        cls.b=build(ROOT,cls.evidence)
    def test_actual_probabilities_remain_unknown(self):
        for r in self.b['candidates']:self.assertIsNone(r['P_Y_do_0']['distribution'])
    def test_all_protocol_fields_present(self):
        validate_current(self.b,ROOT)
    def test_stale_counts_rejected(self):
        b=copy.deepcopy(self.b);b['counts']['A']=1
        with self.assertRaises(protocol.RecordError):validate_current(b)
    def test_false_A_rejected(self):
        b=copy.deepcopy(self.b);b['candidates'][0]['status']='A'
        with self.assertRaises(protocol.RecordError):validate_current(b)
    def test_original_human_gate_retained(self):
        b=copy.deepcopy(self.b);b['candidates'][0]['status']='A'
        with self.assertRaises(protocol.RecordError):protocol.require_human_review_for_a(b)
    def test_unknown_is_not_zero(self):
        b=copy.deepcopy(self.b);b['candidates'][0]['distinguishability']['value']='0'
        with self.assertRaises(protocol.RecordError):validate_current(b)
    def test_control_noise_not_promoted(self):
        j=protocol.load_json(self.evidence/'junction.json');s=protocol.load_json(self.evidence/'scattering.json');v=protocol.load_json(self.evidence/'verification.json')
        j['actual_SA_V_h']='0.08317814'
        with self.assertRaises(protocol.RecordError):check_scope(j,s,v)
    def test_incomplete_verification_rejected(self):
        j=protocol.load_json(self.evidence/'junction.json');s=protocol.load_json(self.evidence/'scattering.json');v=protocol.load_json(self.evidence/'verification.json')
        v['scattering_cross_checks']=[]
        with self.assertRaises(protocol.RecordError):check_scope(j,s,v)
    def test_hash_mutation_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)
            for n in ['junction.json','scattering.json','verification.json']:(p/n).write_bytes((self.evidence/n).read_bytes())
            (p/'junction.json').write_text((p/'junction.json').read_text()+' ')
            with self.assertRaises(protocol.RecordError):read_evidence(ROOT,p)
    def test_missing_evidence_is_not_C(self):
        with tempfile.TemporaryDirectory() as td:
            with self.assertRaises(FileNotFoundError):read_evidence(ROOT,Path(td))
    def test_no_false_external_review(self):
        j=protocol.load_json(self.evidence/'junction.json');s=protocol.load_json(self.evidence/'scattering.json');v=protocol.load_json(self.evidence/'verification.json')
        v['external_peer_review']='passed'
        with self.assertRaises(protocol.RecordError):check_scope(j,s,v)
    def test_report_is_deterministic(self):
        self.assertEqual(render(self.b),render(copy.deepcopy(self.b)))


def main()->None:
    ap=argparse.ArgumentParser();ap.add_argument('--evidence',type=Path,required=True)
    ap.add_argument('--output',type=Path);ap.add_argument('--gate',action='store_true');ap.add_argument('--tests',action='store_true')
    args=ap.parse_args()
    if args.tests:
        os.environ['SA_V4_EVIDENCE']=str(args.evidence.resolve())
        result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(ReportControls))
        if not result.wasSuccessful():raise SystemExit(1)
        return
    if args.output is None:ap.error('--output is required unless --tests')
    b=build(ROOT,args.evidence)
    args.output.mkdir(parents=True,exist_ok=True)
    protocol.write_json(args.output/'candidates.json',b)
    (args.output/'report.md').write_text(render(b),encoding='utf-8')
    if args.gate:protocol.require_human_review_for_a(b)
    print(json.dumps({'counts':b['counts'],'execution':b['provenance']['execution'],
         'past_receiver_probabilities':'uncomputed','external_peer_review':'not_performed'},ensure_ascii=False))

if __name__=='__main__':main()
