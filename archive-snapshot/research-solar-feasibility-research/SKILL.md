---
name: solar-feasibility-research
description: Practical workflow for estimating residential solar conversion cost and sizing in Canada/North NB using live market research, PVWatts-style output estimates, and simple bill-of-materials math.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [research, solar, pricing, pvwatts, canada, north-nb]
---

# Solar Feasibility Research

Use this skill when a user asks for a rough or current estimate of the cost, sizing, and seasonal performance of a residential solar conversion system in Canada, especially Atlantic/North NB.

## Goal

Produce a practical answer with:
- annual energy target from monthly kWh
- array size needed for 50% and/or 100% offset
- panel/inverter/BOS cost ranges in CAD
- winter/seasonal reliability notes for North NB
- an honest view of whether the project looks economically sensible

## Workflow

1. **Convert the load**
   - Monthly kWh × 12 = annual kWh.
   - If the user wants a partial offset goal, compute that separately too.

2. **Estimate solar production for the location**
   - Prefer PVWatts or another location-based yield estimate.
   - For North NB, include winter reality: snow, short days, low sun angle, and tilt/orientation losses.
   - Size conservatively; do not assume perfect summer output year-round.

3. **Choose system class**
   - Simple roof + low shade: string inverter system is usually best value.
   - Shaded / multiple roof planes: SolarEdge or microinverters.
   - Battery/backup requirement: hybrid inverter + battery, but note this is usually costlier.

4. **Collect current CAD price ranges**
   - Panels: per-panel and per-watt prices for a few mainstream Canadian options.
   - Inverters: string, micro, and hybrid options.
   - BOS: racking, wiring, disconnects, breakers, rapid shutdown, monitoring, and likely service upgrades.
   - If live prices are unavailable, label them as market ballparks instead of exact quotes.

5. **Compute a bill of materials**
   - Panel count = system kW ÷ panel W.
   - Use low/mid/high ranges.
   - Separate material-only from labor, permits, tax, freight, and engineering.

6. **Check seasonality and storage**
   - For North NB, show monthly or seasonal imbalance if possible.
   - If the user wants reliability, discuss battery size in kWh as critical-load backup rather than full winter off-grid storage.
   - Call out that off-grid for a 3000 kWh/month home is usually very expensive and often impractical without a generator.

7. **Present payback carefully**
   - Compare annual savings against local electricity price bands.
   - Show rough simple payback ranges, not promises.
   - Mention that installation, tax, permits, and service upgrades can materially change ROI.

## Output style

Keep it practical and decision-oriented:
- “Best value” option
- “Roof-friendly” option
- “Battery-backed / hybrid” option
- low / mid / high total material estimate
- brief recommendation for 50% vs 100% offset

## Pitfalls

- Don’t claim exact current prices unless you actually verified them live.
- Don’t ignore freight, tax, and service upgrades.
- Don’t size off annual average alone; North NB winter is the limiting case.
- Don’t recommend batteries as a substitute for seasonal solar mismatch.
- Don’t bury the user in generic solar theory; show the numbers that matter.

## Verification

Before answering, sanity-check:
- panel count matches target kW
- yearly production is plausible for the location
- material totals aren’t missing inverter or BOS costs
- the recommendation matches the user’s actual goal: full offset, partial offset, or backup resilience
