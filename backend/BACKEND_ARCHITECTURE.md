# Stockarithm Premium Backend Architecture

## Purpose

The Stockarithm backend is a deliberately small paid-access service. It is not the main trading engine. The main system remains the nightly Python/GitHub Actions artifact pipeline. The backend exists only to answer this question:

> Is this browser allowed to read premium artifacts right now?

Everything else should stay static or artifact-based unless there is a concrete reason to make it dynamic.

## Current System Boundary

Stockarithm has two different "backend" layers:

1. Nightly artifact backend
2. Premium entitlement/API backend

The nightly artifact backend already exists:

```text
GitHub Actions
  -> Python trading/idea/product scripts
  -> data/product/*.json
  -> docs/data/public/*.json
  -> docs/*.html
  -> GitHub Pages
```

The premium backend is the new small dynamic layer:

```text
Stripe Checkout/Webhooks
  -> Railway FastAPI service
  -> entitlement JSON store
  -> signed HTTP-only cookie
  -> premium JSON/CSV endpoints
  -> docs/app.html frontend
```

The key architectural rule is simple: the dynamic backend should not become the trading engine. It should serve artifacts created elsewhere.

## Why This Exists

GitHub Pages is excellent for the free/public product:

- static HTML
- public JSON
- no server cost
- easy caching
- low operational risk
- no account system

But GitHub Pages cannot safely serve paid/private data because any file in `docs/` is public. Premium needs:

- payment verification
- subscription entitlement
- session cookie
- protected API endpoints
- CSV downloads behind entitlement
- future private artifact storage

That is why the backend exists.

## Why No Auth0

Auth0 is intentionally not part of this design.

Stockarithm does not need, at launch:

- passwords
- username/password login
- social login
- MFA
- enterprise SSO
- teams/orgs
- role-based access control
- user profile management
- account recovery flows
- identity lifecycle tooling

Stockarithm needs:

- did this email pay?
- is this subscription active?
- can this browser access premium JSON today?

Stripe is already the source of truth for payment. Adding Auth0 would create another control plane, another dashboard, another integration surface, and another failure mode without solving the actual launch problem.

Current approach:

```text
Stripe says paid
  -> Stockarithm stores entitlement
  -> Stockarithm sets signed cookie
  -> API checks signed cookie + entitlement
```

This is enough for the July launch path. If Stockarithm later needs teams, SSO, MFA, or rich account management, then Auth0/Clerk/Supabase Auth can be revisited.

## Source Files

Backend service:

- `backend/stockarithm_api.py`

Backend setup notes:

- `backend/README.md`

Premium static frontend shell:

- `docs/app.html`

Runtime stores, ignored by git:

- `data/premium/entitlements.json`
- `data/premium/stripe_events.json`
- `private_artifacts/`

Dependencies:

- `fastapi`
- `uvicorn[standard]`
- `requests`

## Deployment Target

The intended deployment target is Railway.

Railway runs the FastAPI app as a normal Python web service. The public static site remains on GitHub Pages.

Expected public domains:

```text
https://stockarithm.com          -> GitHub Pages static site
https://api.stockarithm.com      -> Railway FastAPI backend
```

Local development can run the API on port `8080`:

```bash
uvicorn backend.stockarithm_api:app --reload --port 8080
```

## Environment Variables

Required for real Stripe test-mode flow:

```bash
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
JWT_SECRET=<random-long-secret>
APP_URL=https://stockarithm.com/app.html
CORS_ORIGINS=https://stockarithm.com,http://localhost:8000,http://127.0.0.1:8000
```

Production-ish cookie/domain settings:

```bash
COOKIE_DOMAIN=.stockarithm.com
COOKIE_SECURE=true
SESSION_COOKIE=stockarithm_session
SESSION_TTL_SECONDS=2678400
```

Artifact/store settings:

```bash
PUBLIC_ARTIFACT_DIR=docs/data/public
PRIVATE_ARTIFACT_DIR=private_artifacts
ENTITLEMENTS_PATH=data/premium/entitlements.json
PROCESSED_EVENTS_PATH=data/premium/stripe_events.json
```

Defaults are chosen so the service can run locally from repo root before private artifact publishing exists.

## Runtime Data Model

### Entitlements

File:

```text
data/premium/entitlements.json
```

Shape:

```json
{
  "updated_at": "2026-04-23T13:00:00Z",
  "emails": {
    "user@example.com": {
      "email": "user@example.com",
      "customer_id": "cus_...",
      "subscription_id": "sub_...",
      "active": true,
      "tier": "premium",
      "source": "stripe_checkout",
      "updated_at": "2026-04-23T13:00:00Z"
    }
  },
  "customers": {
    "cus_...": "user@example.com"
  }
}
```

This is intentionally simple. Railway filesystem is acceptable for test mode and earliest launch validation. Long-term, this should move to Postgres, Redis, or another persistent store if Railway filesystem persistence is not acceptable.

