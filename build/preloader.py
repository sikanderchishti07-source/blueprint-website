# Site preloader, "Horizon" (modernised Oct 2026: blueprint grid, blur-in logo,
# shine across the name, softer exit).
#
# A thin brand-coloured horizon line grows across the screen (it is the
# progress bar). The BluePrint mark rises from behind it like a sunrise, the
# name slides out beside it, then the screen splits open along the horizon to
# reveal the page. Built from the real logo files, so it is sharp at any size.
#
# Rules it keeps:
#   - once per browser session (first page only), never on later clicks
#   - the page loads underneath; it lifts as soon as the page is ready (after
#     the logo has fully formed) and never waits more than 6.5 seconds
#   - the logo files download only when the preloader actually shows
#   - "reduce motion" visitors see the finished logo, which then fades out
#
# Timing: about 3 seconds in total (between the original ~4 s and the fast ~2.5 s).
# To switch it off: set ENABLED = False and rebuild.

ENABLED = True
LOGO = "/assets/logo/"
TAG = {"en": "Environmental Services", "ar": "للخدمات البيئية"}

_HEAD = """
<script>try{if(sessionStorage.getItem('bpPre'))document.documentElement.className+=' bp-pre-seen'}catch(e){}</script>
<style>
html.bp-pre-on{overflow:hidden}
.bp-pre-seen #bpPre{display:none}
#bpPre{--hz:56%;--navy:#102f50;--teal:#078f88;position:fixed;inset:0;z-index:2147483000;overflow:hidden;direction:ltr}
#bpPre .bpp-sky,#bpPre .bpp-sand{position:absolute;left:0;right:0;transition:transform .9s cubic-bezier(.76,0,.24,1),opacity .58s ease}
#bpPre .bpp-sky{top:0;height:var(--hz);background:linear-gradient(180deg,#eef5f8 0%,#fbfdfe 100%);overflow:hidden}
#bpPre .bpp-sky::before{content:"";position:absolute;inset:0;
  background-image:linear-gradient(rgba(16,47,80,.07) 1px,transparent 1px),linear-gradient(90deg,rgba(16,47,80,.07) 1px,transparent 1px);
  background-size:44px 44px;background-position:center bottom;
  -webkit-mask-image:linear-gradient(to top,#000 0%,transparent 75%);mask-image:linear-gradient(to top,#000 0%,transparent 75%);opacity:0;transition:opacity .9s ease}
#bpPre .bpp-sand{top:var(--hz);bottom:0;background:linear-gradient(180deg,#f6f1e7 0%,#ede4d4 100%)}
#bpPre .bpp-sun{position:absolute;left:50%;top:var(--hz);width:64vmin;height:64vmin;transform:translate(-50%,-50%) scale(.85);border-radius:50%;
  background:radial-gradient(closest-side,rgba(255,221,160,.55),rgba(7,143,136,.10) 62%,rgba(7,143,136,0));opacity:0;transition:opacity .7s,transform 2.4s ease-out}
#bpPre .bpp-line{position:absolute;left:10%;right:10%;top:var(--hz);height:2px;margin-top:-1px;transform:scaleX(0);overflow:hidden;
  background:linear-gradient(90deg,transparent,var(--navy) 16%,var(--teal) 50%,var(--navy) 84%,transparent);
  box-shadow:0 0 14px rgba(7,143,136,.45);transition:opacity .4s}
#bpPre .bpp-line::after{content:"";position:absolute;top:0;bottom:0;width:22%;left:-22%;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.95),transparent);animation:bppShim 1.6s ease-in-out infinite}
#bpPre .bpp-lock{position:absolute;left:0;right:0;bottom:calc(100% - var(--hz));display:flex;justify-content:center;align-items:flex-end;
  padding-bottom:clamp(10px,1.6vmin,16px);transition:opacity .55s,transform .85s cubic-bezier(.76,0,.24,1),filter .55s}
#bpPre .bpp-rise{overflow:hidden;height:clamp(96px,18vmin,172px);display:flex;align-items:flex-end}
#bpPre .bpp-mark{position:relative;height:100%;aspect-ratio:649/675;transform:translateY(105%);filter:blur(6px)}
#bpPre .bpp-mark img{position:absolute;inset:0;width:100%;height:100%;max-width:none}
#bpPre .bpp-w{transform-origin:22% 88%;transform:rotate(-30deg) scale(.7);opacity:0}
#bpPre .bpp-wordwrap{position:relative;max-width:0;overflow:hidden;display:flex;align-items:flex-end}
#bpPre .bpp-word{height:clamp(22px,4vmin,40px);width:auto;max-width:none;margin-left:clamp(12px,2vmin,20px);margin-bottom:clamp(37px,7vmin,67px);
  opacity:0;transform:translateX(-18px);filter:blur(8px)}
#bpPre .bpp-shine{position:absolute;top:0;bottom:0;left:0;width:40%;pointer-events:none;transform:translateX(-120%);
  background:linear-gradient(105deg,transparent 20%,rgba(255,255,255,.9) 50%,transparent 80%)}
#bpPre .bpp-tag{position:absolute;left:0;right:0;top:calc(var(--hz) + clamp(18px,2.8vmin,28px));text-align:center;margin:0;
  font:700 clamp(10px,1.5vmin,13px)/1.2 "Segoe UI",system-ui,-apple-system,sans-serif;letter-spacing:.42em;text-transform:uppercase;color:var(--teal);opacity:0;transition:opacity .5s}
#bpPre .bpp-tag.bpp-ar{letter-spacing:0 !important;text-transform:none;font-size:clamp(14px,2vmin,17px);font-family:"IBM Plex Sans Arabic","Segoe UI",sans-serif}
#bpPre.bpp-play .bpp-sky::before{opacity:1}
#bpPre.bpp-play .bpp-sun{opacity:1;transform:translate(-50%,-50%) scale(1)}
#bpPre.bpp-play .bpp-mark{animation:bppRise .8s cubic-bezier(.2,.8,.2,1) .25s forwards}
#bpPre.bpp-play .bpp-w{animation:bppLeaf .75s cubic-bezier(.34,1.56,.64,1) .62s forwards}
#bpPre.bpp-play .bpp-wordwrap{animation:bppOpen .7s cubic-bezier(.65,0,.2,1) .98s forwards}
#bpPre.bpp-play .bpp-word{animation:bppWord .6s cubic-bezier(.2,.8,.2,1) 1.12s forwards}
#bpPre.bpp-play .bpp-shine{animation:bppShine .9s ease-in-out 1.7s forwards}
#bpPre.bpp-play .bpp-tag{animation:bppTag .7s ease-out 1.4s forwards}
#bpPre.bpp-out{pointer-events:none}
#bpPre.bpp-out .bpp-sky{transform:translateY(-100%)}
#bpPre.bpp-out .bpp-sand{transform:translateY(100%)}
#bpPre.bpp-out .bpp-lock{opacity:0;transform:translateY(-34px) scale(.96);filter:blur(4px)}
#bpPre.bpp-out .bpp-tag,#bpPre.bpp-out .bpp-line,#bpPre.bpp-out .bpp-sun{opacity:0}
@keyframes bppRise{to{transform:translateY(0);filter:none}}
@keyframes bppLeaf{to{transform:none;opacity:1}}
@keyframes bppOpen{to{max-width:560px}}
@keyframes bppWord{to{opacity:1;transform:none;filter:none}}
@keyframes bppShine{to{transform:translateX(320%)}}
@keyframes bppShim{to{left:100%}}
@keyframes bppTag{from{opacity:0;letter-spacing:.9em;filter:blur(4px)}to{opacity:1;letter-spacing:.42em;filter:none}}
@media (prefers-reduced-motion:reduce){
  #bpPre .bpp-mark,#bpPre .bpp-w,#bpPre .bpp-word{transform:none;opacity:1;filter:none}
  #bpPre .bpp-wordwrap{max-width:560px}#bpPre .bpp-tag,#bpPre .bpp-sun{opacity:1}#bpPre .bpp-line{transform:scaleX(1)}
  #bpPre .bpp-line::after,#bpPre .bpp-shine{display:none}
  #bpPre.bpp-play *{animation:none !important}
  #bpPre.bpp-out .bpp-sky,#bpPre.bpp-out .bpp-sand{transform:none;opacity:0}}
</style>
"""

