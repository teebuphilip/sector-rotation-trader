# Real Estate Mortgage Rate Google Trends Capitulation Signal

**Idea ID:** `real-estate-mortgage-rate-google-trends-capitulation-signal`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When Google Trends searches for mortgage/refinance spike 40%+ above 52-week median AND mortgage rates have fallen 30+ bps in prior week, it signals capitulation by underwater borrowers; XLRE rebounds. Rate drops and search capitulation signal housing demand inflection; real estate equities rerate higher.

## Universe
- XLRE

## Data Sources
- Google Trends weekly searches for 'mortgage rates', 'home refinance', 'housing affordability' + FRED mortgage rates (MORTGAGE30US)

## Signal Logic
If mortgage Google Trends spike >40% above median AND rates dropped 30+ bps prior week, long XLRE.

## Entry / Exit
Entry: If mortgage Google Trends spike >40% above median AND rates dropped 30+ bps prior week, long XLRE. Exit: After 10 trading days or if rates rise 15+ bps.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches for 'mortgage rates', 'home refinance', 'housing affordability' + FRED mortgage rates (MORTGAGE30US) via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Housing cycles and rate swings produce search spikes monthly; conditions align 2-4 times per quarter.

## Required Keys
- None
