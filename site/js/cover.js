/* ============================================================
   BluePrint — cover.js
   Drives the pinned home cover. Bails out safely if the cover
   markup is not on the page.
   ============================================================ */
(function () {
  'use strict';
  if (!document.getElementById('wrap')) return;

const MK=[
 {x:22,y:36,c:'AIR QUALITY',v:'boundary &amp; stack',f:.08,t:.50},
 {x:66,y:26,c:'METEOROLOGY',v:'wind &middot; temp',f:.18,t:.62},
 {x:80,y:58,c:'WATER',v:'effluent &amp; discharge',f:.30,t:.78},
 {x:38,y:70,c:'NOISE',v:'boundary &amp; receptor',f:.42,t:.92},
 {x:56,y:45,c:'SOIL',v:'contaminants',f:.54,t:1.04}];

const c01=v=>Math.max(0,Math.min(1,v)), rmp=(p,a,b)=>c01((p-a)/(b-a)), sm=v=>v*v*(3-2*v),
      win=(p,a,b,f=.09)=>sm(rmp(p,a,a+f))*(1-sm(rmp(p,b-f,b)));

/* markers */
const mkL=document.getElementById('mkLayer');
MK.forEach(m=>{const d=document.createElement('div');d.className='mk';
 d.style.left=m.x+'%';d.style.top=m.y+'%';
 d.innerHTML='<span class="mk-d"></span><span class="mk-b"><span class="mk-c">'+m.c+'</span><span class="mk-v">'+m.v+'</span></span>';
 mkL.appendChild(d);m.n=d;});

/* contour lines + scanning band */
const svg=document.getElementById('netSvg');
svg.setAttribute('viewBox','0 0 100 100');
svg.setAttribute('preserveAspectRatio','none');
const NS='http://www.w3.org/2000/svg';
const el=(t,a={})=>{const e=document.createElementNS(NS,t);
  for(const k in a)e.setAttribute(k,a[k]);
  e.setAttribute('vector-effect','non-scaling-stroke');return e;};

const defs=el('defs');
defs.innerHTML='<linearGradient id="bpSweep" x1="0" x2="1">'
  +'<stop offset="0" stop-color="#8fe7f7" stop-opacity="0"/>'
  +'<stop offset=".72" stop-color="#8fe7f7" stop-opacity=".07"/>'
  +'<stop offset="1" stop-color="#8fe7f7" stop-opacity=".16"/></linearGradient>';
svg.appendChild(defs);

[[80,2.6,1.6,'contour',11000,0],
 [86,2.0,1.2,'contour faint',14000,1200]].forEach(([base,a1,a2,cls,dur,delay])=>{
  let d='M-4 '+base;
  for(let x=-4;x<=104;x+=4)
    d+=' L'+x+' '+(base-Math.sin(x*0.105)*a1-Math.cos(x*0.047)*a2).toFixed(2);
  const p=el('path',{d:d,class:cls});
  p.style.strokeDasharray='300 300';
  p.animate([{strokeDashoffset:300},{strokeDashoffset:-300}],
    {duration:dur,iterations:Infinity,easing:'linear',delay:delay});
  svg.appendChild(p);
});

const sg=el('g',{id:'bpSweepG'});
sg.appendChild(el('rect',{x:0,y:0,width:23,height:100,class:'sweepBand'}));
sg.appendChild(el('line',{x1:23,y1:0,x2:23,y2:100,class:'sweepEdge'}));
[21,45,64,84].forEach(function(y){
  sg.appendChild(el('line',{x1:21.9,y1:y,x2:24.1,y2:y,class:'sweepTick'}));
});
svg.appendChild(sg);

const wrap=document.getElementById('wrap'),plane=document.getElementById('plane'),net=document.getElementById('net'),
      s1=document.getElementById('s1'),s2=document.getElementById('s2'),s3=document.getElementById('s3'),
      par=document.getElementById('par'),hudTxt=document.getElementById('hudTxt'),hudBar=document.getElementById('hudBar'),
      chs=[...document.querySelectorAll('.ch')];

/* headline word reveal on load */
function revealHead(){[...document.querySelectorAll('#h1 .w')].forEach((w,i)=>
  setTimeout(()=>w.classList.add('in'), 120+i*95));}
if(document.readyState==='complete'||document.readyState==='interactive') requestAnimationFrame(revealHead);
else addEventListener('DOMContentLoaded',revealHead);
/* safety net: never leave the headline hidden */
setTimeout(()=>document.querySelectorAll('#h1 .w').forEach(w=>w.classList.add('in')), 1800);

/* inertia-smoothed scroll */
let target=0, cur=0, running=false;
const setScene=(el,o,dy,bl)=>{el.style.opacity=o.toFixed(3);
  el.style.transform='translate3d(0,'+dy.toFixed(1)+'px,0)';
  el.style.filter=bl>0.02?'blur('+bl.toFixed(2)+'px)':'none';
  el.style.visibility=o<.02?'hidden':'visible'};

let mx=0,my=0,tmx=0,tmy=0;
addEventListener('mousemove',e=>{tmx=(e.clientX/innerWidth-.5);tmy=(e.clientY/innerHeight-.5)},{passive:true});

function frame(){
  cur += (target-cur)*0.085;
  mx  += (tmx-mx)*0.06;  my += (tmy-my)*0.06;
  const p=cur;

  /* the frame stays put and clips; the picture inside is what moves */
  const kb = plane.firstElementChild;
  if (kb) kb.style.transform =
    'scale(' + (1.10 - .08 * p).toFixed(4) + ') ' +
    'translate3d(' + (mx * -16).toFixed(1) + 'px,' + ((1.5 - 2.5 * p) + my * -6).toFixed(2) + '%,0)';
  net.style.transform='translate3d('+(mx*-26).toFixed(1)+'px,'+((.5-p)*-7).toFixed(2)+'%,0)';

  const o1=1-sm(rmp(p,.16,.32)); setScene(s1,o1,-72*(1-o1),(1-o1)*5);
  const o2=win(p,.28,.72);       setScene(s2,o2,(1-o2)*46,(1-o2)*5);
  const o3=sm(rmp(p,.66,.84));   setScene(s3,o3,(1-o3)*46,(1-o3)*5);
  par.classList.toggle('on',o2>.35);
  document.getElementById('liveCard').classList.toggle('on',o2>.30);

  MK.forEach((m,i)=>{const o=win(p,m.f,m.t,.06);
    m.n.style.opacity=o.toFixed(3);
    m.n.style.transform='translate(-50%,-50%) scale('+(.8+.2*o).toFixed(3)+')';});

  const act=p<.3?0:(p<.7?1:2);
  chs.forEach((c,i)=>c.classList.toggle('on',i===act));
  hudBar.style.transform='scaleX('+p.toFixed(3)+')';
  hudTxt.textContent=(p<.02?'SCROLL':'CHAPTER '+(act+1)+' OF 3')+' · '+String(Math.round(p*100)).padStart(2,'0')+'%';

  if(Math.abs(target-cur)>0.0004||Math.abs(tmx-mx)>0.001){requestAnimationFrame(frame)}else{running=false}
}
function onScroll(){
  const total=wrap.offsetHeight-innerHeight; if(total<=0)return;
  target=c01((scrollY-wrap.offsetTop)/total);
  if(!running){running=true;requestAnimationFrame(frame)}
}

/* ── live ambient air data for Riyadh (public source, client-side) ── */
(function(){
  const card=document.getElementById('liveCard');
  const spark=(el,vals,col)=>{
    if(!vals.length) return;
    const mn=Math.min(...vals), mx=Math.max(...vals), rg=(mx-mn)||1;
    const pts=vals.map((v,i)=>[i*(120/(vals.length-1)), 30-((v-mn)/rg)*24+2]);
    const d=pts.map((p,i)=>(i?'L':'M')+p[0].toFixed(1)+' '+p[1].toFixed(1)).join(' ');
    el.innerHTML='<path class="fill" d="'+d+' L120 34 L0 34 Z" fill="'+col+'"/><path d="'+d+'" stroke="'+col+'"/>';
  };
  const url='https://air-quality-api.open-meteo.com/v1/air-quality'
    +'?latitude=24.7136&longitude=46.6753&current=pm10,pm2_5,us_aqi&hourly=pm2_5,pm10&past_days=1&forecast_days=1';
  fetch(url).then(r=>r.json()).then(d=>{
    const c=d.current||{};
    const aqi=Math.round(c.us_aqi||0);
    /* the US EPA index is defined to 500; anything above is shown as 500+ */
    document.getElementById('aqiVal').textContent = aqi ? (aqi>500 ? '500+' : aqi) : '—';
    const band = aqi<=50?'GOOD' : aqi<=100?'MODERATE' : aqi<=150?'UNHEALTHY · SENSITIVE'
               : aqi<=200?'UNHEALTHY' : aqi<=300?'VERY UNHEALTHY' : 'HAZARDOUS';
    const lab=document.querySelector('.lc-val span');
    if(lab && aqi) lab.textContent = 'AQI · ' + band;
    document.getElementById('pm25').textContent=(c.pm2_5!=null)?c.pm2_5.toFixed(1):'—';
    document.getElementById('pm10').textContent=(c.pm10!=null)?c.pm10.toFixed(1):'—';
    const frac=Math.min(1,aqi/500);
    document.getElementById('aqiArc').style.strokeDashoffset=(255*(1-frac)).toFixed(1);
    const h=d.hourly||{};
    const take=a=>(a||[]).filter(v=>v!=null).slice(-24);
    spark(document.getElementById('sp25'),take(h.pm2_5),'#8fe7f7');
    spark(document.getElementById('sp10'),take(h.pm10),'#c3d49a');
    const t=c.time? new Date(c.time):new Date();
    document.getElementById('lcSrc').textContent='AMBIENT AIR · RIYADH · PUBLIC DATA · '
      + t.toISOString().slice(11,16) + ' UTC';
  }).catch(()=>{ card.style.display='none'; });  /* never show placeholder numbers */
})();

/* ── cover rotation: three images, 6s each, cross-faded ── */
(function(){
  const imgs=[...document.querySelectorAll('.cvr')];
  if(imgs.length<2) return;
  if(matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  let i=0, timer=null;
  const load=n=>{ const el=imgs[n]; if(el && el.dataset.src){ el.src=el.dataset.src; delete el.dataset.src; } };
  load(1);                      /* have the next frame ready before the first change */

  /* cover-3 carries its own labelled pins, so ours step aside while it shows */
  const ANNOTATED = 2;
  const net = document.getElementById('net'), mkL = document.getElementById('mkLayer');
  const syncOverlay = n => {
    const hide = (n === ANNOTATED);
    [net, mkL].forEach(el => { if (!el) return;
      el.style.transition = 'opacity .9s ease';
      el.style.opacity = hide ? '0' : '1'; });
  };
  syncOverlay(0);

  const tick=()=>{ imgs[i].classList.remove('on');
    i=(i+1)%imgs.length; imgs[i].classList.add('on'); syncOverlay(i);
    load((i+1)%imgs.length); }; /* always keep one frame ahead loaded */
  const start=()=>{ if(!timer) timer=setInterval(tick,6000); };
  const stop =()=>{ clearInterval(timer); timer=null; };
  document.addEventListener('visibilitychange',()=>document.hidden?stop():start());
  start();
})();

addEventListener('scroll',onScroll,{passive:true});
addEventListener('resize',onScroll);
onScroll(); cur=target; frame();

})();
