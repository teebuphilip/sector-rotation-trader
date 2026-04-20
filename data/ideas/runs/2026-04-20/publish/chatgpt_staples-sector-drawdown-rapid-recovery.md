# Staples Sector Drawdown Rapid Recovery

**Idea ID:** `staples-sector-drawdown-rapid-recovery`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
When XLP falls 3%+ in 3 days but bounces back 1%+ on the 4th day, it often signals short-term oversold relief. Consumer staples often see quick mean reversion after sharp short-term selloffs.

## Universe
- XLP

## Data Sources
- Yahoo Finance daily prices for XLP

## Signal Logic
Enter long XLP on day 4 if prior 3-day loss >3% and day 4 gains >1%

## Entry / Exit
Entry: Enter long XLP on day 4 if prior 3-day loss >3% and day 4 gains >1% Exit: Exit after 5 trading days or if price falls 2% from entry

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for XLP via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Staples experience frequent short-term selloffs and rebounds in volatile environments.

## Required Keys
- None
