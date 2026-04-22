# Daily Spike In Google Trends Searches For Air Freight Prices Surge

**Idea ID:** `daily-spike-in-google-trends-searches-for-air-freight-prices`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increasing concern about air freight prices indicates rising logistics costs and supply chain stress. Higher freight costs pressure industrial companies and margins.

## Universe
- XLI

## Data Sources
- Google Trends daily search interest for 'air freight prices surge'

## Signal Logic
If daily search interest rises 35% above 7-day average

## Entry / Exit
Entry: If daily search interest rises 35% above 7-day average Exit: After 5 trading days or interest drops below 15% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'air freight prices surge' via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Air freight price concerns frequently spike with economic and geopolitical events.

## Required Keys
- None
