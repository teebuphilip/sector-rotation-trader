# Freight Recession Bounce-back Signal

**Idea ID:** `freight-recession-bounce-back-signal`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When monthly truck freight volume rebounds 3%+ from its lowest point in a 6-month window, it signals logistics demand recovery. Industrial and consumer discretionary sectors experience 2-4 week rallies as inventory replenishment accelerates. Freight recovery is a leading indicator of production and consumption rebound; benefits industrial equipment and logistics operators.

## Universe
- XLI

## Data Sources
- FRED series TRFVOLUSM157N (Truck freight volume monthly) via fred_series adapter

## Signal Logic
Truck freight volume rebounds 3%+ month-over-month from trailing 6-month minimum; enter long XLI on release day close

## Entry / Exit
Entry: Truck freight volume rebounds 3%+ month-over-month from trailing 6-month minimum; enter long XLI on release day close Exit: After 14 trading days OR if truck freight declines 1%+ in next month's report, whichever first

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series TRFVOLUSM157N (Truck freight volume monthly) via fred_series adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: FRED truck freight updates monthly; rebounding cycles occur every 2-3 months during normal business cycles; 14-day exit window ensures capture of mean-reversion momentum.

## Required Keys
- None
