# Daily Jump In Google Trends For Gas Price Protest Signals Energy Sector Volatility

**Idea ID:** `daily-jump-in-google-trends-for-gas-price-protest-signals-en`
**Family:** `consumer_stress`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden spikes in protest-related searches indicate rising consumer anger and regulatory risk impacting energy prices. Energy sector is vulnerable to social unrest and political pressure on fuel pricing.

## Universe
- XLE

## Data Sources
- Google Trends daily search interest

## Signal Logic
Enter short XLE if daily Google Trends for 'gas price protest' rises 50% above 7-day average

## Entry / Exit
Entry: Enter short XLE if daily Google Trends for 'gas price protest' rises 50% above 7-day average Exit: Exit after 5 trading days or if daily interest drops below 7-day average

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
- Why It Should Fire Soon: Social unrest events and protests generate frequent search spikes.

## Required Keys
- None
