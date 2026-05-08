# Daily Jump In Consumer Stress Google Trends Searches For Car Repossession Signals Rising Financial Distress

**Idea ID:** `daily-jump-in-consumer-stress-google-trends-searches-for-car`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Spikes in searches for repossession indicate consumer financial strain that may impact discretionary spending. Higher consumer stress reduces discretionary spending, pressuring retail and leisure sectors.

## Universe
- XLY

## Data Sources
- Google Trends daily search interest

## Signal Logic
If daily searches for 'car repossession' increase over 25% compared to prior 7-day average

## Entry / Exit
Entry: If daily searches for 'car repossession' increase over 25% compared to prior 7-day average Exit: Once searches fall below 10% above prior 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Financial stress indicators fluctuate with economic conditions and can spike due to unemployment or credit tightening.

## Required Keys
- None
