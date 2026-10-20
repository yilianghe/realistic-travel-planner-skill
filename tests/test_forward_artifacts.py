"""Regression checks on actual agent-generated plans, not hand-written happy paths."""
import copy
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('auditor', ROOT/'realistic-travel-planner/scripts/audit_plan.py')
auditor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(auditor)

class ForwardArtifactTests(unittest.TestCase):
    def setUp(self):
        folder = ROOT / 'evaluation/results'
        self.plan = auditor.load_json(folder/'new-skill-B.json')
        self.constraints = auditor.load_json(folder/'new-skill-B-constraints.json')

    def codes(self):
        return {e['code'] for e in auditor.audit(self.plan,self.constraints)['errors']}

    def test_original_agent_B_and_C_pass(self):
        folder = ROOT/'evaluation/results'
        for case in ('B','C'):
            with self.subTest(case=case):
                result = auditor.audit(auditor.load_json(folder/f'new-skill-{case}.json'),auditor.load_json(folder/f'new-skill-{case}-constraints.json'))
                self.assertTrue(result['ok'],result)

    def test_shortened_real_transfer_detected(self):
        move = next(x for x in self.plan['days'][0]['items'] if x['id']=='hotel_museum')
        move['end'] = '12:00'
        move['min_minutes'] = 30
        self.assertIn('DURATION_TOO_SHORT',self.codes())

    def test_omitted_prepaid_hotel_detected(self):
        self.plan['costs'] = [c for c in self.plan['costs'] if c['id']!='hotel']
        self.plan['declared_base_total'] = 389
        self.assertIn('MISSING_COST_CATEGORY',self.codes())

    def test_spending_into_reserve_detected(self):
        next(c for c in self.plan['costs'] if c['id']=='lunch_cost')['unit_amount'] = 230
        self.plan['declared_base_total'] = 839
        self.assertIn('BUDGET_EXCEEDED',self.codes())

    def test_unknown_booking_without_condition_detected(self):
        museum = next(x for x in self.plan['days'][0]['items'] if x['id']=='museum')
        museum['tentative'] = False
        museum.pop('fallback')
        self.assertIn('UNKNOWN_CORE',self.codes())

    def test_overlap_in_generated_day_detected(self):
        dinner = next(x for x in self.plan['days'][0]['items'] if x['id']=='dinner')
        dinner['start'] = '16:30'
        self.assertIn('OVERLAP',self.codes())

if __name__ == '__main__':
    unittest.main()
