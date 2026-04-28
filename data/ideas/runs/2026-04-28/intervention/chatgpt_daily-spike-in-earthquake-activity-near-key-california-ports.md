# Daily Spike In Earthquake Activity Near Key California Ports Signals Supply Chain Risk

**Idea ID:** `daily-spike-in-earthquake-activity-near-key-california-ports`
**Family:** `local_economy_weirdness`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Increased seismic activity near major ports increases risk perceptions of supply chain interruptions. Industrial sector sensitive to shipping and logistic disruptions.

## Universe
- XLI

## Data Sources
- USGS earthquake activity daily reports

## Signal Logic
Enter short XLI if daily earthquake counts near California ports rise by 50% above 30-day average

## Entry / Exit
Entry: Enter short XLI if daily earthquake counts near California ports rise by 50% above 30-day average Exit: Exit after 5 trading days or if activity normalizes below 10-day average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake activity daily reports via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Seismic activity clusters often last several days or weeks, triggering repeated alerts.

## Required Keys
- None
