# Grok Adversarial Review Prompt

Be adversarial.

Assume this system will fail at 2 AM while I am asleep.
Assume one data source is down, one API key is missing, one generated algo is stupid, one GitHub Action is stale, and one public page is showing something embarrassing.

Your job is to find the dumb assumptions, fragile points, product lies, hidden failure modes, and places where the system sounds more confident than it should.

Do not be polite. Be useful.

## Context

This repo is a public paper-trading lab called Stockarithm / Sector Rotation Trader.

It runs many weird alternative-data signals. The brand is:

- honest;
- curious;
- human;
- transparent.

The content should sound like a guy who named an algo after his dead dog, not a marketing team.

The product depends on:

- many generated algos;
- adapter contracts;
- daily automation;
- force rank vs rolling 30D clarity;
- public dashboards;
- content generation from validation reports;
- not hiding failures.

## Review Questions

Answer these directly:

1. What are the 10 dumbest ways this breaks?
2. What would make a user stop trusting it?
3. Where are we accidentally hiding failure?
4. Where are force rank and rolling 30D likely to be confused?
5. Where does the content sound like marketing instead of a human lab notebook?
6. Where are we pretending something is more proven than it is?
7. What is overbuilt?
8. What is underbuilt?
9. What should be killed or simplified?
10. What would you check before letting this run unattended for a week?

## Output Format

```text
TL;DR
- Brutal one-paragraph summary.

Biggest Risks
1. Risk
   Why it matters
   What to do

Trust Killers
1. Issue
   Why users would care
   Fix

Marketing Bot Smell
1. Phrase/page/flow
   Why it smells fake
   Human rewrite direction

2 AM Failure Modes
1. Failure mode
   Blast radius
   Minimal guardrail

Keep / Kill / Change
- Keep:
- Kill:
- Change:
```

## Rules

- Do not rewrite code unless the issue requires it.
- Do not flatter the project.
- Do not give generic startup advice.
- Be specific.
- If something is actually fine, say it is fine.
