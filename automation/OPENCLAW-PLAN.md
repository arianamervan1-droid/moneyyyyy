# OpenClaw plan: connectors vs. all-browser

Run on a persistent host (your computer or a VPS), not in a cloud session.
Log into the browser profile yourself. Never put passwords in files or chat.

## Option A: all browser
- Pros: one method for every account, no API keys.
- Cons: highest ban risk (IG, FB, LinkedIn, X, Reddit detect scripted browsers);
  breaks whenever a site changes its layout; needs a machine that is always on;
  Reddit and LinkedIn auto-engagement breaks platform rules.

## Option B: hybrid (recommended)
| Method | Accounts |
|---|---|
| Existing connectors (Metricool, Chat33, Fanvue), scheduled by OpenClaw cron | Stashly FB, Sweat Cult FB, Luna IG, Lily X, Fanvue |
| Browser automation, posting your own approved queue | Stashly X, personal X, YouTube uploads, TikTok uploads |
| Browser drafts only, you approve each one | LinkedIn, Reddit, personal creator pages |

Why B wins: official routes keep business and AI-influencer accounts safe,
and the browser covers only the gaps that have no connector.

## Rules that carry over (see RUNBOOK.md)
- AI personas (Luna, Bri, Lily) use the platform AI label and never claim real results.
- No price in a post until the owner confirms it.
- Max 1-2 posts per channel per day; pause and alert after two failures.
- Reddit and LinkedIn: draft only.

## Setup order
1. `openclaw onboard` on the host. Add model and channel keys in its prompts.
2. `openclaw browser create-profile main`, then log into each site by hand.
3. Run `bash openclaw-jobs.sh`. Jobs are created disabled.
4. Dry-run one job, check the output, then enable it. Start with Sweat Cult FB.
