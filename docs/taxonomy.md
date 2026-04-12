# Crazy Algo Taxonomy

Purpose: Provide a validated taxonomy of existing crazy algos with concrete examples. This is the reference catalog for future auto‑generated algos and prompt scaffolding.

## Categories

1. **Alt Data: Public Infrastructure / Foot Traffic**
   - **TSA Body Count** (`crazy/algos/tsa.py`)
     - Data: TSA passenger volumes (public web table)
     - Signal: YoY acceleration (risk‑on / risk‑off)
     - Pattern: Web scrape + cached JSON + rolling math
   - **311 Call Rotation** (`crazy/algos/calls311.py`)
     - Data: City 311 calls (Socrata API)
     - Signal: Complaint volume trend
     - Pattern: API + cached JSON + rolling comparisons

2. **Alt Data: Labor / Jobs Sentiment**
   - **LinkedIn Layoff Propagation** (`crazy/algos/linkedin.py`)
     - Data: News/feeds (web scrape)
     - Signal: Layoff mentions trend
     - Pattern: Web scrape + rolling trend filter
   - **Glassdoor Misery Gradient** (`crazy/algos/glassdoor.py`)
     - Data: Employee reviews (web scrape)
     - Signal: Sentiment decline / stress proxy
     - Pattern: Scrape + cache + threshold
   - **Craigslist Desperation Index** (`crazy/algos/craigslist.py`)
     - Data: Craigslist job posts (scrape)
     - Signal: Desperation keywords trend
     - Pattern: Scrape + keyword count + rolling compare

3. **Alt Data: Consumer / Retail Proxy**
   - **Cardboard Box Index** (`crazy/algos/cardboard.py`)
     - Data: Packaging demand proxy (industry data)
     - Signal: Growth vs decline thresholds
     - Pattern: API / feed + cached time series
   - **Liquor Store Leading Indicator** (`crazy/algos/liquor.py`)
     - Data: FRED retail series
     - Signal: 3‑month pct change
     - Pattern: FRED API + threshold

4. **Alt Data: Political / Institutional**
   - **Congress Trading Fade** (`crazy/algos/congress.py`)
     - Data: Congress trade disclosures
     - Signal: Fade net buying / selling
     - Pattern: API + lag + contrarian allocation

5. **Behavioral / Market Mechanics**
   - **Algo Biscotti (Unconditional Loyalty)** (`crazy/algos/biscotti.py`)
     - Data: Price only
     - Signal: Worst 30‑day sector → contrarian buy
     - Pattern: Price ranking + monthly rotation
   - **Algo Baileymol (Chaos Monger)** (`crazy/algos/bailey.py`)
     - Data: Price volatility
     - Signal: Top 3 vol sectors weekly
     - Pattern: Vol ranking + weekly rotation

6. **Social / Community Sentiment**
   - **Reddit Gaming Thread Spike** (`crazy/algos/reddit_gaming_thread_spike.py`)
     - Data: Reddit activity (posts + comments)
     - Signal: Daily spike vs 7‑day average
     - Pattern: API + daily aggregation + spike threshold

## Valid Implementation Patterns (By Type)

### A) Web Scrape + Cache + Rolling Metric
- Use: `cached_fetch(cache_path, ttl_hours, fetch_fn)`
- Example: `crazy/algos/tsa.py`
- Steps:
  1. Fetch HTML
  2. Parse table → DataFrame
  3. Compute rolling metric
  4. Emit signal string

### B) API + Cache + Threshold
- Use: `cached_fetch` + API client
- Example: `crazy/algos/liquor.py`
- Steps:
  1. Read API key via `os.getenv`
  2. Call API
  3. Compute % change
  4. Compare threshold

### C) Price Ranking / Rotation
- Use: Yahoo price download via `scanner.safe_download`
- Example: `crazy/algos/biscotti.py`
- Steps:
  1. Load recent prices
  2. Rank returns or volatility
  3. Select top / bottom
  4. Map to allocations

### D) Social Activity Spike
- Use: API + daily aggregation
- Example: `crazy/algos/reddit_gaming_thread_spike.py`
- Steps:
  1. Collect daily posts/comments
  2. Build 7‑day MA
  3. Trigger on spike
  4. Exit after hold window

## Prompt Guidance (For Auto‑Generation)

- Always choose a pattern above.
- Use only repo‑existing helpers.
- No placeholder stubs.
- If API keys are missing: `record_blocked(...)` and return `HOLD`.

