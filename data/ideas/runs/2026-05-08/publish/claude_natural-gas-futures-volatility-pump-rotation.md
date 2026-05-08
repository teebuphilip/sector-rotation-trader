# Natural Gas Futures Volatility Pump Rotation

**Idea ID:** `natural-gas-futures-volatility-pump-rotation`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Unusual weekly EIA storage draws (>10% above seasonal norm) combined with rising futures volatility trigger energy sector rotation; energy stocks often lag futures by 2-5 trading days due to portfolio rebalancing. Input cost shocks typically compress energy sector valuations but benefit large integrated producers on margin expansion when commodities spike.

## Universe
- XLE

## Data Sources
- EIA Natural Gas Storage Weekly (via html_table adapter) paired with price_only daily futures proxy

## Signal Logic
EIA weekly storage draw >10% above 5-year seasonal median; natural gas futures up 2%+ on day of release; enter long XLE at close

## Entry / Exit
Entry: EIA weekly storage draw >10% above 5-year seasonal median; natural gas futures up 2%+ on day of release; enter long XLE at close Exit: After 10 trading days OR once natural gas futures reverse 3% from entry, whichever first

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use EIA Natural Gas Storage Weekly (via html_table adapter) paired with price_only daily futures proxy via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EIA releases storage weekly; abnormal draws occur 3-4 times per quarter; futures volatility spikes regularly; price action lags trigger by defined window.

## Required Keys
- None
