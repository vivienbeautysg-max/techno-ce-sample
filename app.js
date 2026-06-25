/* TECHNO CE — minimal motion */
(()=>{
  const $=(s,r=document)=>r.querySelector(s);
  const $$=(s,r=document)=>[...r.querySelectorAll(s)];

  // ---------- Nav: pin background after scroll past hero ----------
  const nav=$('#nav');
  const onScroll=()=>{
    const past=window.scrollY > window.innerHeight * 0.85;
    nav.classList.toggle('is-pinned', past);
  };
  window.addEventListener('scroll', onScroll, {passive:true});
  onScroll();

  // ---------- Hero mask-reveal on load ----------
  requestAnimationFrame(()=>document.querySelector('.hero')?.classList.add('is-loaded'));

  // ---------- Hero slideshow ----------
  const slides=$$('.hero__slide');
  const captions=[
    {n:'01 / 03', t:'Singapore Island Country Club — redevelopment, S$7.34M'},
    {n:'02 / 03', t:'ERSS sheet piling — Lower Seletar Reservoir'},
    {n:'03 / 03', t:'Kingfisher Wetland — Bay South, Gardens by the Bay'}
  ];
  const capEl=$('#heroCaption');
  let idx=0;
  if(!matchMedia('(prefers-reduced-motion: reduce)').matches){
    setInterval(()=>{
      slides[idx].classList.remove('is-active');
      idx=(idx+1)%slides.length;
      slides[idx].classList.add('is-active');
      if(capEl){
        capEl.querySelector('.caption-num').textContent=captions[idx].n;
        capEl.querySelector('.caption-text').textContent=captions[idx].t;
      }
    }, 6000);
  }

  // ---------- Counter animation (engineer-precision feel) ----------
  const counters=$$('[data-counter]');
  const fmtNum=(v,decimals=0)=>{
    if(decimals>0){
      const fixed=v.toFixed(decimals);
      const [whole,frac]=fixed.split('.');
      return parseInt(whole,10).toLocaleString()+'.'+frac;
    }
    return Math.round(v).toLocaleString();
  };
  const animateCount=(el)=>{
    const target=parseFloat(el.dataset.counter);
    const decimals=parseInt(el.dataset.decimals||'0',10);
    el.style.fontVariantNumeric='tabular-nums lining-nums';
    if(matchMedia('(prefers-reduced-motion: reduce)').matches){
      el.textContent=fmtNum(target,decimals);return;
    }
    const dur=1900;const t0=performance.now();
    const tick=(t)=>{
      const p=Math.min((t-t0)/dur,1);
      const eased=1-Math.pow(1-p,4);
      el.textContent=fmtNum(target*eased,decimals);
      if(p<1) requestAnimationFrame(tick);
      else el.textContent=fmtNum(target,decimals);
    };
    requestAnimationFrame(tick);
  };
  const countObs=new IntersectionObserver((entries)=>{
    entries.forEach(e=>{
      if(e.isIntersecting){
        animateCount(e.target);
        countObs.unobserve(e.target);
      }
    });
  },{threshold:0.4});
  counters.forEach(c=>countObs.observe(c));

  // ---------- Rule (measurement line) reveal ----------
  const rules=$$('.rule:not(.hero__rule)');
  if(!matchMedia('(prefers-reduced-motion: reduce)').matches && 'IntersectionObserver' in window){
    const ruleObs=new IntersectionObserver((es)=>{
      es.forEach(e=>{
        if(e.isIntersecting){e.target.classList.add('is-in');ruleObs.unobserve(e.target);}
      });
    },{threshold:0.5});
    rules.forEach(r=>ruleObs.observe(r));
  } else {
    rules.forEach(r=>r.classList.add('is-in'));
  }

  // ---------- Scroll reveal handled in premium.js (upgraded motion layer) ----------

  // ---------- Projects data binding (full register modal) ----------
  let projectData=null;
  const fmt=v=>'S$'+(v/1000>=1000?(v/1000000).toFixed(2)+'M':Math.round(v/1000)+'K');
  const loadProjects=async()=>{
    if(projectData) return projectData;
    const r=await fetch('projects.json');
    projectData=await r.json();
    return projectData;
  };
  const openRegister=async()=>{
    const data=await loadProjects();
    const trigger=document.activeElement;
    const dlg=document.createElement('div');
    dlg.className='register';
    dlg.innerHTML=`
      <div class="register__sheet" role="dialog" aria-modal="true" aria-labelledby="regTitle">
        <header class="register__head">
          <div>
            <span class="register__tag">FULL PROJECT REGISTER</span>
            <h2 id="regTitle">${data.projects.length} projects · S$${(data.projects.reduce((s,p)=>s+p.value,0)/1e6).toFixed(1)}M total</h2>
          </div>
          <button class="register__close" type="button">CLOSE <span aria-hidden="true">✕</span></button>
        </header>
        <div class="register__filters">
          ${['all','demolition','civil','piling','landscape','road'].map(s=>`<button data-scope="${s}" class="${s==='all'?'is-on':''}">${s.toUpperCase()}</button>`).join('')}
        </div>
        <div class="register__list">
          ${data.projects.sort((a,b)=>b.value-a.value).map(p=>`
            <article class="reg-row" data-scope="${p.scope}">
              <span class="reg-row__year">${p.year}</span>
              <span class="reg-row__title">${p.title}</span>
              <span class="reg-row__owner">${p.owner}</span>
              <span class="reg-row__value">${fmt(p.value)}</span>
              <span class="reg-row__status reg-row__status--${p.status}">${p.status==='ongoing'?'● ONGOING':'✓ COMPLETED'}</span>
            </article>`).join('')}
        </div>
        <footer class="register__foot">
          UEN 200210947C · Verify on <a href="https://www1.bca.gov.sg/bca-directory" target="_blank" rel="noopener">BCA Directory</a>
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
        const f=focusables();if(!f.length) return;
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
  $$('[data-action="register"], .card__sum-link').forEach(el=>{
    el.addEventListener('click',e=>{e.preventDefault();openRegister();});
  });

  // ---------- Showcase category tabs ----------
  const scTabs=$$('.showcase__tab');
  const scPanels=$$('.showcase__panel');
  const showPanel=(key)=>{
    scTabs.forEach(t=>{
      const on=t.dataset.panel===key;
      t.classList.toggle('is-on',on);
      t.setAttribute('aria-selected',on?'true':'false');
      t.tabIndex=on?0:-1;
    });
    scPanels.forEach(p=>{
      const on=p.dataset.panel===key;
      p.classList.toggle('is-on',on);
      if(on){p.removeAttribute('hidden');}
      else{p.setAttribute('hidden','');}
    });
  };
  scTabs.forEach((tab,i)=>{
    tab.addEventListener('click',()=>showPanel(tab.dataset.panel));
    tab.addEventListener('keydown',(e)=>{
      if(e.key!=='ArrowRight'&&e.key!=='ArrowLeft') return;
      e.preventDefault();
      const dir=e.key==='ArrowRight'?1:-1;
      const next=scTabs[(i+dir+scTabs.length)%scTabs.length];
      showPanel(next.dataset.panel);
      next.focus();
    });
  });

  // ---------- Media tiles (sample placeholders — honest feedback) ----------
  $$('.vtile').forEach(v=>{
    v.addEventListener('click',()=>{
      if(v.querySelector('.vtile__hint')) return;
      const hint=document.createElement('span');
      hint.className='vtile__hint';
      hint.textContent='Sample tile — final video to be embedded';
      hint.style.cssText='position:absolute;inset:auto 0 0 0;z-index:3;padding:.6rem .9rem;'+
        'font:500 .68rem/1.4 var(--mono);letter-spacing:.04em;color:var(--paper);'+
        'background:var(--brand-deep);text-align:center;';
      v.appendChild(hint);
      setTimeout(()=>hint.remove(),2200);
    });
  });

  // ---------- Mobile burger ----------
  const burger=$('#burger'),navLinks=$('.nav__links');
  if(burger&&navLinks){
    burger.setAttribute('aria-expanded','false');
    burger.setAttribute('aria-label','Open menu');
    burger.addEventListener('click',()=>{
      const open=navLinks.classList.toggle('is-open');
      burger.setAttribute('aria-expanded',open);
      burger.setAttribute('aria-label',open?'Close menu':'Open menu');
    });
    navLinks.querySelectorAll('a').forEach(a=>a.addEventListener('click',()=>{
      navLinks.classList.remove('is-open');
      burger.setAttribute('aria-expanded','false');
      burger.setAttribute('aria-label','Open menu');
    }));
  }
})();
