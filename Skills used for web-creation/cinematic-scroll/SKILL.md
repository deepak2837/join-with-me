---
name: cinematic-scroll
description: Build scroll-stopping cinematic websites where scrolling scrubs frame-by-frame through a continuous 8-second macro "journey" video bound to scroll position (the page feels like a movie). Use when someone wants a scroll-driven or animated landing page, a cinematic scroll experience, a video-background scroll site, a "website that feels like a movie", or says "make a scroll-stopping website", "cinematic scroll site", "scroll cinema", "scroll stopper", or "/cinematic-scroll". Runs the full pipeline: concept -> AI macro video -> 60fps interpolation -> scroll-bound site (styled via frontend-design + ui-ux-pro-max) -> deploy.
---

# Cinematic Scroll

Build websites where **scrolling drives you *through* a continuous macro video**. The video is the heavy lifter; the code is a thin layer that binds `video.currentTime` to scroll position and reveals copy over calm parts of the frame.

## The core mechanic (why it works)

It is **not** 3D. It is a single 8-second "extreme macro journey" video playing in a fixed background, with **every frame tied to scroll**: scroll down = play forward, scroll up = rewind. A smoothing (lerp) loop makes the scrub buttery. Text "beats" fade in at scroll checkpoints. That's the whole trick — so the **creative (the video) carries the wow**, and the site is a tasteful frame around it.

## Tools this skill orchestrates (use the user's own connected tools — this skill ships no keys)

- **A video-generation MCP** with a cinematic text-to-video model (this workflow was tuned on Higgsfield's `cinematic_studio_3_0`, but any comparable cinematic model works). The user connects their own account.
- **ffmpeg** (local) — frame interpolation + web encode.
- **The `frontend-design` skill** — drives the visual identity (invoke it; do not hand-roll the look).
- **The `ui-ux-pro-max` skill** — design-system generation + UX/accessibility guardrails (invoke it).
- **A GitHub account** (`gh` CLI) — public repo to CDN-host the video via jsDelivr.
- **A Vercel connector/CLI** — deploy the site.

If any tool is missing, do the steps you can and tell the user what to connect. Never invent credentials.

## Pipeline (run in order)

### 0. Brief the user
Confirm: subject/theme (or let AI ideate), desktop 16:9 vs mobile 9:16, the CTA/purpose, and whether it's an internal showcase or a client site (see **Project location**). One quick pass — don't over-interview.

### 1. Ideate concepts
Generate ~10 radically different scroll-driven concepts, each a single continuous 8-second **extreme macro journey**. User picks their favorite(s) on taste. Prompt + method: `references/concepts-and-prompts.md`.

### 2. Concept -> video prompt
Turn each chosen concept into a detailed cinematic macro-video prompt (single continuous forward push, no cuts, photoreal, no text/logos). See `references/concepts-and-prompts.md`.

### 3. Generate the video  ⚠️ COST GATE
**Always preflight the credit cost and confirm with the user before generating** — video gen spends their credits. Then generate at **16:9, 1080p, 8s, cinematic model, audio off**, and poll to completion. Batching multiple concepts at once is fine (AI output is hit-or-miss ~30-50%). Settings + polling: `references/pipeline.md`.

### 4. Interpolate to 60fps
Raw gen is ~24-30fps and scrubs choppily. Interpolate to **60fps with frequent keyframes** (ffmpeg `minterpolate`) so seeking is smooth. Command: `references/pipeline.md`.

### 5. Web encode  ❓ ASK RESOLUTION
**Ask the user which resolution they want for the deployed video: 720p, 1080p, or 2K** (bigger = sharper but slower to load; 720p is usually invisible-quality behind the grade/text and is the safe default). Encode a faststart `web.mp4` at that resolution for the CDN. For genuine 2K, the source must have been generated at ≥2K in Step 3 — don't upscale to fake detail. Table + commands: `references/pipeline.md`.

### 6. Build the scroll-bound site
1. Copy `assets/scroll-engine.html` into the project as `index.html` — this is the **proven, brand-neutral scroll engine** (scrub + lerp, beats, flow-tour, hold-CTA, loader, HUD, `prefers-reduced-motion`). Leave the JS engine intact.
2. **Invoke `ui-ux-pro-max`** (`--design-system` for the product type) to get pattern/style/palette + guardrails.
3. **Invoke `frontend-design`** to commit to ONE bold, distinctive identity and restyle the engine's design layer (typography, color, layout, atmosphere).
4. **Composition discipline** (this is what makes it look designed, not pasted): pull representative video frames, see where the focal action lives, and place copy in a column over the *calm* part of the frame. Use a restrained directional grade — avoid heavy full-screen scrims. Keep one text column; never cover the video's hero moment.
5. **Every site gets a distinct identity.** Do not reuse fonts/palette across builds (frontend-design forbids convergence). If ui-ux-pro-max suggests a generic font (e.g. Inter), override per frontend-design.

### 7. CDN-host the video (default: public jsDelivr)
Push the `web.mp4` (at the resolution chosen in Step 5) to a **public** GitHub repo under the user's own account; serve via jsDelivr. Reference the CDN URL from `index.html`. Steps + URL pattern: `references/deploy.md`.
> Privacy note: repos/projects should default to **private**, but jsDelivr needs a **public** repo. Confirm with the user before making anything public (they already opted into this default when they ran the skill, but call it out).

### 8. Deploy  🚦 REQUIRES EXPLICIT APPROVAL
**Never publish to Vercel on your own initiative.** First show the user the **local preview** (Step 6 / pipeline.md), then **ask explicitly for approval to publish** and wait for a clear, affirmative go-ahead ("deploy it" / "publish it" / "ship it"). General enthusiasm about the design, silence, or "looks great" is **not** approval to publish. Only after an explicit yes: deploy `index.html` (tiny — video streams from CDN) to Vercel via the user's connector, then report the live URL. Steps: `references/deploy.md`.

## Project location (general-purpose)

Create a self-contained project folder (see the workspace's `My Projects/` convention):
- **Internal showcase / demo** -> `Internal Builds/` — use a neutral premium fictional brand.
- **Client site** -> `Client Sites/` — use the client's real brand + copy, and stamp any required legal templates before launch.

Each project is self-contained: its own `index.html`, `assets/` (source.mp4, scroll.mp4 @60fps, web.mp4), and any brand notes.

## Non-negotiables

- **Confirm cost before generating video.** Never spend credits silently.
- **Never publish without explicit approval.** Always preview locally first; deploy to Vercel only after the user explicitly says to publish. Making the CDN repo public also needs a heads-up (Step 7).
- **The composition must fit the video** — copy over calm regions, hero moment never covered.
- **Distinct identity every time** — no repeated font/palette/layout across sites.
- **Smoothness** — 60fps + lerp scrub + frequent keyframes, or it looks cheap.
- **Portability** — this skill hardcodes no keys, tokens, team IDs, OAuth links, or personal repo names. Always use the user's own connected accounts and their own repo/deploy targets.
- **Accessibility** — keep the engine's focus states, keyboard CTA/tour, and `prefers-reduced-motion` (ui-ux-pro-max checklist).

## Reference files
- `references/concepts-and-prompts.md` — ideation prompt, concept->video-prompt method, worked examples.
- `references/pipeline.md` — video-gen settings, ffmpeg interpolate + web-encode commands, polling.
- `references/deploy.md` — jsDelivr CDN hosting + Vercel deploy, generic and key-free.
- `assets/scroll-engine.html` — the brand-neutral scroll engine to copy and restyle.
