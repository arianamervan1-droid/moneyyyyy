#!/usr/bin/env bash
# Creates OpenClaw cron jobs DISABLED. Enable one at a time after a dry run.
# Review flags with: openclaw cron add --help
set -euo pipefail
add() { openclaw cron add --disabled --cron "$2" --tz America/Los_Angeles \
  --display-name "$1" --declaration-key "$1" "$1" "$3"; }

add "daily-business-run" "47 7 * * *" \
 "Read automation/RUNBOOK.md and queue.json. Validate with validate_queue.py. Schedule only approved posts to auto_pipeline channels via connectors. Obey every guardrail. Report results."
add "stashly-x-browser" "0 10 * * *" \
 "Using browser profile main, post the next approved item from stashly-x-posts.md to X as @automationnorth. Max 1 post. Stop and report on any login or captcha prompt."
add "personal-drafts" "30 8 * * *" \
 "Draft today's posts for personal X, LinkedIn and Reddit in the owner's voice. Save drafts to drafts/ only. Never post or comment."
add "weekly-review" "0 9 * * 1" \
 "Pull analytics, summarize what worked, and propose next week's queue. Draft only."
