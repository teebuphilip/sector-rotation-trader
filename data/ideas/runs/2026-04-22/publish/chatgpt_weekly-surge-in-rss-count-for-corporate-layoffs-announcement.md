# Weekly Surge In Rss Count For Corporate Layoffs Announcements

**Idea ID:** `weekly-surge-in-rss-count-for-corporate-layoffs-announcement`
**Family:** `attention_sentiment`
**Source:** openai / gpt-4.1-mini
**Frequency:** weekly

## Thesis
Spike in corporate layoff news volume signals worsening labor conditions and reduced consumer confidence. Financial sector sensitive to economic downturns and credit risk from labor market stress.

## Universe
- XLF

## Data Sources
- RSS feed counts for 'layoffs' keyword aggregated weekly

## Signal Logic
Enter short XLF when weekly layoff-related RSS count rises >50% above 8-week average

## Entry / Exit
Entry: Enter short XLF when weekly layoff-related RSS count rises >50% above 8-week average Exit: Exit after 3 weeks or when count drops below 20% above average

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use RSS feed counts for 'layoffs' keyword aggregated weekly via scrape (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 18
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Layoff news clusters occur frequently, especially in cyclical downturns.

## Required Keys
- None
