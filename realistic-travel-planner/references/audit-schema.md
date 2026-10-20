# Itinerary audit contract

Python 3.10+; standard library only. Run locally:

```
python scripts/audit_plan.py plan.json --constraints constraints.json
```

Paths in this command are relative to the skill folder. Exit 0 means all supplied
checks passed; exit 1 means bad input or a failed check. Output is JSON with error
codes and budget totals. Use the repository's `evaluation/audit-example.json`
as a working example, not as a real itinerary.

## Plan

- `currency`: nonempty currency code; `travelers`: positive integer.
- `budget_cap`, `reserve`, `declared_base_total`: nonnegative numbers, for the
  **whole party and same scope**. Include prepaid amounts if inside the cap.
- `required_categories`: cost categories needed for this scope (including a
  zero-price line when a needed category is free).
- `days`: nonempty itinerary days, each `date` ISO YYYY-MM-DD, `earliest_start`,
  `latest_end` HH:MM in that day's local timezone, and `items`.
- Each item: unique `id`, `kind` (`core`, `optional`, `transport`, `meal`, `rest`,
  `logistics`, `queue`, `buffer`), `status` (`verified`, `estimated`, `unknown`),
  `cost_refs` array of cost ids, `start` and `end` HH:MM. Optional `min_minutes`
  is a known lower bound; optional `window` has `start`, `end`, and optional
  `last_entry`. Transport must declare `door_to_door: true`.
- Optional stops outside the base day use `kind: optional, included: false`;
  no clock times are needed for excluded options. Included is true by default.
- An unknown core item requires `tentative: true` and a meaningful `fallback`.
  Do not mark a whole stop verified merely because opening hours were found.
- `costs`: unique `id`, `category`, `currency`, numeric `unit_amount`, positive
  numeric `quantity`, boolean `included`, and evidence `status`. Unknown prices
  need `allowance_reason`, describing the explicitly estimated budget allowance.
  Excluded costs are add-on increments, not prepaid amounts removed from scope.

Times must be positive intervals within a single local date. Split overnight
events across calendar days before auditing. UTC offset changes, multi-timezone
transfers and DST ambiguity require explicit manual verification; the checker
does not calculate elapsed time across them. Adjacent non-overlapping blocks
are permitted; buffer adequacy and missing travel blocks remain review tasks.

## Independent constraints (recommended)

Prepare from user inputs and evidence **before** generating the plan. Do not
rewrite constraints merely to make a failing plan pass.

Optional keys: `currency`, `travelers`, `budget_cap`, `minimum_reserve`,
`required_categories`, `required_item_ids`; `days` maps ISO dates to
`earliest_start`/`latest_end`; `activities` maps item ids to authoritative
`min_minutes` and/or `window`. Exact currency/party/cap equality is checked;
reserve is a minimum. Independent windows override self-declared windows.

The checker cannot discover omitted expenses or meal/rest needs on its own;
encode required categories/items from the brief and review completeness. It
checks declared facts, not actual availability, route walking, source URLs,
whole-day fatigue, fallback quality, or whether a place is worth visiting.
