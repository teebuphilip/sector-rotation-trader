# Bank Stress Index Volatility Fear Crush Reversal

**Idea ID:** `bank-stress-index-volatility-fear-crush-reversal`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
VIX spikes >25 while XLF underperforms SPY by >2%, then reverses sharply as Fed rate-cut expectations emerge, driving financials outperformance. Financial sector rallies when fear subsides and rate expectations stabilize in their favor.

## Universe
- XLF

## Data Sources
- Price_only adapter for financial sector ETF XLF and VIX via Yahoo Finance; daily data

## Signal Logic
If VIX > 25 and XLF lags SPY by >2% over 3 days, then VIX falls >5 points in 1 day, long XLF

## Entry / Exit
Entry: If VIX > 25 and XLF lags SPY by >2% over 3 days, then VIX falls >5 points in 1 day, long XLF Exit: Exit after 8 trading days or if XLF underperforms again

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Price_only adapter for financial sector ETF XLF and VIX via Yahoo Finance; daily data via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Daily VIX and ETF data; fear/relief cycles occur 4–6 times per quarter in response to Fed announcements and earnings surprises.

## Required Keys
- None
