# Consumer Stress Weekly Google Trends Spike In Payday Loan Searches

**Idea ID:** `consumer-stress-weekly-google-trends-spike-in-payday-loan-se`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Spike in payday loan searches indicates rising consumer cash flow stress, bearish for discretionary spending. Higher consumer stress reduces spending power in discretionary sectors.

## Universe
- XLY

## Data Sources
- Google Trends weekly search interest for payday loans

## Signal Logic
Enter short XLY if payday loan searches rise >20% WoW for 2 consecutive weeks

## Entry / Exit
Entry: Enter short XLY if payday loan searches rise >20% WoW for 2 consecutive weeks Exit: Exit after searches drop below 10% WoW increase or after 6 weeks

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly search interest for payday loans via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Payday loan search spikes reflect consumer stress cycles seen multiple times per year.

## Required Keys
- None
