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
    ("about",    "About Us", "about.html"),
    ("services", "Services", "services.html"),
    ("projects", "Projects", "projects.html"),
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
    '"hasCredential":["ISO 9001:2015","ISO 14001:2015","ISO 45001:2018",'
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
<meta property="og:image" content="{BASE}img/hero/02-erss-basin.jpg" />
<meta property="og:url" content="{BASE}{canon}" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{title}" />
<meta name="twitter:description" content="{desc}" />
<meta name="twitter:image" content="{BASE}img/hero/02-erss-basin.jpg" />
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
    out.append(f'    <a href="contact.html" class="nav__cta{cta_cls}" data-magnetic="0.35"{cta_cur}>Contact Us →</a>')
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
      <a href="about.html">About Us</a>
      <a href="services.html">Services</a>
      <a href="projects.html">Projects</a>
    </div>
    <div class="foot__col">
      <a href="newsroom.html">Newsroom</a>
      <a href="careers.html">Careers</a>
      <a href="contact.html">Contact Us</a>
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
    <div class="hero__slide is-active" style="background-image:url('img/hero/02-erss-basin.jpg')"></div>
    <div class="hero__slide" style="background-image:url('img/projects/abc-jurong-steps.jpg')"></div>
    <div class="hero__slide" style="background-image:url('img/projects/sun-plaza.jpg')"></div>
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
        <span>ISO 45001</span>
        <span>Green &amp; Gracious <b>Merit</b></span>
      </div>
      <div class="hero__caption" id="heroCaption">
        <span class="caption-num">01 / 03</span>
        <span class="caption-text">Deep-basement removal in sheet-piled ERSS — Mugliston Park Pumping Station, PUB</span>
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
      Twenty-four years on Singapore's sites — demolition and deep-basement removal for its pumping stations, grouting of its disused pipelines, steel structures for its parks and waterways, and the hardscape people walk on.
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
    <a class="ex" href="about.html"><span class="ex__no">01</span><h3>About Us</h3><p>Vision, mission, core values and our awards &amp; certifications.</p><span class="ex__go">Enter →</span></a>
    <a class="ex" href="services.html"><span class="ex__no">02</span><h3>Services</h3><p>Civil engineering, demolition, hardscape and steel structures.</p><span class="ex__go">Enter →</span></a>
    <a class="ex" href="projects.html"><span class="ex__no">03</span><h3>Projects</h3><p>A glimpse — Magical Bridge, ABC Waters and PUB's pumping stations.</p><span class="ex__go">Enter →</span></a>
    <a class="ex" href="newsroom.html"><span class="ex__no">04</span><h3>Newsroom</h3><p>Latest from site — openings, contracts and certifications.</p><span class="ex__go">Enter →</span></a>
    <a class="ex" href="careers.html"><span class="ex__no">05</span><h3>Careers</h3><p>A small team on real sites. Build something you can point to.</p><span class="ex__go">Enter →</span></a>
    <a class="ex" href="contact.html"><span class="ex__no">06</span><h3>Contact Us</h3><p>Phone, email and our Geylang office. We read every brief.</p><span class="ex__go">Enter →</span></a>
  </div>
