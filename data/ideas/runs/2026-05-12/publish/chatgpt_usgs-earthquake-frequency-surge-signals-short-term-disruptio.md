# Usgs Earthquake Frequency Surge Signals Short-term Disruption Recovery Bounce In Industrials

**Idea ID:** `usgs-earthquake-frequency-surge-signals-short-term-disruptio`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A sudden increase in moderate earthquake occurrences correlates with temporary supply chain and infrastructure disruptions followed by rebound construction and industrial activity. Industrial companies often benefit from increased repair and rebuilding efforts following seismic events.

## Universe
- XLI

## Data Sources
- USGS earthquake daily activity counts

## Signal Logic
Enter long XLI when daily count of magnitude 4+ earthquakes in US rises 50% above 14-day average

## Entry / Exit
Entry: Enter long XLI when daily count of magnitude 4+ earthquakes in US rises 50% above 14-day average Exit: Exit after 10 trading days or when earthquake counts revert to normal

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake daily activity counts via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Earthquake swarms and clusters happen multiple times annually, triggering local industrial activity bursts.

## Required Keys
- None
