# Daily Surge In Google Trends For Emergency Food Delivery Signals Consumer Stress Lifting Staples Demand

**Idea ID:** `daily-surge-in-google-trends-for-emergency-food-delivery-sig`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden increase in emergency food delivery searches signals consumer stress and elevated food demand. Consumer staples benefit from stress-driven spikes in emergency food consumption.

## Universe
- XLP

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily Google Trends for 'emergency food delivery' rises 50% vs 7-day average

## Entry / Exit
Entry: If daily Google Trends for 'emergency food delivery' rises 50% vs 7-day average Exit: After 5 trading days or if trend falls below 20% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Consumer food delivery searches often spike during supply chain issues or weather events.

## Required Keys
- None
