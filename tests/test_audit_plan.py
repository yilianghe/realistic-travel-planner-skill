import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'realistic-travel-planner/scripts/audit_plan.py'
spec = importlib.util.spec_from_file_location('auditor', SCRIPT)
auditor = importlib.util.module_from_spec(spec)
spec.loader.exec_module(auditor)

class AuditTests(unittest.TestCase):
    def setUp(self):
        self.plan = auditor.load_json(ROOT / 'evaluation/audit-example.json')
        self.constraints = auditor.load_json(ROOT / 'evaluation/audit-constraints.json')

    def codes(self, plan=None, constraints=None):
        result = auditor.audit(self.plan if plan is None else plan, self.constraints if constraints is None else constraints)
        return {error['code'] for error in result['errors']}

    def test_valid_plan_and_party_totals(self):
        result = auditor.audit(self.plan, self.constraints)
        self.assertTrue(result['ok'], result)
        self.assertEqual(result['totals']['base_plus_reserve'], '110')
        self.assertEqual(result['totals']['headroom'], '40')

    def test_overlap(self):
        self.plan['days'][0]['items'][1]['start'] = '14:00'
        self.assertIn('OVERLAP', self.codes())

    def test_deadline_uses_independent_constraints(self):
        self.plan['days'][0]['latest_end'] = '17:00'
        self.plan['days'][0]['items'][-1]['end'] = '16:10'
        self.assertIn('DAY_BOUNDARY', self.codes())

    def test_cannot_shorten_independent_travel_minimum(self):
        item = self.plan['days'][0]['items'][3]
        item.update(end='15:20', min_minutes=30)
        self.assertIn('DURATION_TOO_SHORT', self.codes())

    def test_operating_window(self):
        self.constraints['activities']['luggage']['window'] = {'start':'14:30', 'end':'15:00'}
        self.assertIn('OPERATING_WINDOW', self.codes())

    def test_last_entry(self):
        self.constraints['activities']['luggage']['window'] = {'start':'13:00', 'end':'17:00', 'last_entry':'14:00'}
        self.assertIn('LAST_ENTRY', self.codes())

    def test_door_to_door_required(self):
        self.plan['days'][0]['items'][0]['door_to_door'] = False
        self.assertIn('TRANSPORT_SCOPE', self.codes())

    def test_missing_luggage(self):
        del self.plan['days'][0]['items'][1]
        self.assertIn('MISSING_REQUIRED_ITEM', self.codes())

    def test_missing_budget_category(self):
        self.constraints['required_categories'].append('hotel')
        self.assertIn('MISSING_COST_CATEGORY', self.codes())

    def test_wrong_arithmetic(self):
        self.plan['declared_base_total'] = 79
        self.assertIn('TOTAL_MISMATCH', self.codes())

    def test_reserve_is_not_free_spending(self):
        self.plan['costs'][0]['unit_amount'] = 80
        self.plan['declared_base_total'] = 130
        self.assertIn('BUDGET_EXCEEDED', self.codes())

    def test_insufficient_reserve(self):
        self.plan['reserve'] = 29
        self.assertIn('RESERVE_TOO_SMALL', self.codes())

    def test_budget_scope_tampering(self):
        for key, value in [('travelers',1),('currency','USD'),('budget_cap',999)]:
            plan = copy.deepcopy(self.plan)
            plan[key] = value
            self.assertIn('CONSTRAINT_MISMATCH', self.codes(plan))

    def test_party_quantity_is_multiplied(self):
        self.plan['costs'][0].update(unit_amount=30,quantity=2)
        self.plan['declared_base_total'] = 110
        self.assertEqual(self.codes(), set())

    def test_unverified_core_needs_fallback(self):
        item = self.plan['days'][0]['items'][2]
        item.update(kind='core', status='unknown')
        self.assertIn('UNKNOWN_CORE', self.codes())
        item.update(tentative=True, fallback='Skip and rest at the hotel')
        self.assertEqual(self.codes(), set())

    def test_unknown_cost_needs_allowance(self):
        self.plan['costs'][0]['status'] = 'unknown'
        self.assertIn('UNKNOWN_COST', self.codes())
        self.plan['costs'][0]['allowance_reason'] = 'Explicit estimate pending a quote'
        self.assertEqual(self.codes(), set())

    def test_active_cost_cannot_be_excluded(self):
        self.plan['costs'][0]['included'] = False
        self.assertIn('EXCLUDED_ACTIVE_COST', self.codes())

    def test_missing_cost_reference(self):
        self.plan['days'][0]['items'][0]['cost_refs'] = ['unlisted']
        self.assertIn('MISSING_COST_REFERENCE', self.codes())

    def test_optional_addon_does_not_pollute_base_schedule_or_budget(self):
        self.plan['days'][0]['items'].append({'id':'addon','kind':'optional','included':False,'status':'unknown','cost_refs':['addon-fee']})
        self.plan['costs'].append({'id':'addon-fee','category':'tickets','currency':'CNY','unit_amount':200,'quantity':2,'included':False,'status':'estimated'})
        result = auditor.audit(self.plan, self.constraints)
        self.assertTrue(result['ok'], result)
        self.assertEqual(result['totals']['excluded_addons'], '400')

    def test_duplicate_item_or_cost_ids(self):
        self.plan['days'][0]['items'].append(copy.deepcopy(self.plan['days'][0]['items'][0]))
        self.plan['costs'].append(copy.deepcopy(self.plan['costs'][0]))
        self.assertTrue({'DUPLICATE_ID','DUPLICATE_COST'}.issubset(self.codes()))

    def test_duplicate_day(self):
        self.plan['days'].append(copy.deepcopy(self.plan['days'][0]))
        self.assertIn('DUPLICATE_DAY', self.codes())

    def test_bad_or_overnight_times_rejected(self):
        for start, end in [('24:00','25:00'),('23:00','01:00'),('14:00','14:00')]:
            plan = copy.deepcopy(self.plan)
            plan['days'][0]['items'][0].update(start=start,end=end)
            self.assertFalse(auditor.audit(plan)['ok'])

    def test_invalid_amounts_and_flags_rejected(self):
        for value in [True,-1,float('nan'),float('inf'),'30']:
            plan = copy.deepcopy(self.plan)
            plan['costs'][0]['unit_amount'] = value
            self.assertIn('INVALID_INPUT', self.codes(plan))
        self.plan['costs'][0]['included'] = 'false'
        self.assertIn('INVALID_INPUT', self.codes())

    def test_empty_or_malformed_input(self):
        self.assertIn('INVALID_INPUT', self.codes({}))
        self.plan['days'] = []
        self.assertIn('INVALID_INPUT', self.codes())

    def test_strict_json_and_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'input.json'
            for content in ['{"x":1,"x":2}', '{"x":NaN}', '{bad json']:
                path.write_text(content, encoding='utf-8')
                process = subprocess.run([sys.executable,str(SCRIPT),str(path)], capture_output=True,text=True)
                self.assertEqual(process.returncode, 1)
                self.assertEqual(json.loads(process.stdout)['errors'][0]['code'], 'INVALID_INPUT')
        valid = subprocess.run([sys.executable,str(SCRIPT),str(ROOT/'evaluation/audit-example.json'),'--constraints',str(ROOT/'evaluation/audit-constraints.json')], capture_output=True,text=True)
        self.assertEqual(valid.returncode, 0, valid.stdout)

if __name__ == '__main__':
    unittest.main()
