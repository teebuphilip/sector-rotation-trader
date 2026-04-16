# Code Review Prompts

Use these prompts as an external review board for the repo.

The split is intentional:

- Gemini: primary code reviewer for runtime bugs, contracts, pipelines, and CI breakage.
- Grok: adversarial reviewer for dumb assumptions, fragile architecture, product/voice weirdness, and "what breaks at 2 AM?" checks.
- Perplexity: source-backed reviewer for APIs, external data sources, rate limits, docs, pricing, and provider reality checks.

Recommended cadence:

- After any meaningful pipeline/code change: run Gemini.
- Before adding a new adapter/data source: run Perplexity.
- Before a launch, workflow change, or public-facing product decision: run Grok.
- Weekly Sunday review: run all three, then reconcile findings manually.

Do not ask these tools to rewrite the repo by default. Ask for findings first.

Review rule:

```text
Find bugs before suggesting architecture rewrites.
```
