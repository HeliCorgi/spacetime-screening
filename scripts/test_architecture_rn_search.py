"""Regression and false-positive controls for the A-directed RN extension."""
from __future__ import annotations
import copy
from fractions import Fraction as F
import tempfile
import unittest
from pathlib import Path
from architecture_search import RecordError,load_json,require_human_review_for_a,validate_record
from architecture_rn_models import Interval,certify_box,geometry_checks,hessian,rational_sweep,seam_diagnostic,numeric_diagnostics
from architecture_rn_verify import verify_sweep,bernstein_box
from architecture_rn_search import ROOT,generate,finalize


class RNSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows,cls.counts,cls.witness=rational_sweep()
        cls.box=certify_box()
        cls.tmp=tempfile.TemporaryDirectory()
        cls.bundle=generate(Path(cls.tmp.name)/'raw')
    @classmethod
    def tearDownClass(cls): cls.tmp.cleanup()
    def test_4d_tensor_and_junction(self): self.assertIn('bulk',geometry_checks())
    def test_exact_subextremal_witness(self):
        self.assertEqual(hessian(F(9,10),F(8099,10000),F(3,4)),F(10097,495000))
    def test_extremal_stability_threshold(self):
        self.assertEqual(hessian(F(3,4),F(9,16),F(1)),0)
        self.assertGreater(hessian(F(4,5),F(16,25),F(1)),0)
    def test_extremal_eta_half_not_stable(self):
        for i in range(1,100):
            m=F(i,100);self.assertLess(hessian(m,m*m,F(1,2)),0)
    def test_charge_free_controls(self):
        for m in [F(1,10),F(1,4),F(2,5),F(49,100)]:
            for e in [F(0),F(1,2),F(1)]:self.assertLess(hessian(m,F(0),e),0)
    def test_sweep_counts_and_invalids(self):
        self.assertEqual(self.counts,{'tested':1890,'outside':1620,'stable':179,'invalid_exterior':270})
    def test_independent_sweep_formula(self):self.assertEqual(verify_sweep(self.rows)['stable'],179)
    def test_mutated_stability_caught(self):
        rows=copy.deepcopy(self.rows);r=next(x for x in rows if x['radially_stable']);r['a2_Vpp']=str(-F(r['a2_Vpp']))
        with self.assertRaises(AssertionError):verify_sweep(rows)
    def test_invalid_geometry_not_a_pass(self):
        for r in self.rows:
            if not r['outside_outer_horizon']:self.assertIsNone(r['radially_stable'])
    def test_exact_box_independent_bernstein(self):self.assertGreater(F(bernstein_box(self.box)['a2_Vpp_lower']),0)
    def test_interval_zero_division_rejected(self):
        with self.assertRaises(AssertionError):Interval(1)/Interval(-1,1)
    def test_interval_square_crossing_zero(self):self.assertEqual((Interval(-2,1)**2).strings(),['0','4'])
    def test_single_seam_roundtrip(self):
        result=seam_diagnostic();self.assertEqual(result['tested'],15)
        self.assertTrue(all(F(r['same_clock_roundtrip'])>0 for r in result['trials']))
    def test_negative_coordinate_leg_not_signal(self):
        rows=seam_diagnostic()['trials'];self.assertTrue(any(F(r['forward_leg_coordinate_delta'])<0 for r in rows))
        self.assertTrue(all(F(r['same_clock_roundtrip'])>0 for r in rows))
    def test_reduced_proper_energy_not_reduced_anec(self):
        rows=numeric_diagnostics(50);self.assertTrue(all(r['radial_ANEC_2piGa']=='-1' for r in rows))
        self.assertGreater(float(rows[-1]['optical_time_over_a']),float(rows[0]['optical_time_over_a']))
    def test_probabilities_stay_unknown(self):
        for r in self.bundle['candidates']:
            self.assertFalse(r['P_Y_do_0']['computed']);self.assertIsNone(r['distinguishability']['value'])
    def test_no_false_A_from_stability(self):
        r=copy.deepcopy(self.bundle['candidates'][0]);r['status']='A'
        with self.assertRaises(RecordError):validate_record(r)
    def test_A_clearance_always_blocks(self):
        with self.assertRaises(RecordError):require_human_review_for_a({'candidates':[{'status':'A'}]})
    def test_missing_probability_reason(self):
        r=copy.deepcopy(self.bundle['candidates'][0]);r['P_Y_do_0']['reason']=''
        with self.assertRaises(RecordError):validate_record(r)
    def test_no_physical_success_flags(self):
        for r in self.bundle['candidates']:
            self.assertFalse(r['support_accounting']['complete']);self.assertFalse(r['stress_energy']['renormalized'])
    def test_stale_verification_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            p=Path(tmp)/'verification.json';p.write_text('{"input_sha256":"wrong"}')
            with self.assertRaises(RecordError):finalize(Path(self.tmp.name)/'raw/candidates.json',p,Path(tmp)/'final',True)
    def test_original_protocol_unchanged(self):
        from architecture_search import sha256
        cfg=load_json(ROOT/'architecture/rn-a-target-v2.json')
        self.assertEqual(sha256(ROOT/cfg['protocol_file']),cfg['protocol_sha256'])


if __name__=='__main__':unittest.main(verbosity=2)
