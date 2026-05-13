# Daily Jump In Google Trends For Home Appliance Repair Signals Consumer Stress Lifting Consumer Staples

**Idea ID:** `daily-jump-in-google-trends-for-home-appliance-repair-signal`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Rising searches for appliance repair indicate household cost pressures, which tend to increase demand for consumer staples as budgets shift. Staples benefit as consumers prioritize essential goods amid stress.

## Universe
- XLP

## Data Sources
- Google Trends daily queries

## Signal Logic
If daily Google Trends volume for 'home appliance repair' increases 12% day-over-day

## Entry / Exit
Entry: If daily Google Trends volume for 'home appliance repair' increases 12% day-over-day Exit: After 7 trading days or when volume drops 10% from peak

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily queries via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Household repair needs fluctuate frequently with seasonal and weather effects.

## Required Keys
- None
