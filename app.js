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

  // ---------- Counter animation ----------
  const counters=$$('[data-counter]');
  const animateCount=(el)=>{
    const target=parseInt(el.dataset.counter,10);
    const dur=1400;const t0=performance.now();
    const tick=(t)=>{
      const p=Math.min((t-t0)/dur,1);
      const eased=1-Math.pow(1-p,3);
      el.textContent=Math.round(target*eased);
      if(p<1) requestAnimationFrame(tick);
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

  // ---------- Scroll reveal ----------
  const revealTargets=$$('.cap, .stat, .manifesto__lead, .manifesto__body, .creds__certs figure, .about__col, .contact__grid > div');
  revealTargets.forEach(el=>el.classList.add('reveal'));
  const revealObs=new IntersectionObserver((entries)=>{
    entries.forEach((e,i)=>{
      if(e.isIntersecting){
        setTimeout(()=>e.target.classList.add('is-in'), i*60);
        revealObs.unobserve(e.target);
      }
    });
  },{threshold:0.15});
  revealTargets.forEach(t=>revealObs.observe(t));

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
