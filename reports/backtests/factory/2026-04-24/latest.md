# Professional Backtest V1

- Run date: 2026-04-24
- Window: 2024-01-01 to 2026-04-24
- Slippage: 5.0 bps per trade
- Method: signal after close, execute next trading day open, long/cash only, SPY benchmark.

## Counts

- BACKTEST_FAIL: 1
- LIVE_ONLY_NON_PRICE: 17

## Results

| Algo | Family | Status | Alpha vs SPY | Trades | Reason |
| --- | --- | --- | ---: | ---: | --- |
| Bank Stress Index Volatility Fear Crush Reversal | crazy | BACKTEST_FAIL | -54.44 | 54 | Backtest completed |
| Daily Spike In Daily Earthquake Activity Near Major Logistics Hubs Signals Bearish Xli | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.earthquake_activity |
| Daily Spike In Freight Logistics Rss News Volume Mentioning Port Labor Strike Triggers Bearish Xli | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Daily Spike In Rss Counts For Cybersecurity Breach News Triggers Bearish Xlk | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Daily Spike In Rss News Counts Around Labor Union Contract Negotiation Signals Bearish Xlf | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Daily Spike In Rss News Counts Mentioning Politician Insider Buying Tech Stock Signals Bullish Xlk | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.rss_count |
| Ev Charger Network Expansion Sprint Demand Surge | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.openchargemap |
| Temperature Extremes Power Demand Spike Utility Boost | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.eia_electricity |
| Weekly Increase In Google Trends Searches For Bulk Shipping Delay Signals Bearish Xlb | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Rise In Google Trends Interest For Food Delivery Delay Signals Bearish Xlp | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Rise In Google Trends Searches For Gas Price Protest Signals Bearish Xle | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Spike In Google Trends For Home Cooling Failure Signals Bearish Xlu | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Spike In Google Trends Searches For Warehouse Automation Failure Signals Bearish Xli | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Surge In Google Trends Searches For City Water Outage Signals Bearish Xlre | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Surge In Google Trends Searches For Commuting Strike Signals Bearish Xly | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Surge In Google Trends Searches For Diy Electronics Repair Signals Bullish Xlk | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Surge In Google Trends Searches For Home Improvement Loan Signals Consumer Stress Lifting Xly | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.google_trends |
| Weekly Surge In Job Postings For Warehouse Workers Signals Bullish Xli | crazy | LIVE_ONLY_NON_PRICE |  |  | Uses non-price adapter: crazy.adapters.rss_count |

This is experimental research, not investment advice. Past performance does not predict future results.
