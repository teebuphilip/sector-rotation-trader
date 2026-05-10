# Commercial Real Estate Financing Stress Google Trends

**Idea ID:** `commercial-real-estate-financing-stress-google-trends`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in commercial real estate financing search terms signal financial distress in office/retail property markets, pressuring REIT and financial valuations. CRE financing stress directly impacts REIT returns and commercial property values.

## Universe
- XLRE

## Data Sources
- Google Trends weekly search interest for 'commercial mortgage rates' and 'CMBS default,' normalized to 12-week baseline

## Signal Logic
If either search term spikes >45% WoW above 12-week MA, short real estate

## Entry / Exit
Entry: If either search term spikes >45% WoW above 12-week MA, short real estate Exit: Exit after 10 trading days or if search interest normalizes to <120% of 12-week MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for 'commercial mortgage rates' and 'CMBS default,' normalized to 12-week baseline via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Commercial mortgage and CMBS stress searches spike >45% WoW 2–3 times per quarter, driven by rate cycle turns and quarterly earnings disappointments.

## Required Keys
- None
