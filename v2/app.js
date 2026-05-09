/* TECHNO CE — Variant B */
(()=>{
  const $=(s,r=document)=>r.querySelector(s);
  const $$=(s,r=document)=>[...r.querySelectorAll(s)];

  // ---------- Hero crossfade ----------
  const hImgs=$$('.hero__img');
  let hi=0;
  setInterval(()=>{
    hImgs[hi].classList.remove('is-on');
    hi=(hi+1)%hImgs.length;
    hImgs[hi].classList.add('is-on');
  },5500);

  // ---------- Reveal (with fallbacks) ----------
  const targets=$$('.w, .caps__list li, .num__grid > div, .creds__grid figure, .index__row');
  const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(reduced || !('IntersectionObserver' in window)){
    targets.forEach(t=>t.classList.add('is-in'));
  } else {
    targets.forEach(t=>t.classList.add('reveal'));
    const obs=new IntersectionObserver((es)=>{
      es.forEach((e,i)=>{
        if(e.isIntersecting){
          setTimeout(()=>e.target.classList.add('is-in'), i*70);
          obs.unobserve(e.target);
        }
      });
    },{threshold:0.08, rootMargin:'0px 0px -5% 0px'});
    targets.forEach(t=>obs.observe(t));
    // Safety net: force reveal anything still hidden after 4s
    setTimeout(()=>targets.forEach(t=>t.classList.add('is-in')), 4000);
  }

  // ---------- Mobile burger ----------
  const burger=$('#burger'),navLinks=$('#navLinks');
  if(burger&&navLinks){
    burger.addEventListener('click',()=>{
      const open=navLinks.classList.toggle('is-open');
      burger.setAttribute('aria-expanded',open);
      burger.setAttribute('aria-label',open?'Close menu':'Open menu');
    });
    navLinks.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
      navLinks.classList.remove('is-open');
      burger.setAttribute('aria-expanded','false');
    }));
  }

  // ---------- Project register ----------
  let data=null;
  const fmt=v=>'S$'+(v/1000>=1000?(v/1000000).toFixed(2)+'M':Math.round(v/1000)+'K');
  const load=async()=>{
    if(data) return data;
    const r=await fetch('../projects.json');
    data=await r.json();
    return data;
  };
  const open=async()=>{
    const d=await load();
    const trigger=document.activeElement;
    const dlg=document.createElement('div');
    dlg.className='register';
    dlg.innerHTML=`
      <div class="register__sheet" role="dialog" aria-modal="true" aria-labelledby="regTitle2">
        <header class="register__head">
          <div>
            <span class="register__tag">FULL PROJECT REGISTER</span>
            <h2 id="regTitle2">${d.projects.length} projects · S$${(d.projects.reduce((s,p)=>s+p.value,0)/1e6).toFixed(1)}M total value</h2>
          </div>
          <button class="register__close" type="button">CLOSE <span aria-hidden="true">✕</span></button>
        </header>
        <div class="register__filters">
          ${['all','demolition','civil','piling','landscape','road'].map(s=>`<button data-scope="${s}" class="${s==='all'?'is-on':''}">${s.toUpperCase()}</button>`).join('')}
        </div>
        <div class="register__list">
          ${d.projects.sort((a,b)=>b.value-a.value).map(p=>`
            <article class="reg-row" data-scope="${p.scope}">
              <span class="reg-row__year">${p.year}</span>
              <span class="reg-row__title">${p.title}</span>
              <span class="reg-row__owner">${p.owner}</span>
              <span class="reg-row__value">${fmt(p.value)}</span>
              <span class="reg-row__status reg-row__status--${p.status}">${p.status==='ongoing'?'● ONGOING':'✓ COMPLETED'}</span>
            </article>`).join('')}
        </div>
        <footer class="register__foot">
          <span>UEN 200210947C</span>
          <span>Verify on <a href="https://www1.bca.gov.sg/bca-directory" target="_blank" rel="noopener">BCA Directory</a></span>
        </footer>
      </div>`;
    document.body.appendChild(dlg);
    document.body.style.overflow='hidden';
    requestAnimationFrame(()=>dlg.classList.add('is-open'));
    const focusables=()=>[...dlg.querySelectorAll('button,a[href],[tabindex]:not([tabindex="-1"])')].filter(el=>!el.disabled);
    const close=()=>{
      dlg.classList.remove('is-open');
      document.body.style.overflow='';
      setTimeout(()=>{dlg.remove();trigger&&trigger.focus&&trigger.focus();},300);
      document.removeEventListener('keydown',onKey);
    };
    const onKey=(e)=>{
      if(e.key==='Escape') close();
      else if(e.key==='Tab'){
        const f=focusables();
        if(!f.length) return;
        const first=f[0],last=f[f.length-1];
        if(e.shiftKey && document.activeElement===first){last.focus();e.preventDefault();}
        else if(!e.shiftKey && document.activeElement===last){first.focus();e.preventDefault();}
      }
    };
    document.addEventListener('keydown',onKey);
    dlg.querySelector('.register__close').addEventListener('click',close);
    dlg.addEventListener('click',e=>{if(e.target===dlg) close();});
    setTimeout(()=>{const f=focusables();f[0]&&f[0].focus();},50);
    dlg.querySelectorAll('.register__filters button').forEach(b=>{
      b.addEventListener('click',()=>{
        dlg.querySelectorAll('.register__filters button').forEach(x=>x.classList.remove('is-on'));
        b.classList.add('is-on');
        const sc=b.dataset.scope;
        dlg.querySelectorAll('.reg-row').forEach(r=>{
          r.style.display=(sc==='all'||r.dataset.scope===sc)?'':'none';
        });
      });
    });
  };
  $$('[data-action="register"]').forEach(el=>el.addEventListener('click',e=>{e.preventDefault();open();}));
})();
