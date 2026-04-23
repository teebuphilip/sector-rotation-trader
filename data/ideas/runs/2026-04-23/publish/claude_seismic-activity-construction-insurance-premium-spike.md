# Seismic Activity Construction Insurance Premium Spike

**Idea ID:** `seismic-activity-construction-insurance-premium-spike`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Clusters of >3.0 magnitude earthquakes in major metro areas spike construction insurance demand and delay project starts. Materials demand softens as contractors postpone work, but insurance/reinsurance stocks see margin improvement. Earthquake swarms delay construction spending and postpone materials purchases; materials producers face near-term demand destruction.

## Universe
- XLB

## Data Sources
- USGS earthquake activity daily API (magnitude >3.0 events in construction-heavy regions: CA, WA, OK) via earthquake_activity adapter, plus XLB (materials/construction) weekly close via price_only adapter

## Signal Logic
If 3+ earthquakes >3.0 magnitude occur within a 7-day window in CA/WA/OK AND XLB closes < 10-day SMA AND XLB shows negative momentum (close < open for 2+ of last 3 days)

## Entry / Exit
Entry: If 3+ earthquakes >3.0 magnitude occur within a 7-day window in CA/WA/OK AND XLB closes < 10-day SMA AND XLB shows negative momentum (close < open for 2+ of last 3 days) Exit: After 14 calendar days OR if no magnitude >3.0 events occur for 5 consecutive days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity daily API (magnitude >3.0 events in construction-heavy regions: CA, WA, OK) via earthquake_activity adapter, plus XLB (materials/construction) weekly close via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic activity clusters occur 2–3 times per quarter in active regions; each swarm triggers construction caution.

## Required Keys
- None
