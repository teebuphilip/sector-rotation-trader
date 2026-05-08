# Bank Stress Premium Decompression Fade

**Idea ID:** `bank-stress-premium-decompression-fade`
**Family:** `consumer_stress`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When money market fund inflows spike (new deposits into MMNRNJ) by 15%+ week-over-week during periods of elevated VIX, it signals panic flight-to-safety. This excess liquidity typically reverts as fear normalizes, creating 5-10 day bullish fade trades in financial equities. Money market inflows during stress compress funding spreads and reduce deposit competition for banks; stabilization allows equities to re-rate upward.

## Universe
- XLF

## Data Sources
- FRED series MMNRNJ (Money Market Mutual Fund Shares weekly) and price_only XLF daily volatility via fred_series and price_only adapters

## Signal Logic
MMNRNJ weekly inflow >15% above 4-week avg; VIX >25; XLF 20-day volatility >25%; enter long XLF

## Entry / Exit
Entry: MMNRNJ weekly inflow >15% above 4-week avg; VIX >25; XLF 20-day volatility >25%; enter long XLF Exit: After 10 trading days OR if VIX drops 30%+ from entry level, whichever first

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series MMNRNJ (Money Market Mutual Fund Shares weekly) and price_only XLF daily volatility via fred_series and price_only adapters via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: FRED money market data updates weekly; stress events occur monthly; VIX spikes provide clear entry windows; panic reversions are typically 7-14 day events.

## Required Keys
- None
