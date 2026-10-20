#!/usr/bin/env python3
"""Pre-flight checks for queue.json: channel names, length limits, banned claims, UTM tagging."""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).parent
LIMITS = {"x": 280, "instagram": 2200, "facebook": 63206, "tiktok": 2200}
BANNED = re.compile(r"\b(lose \d+|guarantee[ds]?|results? guaranteed|cure|testimonial)\b", re.I)

channels = json.loads((HERE / "channels.json").read_text())["channels"]
posts = json.loads((HERE / "queue.json").read_text())["posts"]
errors = []

for p in posts:
    for ch in p["channels"]:
        if ch not in channels:
            errors.append(f"{p['id']}: unknown channel {ch}")
            continue
        if channels[ch].get("status") != "connected":
            errors.append(f"{p['id']}: {ch} is not connected")
        text = p["text"].get(ch, p["text"]["default"])
        if p.get("link") and ch.startswith("x_"):
            text += " " + "x" * 23  # X counts every URL as 23 chars
        net = next((n for n in LIMITS if n in ch), None)
        if net and len(text) > LIMITS[net]:
            errors.append(f"{p['id']}: {ch} text is {len(text)} chars (limit {LIMITS[net]})")
        if BANNED.search(text):
            errors.append(f"{p['id']}: {ch} contains a banned claim")
    if p.get("link") and not p.get("utm_content"):
        errors.append(f"{p['id']}: link without utm_content")

print("\n".join(errors) if errors else f"OK: {len(posts)} post(s) valid")
sys.exit(1 if errors else 0)
