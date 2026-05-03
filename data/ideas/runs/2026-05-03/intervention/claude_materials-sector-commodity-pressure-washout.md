# Materials Sector Commodity Pressure Washout

**Idea ID:** `materials-sector-commodity-pressure-washout`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
When both crude oil and gold drawdown sharply (>8% over 10 days) simultaneously, it signals macro risk-off sentiment crushing commodities-linked valuations, often creating mean-reversion bounce opportunities in materials stocks. Extreme commodity weakness creates valuation compression in materials and mining stocks, generating technical bounce setups as oversold conditions reverse.

## Universe
- XLB

## Data Sources
- FRED series DCOILWTICO (crude oil prices) and GOLDAMND (gold spot) daily; calculate 10-day drawdown from 20-day high

## Signal Logic
If both crude and gold fall >8% from 20-day highs within 10-day window and XLB closes at 20-day low

## Entry / Exit
Entry: If both crude and gold fall >8% from 20-day highs within 10-day window and XLB closes at 20-day low Exit: Exit after 6 trading days or if either commodity bounces >3% from entry low

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series DCOILWTICO (crude oil prices) and GOLDAMND (gold spot) daily; calculate 10-day drawdown from 20-day high via api (daily).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Commodity volatility is consistent; major drawdown events occur 3–4 times per year, providing regular entry opportunities.

## Required Keys
- None