</section>
'''

CLIENTS_ITEMS = ["PUB","NParks","JTC","LTA","MOE","Gardens by the Bay","Sentosa Development",
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

SPECIALITIES = '''<!-- SPECIALITIES -->
<section class="showcase showcase--stack" id="specialities">
  <div class="rule">
    <span class="rule-tag">OUR SPECIALITIES</span>
    <span class="rule-line"></span>
    <span class="rule-tag">FOUR DISCIPLINES</span>
  </div>
  <div class="showcase__panel" id="civil">
    <div class="showcase__lead">
      <h3>Civil Engineering</h3>
      <p>Earthworks, sheet-piled ERSS, slope stabilisation, drainage and road reinstatement — the groundwork beneath Singapore's public infrastructure.</p>
      <div class="showcase__chips"><span>Earthworks</span><span>ERSS &amp; Sheet Piling</span><span>Slope Stabilisation</span><span>Drainage &amp; Premix</span><span>BCA CW02 · B2</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('img/hero/02-erss-basin.jpg')"><figcaption>Sheet-piled ERSS with strutting — Mugliston Park Pumping Station</figcaption></figure>
      <figure class="sc-tile" style="--img:url('img/projects/margaret-drive.jpg')"><figcaption>External works, premix &amp; drainage — Margaret Drive</figcaption></figure>
      <figure class="sc-tile" style="--img:url('img/projects/tampines-boulevard.jpg')"><figcaption>Earthworks &amp; park infrastructure — Tampines Boulevard Park</figcaption></figure>
    </div>
  </div>
  <div class="showcase__panel" id="demolition">
    <div class="showcase__lead">
      <h3>Demolition</h3>
      <p>Pumping stations, NEWater factories and power-station assets — taken down safely on live, constrained sites. Deep basements removed inside sheet-piled ERSS, disused pipelines grouted, and hardcore crushed on site into recycled aggregate.</p>
      <div class="showcase__chips"><span>Deep Basement</span><span>Grouting</span><span>Pumping Stations</span><span>Recycled Aggregate</span><span>BCA CR03</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('img/projects/demolition-longreach.jpg')"><figcaption>Long-reach demolition of a steel-framed structure</figcaption></figure>
      <figure class="sc-tile" style="--img:url('img/projects/demolition-basement.jpg')"><figcaption>Breaking out a deep basement</figcaption></figure>
      <figure class="sc-tile" style="--img:url('img/projects/demolition-pit.jpg')"><figcaption>Basement removal inside ERSS — Mugliston Park Pumping Station</figcaption></figure>
    </div>
  </div>
  <div class="showcase__panel" id="hardscape">
    <div class="showcase__lead">
      <h3>Hardscape</h3>
      <p>Rubble walls, boardwalks, stone-clad steps and paving — the hard surfaces people walk on, built for parks, gardens and waterways.</p>
      <div class="showcase__chips"><span>Rubble Wall</span><span>Boardwalk</span><span>Stone-clad Walls &amp; Steps</span><span>Paving</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('img/projects/kingfisher-bridge.jpg')"><figcaption>Boardwalk &amp; rock-edged pond — Kingfisher Wetland</figcaption></figure>
      <figure class="sc-tile" style="--img:url('img/projects/kingfisher-path.jpg')"><figcaption>Natural-stone edging &amp; footpath — Kingfisher Wetland</figcaption></figure>
      <figure class="sc-tile" style="--img:url('img/projects/abc-jurong-walls.jpg')"><figcaption>Stone-clad walls &amp; steps — ABC Waters, Jurong Canal</figcaption></figure>
    </div>
  </div>
  <div class="showcase__panel" id="steel">
    <div class="showcase__lead">
      <h3>Steel Structures</h3>
      <p>Bird hides, canal-side shelters and playground canopies — fabricated and erected under our BCA Specialist Builder (Structural Steelwork) licence, married to the civil works beneath them.</p>
      <div class="showcase__chips"><span>Bird Hide</span><span>ABC Waters</span><span>Magical Bridge</span><span>BCA SB(SS)</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('img/projects/kingfisher-birdhide.jpg')"><figcaption>Bird hide — Kingfisher Wetland, Bay South</figcaption></figure>
      <figure class="sc-tile" style="--img:url('img/projects/abc-jurong-shelter.jpg')"><figcaption>Canal-side shelter — ABC Waters, Jurong Canal</figcaption></figure>
      <figure class="sc-tile" style="--img:url('img/projects/magical-bridge-canopy.jpg')"><figcaption>Flower canopies — Magical Bridge Playground, Sun Plaza Park</figcaption></figure>
    </div>
  </div>
