# Consumer Stress Spike From Google Trends On Urgent Appliance Repair Searches

**Idea ID:** `consumer-stress-spike-from-google-trends-on-urgent-appliance`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increased searches for urgent appliance repair indicate rising household distress impacting discretionary spending. Consumer discretionary spending tends to decline when stress and urgent repair needs rise.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for appliance repair

## Signal Logic
If weekly search volume rises 25% above 4-week moving average

## Entry / Exit
Entry: If weekly search volume rises 25% above 4-week moving average Exit: When search volume returns below 10% above moving average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for appliance repair via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Appliance issues spike seasonally and with weather changes, causing frequent search surges.

## Required Keys
- None
