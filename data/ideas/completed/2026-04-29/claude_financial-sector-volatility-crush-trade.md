# Financial Sector Volatility Crush Trade

**Idea ID:** `financial-sector-volatility-crush-trade`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When VIX drops 3+ points in a single day while the financial sector (XLF) simultaneously gaps down, it signals a washout in financial stocks despite falling macro volatility—often creating a mean-reversion bounce within days. Financial stocks are oversold when VIX falls but sector falls harder; mean reversion favors the sector.

## Universe
- XLF

## Data Sources
- Yahoo Finance daily prices for XLF and VIX via price_only adapter

## Signal Logic
If VIX falls 3+ points day-over-day AND XLF underperforms SPY by 2%+ on the same day AND XLF closes near its lows

## Entry / Exit
Entry: If VIX falls 3+ points day-over-day AND XLF underperforms SPY by 2%+ on the same day AND XLF closes near its lows Exit: After 5 trading days or once XLF closes 1.5%+ above entry

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Yahoo Finance daily prices for XLF and VIX via price_only adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: VIX daily moves of 3+ points occur several times per month; financial sector gaps down on these days frequently.

## Required Keys
- None
