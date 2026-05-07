# Small Cap Value Dividend Yield Compression Fade

**Idea ID:** `small-cap-value-dividend-yield-compression-fade`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When IWN dividend yield compresses by 15%+ from 12-month high in a 10-day window, it signals overheating rotation out of value into momentum that typically mean-reverts within 2-3 weeks. Value yield compression followed by mean reversion creates tactical long opportunities in financials and small-cap industrial leaders.

## Universe
- XLF

## Data Sources
- Yahoo Finance daily price and dividend data for IWN (Russell 2000 Value) via price_only adapter

## Signal Logic
When IWN dividend yield drops 15% from 12-month rolling high within 10 days

## Entry / Exit
Entry: When IWN dividend yield drops 15% from 12-month rolling high within 10 days Exit: After 12 trading days or when yield rebounds to within 10% of previous peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily price and dividend data for IWN (Russell 2000 Value) via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Dividend yield volatility in small-cap value is common; compressions occur 1-2 times per month in normal markets.

## Required Keys
- None
