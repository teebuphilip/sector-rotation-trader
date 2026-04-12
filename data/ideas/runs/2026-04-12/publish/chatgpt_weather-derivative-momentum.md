# Weather Derivative Momentum

**Idea ID:** `weather-derivative-momentum`
**Source:** openai / gpt-4.1-mini
**Frequency:** daily

## Thesis
Sudden sustained changes in local extreme weather event frequencies (e.g., heatwaves or cold snaps) often impact utility and agriculture-related stocks with a lag of 1-3 weeks. By tracking daily counts of extreme weather alerts aggregated by region and correlating them to affected company headquarters locations, one can generate momentum signals ahead of earnings or operational impacts. This approach exploits short-term weather-driven demand shocks not yet priced into equities.

## Universe
- NEE
- DUK
- EXC
- ADM
- Bunge Limited (BG)
- Corteva (CTVA)

## Data Sources
- NOAA Storm Events Database (https://www.ncdc.noaa.gov/stormevents/)
- NWS Weather Alerts RSS feeds
- Company headquarters location data from public sources (e.g., Wikipedia, SEC filings)

## Signal Logic
Calculate a 7-day rolling count of extreme weather alerts (heatwaves, cold waves, floods) per county. Identify counties with a +50% increase relative to the previous 7-day period. Map companies with HQ or major facilities in these counties. Generate a bullish signal if alerts spike for heatwaves impacting utilities or agriculture-related companies, bearish if cold snaps or floods increase sharply.

## Entry / Exit
Buy companies mapped to counties with +50% heatwave alert increase sustained for 3 consecutive days. Exit when alert counts return to baseline or after 21 days. Sell/short companies exposed to increased cold snap or flood alerts under the same duration and thresholds.

## Position Sizing
Allocate 2% of portfolio per signal, max 10% total exposure to weather-driven signals to limit cluster risk.

## Risks
Weather alerts may be noisy or misclassified; companies might have diversified operations reducing local weather impact; lag between weather event and stock reaction may vary; false positives during overlapping weather events; structural changes in weather patterns may change correlations.

## Implementation Notes
1) Download and parse daily NOAA storm events data. 2) Aggregate alerts by county and event type. 3) Calculate rolling window changes and detect spikes. 4) Map companies to counties using HQ/facility location data. 5) Generate signals and backtest. 6) Automate daily data refresh and signal generation.

## Required Keys
- None
