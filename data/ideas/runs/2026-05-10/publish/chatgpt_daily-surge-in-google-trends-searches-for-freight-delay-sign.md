# Daily Surge In Google Trends Searches For Freight Delay Signals Industrial Sector Caution

**Idea ID:** `daily-surge-in-google-trends-searches-for-freight-delay-sign`
**Family:** `freight_logistics`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Higher frequency of 'freight delay' searches reflects growing supply chain disruptions impacting manufacturers. Supply chain delays increase costs and reduce industrial output.

## Universe
- XLI

## Data Sources
- Google Trends daily search interest for 'freight delay' via google_trends adapter

## Signal Logic
If daily search volume exceeds 8% above 20-day average

## Entry / Exit
Entry: If daily search volume exceeds 8% above 20-day average Exit: When daily search volume falls below 3% above 20-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends daily search interest for 'freight delay' via google_trends adapter via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Freight supply chain disruptions cause frequent daily search spikes.

## Required Keys
- None
