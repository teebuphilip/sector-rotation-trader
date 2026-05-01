# Daily Jump In Usgs Earthquake Activity Intensity Correlates With Temporary Selloff In Infrastructure Sector

**Idea ID:** `daily-jump-in-usgs-earthquake-activity-intensity-correlates-`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Significant increases in local seismic activity cause short-term market nervousness around infrastructure and construction sectors. Increased earthquake activity raises fears of supply chain disruption and infrastructure repair costs.

## Universe
- XLI

## Data Sources
- USGS earthquake activity data

## Signal Logic
Enter short XLI when daily earthquake energy release index rises 30% above 7-day moving average

## Entry / Exit
Entry: Enter short XLI when daily earthquake energy release index rises 30% above 7-day moving average Exit: Exit after 3 trading days or when the index falls below its 7-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity data via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Earthquake activity frequently fluctuates daily, triggering reactive market sentiment.

## Required Keys
- None