### Processed Stripe Events

File:

```text
data/premium/stripe_events.json
```

Shape:

```json
{
  "updated_at": "2026-04-23T13:00:00Z",
  "events": ["evt_..."]
}
```

This prevents webhook replay from double-processing events. It is not meant to be an infinite audit log; the implementation keeps a bounded list.

### Session Cookie

Cookie name:

```text
stockarithm_session
```

Cookie properties:

- signed JWT-style token
- `HttpOnly`
- `Secure` unless disabled locally
- `SameSite=Lax`
- path `/`
- default TTL 31 days

Payload:

```json
{
  "sub": "user@example.com",
  "email": "user@example.com",
  "tier": "premium",
  "iat": 1776949200,
  "exp": 1779627600
}
```

The cookie alone is not enough. Premium endpoints verify both:

1. token signature/expiry
2. active entitlement in the entitlement store

That means a canceled subscription can be blocked even before the cookie expires.

## Stripe Test-Mode Flow

The backend is designed to be built and verified entirely with Stripe test mode first.

### Checkout Completion Flow

```text
User completes Stripe Checkout test session
  -> Stripe redirects user to /unlock?session_id=cs_test_...
  -> backend calls Stripe API to verify Checkout Session
  -> backend extracts customer email
  -> backend stores active entitlement
  -> backend creates signed cookie
  -> backend redirects to APP_URL
  -> docs/app.html checks /api/me/status
  -> app loads premium endpoints if entitled
```

### Webhook Flow

```text
Stripe sends POST /webhook
  -> backend verifies Stripe-Signature header
  -> backend checks processed event IDs
  -> backend handles event type
  -> backend updates entitlement store
  -> backend records event ID
  -> backend returns 200
```

Handled events:

- `checkout.session.completed`
- `customer.subscription.deleted`
- `customer.subscription.paused`
- `customer.subscription.updated`
- `invoice.paid`

The webhook path matters because users can cancel, pause, or update subscriptions outside the app.

## Endpoint Contract

### `GET /health`

Purpose: Railway health check and smoke test.

Returns:

```json
{
  "ok": true,
  "service": "stockarithm-premium-api",
  "time": "2026-04-23T13:00:00Z"
}
```

### `GET /unlock?session_id=...`

Purpose: turn a completed Stripe Checkout Session into a browser session.

Steps:

1. Look up Checkout Session from Stripe using `STRIPE_SECRET_KEY`.
2. Verify session is complete/paid enough for entitlement.
3. Extract customer email.
4. Store entitlement.
5. Set `stockarithm_session` cookie.
6. Redirect to `APP_URL`.

Failure cases:

- missing Stripe config -> `500`
- invalid session -> `400`
- incomplete checkout -> `402`
- missing email -> `400`

### `POST /webhook`

Purpose: receive Stripe lifecycle events.

Security:

- requires valid `Stripe-Signature`
- verifies HMAC against `STRIPE_WEBHOOK_SECRET`
- records event IDs to avoid replay/double-processing

### `GET /api/me/status`

Purpose: frontend entitlement check.

Unauthenticated response:

```json
{
  "authenticated": false,
  "entitled": false,
  "tier": "free"
}
```

Authenticated entitled response:

```json
{
  "authenticated": true,
  "entitled": true,
  "tier": "premium",
  "email": "user@example.com"
}
```

### `POST /logout`

Purpose: clear the session cookie.

### `GET /api/premium/leaderboard`

Purpose: premium leaderboard payload.

Auth:

- requires valid signed cookie
- requires active entitlement

Artifact lookup:

1. `PRIVATE_ARTIFACT_DIR/leaderboard.json`
2. fallback `PUBLIC_ARTIFACT_DIR/leaderboard.json`

The public fallback exists only so the backend can be tested before private publishing exists.

### `GET /api/premium/signal/{algo_id}`

Purpose: per-algo detail.

Current behavior:

- finds algo in leaderboard
- reads matching state file from `data/<algo_type>/state/<algo_id>.json`
- returns algo row plus state

This is staged, not final. Long-term this should read from private artifacts instead of raw repo state files.

### `GET /api/premium/ticker/{symbol}`

Purpose: premium ticker detail.

Current behavior:

- reads full `docs/signals/<SYMBOL>.json` if available
- falls back to public signal payload

This is also staged. Long-term this should read from private artifact storage.

### `GET /api/premium/download/{kind}`

Supported `kind` values:

- `algo_performance`
- `signals_today`
- `trade_history`

All are gated behind entitlement.

Current sources:

- `algo_performance`: leaderboard artifact
- `signals_today`: signal index artifact
- `trade_history`: state files under `data/normal/state` and `data/crazy/state`

This is enough to test the endpoint surface. Final paid launch should use explicit private CSV artifacts generated nightly.

