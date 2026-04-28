# Real Estate Cap Rate Compression Yield Chase Unwind

**Idea ID:** `real-estate-cap-rate-compression-yield-chase-unwind`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When 10-year mortgage rates fall >15 bps in a week but XLRE underperforms SPY by >1.5%, yield-chasing capital rotates away from real estate. Sentiment on cap rate compression fades. Rate cuts typically boost REIT valuations; when they don't, it signals investor skepticism about fundamental demand or dividend sustainability.

## Universe
- XLRE

## Data Sources
- FRED commercial real estate cap rate series (MORTGAGE30US, TERMCBCCALLNS) daily; XLRE ETF daily price via price_only adapter

## Signal Logic
10-year mortgage rate falls >15 bps weekly AND XLRE underperforms SPY by >1.5% over same period

## Entry / Exit
Entry: 10-year mortgage rate falls >15 bps weekly AND XLRE underperforms SPY by >1.5% over same period Exit: XLRE outperforms SPY >1% or 12 trading days elapsed

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED commercial real estate cap rate series (MORTGAGE30US, TERMCBCCALLNS) daily; XLRE ETF daily price via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Mortgage rates are volatile; 15 bps weekly moves occur 8–10 times annually. Signal matures quickly and fires 3–4 times per quarter.

## Required Keys
- None
