#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Techno CE — Variant A multi-page generator.
Emits one static HTML file per nav tab from a shared shell (head / nav /
footer / scripts) so the chrome stays consistent across all pages.
Run:  python build.py      (writes index.html + about/services/.../contact.html)
Output is plain static HTML — no runtime dependency.
"""
import io, os

BASE = "https://vivienbeautysg-max.github.io/techno-ce-sample/"
HERE = os.path.dirname(os.path.abspath(__file__))

# (key, label, file) — order = nav order
NAV_ITEMS = [
    ("about",    "About",    "about.html"),
    ("services", "Services", "services.html"),
    ("projects", "Projects", "projects.html"),
    ("showcase", "Showcase", "showcase.html"),
    ("media",    "Media",    "media.html"),
    ("newsroom", "Newsroom", "newsroom.html"),
    ("careers",  "Careers",  "careers.html"),
]

JSONLD = ('{"@context":"https://schema.org","@type":"GeneralContractor",'
    '"name":"Techno CE Pte Ltd","alternateName":"Techno CE","url":"%s",'
    '"logo":"%simg/logo.svg","foundingDate":"2002-12-20","numberOfEmployees":10,'
    '"identifier":"UEN 200210947C","address":{"@type":"PostalAddress",'
    '"streetAddress":"100 Lorong 23 Geylang #03-03 D\'Centennial",'
    '"addressLocality":"Singapore","postalCode":"388398","addressCountry":"SG"},'
    '"telephone":"+65-6745-5725","faxNumber":"+65-6745-5200",'
    '"email":"technoce@singnet.com.sg","areaServed":{"@type":"Country","name":"Singapore"},'
    '"hasCredential":["ISO 9001:2015","ISO 14001:2015",'
    '"BCA Green and Gracious Builder Award (Merit)","BCA CW02 Grade B2","BCA CW01 Grade C3"]}'
    ) % (BASE, BASE)


def head(title, desc, canon):
    return f'''<!doctype html>
<html lang="en-SG">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<script>(function(e){{e.className+=' js';try{{if(!matchMedia('(prefers-reduced-motion: reduce)').matches)e.className+=' motion';}}catch(x){{}}try{{if(sessionStorage.getItem('tce_seen'))e.className+=' no-intro';else sessionStorage.setItem('tce_seen','1');}}catch(x){{}}}})(document.documentElement);</script>
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="theme-color" content="#1F3A5F" />
<link rel="canonical" href="{BASE}{canon}" />
<link rel="icon" type="image/svg+xml" href="img/logo.svg" />
<link rel="apple-touch-icon" href="img/logo.svg" />
<meta property="og:type" content="website" />
<meta property="og:locale" content="en_SG" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{desc}" />
<meta property="og:image" content="{BASE}img/hero/01-sicc-golf.jpg" />
<meta property="og:url" content="{BASE}{canon}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{desc}" />
<meta name="twitter:image" content="{BASE}img/hero/01-sicc-golf.jpg" />
<script type="application/ld+json">
{JSONLD}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,200;0,300;0,400;0,500;0,600;0,700;1,300;1,400&family=Source+Serif+4:ital,opsz,wght@0,8..60,300;0,8..60,400;1,8..60,300;1,8..60,400;1,8..60,500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
'''

PRELUDE = '''
<div class="progress" aria-hidden="true"></div>
<div class="preloader" aria-hidden="true">
  <span class="preloader__brand"><img src="img/logo.svg" alt="" width="34" height="34" />Techno&nbsp;CE</span>
  <span class="preloader__bar"></span>
</div>

<a class="skip" href="#top">Skip to main content</a>
'''


def nav(active):
    out = ['<header class="nav" id="nav">',
           '  <a class="nav__logo" href="index.html" aria-label="Techno CE — home">',
           '    <img class="nav__mark" src="img/logo.svg" alt="" width="32" height="32" />',
           '    <span class="nav__name">TECHNO CE <span class="nav__name-pte">PTE LTD</span></span>',
           '  </a>',
           '  <nav class="nav__links">']
    for key, label, href in NAV_ITEMS:
        cur = ' class="is-active" aria-current="page"' if key == active else ''
        out.append(f'    <a href="{href}"{cur}>{label}</a>')
    cta_cur = ' aria-current="page"' if active == 'contact' else ''
    cta_cls = ' is-active' if active == 'contact' else ''
    out.append('    <a href="v2/" class="nav__variant" aria-label="View alternate design, Variant B"><span aria-hidden="true">⇆ B</span></a>')
    out.append(f'    <a href="contact.html" class="nav__cta{cta_cls}" data-magnetic="0.35"{cta_cur}>Get a Quote →</a>')
    out.append('  </nav>')
    out.append('  <button class="nav__burger" aria-label="Menu" id="burger"><span></span><span></span></button>')
    out.append('</header>')
    return "\n".join(out)


def pagehead(tag_right, title_html, sub, img):
    return f'''<section class="pagehead" style="--img:url('{img}')">
  <div class="rule rule--light pagehead__rule">
    <span class="rule-tag">TECHNO CE</span>
    <span class="rule-line"></span>
    <span class="rule-tag">{tag_right}</span>
  </div>
  <h1 class="pagehead__title">{title_html}</h1>
  <p class="pagehead__sub">{sub}</p>
</section>
'''

FOOTER = '''
<footer class="foot">
  <div class="foot__rule"></div>
  <div class="foot__cols">
    <div class="foot__col">
      <span class="foot__brand">TECHNO CE PTE LTD</span>
      <span>UEN 200210947C</span>
      <span>Incorporated 20 Dec 2002</span>
    </div>
    <div class="foot__col">
      <a href="about.html">About</a>
      <a href="services.html">Services</a>
      <a href="projects.html">Projects</a>
      <a href="showcase.html">Showcase</a>
    </div>
    <div class="foot__col">
      <a href="media.html">Media</a>
      <a href="newsroom.html">Newsroom</a>
      <a href="careers.html">Careers</a>
      <a href="contact.html">Contact</a>
    </div>
    <div class="foot__col foot__col--end">
      <span>100 Lorong 23 Geylang #03-03</span>
      <span>+65 6745 5725 · technoce@singnet.com.sg</span>
      <span>© 2026 Techno CE Pte Ltd</span>
      <a href="#top">Back to top ↑</a>
    </div>
  </div>
</footer>

<script src="app.js"></script>
<script src="premium.js"></script>
</body>
</html>
'''


def page(active, title, desc, canon, body):
    return head(title, desc, canon) + PRELUDE + nav(active) + '\n\n<main id="top">\n' + body + '\n</main>\n' + FOOTER


# ============================================================ CONTENT BLOCKS

HERO = '''<!-- HERO -->
<section class="hero">
  <div class="hero__media" id="heroMedia">
    <div class="hero__slide is-active" style="background-image:url('img/hero/01-sicc-golf.jpg')"></div>
    <div class="hero__slide" style="background-image:url('img/hero/02-erss-basin.jpg')"></div>
    <div class="hero__slide" style="background-image:url('img/hero/03-kingfisher-pavilion.jpg')"></div>
    <div class="hero__veil"></div>
  </div>
  <div class="hero__rule">
    <span class="rule-tag">TECHNO CE</span>
    <span class="rule-line"></span>
    <span class="rule-tag">SINGAPORE · EST. 2002</span>
  </div>
  <div class="hero__copy">
    <h1 class="hero__title">
      <span class="hero__line">We build,</span>
      <span class="hero__line">and we <em>take it</em> down.</span>
      <span class="hero__line hero__line--mut">Since 2002.</span>
    </h1>
    <div class="hero__meta">
      <div class="hero__badges">
        <span>BCA CW02 <b>B2</b></span>
        <span>BCA CW01 <b>C3</b></span>
        <span>ISO 9001</span>
        <span>ISO 14001</span>
        <span>Green &amp; Gracious <b>Merit</b></span>
      </div>
      <div class="hero__caption" id="heroCaption">
        <span class="caption-num">01 / 03</span>
        <span class="caption-text">Singapore Island Country Club — redevelopment, S$7.34M</span>
      </div>
    </div>
  </div>
  <a class="hero__scroll" href="#receipts">SCROLL ↓</a>
  <aside class="hero__live" role="status" aria-label="Current contract on site">
    <span class="hero__live-dot" aria-hidden="true"></span>
    <span class="hero__live-tag">CURRENT CONTRACT</span>
    <span class="hero__live-sep" aria-hidden="true">·</span>
    <span class="hero__live-job">DTSS Phase 2 — Flow Diversion &amp; Demolition, Contract 1</span>
    <span class="hero__live-sep" aria-hidden="true">·</span>
    <span class="hero__live-meta">PUB · CR03</span>
    <span class="hero__live-sep" aria-hidden="true">·</span>
    <span class="hero__live-meta">S$9.46M</span>
  </aside>
</section>
'''

RECEIPTS = '''<!-- RECEIPTS -->
<section class="receipts" id="receipts">
  <div class="rule">
    <span class="rule-tag">RECEIPTS</span>
    <span class="rule-line"></span>
    <span class="rule-tag">DELIVERED, NOT PROMISED</span>
  </div>
  <div class="receipts__grid">
    <div class="stat" aria-label="24 plus years">
      <div class="stat__num" aria-hidden="true"><span data-counter="24">0</span><sup>+</sup></div>
      <div class="stat__lbl">On site, since 2002</div>
    </div>
    <div class="stat" aria-label="34 projects">
      <div class="stat__num" aria-hidden="true"><span data-counter="34">0</span></div>
      <div class="stat__lbl">Projects delivered &amp; ongoing</div>
    </div>
    <div class="stat" aria-label="80.9 million Singapore dollars in contract value">
      <div class="stat__num" aria-hidden="true">S$<span data-counter="80.9" data-decimals="1">0</span>M</div>
      <div class="stat__lbl">Contract value, cumulative</div>
    </div>
    <div class="stat" aria-label="6 BCA workheads, all current">
      <div class="stat__num" aria-hidden="true"><span data-counter="6">0</span></div>
      <div class="stat__lbl">BCA workheads, all current</div>
    </div>
  </div>
</section>
'''

MANIFESTO = '''<!-- MANIFESTO -->
<section class="manifesto">
  <div class="rule">
    <span class="rule-tag">TWO HANDS, ONE PRACTICE</span>
    <span class="rule-line"></span>
    <span class="rule-tag">SINCE 2002</span>
  </div>
  <div class="manifesto__grid">
    <p class="manifesto__lead">
      From the demolition of the <em>Bedok NEWater Factory</em> to the timber pavilions at <em>Bay South</em>, Techno&nbsp;CE moves between the heavy and the delicate without changing gear.
    </p>
    <p class="manifesto__body">
      Twenty-four years on Singapore's sites — sheet piling for the country's reservoirs, earthworks for its golf clubs, demolition for its pumping stations, and the quiet finishing on its parks.
    </p>
  </div>
  <figure class="pullquote">
    <blockquote>
      We are <em>ten people.</em> We work for the agencies that build the country.
    </blockquote>
    <figcaption>— Techno CE Pte Ltd · Estd 2002 · Singapore</figcaption>
  </figure>
</section>
'''

EXPLORE = '''<!-- EXPLORE -->
<section class="explore">
  <div class="rule">
    <span class="rule-tag">EXPLORE</span>
    <span class="rule-line"></span>
    <span class="rule-tag">FIND YOUR WAY IN</span>
  </div>
  <div class="explore__grid">
    <a class="ex" href="about.html"><span class="ex__no">01</span><h3>About</h3><p>Vision, mission, core values and the people behind the practice.</p><span class="ex__go">Enter →</span></a>
    <a class="ex" href="services.html"><span class="ex__no">02</span><h3>Services</h3><p>Seven BCA workheads — civil, demolition, piling, RC, roads and recovery.</p><span class="ex__go">Enter →</span></a>
    <a class="ex" href="projects.html"><span class="ex__no">03</span><h3>Projects</h3><p>34 contracts for PUB, NParks, JTC, LTA and the country clubs.</p><span class="ex__go">Enter →</span></a>
    <a class="ex" href="showcase.html"><span class="ex__no">04</span><h3>Showcase</h3><p>Demolition, softscape, steel structure and the team behind it.</p><span class="ex__go">Enter →</span></a>
    <a class="ex" href="media.html"><span class="ex__no">05</span><h3>Media</h3><p>Site reels, time-lapses and features — our work in motion.</p><span class="ex__go">Enter →</span></a>
    <a class="ex" href="newsroom.html"><span class="ex__no">06</span><h3>Newsroom</h3><p>Latest from site — awards, milestones and sustainability.</p><span class="ex__go">Enter →</span></a>
    <a class="ex" href="careers.html"><span class="ex__no">07</span><h3>Careers</h3><p>A small team on real sites. Build something you can point to.</p><span class="ex__go">Enter →</span></a>
  </div>
</section>
'''

CLIENTS_ITEMS = ["PUB","NParks","JTC","LTA","MOE","Gardens by the Bay","Sentosa Development",
    "Sentosa Golf Club","SICC","Tanah Merah Country Club","Seletar Country Club","NSRCC",
    "Keppel Club","NTU","YTL PowerSeraya","China Railway First Group","TEHC International"]


def clients_block():
    a = "".join(f'      <span class="marquee__item">{x}</span>\n' for x in CLIENTS_ITEMS)
    b = "".join(f'      <span class="marquee__item marquee__dup" aria-hidden="true">{x}</span>\n' for x in CLIENTS_ITEMS)
    return ('''<!-- CLIENTS -->
<section class="clients">
  <div class="rule rule--light">
    <span class="rule-tag">CLIENTS</span>
    <span class="rule-line"></span>
    <span class="rule-tag">TRUSTED BY THE AGENCIES THAT BUILD SINGAPORE</span>
  </div>
  <div class="marquee" role="region" aria-label="Trusted by Singapore's public agencies and partners">
    <div class="marquee__track">
''' + a + b + '''    </div>
  </div>
</section>
''')

CTA_BAND = '''<!-- CTA BAND -->
<section class="cta-band">
  <a class="cta-band__link" href="contact.html">
    <span class="cta-band__eyebrow">Have a project?</span>
    <span class="cta-band__big">Let's talk <span aria-hidden="true">→</span></span>
  </a>
</section>
'''

CAPS = '''<!-- CAPABILITIES -->
<section class="caps" id="capabilities">
  <div class="rule">
    <span class="rule-tag">SEVEN WORKHEADS</span>
    <span class="rule-line"></span>
    <span class="rule-tag">SIX BCA-CURRENT + RECOVERY</span>
  </div>
  <div class="caps__grid">
    <article class="cap">
      <span class="cap__no">01</span>
      <h3>Civil Engineering &amp; Earthworks</h3>
      <p>Bulk earthwork, slope stabilisation, infrastructure works for JTC, NParks, PUB and country-club developments.</p>
      <span class="cap__grade">CW02 · Grade B2</span>
    </article>
    <article class="cap">
      <span class="cap__no">02</span>
      <h3>Demolition &amp; Reinstatement</h3>
      <p>Pumping stations, NEWater factories, power-station assets. Land returned to JTC ready-state. Our specialty.</p>
      <span class="cap__grade">CR03 · Single Grade</span>
    </article>
    <article class="cap">
      <span class="cap__no">03</span>
      <h3>Piling Works &amp; ERSS</h3>
      <p>Sheet piling and earth-retaining stabilising structures for reservoir, basement, and infrastructure works.</p>
      <span class="cap__grade">CR08 · L1 · SB(PW)</span>
    </article>
    <article class="cap">
      <span class="cap__no">04</span>
      <h3>Reinforced Concrete</h3>
      <p>Retaining walls, pond and waterfall structures, bridges and tunnels for golf clubs and parks.</p>
      <span class="cap__grade">CW01 · Grade C3</span>
    </article>
    <article class="cap">
      <span class="cap__no">05</span>
      <h3>Road, Pipe &amp; Premix</h3>
      <p>Cable / pipe laying, road reinstatement, asphalt premix and drainage works for LTA and developers.</p>
      <span class="cap__grade">CR07 · L1</span>
    </article>
    <article class="cap">
      <span class="cap__no">06</span>
      <h3>Waterproofing Installation</h3>
      <p>Waterproofing systems for buildings, basements and water-retaining structures.</p>
      <span class="cap__grade">CR13 · L1</span>
    </article>
    <article class="cap cap--recover">
      <span class="cap__no">07</span>
      <h3>Recycled Aggregate &amp; Recovery</h3>
      <p>On-site crusher and power screen turn demolition hardcore into clean, graded recycled aggregate — less to landfill, less hauled in. The circle closes on our own sites.</p>
      <span class="cap__grade">CIRCULAR · ON-SITE</span>
    </article>
  </div>
</section>
'''

WORK = '''<!-- SELECTED WORK -->
<section class="work" id="work">
  <div class="rule">
    <span class="rule-tag">SELECTED WORK</span>
    <span class="rule-line"></span>
    <span class="rule-tag">SCROLL →</span>
  </div>
  <div class="work__rail" id="workRail">
    <article class="card" style="--rot:-1deg">
      <div class="card__img" style="background-image:url('img/projects/demolition-pit.jpg')"></div>
      <div class="card__meta">
        <span class="card__year">2024 — Ongoing</span>
        <h4>DTSS Phase 2 — Flow Diversion &amp; Demolition, Contract 1</h4>
        <span class="card__owner">Public Utilities Board (PUB)</span>
        <span class="card__value">S$9,455,000</span>
      </div>
    </article>
    <article class="card" style="--rot:0.8deg">
      <div class="card__img" style="background-image:url('img/projects/golf-aerial.jpg')"></div>
      <div class="card__meta">
        <span class="card__year">2022</span>
        <h4>Sentosa Golf Club — Tanjong Course Redevelopment</h4>
        <span class="card__owner">Sentosa Golf Club</span>
        <span class="card__value">S$7,412,842</span>
      </div>
    </article>
    <article class="card" style="--rot:-0.6deg">
      <div class="card__img" style="background-image:url('img/projects/sentosa-pavilion.jpg')"></div>
      <div class="card__meta">
        <span class="card__year">2021</span>
        <h4>Singapore Island Country Club — Redevelopment</h4>
        <span class="card__owner">SICC</span>
        <span class="card__value">S$7,344,396</span>
      </div>
    </article>
    <article class="card" style="--rot:1.2deg">
      <div class="card__img" style="background-image:url('img/projects/tampines-boulevard.jpg')"></div>
      <div class="card__meta">
        <span class="card__year">2025 — Opened</span>
        <h4>Tampines Boulevard Park — 10.06 ha Park Construction</h4>
        <span class="card__owner">National Parks Board (NParks)</span>
        <span class="card__value">S$5,924,112</span>
      </div>
    </article>
    <article class="card" style="--rot:-0.9deg">
      <div class="card__img" style="background-image:url('img/projects/bulim-landscape.jpg')"></div>
      <div class="card__meta">
        <span class="card__year">2023 — Ongoing</span>
        <h4>Bulim Phase 1 — Landscape &amp; Associated Works</h4>
        <span class="card__owner">JTC Corporation</span>
        <span class="card__value">S$4,221,332</span>
      </div>
    </article>
    <article class="card" style="--rot:0.4deg">
      <div class="card__img" style="background-image:url('img/projects/kingfisher-bridge.jpg')"></div>
      <div class="card__meta">
        <span class="card__year">2019</span>
        <h4>Kingfisher Wetland — Bay South, Gardens by the Bay</h4>
        <span class="card__owner">Gardens by the Bay</span>
        <span class="card__value">S$436,500</span>
      </div>
    </article>
    <article class="card" style="--rot:-1.1deg">
      <div class="card__img" style="background-image:url('img/projects/sun-plaza.jpg')"></div>
      <div class="card__meta">
        <span class="card__year">2024 — Ongoing</span>
        <h4>Sun Plaza Park — Inclusive Playground (5y maint.)</h4>
        <span class="card__owner">National Parks Board (NParks)</span>
        <span class="card__value">S$3,554,747</span>
      </div>
    </article>
    <article class="card" style="--rot:0.7deg">
      <div class="card__img" style="background-image:url('img/projects/margaret-drive.jpg')"></div>
      <div class="card__meta">
        <span class="card__year">2020</span>
        <h4>Margaret Drive — External Premix &amp; Drainage</h4>
        <span class="card__owner">LTA / Margaret Ville</span>
        <span class="card__value">S$695,577</span>
      </div>
    </article>
    <article class="card card--summary">
      <div class="card__sum">
        <span class="card__sum-num">+26</span>
        <span class="card__sum-lbl">More projects across<br>PUB · NParks · JTC · LTA · MOE · Sentosa Dev · Keppel · NTU · YTL PowerSeraya</span>
        <button type="button" class="card__sum-link" data-action="register">Open full register <span aria-hidden="true">→</span></button>
      </div>
    </article>
  </div>
</section>
'''

SHOWCASE = '''<!-- SHOWCASE -->
<section class="showcase" id="showcase">
  <div class="rule">
    <span class="rule-tag">SHOWCASE</span>
    <span class="rule-line"></span>
    <span class="rule-tag">WHAT WE'RE KNOWN FOR</span>
  </div>
  <div class="showcase__tabs" role="tablist" aria-label="Showcase categories">
    <button class="showcase__tab is-on" role="tab" aria-selected="true" id="sc-tab-demo" aria-controls="sc-panel-demo" data-panel="demo"><span class="showcase__tab-no">A</span>Demolition</button>
    <button class="showcase__tab" role="tab" aria-selected="false" tabindex="-1" id="sc-tab-soft" aria-controls="sc-panel-soft" data-panel="soft"><span class="showcase__tab-no">B</span>Softscape</button>
    <button class="showcase__tab" role="tab" aria-selected="false" tabindex="-1" id="sc-tab-steel" aria-controls="sc-panel-steel" data-panel="steel"><span class="showcase__tab-no">C</span>Steel Structure</button>
    <button class="showcase__tab" role="tab" aria-selected="false" tabindex="-1" id="sc-tab-team" aria-controls="sc-panel-team" data-panel="team"><span class="showcase__tab-no">D</span>Team Spirit &amp; Well-being</button>
  </div>
  <div class="showcase__panel is-on" role="tabpanel" id="sc-panel-demo" aria-labelledby="sc-tab-demo" data-panel="demo">
    <div class="showcase__lead">
      <h3>Demolition</h3>
      <p>Heavy take-down on live, constrained sites — pumping stations, NEWater factories and power-station assets, brought down safely and returned to ready-state.</p>
      <div class="showcase__chips"><span>ERSS</span><span>Deep Basement</span><span>Tall Steel Structure</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('img/projects/demolition-pit.jpg')"><figcaption>ERSS &amp; deep-basement removal</figcaption></figure>
      <figure class="sc-tile" style="--img:url('img/hero/02-erss-basin.jpg')"><figcaption>Sheet-piled ERSS basin</figcaption></figure>
      <figure class="sc-tile" style="--img:url('img/projects/golf-aerial.jpg')"><figcaption>Site clearance &amp; earthwork</figcaption></figure>
    </div>
  </div>
  <div class="showcase__panel" role="tabpanel" id="sc-panel-soft" aria-labelledby="sc-tab-soft" data-panel="soft" hidden>
    <div class="showcase__lead">
      <h3>Softscape</h3>
      <p>The delicate end of the practice — parks, gardens and waterfront landscapes built to last and to be lived in, for NParks and Gardens by the Bay.</p>
      <div class="showcase__chips"><span>Boardwalk</span><span>Stone-clad Wall</span><span>Shelters</span><span>Ponds &amp; Wetlands</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('img/projects/kingfisher-bridge.jpg')"><figcaption>Timber boardwalk &amp; arched bridge</figcaption></figure>
      <figure class="sc-tile" style="--img:url('img/projects/bulim-landscape.jpg')"><figcaption>Landscape &amp; stone-clad walls</figcaption></figure>
      <figure class="sc-tile" style="--img:url('img/projects/tampines-boulevard.jpg')"><figcaption>Tampines Boulevard Park, 10.06 ha</figcaption></figure>
    </div>
  </div>
  <div class="showcase__panel" role="tabpanel" id="sc-panel-steel" aria-labelledby="sc-tab-steel" data-panel="steel" hidden>
    <div class="showcase__lead">
      <h3>Steel Structure</h3>
      <p>Shelters, pavilions and walkway roofs — fabricated and erected to BCA SB(SS) standard, married to the civil works underneath them.</p>
      <div class="showcase__chips"><span>ERSS</span><span>Shelters</span><span>Pavilions</span><span>Walkway Roofs</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('img/hero/03-kingfisher-pavilion.jpg')"><figcaption>Kingfisher pavilion, Bay South</figcaption></figure>
      <figure class="sc-tile" style="--img:url('img/projects/sentosa-pavilion.jpg')"><figcaption>Course pavilion &amp; shelter</figcaption></figure>
      <figure class="sc-tile" style="--img:url('img/projects/sun-plaza.jpg')"><figcaption>Inclusive playground steelwork</figcaption></figure>
    </div>
  </div>
  <div class="showcase__panel" role="tabpanel" id="sc-panel-team" aria-labelledby="sc-tab-team" data-panel="team" hidden>
    <div class="showcase__lead">
      <h3>Team Spirit &amp; Well-being</h3>
      <p>Ten people, long timesheets, one studio — and the outings, feasts and celebrations that keep a small team together year after year.</p>
      <div class="showcase__chips"><span>Company Outings</span><span>Durian Fest</span><span>D&amp;D Night</span><span>Family Day</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile sc-tile--ph"><span class="sc-tile__ico" aria-hidden="true">🚌</span><figcaption>Company outings — photos to be added</figcaption></figure>
      <figure class="sc-tile sc-tile--ph"><span class="sc-tile__ico" aria-hidden="true">🍴</span><figcaption>Annual durian fest — photos to be added</figcaption></figure>
      <figure class="sc-tile sc-tile--ph"><span class="sc-tile__ico" aria-hidden="true">🎉</span><figcaption>Dinner &amp; Dance — photos to be added</figcaption></figure>
    </div>
  </div>
</section>
'''

MEDIA = '''<!-- MEDIA -->
<section class="media" id="media">
  <div class="rule">
    <span class="rule-tag">MEDIA</span>
    <span class="rule-line"></span>
    <span class="rule-tag">SEE US IN MOTION</span>
  </div>
  <div class="media__intro">
    <p class="media__lead">Our work moves — site reels, project time-lapses and the moments the agencies don't get to see.</p>
    <p class="media__note">Sample tiles · final cuts to be embedded — TikTok, news features and our own production.</p>
  </div>
  <div class="media__grid">
    <button class="vtile" type="button" aria-label="Play sample: site reel (placeholder)">
      <span class="vtile__img" style="--img:url('img/projects/demolition-pit.jpg')"></span>
      <span class="vtile__play" aria-hidden="true"></span>
      <span class="vtile__meta"><b>Own Production</b><span>Demolition site reel · 0:45</span></span>
    </button>
    <button class="vtile" type="button" aria-label="Play sample: news feature (placeholder)">
      <span class="vtile__img" style="--img:url('img/projects/tampines-boulevard.jpg')"></span>
      <span class="vtile__play" aria-hidden="true"></span>
      <span class="vtile__meta"><b>In the Media</b><span>Tampines Boulevard Park opening</span></span>
    </button>
    <button class="vtile" type="button" aria-label="Play sample: TikTok clip (placeholder)">
      <span class="vtile__img" style="--img:url('img/projects/kingfisher-bridge.jpg')"></span>
      <span class="vtile__play" aria-hidden="true"></span>
      <span class="vtile__meta"><b>TikTok · @technoce</b><span>Building Bay South, in 30 seconds</span></span>
    </button>
  </div>
</section>
'''

CREDS = '''<!-- CREDENTIALS -->
<section class="creds" id="credentials">
  <div class="rule">
    <span class="rule-tag">CREDENTIALS</span>
    <span class="rule-line"></span>
    <span class="rule-tag">VERIFIABLE · CURRENT</span>
  </div>
  <div class="creds__grid">
    <div class="creds__certs">
      <figure style="--rot:-2deg"><img src="img/certs/iso-9001.jpg" alt="ISO 9001:2015 — Quality Management"></figure>
      <figure style="--rot:1.5deg"><img src="img/certs/iso-14001.jpg" alt="ISO 14001:2015 — Environmental Management"></figure>
      <figure style="--rot:-1deg"><img src="img/certs/green-gracious.png" alt="BCA Green and Gracious Builder Award — Merit"></figure>
      <figure style="--rot:2deg"><img src="img/certs/progressive-wage.png" alt="Progressive Wage Mark — MOM"></figure>
    </div>
    <div class="creds__table">
      <h3 id="bca-workheads">BCA Registered Workheads</h3>
      <table aria-labelledby="bca-workheads">
        <caption class="sr-only">Six BCA-registered workheads, all valid until July 2027.</caption>
        <thead><tr><th scope="col">Code</th><th scope="col">Workhead</th><th scope="col">Grade</th><th scope="col">Valid until</th></tr></thead>
        <tbody>
          <tr><th scope="row">CW01</th><td>General Building</td><td><b>C3</b></td><td>2027/07</td></tr>
          <tr><th scope="row">CW02</th><td>Civil Engineering</td><td><b>B2</b></td><td>2027/07</td></tr>
          <tr><th scope="row">CR03</th><td>Demolition</td><td>Single</td><td>2027/07</td></tr>
          <tr><th scope="row">CR07</th><td>Cable / Pipe Laying</td><td>L1</td><td>2027/07</td></tr>
          <tr><th scope="row">CR08</th><td>Piling Works</td><td>L1</td><td>2027/07</td></tr>
          <tr><th scope="row">CR13</th><td>Waterproofing</td><td>L1</td><td>2027/07</td></tr>
        </tbody>
      </table>
      <h3 id="lic-builder" style="margin-top:2rem">Licensed Builder</h3>
      <table aria-labelledby="lic-builder">
        <caption class="sr-only">Three BCA Licensed Builder licences.</caption>
        <thead><tr><th scope="col">Licence</th><th scope="col">Description</th><th scope="col">Valid until</th></tr></thead>
        <tbody>
          <tr><th scope="row">GB1</th><td>General Builder Class 1</td><td>24/12/2026</td></tr>
          <tr><th scope="row">SB(PW)</th><td>Specialist · Piling Works</td><td>07/11/2027</td></tr>
          <tr><th scope="row">SB(SS)</th><td>Specialist · Structural Steelwork</td><td>20/11/2028</td></tr>
        </tbody>
      </table>
      <p class="creds__verify">
        Verify on <a href="https://www1.bca.gov.sg/bca-directory" target="_blank" rel="noopener">BCA Directory →</a>
        UEN <code>200210947C</code>
      </p>
    </div>
  </div>
</section>
'''

ABOUT_BODY = '''<!-- VISION / MISSION / MOTTO -->
<section class="about about--page" id="about">
  <div class="rule rule--light">
    <span class="rule-tag">VISION · MISSION · MOTTO</span>
    <span class="rule-line"></span>
    <span class="rule-tag">WHO WE ARE</span>
  </div>
  <div class="about__grid">
    <div class="about__col">
      <span class="about__lbl">Vision</span>
      <h3>Take pride<br/>in every job.</h3>
      <p class="about__col-sub">To be the specialist Singapore's agencies trust for the work that is hard to build — and harder to take down.</p>
    </div>
    <div class="about__col">
      <span class="about__lbl">Mission</span>
      <h3>Build it,<br/>and leave it better.</h3>
      <p class="about__col-sub">To deliver every civil, demolition and landscape contract safely, cleanly and on time — returning each site better than we found it.</p>
    </div>
    <div class="about__col">
      <span class="about__lbl">Motto</span>
      <h3 class="about__motto"><em>Mission Possible.</em></h3>
      <p class="about__col-sub">Twenty-four years of saying yes to the contracts others walk away from.</p>
    </div>
  </div>
  <div class="values" id="values">
    <div class="values__head">
      <span class="about__lbl">Core Values</span>
      <h3 class="values__title">Five things we don't compromise.</h3>
    </div>
    <ol class="values__list">
      <li><span class="values__no">01</span><h4>Safety First</h4><p>Everyone goes home. No job is worth a shortcut.</p></li>
      <li><span class="values__no">02</span><h4>Integrity</h4><p>We keep our word, and we keep our records.</p></li>
      <li><span class="values__no">03</span><h4>Craftsmanship</h4><p>Heavy or delicate — built to last, finished by hand.</p></li>
      <li><span class="values__no">04</span><h4>Sustainability</h4><p>We recycle what we remove — hardcore back to aggregate.</p></li>
      <li><span class="values__no">05</span><h4>Our People</h4><p>A small team, on payroll, on our own sites.</p></li>
    </ol>
  </div>
  <p class="about__foot">
    Techno&nbsp;CE&nbsp;Pte&nbsp;Ltd was incorporated on 20 December 2002 (UEN 200210947C). Civil-engineering specialist, BCA grade B2 in CW02 and C3 in CW01, certified to ISO 9001 and ISO 14001, and recognised under the BCA Green &amp; Gracious Builder Award and the Progressive Wage Mark.
  </p>
</section>
'''

NEWS = '''<!-- NEWSROOM -->
<section class="news" id="newsroom">
  <div class="rule">
    <span class="rule-tag">NEWSROOM</span>
    <span class="rule-line"></span>
    <span class="rule-tag">LATEST FROM SITE</span>
  </div>
  <div class="news__grid">
    <article class="post">
      <span class="post__date">Feb 2025</span>
      <h3>Tampines Boulevard Park opens to the public</h3>
      <p>Our 10.06-hectare park construction for NParks — across two sections split by Tampines Avenue 12 — officially opened on 22 February 2025.</p>
      <span class="post__tag">Project · NParks</span>
    </article>
    <article class="post">
      <span class="post__date">2024</span>
      <h3>Awarded PUB DTSS Phase 2 — Flow Diversion &amp; Demolition</h3>
      <p>Techno CE is appointed for Contract 1 of the Deep Tunnel Sewerage System Phase 2 — decommissioning used-water pumping installations and removing sheet-piled basements.</p>
      <span class="post__tag">Contract · PUB</span>
    </article>
    <article class="post">
      <span class="post__date">Ongoing</span>
      <h3>Closing the loop: on-site crusher &amp; power screen</h3>
      <p>We're processing demolition hardcore into recycled aggregate on our own sites — cutting both landfill and the lorries hauling new stone in.</p>
      <span class="post__tag">Sustainability</span>
    </article>
    <article class="post">
      <span class="post__date">Recognised</span>
      <h3>BCA Green &amp; Gracious Builder — Merit</h3>
      <p>Recognised for environmental care and good site conduct, alongside our ISO 9001, ISO 14001 and Progressive Wage Mark.</p>
      <span class="post__tag">Award · BCA</span>
    </article>
  </div>
  <p class="news__note">Sample headlines drawn from real milestones — to be replaced with live posts &amp; media coverage.</p>
</section>
'''

CAREERS = '''<!-- CAREERS -->
<section class="careers" id="careers">
  <div class="rule">
    <span class="rule-tag">CAREERS</span>
    <span class="rule-line"></span>
    <span class="rule-tag">BUILD WITH US</span>
  </div>
  <div class="careers__grid">
    <div class="careers__intro">
      <h3>A small team, on real sites.</h3>
      <p>We don't subcontract our project management — we are on the sites we build. If you want responsibility early, fair wages and work you can point to from the road, talk to us.</p>
      <p class="careers__perk">Progressive Wage Mark employer · structured training · on-site mentoring</p>
    </div>
    <ul class="careers__roles">
      <li><span class="careers__role-k">Open</span><h4>Project Engineer — Civil &amp; Demolition</h4><span class="careers__loc">Geylang HQ &amp; sites · Full-time</span></li>
      <li><span class="careers__role-k">Open</span><h4>Site Supervisor</h4><span class="careers__loc">Island-wide sites · Full-time</span></li>
      <li><span class="careers__role-k">Open</span><h4>Quantity Surveyor</h4><span class="careers__loc">Geylang HQ · Full-time</span></li>
      <li><span class="careers__role-k">Talent pool</span><h4>Plant &amp; Machinery Operator</h4><span class="careers__loc">Crusher / excavator · Sites</span></li>
    </ul>
  </div>
  <a class="careers__cta" href="mailto:technoce@singnet.com.sg?subject=Career%20enquiry%20%E2%80%94%20Techno%20CE">
    Send your CV to technoce@singnet.com.sg <span aria-hidden="true">→</span>
  </a>
  <p class="news__note">Sample roles · final openings to be confirmed by Techno CE.</p>
</section>
'''

CONTACT_BODY = '''<!-- CONTACT -->
<section class="contact contact--page" id="contact">
  <div class="rule">
    <span class="rule-tag">CONTACT</span>
    <span class="rule-line"></span>
    <span class="rule-tag">WE READ EVERY BRIEF</span>
  </div>
  <div class="contact__grid">
    <div>
      <span class="contact__lbl">Phone</span>
      <a href="tel:+6567455725">+65 6745 5725</a>
      <span class="contact__sub">Fax · 6745 5200</span>
    </div>
    <div>
      <span class="contact__lbl">Email</span>
      <a href="mailto:technoce@singnet.com.sg">technoce@singnet.com.sg</a>
    </div>
    <div>
      <span class="contact__lbl">Office</span>
      <a href="https://maps.google.com/?q=100+Lorong+23+Geylang+%2303-03+D'Centennial+Singapore+388398" target="_blank" rel="noopener">100 Lorong 23 Geylang<br/>#03-03 D'Centennial<br/>Singapore 388398</a>
    </div>
  </div>
  <a class="contact__cta" href="https://www1.bca.gov.sg/bca-directory" target="_blank" rel="noopener">
    Verify Techno CE on the BCA Directory <span>→</span>
  </a>
</section>
'''

# ============================================================ PAGES

PAGES = {
 "index.html": page("home",
    "Techno CE — Civil engineering, Singapore. Since 2002.",
    "Techno CE Pte Ltd is a Singapore civil engineering firm — demolition, piling, earthworks, RC works, road &amp; landscape construction. BCA CW02 B2 / CW01 C3. ISO 9001 &amp; 14001.",
    "", HERO + RECEIPTS + MANIFESTO + EXPLORE + clients_block() + CTA_BAND),

 "about.html": page("about",
    "About — Techno CE",
    "Vision, mission, motto and core values of Techno CE Pte Ltd — a ten-person Singapore civil engineering practice since 2002.",
    "about.html",
    pagehead("ABOUT", "Two hands,<br>one practice.",
        "A ten-person Singapore practice that moves between the heavy and the delicate without changing gear.",
        "img/hero/01-sicc-golf.jpg")
    + MANIFESTO + ABOUT_BODY + CREDS),

 "services.html": page("services",
    "Services — Techno CE",
    "Seven BCA workheads: civil engineering, demolition, piling &amp; ERSS, reinforced concrete, roads, waterproofing and on-site recycled aggregate recovery.",
    "services.html",
    pagehead("SERVICES", "Seven Workheads",
        "Six BCA-current workheads — and a crusher line that closes the loop.",
        "img/projects/demolition-pit.jpg")
    + CAPS),

 "projects.html": page("projects",
    "Projects — Techno CE",
    "34 contracts, S$80.9M delivered &amp; ongoing for PUB, NParks, JTC, LTA, MOE, Sentosa, SICC and the country clubs.",
    "projects.html",
    pagehead("PROJECTS", "Present &amp; Past",
        "34 contracts for the agencies that build Singapore.",
        "img/projects/golf-aerial.jpg")
    + WORK),

 "showcase.html": page("showcase",
    "Showcase — Techno CE",
    "What we're known for: demolition, softscape, steel structure, and the team behind it all.",
    "showcase.html",
    pagehead("SHOWCASE", "What We're Known For",
        "Four sides of the practice — pick one.",
        "img/hero/03-kingfisher-pavilion.jpg")
    + SHOWCASE),

 "media.html": page("media",
    "Media — Techno CE",
    "Our work in motion — site reels, project time-lapses, news features and our own production.",
    "media.html",
    pagehead("MEDIA", "See Us In Motion",
        "Site reels, time-lapses and the moments the agencies don't see.",
        "img/projects/tampines-boulevard.jpg")
    + MEDIA),

 "newsroom.html": page("newsroom",
    "Newsroom — Techno CE",
    "Latest from site — awards, project milestones and sustainability news from Techno CE.",
    "newsroom.html",
    pagehead("NEWSROOM", "Latest From Site",
        "Awards, milestones and what's new on our sites.",
        "img/projects/bulim-landscape.jpg")
    + NEWS),

 "careers.html": page("careers",
    "Careers — Techno CE",
    "Join a small team on real sites. Progressive Wage Mark employer, structured training, on-site mentoring.",
    "careers.html",
    pagehead("CAREERS", "Build With Us",
        "Responsibility early, fair wages, and work you can point to.",
        "img/projects/sun-plaza.jpg")
    + CAREERS),

 "contact.html": page("contact",
    "Contact — Techno CE",
    "Have a project? Phone +65 6745 5725, email technoce@singnet.com.sg, office at 100 Lorong 23 Geylang.",
    "contact.html",
    pagehead("CONTACT", "Have A Project?",
        "We read every brief. Tell us what you're building — or taking down.",
        "img/projects/sentosa-pavilion.jpg")
    + CONTACT_BODY + clients_block()),
}


def main():
    for fname, html in PAGES.items():
        with io.open(os.path.join(HERE, fname), "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        print("wrote", fname, len(html), "bytes")


if __name__ == "__main__":
    main()
