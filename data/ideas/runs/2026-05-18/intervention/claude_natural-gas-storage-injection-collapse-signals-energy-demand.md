# Natural Gas Storage Injection Collapse Signals Energy Demand Shock

**Idea ID:** `natural-gas-storage-injection-collapse-signals-energy-demand`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When weekly natural gas storage injections plummet (or turn to unexpected draws), it signals either demand spike or supply shock, creating energy price volatility and sector stress. Unexpected storage draws or injection collapses support energy prices and create near-term energy sector gains from price recovery.

## Universe
- XLE

## Data Sources
- EIA weekly natural gas storage updates through fred_series adapter

## Signal Logic
If weekly EIA gas storage injection falls below historical 5-year minimum for that week by 50% or more, go long XLE.

## Entry / Exit
Entry: If weekly EIA gas storage injection falls below historical 5-year minimum for that week by 50% or more, go long XLE. Exit: Exit after 8 trading days or when injection rebounds to normal levels.

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use EIA weekly natural gas storage updates through fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Gas storage swings 50%+ vs. seasonal norms occur 4–8 times per year, particularly in winter and summer transition periods.

## Required Keys
- None
