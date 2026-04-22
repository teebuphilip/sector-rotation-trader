# Freight Logistics Surge In Railcar Loadings Vs Industrial Etf Pullback

**Idea ID:** `freight-logistics-surge-in-railcar-loadings-vs-industrial-et`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Unexpected surge in railcar loadings while industrial sector ETF declines may indicate inventory build-up or supply chain stress. Rising freight shipments concurrent with sector weakness often precede inventory corrections and price pullbacks.

## Universe
- XLI

## Data Sources
- Weekly freight railcar loadings data

## Signal Logic
Enter short XLI if railcar loadings rise >5% WoW but XLI falls >1% WoW

## Entry / Exit
Entry: Enter short XLI if railcar loadings rise >5% WoW but XLI falls >1% WoW Exit: Exit after railcar loadings drop below 3% WoW increase or XLI rebounds 2%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Weekly freight railcar loadings data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Railcar loadings data updates weekly and often show volatility around economic cycles.

## Required Keys
- None
