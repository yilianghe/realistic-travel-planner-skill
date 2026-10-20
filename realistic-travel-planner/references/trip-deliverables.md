# Produce usable travel decisions

Read only the sections needed. Use host tools actually available; this reference
does not install a routing engine, weather provider, hotel inventory or booking API.

## Recover from a blocked stop or missing tool

- Preserve the traveler's goal (for example, non-scenic nature photography), budget
  scope and rhythm. Do not silently substitute ticketed sightseeing for a wild
  setting, or a different experience for the desired one.
- State the blocker and its evidence once. Distinguish an existing prohibition
  from merely unverified future operating status. Missing evidence is not proof
  of closure. A recent social visit does not establish permission to enter.
- Research 1-2 alternatives that preserve the desired experience where possible.
  Show the match and the compromise, source the access status, and recommend one
  if evidence supports it. Do not use an unverified alternative to hide the gap.
- If there is no verified matching candidate, say so and deliver the useful
  remainder: candidate topology, lodging decision, weather applicability,
  cost drivers, and the exact unresolved edge. Do not invent cave entrances,
  connections or permission, and do not turn a repeat warning into the entire
  next answer. No alternate destination or purchase is implied to be accepted.
- Use a bounded alternative source/query after a failed lookup, then report the
  specific missing result. Do not send all research back to the traveler when
  publicly accessible work remains possible. Ask for a screenshot/login check
  only for a remaining decision-critical fact that accessible tools cannot get.

## Route deliverable

For a sufficiently specified trip, provide these fields in prose or a compact
table; avoid a giant blank template:

1. **Access:** named start and destination entrance/parking/meeting point, with a
   provider URL or official location link when obtained. If only a district is
   known, use a named representative origin, label the assumption, and explain
   the likely sensitivity; do not repeatedly demand a home address.
2. **Sequence:** origin -> access point -> ordered core/photo/meal/rest stops ->
   exit -> transport/overnight base. Explain the order by geography, light,
   operating windows or capacity. Do not fill an unknown trail with invented POIs.
3. **Legs:** mode, distance, base duration, door-to-door additions, query date,
   applicable date and confidence. Separate outbound/return and driving/walking.
   Unknown edges remain unknown; a coordinate or place-name search link is not
   a computed distance, a verified path or proof of access.
4. **Hikes:** distinguish the sourced full track from the adopted short variant.
   Give length, ascent, surface/technical obstacles, moving time, photo dwell,
   recovery and escape options where established. Do not borrow the full track's
   statistics for an unmeasured shortcut. Running distance does not establish
   hiking pace, navigation skill or cave/climbing competence.
5. **Schedule:** provide a feasible departure/arrival/activity/return window from
   supported legs. If timing is provisional, use ranges and state their basis.
   Respect the earliest departure. A loop may still require a shuttle to the car;
   account for it. Include actual meal/rest blocks and delay/drop rules.
6. **Decision:** core, removable with incremental time/cost, and traveler-specific
   skips. Set a turnaround rule from the measured return leg and daylight/entry
   deadline. Do not invent a universal safe return time or cave light window.

Give a GPX/track only when a legitimate source exists and its applicability is
known; say whether it was checked. Never label a hand-drawn line a verified trail.
Describe provider links as search/navigation handoffs unless actually queried.

## Accommodation deliverable

- First decide: same-day return, overnight, or overnight contingency. Explain the
  route/fatigue/budget tradeoff. A short day trip can legitimately have no hotel;
  a tired driver may need a contingency without committing to a booking.
- Compare base areas by end-of-day access, next morning's core stop, parking,
  food and the traveler's quiet/convenience preference before comparing properties.
- Normally offer 2-3 named, sourced candidates when overnight lodging is useful.
  Include exact dates, guests, room count/type, total payable amount (taxes and
  mandatory fees), parking and breakfast inclusions, check-in/out, cancellation,
  and availability status. Omit a field only with a brief uncertainty note.
- Distinguish published listing/rate from a live dated available room. A low
  teaser price, old review or hotel homepage is not an available dated quote.
  Compare equivalent room/guest scopes. Do not invent review scores or facilities.
- If booking inventory is unavailable or dates are not released, still recommend
  an area and sourced existing candidates, label price/inventory unknown, and
  give a planning allowance only if useful and clearly described as an assumption.
- Put the recommended room/parking/meal cost into the same trip budget. An upgrade
  may require cutting another expense; do not add it silently above the cap.

## Weather deliverable

1. Inspect the provider's actual **issue timestamp and valid calendar dates**,
   including year and local timezone. A weather webpage opening today can still
   contain stale data; snippets saying 'today' are not sufficient. Verify that
   the forecast covers the trip and that the station fits the site/elevation.
2. When covered, query a first-party meteorological service or available weather
   tool and report the relevant temperature range, rain/timing, wind and warnings;
   add visibility/cloud for photo-dependent or mountain trips when available.
   Cite provider, issue time and travel-day validity. Do not infer 'no warning'
   simply because the tool did not return a warning field.
3. Within about 7 days, use the covered daily forecast and shorter-period detail
   if available. At 8-15 days, treat provider products as trends, not a precise
   hour-by-hour promise. The provider's actual horizon/quality governs these
   planning bands; do not extend them to a missing date.
4. Beyond the covered daily forecast, state that the travel-day forecast is not
   available. Give sourced seasonal context only when helpful; historical ranges
   and long-range climate outlooks are not a daily forecast. Do not quote invented
   January temperatures from memory or replace January with today's October data.
5. Translate evidence into the route: choose the outdoor window, shorten exposed
   segments, switch to a matching weather-resistant option, or defer a stop when
   needed. Use official warnings/closures and site-specific conditions rather
   than an invented universal rain/wind threshold. Cave/interior conditions are
   not guaranteed by a dry city-level forecast; local assessment still matters.
6. For distant dates, give concrete user-visible recheck dates derived from the
   trip: roughly one week before for route adjustment, 1-3 days before for
   weather/closure confirmation, and departure morning for nowcast if relevant.
   Explain the decision each recheck controls. These are a checklist, not an
   automation or a promise to monitor later. Schedule follow-up only if requested.
7. Photographing a sunbeam, sunrise, cloud sea or snow view is conditional on
   geometry/season and actual cloud/visibility. Do not guarantee a named photo
   effect or copy a creator's photo time as a year-round viewing window.

Source examples (not required providers): [China Weather's 8-15 day product](https://www.weather.com.cn/weather15d/101280800.shtml)
explicitly describes uncertainty; [AMap route API documentation](https://lbs.amap.com/api/webservice/guide/api/newroute)
describes a keyed routing service. A skill referencing them does not itself
have access to those services or prove a current route/forecast was retrieved.
