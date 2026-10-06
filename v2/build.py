#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Techno CE — Variant B ("Quiet Practice", light) multi-page generator.
Same pages as Variant A, in v2's light editorial style.
Run:  python build.py   (from inside the v2/ folder)
"""
import io, os

BASE = "https://vivienbeautysg-max.github.io/techno-ce-sample/v2/"
HERE = os.path.dirname(os.path.abspath(__file__))

NAV_ITEMS = [
    ("about",    "About Us", "about.html"),
    ("services", "Services", "services.html"),
    ("projects", "Projects", "projects.html"),
    ("newsroom", "Newsroom", "newsroom.html"),
    ("careers",  "Careers",  "careers.html"),
]

REVEAL_GROUPS = ('{"r-mask":[".pagehead__title",".cta-band__big",".about__lead",".num__cap",'
    '".values__title",".vmm__col h3",".careers__intro h3",".showcase__lead h3"],'
    '"r-up":[".pagehead__sub",".index__row",".w",".num__grid > div",'
    '".values__list li",".post",".careers__roles li",".about p",".showcase__lead p",'
    '".showcase__chips",".careers__intro p",".careers__perk",".creds__verify"],'
    '"r-img":[],"r-fade":[".creds__grid figure"]}')


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
    out.append(f'    <a href="contact.html"{ccur}>Contact Us</a>')
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
    <span>Techno CE Pte Ltd · UEN 200210947C · BCA CW02 B2 · CW01 C3 · ISO 9001:2015 · ISO 14001:2015 · ISO 45001:2018</span>
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
    <img class="hero__img is-on" src="../img/hero/02-erss-basin.jpg" alt="Deep-basement removal in sheet-piled ERSS — Mugliston Park Pumping Station, PUB" />
    <img class="hero__img" src="../img/projects/abc-jurong-steps.jpg" alt="ABC Waters at Jurong Canal — PUB" aria-hidden="true" />
    <img class="hero__img" src="../img/projects/sun-plaza.jpg" alt="Magical Bridge Playground — Sun Plaza Park, NParks" aria-hidden="true" />
  </div>
  <div class="hero__text">
    <span class="hero__eyebrow">— Estd 2002 · Singapore</span>
    <h1 class="hero__h">
      <span class="hero__h-line">A quiet practice</span>
      <span class="hero__h-line"><i>of civil&nbsp;engineering.</i></span>
    </h1>
    <p class="hero__sub">
      For pumping stations, parks &amp; waterways — and the things underneath. Twenty-four years on Singapore's sites, working hand-in-hand with the agencies that build the country.
    </p>
    <div class="hero__chips" role="list">
      <span role="listitem">BCA CW02 B2</span><span aria-hidden="true">·</span>
      <span role="listitem">CW01 C3</span><span aria-hidden="true">·</span>
      <span role="listitem">ISO 9001 / 14001 / 45001</span><span aria-hidden="true">·</span>
      <span role="listitem">Green &amp; Gracious Merit</span>
    </div>
  </div>
</section>
'''

INDEX = '''<!-- INDEX / DIRECTORY -->
<section class="index">
  <div class="index__row"><span>I</span><a href="about.html">About Us</a><span class="index__dot"></span></div>
  <div class="index__row"><span>II</span><a href="services.html">Services</a><span class="index__dot"></span></div>
  <div class="index__row"><span>III</span><a href="projects.html">Projects</a><span class="index__dot"></span></div>
  <div class="index__row"><span>IV</span><a href="newsroom.html">Newsroom</a><span class="index__dot"></span></div>
  <div class="index__row"><span>V</span><a href="careers.html">Careers</a><span class="index__dot"></span></div>
  <div class="index__row"><span>VI</span><a href="contact.html">Contact Us</a><span class="index__dot"></span></div>
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
  <a class="cta-band__link" href="contact.html">
    <span class="cta-band__eyebrow">Have a project?</span>
    <span class="cta-band__big">Let's talk <span aria-hidden="true">→</span></span>
  </a>
</section>
'''

GLIMPSE = '''<!-- A GLIMPSE OF PROJECTS -->
<section class="works" id="works">
  <header class="sec-head">
    <span class="sec-head__num">—</span>
    <h2>A Glimpse of Projects</h2>
    <span class="sec-head__meta">Six of thirty-four</span>
  </header>

  <article class="w" data-i="01">
    <div class="w__no">01<span>&nbsp;/&nbsp;06</span></div>
    <div class="w__media"><img src="../img/projects/sun-plaza.jpg" alt="Magical Bridge Playground at Sun Plaza Park"></div>
    <div class="w__copy">
      <span class="w__year">Opened Jun 2026</span>
      <h3>Magical Bridge Playground — Sun Plaza Park</h3>
      <dl><dt>Owner</dt><dd>National Parks Board (NParks)</dd>
          <dt>Value</dt><dd>S$3,554,747</dd>
          <dt>Speciality</dt><dd>Steel Structures</dd></dl>
    </div>
  </article>

  <article class="w" data-i="02">
    <div class="w__no">02<span>&nbsp;/&nbsp;06</span></div>
    <div class="w__media"><img src="../img/projects/abc-jurong-shelter.jpg" alt="Canal-side shelter at ABC Waters, Jurong Canal"></div>
    <div class="w__copy">
      <span class="w__year">Completed</span>
      <h3>ABC Waters at Jurong Canal — PIE to Boon Lay Way</h3>
      <dl><dt>Owner</dt><dd>Public Utilities Board (PUB)</dd>
          <dt>Value</dt><dd>S$2,877,000</dd>
          <dt>Speciality</dt><dd>Steel Structures · Hardscape</dd></dl>
    </div>
  </article>

  <article class="w" data-i="03">
    <div class="w__no">03<span>&nbsp;/&nbsp;06</span></div>
    <div class="w__media"><img src="../img/projects/demolition-pit.jpg" alt="Basement removal inside ERSS at Mugliston Park Pumping Station"></div>
    <div class="w__copy">
      <span class="w__year">Completed</span>
      <h3>Mugliston Park Pumping Station — Demolition &amp; Grouting of Disused Pipelines</h3>
      <dl><dt>Owner</dt><dd>Public Utilities Board (PUB)</dd>
          <dt>Value</dt><dd>S$3,475,000</dd>
          <dt>Speciality</dt><dd>Demolition</dd></dl>
    </div>
  </article>

  <article class="w" data-i="04">
    <div class="w__no">04<span>&nbsp;/&nbsp;06</span></div>
    <div class="w__media w__media--ph"><span class="w__ph-code">MSPS</span><span class="w__ph-note">Site photos to come</span></div>
    <div class="w__copy">
      <span class="w__year">Ongoing</span>
      <h3>Marina South Pump Sump 3 — Demolition &amp; Grouting of Abandoned Sewers</h3>
      <dl><dt>Owner</dt><dd>Public Utilities Board (PUB)</dd>
          <dt>Value</dt><dd>S$2,777,000</dd>
          <dt>Speciality</dt><dd>Demolition</dd></dl>
    </div>
  </article>

  <article class="w" data-i="05">
    <div class="w__no">05<span>&nbsp;/&nbsp;06</span></div>
    <div class="w__media w__media--ph"><span class="w__ph-code">JPS</span><span class="w__ph-note">Site photos to come</span></div>
    <div class="w__copy">
      <span class="w__year">Ongoing</span>
      <h3>Jurong Power Station — Demolition &amp; Land Return to JTC</h3>
      <dl><dt>Owner</dt><dd>YTL PowerSeraya</dd>
          <dt>Value</dt><dd>S$2,290,000</dd>
          <dt>Speciality</dt><dd>Demolition</dd></dl>
    </div>
  </article>

  <article class="w" data-i="06">
    <div class="w__no">06<span>&nbsp;/&nbsp;06</span></div>
    <div class="w__media w__media--ph"><span class="w__ph-code">BNF</span><span class="w__ph-note">Site photos to come</span></div>
    <div class="w__copy">
      <span class="w__year">Ongoing</span>
      <h3>Bedok NEWater Factory — Demolition &amp; Land Reinstatement</h3>
      <dl><dt>Owner</dt><dd>Public Utilities Board (PUB)</dd>
          <dt>Value</dt><dd>S$3,788,002</dd>
          <dt>Speciality</dt><dd>Demolition</dd></dl>
    </div>
  </article>

  <button class="works__more" type="button" data-action="register">+28 more — see the full register, all 34 <span aria-hidden="true">↗</span></button>
</section>
'''

SPECIALITIES = '''<!-- SPECIALITIES -->
<section class="showcase showcase--stack" id="specialities">
  <header class="sec-head">
    <span class="sec-head__num">—</span>
    <h2>Four disciplines, one team</h2>
    <span class="sec-head__meta">Our specialities</span>
  </header>
  <div class="showcase__panel" id="civil">
    <div class="showcase__lead">
      <h3>Civil Engineering</h3>
      <p>Earthworks, sheet-piled ERSS, slope stabilisation, drainage and road reinstatement — the groundwork beneath Singapore's public infrastructure.</p>
      <div class="showcase__chips"><span>Earthworks</span><span>ERSS &amp; Sheet Piling</span><span>Slope Stabilisation</span><span>Drainage &amp; Premix</span><span>BCA CW02 · B2</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('../img/hero/02-erss-basin.jpg')"><figcaption>Sheet-piled ERSS with strutting — Mugliston Park Pumping Station</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/margaret-drive.jpg')"><figcaption>External works, premix &amp; drainage — Margaret Drive</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/tampines-boulevard.jpg')"><figcaption>Earthworks &amp; park infrastructure — Tampines Boulevard Park</figcaption></figure>
    </div>
  </div>
  <div class="showcase__panel" id="demolition">
    <div class="showcase__lead">
      <h3>Demolition</h3>
      <p>Pumping stations, NEWater factories and power-station assets — taken down safely on live, constrained sites. Deep basements removed inside sheet-piled ERSS, disused pipelines grouted, and hardcore crushed on site into recycled aggregate.</p>
      <div class="showcase__chips"><span>Deep Basement</span><span>Grouting</span><span>Pumping Stations</span><span>Recycled Aggregate</span><span>BCA CR03</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('../img/projects/demolition-longreach.jpg')"><figcaption>Long-reach demolition of a steel-framed structure</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/demolition-basement.jpg')"><figcaption>Breaking out a deep basement</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/demolition-pit.jpg')"><figcaption>Basement removal inside ERSS — Mugliston Park Pumping Station</figcaption></figure>
    </div>
  </div>
  <div class="showcase__panel" id="hardscape">
    <div class="showcase__lead">
      <h3>Hardscape</h3>
      <p>Rubble walls, boardwalks, stone-clad steps and paving — the hard surfaces people walk on, built for parks, gardens and waterways.</p>
      <div class="showcase__chips"><span>Rubble Wall</span><span>Boardwalk</span><span>Stone-clad Walls &amp; Steps</span><span>Paving</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('../img/projects/kingfisher-bridge.jpg')"><figcaption>Boardwalk &amp; rock-edged pond — Kingfisher Wetland</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/kingfisher-path.jpg')"><figcaption>Natural-stone edging &amp; footpath — Kingfisher Wetland</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/abc-jurong-walls.jpg')"><figcaption>Stone-clad walls &amp; steps — ABC Waters, Jurong Canal</figcaption></figure>
    </div>
  </div>
  <div class="showcase__panel" id="steel">
    <div class="showcase__lead">
      <h3>Steel Structures</h3>
      <p>Bird hides, canal-side shelters and playground canopies — fabricated and erected under our BCA Specialist Builder (Structural Steelwork) licence, married to the civil works beneath them.</p>
      <div class="showcase__chips"><span>Bird Hide</span><span>ABC Waters</span><span>Magical Bridge</span><span>BCA SB(SS)</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('../img/projects/kingfisher-birdhide.jpg')"><figcaption>Bird hide — Kingfisher Wetland, Bay South</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/abc-jurong-shelter.jpg')"><figcaption>Canal-side shelter — ABC Waters, Jurong Canal</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/magical-bridge-canopy.jpg')"><figcaption>Flower canopies — Magical Bridge Playground, Sun Plaza Park</figcaption></figure>
    </div>
  </div>
</section>
'''

CREDS = '''<!-- AWARDS & CERTIFICATIONS -->
<section class="creds" id="credentials">
  <header class="sec-head">
    <span class="sec-head__num">—</span>
    <h2>Awards &amp; Certifications</h2>
    <span class="sec-head__meta">ISO · BCA</span>
  </header>
  <div class="creds__grid">
    <figure><img src="../img/certs/iso-9001.jpg" alt="ISO 9001:2015 — Quality Management"><figcaption>ISO 9001:2015 — Quality Management</figcaption></figure>
    <figure><img src="../img/certs/iso-14001.jpg" alt="ISO 14001:2015 — Environmental Management"><figcaption>ISO 14001:2015 — Environmental Management</figcaption></figure>
    <figure><img src="../img/certs/iso-45001.jpg" alt="ISO 45001:2018 — Occupational Health &amp; Safety Management"><figcaption>ISO 45001:2018 — Occupational Health &amp; Safety Management</figcaption></figure>
    <figure><img src="../img/certs/green-gracious.png" alt="BCA Green and Gracious Builder Award — Merit"><figcaption>BCA Green &amp; Gracious Builder — Merit</figcaption></figure>
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
    <p>Our books are kept by an external auditor; our standards by ISO 9001, ISO 14001 and ISO 45001; our manners on the construction site by the BCA Green &amp; Gracious framework, in which we hold the Merit recognition.</p>
  </div>
</section>
'''

NEWS = '''<!-- NEWSROOM -->
<section class="news" id="newsroom">
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
    "Techno CE Pte Ltd is a Singapore civil engineering firm — civil engineering, demolition, hardscape and steel structures. BCA CW02 B2 / CW01 C3. ISO 9001, 14001 &amp; 45001.",
    "", HERO + INDEX + NUM + PULLQUOTE + clients_block() + CTA_BAND),

 "about.html": page("about",
    "About Us — Techno CE",
    "Vision, mission, core values, awards and certifications of Techno CE Pte Ltd — a ten-person Singapore civil engineering practice since 2002.",
    "about.html",
    pagehead("About Us", "A quiet practice,<br>since 2002.",
        "Vision, mission, values — and the ten people who keep them.")
    + VMM + VALUES + STUDIO + CREDS),

 "services.html": page("services",
    "Services — Techno CE",
    "Our specialities: civil engineering, demolition (deep basement, grouting), hardscape (rubble wall, boardwalk) and steel structures.",
    "services.html",
    pagehead("Services", "Our specialities.",
        "Civil engineering, demolition, hardscape and steel structures — delivered by our own team.")
    + SPECIALITIES),

 "projects.html": page("projects",
    "Projects — Techno CE",
    "A glimpse of our projects — Magical Bridge Playground, ABC Waters at Jurong Canal, and demolition for PUB's pumping stations, Bedok NEWater Factory and Jurong Power Station.",
    "projects.html",
    pagehead("Projects", "A glimpse of our work.",
        "Six contracts that show what we do best — for PUB, NParks and YTL PowerSeraya.")
    + GLIMPSE),

 "newsroom.html": page("newsroom",
    "Newsroom — Techno CE",
    "Latest from site — project openings, contracts and certifications from Techno CE.",
    "newsroom.html",
    pagehead("Newsroom", "Latest from site.",
        "Awards, milestones and what's new on our sites.")
    + NEWS),

 "careers.html": page("careers",
    "Careers — Techno CE",
    "Join a small team on real sites. Structured training, on-site mentoring and an ISO 45001 safety system.",
    "careers.html",
    pagehead("Careers", "Build with us.",
        "Responsibility early, fair wages, and work you can point to.")
    + CAREERS),

 "contact.html": page("contact",
    "Contact Us — Techno CE",
    "Have a project? Phone +65 6745 5725, email technoce@singnet.com.sg, office at 100 Lorong 23 Geylang.",
    "contact.html",
    pagehead("Contact Us", "Have a project?",
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
