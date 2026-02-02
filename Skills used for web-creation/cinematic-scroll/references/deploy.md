# Deploy — CDN-host the video, ship the site

Generic and **key-free**. Use the user's own GitHub account and Vercel connector. Never hardcode tokens, team IDs, OAuth links, or personal repo/URL names — read them from the user's own connected tools at run time.

## Why host the video on a CDN
The deployed page is just a tiny `index.html`; the video streams from a CDN. This keeps the deploy payload small and the site fast. Heavy media never belongs in the deploy bundle.

## Step 7 — Host `web.mp4` on jsDelivr (public repo)

jsDelivr serves files from **public** GitHub repos with a global CDN, range requests (needed for scroll-seeking), and CORS — for free.

> Privacy: default to **private** for repos/projects. jsDelivr requires the asset repo to be **public**, so confirm with the user before creating it. (Only the small, non-sensitive video assets go here — not the site or any secrets.)

1. Create/choose a **public** repo under the user's own account and push the web video(s):
   ```bash
   # inside a scratch folder containing your web.mp4 (rename per project, e.g. mysite.mp4)
   git init -q && git add -A && git commit -q -m "Add background video"
   gh repo create <asset-repo> --public --source=. --push
   ```
2. Build the jsDelivr URL (pattern — substitute the user's own owner/repo):
   ```
   https://cdn.jsdelivr.net/gh/<owner>/<asset-repo>@<branch>/<file>.mp4
   ```
3. Verify it serves with range support before wiring it in:
   ```bash
   curl -sI -H "Range: bytes=0-100" "<jsdelivr-url>" | grep -iE "HTTP/|accept-ranges|content-type"
   # expect: 200/206, accept-ranges: bytes, content-type: video/mp4
   ```
4. Point `index.html`'s `<source src>` at the jsDelivr URL (keep a local `assets/scroll.mp4` fallback — the engine already falls back on error).

> jsDelivr caches per commit; `@main` is fine, or pin `@<commit-sha>` for immutability. New pushes may take a moment to propagate.

## Step 8 — Deploy the site to Vercel

> 🚦 **Explicit-approval gate.** Do not publish on your own initiative. Show the local preview, then ask the user directly for the go-ahead to publish and wait for an affirmative ("deploy it" / "ship it"). Praise for the design is not permission to publish. Only proceed after an explicit yes.

Deploy just `index.html` (the video is on the CDN) via the user's Vercel connector/MCP or the Vercel CLI — whichever they have connected.

- **Via a Vercel MCP/connector:** deploy the single `index.html` to a new production project under the user's own team. Discover the team from the connector (don't hardcode it).
- **Via CLI (if they prefer):** run the platform's deploy from the project folder using their own login.

After deploy:
- Report the **live URL**.
- New Vercel projects are commonly gated behind **Deployment Protection** (the URL redirects to a login) — this keeps it private. If the user wants it publicly viewable (e.g. to show prospects), tell them to turn off **Project → Settings → Deployment Protection**, or generate a shareable bypass link.

## Troubleshooting
- **403 "no permission to create a project"** → the connector's token lacks create rights, or 2FA/SSO needs completing on the user's side. Have them reconnect/authorize; do not ask for tokens.
- **Video 404 on the live site** → jsDelivr not propagated yet, wrong owner/repo/branch/path, or the repo is still private. Re-check the URL and that the repo is public.
- **Choppy scrub on deploy but smooth locally** → the deployed encode lost frequent keyframes; re-encode with `-g 6` (see pipeline.md).