</section>
'''

GLIMPSE = '''<!-- A GLIMPSE OF PROJECTS -->
<section class="work" id="work">
  <div class="rule">
    <span class="rule-tag">A GLIMPSE OF PROJECTS</span>
    <span class="rule-line"></span>
    <span class="rule-tag">SCROLL →</span>
  </div>
  <div class="work__rail" id="workRail">
    <article class="card" style="--rot:-1deg">
      <div class="card__img" style="background-image:url('img/projects/sun-plaza.jpg')"></div>
      <div class="card__meta">
        <span class="card__year">Opened Jun 2026</span>
        <h4>Magical Bridge Playground — Sun Plaza Park</h4>
        <span class="card__owner">National Parks Board (NParks)</span>
        <span class="card__value">S$3,554,747</span>
      </div>
    </article>
    <article class="card" style="--rot:0.8deg">
      <div class="card__img" style="background-image:url('img/projects/abc-jurong-shelter.jpg')"></div>
      <div class="card__meta">
        <span class="card__year">Completed</span>
        <h4>ABC Waters at Jurong Canal — PIE to Boon Lay Way</h4>
        <span class="card__owner">Public Utilities Board (PUB)</span>
        <span class="card__value">S$2,877,000</span>
      </div>
    </article>
    <article class="card" style="--rot:-0.6deg">
      <div class="card__img" style="background-image:url('img/projects/demolition-pit.jpg')"></div>
      <div class="card__meta">
        <span class="card__year">Completed</span>
        <h4>Mugliston Park Pumping Station — Demolition &amp; Grouting of Disused Pipelines</h4>
        <span class="card__owner">Public Utilities Board (PUB)</span>
        <span class="card__value">S$3,475,000</span>
      </div>
    </article>
    <article class="card" style="--rot:1.2deg">
      <div class="card__img card__img--ph"><span class="card__ph-code">MSPS</span><span class="card__ph-note">Site photos to come</span></div>
      <div class="card__meta">
        <span class="card__year">Ongoing</span>
        <h4>Marina South Pump Sump 3 — Demolition &amp; Grouting of Abandoned Sewers</h4>
        <span class="card__owner">Public Utilities Board (PUB)</span>
        <span class="card__value">S$2,777,000</span>
      </div>
    </article>
    <article class="card" style="--rot:-0.9deg">
      <div class="card__img card__img--ph"><span class="card__ph-code">JPS</span><span class="card__ph-note">Site photos to come</span></div>
      <div class="card__meta">
        <span class="card__year">Ongoing</span>
        <h4>Jurong Power Station — Demolition &amp; Land Return to JTC</h4>
        <span class="card__owner">YTL PowerSeraya</span>
        <span class="card__value">S$2,290,000</span>
      </div>
    </article>
    <article class="card" style="--rot:0.4deg">
      <div class="card__img card__img--ph"><span class="card__ph-code">BNF</span><span class="card__ph-note">Site photos to come</span></div>
      <div class="card__meta">
        <span class="card__year">Ongoing</span>
        <h4>Bedok NEWater Factory — Demolition &amp; Land Reinstatement</h4>
        <span class="card__owner">Public Utilities Board (PUB)</span>
        <span class="card__value">S$3,788,002</span>
      </div>
    </article>
    <article class="card card--summary">
      <div class="card__sum">
        <span class="card__sum-num">+28</span>
        <span class="card__sum-lbl">More projects across<br>PUB · NParks · JTC · LTA · MOE · Sentosa Dev · Keppel · NTU · YTL PowerSeraya</span>
        <button type="button" class="card__sum-link" data-action="register">Open full register <span aria-hidden="true">→</span></button>
      </div>
    </article>
  </div>
