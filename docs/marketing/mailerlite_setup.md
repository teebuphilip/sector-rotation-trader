# MailerLite Setup

This is the manual setup checklist for execution-plan task 52.

## Goal

Set up the public waitlist and first email automation without mixing marketing state into the trading pipeline.

## MailerLite Account

Create a MailerLite account on the free tier.

Required groups:

```text
waitlist
free_tier
paid_tier
```

Required custom fields:

```text
source
signup_date
```

## Waitlist Form

Create an embedded form named:

```text
Stockarithm Waitlist
```

Form behavior:

- Add new subscribers to group `waitlist`.
- Capture email address.
- Capture optional custom field `source`.
- Disable marketing-speak confirmation copy.
- Confirmation copy should say: `You're on the list. Weekly lab notes start soon.`

## Landing Page Wiring

The repo-side form lives in:

```text
docs/landing.html
```

The landing page is wired to this MailerLite form action:

```text
https://assets.mailerlite.com/jsonp/2275606/forms/185025288971748377/subscribe
```

After replacement, test locally by opening:

```text
docs/landing.html
```

and submitting a real email address you control.

## Automation

Create an automation named:

```text
Biscotti Launch Email
```

Trigger:

```text
Subscriber joins group: waitlist
```

For now, do not auto-send the July 1 email immediately on signup. Keep subscribers in `waitlist`.

Scheduled campaign:

```text
Date: 2026-07-01
Time: 9:00 AM America/New_York
Audience: waitlist
Subject: Why I named a trading algorithm after my dog
```

Draft source file, when written:

```text
drafts/biscotti_email.md
```

## Segment Rules

Use these segments for launch operations:

```text
waitlist: all pre-launch signups
free_tier: users who sign up but do not pay
paid_tier: users with active Stripe subscription
```

Stripe/Railway can assign `free_tier` and `paid_tier` later. MailerLite setup should not block the current paper-trading pipeline.

## Done Criteria

Task 52 is done only when:

- MailerLite account exists.
- Groups `waitlist`, `free_tier`, and `paid_tier` exist.
- `docs/landing.html` has the real form action URL. Done.
- A test subscriber lands in the `waitlist` group.
- July 1 Biscotti campaign exists as a scheduled draft or scheduled send.
