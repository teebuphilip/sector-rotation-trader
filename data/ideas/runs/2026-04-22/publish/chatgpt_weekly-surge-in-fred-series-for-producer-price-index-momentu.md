# Weekly Surge In Fred Series For Producer Price Index Momentum

**Idea ID:** `weekly-surge-in-fred-series-for-producer-price-index-momentu`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Acceleration in PPI signals rising input costs that can pressure corporate margins, especially in industrials. Industrial companies face margin compression from rising input prices.

## Universe
- XLI

## Data Sources
- FRED weekly producer price index (PPI) change data

## Signal Logic
Enter short XLI when weekly PPI increase exceeds 0.5% WoW

## Entry / Exit
Entry: Enter short XLI when weekly PPI increase exceeds 0.5% WoW Exit: Exit after 4 weeks or when PPI growth falls below 0.1% WoW

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly producer price index (PPI) change data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: PPI changes regularly exceed 0.5% WoW during commodity price volatility.

## Required Keys
- None
