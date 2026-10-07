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
    <span>Techno CE Pte Ltd · UEN 200210947C · BCA CW02 B2 · CW01 C3 · ISO 9001:2015 · ISO 14001:2015 · ISO 45001:2018 · bizSAFE Star</span>
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
    <picture><source media="(max-width:1100px)" srcset="../img/hero/b1-erss-l.jpg"><img class="hero__img is-on" src="../img/hero/b1-erss.jpg" alt="Deep-basement removal in sheet-piled ERSS — Mugliston Park Pumping Station, PUB" /></picture>
    <picture><source media="(max-width:1100px)" srcset="../img/hero/b2-kingfisher-path-l.jpg"><img class="hero__img" src="../img/hero/b2-kingfisher-path.jpg" alt="Footpath and stream edge — Kingfisher Wetland, Gardens by the Bay" aria-hidden="true" /></picture>
    <picture><source media="(max-width:1100px)" srcset="../img/hero/b3-tampines-stairs-l.jpg"><img class="hero__img" src="../img/hero/b3-tampines-stairs.jpg" alt="Steps and railings — Tampines Boulevard Park, NParks" aria-hidden="true" /></picture>
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
      <span role="listitem">bizSAFE Star</span><span aria-hidden="true">·</span>
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
    <span class="sec-head__meta">As of Sep 2026</span>
  </header>
  <div class="num__grid">
    <div><b>24<sup>+</sup></b><span>years on site, since 2002</span></div>
    <div><b>30</b><span>contracts in our record</span></div>
    <div><b>S$62.6<sup>M</sup></b><span>aggregate contract value</span></div>
    <div><b>5</b><span>BCA workheads</span></div>
  </div>
  <p class="num__cap">Our own supervisors. Our own plant. We work for the agencies that build Singapore.</p>
</section>
'''

PULLQUOTE = '''<!-- PULL-QUOTE -->
<figure class="pullquote">
  <blockquote>
    Our own supervisors. <em>Our own plant.</em> We self-perform the civil scope.
  </blockquote>
  <figcaption>— Techno CE Pte Ltd · Estd 2002 · Singapore</figcaption>
