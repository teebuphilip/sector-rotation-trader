# Daily Google Trends Spike For Home Pest Control Emergency Predicts Consumer Staples Defensive Rotation

**Idea ID:** `daily-google-trends-spike-for-home-pest-control-emergency-pr`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in emergency pest control searches reflect unplanned household expenses and stress, often driving rotation into staples. Staples sector gains as consumers prioritize essential spending during stress events.

## Universe
- XLP

## Data Sources
- Google Trends daily search interest

## Signal Logic
Enter long if daily search interest for 'home pest control emergency' rises 30% above 7-day average

## Entry / Exit
Entry: Enter long if daily search interest for 'home pest control emergency' rises 30% above 7-day average Exit: Exit after 10 days or if interest falls below 7-day average

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
- Why It Should Fire Soon: Pest-related consumer stress events occur frequently with weather changes and seasonal pests.

## Required Keys
- None
