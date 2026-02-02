# Concepts & Prompts

## Step 1 — Ideate concepts

Ask the model (or yourself) for **10 radically different scroll-driven concepts**, each built around a single continuous **8-second extreme macro journey**. The user picks favorites on taste. Ideation is cheap; taste is the scarce part.

Ideation prompt:

> You are the sole creative director for a set of premium, scroll-driven commercial landing pages. Give me 10 radically different concepts. Each must be built around a **single continuous 8-second extreme macro journey** — one unbroken forward camera push through a material or environment, ending on a product/payoff. For each: a one-line brand + industry, the journey (what we push through, in order), and a fitting call-to-action. Make them as visually interesting and distinct from each other as possible (different materials, palettes, industries).

Good journeys share a shape: **start inside/at a micro detail → push forward through a transformation → break out onto the payoff.** Examples of strong subjects: a bubble inside aged whiskey, a dissolving capsule, a silicon lattice into a circuit-city, deep-sea bioluminescence, forming diamond, cacao into tempered chocolate, ground → aurora → curve of Earth, a vinyl groove, a honeycomb cell.

## Step 2 — Concept → cinematic video prompt

Turn each chosen concept into a detailed prompt for the video model. Structure that works:

> A single continuous 8-second cinematic macro [tracking/ascending] shot moving relentlessly forward, **no cuts**. Open on [micro detail at molecular/extreme-macro scale], [lighting]. The camera pushes forward and [transition] into [mid environment], [textures, particles, light behaviour]. It [accelerates/glides] through [environment] and finally emerges [payoff / hero object] under [light]. Photoreal, ultra-detailed, macro lens, cinematic color grade, [palette]. **No text, no logos, no captions.**

Rules that keep results clean:
- **One continuous forward move, no cuts** — say it explicitly.
- Describe **three stages**: open → through → emerge.
- Name the **palette** (it becomes the site's color system).
- End with **"no text, no logos, no captions"** so the frame stays clean for your overlay.
- Keep it ~8 seconds of action; don't over-stuff.

## Worked example (silicon / AI compute)

> A single continuous 8-second cinematic macro tracking shot moving relentlessly forward, no cuts. Open on the hexagonal crystalline lattice of silicon at molecular scale, cold blue light glinting off the atomic bonds. The camera pushes forward and descends onto a vast neon circuit metropolis: glowing copper interconnects stretching to the horizon like city streets, pulses of cyan and magenta data racing along the traces. It accelerates down a canyon of glowing circuitry and finally emerges rising over the mirror-polished surface of a finished processor. Photoreal, ultra-detailed, macro lens, cinematic color grade, dark background, electric blue and violet palette. No text, no logos, no captions.

## Mapping the video to beats

Once you have the video, place the site's copy "beats" at scroll points where the frame is **calm** (so text is legible) and that match the narrative:
- ~0.00–0.14 → hero / opening
- ~0.20–0.40, 0.44–0.66 → mid-journey moments
- ~0.68–0.82 → detail / spec block
- ~0.86–1.00 → payoff + CTA

Pull a few frames at these points (ffmpeg) to see where the action is before finalizing copy placement.