</section>
'''

CREDS = '''<!-- CREDENTIALS -->
<section class="creds" id="credentials">
  <div class="rule">
    <span class="rule-tag">AWARDS &amp; CERTIFICATIONS</span>
    <span class="rule-line"></span>
    <span class="rule-tag">ISO · BCA</span>
  </div>
  <div class="creds__grid">
    <div class="creds__certs">
      <figure style="--rot:-2deg"><img src="img/certs/iso-9001.jpg" alt="ISO 9001:2015 — Quality Management"></figure>
      <figure style="--rot:1.5deg"><img src="img/certs/iso-14001.jpg" alt="ISO 14001:2015 — Environmental Management"></figure>
      <figure style="--rot:-1deg"><img src="img/certs/iso-45001.jpg" alt="ISO 45001:2018 — Occupational Health &amp; Safety Management"></figure>
      <figure style="--rot:2deg"><img src="img/certs/green-gracious.png" alt="BCA Green and Gracious Builder Award — Merit"></figure>
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
    Techno&nbsp;CE&nbsp;Pte&nbsp;Ltd was incorporated on 20 December 2002 (UEN 200210947C). Civil-engineering specialist, BCA grade B2 in CW02 and C3 in CW01, certified to ISO 9001, ISO 14001 and ISO 45001, and recognised under the BCA Green &amp; Gracious Builder Award.
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
      <span class="post__date">Jun 2026</span>
      <h3>Magical Bridge Playground opens at Sun Plaza Park</h3>
      <p>Our inclusive playground contract for NParks — home to Singapore's first wheelchair-user accessible slide — officially opened on 17 June 2026.</p>
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
      <span class="post__date">Jun 2025</span>
      <h3>ISO 45001 joins ISO 9001 &amp; ISO 14001</h3>
      <p>Our occupational health &amp; safety management system is certified to ISO 45001:2018 — alongside quality and environmental — for the provision of civil engineering services.</p>
      <span class="post__tag">Certification · ISO</span>
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
      <p class="careers__perk">Structured training · on-site mentoring · ISO 45001 safety system</p>
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
    "Techno CE Pte Ltd is a Singapore civil engineering firm — civil engineering, demolition, hardscape and steel structures. BCA CW02 B2 / CW01 C3. ISO 9001, 14001 &amp; 45001.",
    "", HERO + RECEIPTS + MANIFESTO + EXPLORE + clients_block() + CTA_BAND),

 "about.html": page("about",
    "About Us — Techno CE",
    "Vision, mission, core values, awards and certifications of Techno CE Pte Ltd — a ten-person Singapore civil engineering practice since 2002.",
    "about.html",
    pagehead("ABOUT US", "Two hands,<br>one practice.",
        "A ten-person Singapore practice that moves between the heavy and the delicate without changing gear.",
        "img/hero/03-kingfisher-pavilion.jpg")
    + MANIFESTO + ABOUT_BODY + CREDS),

 "services.html": page("services",
    "Services — Techno CE",
    "Our specialities: civil engineering, demolition (deep basement, grouting), hardscape (rubble wall, boardwalk) and steel structures.",
    "services.html",
    pagehead("SERVICES", "Our Specialities",
        "Civil engineering, demolition, hardscape and steel structures — delivered by our own team.",
        "img/projects/demolition-longreach.jpg")
    + SPECIALITIES),

 "projects.html": page("projects",
    "Projects — Techno CE",
    "A glimpse of our projects — Magical Bridge Playground, ABC Waters at Jurong Canal, and demolition for PUB's pumping stations, Bedok NEWater Factory and Jurong Power Station.",
    "projects.html",
    pagehead("PROJECTS", "A Glimpse of Our Work",
        "Six contracts that show what we do best — for PUB, NParks and YTL PowerSeraya.",
        "img/hero/02-erss-basin.jpg")
    + GLIMPSE),

 "newsroom.html": page("newsroom",
    "Newsroom — Techno CE",
    "Latest from site — project openings, contracts and certifications from Techno CE.",
    "newsroom.html",
    pagehead("NEWSROOM", "Latest From Site",
        "Awards, milestones and what's new on our sites.",
        "img/projects/bulim-landscape.jpg")
    + NEWS),

 "careers.html": page("careers",
    "Careers — Techno CE",
    "Join a small team on real sites. Structured training, on-site mentoring and an ISO 45001 safety system.",
    "careers.html",
    pagehead("CAREERS", "Build With Us",
        "Responsibility early, fair wages, and work you can point to.",
        "img/projects/sun-plaza.jpg")
    + CAREERS),

 "contact.html": page("contact",
    "Contact Us — Techno CE",
    "Have a project? Phone +65 6745 5725, email technoce@singnet.com.sg, office at 100 Lorong 23 Geylang.",
    "contact.html",
    pagehead("CONTACT US", "Have A Project?",
        "We read every brief. Tell us what you're building — or taking down.",
        "img/projects/abc-jurong-shelter.jpg")
    + CONTACT_BODY + clients_block()),
}


def main():
    for fname, html in PAGES.items():
        with io.open(os.path.join(HERE, fname), "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        print("wrote", fname, len(html), "bytes")


if __name__ == "__main__":
    main()
