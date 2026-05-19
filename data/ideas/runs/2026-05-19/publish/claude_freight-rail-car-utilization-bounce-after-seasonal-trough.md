# Freight Rail Car Utilization Bounce After Seasonal Trough

**Idea ID:** `freight-rail-car-utilization-bounce-after-seasonal-trough`
**Family:** `freight_logistics`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Post-holiday seasonal freight collapse (Q1) reverses sharply as spring manufacturing ramps; rail car utilization jumps >15% week-over-week signal economic recovery confidence. Rail utilization surge indicates industrial production recovery and demand acceleration across consumer goods and materials.

## Universe
- XLI

## Data Sources
- Association of American Railroads weekly freight car orders and loads through html_table adapter

## Signal Logic
When weekly freight car loads exceed 52-week average by >8% after 4+ weeks below average

## Entry / Exit
Entry: When weekly freight car loads exceed 52-week average by >8% after 4+ weeks below average Exit: After 3 weeks of sustained above-average loads or after 21 days

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Association of American Railroads weekly freight car orders and loads through html_table adapter via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 36
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Seasonal freight cycles repeat annually; Q1-to-Q2 transition produces reliable utilization spikes multiple times per year in the dataset.

## Required Keys
- None
