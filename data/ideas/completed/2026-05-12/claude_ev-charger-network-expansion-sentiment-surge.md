# Ev Charger Network Expansion Sentiment Surge

**Idea ID:** `ev-charger-network-expansion-sentiment-surge`
**Family:** `attention_sentiment`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
Spikes in charger installation and concurrent surge in consumer searches signal bullish infrastructure narrative, lifting XLK (chip/software) and XLI (automotive) positioning. EV charging expansion is a positive signal for semiconductor and software demand in automotive electrification.

## Universe
- XLK

## Data Sources
- OpenChargeMap API weekly count of newly added chargers across US; pair with Google Trends weekly search volume for 'EV charging stations near me'

## Signal Logic
If weekly new charger count rises >20% QoQ and Google Trends 'EV charging' searches rise >30% YoY

## Entry / Exit
Entry: If weekly new charger count rises >20% QoQ and Google Trends 'EV charging' searches rise >30% YoY Exit: After 4 weeks or if charger growth rate decelerates below 10% QoQ

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap API weekly count of newly added chargers across US; pair with Google Trends weekly search volume for 'EV charging stations near me' via api (weekly).

## High Action Metadata
- Expected Fire Rate: monthly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Government subsidy cycles and corporate announcements cluster charger expansion; signal fires 3–4 times per year.

## Required Keys
- None
