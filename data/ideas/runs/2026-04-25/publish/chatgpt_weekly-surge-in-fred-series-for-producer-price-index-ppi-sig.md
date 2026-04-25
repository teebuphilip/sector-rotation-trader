# Weekly Surge In Fred Series For Producer Price Index Ppi Signals Bearish Xlb

**Idea ID:** `weekly-surge-in-fred-series-for-producer-price-index-ppi-sig`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sharp rise in PPI indicates input cost inflation pressure for materials companies, squeezing margins. Materials sector margins are sensitive to input cost inflation, reducing earnings expectations.

## Universe
- XLB

## Data Sources
- FRED Producer Price Index (PPI) weekly aggregated data

## Signal Logic
Enter short XLB if weekly PPI rises more than 1.5% week-over-week

## Entry / Exit
Entry: Enter short XLB if weekly PPI rises more than 1.5% week-over-week Exit: Exit after 4 weeks or if PPI growth decelerates below 0.5% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED Producer Price Index (PPI) weekly aggregated data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Commodity price shocks and inflation pressures often spike multiple times per year.

## Required Keys
- None
