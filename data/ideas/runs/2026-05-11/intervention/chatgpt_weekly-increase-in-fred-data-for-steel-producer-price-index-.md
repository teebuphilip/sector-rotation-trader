# Weekly Increase In Fred Data For Steel Producer Price Index Signals Inflation Pressure On Materials Sector

**Idea ID:** `weekly-increase-in-fred-data-for-steel-producer-price-index-`
**Family:** `macro_input_pressure`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising steel producer prices often indicate cost pressure that can squeeze margins in materials and industrial sectors. Materials sector profitability is sensitive to input cost inflation like steel prices.

## Universe
- XLB

## Data Sources
- FRED series producer price indexes

## Signal Logic
Enter short XLB when weekly steel PPI rises more than 1% week-over-week

## Entry / Exit
Entry: Enter short XLB when weekly steel PPI rises more than 1% week-over-week Exit: Exit after 4 weeks or when steel PPI growth rate drops below 0.2%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series producer price indexes via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Steel price indexes move regularly with inflation cycles and supply shocks.

## Required Keys
- None
