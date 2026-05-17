# High Yield Bond Spread Widening Spike Signals Credit Fear Flight-to-quality

**Idea ID:** `high-yield-bond-spread-widening-spike-signals-credit-fear-fl`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When HY OAS spreads widen >30 bps in a single day, credit stress emerges. Flight-to-quality rotations out of consumer discretionary and cyclicals into utilities and staples. Credit tightening signals economic stress and weakening consumer balance sheets; discretionary spending declines.

## Universe
- XLY

## Data Sources
- FRED series BAMLH0A0HYM2 (High Yield OAS spread) daily

## Signal Logic
HY OAS widens >30 bps day-over-day; XLY closes down >0.7%; simultaneous buy XLP (staples)

## Entry / Exit
Entry: HY OAS widens >30 bps day-over-day; XLY closes down >0.7%; simultaneous buy XLP (staples) Exit: HY OAS tightens >15 bps from widening day or 6 trading days elapse

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series BAMLH0A0HYM2 (High Yield OAS spread) daily via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Credit spreads fluctuate sharply 1–2 times per week; >30 bps daily moves occur 2–3 times per month on average.

## Required Keys
- None
