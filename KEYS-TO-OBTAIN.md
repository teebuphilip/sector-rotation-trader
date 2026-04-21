# KEYS-TO-OBTAIN.md

API keys needed to unlock blocked algos and the Polygon.io swap.
Add each key as a GitHub Actions secret in both repos (sector-rotation-trader + AFH).

---

## POLYGON_API_KEY
**Used by:** `scanner_polygon.py`, `precompute_signals_poly.py` (Week 3 yfinance swap)
**Get it:** https://polygon.io — free tier, no credit card, sign up with email
**Tier needed:** Free (Starter) — 15-min delayed data, unlimited API calls
**Note:** Free tier is sufficient; pipeline runs at 6:30 PM ET, market closes at 4 PM

---

## YELP_API_KEY
**Used by:** `crazy/algos/yelp_closure_velocity.py`
**Get it:** https://www.yelp.com/developers/v3/manage_app — create app, grab "API Key"
**Tier needed:** Free — 500 calls/day on free plan
**Note:** Yelp has been restricting new app approvals. If denied, algo stays BLOCKED.

---

## OPENCHARGEMAP_API_KEY
**Used by:** `crazy/adapters/openchargemap.py`
**Get it:** https://openchargemap.org/site/develop/api — register, request API key
**Tier needed:** Free
**Note:** No-key mode returns limited data; key unlocks full global POI dataset

---

## PREMIUM_SECRET
**Used by:** `scripts/generate_premium_token.py`, `scripts/build_public_pages.py`
**Get it:** Generate locally — `python -c "import secrets; print(secrets.token_hex(32))"`
**Tier needed:** N/A — self-generated
**Note:** Used to HMAC-sign monthly premium access tokens for the public site paywall

---

## Dead / Postponed

| Key | Reason |
|-----|--------|
| `TWITTER_BEARER_TOKEN` | Free tier killed Jan 2023; $100/month for Basic. Algos POSTPONED. |
| `GLASSDOOR_API_KEY` | API completely shut down ~2022. Algo needs scraper rewrite. POSTPONED. |
| `REDDIT_CLIENT_ID` / `REDDIT_CLIENT_SECRET` | Free but rate-limited. Already wired in if algo is active. |

---

## Where to add secrets (GitHub)

1. Go to repo → **Settings → Secrets and variables → Actions**
2. Click **New repository secret**
3. Name must match exactly (all caps, underscores)
4. For AFH repo: repeat for any shared keys (POLYGON_API_KEY, PREMIUM_SECRET)
