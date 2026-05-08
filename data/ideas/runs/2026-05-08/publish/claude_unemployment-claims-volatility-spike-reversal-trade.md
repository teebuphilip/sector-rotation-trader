# Unemployment Claims Volatility Spike Reversal Trade

**Idea ID:** `unemployment-claims-volatility-spike-reversal-trade`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly initial jobless claims spike unexpectedly above their 4-week moving average by more than 15%, labor market shock creates mean-reversion pressure. Claims typically normalize within 2-4 weeks unless structural deterioration is occurring. Claims spikes signal potential Fed rate-cut expectations and flight-to-safety rotation into financials as bond yields compress.

## Universe
- XLF

## Data Sources
- FRED series ICSA (Initial Claims weekly) via fred_series adapter

## Signal Logic
Initial claims breach 4-week MA by 15%+ on weekly close; enter long XLF

## Entry / Exit
Entry: Initial claims breach 4-week MA by 15%+ on weekly close; enter long XLF Exit: Claims return within 5% of 4-week MA OR after 3 weeks, whichever comes first

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series ICSA (Initial Claims weekly) via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: FRED jobless claims data updates weekly; volatility spikes occur monthly on seasonal and unexpected labor market moves; reversion typically completes within 21 days.

## Required Keys
- None
