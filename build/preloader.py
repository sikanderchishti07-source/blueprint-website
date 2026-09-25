# Site preloader, built on the client's own artwork (assets/img/preloader.webp).
#
# The artwork already carries the logo, tagline, bar and icons. On top of it:
#   - the progress bar fills for real as the page loads
#   - a soft light sweep crosses the logo, and a gentle glow breathes behind it
#   - the scene slowly zooms, then everything fades into the page
#
# Rules it keeps:
#   - shows once per browser session (first page only), never on later clicks
#   - the page loads underneath the whole time; it lifts as soon as the page is
#     ready (after a short minimum so the animation reads) and never waits more
#     than 6 seconds
#   - visitors with "reduce motion" switched on get no zoom, sweep or glow
#   - the artwork is a CSS background, so it is not downloaded on later pages
#
# To switch it off: set ENABLED = False and rebuild.

ENABLED = True
IMG = "/assets/img/preloader.webp"
RATIO = 1672 / 941                  # artwork proportions
# the progress bar drawn in the artwork, as % of the artwork
BAR = dict(left=39.72, top=60.55, width=20.49, height=1.40)

_CSS = """
<script>try{if(sessionStorage.getItem('bpPre'))document.documentElement.className+=' bp-pre-seen'}catch(e){}</script>
<style>
html.bp-pre-on{overflow:hidden}
.bp-pre-seen #bpPre{display:none}
#bpPre{position:fixed;inset:0;z-index:2147483000;overflow:hidden;direction:ltr;
  background:linear-gradient(180deg,rgb(61,128,173) 0%,rgb(160,200,225) 45%,rgb(57,93,81) 100%);
  transition:opacity .75s ease,transform .9s cubic-bezier(.2,.7,.2,1)}
#bpPre.bpp-out{opacity:0;transform:scale(1.035);pointer-events:none}
.bpp-stage{position:absolute;left:50%;top:50%;
  width:min(100vw,calc(100vh * __R__));height:min(100vh,calc(100vw / __R__));
  -webkit-mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent),linear-gradient(180deg,transparent,#000 5%,#000 95%,transparent);
  -webkit-mask-composite:source-in;mask-image:linear-gradient(90deg,transparent,#000 6%,#000 94%,transparent),linear-gradient(180deg,transparent,#000 5%,#000 95%,transparent);
  mask-composite:intersect;
  transform:translate(-50%,-50%);background:url(__IMG__) center/100% 100% no-repeat;
  animation:bppZoom 7s cubic-bezier(.2,.6,.2,1) forwards}
@media (max-aspect-ratio:1/1){.bpp-stage{width:calc(100vw * 3.215);height:calc(100vw * 3.215 / __R__);-webkit-mask-image:none;mask-image:none}}
#bpPre::before{content:"";position:absolute;inset:-40px;background:url(__IMG__) center/cover no-repeat;
  filter:blur(28px) saturate(1.1);opacity:.9}
.bpp-bar{position:absolute;left:__BL__%;top:__BT__%;width:__BW__%;height:__BH__%;
  border-radius:999px;background:rgb(221,219,218);overflow:hidden}
.bpp-fill{position:absolute;inset:0;border-radius:inherit;transform:scaleX(.02);transform-origin:left center;
  background:linear-gradient(90deg,#046ce4 0%,#2ca8bf 55%,#78bc3d 100%)}
.bpp-fill::after{content:"";position:absolute;inset:0;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.65),transparent);
  transform:translateX(-100%);animation:bppShine 1.3s ease-in-out infinite}
.bpp-glow{position:absolute;left:34.5%;top:6%;width:30%;height:50%;border-radius:50%;
  background:radial-gradient(closest-side,rgba(255,255,255,.55),rgba(255,255,255,0));
  mix-blend-mode:screen;opacity:0;animation:bppGlow 2.8s ease-in-out .2s infinite alternate}
.bpp-sweep{position:absolute;left:36%;top:17%;width:28%;height:32%;overflow:hidden;mix-blend-mode:screen;
  -webkit-mask-image:radial-gradient(closest-side,#000 55%,transparent);mask-image:radial-gradient(closest-side,#000 55%,transparent)}
.bpp-sweep::before{content:"";position:absolute;top:-20%;bottom:-20%;width:35%;left:-40%;
  background:linear-gradient(100deg,transparent,rgba(255,255,255,.55),transparent);
  animation:bppSweep 2.6s ease-in-out .5s infinite}
@keyframes bppZoom{from{transform:translate(-50%,-50%) scale(1.025)}to{transform:translate(-50%,-50%) scale(1)}}
@keyframes bppShine{to{transform:translateX(100%)}}
@keyframes bppGlow{to{opacity:.8}}
@keyframes bppSweep{0%{left:-40%}60%,100%{left:110%}}
@media (prefers-reduced-motion:reduce){.bpp-stage,.bpp-glow,.bpp-sweep::before,.bpp-fill::after{animation:none}
  .bpp-stage{transform:translate(-50%,-50%)}}
</style>
"""
_CSS = (_CSS.replace("__R__", "%.5f" % RATIO).replace("__IMG__", IMG)
        .replace("__BL__", str(BAR["left"])).replace("__BT__", str(BAR["top"]))
        .replace("__BW__", str(BAR["width"])).replace("__BH__", str(BAR["height"])))

_BODY = """
<div id="bpPre" aria-hidden="true">
  <div class="bpp-stage">
    <div class="bpp-glow"></div>
    <div class="bpp-sweep"></div>
    <div class="bpp-bar"><div class="bpp-fill"></div></div>
  </div>
</div>
<script>
(function(){
  var d=document.documentElement,p=document.getElementById('bpPre');
  if(!p)return;
  try{if(sessionStorage.getItem('bpPre')){p.parentNode.removeChild(p);return}
      sessionStorage.setItem('bpPre','1')}catch(e){}
  d.classList.add('bp-pre-on');
  var fill=p.querySelector('.bpp-fill'),t0=Date.now(),done=false,MIN=1900,MAX=6000,
      reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches;
  function tick(){if(done)return;var e=Date.now()-t0;
    fill.style.transform='scaleX('+Math.max(.02,Math.min(.9,1-Math.exp(-e/950)))+')';
    requestAnimationFrame(tick)}
  function finish(){if(done)return;done=true;
    fill.style.transition='transform .45s ease-out';fill.style.transform='scaleX(1)';
    setTimeout(function(){p.classList.add('bpp-out');d.classList.remove('bp-pre-on');
      setTimeout(function(){if(p.parentNode)p.parentNode.removeChild(p)},900)},480)}
  function ready(){setTimeout(finish,reduce?0:Math.max(0,MIN-(Date.now()-t0)))}
  requestAnimationFrame(tick);
  if(document.readyState==='complete')ready();else window.addEventListener('load',ready);
  setTimeout(finish,MAX);
})();
</script>
"""

HEAD = _CSS if ENABLED else ""
BODY = _BODY if ENABLED else ""
