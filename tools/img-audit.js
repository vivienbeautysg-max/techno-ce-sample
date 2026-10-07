/* Image-fit audit — run in the browser console on any page of the site
   (or via the preview tool). For every photo slot on every page it measures
   the rendered box and the source image, and flags:
     UPSCALE  device pixels needed > source pixels × 1.25 (blurry)
     CROP     less than 40% of the source width or height left visible
   Usage: await TCE_imgAudit()  → array of rows; failures have ok:false.
   Rules: device pixel ratio is counted up to 2 (3x phones are served 2x, the
   usual practice — the difference is not visible at phone size). Page-header
   bands (.pagehead, a 34%-opacity texture) are exempt from CROP, not UPSCALE.
   FLUTTER-NO: maintenance script for an existing static HTML site. */
window.TCE_imgAudit = async function (opts) {
  const o = Object.assign({
    pages: ['index.html', 'about.html', 'services.html', 'projects.html', 'newsroom.html', 'careers.html', 'contact.html'],
    variants: ['', 'v2/'],
    views: [[1280, 800, 1], [1440, 900, 2], [1960, 1895, 1.5], [2560, 1440, 1],
            [1024, 1366, 2], [768, 1024, 2], [430, 932, 3], [375, 812, 3]],
    maxUpscale: 1.25, minVisible: 0.4
  }, opts || {});
  const root = location.href.replace(/(v2\/)?[^\/]*$/, '');
  const natCache = {};
  const nat = (u) => natCache[u] || (natCache[u] = new Promise((res) => {
    const i = new Image(); i.onload = () => res([i.naturalWidth, i.naturalHeight]); i.onerror = () => res(null); i.src = u;
  }));
  const urlOf = (bg) => { const m = bg && bg.match(/url\(["']?([^"')]+)["']?\)/); return m ? m[1] : null; };
  const rows = [];
  for (const [w, h, dpr] of o.views) {
    for (const v of o.variants) for (const p of o.pages) {
      const f = document.createElement('iframe');
      f.style.cssText = `position:fixed;left:-30000px;top:0;width:${w}px;height:${h}px;border:0`;
      document.body.appendChild(f);
      const loaded = new Promise((r) => f.addEventListener('load', r, { once: true }));
      f.src = root + v + p + '?audit=' + Date.now(); await loaded; await new Promise((r) => setTimeout(r, 700));
      const d = f.contentDocument, win = f.contentWindow;
      const slots = [];
      d.querySelectorAll('body *').forEach((el) => {
        if (el.closest('.preloader')) return;
        if (el.tagName === 'IMG') {
          if (/logo\.svg/.test(el.src)) return;
          slots.push({ el, url: el.currentSrc || el.src, fit: win.getComputedStyle(el).objectFit });
          return;
        }
        for (const pseudo of [null, '::before', '::after']) {
          const cs = win.getComputedStyle(el, pseudo);
          const u = urlOf(cs.backgroundImage);
          if (u && /\.(jpe?g|png|webp)/i.test(u)) slots.push({ el, url: u, fit: cs.backgroundSize === 'cover' ? 'cover' : cs.backgroundSize, pseudo });
        }
      });
      for (const s of slots) {
        const r = s.el.getBoundingClientRect();
        if (r.width < 40 || r.height < 40) continue;
        const n = await nat(new URL(s.url, f.src).href);
        if (!n) { rows.push({ view: `${w}x${h}@${dpr}`, page: v + p, img: s.url, ok: false, why: 'MISSING' }); continue; }
        const [nw, nh] = n;
        const cover = s.fit === 'cover' || s.fit === 'auto' || !s.fit;
        const sc = cover ? Math.max(r.width / nw, r.height / nh) : Math.min(r.width / nw, r.height / nh);
        const up = sc * Math.min(dpr, 2);
        const visW = Math.min(1, r.width / sc / nw), visH = Math.min(1, r.height / sc / nh);
        const why = [];
        if (up > o.maxUpscale) why.push('UPSCALE');
        if (cover && !s.el.closest('.pagehead') && Math.min(visW, visH) < o.minVisible) why.push('CROP');
        rows.push({ view: `${w}x${h}@${dpr}`, page: v + p, img: s.url.split('/').pop(), box: `${Math.round(r.width)}x${Math.round(r.height)}`,
          natural: `${nw}x${nh}`, upscale: +up.toFixed(2), visible: `${visW.toFixed(2)}w ${visH.toFixed(2)}h`, ok: !why.length, why: why.join('+') });
      }
      f.remove();
    }
  }
  return rows;
};
