# Ev Charger Count Growth Slowdown Signals Ev Subsidy Cliff Ahead

**Idea ID:** `ev-charger-count-growth-slowdown-signals-ev-subsidy-cliff-ah`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When weekly EV charger growth drops below 0.3% (i.e., rollover in new installations), it signals waning subsidy tailwinds and slowing EV infrastructure buildout sentiment. EV-related tech and semiconductor stocks rally on infrastructure optimism; slowdown in charger deployment signals reduced future demand for EV chips.

## Universe
- XLK

## Data Sources
- OpenChargeMap daily EV charger count (US total) via openchargemap adapter

## Signal Logic
Weekly EV charger growth (7-day percent change) falls below 0.3% AND semiconductor ETF (SOXX) closes down >0.9% on same week

## Entry / Exit
Entry: Weekly EV charger growth (7-day percent change) falls below 0.3% AND semiconductor ETF (SOXX) closes down >0.9% on same week Exit: SOXX closes up >1% from entry or 2 weeks elapse

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap daily EV charger count (US total) via openchargemap adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: EV infrastructure growth is lumpy; 0.3% weekly threshold is crossed 2–3 times per quarter.

## Required Keys
- None
