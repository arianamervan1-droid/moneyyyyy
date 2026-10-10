# Sweat Cult — Gym Starter Pilot (brief v1, 2026-10-10)

## 1. What I verified in your connected tools (live data)

| Source | Finding |
|---|---|
| Shopify (`sweat-cult-shop-26cn7`) | **Trial plan**, 0 orders. 23 products, all print-on-demand apparel/accessories. Not where digital sales happen. |
| Lovable "Sweat Cult Storefront" (published) | Digital checkout runs on-site (Stripe). Catalog in DB has **~50 items**: 30-Day Gym Reset Guide $27 (featured, "Start Here"), 90-Day Strength Blueprint $47, Beginner Strength Program $27, Full Body Guide $24, nutrition/meal/grocery guides $12–19, trackers/planners $5–12, Elite Vault $97, and **three existing membership SKUs: Community $10/mo, Women $25/mo, Men $30/mo**. |
| Funnel data (Aug 4 – Oct 10) | 1,687 page views · 201 product views · 71 begin_checkout events · 4 lead events · **0 rows in `purchases`, 0 in `subscriptions`**. (1 `purchase` event on Oct 6 has no matching purchase row — likely a test.) **Real revenue to date: $0.** |
| Klaviyo | Email list exists but is effectively empty (a few profiles, mostly your own/test addresses). Day 2/4/7 follow-up flow reportedly live. |
| Metricool | Connected: Instagram `lunaxxfit_`, TikTok `stashly_1`, Facebook page. **Follower counts not retrieved yet** (my analytics call needs the right metric IDs). |
| sweatcult.shop | Not reachable from my sandbox (DNS), so I could not view it directly; I reviewed it through its Lovable source and database instead. |

**Implication:** Sweat Cult does not have a product gap. It has a traffic/trust gap: ~1.7k visits, ~0 purchases, and three unsold membership SKUs. Building a bigger membership app before anyone has paid would repeat that.

## 2. Research (directional — sources are mostly blogs, not rigorous studies)

- **Demand for the problem is real but weakly measured.** No formal beginner survey found. Blog/trainer sources consistently cite: not knowing what to do, copying random workouts, intimidation, and drop-off in the first weeks; one gym blog cites research that ~half of people starting an exercise program stop within six months. Treat as directional, not proof people will *pay*.
- **Complaints about existing tools:** beginner roundups say apps like Fitbod/NTC feel overwhelming at first; a Reddit user complains plans in spreadsheets/PDFs are hard to use.
- **Price landscape:** Hevy Pro ~$2.99–3.99/mo, Strong Pro $4.99/mo, JEFIT Elite $12.99/mo, Fitbod $15.99/mo (competitor-blog sources; verify in app stores). Online coaching: entry ~$100–175/mo, typical $150–300/mo.
- **Logging/tracking is a commodity** (Hevy/Strong are nearly free). We cannot win there and should not build it.
- **Gap:** between a $3–16 self-serve app and $100+/mo coaching there is little human guidance for beginners at ~$20–40/mo.

## 3. The one problem to solve

> "I finally got a gym membership, but every week I walk in not knowing what to do, so I skip."

Not "get fit." Specifically: **a beginner who has a gym but no plan and no one checking in.**

**Differentiation (what we can honestly claim):** a credentialed (ISSA) trainer chooses a single 3-day plan for you, tells you each Sunday what this week's three sessions are, and checks in. No library to browse, no dashboard. Logging happens in free tools (Hevy free or a template) — we don't build an app.

## 4. Smallest paid pilot (recommended)

**"Gym Starter — Founding Cohort"**, 10 seats, 4 weeks, then month-to-month.

- **Price to test:** $29/month founding rate (compare: $19 and $49 as later A/B). Rationale: above apps, far below coaching, covers real support time. ⚠ Your existing Women/Men tiers are $25/$30 — **don't launch another SKU; repurpose one** (see decisions).
- **What members get (minimum):**
  1. Onboarding form → you assign 3-day or 4-day plan (4 weeks, from your existing Reset Guide / Strength Program content so little is new).
  2. Exercise cues + substitutions page.
  3. Sunday "plan your week" email/text (Klaviyo, templated, 5 min to personalize).
  4. One weekly check-in question in the existing community chat; you reply to each member briefly.
  5. Existing grocery/meal guides included as a bonus (already written).
