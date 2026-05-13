# Rare Earth Element And Lithium Commodity Price Surge Signals Supply Shock And Inflation Expectations Lift

**Idea ID:** `rare-earth-element-and-lithium-commodity-price-surge-signals`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** daily

## Thesis
Lithium and rare earth futures spike on supply disruptions (mine shutdowns, export bans) or demand surges (EV/renewable buildout acceleration). 15%+ 5-day moves trigger inflation concerns and materials rallies. Lithium and rare earth cost spikes are passed through to battery and electronics manufacturers, raising input costs but supporting materials producer margins.

## Universe
- XLB

## Data Sources
- Commodity futures prices for lithium carbonate (China) and rare earth rare earth (US) via price_only adapter using SPDR commodity ETFs (XLB, LIT proxies) or direct futures

## Signal Logic
When lithium or rare earth futures rise 12% or more over 3 trading days AND close above 20-day moving average

## Entry / Exit
Entry: When lithium or rare earth futures rise 12% or more over 3 trading days AND close above 20-day moving average Exit: After 8 trading days or when price falls back below 20-day MA

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Commodity futures prices for lithium carbonate (China) and rare earth rare earth (US) via price_only adapter using SPDR commodity ETFs (XLB, LIT proxies) or direct futures via api (daily).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Commodity markets are volatile and supply disruptions are frequent. Mine accidents, geopolitical events, and demand shifts produce 10-30% weekly moves multiple times per year.

## Required Keys
- None
