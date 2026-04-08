# Online Ad Impression Volatility Trader

**Idea ID:** `online-ad-impression-volatility`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
Online ad impressions can be volatile due to user behavior and campaign changes. By tracking real-time changes in ad impressions, we can identify opportunities to profit from this volatility.

## Universe
- GOOG
- FB
- TWTR
- SNAP
- PINS

## Data Sources
- Google Trends
- Twitter API
- Facebook Ad Library API

## Signal Logic
Monitor daily changes in ad impressions for a basket of popular websites and social media platforms. Look for volatility spikes above 10% from the prior day's volume.

## Entry / Exit
Buy when daily impression volume jumps more than 10%, sell when it reverts back to normal levels within 3 days.

## Position Sizing
Size positions based on the magnitude of the impression spike, with larger positions for 20%+ changes.

## Risks
Impression volatility may not always translate to stock price movements. Data quality and timeliness from APIs can be inconsistent.

## Implementation Notes
Retrieve daily ad impression data, calculate volatility, and generate trading signals. May need to handle API rate limiting and process large data volumes.

## Required Keys
- Google Trends API key
- Twitter API key
- Facebook Ad Library API key