</figure>
'''

CLIENTS_ITEMS = ["PUB","NParks","JTC","LTA","MOE","NTU","Gardens by the Bay","Sentosa Development",
    "Keppel Club","China Railway First Group","TEHC International","TPS Construction"]


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
    <span class="sec-head__meta">Six of thirty</span>
  </header>

  <article class="w" data-i="01">
    <div class="w__no">01<span>&nbsp;/&nbsp;06</span></div>
    <div class="w__media"><img src="../img/projects/c-magical-bridge.jpg" alt="Flower canopy and play equipment at Magical Bridge Inclusive Playground, Sun Plaza Park"></div>
    <div class="w__copy">
      <span class="w__year">Completed Jun 2026</span>
      <h3>Magical Bridge Inclusive Playground — Sun Plaza Park</h3>
      <dl><dt>Owner</dt><dd>National Parks Board (NParks)</dd>
          <dt>Value</dt><dd>S$3,554,747</dd>
          <dt>Speciality</dt><dd>Steel Structures · Hardscape</dd></dl>
    </div>
  </article>

  <article class="w" data-i="02">
    <div class="w__no">02<span>&nbsp;/&nbsp;06</span></div>
    <div class="w__media"><img src="../img/projects/c-abc.jpg" alt="Canal-side shelter and access steps at ABC Waters, Jurong Canal"></div>
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
    <div class="w__media"><img src="../img/projects/c-mugliston.jpg" alt="Excavators removing the basement inside sheet-piled ERSS at Mugliston Park Pumping Station"></div>
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
    <div class="w__media"><img src="../img/projects/c-kingfisher.jpg" alt="Footpath, timber railings and rock-edged stream at Kingfisher Wetland, Bay South"></div>
    <div class="w__copy">
      <span class="w__year">Completed</span>
      <h3>Kingfisher Wetland — Bay South, Gardens by the Bay</h3>
      <dl><dt>Owner</dt><dd>Gardens by the Bay · via TEHC International</dd>
          <dt>Value</dt><dd>S$436,500</dd>
          <dt>Speciality</dt><dd>Hardscape</dd></dl>
    </div>
  </article>

  <article class="w" data-i="05">
    <div class="w__no">05<span>&nbsp;/&nbsp;06</span></div>
    <div class="w__media"><img src="../img/projects/c-tampines.jpg" alt="Access steps and railings up a planted mound at Tampines Boulevard Park"></div>
    <div class="w__copy">
      <span class="w__year">Completed</span>
      <h3>Tampines Boulevard Park</h3>
      <dl><dt>Owner</dt><dd>NParks · via TEHC International</dd>
          <dt>Value</dt><dd>S$5,924,112</dd>
          <dt>Speciality</dt><dd>Civil Engineering · Hardscape</dd></dl>
    </div>
  </article>

  <article class="w" data-i="06">
    <div class="w__no">06<span>&nbsp;/&nbsp;06</span></div>
    <div class="w__media"><img src="../img/projects/c-bulim.jpg" alt="Shelter and planting along the estate spine at JTC Bulim Phase 1"></div>
    <div class="w__copy">
      <span class="w__year">Ongoing</span>
      <h3>JTC Bulim Phase 1 — Landscape &amp; Associated Works</h3>
      <dl><dt>Owner</dt><dd>JTC · via TEHC International</dd>
          <dt>Value</dt><dd>S$4,221,333</dd>
          <dt>Speciality</dt><dd>Steel Structures · Hardscape</dd></dl>
    </div>
  </article>

  <button class="works__more" type="button" data-action="register">+24 more — see the full register, all 30 <span aria-hidden="true">↗</span></button>
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
      <p>Earthworks and site formation, ERSS and sheet piling, reinforced concrete, drainage and roadworks — from bulk excavation and sheet-piled cofferdams around live structures to retaining walls, pump sumps, drains and asphalt premix.</p>
      <div class="showcase__chips"><span>Earthworks &amp; Site Formation</span><span>ERSS &amp; Sheet Piling</span><span>Reinforced Concrete</span><span>Drainage &amp; Roadworks</span><span>BCA CW02 · B2</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('../img/projects/t-ce-erss.jpg')"><figcaption>Sheet-piled ERSS with strutting — Mugliston Park Pumping Station</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/t-ce-margaret.jpg')"><figcaption>External works, premix &amp; drainage — Margaret Drive</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/t-ce-tampines.jpg')"><figcaption>Site formation &amp; park infrastructure — Tampines Boulevard Park</figcaption></figure>
    </div>
  </div>
  <div class="showcase__panel" id="demolition">
    <div class="showcase__lead">
      <h3>Demolition</h3>
      <p>Buildings, pumping stations and carparks — taken down safely on live, constrained sites. Deep basements removed inside sheet-piled ERSS, disused services grouted, and the land reinstated, with our own long-reach excavators and demolition attachments.</p>
      <div class="showcase__chips"><span>Deep Basement</span><span>Grouting</span><span>Pumping Stations</span><span>Land Reinstatement</span><span>BCA CR03</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('../img/projects/t-demo-mugliston.jpg')"><figcaption>Basement floor removal inside ERSS — Mugliston Park Pumping Station</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/t-demo-longreach.jpg')"><figcaption>Long-reach demolition — our own fleet</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/t-demo-basement.jpg')"><figcaption>Breaking out a deep basement</figcaption></figure>
    </div>
  </div>
  <div class="showcase__panel" id="hardscape">
    <div class="showcase__lead">
      <h3>Hardscape</h3>
      <p>Rubble walls, boardwalks and water-edge treatment, access steps, terraces and paths — the hard landscape that finishes a public space.</p>
      <div class="showcase__chips"><span>Rubble Wall</span><span>Boardwalk</span><span>Steps &amp; Terraces</span><span>Water-edge Treatment</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('../img/projects/t-hard-boardwalk.jpg')"><figcaption>Boardwalk &amp; water-edge treatment — Kingfisher Wetland</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/t-hard-rubble.jpg')"><figcaption>Rubble wall &amp; planted embankment</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/t-hard-steps.jpg')"><figcaption>Access steps &amp; terraces — ABC Waters, Jurong Canal</figcaption></figure>
    </div>
  </div>
  <div class="showcase__panel" id="steel">
    <div class="showcase__lead">
      <h3>Steel Structures</h3>
      <p>Shelters and shade structures for parks, playgrounds and waterways — fabricated and erected under our BCA Specialist Builder (Structural Steelwork) licence, married to the civil works beneath them.</p>
      <div class="showcase__chips"><span>Shelters</span><span>Shade Structures</span><span>Magical Bridge</span><span>ABC Waters</span><span>BCA SB(SS)</span></div>
    </div>
    <div class="showcase__grid">
      <figure class="sc-tile" style="--img:url('../img/projects/t-steel-stage.jpg')"><figcaption>Stage shelter — Magical Bridge Playground, Sun Plaza Park</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/t-steel-abc.jpg')"><figcaption>Canal-side shelter — ABC Waters, Jurong Canal</figcaption></figure>
      <figure class="sc-tile" style="--img:url('../img/projects/t-steel-bulim.jpg')"><figcaption>Shelters along the estate spine — JTC Bulim Phase 1</figcaption></figure>
    </div>
  </div>
</section>
'''