- **Not in the pilot:** custom logging app, progress dashboards, meal plans tailored to individuals, anything medical.
- **Success criteria (4 weeks):** 10 paid, ≥7 finish week 4, ≥5 say they'd continue, ≤3 hrs/week of your time.
- **Guardrails:** general fitness guidance only; no weight-loss promises; no medical diets; clear "check with your doctor" line; no invented testimonials.

## 5. Revenue vs. profit (assumptions flagged)

Assumptions: Stripe 2.9% + $0.30 per charge (3rd-party sources also cite +0.7% if Stripe Billing is used — not included); $60/mo fixed tools **placeholder** (Lovable/Klaviyo/Shopify plans — need your real bills); 20 min/member/month of support; monthly churn 10–20% **assumed, not measured** (no benchmark found for this product).

| Price | Net/member | Members for $500 profit | for $1,000 | for $3,000 | Support hrs/wk at $3k |
|---|---|---|---|---|---|
| $19 | $18.15 | 31 | 59 | 169 | ~13 |
| $29 | $27.86 | 21 | 39 | 110 | ~8.5 |
| $49 | $47.28 | 12 | 23 | 65 | ~5 |

- **10 pilot members at $29:** $290 revenue → ~$279 after fees → ~$219 profit after the $60 placeholder, before your time. That validates demand; it does not pay rent.
- Steady state at 10–20% churn means you must keep adding roughly 10–20% of your base every month just to stand still (e.g., 39 members ≈ 4–8 new/month).
- Your 4–6 hrs/week caps this at roughly 40–60 members at 1:1-ish support. **$3k/month profit needs either a higher price (~$49+), group-based support (~10 min/member/month), or a second product** — raise this after pilot data.
- Acquisition cost isn't included; organic only for now.

## 6. Decisions I need from you (nothing was changed, published, or sent)

1. **Reuse or add?** Repurpose the existing "Sweat Cult Community" ($10) SKU into the pilot, or create a new SKU in the same Lovable store? (Recommend: edit existing, price $29, 10-seat cap.)
2. **Price:** go with $29 founding?
3. **Refund policy:** e.g., first-month money-back? (Your decision; it affects the risk to buyers.)
4. **Audience size:** how many followers on `lunaxxfit_` (IG), TikTok, and the Facebook page, and any existing email/DM list? 10 buyers from ~0 warm audience needs outreach to people you know first.
5. **Can I draft (not send) outreach** to 20–30 warm contacts and the launch posts for your approval?

## 7. Next steps once you approve
- Update the product page copy/onboarding in Lovable (needs your OK; uses workspace credits).
- Write onboarding form, Sunday email template, week-1 workout, feedback survey (drafts ready on request).
- Add an admin metrics view from existing `analytics_events`, `purchases`, `subscriptions`, `manual_costs` tables for visits → sign-ups → purchases → cancellations → profit.
- Weekly review of real numbers; adjust the offer from data.

**Sources:** [Fitbod/JEFIT/Hevy/Strong pricing roundup](https://www.sensai.fit/blog/fitness-app-pricing-free-tier-comparison), [Boostcamp app comparison](https://www.boostcamp.app/best/workout-apps), [Online coaching price guide](https://www.fitbudd.com/insights/how-much-to-charge-for-online-personal-training-complete-pricing-guide), [Why gym beginners quit](https://k24.digital/lifestyle/health-and-fitness/why-most-gym-beginners-quit-after-a-few-weeks/amp), [PureGym beginner guide](https://www.puregym.com/us/blog/how-to-start-going-to-the-gym-and-actually-stick-with-it), [Beginner apps test](https://indiehackers.com/post/best-workout-apps-for-beginners-2026-i-tested-7-fitness-apps-for-2-months-442af07d69), [Stripe fee breakdown](https://flexprice.io/blog/stripe-pricing-breakdown-2026).
