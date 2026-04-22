# Labor Jobs Surge In Temporary Help Services Signals Upcoming Strength In Industrial Sector

**Idea ID:** `labor-jobs-surge-in-temporary-help-services-signals-upcoming`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising temporary help employment often leads industrial production before permanent hires catch up. Temporary jobs growth indicates rising industrial activity and capacity ramp-up.

## Universe
- XLI

## Data Sources
- FRED API: Temporary Help Services Employment

## Signal Logic
Enter long XLI if temporary help employment grows >0.5% week-over-week for two consecutive weeks

## Entry / Exit
Entry: Enter long XLI if temporary help employment grows >0.5% week-over-week for two consecutive weeks Exit: Exit after 6 weeks or if growth turns negative for a week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED API: Temporary Help Services Employment via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Temporary help employment data releases weekly and often show meaningful growth spurts.

## Required Keys
- None
