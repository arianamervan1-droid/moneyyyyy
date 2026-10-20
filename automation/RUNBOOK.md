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
- `draft_for_approval` (default): the run only creates drafts / posts-for-review. Nothing goes live without a yes.
- `auto`: posts go out on schedule. Switch only after ~2 weeks of approved drafts look right.

## Hard rules
- No results/weight-loss promises, no fake testimonials, no medical advice.
- Don't post one identical text to every account: personal, business and content pages each get their own voice (use per-channel `text` overrides).
- No bulk DMs, no group spam, no engagement pods.
