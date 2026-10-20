# Posting automation runbook

Goal: one queue, many channels, every post tagged so we can see which ones make money.

## Flow
1. Add/approve posts in `queue.json` (status: draft -> approved).
2. `python3 automation/validate_queue.py` must pass.
3. Run (manually or from the scheduled task) for each `approved` post:
   - **Instagram / Facebook / TikTok (business)** -> Metricool `createScheduledPost` (brand 6596743), at the time from `getBestTimeToPostByNetwork` if `when` is null.
   - **X** -> Chat33 `validate_post` then `create_post` on the X account id.
   - Mark the post `scheduled` with the returned id.
4. Weekly: pull Metricool analytics + Shopify/Lovable purchases, double down on the `utm_content` values that led to checkout.

## Modes (`channels.json` -> `mode`)
- `auto` (current, set by the owner 2026-10-20): the daily run writes posts, validates them, and schedules/publishes them to **business channels only** (`mode: auto_pipeline`). Personal accounts are never touched.
- `draft_for_approval`: fallback if the owner asks to review first.

## Hard rules
- No results/weight-loss promises, no fake testimonials, no medical advice.
- Don't post one identical text to every account: personal, business and content pages each get their own voice (use per-channel `text` overrides).
- No bulk DMs, no group spam, no engagement pods.

## Auto-publish guardrails (the run must obey all of these)
- Only channels with `mode: auto_pipeline` and `status: connected`; `validate_queue.py` must pass first.
- Skip any post that mentions a price until the owner confirms it (product page says $27; checkout price is unconfirmed, and $21.60 is only true once a SWEAT20 code exists) and the checkout is tested.
- Instagram/TikTok need real media; if none exists, skip that channel, do not post text-only.
- AI-influencer pages (lunaxxfit, briannaxx_01, Lily Bri): do NOT set the platform AI label (`isAiGenerated` / `isAigc`) until the owner says when and how (owner decision 2026-10-20, tied to the brand story). Until then, never claim credentials, real results or testimonials, and publish only text and graphics on these pages, not AI-generated people or video. The owner will lift that when giving the labeling go-ahead.
- Max 1-2 posts per channel per day. Pause everything and tell the owner if a post fails twice.

## Bri (briannaxx_01)
- Owner approved 2026-10-20 with the AI label ON for every Bri post (`isAiGenerated: true` on Instagram, `isAigc` on TikTok). Her bio must say she is AI. Captions never claim she is a real woman. Clothed, non-explicit only. Never strip metadata or try to avoid platform AI detection.
