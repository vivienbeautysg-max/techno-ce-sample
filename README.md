# Techno CE — Website Sample

Static multi-page site for **Techno CE Pte Ltd** (UEN 200210947C), a Singapore
civil engineering firm. Sample build for client review — two design directions.

- **Variant A** (root) — "Industrial Editorial", dark navy. → `index.html`, `about.html`, `services.html`, `projects.html`, `showcase.html`, `media.html`, `newsroom.html`, `careers.html`, `contact.html`
- **Variant B** (`v2/`) — "Quiet Practice", light editorial. → same 9 pages under `v2/`

Each variant is **9 separate pages** (one per nav tab): Home · About · Services ·
Projects · Showcase · Media · Newsroom · Careers · Contact.

## Files
- `build.py` — generator for Variant A pages (run: `python build.py`)
- `v2/build.py` — generator for Variant B pages (run from inside `v2/`)
- `style.css` / `v2/style.css` — design systems + premium motion layer
- `app.js` — core JS (hero, counters, showcase tabs, register modal, burger, nav pin)
- `premium.js` — shared premium motion: intro preloader, scroll progress, reveal
  choreography, hero parallax, scrollspy, magnetic buttons, custom cursor.
  (Variant B overrides reveal targets via `window.TCE_REVEAL_GROUPS`.)
- `projects.json` — shared full project register
- `img/` — curated photography

> The `.html` pages are **generated** by the `build.py` scripts. Edit content in
> the generator, then re-run it — don't hand-edit the pages.

## Motion
Dependency-free, GPU-friendly, fully `prefers-reduced-motion`-safe (reduced-motion
users get instant content, no looping). The intro plays once per session. If JS
fails to load, content is never hidden.

## Placeholder content (replace with real assets)
- **Media** video tiles — mock thumbnails; embed real TikTok / news / own-production.
- **Newsroom** posts — drawn from real milestones, but copy is draft.
- **Careers** roles — sample openings, to be confirmed by Techno CE.
- **Team Spirit** tiles — awaiting real outing / durian-fest / D&D photos.
- Improved Vision / Mission / Motto / Core Values — proposed drafts for approval.
