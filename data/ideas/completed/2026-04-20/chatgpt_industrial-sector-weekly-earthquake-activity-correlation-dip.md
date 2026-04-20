# Industrial Sector Weekly Earthquake Activity Correlation Dip

**Idea ID:** `industrial-sector-weekly-earthquake-activity-correlation-dip`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden 40%+ weekly drop in earthquake activity near industrial regions correlates with short-term industrial sector strength due to fewer disruption risks. Lower seismic disturbances reduce operational risks for industrial companies.

## Universe
- XLI

## Data Sources
- USGS earthquake_activity weekly counts near major industrial hubs

## Signal Logic
Enter long XLI if weekly earthquake counts drop more than 40% vs prior week

## Entry / Exit
Entry: Enter long XLI if weekly earthquake counts drop more than 40% vs prior week Exit: Exit after 3 weeks or if XLI drops 4%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use USGS earthquake_activity weekly counts near major industrial hubs via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Earthquake activity fluctuates regularly enough to trigger dips and recoveries on a weekly basis.

## Required Keys
- None
