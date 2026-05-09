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
  setInterval(()=>{
    slides[idx].classList.remove('is-active');
    idx=(idx+1)%slides.length;
    slides[idx].classList.add('is-active');
    if(capEl){
      capEl.querySelector('.caption-num').textContent=captions[idx].n;
      capEl.querySelector('.caption-text').textContent=captions[idx].t;
    }
  }, 6000);

  // ---------- Counter animation (engineer-precision feel) ----------
  const counters=$$('[data-counter]');
  const animateCount=(el)=>{
    const target=parseInt(el.dataset.counter,10);
    el.style.fontVariantNumeric='tabular-nums lining-nums';
    if(matchMedia('(prefers-reduced-motion: reduce)').matches){
      el.textContent=target.toLocaleString();return;
    }
    const dur=1900;const t0=performance.now();
    const tick=(t)=>{
      const p=Math.min((t-t0)/dur,1);
      const eased=1-Math.pow(1-p,4); /* quartic-out: settles, not blasts */
      el.textContent=Math.round(target*eased).toLocaleString();
      if(p<1) requestAnimationFrame(tick);
      else el.textContent=target.toLocaleString();
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

  // ---------- Scroll reveal (with fallbacks) ----------
  const revealTargets=$$('.cap, .stat, .manifesto__lead, .manifesto__body, .creds__certs figure, .about__col, .contact__grid > div');
  const reducedMotion=matchMedia('(prefers-reduced-motion: reduce)').matches;
  if(reducedMotion || !('IntersectionObserver' in window)){
    revealTargets.forEach(el=>el.classList.add('is-in'));
  } else {
    revealTargets.forEach(el=>el.classList.add('reveal'));
    const revealObs=new IntersectionObserver((entries)=>{
      entries.forEach((e,i)=>{
        if(e.isIntersecting){
          setTimeout(()=>e.target.classList.add('is-in'), i*60);
          revealObs.unobserve(e.target);
        }
      });
    },{threshold:0.08, rootMargin:'0px 0px -5% 0px'});
    revealTargets.forEach(t=>revealObs.observe(t));
    setTimeout(()=>revealTargets.forEach(t=>t.classList.add('is-in')), 4000);
  }

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

  // ---------- Smooth burger (mobile placeholder) ----------
  const burger=$('#burger');
  if(burger){
    burger.addEventListener('click',()=>{
      const links=$('.nav__links');
      links.style.display = links.style.display==='flex'?'none':'flex';
      links.style.position='fixed';
      links.style.top='4rem';links.style.right='1rem';
      links.style.flexDirection='column';
      links.style.background='var(--paper)';
      links.style.padding='1.5rem';
      links.style.gap='1rem';
      links.style.border='1px solid rgba(0,0,0,.1)';
    });
  }
})();
