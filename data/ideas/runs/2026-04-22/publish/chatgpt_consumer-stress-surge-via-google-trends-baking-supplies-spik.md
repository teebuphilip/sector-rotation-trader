# Consumer Stress Surge Via Google Trends Baking Supplies Spike

**Idea ID:** `consumer-stress-surge-via-google-trends-baking-supplies-spik`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increase in searches for baking supplies signals rising home cooking and possible consumer stress or lockdown anticipation. Rising consumer stress often causes defensive consumer staples buying but signals risk aversion for broader consumer sectors.

## Universe
- XLP

## Data Sources
- Google Trends weekly search interest for baking supplies

## Signal Logic
Enter short XLY if baking supplies Google Trends rises more than 15% WoW for 2 consecutive weeks

## Entry / Exit
Entry: Enter short XLY if baking supplies Google Trends rises more than 15% WoW for 2 consecutive weeks Exit: Exit after Google Trends falls below 10% WoW increase for 2 weeks or after 4 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for baking supplies via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Google Trends spikes in baking supplies happen multiple times yearly due to consumer stress or event-driven cooking booms.

## Required Keys
- None
