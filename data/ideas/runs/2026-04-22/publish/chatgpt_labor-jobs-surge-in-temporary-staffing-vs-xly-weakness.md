# Labor Jobs Surge In Temporary Staffing Vs Xly Weakness

**Idea ID:** `labor-jobs-surge-in-temporary-staffing-vs-xly-weakness`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Rising temporary job postings while consumer discretionary ETF lags indicates cautious hiring and consumer spending uncertainty. Temporary hiring surges often precede mixed consumer discretionary performance due to consumer caution.

## Universe
- XLY

## Data Sources
- Weekly temporary staffing job postings data

## Signal Logic
Enter short XLY if temporary staffing postings rise 10% WoW and XLY price down 2% WoW

## Entry / Exit
Entry: Enter short XLY if temporary staffing postings rise 10% WoW and XLY price down 2% WoW Exit: Exit after temporary staffing postings normalize or XLY recovers 3% WoW

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Weekly temporary staffing job postings data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 24
- Adapter Status: existing
- Trigger Sensitivity: medium
- Why It Should Fire Soon: Temporary staffing data updates weekly and can spike with economic uncertainty multiple times yearly.

## Required Keys
- None
