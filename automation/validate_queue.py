#!/usr/bin/env python3
"""Pre-flight checks for queue.json: channel names, length limits, banned claims, UTM tagging."""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).parent
LIMITS = {"x": 280, "ig": 2200, "fb": 63206, "tt": 2200}
BANNED = re.compile(r"\b(lose \d+|guarantee[ds]?|results? guaranteed|cure|testimonial)\b", re.I)

channels = json.loads((HERE / "channels.json").read_text())["channels"]
posts = json.loads((HERE / "queue.json").read_text())["posts"]
errors = []

for p in posts:
    for ch in p["channels"]:
        if ch not in channels:
            errors.append(f"{p['id']}: unknown channel {ch}")
            continue
        if channels[ch].get("mode") != "auto_pipeline":
            errors.append(f"{p['id']}: {ch} is not an auto_pipeline channel (personal and unknown accounts are posted together, never by the pipeline)")
        if channels[ch].get("status") != "connected":
            errors.append(f"{p['id']}: {ch} is not connected")
        text = p["text"].get(ch, p["text"]["default"])
        if p.get("link") and ch.split("_")[1] == "x":
            text += " " + "x" * 23  # X counts every URL as 23 chars
        net = ch.split("_")[1] if ch.count("_") >= 2 else None
        if net and len(text) > LIMITS[net]:
            errors.append(f"{p['id']}: {ch} text is {len(text)} chars (limit {LIMITS[net]})")
        if BANNED.search(text):
            errors.append(f"{p['id']}: {ch} contains a banned claim")
    if p.get("link") and not p.get("utm_content"):
        errors.append(f"{p['id']}: link without utm_content")

print("\n".join(errors) if errors else f"OK: {len(posts)} post(s) valid")
sys.exit(1 if errors else 0)
