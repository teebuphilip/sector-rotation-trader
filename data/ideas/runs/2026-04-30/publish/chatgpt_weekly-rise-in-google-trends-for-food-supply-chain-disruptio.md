# Weekly Rise In Google Trends For Food Supply Chain Disruption Signals Bearish Xlp

**Idea ID:** `weekly-rise-in-google-trends-for-food-supply-chain-disruptio`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Increasing search interest in food supply chain disruptions signals near-term risk to consumer staples supply. Supply chain issues increase costs and reduce availability, pressuring staples stocks.

## Universe
- XLP

## Data Sources
- Google Trends weekly searches

## Signal Logic
Enter short XLP if weekly search interest for 'food supply chain disruption' rises 25%+ above prior 5-week average

## Entry / Exit
Entry: Enter short XLP if weekly search interest for 'food supply chain disruption' rises 25%+ above prior 5-week average Exit: Exit after 4 weeks or if interest normalizes

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Food supply chain disruptions cause repeated search interest spikes.

## Required Keys
- None
