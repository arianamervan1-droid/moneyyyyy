# Lovable fixes — ready to send when credits return

Status: APPLIED TO PREVIEW ONLY on 2026-10-20 (Lovable commit 23982c29, 4.2 credits). NOT published; owner must review the preview and publish. Verified by Lovable in preview: build passes, 6/6 discount tests pass, no 390px overflow, no prices/discounts/checkout changed, copy renders. Not verified: banner on the real sweatcult.shop host. Finding: the lead popup is not mounted anywhere in the app, so it was not the cause of live interruptions; the new rules apply if it is re-enabled.

Send this as one message to the "Sweat Cult Storefront" project:

---
Conversion fixes for the Sweat Cult store. Do NOT publish; I will review the preview and publish myself. Do NOT change any prices, discounts or checkout amounts. Honest copy only: no invented reviews, testimonials, ratings, scarcity or results. Brand: black, charcoal and warm gold (keep the existing design tokens). Slogan: "Train With Purpose. Wear the Mindset."

1) Email popup (src/components/lead-capture-popup.tsx): never show it on /products/*, /checkout/* or /free-routine*. Elsewhere, remove the 8-second timer entirely; show it only on exit intent on desktop. On mobile do not show it at all. Keep it dismissible, once per session, and keep the existing capture logic.

2) Test-mode banner: confirm the production build uses a live publishable Stripe key. If the PaymentTestModeBanner can ever appear on the published site, make it render only when the hostname is an id-preview--*.lovable.app or localhost preview host, never on sweatcult.shop, www.sweatcult.shop or *.lovable.app published hosts. Report what you found.

3) Reset Guide product page (src/routes/products.$slug.tsx, slug 30-day-gym-reset-guide): add, directly under the main buy button, one understated line: "27 pages. 30 days. One plan. Written by an ISSA-certified trainer." Add an "About the author" section below the 'Who this guide is for' section with this exact copy: "I'm an ISSA-certified personal trainer and nutritionist. I wrote this plan for women who are new to the gym and want to stop guessing." (no photo placeholder, no fake credentials). Add this FAQ at the end of the existing RESET_GUIDE_FAQ: Q "Does this promise weight loss?" A "No. It's a training plan that gives you structure for 30 days. Results depend on many things I can't control, and this is general fitness information, not medical advice. Check with your doctor before starting a new exercise program."

4) Mobile buying flow: on the Reset Guide page at 390px width, make sure the sticky buy bar does not cover the FAQ or the footer content and the first buy button is visible without scrolling past more than one screen of text. Report with a 390px screenshot check.

Verify in preview/test mode (do not pay): build and tests pass; popup does not appear on /products/30-day-gym-reset-guide at 390px and 1280px after 15 seconds; no test banner on a non-preview host; new copy renders; no horizontal overflow at 390px; prices unchanged. Report exactly what changed and what you could not verify.
---

## Owner decision still open (blocks nothing above)
Price shown on the page ($27) vs charged at checkout ($21.60 after auto-applied SWEAT20, whose launch offer expired Sep 19):
- Option A: keep $21.60 and say so on the page.
- Option B: switch off SWEAT20 for the Reset Guide and charge $27.
Until decided, all campaign copy uses a {PRICE} placeholder for direct offers.
