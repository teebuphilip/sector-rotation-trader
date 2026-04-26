# Construction Equipment Rental Search Surge

**Idea ID:** `construction-equipment-rental-search-surge`
**Family:** `macro_input_pressure`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in construction equipment rental searches signal acceleration in commercial/residential development permitting and project starts, leading infrastructure and materials demand. Equipment rental surge precedes capital spending in construction, cement demand, and industrial equipment manufacturing.

## Universe
- XLI

## Data Sources
- Google Trends weekly interest for 'heavy equipment rental', 'excavator rental', 'crane rental' via google_trends adapter

## Signal Logic
If weekly search index exceeds 125% of 13-week moving average, go long XLI

## Entry / Exit
Entry: If weekly search index exceeds 125% of 13-week moving average, go long XLI Exit: After 4 weeks or if index falls to 105% of moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly interest for 'heavy equipment rental', 'excavator rental', 'crane rental' via google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seasonal construction cycles, permit issuance waves, and weather-driven project starts ensure equipment rental searches spike multiple times per quarter.

## Required Keys
- None
