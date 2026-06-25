/* ====================================================================
   TECHNO CE — Premium motion layer
   Intro · scroll progress · reveal choreography · hero parallax ·
   scrollspy · magnetic buttons · custom cursor · (marquee is CSS).
   Everything degrades gracefully: if this file errors, a catch reveals
   all content and removes motion gating so the page is never stuck.
   ==================================================================== */
(() => {
  const root = document.documentElement;
  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine   = matchMedia('(hover:hover) and (pointer:fine)').matches;
  const hasIO  = 'IntersectionObserver' in window;

  try {
    // ---------- Scroll progress bar ----------
    const prog = $('.progress');
    if (prog) {
      let raf = false;
      const upd = () => {
        const max = root.scrollHeight - window.innerHeight;
        prog.style.transform = 'scaleX(' + (max > 0 ? window.scrollY / max : 0) + ')';
        raf = false;
      };
      const tick = () => { if (!raf) { requestAnimationFrame(upd); raf = true; } };
      addEventListener('scroll', tick, { passive: true });
      addEventListener('resize', tick); upd();
    }

    // ---------- Remove the intro preloader node after it wipes away ----------
    const pre = $('.preloader');
    if (pre) {
      if (reduce) pre.remove();
      else {
        pre.addEventListener('animationend', e => { if (e.animationName === 'plExit') pre.remove(); });
        setTimeout(() => pre.remove(), 3200); // failsafe
      }
    }

    if (!reduce && hasIO) {
      // ---------- Reveal choreography ----------
      const groups = {
        'r-mask': ['.manifesto__lead', '.pullquote blockquote', '.contact__hero', '.values__title', '.media__lead', '.careers__intro h3', '.showcase__lead h3'],
        'r-up'  : ['.stat', '.cap', '.values__list li', '.post', '.careers__roles li', '.contact__grid > div', '.manifesto__body', '.about__col', '.careers__intro p', '.careers__perk', '.showcase__lead p', '.showcase__chips', '.creds__verify', '.creds__table', '.news__note'],
        'r-img' : ['.vtile'],
        'r-fade': ['.card', '.creds__certs figure']
      };
      const all = [];
      Object.keys(groups).forEach(cls => groups[cls].forEach(sel => $$(sel).forEach(el => {
        if (el.dataset.rev) return;
        // Skip elements inside a closed showcase tab — the panel's own
        // fade handles them when opened; otherwise they'd wait for the failsafe.
        if (el.closest('.showcase__panel[hidden]')) return;
        el.dataset.rev = '1';
        el.classList.add(cls);
        all.push(el);
      })));

      // Stagger siblings that share a parent
      const byParent = new Map();
      all.forEach(el => {
        const p = el.parentElement;
        if (!byParent.has(p)) byParent.set(p, []);
        byParent.get(p).push(el);
      });
      byParent.forEach(list => {
        if (list.length > 1) list.forEach((el, i) => el.style.setProperty('--d', Math.min(i, 8) * 70 + 'ms'));
      });

      const obs = new IntersectionObserver((entries) => {
        entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); obs.unobserve(e.target); } });
      }, { threshold: 0.12, rootMargin: '0px 0px -6% 0px' });
      all.forEach(el => obs.observe(el));
      setTimeout(() => all.forEach(el => el.classList.add('in')), 3000); // failsafe

      // ---------- Hero parallax (capped to its safe-zone so it never gaps) ----------
      const hero = $('.hero'), heroMedia = $('.hero__media');
      if (hero && heroMedia) {
        let raf = false;
        const move = () => {
          const y = window.scrollY;
          if (y < window.innerHeight) {
            // Cap to the media's over-scan (top:-9% → 9% headroom) so it never gaps.
            const ty = Math.min(y * 0.08, hero.offsetHeight * 0.085);
            heroMedia.style.transform = 'translateY(' + ty + 'px)';
          }
          raf = false;
        };
        addEventListener('scroll', () => { if (!raf) { requestAnimationFrame(move); raf = true; } }, { passive: true });
      }

      // ---------- Magnetic buttons ----------
      if (fine) {
        $$('[data-magnetic]').forEach(el => {
          const k = parseFloat(el.dataset.magnetic) || 0.3;
          let mraf = false, cx = 0, cy = 0;
          el.addEventListener('mousemove', e => {
            cx = e.clientX; cy = e.clientY;
            if (mraf) return; mraf = true;
            requestAnimationFrame(() => {
              const r = el.getBoundingClientRect();
              el.style.transform = 'translate(' + (cx - (r.left + r.width / 2)) * k + 'px,' + (cy - (r.top + r.height / 2)) * k + 'px)';
              mraf = false;
            });
          });
          el.addEventListener('mouseleave', () => { el.style.transform = ''; });
        });
      }

      // ---------- Custom cursor ----------
      if (fine) {
        const ring = document.createElement('div'); ring.className = 'cursor';
        const dot  = document.createElement('div'); dot.className  = 'cursor__dot';
        document.body.append(ring, dot);
        root.classList.add('has-cursor');
        let mx = innerWidth / 2, my = innerHeight / 2, rx = mx, ry = my;
        addEventListener('mousemove', e => {
          mx = e.clientX; my = e.clientY;
          dot.style.transform = 'translate(' + mx + 'px,' + my + 'px) translate(-50%,-50%)';
        });
        let cRaf = null;
        const loop = () => {
          rx += (mx - rx) * 0.18; ry += (my - ry) * 0.18;
          ring.style.transform = 'translate(' + rx + 'px,' + ry + 'px) translate(-50%,-50%)';
          cRaf = requestAnimationFrame(loop);
        };
        cRaf = requestAnimationFrame(loop);
        document.addEventListener('visibilitychange', () => {
          if (document.hidden) { if (cRaf) { cancelAnimationFrame(cRaf); cRaf = null; } }
          else if (!cRaf) { cRaf = requestAnimationFrame(loop); }
        });
        const HOV = 'a,button,[data-magnetic],.showcase__tab,.vtile,.reg-row,.card';
        document.addEventListener('mouseover', e => { if (e.target.closest(HOV)) ring.classList.add('is-hover'); });
        document.addEventListener('mouseout',  e => { if (e.target.closest(HOV)) ring.classList.remove('is-hover'); });
        document.addEventListener('mouseleave', () => { ring.style.opacity = '0'; dot.style.opacity = '0'; });
        document.addEventListener('mouseenter', () => { ring.style.opacity = ''; dot.style.opacity = ''; });
      }
    }

    // ---------- Scrollspy: highlight the nav link of the section in view ----------
    if (hasIO) {
      const links = $$('.nav__links a[href^="#"]');
      const map = links.map(a => ({ a, sec: document.querySelector(a.getAttribute('href')) })).filter(o => o.sec);
      if (map.length) {
        const visible = new Set();
        const spy = new IntersectionObserver((entries) => {
          entries.forEach(e => { e.isIntersecting ? visible.add(e.target) : visible.delete(e.target); });
          const current = map.find(o => visible.has(o.sec)); // first in DOM order = topmost
          if (current) {
            links.forEach(a => a.classList.remove('is-active'));
            current.a.classList.add('is-active');
          }
        }, { rootMargin: '-45% 0px -50% 0px' });
        map.forEach(o => spy.observe(o.sec));
      }
    }
  } catch (err) {
    // Never let a motion failure hide the site.
    root.classList.remove('motion');
    $$('[data-rev]').forEach(el => el.classList.add('in'));
    const pre = $('.preloader'); if (pre) pre.remove();
    console.error('[premium.js] disabled motion after error:', err);
  }
})();