_BODY = """
<div id="bpPre" aria-hidden="true">
  <div class="bpp-sky"></div><div class="bpp-sand"></div><div class="bpp-sun"></div>
  <div class="bpp-lock"><div class="bpp-rise"><div class="bpp-mark">
    <img class="bpp-b" data-src="__L__blueprint-b.png" alt=""><img class="bpp-w" data-src="__L__blueprint-wave.png" alt="">
  </div></div><div class="bpp-wordwrap"><img class="bpp-word" data-src="__L__blueprint-wordmark.png" alt=""><span class="bpp-shine"></span></div></div>
  <div class="bpp-line"></div>
  <p class="bpp-tag__ARCLS__">__TAG__</p>
</div>
<script>
(function(){
  var d=document.documentElement,p=document.getElementById('bpPre');if(!p)return;
  try{if(sessionStorage.getItem('bpPre')){p.parentNode.removeChild(p);return}sessionStorage.setItem('bpPre','1')}catch(e){}
  d.classList.add('bp-pre-on');
  var line=p.querySelector('.bpp-line'),imgs=p.querySelectorAll('img[data-src]'),t0=Date.now(),started=0,done=false,loaded=false,
      reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches,FORM=reduce?250:1900,MAX=5000,left=imgs.length;
  function start(){if(started)return;started=Date.now();p.classList.add('bpp-play');maybe()}
  for(var i=0;i<imgs.length;i++){imgs[i].onload=imgs[i].onerror=function(){if(--left<=0)start()};imgs[i].src=imgs[i].getAttribute('data-src')}
  setTimeout(start,700);
  (function tick(){if(done)return;var e=Date.now()-t0;
    var k=Math.min(.88,1-Math.exp(-e/675));if(!reduce)line.style.transform='scaleX('+k+')';requestAnimationFrame(tick)})();
  function finish(){if(done)return;done=true;
    line.style.transition='transform .35s ease-out, opacity .35s';line.style.transform='scaleX(1)';
    setTimeout(function(){p.classList.add('bpp-out');d.classList.remove('bp-pre-on');
      setTimeout(function(){if(p.parentNode)p.parentNode.removeChild(p)},1000)},reduce?0:380)}
  function maybe(){if(loaded&&started)setTimeout(finish,Math.max(0,FORM-(Date.now()-started)))}
  function ready(){loaded=true;maybe()}
  if(document.readyState!=='loading')ready();else document.addEventListener('DOMContentLoaded',ready);  /* photos keep loading behind the split */
  setTimeout(finish,MAX);
})();
</script>
"""


def body(lang="en"):
    if not ENABLED:
        return ""
    ar = lang == "ar"
    return (_BODY.replace("__L__", LOGO).replace("__TAG__", TAG["ar" if ar else "en"])
            .replace("__ARCLS__", " bpp-ar" if ar else ""))


HEAD = _HEAD if ENABLED else ""
BODY = body("en")          # kept so older templates still build