CREDS = '''<!-- AWARDS & CERTIFICATIONS -->
<section class="creds" id="credentials">
  <header class="sec-head">
    <span class="sec-head__num">—</span>
    <h2>Awards &amp; Certifications</h2>
    <span class="sec-head__meta">ISO · bizSAFE · BCA</span>
  </header>
  <div class="creds__grid">
    <figure><img src="../img/certs/iso-9001.jpg" alt="ISO 9001:2015 — Quality Management, valid to May 2029" loading="lazy"><figcaption>ISO 9001:2015 — Quality Management, valid to May 2029</figcaption></figure>
    <figure><img src="../img/certs/iso-14001.jpg" alt="ISO 14001:2015 — Environmental Management, valid to May 2029" loading="lazy"><figcaption>ISO 14001:2015 — Environmental Management, valid to May 2029</figcaption></figure>
    <figure><img src="../img/certs/iso-45001.jpg" alt="ISO 45001:2018 — Occupational Health &amp; Safety Management, valid to May 2029" loading="lazy"><figcaption>ISO 45001:2018 — Occupational Health &amp; Safety Management, valid to May 2029</figcaption></figure>
    <figure><img src="../img/certs/bizsafe-star.jpg" alt="bizSAFE Star — Workplace Safety and Health Council, valid to May 2029" loading="lazy"><figcaption>bizSAFE Star — Workplace Safety and Health Council, valid to May 2029</figcaption></figure>
    <figure><img src="../img/certs/green-gracious.jpg" alt="BCA Green and Gracious Builder Award — Merit, valid to May 2027" loading="lazy"><figcaption>BCA Green and Gracious Builder Award — Merit, valid to May 2027</figcaption></figure>
    <figure><img src="../img/certs/progressive-wage.jpg" alt="Progressive Wage Mark — valid to April 2027" loading="lazy"><figcaption>Progressive Wage Mark — valid to April 2027</figcaption></figure>
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
      <h3>Take pride of our works.</h3>
    </div>
    <div class="vmm__col">
      <span class="vmm__lbl">Mission</span>
      <h3>The best is yet to come.</h3>
    </div>
    <div class="vmm__col">
      <span class="vmm__lbl">Motto</span>
      <h3><em>Mission possible.</em></h3>
    </div>
  </div>
</section>
'''

