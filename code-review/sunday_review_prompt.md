# Sunday Full Review Prompt

Use this when doing the weekly Sunday review.

Run Gemini, Grok, and Perplexity separately with their dedicated prompts first. Then use this prompt to reconcile the findings.

## Input

Paste:

- Gemini findings;
- Grok findings;
- Perplexity findings;
- current execution plan table;
- any tactical email or validation output from the week.

## Task

Create one weekly action plan.

## Output Format

```text
TL;DR
- One paragraph on what matters this week.

Must Fix Before Next Daily Run
1. Item
   Owner/tool
   Why
   Command or file

Should Fix This Week
1. Item
   Owner/tool
   Why
   Command or file

Park / Ignore
1. Item
   Why not now

Adapter / Data Source Decisions
1. Source
   Build / park / reject
   Reason

Content / Trust Issues
1. Issue
   Fix

Updated Priority Table
| # | Task | Status | Priority | Notes |
```

## Rules

- Prefer fixes that keep the daily pipeline alive.
- Do not add new architecture unless needed.
- If a finding is vague, park it.
- If Gemini and Grok disagree, prioritize concrete runtime failures over vibes.
- If Perplexity cannot verify a source, park the adapter.
