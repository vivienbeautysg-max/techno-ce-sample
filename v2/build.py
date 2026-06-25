#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Techno CE — Variant B ("Quiet Practice", light) multi-page generator.
Same 9 tabs as Variant A, in v2's light editorial style.
Run:  python build.py   (from inside the v2/ folder)
"""
import io, os

BASE = "https://vivienbeautysg-max.github.io/techno-ce-sample/v2/"
HERE = os.path.dirname(os.path.abspath(__file__))

NAV_ITEMS = [
    ("about",    "About",    "about.html"),
    ("services", "Services", "services.html"),
    ("projects", "Projects", "projects.html"),
    ("showcase", "Showcase", "showcase.html"),
    ("media",    "Media",    "media.html"),
    ("newsroom", "Newsroom", "newsroom.html"),
    ("careers",  "Careers",  "careers.html"),
]

REVEAL_GROUPS = ('{"r-mask":[".pagehead__title",".cta-band__big",".about__lead",".num__cap",'
    '".values__title",".vmm__col h3",".media__lead",".careers__intro h3",".showcase__lead h3"],'
    '"r-up":[".pagehead__sub",".index__row",".w",".caps__list li",".num__grid > div",'
    '".values__list li",".post",".careers__roles li",".about p",".showcase__lead p",'
    '".showcase__chips",".careers__intro p",".careers__perk",".media__note",".creds__verify"],'
    '"r-img":[".vtile"],"r-fade":[".creds__grid figure"]}')


def head(title, desc, canon):
    return f'''<!doctype html>
<html lang="en-SG">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width,initial-scale=1" />
<script>(function(e){{e.className+=' js';try{{if(!matchMedia('(prefers-reduced-motion: reduce)').matches)e.className+=' motion';}}catch(x){{}}try{{if(sessionStorage.getItem('tce_seen_b'))e.className+=' no-intro';else sessionStorage.setItem('tce_seen_b','1');}}catch(x){{}}}})(document.documentElement);</script>
<script>window.TCE_REVEAL_GROUPS={REVEAL_GROUPS};</script>
<title>{title}</title>
<meta name="description" content="{desc}" />
<meta name="theme-color" content="#F2F6FB" />
<meta name="robots" content="noindex" />
<link rel="canonical" href="{BASE}{canon}" />
<link rel="icon" type="image/svg+xml" href="../img/logo.svg" />
<link rel="apple-touch-icon" href="../img/logo.svg" />
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
  <span class="preloader__brand"><img src="../img/logo.svg" alt="" width="34" height="34" />Techno&nbsp;CE</span>
  <span class="preloader__bar"></span>
</div>

<a class="skip" href="#top">Skip to main content</a>
'''


def nav(active):
    out = ['<header class="nav" id="nav">',
           '  <a class="nav__logo" href="index.html" aria-label="Techno CE — home">',
           '    <img class="nav__mark" src="../img/logo.svg" alt="" width="30" height="30" />',
           '    <span class="nav__wordmark">Techno&nbsp;CE</span>',
           '  </a>',
           '  <span class="nav__divider" aria-hidden="true">/</span>',
           '  <span class="nav__loc">Singapore · Civil Engineering</span>',
           '  <nav class="nav__links" id="navLinks">',
           '    <a href="../" class="nav__variant" aria-label="Switch to Variant A design"><span aria-hidden="true">↩</span> Variant&nbsp;A</a>']
    for key, label, href in NAV_ITEMS:
        cur = ' class="is-active" aria-current="page"' if key == active else ''
        out.append(f'    <a href="{href}"{cur}>{label}</a>')
    ccur = ' class="is-active" aria-current="page"' if active == 'contact' else ''
    out.append(f'    <a href="contact.html"{ccur}>Contact</a>')
    out.append('  </nav>')
    out.append('  <button class="nav__burger" id="burger" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks"><span></span><span></span><span></span></button>')
    out.append('</header>')
    return "\n".join(out)


def pagehead(eyebrow, title_html, sub):
    return f'''<section class="pagehead">
  <span class="pagehead__eyebrow">{eyebrow}</span>
  <h1 class="pagehead__title">{title_html}</h1>
  <p class="pagehead__sub">{sub}</p>
</section>
'''

FOOTER = '''
<footer class="foot">
  <div class="foot__line">
    <span>Techno CE Pte Ltd · UEN 200210947C · BCA CW02 B2 · CW01 C3 · ISO 9001:2015 · ISO 14001:2015</span>
    <span>© 2002–2026 Techno CE Pte Ltd · 100 Lorong 23 Geylang #03-03 · +65 6745 5725</span>
  </div>
  <div class="foot__line foot__line--legal">
    <span>All third-party trademarks are the property of their respective owners. Their appearance on this site does not imply endorsement.</span>
  </div>
</footer>

<script src="app.js"></script>
<script src="../premium.js"></script>
</body>
</html>
'''


def page(active, title, desc, canon, body):
    return head(title, desc, canon) + PRELUDE + nav(active) + '\n\n<main id="top">\n' + body + '\n</main>\n' + FOOTER


# ============================================================ CONTENT

HERO = '''<!-- HERO -->
<section class="hero">
  <div class="hero__art">
    <img class="hero__img is-on" src="../img/hero/03-kingfisher-pavilion.jpg" alt="Kingfisher Wetland pavilion at Bay South, Gardens by the Bay — built by Techno CE" />
    <img class="hero__img" src="../img/projects/kingfisher-bridge.jpg" alt="" aria-hidden="true" />
    <img class="hero__img" src="../img/projects/sentosa-pavilion.jpg" alt="" aria-hidden="true" />
  </div>
  <div class="hero__text">
    <span class="hero__eyebrow">— Estd 2002 · Singapore</span>
    <h1 class="hero__h">
      <span class="hero__h-line">A quiet practice</span>
      <span class="hero__h-line"><i>of civil&nbsp;engineering.</i></span>
    </h1>
    <p class="hero__sub">
      For parks &amp; gardens, golf courses, reservoirs and the things underneath. Twenty-four years on Singapore's sites, working hand-in-hand with the agencies that build the country.
    </p>
    <div class="hero__chips" role="list">
      <span role="listitem">BCA CW02 B2</span><span aria-hidden="true">·</span>
      <span role="listitem">CW01 C3</span><span aria-hidden="true">·</span>
      <span role="listitem">ISO 9001 / 14001</span><span aria-hidden="true">·</span>
      <span role="listitem">Green &amp; Gracious Merit</span>
    </div>
  </div>
</section>
'''

INDEX = '''<!-- INDEX / DIRECTORY -->
<section class="index">
  <div class="index__row"><span>I</span><a href="about.html">About</a><span class="index__dot"></span></div>
  <div class="index__row"><span>II</span><a href="services.html">Services</a><span class="index__dot"></span></div>
  <div class="index__row"><span>III</span><a href="projects.html">Projects</a><span class="index__dot"></span></div>
  <div class="index__row"><span>IV</span><a href="showcase.html">Showcase</a><span class="index__dot"></span></div>
  <div class="index__row"><span>V</span><a href="media.html">Media</a><span class="index__dot"></span></div>
  <div class="index__row"><span>VI</span><a href="newsroom.html">Newsroom</a><span class="index__dot"></span></div>
  <div class="index__row"><span>VII</span><a href="careers.html">Careers</a><span class="index__dot"></span></div>
</section>
'''

NUM = '''<!-- NUMBERS -->
<section class="num" id="numbers">
  <header class="sec-head">
    <span class="sec-head__num">—</span>
    <h2>By the Numbers</h2>
    <span class="sec-head__meta">As of May 2026</span>
  </header>
  <div class="num__grid">
    <div><b>24<sup>+</sup></b><span>years on site, since 2002</span></div>
    <div><b>34</b><span>projects delivered &amp; ongoing</span></div>
    <div><b>S$80.9<sup>M</sup></b><span>contract value across portfolio</span></div>
    <div><b>10</b><span>people, all on payroll</span></div>
  </div>
  <p class="num__cap">A small studio. Long timesheets. We work for the agencies that build Singapore.</p>
</section>
'''

PULLQUOTE = '''<!-- PULL-QUOTE -->
<figure class="pullquote">
  <blockquote>
    We are <em>ten people.</em> We work for the agencies that build the country.
  </blockquote>
  <figcaption>— Techno CE Pte Ltd · Estd 2002 · Singapore</figcaption>
</figure>
'''

CLIENTS_ITEMS = ["PUB","NParks","JTC","LTA","MOE","Gardens by the Bay","Sentosa Development",
    "Sentosa Golf Club","SICC","Tanah Merah Country Club","Seletar Country Club","NSRCC",
    "Keppel Club","NTU","YTL PowerSeraya","China Railway First Group","TEHC International"]


def clients_block():
    a = "".join(f'      <span class="marquee__item">{x}</span>\n' for x in CLIENTS_ITEMS)
    b = "".join(f'      <span class="marquee__item marquee__dup" aria-hidden="true">{x}</span>\n' for x in CLIENTS_ITEMS)
    return ('''<!-- CLIENTS -->
<section class="clients-band">
  <div class="clients-band__head"><span class="clients-band__lbl">Trusted by the agencies that build Singapore</span></div>
  <div class="marquee" role="region" aria-label="Trusted by Singapore's public agencies and partners">
    <div class="marquee__track">
''' + a + b + '''    </div>
  </div>
</section>
''')

CTA_BAND = '''<!-- CTA BAND -->
<section class="cta-band">
  <a class="cta-band__link" href="contact.html" data-magnetic="0.2">
    <span class="cta-band__eyebrow">Have a project?</span>
    <span class="cta-band__big">Let's talk <span aria-hidden="true">→</span></span>
  </a>
</section>
'''

WORKS = '''<!-- WORKS -->
<section class="works" id="works">
  <header class="sec-head">
    <span class="sec-head__num">—</span>
    <h2>Selected Works</h2>
    <span class="sec-head__meta">Eight of thirty-four</span>
  </header>

  <article class="w" data-i="01">
    <div class="w__no">01<span>&nbsp;/&nbsp;08</span></div>
    <div class="w__media"><img src="../img/projects/demolition-pit.jpg" alt="DTSS Phase 2 demolition basin"></div>
    <div class="w__copy">
      <span class="w__year">2024 — Ongoing</span>
      <h3>DTSS Phase 2 — Flow Diversion &amp; Demolition</h3>
      <p>Used-water pumping installations decommissioning, sheet-piled basement removal, and grouting of disused mains across multiple sites — Public Utilities Board, Contract&nbsp;1.</p>
      <dl><dt>Owner</dt><dd>Public Utilities Board (PUB)</dd>
          <dt>Value</dt><dd>S$9,455,000</dd>
          <dt>Workhead</dt><dd>CR03 · Demolition</dd></dl>
    </div>
  </article>

  <article class="w" data-i="02">
    <div class="w__no">02<span>&nbsp;/&nbsp;08</span></div>
    <div class="w__media"><img src="../img/projects/golf-aerial.jpg" alt="Sentosa golf course aerial"></div>
    <div class="w__copy">
      <span class="w__year">2022</span>
      <h3>Sentosa Golf Club — Tanjong Course Redevelopment</h3>
      <p>Earthwork, RC bridge and tunnel works for the redevelopment of the Tanjong course. A long collaboration with TEHC International, on Singapore's most exposed coastline.</p>
      <dl><dt>Owner</dt><dd>Sentosa Golf Club</dd>
          <dt>Value</dt><dd>S$7,412,842</dd>
          <dt>Workhead</dt><dd>CW02 · Civil</dd></dl>
    </div>
  </article>

  <article class="w" data-i="03">
    <div class="w__no">03<span>&nbsp;/&nbsp;08</span></div>
    <div class="w__media"><img src="../img/projects/sentosa-pavilion.jpg" alt="Singapore Island Country Club pavilion"></div>
    <div class="w__copy">
      <span class="w__year">2021</span>
      <h3>Singapore Island Country Club — Redevelopment</h3>
      <p>Earthwork and reinforced concrete retaining walls. The smaller pavilions on the course were finished by the same hands that earlier rebuilt the slope they sit on.</p>
      <dl><dt>Owner</dt><dd>Singapore Island Country Club</dd>
          <dt>Value</dt><dd>S$7,344,396</dd>
          <dt>Workhead</dt><dd>CW01 / CW02</dd></dl>
    </div>
  </article>

  <article class="w" data-i="04">
    <div class="w__no">04<span>&nbsp;/&nbsp;08</span></div>
    <div class="w__media"><img src="../img/projects/tampines-boulevard.jpg" alt="Tampines Boulevard Park"></div>
    <div class="w__copy">
      <span class="w__year">Opened Feb 2025</span>
      <h3>Tampines Boulevard Park</h3>
      <p>10.06&nbsp;hectares across two sections, separated by Tampines Avenue 12. Civil and landscape works for NParks. Officially opened on 22&nbsp;February&nbsp;2025.</p>
      <dl><dt>Owner</dt><dd>National Parks Board (NParks)</dd>
          <dt>Value</dt><dd>S$5,924,112</dd>
          <dt>Status</dt><dd>Opened to public</dd></dl>
    </div>
  </article>

  <article class="w" data-i="05">
    <div class="w__no">05<span>&nbsp;/&nbsp;08</span></div>
    <div class="w__media"><img src="../img/projects/bulim-landscape.jpg" alt="Bulim Phase 1 landscape"></div>
    <div class="w__copy">
      <span class="w__year">2023 — Ongoing</span>
      <h3>Bulim Phase 1 — Landscape &amp; Associated Works</h3>
      <p>Nominated sub-contract for the construction of infrastructure works at Bulim Phase 1, JTC's industrial expansion in Jurong West.</p>
      <dl><dt>Owner</dt><dd>JTC Corporation</dd>
          <dt>Value</dt><dd>S$4,221,332</dd>
          <dt>Workhead</dt><dd>Landscape</dd></dl>
    </div>
  </article>

  <article class="w" data-i="06">
    <div class="w__no">06<span>&nbsp;/&nbsp;08</span></div>
    <div class="w__media"><img src="../img/projects/kingfisher-bridge.jpg" alt="Kingfisher Wetland bridge"></div>
    <div class="w__copy">
      <span class="w__year">2018</span>
      <h3>Kingfisher Wetland — Bay South, Gardens by the Bay</h3>
      <p>Design and build of the Kingfisher Wetland and its arched timber bridge. A small contract; an outsized line in the portfolio.</p>
      <dl><dt>Owner</dt><dd>Gardens by the Bay</dd>
          <dt>Value</dt><dd>S$436,500</dd>
          <dt>Workhead</dt><dd>Civil / Landscape</dd></dl>
    </div>
  </article>

  <article class="w" data-i="07">
    <div class="w__no">07<span>&nbsp;/&nbsp;08</span></div>
    <div class="w__media"><img src="../img/projects/sun-plaza.jpg" alt="Sun Plaza Park inclusive playground"></div>
    <div class="w__copy">
      <span class="w__year">2024 — Ongoing</span>
      <h3>Sun Plaza Park — Inclusive Playground</h3>
      <p>Design-and-build of the inclusive playground at Sun Plaza Park, with five years of subsequent maintenance for the play equipment.</p>
      <dl><dt>Owner</dt><dd>National Parks Board (NParks)</dd>
          <dt>Value</dt><dd>S$3,554,747</dd>
          <dt>Workhead</dt><dd>Landscape · D&amp;B</dd></dl>
    </div>
  </article>

  <article class="w" data-i="08">
    <div class="w__no">08<span>&nbsp;/&nbsp;08</span></div>
    <div class="w__media"><img src="../img/projects/margaret-drive.jpg" alt="Margaret Drive external works"></div>
    <div class="w__copy">
      <span class="w__year">2020</span>
      <h3>Margaret Drive — External Works at Margaret Ville</h3>
      <p>Asphalt premix and drainage works on the external roads serving the Margaret Ville development; in collaboration with LTA standards.</p>
      <dl><dt>Owner</dt><dd>LTA / Margaret Ville</dd>
          <dt>Value</dt><dd>S$695,577</dd>
          <dt>Workhead</dt><dd>CR07 · Road</dd></dl>
    </div>
  </article>

  <button class="works__more" type="button" data-action="register">See the full register, all 34 <span aria-hidden="true">↗</span></button>
</section>
'''

CAPS = '''<!-- CAPABILITIES -->
<section class="caps" id="capabilities">
  <header class="sec-head">
    <span class="sec-head__num">—</span>
    <h2>Seven Capabilities</h2>
    <span class="sec-head__meta">Six BCA-current + recovery</span>
  </header>
  <ol class="caps__list">
    <li><span class="caps__no">i.</span><h3>Civil Engineering &amp; Earthworks</h3><p>For JTC, NParks, PUB and country-club developments.</p><span class="caps__grade">CW02 · B2</span></li>
    <li><span class="caps__no">ii.</span><h3>Demolition &amp; Reinstatement</h3><p>Pumping stations, NEWater factories, power stations.</p><span class="caps__grade">CR03 · Single</span></li>
    <li><span class="caps__no">iii.</span><h3>Piling Works &amp; ERSS</h3><p>Sheet piling for reservoirs and basements.</p><span class="caps__grade">CR08 / SB(PW)</span></li>
    <li><span class="caps__no">iv.</span><h3>Reinforced Concrete</h3><p>Retaining walls, ponds, waterfalls, bridges, tunnels.</p><span class="caps__grade">CW01 · C3</span></li>
    <li><span class="caps__no">v.</span><h3>Road, Pipe &amp; Premix</h3><p>Cable / pipe laying, road reinstatement, asphalt.</p><span class="caps__grade">CR07 · L1</span></li>
    <li><span class="caps__no">vi.</span><h3>Waterproofing</h3><p>Buildings, basements, water-retaining structures.</p><span class="caps__grade">CR13 · L1</span></li>
    <li><span class="caps__no">vii.</span><h3>Recycled Aggregate &amp; Recovery</h3><p>On-site crusher &amp; power screen turn demolition hardcore into clean, graded recycled aggregate — less to landfill, less hauled in.</p><span class="caps__grade">Circular · On-site</span></li>
  </ol>
</section>
'''

CREDS = '''<!-- CREDENTIALS -->
<section class="creds" id="credentials">
  <header class="sec-head">
    <span class="sec-head__num">—</span>
    <h2>Credentials</h2>
    <span class="sec-head__meta">Verifiable, current</span>
  </header>
  <div class="creds__grid">
    <figure><img src="../img/certs/iso-9001.jpg" alt="ISO 9001:2015"><figcaption>ISO 9001:2015 — Quality Management</figcaption></figure>
    <figure><img src="../img/certs/iso-14001.jpg" alt="ISO 14001:2015"><figcaption>ISO 14001:2015 — Environmental Management</figcaption></figure>
    <figure><img src="../img/certs/green-gracious.png" alt="Green & Gracious Merit"><figcaption>BCA Green &amp; Gracious — Merit</figcaption></figure>
    <figure><img src="../img/certs/progressive-wage.png" alt="Progressive Wage Mark"><figcaption>Progressive Wage Mark — MOM</figcaption></figure>
  </div>
  <p class="creds__verify">UEN <code>200210947C</code> · Verify on the <a href="https://www1.bca.gov.sg/bca-directory" target="_blank" rel="noopener">BCA Directory →</a></p>
</section>
'''

VMM = '''<!-- VISION / MISSION / MOTTO -->
<section class="about">
  <header class="sec-head">
    <span class="sec-head__num">—</span>
    <h2>Vision, Mission &amp; Motto</h2>
    <span class="sec-head__meta">Who we are</span>
  </header>
  <div class="vmm">
    <div class="vmm__col">
      <span class="vmm__lbl">Vision</span>
      <h3>Take pride in every job.</h3>
      <p class="vmm__sub">To be the specialist Singapore's agencies trust for the work that is hard to build — and harder to take down.</p>
    </div>
    <div class="vmm__col">
      <span class="vmm__lbl">Mission</span>
      <h3>Build it, and leave it better.</h3>
      <p class="vmm__sub">To deliver every civil, demolition and landscape contract safely, cleanly and on time — returning each site better than we found it.</p>
    </div>
    <div class="vmm__col">
      <span class="vmm__lbl">Motto</span>
      <h3><em>Mission Possible.</em></h3>
      <p class="vmm__sub">Twenty-four years of saying yes to the contracts others walk away from.</p>
    </div>
  </div>
</section>
'''

VALUES = '''<!-- CORE VALUES -->
<div class="values">
  <div class="values__head">
    <span class="values__lbl">Core Values</span>
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
'''

STUDIO = '''<!-- STUDIO & PRACTICE -->
<section class="about" id="about">
  <header class="sec-head">
    <span class="sec-head__num">—</span>
    <h2>Studio &amp; Practice</h2>
    <span class="sec-head__meta">100 Lorong 23 Geylang</span>
  </header>
  <div class="about__grid">
    <p class="about__lead">Take pride of our works. <i>The best is yet to come.</i> — Mission Possible.</p>
    <p>Techno&nbsp;CE&nbsp;Pte&nbsp;Ltd was incorporated on 20&nbsp;December&nbsp;2002 (UEN&nbsp;200210947C). Today, ten people work from a single studio at D'Centennial in Geylang. We do not subcontract our project management. We are on the sites we build.</p>
    <p>Our books are kept by an external auditor; our standards by ISO 9001 and ISO 14001; our wages by the Progressive Wage Mark; our manners on the construction site by the BCA Green &amp; Gracious framework, in which we hold the Merit recognition.</p>
  </div>
</section>
'''

SHOWCASE = '''<!-- SHOWCASE -->
<section class="showcase" id="showcase">
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
      <figure class="sc-tile" style="--img:url('../img/projects/demolition-pit.jpg')"><figcaption>ERSS &amp; deep-basement removal</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/hero/02-erss-basin.jpg')"><figcaption>Sheet-piled ERSS basin</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/golf-aerial.jpg')"><figcaption>Site clearance &amp; earthwork</figcaption></figure>
    </div>
  </div>
  <div class="showcase__panel" role="tabpanel" id="sc-panel-soft" aria-labelledby="sc-tab-soft" data-panel="soft" hidden>
    <div class="showcase__lead">
      <h3>Softscape</h3>
      <p>The delicate end of the practice — parks, gardens and waterfront landscapes built to last and to be lived in, for NParks and Gardens by the Bay.</p>
      <div class="showcase__chips"><span>Boardwalk</span><span>Stone-clad Wall</span><span>Shelters</span><span>Ponds &amp; Wetlands</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('../img/projects/kingfisher-bridge.jpg')"><figcaption>Timber boardwalk &amp; arched bridge</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/bulim-landscape.jpg')"><figcaption>Landscape &amp; stone-clad walls</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/tampines-boulevard.jpg')"><figcaption>Tampines Boulevard Park, 10.06 ha</figcaption></figure>
    </div>
  </div>
  <div class="showcase__panel" role="tabpanel" id="sc-panel-steel" aria-labelledby="sc-tab-steel" data-panel="steel" hidden>
    <div class="showcase__lead">
      <h3>Steel Structure</h3>
      <p>Shelters, pavilions and walkway roofs — fabricated and erected to BCA SB(SS) standard, married to the civil works underneath them.</p>
      <div class="showcase__chips"><span>ERSS</span><span>Shelters</span><span>Pavilions</span><span>Walkway Roofs</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('../img/hero/03-kingfisher-pavilion.jpg')"><figcaption>Kingfisher pavilion, Bay South</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/sentosa-pavilion.jpg')"><figcaption>Course pavilion &amp; shelter</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/sun-plaza.jpg')"><figcaption>Inclusive playground steelwork</figcaption></figure>
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
  <div class="media__intro">
    <p class="media__lead">Our work moves — site reels, project time-lapses and the moments the agencies don't get to see.</p>
    <p class="media__note">Sample tiles · final cuts to be embedded — TikTok, news features and our own production.</p>
  </div>
  <div class="media__grid">
    <button class="vtile" type="button" aria-label="Play sample: site reel (placeholder)">
      <span class="vtile__img" style="--img:url('../img/projects/demolition-pit.jpg')"></span>
      <span class="vtile__play" aria-hidden="true"></span>
      <span class="vtile__meta"><b>Own Production</b><span>Demolition site reel · 0:45</span></span>
    </button>
    <button class="vtile" type="button" aria-label="Play sample: news feature (placeholder)">
      <span class="vtile__img" style="--img:url('../img/projects/tampines-boulevard.jpg')"></span>
      <span class="vtile__play" aria-hidden="true"></span>
      <span class="vtile__meta"><b>In the Media</b><span>Tampines Boulevard Park opening</span></span>
    </button>
    <button class="vtile" type="button" aria-label="Play sample: TikTok clip (placeholder)">
      <span class="vtile__img" style="--img:url('../img/projects/kingfisher-bridge.jpg')"></span>
      <span class="vtile__play" aria-hidden="true"></span>
      <span class="vtile__meta"><b>TikTok · @technoce</b><span>Building Bay South, in 30 seconds</span></span>
    </button>
  </div>
</section>
'''

NEWS = '''<!-- NEWSROOM -->
<section class="news" id="newsroom">
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
  <a class="careers__cta" href="mailto:technoce@singnet.com.sg?subject=Career%20enquiry%20%E2%80%94%20Techno%20CE" data-magnetic="0.25">
    Send your CV to technoce@singnet.com.sg <span aria-hidden="true">→</span>
  </a>
  <p class="news__note">Sample roles · final openings to be confirmed by Techno CE.</p>
</section>
'''

CONTACT = '''<!-- CONTACT -->
<section class="contact" id="contact">
  <header class="sec-head">
    <span class="sec-head__num">—</span>
    <h2>Have a project?</h2>
    <span class="sec-head__meta">We read every brief.</span>
  </header>
  <div class="contact__grid">
    <a href="tel:+6567455725"><span>By phone</span>+65 6745 5725</a>
    <a href="mailto:technoce@singnet.com.sg"><span>By email</span>technoce@singnet.com.sg</a>
    <a href="https://maps.google.com/?q=100+Lorong+23+Geylang+Singapore+388398" target="_blank" rel="noopener"><span>By post</span>100 Lorong 23 Geylang #03-03 D'Centennial Singapore 388398</a>
  </div>
</section>
'''

# ============================================================ PAGES

PAGES = {
 "index.html": page("home",
    "Techno CE — Quiet civil engineering. Singapore. Since 2002.",
    "Techno CE Pte Ltd — civil engineering for parks, gardens, golf courses, demolition and infrastructure across Singapore. Since 2002.",
    "", HERO + INDEX + NUM + PULLQUOTE + clients_block() + CTA_BAND),

 "about.html": page("about",
    "About — Techno CE",
    "Vision, mission, motto and core values of Techno CE Pte Ltd — a ten-person Singapore civil engineering practice since 2002.",
    "about.html",
    pagehead("About", "A quiet practice,<br>since 2002.",
        "Vision, mission, values — and the ten people who keep them.")
    + VMM + VALUES + STUDIO + CREDS),

 "services.html": page("services",
    "Services — Techno CE",
    "Seven capabilities: civil engineering, demolition, piling & ERSS, reinforced concrete, roads, waterproofing and recycled aggregate recovery.",
    "services.html",
    pagehead("Services", "Seven capabilities.",
        "Six BCA-current workheads — and a crusher line that closes the loop.")
    + CAPS),

 "projects.html": page("projects",
    "Projects — Techno CE",
    "34 contracts for PUB, NParks, JTC, LTA, MOE, Sentosa, SICC and the country clubs.",
    "projects.html",
    pagehead("Projects", "Present &amp; past.",
        "Thirty-four contracts for the agencies that build Singapore.")
    + WORKS),

 "showcase.html": page("showcase",
    "Showcase — Techno CE",
    "What we're known for: demolition, softscape, steel structure, and the team behind it.",
    "showcase.html",
    pagehead("Showcase", "What we're<br>known for.",
        "Four sides of the practice — pick one.")
    + SHOWCASE),

 "media.html": page("media",
    "Media — Techno CE",
    "Our work in motion — site reels, project time-lapses, news features and our own production.",
    "media.html",
    pagehead("Media", "In motion.",
        "Site reels, time-lapses and the moments the agencies don't see.")
    + MEDIA),

 "newsroom.html": page("newsroom",
    "Newsroom — Techno CE",
    "Latest from site — awards, project milestones and sustainability news from Techno CE.",
    "newsroom.html",
    pagehead("Newsroom", "Latest from site.",
        "Awards, milestones and what's new on our sites.")
    + NEWS),

 "careers.html": page("careers",
    "Careers — Techno CE",
    "Join a small team on real sites. Progressive Wage Mark employer, structured training, on-site mentoring.",
    "careers.html",
    pagehead("Careers", "Build with us.",
        "Responsibility early, fair wages, and work you can point to.")
    + CAREERS),

 "contact.html": page("contact",
    "Contact — Techno CE",
    "Have a project? Phone +65 6745 5725, email technoce@singnet.com.sg, office at 100 Lorong 23 Geylang.",
    "contact.html",
    pagehead("Contact", "Have a project?",
        "We read every brief. Tell us what you're building — or taking down.")
    + CONTACT + clients_block()),
}


def main():
    for fname, html in PAGES.items():
        with io.open(os.path.join(HERE, fname), "w", encoding="utf-8", newline="\n") as f:
            f.write(html)
        print("wrote v2/" + fname, len(html), "bytes")


if __name__ == "__main__":
    main()
