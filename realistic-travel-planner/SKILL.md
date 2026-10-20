---
name: realistic-travel-planner
description: Plan and review practical leisure trips with usable route sequences, relevant lodging comparisons, date-aware weather checks, door-to-door schedules, and budget audits. Use for personalized itineraries, hiking plans, and trip repairs rather than generic destination summaries or executing bookings.
---

# Realistic Travel Planner

Make the trip executable and worthwhile for this traveler. A full calendar is not a success criterion. Respond in the user's language.

Deliver useful planning, not an intake form or a series of cautions. Read the relevant sections of [trip-deliverables.md](references/trip-deliverables.md) whenever producing routes, lodging advice, weather advice, or a recovery plan after a blocked attraction. Reuse the established brief across turns. Once the material constraints are known, produce a substantive recommendation in the next answer; ask further questions only when their answers would change that recommendation.

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

Localize a missing fact to the affected segment. An inaccessible map, unavailable hotel quote, or forecast outside its horizon must not erase the rest of the plan. Report a confirmed restriction once, then advance the decision with matched alternatives or a clearly labeled candidate structure. Do not repeat the same warning and ask the same budget/intake questions in successive answers. A spending allocation is not evidence of actual cost, and a risk notice alone is not an itinerary.

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

Show the route itself: named start/access/parking point, ordered stops, leg distances and times where supported, return geometry, and exit/turnaround logic. For hikes distinguish driving access from the walking track; give sourced distance, ascent, terrain and moving/photo/rest time separately when available. Label unsupported edges rather than inventing connections. A provider search/navigation link is a handoff to a map, not proof that a route was queried or a wild trail is passable.

## Lodging and weather when relevant

Determine whether an overnight stay serves the trip. For overnight trips compare useful base areas and normally 2-3 sourced properties, with date/party/room scope, parking, check-in/out, cancellation, total price and availability status. If rates are not released, recommend a base area and existing candidates without fabricating quotes. For a day trip state whether lodging is needed and why; do not add a hotel merely to populate a section. Honor an explicit request to compare accommodation even for a potential day trip.

Weather advice must identify the destination/site, the travel date, the forecast's issue time and valid period. Retrieve a matching forecast when the date is covered; otherwise distinguish sourced seasonal context from an unavailable daily forecast. Do not use today's weather or a stale search excerpt as the travel-day forecast. Translate rain, wind, temperature and visibility into activity choices and a recheck/decision point; do not promise photographic light effects. Follow the operational details in [trip-deliverables.md](references/trip-deliverables.md).

## 5. Make costs comparable

Use one explicit budget scope and currency. Convert per-person, per-room, per-vehicle and per-night amounts to whole-party totals with quantities. Include relevant lodging, intercity and local transport, transfers, tickets, food, luggage/parking and mandatory fees; list intentionally excluded categories with reasons. Do not silently treat prepaid expenses as free: whether they count depends on the user's cap.

Keep base spending, contingency and optional increments separate. Check `base + contingency <= cap`; explain an overrun instead of hiding it in the reserve. Unknown prices remain unknown or have an explicitly labeled planning allowance; an allowance is not a verified quote. Include add-on transport when quoting an optional stop's marginal cost.

## Build usable Plan B choices

For consequential or likely disruptions, attach a concrete alternative to the affected step. Follow [itinerary-output.md](references/itinerary-output.md) for the copy-ready format and contingency requirements. Specify the trigger, named replacement or practical exit, door-to-door switch time, net cost change, and where the revised day rejoins the plan. Protect meals, recovery, fixed bookings and the reserve. Research alternatives under the same date, preference and evidence rules as the main plan; a nearby place is not automatically open or suitable. Prefer a few useful choices over an alternative for every stop.

## 6. Audit before presenting the final plan

Check against the original traveler constraints and source evidence, not just your own draft:

- No overlap, impossible transfer, opening/entry conflict, missing meal/rest, or departure conflict.
- Full door-to-door time and realistic uncertainty buffers.
- Core bookings either verified for the date or explicitly tentative with a fallback.
- Party/currency/night arithmetic, required cost categories, prepaid scope, reserve and optional increments.
- Walking and accumulated load fit the group; a removable stop can actually be removed without breaking the next move.
- Each offered Plan B fits its revised timeline and budget, has a workable decision cutoff, and does not depend on the same failure as the original. Audit mutually exclusive branches separately; replace the original expense rather than adding both meals or counting a nonrefundable expense as recovered.

For clocked schedules or nontrivial budget arithmetic, use [the audit schema](references/audit-schema.md) and run `python scripts/audit_plan.py PLAN.json`. Save the intermediate JSON privately; do not require the traveler to read it. Prefer `--constraints CONSTRAINTS.json` to keep user limits separate from the generated plan. Fix errors and rerun. The checker verifies supplied numbers/windows only; it cannot prove sources, prices, route completeness, enjoyment or safety. If execution is unavailable, do the equivalent manual checks and disclose that the automated check was not run. Do not impose JSON or a code workflow for a simple recommendation.

## Deliver a copy-ready, structured guide

For a finished itinerary or substantive draft, read and apply [itinerary-output.md](references/itinerary-output.md). Deliver self-contained, structured prose in the user's language, ready to copy as a travel guide. Lead with the recommended plan and main compromise, then use clear sections and chronological blocks with core/removable markers, meal/rest time and Plan B choices beside the affected steps. Include route, relevant lodging judgement, date-aware weather, complete budget, skips, and actionable uncertainties with sources. Keep internal research logs and audit JSON out of the guide. Distinguish verified facts, estimates and unknowns locally; a provisional plan must say what prevents confirmation. Scale the format to the trip, and do not force the full template onto intake questions or a small follow-up. Do not claim booking or payment happened without performing an authorized action.
