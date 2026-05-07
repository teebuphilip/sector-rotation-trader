# Weekly Rise In Google Trends For Food Delivery Delay Signals Consumer Stress Impacting Staples Sector

**Idea ID:** `weekly-rise-in-google-trends-for-food-delivery-delay-signals`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing delivery delay searches indicate supply chain stress affecting consumer staples availability. Supply chain issues pressure staples companies through higher costs and reduced sales.

## Universe
- XLP

## Data Sources
- Google Trends weekly searches for 'food delivery delay'

## Signal Logic
Enter short XLP if weekly search interest rises 25% above 8-week average

## Entry / Exit
Entry: Enter short XLP if weekly search interest rises 25% above 8-week average Exit: Exit after 4 weeks or when searches fall below 10% above baseline

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches for 'food delivery delay' via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Food delivery issues are frequent due to logistics and staffing constraints in urban areas.

## Required Keys
- None
