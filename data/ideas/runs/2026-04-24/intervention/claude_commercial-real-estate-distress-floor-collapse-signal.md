# Commercial Real Estate Distress Floor Collapse Signal

**Idea ID:** `commercial-real-estate-distress-floor-collapse-signal`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
30-year mortgage rates drop >0.5% in a single week, signaling flight-to-safety demand, which precedes weakness in REITs and property valuations. Sharp mortgage rate drops indicate investor panic and reduced appetite for real estate risk assets.

## Universe
- XLRE

## Data Sources
- FRED series MORTGAGE30US (30-year mortgage rate) via fred_series adapter

## Signal Logic
If weekly mortgage rate drop > 50 bps from prior week close, short XLRE

## Entry / Exit
Entry: If weekly mortgage rate drop > 50 bps from prior week close, short XLRE Exit: Exit after 10 trading days or if rates stabilize/rise for 2 consecutive weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series MORTGAGE30US (30-year mortgage rate) via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Mortgage rates publish weekly and volatility spikes occur monthly on average during Fed policy shifts and macro uncertainty.

## Required Keys
- None