VALUES = '''<!-- HOW WE WORK -->
<div class="values">
  <div class="values__head">
    <span class="values__lbl">How We Work</span>
    <h3 class="values__title">What we ask of ourselves on every contract.</h3>
  </div>
  <ol class="values__list">
    <li><span class="values__no">01</span><h4>Self-delivery</h4><p>Our own supervisors, our own plant. Programme and workmanship stay where the accountability sits.</p></li>
    <li><span class="values__no">02</span><h4>Safety led from the top</h4><p>A WSH and Environment team reporting to the Managing Director, with officers and supervisors on the ground.</p></li>
    <li><span class="values__no">03</span><h4>Relationships that repeat</h4><p>Thirteen of our thirty contracts for a single main contractor, worth more than S$44 million.</p></li>
    <li><span class="values__no">04</span><h4>Work that gets used</h4><p>Parks and playgrounds open to the public the week we leave. We finish them accordingly.</p></li>
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
    <p class="about__lead">Take pride of our works. <i>The best is yet to come.</i> — Mission possible.</p>
    <p>Techno&nbsp;CE&nbsp;Pte&nbsp;Ltd was incorporated on 20&nbsp;December&nbsp;2002 (UEN&nbsp;200210947C). We work from our office at D'Centennial in Geylang — with our own supervisors and our own plant on site. We do not subcontract our project management. We are on the sites we build.</p>
    <p>Our standards are certified to ISO 9001, ISO 14001, ISO 45001 and bizSAFE Star; our conduct on site is recognised by the BCA Green &amp; Gracious Builder Award, in which we hold Merit; and our pay by the Progressive Wage Mark.</p>
  </div>
</section>
'''

NEWS = '''<!-- NEWSROOM -->
<section class="news" id="newsroom">
  <div class="news__grid">
    <article class="post">
      <span class="post__date">Sep 2026</span>
      <h3>Company profile, Revision 1</h3>
      <p>Our updated profile: thirty contracts and S$62.6 million in aggregate contract value, five BCA workheads, and a fleet we own and operate ourselves.</p>
      <span class="post__tag">Company</span>
    </article>
    <article class="post">
      <span class="post__date">Jun 2026</span>
      <h3>Magical Bridge Playground handed over</h3>
      <p>Our design-and-build inclusive playground for NParks at Sun Plaza Park was handed over on 16 June 2026 and opened to the public the next day.</p>
      <span class="post__tag">Project · NParks</span>
    </article>
    <article class="post">
      <span class="post__date">May 2026</span>
      <h3>Recertified: ISO 9001, 14001 &amp; 45001 · bizSAFE Star</h3>
      <p>Our quality, environmental and safety management systems were recertified in April 2026, and bizSAFE Star — the highest level of the WSH Council's programme — renewed in May.</p>
      <span class="post__tag">Certification</span>
    </article>
    <article class="post">
      <span class="post__date">Ongoing</span>
      <h3>On site: JTC Bulim Phase 1</h3>
      <p>Shelters, shared paths and streetscape planting along the estate spine — our nominated sub-contract for landscape works within the Bulim Phase 1 infrastructure contract.</p>
      <span class="post__tag">Project · JTC</span>
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
      <p class="careers__perk">bizSAFE Star · ISO 45001 safety system · Progressive Wage Mark employer</p>
    </div>
    <ul class="careers__roles">
      <li><span class="careers__role-k">Open</span><h4>Project Engineer — Civil &amp; Demolition</h4><span class="careers__loc">Geylang HQ &amp; sites · Full-time</span></li>
      <li><span class="careers__role-k">Open</span><h4>Site Supervisor</h4><span class="careers__loc">Island-wide sites · Full-time</span></li>
      <li><span class="careers__role-k">Open</span><h4>Quantity Surveyor</h4><span class="careers__loc">Geylang HQ · Full-time</span></li>
      <li><span class="careers__role-k">Talent pool</span><h4>Plant &amp; Machinery Operator</h4><span class="careers__loc">Excavator / long-reach · Sites</span></li>
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
    "Vision, mission, how we work, awards and certifications of Techno CE Pte Ltd — a Singapore civil engineering contractor since 2002.",
    "about.html",
    pagehead("About Us", "A quiet practice,<br>since 2002.",
        "Our own supervisors, our own plant — for public agencies and the main contractors delivering on their behalf.")
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
    "A glimpse of our projects — Magical Bridge Playground, ABC Waters at Jurong Canal, Mugliston Park Pumping Station, Kingfisher Wetland, Tampines Boulevard Park and JTC Bulim. Thirty contracts, S$62.6 million.",
    "projects.html",
    pagehead("Projects", "A glimpse of our work.",
        "Six of our thirty contracts — for PUB, NParks, JTC and Gardens by the Bay.")
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
    "Join a small team on real sites. bizSAFE Star, an ISO 45001 safety system and a Progressive Wage Mark employer.",
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
