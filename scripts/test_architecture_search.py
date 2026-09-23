"""Fail-closed tests, including deliberate false successes and mutated calculations."""
from __future__ import annotations
import contextlib
import copy
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from architecture_search import (ROOT, REQUIRED, RecordError, compare_precision, collect_verifications, finalize,
    load_json, require_human_review_for_a, run_batch, validate_bundle, validate_record, write_json)
from architecture_verify import verify, verify_shell, verify_rotating
import mpmath as mp


class ProtocolTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp=tempfile.TemporaryDirectory()
        cls.output=Path(cls.tmp.name)/'raw'
        with contextlib.redirect_stdout(io.StringIO()):
            cls.bundle=run_batch(ROOT,cls.output)
    @classmethod
    def tearDownClass(cls):cls.tmp.cleanup()
    def record(self,cid='flat-local-source'):
        return copy.deepcopy(next(r for r in self.bundle['candidates'] if r['candidate_id']==cid))
    def rejects(self,row):
        with self.assertRaises(RecordError):validate_record(row)
    def test_required_fields_each_rejected_when_missing(self):
        for field in REQUIRED:
            with self.subTest(field=field):
                row=self.record();del row[field];self.rejects(row)
    def test_initial_counts_are_not_probabilities(self):
        self.assertEqual(self.bundle['counts'],{'A':0,'B':3,'C':4})
        self.assertEqual(sum(r['calculation']['tested'] for r in self.bundle['candidates']),2282)
    def test_exactly_one_primary_status(self):
        for status in ['PASS','B/C',None,[],True]:
            row=self.record();row['status']=status;self.rejects(row)
    def test_dimension_two_rejected(self):
        row=self.record();row['dimension']=2;self.rejects(row)
    def test_dimension_string_rejected(self):
        row=self.record();row['dimension']='4';self.rejects(row)
    def test_dimension_boolean_rejected(self):
        row=self.record();row['dimension']=True;self.rejects(row)
    def test_wrong_dimension_split_rejected(self):
        row=self.record();row['dimension_split']={'space':1,'time':3};self.rejects(row)
    def test_unknown_probability_is_not_zero(self):
        row=self.record('fkz-mass-controlled-ring');row['P_Y_do_0']['distribution']=0;self.rejects(row)
    def test_unknown_reason_required(self):
        row=self.record('fkz-mass-controlled-ring');row['P_Y_do_0']['reason']='';self.rejects(row)
    def test_unknown_D_is_not_zero(self):
        row=self.record('fkz-mass-controlled-ring');row['distinguishability']['value']='0';self.rejects(row)
    def test_invalid_probability_flag(self):
        row=self.record();row['P_Y_do_0']['computed']='true';self.rejects(row)
    def test_negative_variance_rejected(self):
        row=self.record();row['P_Y_do_0']['distribution']['variance']='-1';self.rejects(row)
    def test_nan_rejected(self):
        row=self.record();row['distinguishability']['value']='NaN';self.rejects(row)
    def test_duplicate_json_keys_rejected(self):
        path=Path(self.tmp.name)/'duplicates.json';path.write_text('{"a":1,"a":2}')
        with self.assertRaises(RecordError):load_json(path)
    def test_json_infinity_rejected(self):
        path=Path(self.tmp.name)/'infinity.json';path.write_text('{"a":Infinity}')
        with self.assertRaises(RecordError):load_json(path)
    def test_identical_laws_cannot_have_positive_D(self):
        row=self.record();row['distinguishability']['value']='0.3';self.rejects(row)
    def test_C_needs_obstruction(self):
        row=self.record();row['obstructions']=[];self.rejects(row)
    def test_B_needs_unresolved_assumption(self):
        row=self.record('fkz-mass-controlled-ring');row['unresolved_assumptions']=[];self.rejects(row)
    def test_A_cannot_be_geometry_only(self):
        row=self.record('schwarzschild-eos-4');row['status']='A';self.rejects(row)
    def test_A_cannot_be_classical_path_only(self):
        row=self.record('fkz-mass-controlled-ring');row['status']='A';self.rejects(row)
    def test_A_cannot_be_local_forward_control(self):
        row=self.record();row['status']='A';row['distinguishability']['receiver_precedes_sender']=False;self.rejects(row)
    def test_human_gate_blocks_all_A(self):
        with self.assertRaises(RecordError):require_human_review_for_a({'candidates':[{'status':'A'}]})
        require_human_review_for_a(self.bundle)
    def test_no_disabling_human_review(self):
        row=self.record();row['verification']['human_review_for_A']=False;self.rejects(row)
    def test_all_seven_stages_required(self):
        row=self.record();del row['stages']['5'];self.rejects(row)
    def test_not_run_not_passed(self):
        row=self.record();row['stages']['4']['state']='passed';self.rejects(row)
    def test_literature_provenance_required(self):
        row=self.record();del row['literature'][0]['used_for'];self.rejects(row)
    def test_support_accounting_required(self):
        row=self.record();del row['support_accounting']['complete'];self.rejects(row)
    def test_assumption_change_log_required(self):
        row=self.record();del row['assumption_changes'];self.rejects(row)
    def test_empty_batch_not_success(self):
        b=copy.deepcopy(self.bundle);b['candidates']=[]
        with self.assertRaises(RecordError):validate_bundle(b)
    def test_duplicate_ids_rejected(self):
        b=copy.deepcopy(self.bundle);b['candidates'].append(b['candidates'][0])
        with self.assertRaises(RecordError):validate_bundle(b)
    def test_stale_counts_rejected(self):
        b=copy.deepcopy(self.bundle);b['counts']['A']=1
        with self.assertRaises(RecordError):validate_bundle(b)
    def test_code_hash_mismatch_rejected(self):
        b=copy.deepcopy(self.bundle);b['provenance']['file_sha256']['scripts/architecture_models.py']='0'*64
        with self.assertRaises(RecordError):validate_bundle(b,ROOT)
    def test_path_traversal_rejected(self):
        b=copy.deepcopy(self.bundle);b['provenance']['file_sha256']['../../outside']='0'*64
        with self.assertRaises(RecordError):validate_bundle(b,ROOT)
    def test_precision_mismatch_rejected(self):
        with self.assertRaises(RecordError):compare_precision('1e-99','1.1e-99')
    def test_stale_verification_artifact_rejected(self):
        v=Path(self.tmp.name)/'stale.json';write_json(v,{'input_sha256':'0'*64})
        with self.assertRaises(RecordError):finalize(self.output/'candidates.json',v,Path(self.tmp.name)/'bad')
    def test_mutated_stability_sign_caught_independently(self):
        row=self.record('schwarzschild-eos-4')
        row['calculation']['trials'][0]['a0_squared_Vpp']='100'
        with mp.workdps(80),self.assertRaises(RecordError):verify_shell(row)
    def test_postselection_false_positive_control(self):
        # Independent fair b,y. Keeping only equality fakes a perfect message;
        # receiver's unconditioned y remains fair for each intervention.
        joint={(b,y):.25 for b in (0,1) for y in (0,1)}
        marg=[[joint[(b,y)]/.5 for y in (0,1)] for b in (0,1)]
        self.assertEqual(marg[0],marg[1])
        self.assertEqual(sum(joint[(b,y)] for b,y in joint if b==y),.5)
        row=self.record();del row['sender_intervention']['uses_postselection'];self.rejects(row)
    def test_cli_reports_failure_nonzero(self):
        b=copy.deepcopy(self.bundle);b['candidates'][0]['dimension']=2
        bad=Path(self.tmp.name)/'bad-records.json';write_json(bad,b)
        p=subprocess.run([sys.executable,str(ROOT/'scripts/architecture_search.py'),'validate','--records',str(bad)],capture_output=True,text=True)
        self.assertNotEqual(p.returncode,0);self.assertIn('FAILED',p.stderr)
    def test_no_unverified_report_clearance(self):
        v=Path(self.tmp.name)/'absent-verification.json';write_json(v,{'input_sha256':'wrong'})
        dest=Path(self.tmp.name)/'must-not-exist'
        with self.assertRaises(RecordError):finalize(self.output/'candidates.json',v,dest)
        self.assertFalse((dest/'report.md').exists())

    def test_rotating_ergosurface_exact_zero(self):
        row=self.record('rotating-global-time')
        self.assertTrue(any(v['g_tt_equator']=='0' for v in row['calculation']['trials']))
        for precision in (80,110):
            with mp.workdps(precision):verify_rotating(row)
    def test_separate_task_and_missing_collection_rejected(self):
        directory=Path(self.tmp.name)/'partial-tasks'
        with contextlib.redirect_stdout(io.StringIO()):
            result=verify(self.output/'candidates.json',directory/'flat.json',candidate_id='flat-local-source')
        self.assertEqual(set(result['candidates']),{'flat-local-source'})
        with self.assertRaises(RecordError):
            collect_verifications(self.output/'candidates.json',directory,Path(self.tmp.name)/'incomplete.json')
    def test_empty_verification_collection_rejected(self):
        with self.assertRaises(RecordError):
            collect_verifications(self.output/'candidates.json',Path(self.tmp.name)/'empty',Path(self.tmp.name)/'out.json')
    def test_unknown_verification_task_rejected(self):
        with self.assertRaises(RecordError):
            verify(self.output/'candidates.json',Path(self.tmp.name)/'unknown.json',candidate_id='invented')

    def test_source_boolean_required(self):
        row=self.record();row['stress_energy']['renormalized']='true';self.rejects(row)
    def test_complete_assumption_change_required(self):
        row=self.record('schwarzschild-eos-4');del row['assumption_changes'][0]['reason'];self.rejects(row)
    def test_stage_name_required(self):
        row=self.record();del row['stages']['1']['name'];self.rejects(row)
    def test_calculation_trial_count_required(self):
        row=self.record();row['calculation']['tested']+=1;self.rejects(row)
    def test_numerical_budget_required(self):
        row=self.record();del row['numerical_error_budget'];self.rejects(row)
    def test_obstruction_cannot_be_relabeled_escape(self):
        row=self.record();row['status']='B';self.rejects(row)

if __name__=='__main__':unittest.main(verbosity=2)
