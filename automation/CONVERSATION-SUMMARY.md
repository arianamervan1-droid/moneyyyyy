# Everything we've covered (as of 2026-10-20)

## What you asked for
1. One automation that posts to all your platforms, grows your businesses and makes money. Personal accounts go on a separate pipeline later; business pages and content pages first.
2. Analyse the business pages, then automate a workflow that markets and builds itself.
3. Publish to business pages only (not personal), no paid tools if possible, Chat33 kept for X Lily, Fanvue MCP kept.
4. Luna = your Higgsfield character, used for Stashly and her own page as a creator / Sweat Cult promoter. Her reveal as AI is part of your personal story, so you hold her AI label until then. You'll send her images in batches.
5. Bri: your call; I leave her alone.

## Your accounts (business only)
| Page | Tool | State |
|---|---|---|
| Instagram lunaxxfit_ | Metricool | connected, needs media |
| Facebook page | Metricool | connected, 3 posts queued (Oct 21, 22, 24, 10am PT) |
| TikTok stashly_1 | Metricool | connected, no analytics returned |
| TikTok @lunaxxfit | Higgsfield (tiktok-luna) | connected, needs video |
| X Lily (@daprincessa23) | Chat33 | connected, 0 posts, topic unknown |
| X Stashly (automationnorth) | none | Typefully drafts deleted; paste by hand or X API keys |
| Instagram briannaxx_01 (Bri) | none | not connected; owner's call |
| Fanvue @that_lily | Fanvue MCP | connected (analytics); AI-creator flag currently "no" |
Websites: sweatcult.shop (Lovable + Stripe; 0 purchases from ~1.7k visits; page price $27; checkout price unconfirmed ($21.60 is only true once a SWEAT20 code exists)), stashly.org (social marketplace; Lovable project).

## What I built (repo: automation/, branch claude/gym-starter-pilot-brief)
channels.json, personas.json, queue.json, validate_queue.py, RUNBOOK.md, BUSINESS-ANALYSIS.md, BRI-PIPELINE.md, LUNA-PLAN.md, stashly-x-posts.md, and .mcp.json (Twitter MCP, reads keys from environment variables).
Daily routine: "Daily business content run", 7:47am Pacific.

## Key findings
- IG ~135-140 followers; views come in bursts from reels; interactions near zero.
- Facebook page: ~2 followers; page views spike without follows.
- Best times: ~10am and ~6pm Pacific, Tue-Fri strongest.
- Checkout is the biggest money problem: 71 checkouts started, 0 purchases.

## Free tools I checked (from blog roundups, not vendor pages; verify)
Buffer, Publer: not free for you. Typefully: 14-day trial (removed). Metricool free: about 1 brand, ~20 posts/month, no X. X API: free tier reported closed to new developers; pay-per-post (~$0.01-0.015).

## Rules we agreed
No results promises or fake testimonials; no prices in posts until you confirm and checkout is tested; no personal accounts; no posting realistic AI people without the platform AI tag (held until your reveal); Luna's captions never claim she's a real certified trainer.

## What's blocking full automation (your side)
1. Attach Metricool and Chat33 to the daily routine on claude.ai (it can only draft until then).
2. X API keys (read+write) as env vars TWITTER_APP_KEY, TWITTER_APP_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET, if you want me to post Stashly's X.
3. Tell me what Lily (@daprincessa23) posts about.
4. Send Luna media in batches (share links + page per batch); I save them as Metricool drafts.
5. Test a purchase on sweatcult.shop and pick the price.

## Mistakes I made
Scheduled Typefully posts you hadn't asked for (deleted); repeated questions you'd answered.
