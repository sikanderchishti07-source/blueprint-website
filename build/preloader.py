# Site preloader, "Horizon".
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
# To switch it off: set ENABLED = False and rebuild.

ENABLED = True
LOGO = "/assets/logo/"
TAG = {"en": "Environmental Services", "ar": "للخدمات البيئية"}

_HEAD = """
<script>try{if(sessionStorage.getItem('bpPre'))document.documentElement.className+=' bp-pre-seen'}catch(e){}</script>
<style>
html.bp-pre-on{overflow:hidden}
.bp-pre-seen #bpPre{display:none}
#bpPre{--hz:56%;position:fixed;inset:0;z-index:2147483000;overflow:hidden;direction:ltr}
#bpPre .bpp-sky,#bpPre .bpp-sand{position:absolute;left:0;right:0;transition:transform 1.05s cubic-bezier(.75,0,.2,1),opacity .7s ease}
#bpPre .bpp-sky{top:0;height:var(--hz);background:linear-gradient(180deg,#eef5f9 0%,#f7fbfd 100%)}
#bpPre .bpp-sand{top:var(--hz);bottom:0;background:linear-gradient(180deg,#f5efe3 0%,#ece3d2 100%)}
#bpPre .bpp-sun{position:absolute;left:50%;top:var(--hz);width:60vmin;height:60vmin;transform:translate(-50%,-50%);border-radius:50%;
  background:radial-gradient(closest-side,rgba(255,226,160,.55),rgba(255,226,160,0));opacity:0;transition:opacity .6s}
#bpPre .bpp-line{position:absolute;left:10%;right:10%;top:var(--hz);height:2px;margin-top:-1px;transform:scaleX(0);
  background:linear-gradient(90deg,transparent,#1640b8 18%,#0e93a8 50%,#6a7a3a 82%,transparent);
  box-shadow:0 0 12px rgba(14,147,168,.45);transition:opacity .4s}
#bpPre .bpp-lock{position:absolute;left:0;right:0;bottom:calc(100% - var(--hz));display:flex;justify-content:center;align-items:flex-end;
  padding-bottom:clamp(10px,1.6vmin,16px);transition:opacity .5s,transform .8s}
#bpPre .bpp-rise{overflow:hidden;height:clamp(96px,18vmin,172px);display:flex;align-items:flex-end}
#bpPre .bpp-mark{position:relative;height:100%;aspect-ratio:201/240;transform:translateY(105%)}
#bpPre .bpp-mark img{position:absolute;inset:0;width:100%;height:100%;max-width:none}
#bpPre .bpp-w{transform-origin:20% 90%;transform:rotate(-14deg);opacity:0}
#bpPre .bpp-wordwrap{max-width:0;overflow:hidden;display:flex;align-items:flex-end}
#bpPre .bpp-word{height:clamp(40px,7.4vmin,72px);width:auto;max-width:none;margin-left:clamp(12px,2vmin,20px);margin-bottom:clamp(14px,2.6vmin,26px);opacity:0;transform:translateX(-24px)}
#bpPre .bpp-tag{position:absolute;left:0;right:0;top:calc(var(--hz) + clamp(16px,2.6vmin,26px));text-align:center;margin:0;
  font:500 clamp(11px,1.6vmin,14px)/1.2 "Segoe UI",system-ui,-apple-system,sans-serif;letter-spacing:.42em;text-transform:uppercase;color:#6a7a3a;opacity:0;transition:opacity .5s}
#bpPre .bpp-tag.bpp-ar{letter-spacing:0 !important;text-transform:none;font-size:clamp(14px,2vmin,17px);font-family:"IBM Plex Sans Arabic","Segoe UI",sans-serif}
#bpPre.bpp-play .bpp-sun{opacity:1}
#bpPre.bpp-play .bpp-mark{animation:bppRise .95s cubic-bezier(.2,.8,.2,1) .35s forwards}
#bpPre.bpp-play .bpp-w{animation:bppLeaf .8s cubic-bezier(.2,.8,.2,1) .8s forwards}
#bpPre.bpp-play .bpp-wordwrap{animation:bppOpen .9s cubic-bezier(.65,0,.2,1) 1.3s forwards}
#bpPre.bpp-play .bpp-word{animation:bppWord .7s ease-out 1.55s forwards}
#bpPre.bpp-play .bpp-tag{animation:bppTag .8s ease-out 1.85s forwards}
#bpPre.bpp-out{pointer-events:none}
#bpPre.bpp-out .bpp-sky{transform:translateY(-100%)}
#bpPre.bpp-out .bpp-sand{transform:translateY(100%)}
#bpPre.bpp-out .bpp-lock{opacity:0;transform:translateY(-30px)}
#bpPre.bpp-out .bpp-tag,#bpPre.bpp-out .bpp-line,#bpPre.bpp-out .bpp-sun{opacity:0}
@keyframes bppRise{to{transform:translateY(0)}}
@keyframes bppLeaf{to{transform:rotate(0);opacity:1}}
@keyframes bppOpen{to{max-width:560px}}
@keyframes bppWord{to{opacity:1;transform:none}}
@keyframes bppTag{from{opacity:0;letter-spacing:.9em}to{opacity:1;letter-spacing:.42em}}
@media (prefers-reduced-motion:reduce){
  #bpPre .bpp-mark,#bpPre .bpp-w,#bpPre .bpp-word{transform:none;opacity:1}
  #bpPre .bpp-wordwrap{max-width:560px}#bpPre .bpp-tag,#bpPre .bpp-sun{opacity:1}#bpPre .bpp-line{transform:scaleX(1)}
  #bpPre.bpp-play *{animation:none !important}
  #bpPre.bpp-out .bpp-sky,#bpPre.bpp-out .bpp-sand{transform:none;opacity:0}}
</style>
"""

