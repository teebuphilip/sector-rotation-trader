# Labor Jobs Weekly Surge In Healthcare Job Postings Signals Biotech Sector Strength

**Idea ID:** `labor-jobs-weekly-surge-in-healthcare-job-postings-signals-b`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising healthcare job postings often precede earnings strength and sector outperformance. Healthcare job growth signals innovation and capacity expansion.

## Universe
- XLV

## Data Sources
- FRED series or public job posting scrapes for healthcare sector

## Signal Logic
Enter long XLV if weekly healthcare job postings rise >15% above 5-week average

## Entry / Exit
Entry: Enter long XLV if weekly healthcare job postings rise >15% above 5-week average Exit: Exit after 5 weeks or if job postings decline below 10% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED series or public job posting scrapes for healthcare sector via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Healthcare job posting data reacts quickly to industry hiring cycles.

## Required Keys
- None
