# Professional Backtest V1

- Run date: 2026-05-08
- Window: 2024-01-01 to 2026-05-08
- Slippage: 5.0 bps per trade
- Method: signal after close, execute next trading day open, long/cash only, SPY benchmark.

## Counts

- INSUFFICIENT_ACTIVITY: 1
- LIVE_ONLY_NON_PRICE: 12

## Results

| Algo | Family | Status | Alpha vs SPY | Trades | Reason |
| --- | --- | --- | ---: | ---: | --- |
| Daily Jump In Consumer Stress Google Trends Searches For Car Repossession Signals Rising Financial Distress | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Jump In Google Trends Searches For Electric Vehicle Battery Failure Signals Consumer Tech Stress | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Jump In Rss News Counts Mentioning Labor Strike Signals Imminent Industrial Disruption | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Daily Spike In Google Trends Searches For Emergency Plumber Signals Consumer Home Repair Stress | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Daily Spike In Google Trends Searches For Home Heating System Failure Signals Winter Utility Stress | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Natural Gas Futures Volatility Pump Rotation | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.eia_electricity |
| Regional Earthquake Cluster Insurance Demand Spike | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.earthquake_activity |
| Utility Volatility Compression Reversion Bounce | crazy | INSUFFICIENT_ACTIVITY | -59.04 | 0 | Backtest completed |
| Weekly Increase In Google Trends Searches For Small Business Loan Default Signals Rising Credit Stress | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Increase In Usgs Earthquake Activity Within Key Logistics Hubs Signals Potential Freight Delays | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.earthquake_activity |
| Weekly Jump In Google Trends Searches For Airport Security Delay Signals Travel Mobility Disruptions | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Surge In Google Trends Searches For Truck Driver Strike Signals Imminent Logistics Disruption | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Surge In Google Trends Searches For Warehouse Worker Shortage Signals Labor Tightness | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |

This is experimental research, not investment advice. Past performance does not predict future results.
