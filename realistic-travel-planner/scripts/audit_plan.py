"""Audit supplied schedule/budget facts; no network calls or booking actions."""
import argparse
from datetime import date
from decimal import Decimal, InvalidOperation
import json
from pathlib import Path
import re
import sys

KINDS = {'core', 'optional', 'transport', 'meal', 'rest', 'logistics', 'queue', 'buffer'}
STATUSES = {'verified', 'estimated', 'unknown'}

def number(value, name, positive=False):
    if isinstance(value, bool) or not isinstance(value, (int, float, Decimal)):
        raise ValueError(name + ' must be a finite number')
    result = Decimal(str(value))
    if not result.is_finite() or result < 0 or (positive and result == 0):
        raise ValueError(name + ' must be finite and ' + ('positive' if positive else 'nonnegative'))
    return result

def minute(value):
    if not isinstance(value, str) or not re.fullmatch(r'(?:[01]\d|2[0-3]):[0-5]\d', value):
        raise ValueError('Times must be HH:MM within one local calendar day')
    hour, mins = map(int, value.split(':'))
    return hour * 60 + mins

def require_list(value, name):
    if not isinstance(value, list):
        raise ValueError(name + ' must be a list')
    return value

def flag(value, name):
    if not isinstance(value, bool):
        raise ValueError(name + ' must be boolean')
    return value

def text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(name + ' must be a nonempty string')
    return value

