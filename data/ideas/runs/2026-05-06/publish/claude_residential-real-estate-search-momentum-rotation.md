# Residential Real Estate Search Momentum Rotation

**Idea ID:** `residential-real-estate-search-momentum-rotation`
**Family:** `local_economy_weirdness`
**Source:** anthropic / claude-haiku-4-5-20251001
**Frequency:** weekly

## Thesis
When search momentum shifts from rentals to home purchases (purchase searches rise 25%+ relative to rental searches over 2 weeks), real estate sentiment turns bullish, benefiting REITs and home builders within 10-15 days. Mortgage and purchase search surges reflect consumer confidence in home equity and signal REIT and homebuilder demand cycles.

## Universe
- XLRE

## Data Sources
- Google Trends weekly searches for 'home for sale near me' + 'rental apartment listings' + 'mortgage calculator' through google_trends adapter

## Signal Logic
If home purchase search index rises 25%+ relative to rental search index over 2 weeks, enter long XLRE on Friday close

## Entry / Exit
Entry: If home purchase search index rises 25%+ relative to rental search index over 2 weeks, enter long XLRE on Friday close Exit: Exit after 12 trading days or if relative momentum drops below 10%

## Position Sizing
Allocate 5% per signal, max 20% total exposure.

## Risks
Data source instability, false positives, and regime shifts.

## Implementation Notes
Use Google Trends weekly searches for 'home for sale near me' + 'rental apartment listings' + 'mortgage calculator' through google_trends adapter via api (weekly).

## High Action Metadata
- Expected Fire Rate: weekly
- Historical Backfill: True
- Minimum History Months: 12
- Adapter Status: existing
- Trigger Sensitivity: high
- Why It Should Fire Soon: Real estate search rotation is seasonal; spring/fall buying seasons and rate cut cycles trigger 25%+ relative swings every 6-8 weeks.

## Required Keys
- None
