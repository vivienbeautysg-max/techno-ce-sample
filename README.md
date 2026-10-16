# Techno CE — Website Sample

Static multi-page site for **Techno CE Pte Ltd** (UEN 200210947C), a Singapore
civil engineering firm. Design: "Quiet Practice", light editorial.

- **The client chose Variant B (Oct 2026)** — it is now the site, at the root:
  `index.html`, `about.html`, `services.html`, `projects.html`, `newsroom.html`, `careers.html`, `contact.html`
- `v2/` holds only redirect stubs, so old Variant B links keep working.
- The dark **Variant A** is retired; its last version is git tag `variant-a-final`.

The site is **7 separate pages**, following the client's framework (Oct 2026):
Home · About Us · Services · Projects (a glimpse) · Newsroom · Careers · Contact Us.
Services = four specialities — Civil Engineering, Demolition, Hardscape, Steel Structures.
No golf-course photography (client request: it implies golf-course work).

## Files
- `build.py` — generator for all pages + `v2/` redirect stubs (run: `python build.py`)
- `style.css` — design system + premium motion layer
- `app.js` — core JS (hero, counters, register modal, burger, nav pin)
- `premium.js` — premium motion: intro preloader, scroll progress, reveal
  choreography, hero parallax, scrollspy, magnetic buttons, custom cursor.
  (Reveal targets are set per page via `window.TCE_REVEAL_GROUPS`.)
- `projects.json` — full project register (30 contracts, transcribed from the
  Company Profile 2026 Revision 1, pp. 31–33)
- `img/` — curated photography. Sources: `X:\TCE\TCE_Company Profile_2026_R1.pdf`
  (extracted to `X:\TCE\_extracted_r1\`) and higher-resolution originals of the same
  photos from the Mar 2026 profile (`X:\TCE\_extracted\`). Never upscaled.
  - Home hero: 4:5 portrait (`hero/b*.jpg`) + 5:4 landscape (`-l.jpg`, ≤1100px)
    via `<picture>`. Any future full-bleed slot must use the 3300–4400px originals.
  - Speciality tiles 4:3 ≤960w (`t-*.jpg`), project cards 4:5 ≤900×1125 (`c-*.jpg`).
  - Low-resolution R1 photos (≈700–850px, e.g. Magical Bridge) are used only at card
    or tile size, never full-bleed.

## Photo-fit check (run after any image or layout change)
Open any page of the local preview, then in the browser console:
`await import('/tools/img-audit.js'); (await TCE_imgAudit()).filter(r => !r.ok)`
(or load the file with a `<script>` tag). It renders all 7 pages at 8 screen sizes
(1280×800@1 … 375×812@3) and lists every photo that would be shown larger than its
pixels (×1.25) or cropped below 40%. Expected result: an empty list.

> The `.html` pages are **generated** by the `build.py` scripts. Edit content in
> the generator, then re-run it — don't hand-edit the pages.

## Motion
Dependency-free, GPU-friendly, fully `prefers-reduced-motion`-safe (reduced-motion
users get instant content, no looping). The intro plays once per session. If JS
fails to load, content is never hidden.

## Placeholder content (replace with real assets)
- **Newsroom** posts — drawn from real milestones, but copy is draft.
- **Careers** roles — sample openings, to be confirmed by Techno CE.
- Certificates on site are the renewed ones from the R1 profile (ISO to May 2029,
  bizSAFE Star to May 2029, Green & Gracious to May 2027, PWM to Apr 2027).
