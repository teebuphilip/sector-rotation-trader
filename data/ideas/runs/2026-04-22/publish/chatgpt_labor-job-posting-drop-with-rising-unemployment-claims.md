# Labor Job Posting Drop With Rising Unemployment Claims

**Idea ID:** `labor-job-posting-drop-with-rising-unemployment-claims`
**Family:** `labor_jobs`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
A simultaneous drop in job postings and rise in unemployment claims signals labor demand weakening rapidly. Financial sector sensitive to labor market stress and potential credit risks.

## Universe
- XLF

## Data Sources
- FRED weekly unemployment claims and job postings data

## Signal Logic
Enter short XLF when job postings drop 5% WoW and unemployment claims rise 3% WoW

## Entry / Exit
Entry: Enter short XLF when job postings drop 5% WoW and unemployment claims rise 3% WoW Exit: Exit after 4 weeks or if either metric reverses by 2%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use FRED weekly unemployment claims and job postings data via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Weekly labor data commonly shows small but meaningful opposite moves during slowdowns.

## Required Keys
- None
