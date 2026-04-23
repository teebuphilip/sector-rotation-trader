# Labor Jobs Report Weekly Spike In Temp Job Postings Signals Short-term Xly Weakness

**Idea ID:** `labor-jobs-report-weekly-spike-in-temp-job-postings-signals-`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A sudden surge in temporary job postings often indicates companies preparing for economic uncertainty or layoffs, leading to consumer caution. Temporary job growth spikes reflect labor market caution that can depress discretionary spending.

## Universe
- XLY

## Data Sources
- Indeed temp job postings weekly count

## Signal Logic
Enter short XLY when temp job postings increase 20%+ over prior 2 weeks

## Entry / Exit
Entry: Enter short XLY when temp job postings increase 20%+ over prior 2 weeks Exit: Exit after 3 weeks or when postings revert below 10% increase

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Indeed temp job postings weekly count via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weekly labor job postings regularly show sudden temp job surges around seasonal and business cycle events.

## Required Keys
- None
