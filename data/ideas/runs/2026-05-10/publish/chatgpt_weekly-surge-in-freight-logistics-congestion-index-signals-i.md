# Weekly Surge In Freight Logistics Congestion Index Signals Industrial Sector Pressure

**Idea ID:** `weekly-surge-in-freight-logistics-congestion-index-signals-i`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sharp weekly increase in freight congestion often precedes supply chain bottlenecks, slowing manufacturing output. Industrial sector earnings rely heavily on smooth freight logistics; congestion constrains growth.

## Universe
- XLI

## Data Sources
- Freight congestion index weekly data via html_table adapter

## Signal Logic
If weekly congestion index rises more than 5% compared to prior week

## Entry / Exit
Entry: If weekly congestion index rises more than 5% compared to prior week Exit: Once congestion index falls below 2% weekly change

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Freight congestion index weekly data via html_table adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Freight congestion varies regularly with ongoing supply chain disruptions and seasonal factors.

## Required Keys
- None
