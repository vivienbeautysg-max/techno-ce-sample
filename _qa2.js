const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch();
  const ctx = await browser.newContext();

  // ---------- v1 desktop ----------
  let p = await ctx.newPage();
  await p.setViewportSize({width:1440,height:900});
  await p.goto('http://localhost:8765/', {waitUntil:'networkidle'});
  await p.waitForTimeout(2500);
  await p.screenshot({path:'qa-v1-hero.jpg', quality:80, type:'jpeg'});
  await p.evaluate(()=>document.querySelector('[data-action=register]').click());
  await p.waitForTimeout(800);
  await p.screenshot({path:'qa-v1-register.jpg', quality:80, type:'jpeg'});
  await p.close();

  // ---------- v1 mobile ----------
  p = await ctx.newPage();
  await p.setViewportSize({width:390,height:844});
  await p.goto('http://localhost:8765/', {waitUntil:'networkidle'});
  await p.waitForTimeout(2500);
  await p.screenshot({path:'qa-v1-m-hero.jpg', quality:80, type:'jpeg'});
  await p.evaluate(()=>window.scrollTo(0,window.innerHeight*1.05));
  await p.waitForTimeout(600);
  await p.screenshot({path:'qa-v1-m-receipts.jpg', quality:80, type:'jpeg'});
  await p.evaluate(()=>window.scrollTo(0,window.innerHeight*3.5));
  await p.waitForTimeout(600);
  await p.screenshot({path:'qa-v1-m-work.jpg', quality:80, type:'jpeg'});
  await p.close();

  // ---------- v2 desktop ----------
  p = await ctx.newPage();
  await p.setViewportSize({width:1440,height:900});
  await p.goto('http://localhost:8765/v2/', {waitUntil:'networkidle'});
  await p.waitForTimeout(2500);
  await p.screenshot({path:'qa-v2-hero.jpg', quality:80, type:'jpeg'});
  await p.evaluate(()=>window.scrollTo(0,window.innerHeight*1.1));
  await p.waitForTimeout(600);
  await p.screenshot({path:'qa-v2-index.jpg', quality:80, type:'jpeg'});
  await p.evaluate(()=>window.scrollTo(0,window.innerHeight*2.4));
  await p.waitForTimeout(600);
  await p.screenshot({path:'qa-v2-works.jpg', quality:80, type:'jpeg'});
  await p.evaluate(()=>window.scrollTo(0,document.body.scrollHeight*0.7));
  await p.waitForTimeout(600);
  await p.screenshot({path:'qa-v2-creds.jpg', quality:80, type:'jpeg'});
  await p.close();

  // ---------- v2 mobile ----------
  p = await ctx.newPage();
  await p.setViewportSize({width:390,height:844});
  await p.goto('http://localhost:8765/v2/', {waitUntil:'networkidle'});
  await p.waitForTimeout(2500);
  await p.screenshot({path:'qa-v2-m-hero.jpg', quality:80, type:'jpeg'});
  await p.close();

  await browser.close();
  console.log('done');
})();