def _audit(plan, constraints):
    errors = []
    def fail(code, message):
        errors.append({'code': code, 'message': message})

    currency = text(plan['currency'], 'currency')
    party = plan['travelers']
    if isinstance(party, bool) or not isinstance(party, int) or party < 1:
        raise ValueError('travelers must be a positive integer')
    cap = number(plan['budget_cap'], 'budget_cap')
    reserve = number(plan['reserve'], 'reserve')
    declared = number(plan['declared_base_total'], 'declared_base_total')
    required_categories = set(text(x, 'category') for x in require_list(plan['required_categories'], 'required_categories'))
    for name, actual in [('currency', currency), ('travelers', party), ('budget_cap', cap)]:
        if name in constraints and actual != constraints[name]:
            fail('CONSTRAINT_MISMATCH', name + ' differs from the independent constraints')
    if reserve < number(constraints.get('minimum_reserve', 0), 'minimum_reserve'):
        fail('RESERVE_TOO_SMALL', 'Reserve is below the requested minimum')
    required_categories.update(require_list(constraints.get('required_categories', []), 'constraint categories'))

    items = {}
    days_seen = set()
    days = require_list(plan['days'], 'days')
    if not days:
        raise ValueError('days must contain at least one local date')
    for day in days:
        day_date = date.fromisoformat(day['date']).isoformat()
        if day_date in days_seen:
            fail('DUPLICATE_DAY', day_date)
        days_seen.add(day_date)
        limits = constraints.get('days', {}).get(day_date, {})
        earliest = minute(limits.get('earliest_start', day['earliest_start']))
        latest = minute(limits.get('latest_end', day['latest_end']))
        if latest <= earliest:
            raise ValueError('Day limits must be ordered within one local date')
        active = []
        for item in require_list(day['items'], 'items'):
            iid = text(item['id'], 'item.id')
            if iid in items:
                fail('DUPLICATE_ID', iid)
            items[iid] = item
            kind = item['kind']
            if kind not in KINDS or item['status'] not in STATUSES:
                raise ValueError('Invalid item kind or evidence status: ' + iid)
            included = flag(item.get('included', True), 'item.included')
            require_list(item['cost_refs'], 'cost_refs')
            if not included:
                if kind != 'optional':
                    fail('EXCLUDED_REQUIRED_ITEM', iid + ' is excluded but not optional')
                continue
            start, end = minute(item['start']), minute(item['end'])
            if end <= start:
                fail('NONPOSITIVE_DURATION', iid)
            if start < earliest or end > latest:
                fail('DAY_BOUNDARY', iid + ' violates departure/return limits')
            fact = constraints.get('activities', {}).get(iid, {})
            minimum = max(number(item.get('min_minutes', 0), 'min_minutes'), number(fact.get('min_minutes', 0), 'constraint min_minutes'))
            if end - start < minimum:
                fail('DURATION_TOO_SHORT', iid + ' has less than its supplied minimum duration')
            window = fact.get('window', item.get('window'))
            if window:
                if start < minute(window['start']) or end > minute(window['end']):
                    fail('OPERATING_WINDOW', iid + ' falls outside the operating window')
                if 'last_entry' in window and start > minute(window['last_entry']):
                    fail('LAST_ENTRY', iid + ' begins after last entry')
            if kind == 'transport' and item.get('door_to_door') is not True:
                fail('TRANSPORT_SCOPE', iid + ' is not explicitly door-to-door')
            if kind == 'core' and item['status'] == 'unknown':
                if item.get('tentative') is not True or not item.get('fallback'):
                    fail('UNKNOWN_CORE', iid + ' needs a tentative label and fallback')
            active.append((start, end, iid))
        active.sort()
        previous_end = -1
        previous_id = ''
        for start, end, iid in active:
            if start < previous_end:
                fail('OVERLAP', previous_id + ' overlaps ' + iid)
            if end > previous_end:
                previous_end, previous_id = end, iid

    for iid in require_list(constraints.get('required_item_ids', []), 'required_item_ids'):
        if iid not in items or items[iid].get('included', True) is not True:
            fail('MISSING_REQUIRED_ITEM', iid)

    costs = {}
    categories = set()
    base, optional = Decimal(0), Decimal(0)
    for entry in require_list(plan['costs'], 'costs'):
        cid = text(entry['id'], 'cost.id')
        if cid in costs:
            fail('DUPLICATE_COST', cid)
        costs[cid] = entry
        if entry['currency'] != currency:
            fail('CURRENCY_MISMATCH', cid)
        amount = number(entry['unit_amount'], 'unit_amount') * number(entry['quantity'], 'quantity', positive=True)
        category = text(entry['category'], 'cost.category')
        if entry['status'] not in STATUSES:
            raise ValueError('Invalid cost status: ' + cid)
        if entry['status'] == 'unknown' and not entry.get('allowance_reason'):
            fail('UNKNOWN_COST', cid + ' needs an explicit planning allowance reason')
        if flag(entry['included'], 'cost.included'):
            base += amount
            categories.add(category)
        else:
            optional += amount
    for iid, item in items.items():
        for cid in item['cost_refs']:
            if cid not in costs:
                fail('MISSING_COST_REFERENCE', iid + ' references ' + str(cid))
            elif item.get('included', True) and not costs[cid]['included']:
                fail('EXCLUDED_ACTIVE_COST', iid + ' depends on an excluded cost')
    for category in sorted(required_categories - categories):
        fail('MISSING_COST_CATEGORY', category)
    if base != declared:
        fail('TOTAL_MISMATCH', 'Declared total ' + str(declared) + ' differs from ledger ' + str(base))
    if base + reserve > cap:
        fail('BUDGET_EXCEEDED', 'Base spending plus reserve exceeds the cap')
    return {'ok': not errors, 'errors': errors, 'totals': {'currency': currency, 'base': str(base), 'reserve': str(reserve), 'base_plus_reserve': str(base + reserve), 'cap': str(cap), 'headroom': str(cap - base - reserve), 'excluded_addons': str(optional)}, 'limits': 'Checks supplied data only; does not verify live facts, completeness of routes/costs, fatigue, or source truth.'}

def audit(plan, constraints=None):
    try:
        return _audit(plan, constraints or {})
    except (KeyError, TypeError, ValueError, InvalidOperation, AttributeError) as exc:
        return {'ok': False, 'errors': [{'code': 'INVALID_INPUT', 'message': str(exc)}]}

def load_json(path):
    def reject_constant(value):
        raise ValueError('Nonfinite JSON number: ' + value)
    def unique_keys(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('Duplicate JSON key: ' + key)
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding='utf-8-sig'), parse_float=Decimal, parse_constant=reject_constant, object_pairs_hook=unique_keys)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('plan')
    parser.add_argument('--constraints')
    args = parser.parse_args()
    try:
        result = audit(load_json(args.plan), load_json(args.constraints) if args.constraints else None)
    except (OSError, ValueError) as exc:
        result = {'ok': False, 'errors': [{'code': 'INVALID_INPUT', 'message': str(exc)}]}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result['ok'] else 1

if __name__ == '__main__':
    sys.exit(main())
