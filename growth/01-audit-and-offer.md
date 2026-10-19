# Sweat Cult — audit, offer and first fix (2026-10-19)

Scope: digital products only, Facebook only, black / charcoal / warm gold, slogan "Train With Purpose. Wear the Mindset."

## How this was inspected (and its limits)
- I could NOT open www.sweatcult.shop from my environment (network is blocked). I reviewed the site's source code, product database, analytics tables and preview screenshots instead.
- Everything below marked "verified" was read from those sources. Nothing was clicked through on the live site. The owner needs to run the short phone checklist at the bottom.

## Current catalog (verified from the database)
- 35 active digital products, no apparel. Featured: 30-Day Gym Reset Guide $27.
- New: First Week at the Gym playbook $17; The Gym Starter Kit $37; Gym Starter membership ($29/mo) exists but is hidden.
- Checkout: on-site Stripe. SWEAT20 (20% off) is auto-applied to eligible products, so the Reset Guide actually charges $21.60, even though the page and button say $27 and the site's own "launch offer" code expired Sep 19, 2026.

## Three biggest barriers to a paid sale
1. **Trust and proof.**
   - The Reset Guide carried a "Best Seller" badge in the database with 0 sales. Fixed (see below).
   - No real reviews exist (0 in the database). The review section stays hidden, which is correct; do not fake it.
   - The product page never said who wrote the guide. Fixed (ISSA-certified trainer line added to the description).
2. **Interruptions.**
   - `lead-capture-popup`: a full-screen blurred email popup 8 seconds after landing, on every page including product pages, on mobile.
   - `payment-test-mode-banner`: shows "Preview mode — all payments here are test payments" if the site was ever built with a test Stripe key. Unverified on live; must be checked on a phone.
3. **Price mismatch / unclear offer.**
   - Page and button: $27. Checkout: $21.60 (SWEAT20 auto-applied). The expiry in the code (Sep 19) says the offer ended; checkout says otherwise. This confuses buyers and hides the true price from ad math.
   - Decision needed from the owner: keep the $21.60 price and say so on the page, or end SWEAT20 and charge $27.

## Analytics (all time, Aug 4 – Oct 19, from the site's own event table)
| Metric | Value | Note |
|---|---|---|
| Unique visitors | 1,559 | includes owner/test traffic |
| Page views | 1,999 | |
| Product views | 222 (210 visitors) | |
| Checkout starts | 85 (82 visitors) | includes owner and tool tests; cannot be separated |
| Paid, live, non-test purchases | 0 | `purchases` table is empty; the 1 "purchase" event on Oct 6 has no matching order |
| Revenue | $0 | |
| Subscriptions | 0 | |
| Email signups | 2 subscribers, 7 leads | |
| Reviews | 0 | |
| Logged advertising cost | $0 in the database | owner says ~$5 on Snap for each of two sites; unverified, no export provided |

Traffic sources: direct/none 1,346; Snapchat paid 156 (0 product views, 0 checkout starts); Instagram 36; Facebook organic 10 (8 product views, 0 checkout starts); Google 5; TikTok 3.

Facebook ads: not connected (no Meta Ads connection, no pixel data available to me). To review ads I need either Meta Ads Manager access via a connector, or a CSV export of Campaign / Ad set / Ad: spend, link clicks, landing page views, purchases, purchase value.

## Affordable customer acquisition cost (assumptions flagged)
- Net revenue per sale at today's checkout price: $21.60 − Stripe (2.9% + $0.30 ≈ $0.93) = **about $20.67**.
- At $27 with no discount: $27 − $1.08 = **about $25.92**.
- Digital product, no per-sale cost; no logged tool costs (assumed $0, owner to confirm).
- With one product and no proven repeat purchases, break-even CAC equals net revenue per sale. A safer ceiling to test is about **50% of net: $10 at today's price, $13 at $27**, until real conversion data exists.
- No ad budget should be raised until there is at least one verified paid sale from free traffic.

## Target customer and main product
- **Customer:** a woman new to the gym (or returning) who walks in without a plan and quits when nothing tells her what comes next.
- **Product:** 30-Day Gym Reset Guide. It already has real preview pages, a clear structure and an honest "who it's for" section, which no other product has.
- **Problem it solves:** no plan, no progression, intimidation by equipment.
- **What buyers get (verified from the product page and preview images):** 27-page phone-friendly PDF; 30 days of scheduled workouts; 3–5 training days a week with rest days; sets, reps, rest and effort targets with weekly progression; exercise swaps for busy gyms or missing equipment; 8-minute warm-up and cool-down with form cues; printable training logs; instant download plus Library access.
- **Why worth the price:** the page already compares it to a single personal-training session ("$60 or more"). Keep it, but never state results.

## Product page: what was changed now (database only, reversible)
Live-site effect, pending a phone check by the owner:
- Badge: "Best Seller" → "Start here".
- Description: now says who it's for, how Week 1 works, and "Written by an ISSA-certified personal trainer. General fitness information, not medical advice."
- "What's included": 7 specific bullets matching the guide (27-page PDF, 30 scheduled days, 3–5 day structure, swaps, warm-up and cues, logs, instant download).

Revert SQL (restores the previous values):
```sql
update public.products set badge = 'Best Seller',
 description = 'A structured 30-day gym reset built for anyone who wants a clear plan instead of guesswork. Every session is mapped out — what to train, how many sets, and how to progress week to week.',
 includes = array['A 30-day structured training calendar','Session-by-session workout breakdowns','Progression guidance week to week','Warm-up and movement notes','Instant digital download']
where slug = '30-day-gym-reset-guide';
```

## Page copy to use (already on the page unless marked NEW)
- Headline (live): "Walk Into the Gym Knowing Exactly What to Do for the Next 30 Days."
- Button (live): "Get Instant Access — $27"
- NEW short pitch under the button: "27 pages. 30 days. One plan. Written by an ISSA-certified trainer."
- NEW "About the author" block (needs a code change): "I'm an ISSA-certified personal trainer and nutritionist. I wrote this plan for women who are new to the gym and want to stop guessing." Add the owner's real photo if she wants one.
- FAQs (live): 7 questions on beginners, equipment, days per week, Planet Fitness, membership, delivery and returns.
- NEW FAQ: "Does this promise weight loss?" — "No. It's a training plan. It gives you structure for 30 days; results depend on many things I can't control."

## Needs code changes (Lovable credits are out; queued, not done)
1. Don't show the email popup on product and checkout pages; on mobile, show it only after the visitor leaves (or after 45+ seconds) so it never covers the buy button.
2. Confirm the live build uses a live Stripe key so the test-mode banner never appears; if it does appear, fix it first.
3. Make price honest: either show the SWEAT20 price on the page ("$27, $21.60 with launch code applied at checkout") or switch off SWEAT20 and charge $27.
4. Add the "About the author" block and the weight-loss FAQ above.
5. Add a real review section only after real buyers leave reviews.

## Owner phone checklist (3 minutes, no payment)
1. Open www.sweatcult.shop/products/30-day-gym-reset-guide on your phone. Do you see the badge "Start here" and a line about the ISSA-certified trainer?
2. Do you see any banner saying "test payments"? (If yes, tell me immediately.)
3. Wait 10 seconds. Does a popup cover the screen? Screenshot it.
4. Tap "Get Instant Access — $27". What price does the Stripe form show?
