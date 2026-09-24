"""Regression, independent arithmetic, and fail-closed controls for v3."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import mpmath as mp
import architecture_charged_models as model
import architecture_charged_search as search
import architecture_charged_verify as verifier


class ChargedCompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp=tempfile.TemporaryDirectory()
        cls.root=Path(cls.temp.name)
        cls.bundle=search.run(cls.root/'raw')
        cls.records=cls.root/'raw/candidates.json'
        cls.proofpath=cls.root/'verification.json'
        cls.proof=verifier.verify(cls.records,cls.proofpath)

    @classmethod
    def tearDownClass(cls):
        cls.temp.cleanup()

    def test_counts_not_success_probability(self):
        self.assertEqual(self.bundle['counts'],{'A':0,'B':1,'C':1})
        self.assertEqual([r['calculation']['tested'] for r in self.bundle['candidates']],[18,19])

    def test_protocol_unchanged(self):
        self.assertEqual(search.protocol.sha256(search.ROOT/'docs/4d-past-signalling-protocol.txt'),
            '3b024b673c099d1886112372fe9b0b6095505380c6c202d93c5ea8b9389159dd')

    def test_unknown_distributions_are_not_zero(self):
        for r in self.bundle['candidates']:
            self.assertIsNone(r['distinguishability']['value'])
            self.assertFalse(r['P_Y_do_0']['computed'])
            self.assertIsNone(r['P_Y_do_1']['distribution'])

    def test_no_false_A_from_path(self):
        b=copy.deepcopy(self.bundle);b['candidates'][1]['status']='A'
        b['counts']={'A':1,'B':0,'C':1}
        with self.assertRaises(search.protocol.RecordError):search.validate(b)

    def test_full_dimension_required(self):
        b=copy.deepcopy(self.bundle);b['candidates'][0]['dimension']=2
        with self.assertRaises(search.protocol.RecordError):search.validate(b)

    def test_source_metadata_required(self):
        b=copy.deepcopy(self.bundle);del b['candidates'][0]['literature']
        with self.assertRaises(search.protocol.RecordError):search.validate(b)

    def test_unknown_probability_reason_required(self):
        b=copy.deepcopy(self.bundle);b['candidates'][1]['P_Y_do_0']['reason']=''
        with self.assertRaises(search.protocol.RecordError):search.validate(b)

    def test_missing_point_is_not_success(self):
        b=copy.deepcopy(self.bundle);b['candidates'][0]['calculation']['trials'].pop()
        with self.assertRaises(search.protocol.RecordError):search.validate(b)

    def test_precision_not_weakened(self):
        with self.assertRaises(search.protocol.RecordError):search.protocol.compare_precision('1','1.00000000001')

    def test_exact_tail_and_lapse_relaxation(self):
        e=self.bundle['exact_checks']
        self.assertEqual(e['RN_r4_R'],'-2*epsilon^2')
        self.assertTrue(e['log_lapse_tail_cancels_r4_trace'])

    def test_full_4d_separate_verification(self):
        self.assertEqual(self.proof['checks']['MP_bulk_Einstein_Maxwell'],'direct 4D tensor identity')
        self.assertEqual(self.proof['checks']['RN_Kretschmann'],'direct Riemann contraction')
        self.assertEqual(self.proof['checks']['minimal_KG'],'full 4D separated operator')
        self.assertFalse(self.proof['checks']['independent_researcher_review'])
        self.assertEqual(sum(c['checked'] for c in self.proof['candidates']),37)

    def test_mutated_stress_caught(self):
        row=copy.deepcopy(self.bundle['candidates'][0]['calculation']['trials'][0])
        row['eight_pi_G_pt_extra']='123'
        with self.assertRaises(ValueError):verifier.verify_trial(row)

    def test_mutated_anomaly_caught(self):
        row=copy.deepcopy(self.bundle['candidates'][0]['calculation']['trials'][0])
        row['scalar_anomaly_beta0']='123'
        with self.assertRaises(ValueError):verifier.verify_trial(row)

    def test_mutated_surface_charge_caught(self):
        row=copy.deepcopy(self.bundle['candidates'][1]['calculation']['trials'][0])
        row['charge_G1']='-1'
        with self.assertRaises(ValueError):verifier.verify_trial(row)

    def test_mutated_return_time_caught(self):
        row=copy.deepcopy(self.bundle['candidates'][1]['calculation']['trials'][-1])
        row['proper_margin']='10'
        with self.assertRaises(ValueError):verifier.verify_trial(row)

    def test_nonfinite_not_agreement(self):
        for value in ('nan','inf','-inf'):
            with self.assertRaises(ValueError):verifier.close(value,'1')

    def test_invalid_geometry_rejected(self):
        for args in ((1,1,2),(1,-1,10),(-1,1,10)):
            with self.assertRaises(ValueError):model.optical_time(*map(mp.mpf,args))
        with self.assertRaises(ValueError):model.mp_boundary(mp.mpf(1),mp.mpf(1),mp.mpf(10),mp.mpf(2))

    def test_zero_time_shift_is_forward_control(self):
        with mp.workdps(50):
            T=model.optical_time(mp.mpf(1),mp.mpf('.1'),mp.mpf(10))
            self.assertGreater(T,0)
            self.assertLess(T,60)

    def test_positive_minimal_test_field_potential(self):
        for row in self.bundle['candidates'][0]['calculation']['trials']:
            if row['kind']=='RN_point':self.assertGreater(mp.mpf(row['minimal_scalar_l0_potential']),0)

    def test_normalized_ANEC_negative(self):
        for row in self.bundle['candidates'][0]['calculation']['trials']:
            if row['kind']=='RN_ANEC':self.assertLess(mp.mpf(row['ANEC_G1']),0)

    def test_final_report_reproducible(self):
        out=self.root/'verified'
        b=search.finalize(self.records,self.proofpath,out,gate=True)
        self.assertEqual((out/'report.md').read_text(),search.report(b))
        self.assertEqual(b['counts'],{'A':0,'B':1,'C':1})

    def test_stale_proof_rejected(self):
        p=copy.deepcopy(self.proof);p['records_sha256']='0'*64
        path=self.root/'stale.json';search.write(path,p)
        with self.assertRaises(search.protocol.RecordError):search.finalize(self.records,path,self.root/'bad')

    def test_missing_verification_rejected(self):
        p=copy.deepcopy(self.proof);p['candidates'].pop()
        path=self.root/'missing.json';search.write(path,p)
        with self.assertRaises(search.protocol.RecordError):search.finalize(self.records,path,self.root/'bad')

    def test_input_hash_mismatch_rejected(self):
        b=copy.deepcopy(self.bundle);b['provenance']['file_sha256'][search.CONFIG]='0'*64
        with self.assertRaises(search.protocol.RecordError):search.validate(b)

    def test_human_gate_even_after_validation(self):
        # Isolate the last safeguard; validation is bypassed ONLY by this test mock.
        b=copy.deepcopy(self.bundle);b['counts']={'A':1,'B':0,'C':1}
        raw=self.root/'test-A.json';search.write(raw,b)
        p=copy.deepcopy(self.proof);p['records_sha256']=search.protocol.sha256(raw)
        proof=self.root/'test-A-proof.json';search.write(proof,p)
        with patch.object(search,'validate',return_value=None):
            with self.assertRaises(search.protocol.RecordError):
                search.finalize(raw,proof,self.root/'test-A-output',gate=True)
        self.assertTrue((self.root/'test-A-output/report.md').exists())


if __name__=='__main__':unittest.main(verbosity=2)