_BODY = """
<div id="bpPre" aria-hidden="true">
  <div class="bpp-sky"></div><div class="bpp-sand"></div><div class="bpp-sun"></div>
  <div class="bpp-lock"><div class="bpp-rise"><div class="bpp-mark">
    <img class="bpp-b" data-src="__L__blueprint-b.png" alt=""><img class="bpp-w" data-src="__L__blueprint-wave.png" alt="">
  </div></div><div class="bpp-wordwrap"><img class="bpp-word" data-src="__L__blueprint-wordmark.png" alt=""></div></div>
  <div class="bpp-line"></div>
  <p class="bpp-tag__ARCLS__">__TAG__</p>
</div>
<script>
(function(){
  var d=document.documentElement,p=document.getElementById('bpPre');if(!p)return;
  try{if(sessionStorage.getItem('bpPre')){p.parentNode.removeChild(p);return}sessionStorage.setItem('bpPre','1')}catch(e){}
  d.classList.add('bp-pre-on');
  var line=p.querySelector('.bpp-line'),imgs=p.querySelectorAll('img[data-src]'),t0=Date.now(),started=0,done=false,loaded=false,
      reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches,FORM=reduce?300:2500,MAX=6500,left=imgs.length;
  function start(){if(started)return;started=Date.now();p.classList.add('bpp-play');maybe()}
  for(var i=0;i<imgs.length;i++){imgs[i].onload=imgs[i].onerror=function(){if(--left<=0)start()};imgs[i].src=imgs[i].getAttribute('data-src')}
  setTimeout(start,900);
  (function tick(){if(done)return;var e=Date.now()-t0;
    if(!reduce)line.style.transform='scaleX('+Math.min(.88,1-Math.exp(-e/900))+')';requestAnimationFrame(tick)})();
  function finish(){if(done)return;done=true;
    line.style.transition='transform .45s ease-out, opacity .4s';line.style.transform='scaleX(1)';
    setTimeout(function(){p.classList.add('bpp-out');d.classList.remove('bp-pre-on');
      setTimeout(function(){if(p.parentNode)p.parentNode.removeChild(p)},1200)},reduce?0:500)}
  function maybe(){if(loaded&&started)setTimeout(finish,Math.max(0,FORM-(Date.now()-started)))}
  function ready(){loaded=true;maybe()}
  if(document.readyState==='complete')ready();else window.addEventListener('load',ready);
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
