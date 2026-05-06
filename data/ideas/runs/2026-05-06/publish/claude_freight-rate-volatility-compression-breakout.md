# Freight Rate Volatility Compression Breakout

**Idea ID:** `freight-rate-volatility-compression-breakout`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Trucking demand volatility (20-day rolling standard deviation) drops to multi-month lows before sharp directional breakouts; low volatility regimes rarely persist beyond 2 weeks. Freight stability shocks correlate with industrial production cycles and supply chain tightening, benefiting industrials and logistics infrastructure.

## Universe
- XLI

## Data Sources
- FRED series TRUCKD (trucking demand proxy) daily observations through fred_series adapter

## Signal Logic
If 20-day rolling volatility of TRUCKD drops below 25th percentile of trailing 3-month range, enter long

## Entry / Exit
Entry: If 20-day rolling volatility of TRUCKD drops below 25th percentile of trailing 3-month range, enter long Exit: Exit after 10 trading days or if volatility exceeds 75th percentile

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series TRUCKD (trucking demand proxy) daily observations through fred_series adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Volatility compression windows occur every 3-4 weeks in freight data, with breakouts reliably following within 5-10 days.

## Required Keys
- None
