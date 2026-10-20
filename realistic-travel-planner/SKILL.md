---
name: realistic-travel-planner
description: Plan and review practical leisure trips by clarifying traveler priorities, checking dated evidence, scheduling door-to-door travel and recovery, separating core and removable stops, and auditing time and budget. Use for personalized itineraries and itinerary repairs, rather than generic destination summaries or executing bookings.
---

# Realistic Travel Planner

Make the trip executable and worthwhile for this traveler. A full calendar is not a success criterion. Respond in the user's language.

## 1. Establish the planning contract before a daily itinerary

Reuse facts already provided. Confirm only missing information that could change the plan:

- Dates, arrival/departure times, actual starting point, booked commitments, destination or candidates.
- Daily rhythm: earliest comfortable departure, bedtime, late nights, meal and nap needs.
- Capacity: comfortable walking/standing, stairs, driving, recovery, luggage; ask for practical limits rather than diagnoses.
- Companions and their different needs; plan for the limiting constraint when staying together.
- Budget: currency, per person or whole party, trip or daily cap, included/excluded expenses, willingness to pay for convenience, allocation priorities, and contingency reserve.
- Desired experience: what would make the trip worthwhile, must-do items, dislikes, and willingness to skip a famous stop.

Ask a compact batch, normally at most three questions; combine related fields. Do not repeat answered questions or demand a complete profile. If a decision-critical answer is pending, continue destination/evidence research but do not lock a daily itinerary. For an explicitly requested rough draft, state assumptions and show provisional day shapes rather than invented clock precision. For a review or same-day repair, preserve valid bookings and ask only about the changed state.

## 2. Check feasibility before recommending stops

Use current search, official pages, maps, or tools actually available in the host. The skill installs no data provider. Read [evidence.md](references/evidence.md) when researching changing facts or when tools are unavailable.

Verify the exact visit date where possible: opening and last-entry times, closed days, booking/release rules, ticket availability, transport service and last departure, check-in/luggage arrangements, weather or closure conditions that change the decision. A published timetable or price does not prove live availability. A map route does not prove a dated direct train exists.

Keep an evidence ledger for decision-critical facts: claim, applicability date, source URL/provider, checked-at date/time with timezone, and status `verified`, `estimated`, or `unknown`. Explain conflicting evidence. Separate recent experience reports about queues and enjoyment from official operating rules. Cite the facts that determine the route; do not bury critical caveats at the end.

If a core activity depends on unknown entry/availability, keep it tentative and name a fallback and a latest decision time. Ask the user to check an authenticated booking screen only if the missing fact materially changes the trip and accessible channels cannot resolve it. Never invent certainty to finish a table.

## 3. Choose what deserves the traveler's time

Select anchors around the desired experience, not popularity. Group by geography only after checking operating windows and the traveler's rhythm. Explain tradeoffs when two must-do items conflict.

For each day distinguish:

- **Core:** the main reason for the day; protect its time and reservation.
- **Removable:** genuinely optional, with its extra time/cost and the condition for dropping it. Show this outside the committed schedule unless its full time and cost are budgeted.
- **Skip:** plausible or famous candidates rejected for this traveler, with a concrete reason such as low fit, duplicate experience, long detour, or poor seasonal conditions. Do not invent a blacklist or force exclusions when no reasonable alternative was considered.

Default conservatively when capacity is unclear. Evaluate early starts, walking, queues, stairs, driving, heat and poor sleep together. Do not label a day relaxed merely because each individual segment looks short. When oversubscribed, cut or move a stop before shrinking meals, transit or rest to implausible lengths.

## 4. Build a door-to-door schedule

For each major move account for origin exit/checkout, luggage, walk to pickup/station, wait, ride, transfer, destination approach/entry and a disruption buffer. Avoid double counting components already included in a map estimate. Label the base estimate, additions and uncertainty. Never substitute straight-line distance or in-vehicle time for door-to-door time.

Reserve real blocks for queues/security, meals, seated recovery, luggage, and arrival/departure friction. Respect last entry, fixed bookings, station/airport lead time and date-specific service. Distinguish arrival at the gate from actual entry. Use ranges or rounded times where uncertainty is large; precision is not evidence.

Keep an executable base day and a short add-on list. Give a clear overrun rule, for example: if lunch finishes after 14:00, drop the optional viewpoint and keep the booked museum. If uncertainty threatens a core reservation, move it, change transport or leave more space.

## 5. Make costs comparable

Use one explicit budget scope and currency. Convert per-person, per-room, per-vehicle and per-night amounts to whole-party totals with quantities. Include relevant lodging, intercity and local transport, transfers, tickets, food, luggage/parking and mandatory fees; list intentionally excluded categories with reasons. Do not silently treat prepaid expenses as free: whether they count depends on the user's cap.

Keep base spending, contingency and optional increments separate. Check `base + contingency <= cap`; explain an overrun instead of hiding it in the reserve. Unknown prices remain unknown or have an explicitly labeled planning allowance; an allowance is not a verified quote. Include add-on transport when quoting an optional stop's marginal cost.

## 6. Audit before presenting the final plan

Check against the original traveler constraints and source evidence, not just your own draft:

- No overlap, impossible transfer, opening/entry conflict, missing meal/rest, or departure conflict.
- Full door-to-door time and realistic uncertainty buffers.
- Core bookings either verified for the date or explicitly tentative with a fallback.
- Party/currency/night arithmetic, required cost categories, prepaid scope, reserve and optional increments.
- Walking and accumulated load fit the group; a removable stop can actually be removed without breaking the next move.

For clocked schedules or nontrivial budget arithmetic, use [the audit schema](references/audit-schema.md) and run `python scripts/audit_plan.py PLAN.json`. Save the intermediate JSON privately; do not require the traveler to read it. Prefer `--constraints CONSTRAINTS.json` to keep user limits separate from the generated plan. Fix errors and rerun. The checker verifies supplied numbers/windows only; it cannot prove sources, prices, route completeness, enjoyment or safety. If execution is unavailable, do the equivalent manual checks and disclose that the automated check was not run. Do not impose JSON or a code workflow for a simple recommendation.

## Deliver in the amount of detail needed

Start with the recommendation and the main compromise. Include the confirmed assumptions; a base itinerary with core/removable markers; door-to-door major moves; meal/recovery blocks; budget scope, subtotal/reserve/add-ons; relevant skips; and actionable unresolved items with sources and fallbacks. State what has actually been checked and what remains uncertain. A small trip needs a small answer. Do not claim booking or payment happened without performing an authorized action.
