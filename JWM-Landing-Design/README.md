# Join With Me — Landing Page Design

**Design direction: “The Trail”** — one design language, three interchangeable palettes.
Homepage revamp, mobile-first, built from Join With Me's own content and photography.

---

## Open this first

| File | What it is |
|---|---|
| **`index.html`** | The master. Same page, with a live **theme switcher** (bottom-left) so you can flip between all three palettes in front of the client. Start here. |
| `theme-01-sahyadri.html` | Standalone build — **Sahyadri** palette (deep forest + the logo's lime). Recommended default. |
| `theme-02-monsoon.html` | Standalone build — **Monsoon** palette (river teal-green + golden yellow). |
| `theme-03-terracotta.html` | Standalone build — **Terracotta Trail** palette (farm olive + ochre). |
| `design-system.html` | Tokens, type scale, spacing, radii, elevation, components and build rules. |
| `boards/` | Flat JPGs of everything — for WhatsApp, email or dropping into a deck. |

Just double-click any `.html` file. No server, no build step, no internet needed
(fonts load from Google Fonts, so keep a connection for the exact typefaces).

Each `theme-0x.html` is fully self-contained — share one on its own without the others.

---

## Getting this into Figma

The three theme files are written to convert cleanly through **[html.to.design](https://www.figma.com/community/plugin/1159123024924461424)**
(free plugin, in Figma → Resources → Plugins → search “html.to.design”).

1. In Figma, run the plugin.
2. Choose **“Import HTML code”** (or the browser-extension option if you prefer).
3. Paste in the contents of `theme-01-sahyadri.html` — or open the file in Chrome
   with the html.to.design extension and capture the page.
4. Import at width **1440** for desktop and **390** for mobile.

**Add `?flat=1` to the URL before importing.** That switches on export mode, which:

- freezes every scroll animation in its **final, visible** state, so nothing lands in Figma at 0% opacity;
- removes the theme switcher and lightbox (review-only tools);
- un-sticks the bottom CTA bar so it lands after the footer as its own component board
  instead of floating over the middle of the page.

Everything is flexbox and CSS grid, so sections arrive as **auto-layout frames**.
Headings, body copy and labels arrive as **real editable text nodes**. All three
typefaces (Fraunces, Plus Jakarta Sans, DM Mono) are free Google Fonts, so Figma
will match them without substitution — install them in Figma first if you haven't.

`design-system.html` imports the same way and gives you a tokens page to build
Figma colour and text styles from.

---

## What's on the page

| # | Section | Notes |
|---|---|---|
| — | Header | Wide floating capsule in grass green, logo inside it. Collapses to logo + call + menu. |
| 01 | Hero | Editorial split: headline left, photo stack right, floating **Next walk** card with live urgency, trust row (16,000+ / 898+ / 4.9★). |
| — | Marquee | Scrolling proof strip — kid-friendly, pet-friendly, naturalist-guided… |
| 02 | The Promise | Four pillars + the “Anyone can do this” banner. |
| 03 | The Walks | All five real experiences with prices, tags and **date chips** (Full / Filling / Open). |
| 04 | Since we started | Dark band, animated count-up. |
| 05 | A day with us | The real Lakeside itinerary, 8:00 AM → 1:00 PM, as a photo timeline. |
| 06 | Film & gallery | Join With Me's own drone film + a 4×3 photo grid with lightbox. |
| 07 | The practical bit | What's included / what to carry. |
| 08 | Trusted by | ASB, JBCN, Shishuvan, Inodai, IDA + four use cases. |
| 09 | Where we walk | Five regions, map card, real local-train times. |
| 10 | Stories | Real review + three shorter quotes. |
| 11 | Questions | Eight FAQs, accordion. |
| 12 | Need help | Both phone numbers, WhatsApp, book. |
| 13 | **Reels** | Scroll-driven reel stack — see below. |
| — | Footer | Full sitemap + oversized wordmark. |
| — | Sunflower | Floating nature-connect assistant, bottom right. |

---

## The reels section (13)

The finale. Page scroll drives it — there is **no nested scroller**, so the user
is never trapped: scroll past the fifth reel and the footer arrives normally.

- **Mobile** — the frame stays put and the front reel flies up and out of it as you
  scroll, with the next one already stacked behind. Instagram reels / a dating-app
  deck, not a vertical list. Story-style progress bar across the top.
- **Desktop** — an overlapping 3D stack. The front card plays full size; the others
  fan out behind it, rotated and dimmed, like the iPhone tab switcher. Almost no
  text: just `03 / 05`, one caption line and a Watch link.
- Only the reel nearest the centre is allowed to play, so five videos cost about
  as much as one. The rest stay paused with `preload="none"` until they're needed.

### The five reels

Your files are in and processed. Each was cropped to 9:16, capped at 20 seconds
(a landing-page reel only gets a few seconds of attention), re-encoded at 608x1080
and given a poster frame. Originals are kept untouched in
`assets/video/reels/_originals/`.

| # | Caption shown | From your file | Size |
|---|---|---|---|
| 01 | 1.5 hours from Mumbai | Lakeside Nature Walk (short) | 1.8 MB |
| 02 | Monsoon is here | Lakeside Nature Walk (long) | 3.3 MB |
| 03 | Forest Lakeside Nature Walk, Badlapur | Forest Lakeside – Badlapur | 2.8 MB |
| 04 | A family-friendly riverside nature walk | Riverside Nature Walk | 3.1 MB |
| 05 | “I knew girls are powerful — now I've witnessed it live” | Yes girls are powerful | 4.1 MB |

Reel 03 opened on ~2 seconds of black title card, so it starts at 2.2s instead.

**⚠️ Confirm the Instagram links.** Each reel's paper-plane icon and the desktop
**Watch ↗** button point at one of the five permalinks you sent, but I had no way
to verify which URL belongs to which video — Instagram blocks metadata for logged-out
requests. Check the five `instagram.com/reel/...` links in the markup against the
right clips before this goes live.

To replace any reel later, drop a new file over `assets/video/reels/reel-0X.mp4`
and regenerate its poster. Nothing else needs changing.

### Why not the official Instagram embed

You gave me the `<blockquote class="instagram-media">` embed codes. I did not use
them, for three reasons:

1. **They cannot autoplay.** The embed is a cross-origin iframe served by
   Instagram. There is no API to start playback from the page, and mobile browsers
   block autoplay of embedded media regardless. You would get a static card with a
   play button that opens Instagram in a new tab — the opposite of what you asked for.
2. **They cannot be styled.** Instagram's white card, its own fonts and its own
   chrome are fixed. No full-bleed, no scroll-driven deck, no custom UI.
3. **`embed.js` is heavy** — several hundred KB plus per-reel iframe requests, all
   third-party, all blocking. It would be the slowest thing on the page.

Self-hosted MP4s give autoplay, full design control and far better performance.
The Instagram permalinks are still in the markup: every reel's paper-plane icon
and the desktop **Watch on Instagram** button link out to the original post, and
the section header links to `@joinwithme.in`. So the traffic still goes to Instagram —
the reel just plays on your page first.

Reel 05 is credited to **@barefootsagar** (Sagar Bharat Gala), not to Join With Me.
Since it is someone else's post, get their OK before self-hosting that one.

---

## Content — what's real and what isn't

Everything is taken from joinwithme.in and the assets you shared, **except**:

- ⚠️ **Three short testimonials** in section 10 (“Parent, Mumbai”, “Family group”, “Pet parent”)
  are **placeholder copy** written to show the layout. The long Ruchika Agrawal quote above
  them is real and verbatim. Swap the three short ones for real Google reviews before launch.
  They are flagged with an HTML comment in the file.
- ⚠️ **The eight FAQs** are drafted from facts stated on your existing site (pace, pets, meals,
  how to reach, private hikes, refund policy). They still need your sign-off —
  `joinwithme.in/faqs` currently returns a **404**, so there was no existing copy to pull from.
  *That broken link is worth fixing on the live site regardless.*
- The **“5 regions”** stat is derived (Karjat, Badlapur, Palghar, Mumbai, Pench), not published.
- Dates and availability are copied from the site as of 13 Aug 2026 and will need refreshing.

Numbers used as published: **16,000+** people reconnected, **898+** walks led,
**4.9/5** from **1,000+** experiencers, prices ₹1,599 / ₹1,699 / ₹1,799 / from ₹999.

---

## Photography

All 100 images and the film are Join With Me's own, pulled from the live site and
normalised (AVIF/WebP → JPEG, capped at 1800px, progressive) into `assets/`.
No stock, no AI imagery.

Promo graphics with baked-in text (`Lakeside MONSOON Hike`, `Forest Lakeside`,
`Riverside`) were **deliberately replaced** with clean photographs — the card
titles already say the name, and the burnt-in text was cropping badly.

The brand video was re-encoded twice: `jwm-film.mp4` (1280px, with sound, for the
player) and `jwm-ambient-720.mp4` (960px, silent, spare for a future hero loop).

---

## Rebuilding the theme files

`index.html` is the only file you edit. To regenerate the three builds:

```bash
python build.py
```

---

## Known trade-offs

- **`backdrop-filter`** (frosted glass on the header and the map pins) does not survive
  the Figma import. Every element using it also has a solid-ish background colour, so it
  degrades to a flat panel rather than disappearing.
- **The marquee and count-up are motion-only.** In Figma they land as static text —
  which is correct; the design reads fine without them.
- **The FAQ shows one answer open.** The other seven answers are in the DOM but collapsed,
  so they import clipped. Expand them in Figma if the client wants to see all the copy.
- **The page is ~15,300px tall at 1440.** That is one long Figma frame; consider splitting
  it per section after import.

---

## Section transitions

There are no flat horizontal rules between sections. Each dark band fades in from
the paper above it, holds, then fades back out, with two soft colour blooms placed
off-centre. The light sections carry their own ambient blooms on a full-bleed layer
that deliberately runs past the section's top and bottom edges — that overhang is
what stops a visible seam appearing where two sections meet. Every tint is built
from the active theme's `--glow-*` variables, so all three palettes diffuse in
their own colour.

## Sprout — the nature-connect button

Bottom-right, above the sticky bar. The mark is a leaf that doubles as a speech
bubble: the midrib is the bubble's tail and three new shoots along it read as
typing dots. It breathes on a 3.4s loop and opens into a pill on hover
(“Which walk suits us?”). Currently it jumps to the Need help section — point it
at your chat provider when you have one.

## Not location-specific

The page is written for the brand, not for one trek. The itinerary is framed as
“every Join With Me experience follows the same shape”, the water stop covers a
waterfall, river bend or forest lake depending on the walk, and the included list
no longer names Karjat features. Location names now appear only where they are
genuinely per-walk: the experience cards, the next-batch card and the regions list.

---

## Navbar

A wide floating capsule rather than a full-width bar, in a grass green that is its
own token per theme (`--grass-a` / `--grass-b`) — fresher than the deep forest used
for the section bands. The logo sits **inside** the capsule on the left, the links
run through the middle with icons and an active pill, and the two actions sit right.
It lifts and tightens slightly once you scroll.

It degrades in two steps: under 1100px the links move behind the menu button, under
620px the capsule shrinks to logo + a call icon + menu.

## The sticky Book-now bar is gone

Removed entirely — markup, styles and its scroll handler. Booking now lives in the
navbar CTA, the date chips on each walk card, and the Need Help block.

## The assistant

A real sunflower head, cropped from `paul-green-5lRxNLHfZOY-unsplash.jpg`, as the
face of the button. It breathes on a loop, turns slightly on hover and opens into a
pill (“Which walk suits us?”). Points at the Need Help section until you have a
chat provider to wire it to.

## Stock assets in use

From `latest stock images for testing/`, kept deliberately to three places so the
page stays built on your own photography:

| Asset | Where | Why |
|---|---|---|
| `paul-green` sunflower | Assistant button | The button face |
| `14327369` forest clip | Behind the stats band | Ambient motion under the numbers, held at 20% so the figures stay loudest |
| `matthew-smith` moss | Need Help card | Texture behind the contact block |

Everything else — hero, pillars, walk cards, itinerary, gallery, reels — is still
Join With Me's own material. Say the word if you want stock pushed further into the
gallery or the walk cards.
