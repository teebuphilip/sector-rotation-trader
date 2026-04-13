# Coffee Shop WiFi Usage

**Idea ID:** `coffee-shop-wifi-usage`
**Source:** anthropic / claude-3-haiku-20240307
**Frequency:** daily

## Thesis
The relative number of people using WiFi at popular coffee shop chains can signal changes in foot traffic and consumer spending in those areas.

## Universe
- SBUX
- DNKN
- PEET
- BJRI

## Data Sources
- Foursquare location data
- Public WiFi usage statistics

## Signal Logic
Monitor the relative WiFi usage at major coffee shop chains in different neighborhoods. Look for changes in usage that deviate from seasonal norms or the average across all locations.

## Entry / Exit
Buy when WiFi usage at a location increases significantly above the chain average. Sell when usage returns to normal levels.

## Position Sizing
Allocate a small percentage of the portfolio (e.g., 2-5%) to each coffee shop location trade, diversifying across multiple chains and neighborhoods.

## Risks
Foot traffic and WiFi usage can be affected by factors beyond just consumer spending, like weather, local events, or network outages. Liquidity may be low for smaller coffee shop chains.

## Implementation Notes
Collect Foursquare location data and public WiFi usage statistics. Analyze trends in relative usage across locations to generate buy/sell signals. Monitor for anomalies and adjust thresholds accordingly.

## Required Keys
- Foursquare API
