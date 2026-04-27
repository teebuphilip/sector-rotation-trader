# Unemployment Claims Surprise Volatility Pop Trade

**Idea ID:** `unemployment-claims-surprise-volatility-pop-trade`
**Family:** `labor_jobs`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly jobless claims exceed prior week by 10k+ AND exceed 52-week average by 15%+, it signals labor market deterioration; XLF and XLI reverse hard over next 5-10 days as recession fears spike and fade. Jobless claims spikes trigger cyclical sector selloffs; financials and industrials are hit first due to credit cycle fears.

## Universe
- XLF

## Data Sources
- FRED Initial Jobless Claims (ICSA) weekly release

## Signal Logic
If claims surge >10k WoW and >15% above 52-week avg, short XLF.

## Entry / Exit
Entry: If claims surge >10k WoW and >15% above 52-week avg, short XLF. Exit: After 8 trading days or if claims fall 5k+ WoW.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED Initial Jobless Claims (ICSA) weekly release via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Jobless claims spike frequently; threshold fires 3-5 times per quarter as labor volatility is persistent.

## Required Keys
- None