## Artifact Strategy

The backend should not calculate performance live. It should read artifacts.

Current staged order:

```text
PRIVATE_ARTIFACT_DIR/<file>
  -> if missing, fallback to docs/data/public/<file>
```

Final desired order:

```text
Nightly pipeline
  -> publish_public.py writes stripped public artifacts
  -> publish_private.py writes full private artifacts
  -> Railway serves private artifacts only to entitled users
```

Private artifacts should eventually include:

- full leaderboard
- per-algo detail
- per-ticker detail
- trade history
- equity curves
- CSV downloads
- comparator grading details

Public artifacts should never contain those full internals.

## Security Model

Security goal:

> Keep casual users and crawlers away from premium data. Do not overbuild enterprise identity before revenue proves it matters.

Current controls:

- premium data served only through Railway API
- API checks signed cookie
- API checks active entitlement store
- Stripe webhooks verify HMAC signature
- Stripe event IDs are replay-guarded
- runtime entitlement/private files are gitignored
- public static site remains separate from premium API

Known limitations:

- file-backed entitlements are not a durable production database
- no rate limiting yet
- no admin dashboard
- no audit UI
- no customer portal integration yet
- private artifact publisher is not built yet
- raw state file access is acceptable for staging but should be replaced with private artifacts before real paid launch

## CORS And Cookies

The static frontend and API run on different hostnames:

```text
stockarithm.com
api.stockarithm.com
```

That requires:

- `CORS_ORIGINS` includes `https://stockarithm.com`
- frontend fetches with `credentials: "include"`
- backend CORS allows credentials
- cookie domain should be `.stockarithm.com` in production
- cookie must be `Secure` in production

`docs/app.html` defaults API base to:

```text
https://api.stockarithm.com
```

For local testing, override in browser console:

```js
localStorage.setItem('stockarithm_api_base', 'http://localhost:8080')
```

## Local Testing Plan

Basic server check:

```bash
uvicorn backend.stockarithm_api:app --reload --port 8080
curl http://localhost:8080/health
```

Frontend local API override:

```js
localStorage.setItem('stockarithm_api_base', 'http://localhost:8080')
```

Manual entitlement-only smoke test can be done by temporarily writing an entitlement JSON and minting a cookie through `/unlock` once Stripe test checkout exists. Do not hand-edit entitlements for production.

Stripe test-mode validation:

1. Create Stripe test product/price.
2. Configure Checkout success URL to `https://api.stockarithm.com/unlock?session_id={CHECKOUT_SESSION_ID}`.
3. Configure webhook endpoint to `https://api.stockarithm.com/webhook`.
4. Set Railway env vars.
5. Complete checkout with Stripe test card.
6. Confirm cookie is set.
7. Confirm `/api/me/status` returns entitled.
8. Confirm `docs/app.html` renders the premium leaderboard.
9. Cancel subscription in Stripe test mode.
10. Confirm entitlement is removed by webhook and premium API returns `403`.

## Railway Deployment Plan

1. Create Railway service from repo.
2. Set start command:

```bash
uvicorn backend.stockarithm_api:app --host 0.0.0.0 --port $PORT
```

3. Set env vars:

```bash
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
JWT_SECRET=...
APP_URL=https://stockarithm.com/app.html
CORS_ORIGINS=https://stockarithm.com
COOKIE_DOMAIN=.stockarithm.com
COOKIE_SECURE=true
```

4. Add custom domain:

```text
api.stockarithm.com
```

5. Point DNS to Railway target.
6. Add Stripe test webhook to `https://api.stockarithm.com/webhook`.
7. Run end-to-end test checkout.

## What Is Staged vs Done

Staged now:

- FastAPI service
- Stripe webhook handler
- Stripe Checkout unlock path
- signed cookie sessions
- entitlement store
- premium endpoints
- CSV endpoints
- static `docs/app.html`

Not done yet:

- Railway deploy
- Stripe test product/price/session wiring
- Stripe webhook endpoint in dashboard
- private artifact publisher
- production durable entitlement DB
- customer portal cancel link
- rate limiting
- full end-to-end paid checkout test

## Failure Modes To Watch

Most likely issues:

- cookie domain wrong (`stockarithm.com` vs `.stockarithm.com`)
- CORS missing credentials
- Stripe success URL missing `{CHECKOUT_SESSION_ID}`
- webhook secret from wrong Stripe endpoint/mode
- Railway filesystem persistence assumptions wrong
- private artifacts missing, causing public fallback to hide gaps
- browser blocks insecure cookies in local HTTP testing unless `COOKIE_SECURE=false`

## Design Principle

Do not turn this into a SaaS platform before the first subscriber.

The correct architecture for launch is:

```text
Static public proof layer
  + Stripe as payment truth
  + tiny entitlement API
  + private artifacts
```

That is enough to charge, test demand, and avoid premature identity/vendor complexity.
