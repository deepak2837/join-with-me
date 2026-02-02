# Pipeline — video generation, interpolation, web encode

All commands below are generic. Use the user's own connected video MCP; this file contains **no keys**.

## Step 3 — Generate the macro video

Use a cinematic **text-to-video** model on the user's video MCP. This workflow was tuned on Higgsfield's `cinematic_studio_3_0`, but any comparable cinematic model works (Kling, Seedance, Veo, etc.).

Recommended settings:
- **Aspect:** `16:9` (desktop) or `9:16` (mobile)
- **Resolution:** generate at **≥ the user's chosen final resolution** (Step 5). 1080p covers 720p/1080p delivery; for a genuine 2K site, generate at 2K/4K here (higher credit cost). Never upscale later to fake detail.
- **Duration:** `8` seconds
- **Genre/look:** cinematic / "epic" if the model offers it
- **Audio:** OFF (the site is silent; saves credits)

### ⚠️ Cost gate — do this every time
1. **Preflight the credit cost** (most MCPs expose a cost/preflight flag) and **tell the user the number before generating.** Never spend silently.
2. Generating a **batch of 2–4** concepts at once is smart — AI output is hit-or-miss (~30–50% keep rate), and jobs run in parallel.
3. Submit, then **poll the job status** until each completes; download each result MP4 into the project's `assets/` as `source.mp4`.

Typical cinematic-model output is ~24–30 fps — which scrubs choppily. That's what Step 4 fixes.

## Step 4 — Interpolate to 60fps (smooth scrub)

Motion-interpolate to 60fps with **frequent keyframes** so `currentTime` seeking is smooth (sparse keyframes = janky scrubbing).

```bash
ffmpeg -y -i source.mp4 \
  -vf "minterpolate=fps=60:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1" \
  -c:v libx264 -preset medium -crf 20 -g 6 -keyint_min 6 -pix_fmt yuv420p -an \
  scroll.mp4
```
- `minterpolate ... mci` synthesizes true in-between frames (best quality; it is CPU-heavy — a few minutes for 8s @1080p is normal).
- `-g 6 -keyint_min 6` = a keyframe every 6 frames → smooth seeking.
- `-an` = drop audio.

`scroll.mp4` is your master for local preview.

## Step 5 — Web encode (ASK the user the output resolution)

**Ask the user which resolution they want for the deployed video: 720p, 1080p, or 2K.** Then encode `web.mp4` accordingly. Explain the trade-off — bigger = sharper but slower to load; a full-bleed background sits behind a grade + text, so 720p is usually invisible-quality and the safest default, but let them choose.

| Choice | `scale=` | crf | Typical 8s size | When to pick it |
|---|---|---|---|---|
| **720p** | `1280:720` | 26 | ~2–5 MB | Default. Fastest load; imperceptible behind grade/text. |
| **1080p** | `1920:1080` | 24 | ~8–15 MB | Video is a sharp hero focal point; load budget is fine. |
| **2K** | `2560:1440` | 23 | ~15–30 MB | Only worth it if the **source was generated at ≥2K** (see note). |

```bash
# Set RES to the user's choice: 1280:720  |  1920:1080  |  2560:1440
RES=1280:720
# Match crf to the choice above (720p→26, 1080p→24, 2K→23)
ffmpeg -y -i scroll.mp4 -vf scale=$RES \
  -c:v libx264 -crf 26 -preset veryfast -g 6 -keyint_min 6 -pix_fmt yuv420p \
  -movflags +faststart -an web.mp4
```
- `+faststart` moves the moov atom to the front for instant streaming.
- Keep `-g 6` so scrubbing stays smooth on the deployed copy too.
- This `web.mp4` is what you push to the CDN (Step 7).

> **2K/4K caveat:** the web copy can't have more real detail than the master. If the user wants genuine 2K, also **generate at 2K/4K in Step 3** (Cinema Studio and similar models support it, at higher credit cost). Scaling a 1080p master up to 2K just makes a bigger file with no added detail — so tie the generation resolution to the final choice up front.

## Preview locally

Serve the project folder and open it (the engine references `assets/scroll.mp4`):

```bash
python3 -m http.server 8123   # then open http://localhost:8123
```

Let the loader clear (first-frame buffer) before judging the scrub.

## Notes
- **HDR / phone source:** if a source is HDR (rare for gen models), tone-map to bt709 during encode.
- **Duration mismatch:** the engine reads `film.duration` at runtime, so 8s vs 10s just works.
- **Choosing keepers:** review a few frames (open/mid/end) of each batch output; regenerate only the weak ones.
