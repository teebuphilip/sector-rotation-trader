# Tech Sector Volatility Crush Reversal Play

**Idea ID:** `tech-sector-volatility-crush-reversal-play`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When tech sector volatility falls to 30% below its 100-day average, it often signals complacency that precedes a sharp volatility re-expansion and repricing event. Low volatility in tech often precedes correction periods as valuations become stretched and sentiment turns; positioning unwinds create sharp drawdowns.

## Universe
- XLK

## Data Sources
- Yahoo Finance daily close prices and intraday range for XLK (technology ETF); calculate 20-day realized volatility vs. 100-day baseline

## Signal Logic
If XLK 20-day realized volatility drops below 70% of 100-day baseline and closes near daily high

## Entry / Exit
Entry: If XLK 20-day realized volatility drops below 70% of 100-day baseline and closes near daily high Exit: Exit after 10 trading days or once volatility spikes above 100-day baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily close prices and intraday range for XLK (technology ETF); calculate 20-day realized volatility vs. 100-day baseline via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Tech volatility cycles are frequent and predictable; complacency periods occur several times per quarter.

## Required Keys
- None
