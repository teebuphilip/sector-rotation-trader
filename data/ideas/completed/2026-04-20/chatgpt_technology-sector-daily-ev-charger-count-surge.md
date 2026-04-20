# Technology Sector Daily Ev Charger Count Surge

**Idea ID:** `technology-sector-daily-ev-charger-count-surge`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
A daily 5%+ increase in EV charger counts correlates with tech sector optimism driven by green technology adoption. Rising EV infrastructure investment reflects tech innovation and policy tailwinds.

## Universe
- XLK

## Data Sources
- OpenChargeMap daily US EV charger counts aggregated

## Signal Logic
Enter long XLK if daily EV charger counts increase >5% compared to prior day

## Entry / Exit
Entry: Enter long XLK if daily EV charger counts increase >5% compared to prior day Exit: Exit after 7 trading days or if XLK drops 3%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use OpenChargeMap daily US EV charger counts aggregated via api (daily).

## High Action Metadata
- Expected Fire Rate: daily
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: EV infrastructure expands steadily with occasional daily surges.

## Required Keys
- None
