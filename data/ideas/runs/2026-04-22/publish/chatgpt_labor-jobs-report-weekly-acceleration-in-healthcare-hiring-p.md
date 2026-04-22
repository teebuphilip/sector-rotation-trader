# Labor Jobs Report Weekly Acceleration In Healthcare Hiring Paired With Xlv Outperformance

**Idea ID:** `labor-jobs-report-weekly-acceleration-in-healthcare-hiring-p`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A rapid weekly increase in healthcare job postings signals anticipated sector growth and potential upward earnings revisions. Healthcare hiring acceleration suggests improving fundamentals for healthcare stocks.

## Universe
- XLV

## Data Sources
- Labor jobs weekly healthcare sector job postings and Yahoo Finance weekly XLV prices

## Signal Logic
Enter long XLV when healthcare job postings increase more than 7% week-over-week and XLV outperforms SPY that week

## Entry / Exit
Entry: Enter long XLV when healthcare job postings increase more than 7% week-over-week and XLV outperforms SPY that week Exit: Exit after 4 weeks or when job postings growth falls below 3% week-over-week

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Labor jobs weekly healthcare sector job postings and Yahoo Finance weekly XLV prices via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Healthcare jobs data update weekly with frequent visible accelerations.

## Required Keys
- None
