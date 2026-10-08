import { chromium } from 'playwright-core';
const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
const p=await b.newPage({viewport:{width:430,height:900},deviceScaleFactor:2});
const errs=[];p.on('pageerror',e=>errs.push(e.message));
// delay live API so skeletons are visible
await p.route('**/api/live/**',async r=>{await new Promise(x=>setTimeout(x,2500));r.continue();});
await p.goto('http://localhost:8787/#home');
await p.evaluate(()=>{localStorage.setItem('clubhub-myclub','"galatasaray"');localStorage.setItem('clubhub-seenWelcome','1')});
await p.reload();await p.waitForTimeout(700);
await p.screenshot({path:'t6shots/skel-home.png',fullPage:false});
// club page load (league file is local, fast; but season tab uses live) -> open season
await p.goto('http://localhost:8787/#galatasarayseason');await p.waitForTimeout(700);
await p.screenshot({path:'t6shots/skel-season.png',fullPage:false});
console.log('errors:',errs.length?errs:'none');
await b.close();
