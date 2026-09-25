(function(){
  var lb=document.getElementById('eqpLb'); if(!lb) return;
  var btns=[].slice.call(document.querySelectorAll('.eqp-ph[data-full]')), cur=0, last=null;
  var $=function(id){return document.getElementById(id);};
  var of=document.documentElement.lang==='ar'?' من ':' of ';
  function show(i){ cur=(i+btns.length)%btns.length; var b=btns[cur], row=b.closest('.eqp-row'), sec=b.closest('.eqp-sec');
    $('eqpLbImg').src=b.dataset.full; $('eqpLbImg').alt=b.querySelector('img').alt;
    $('eqpLbCat').textContent=sec.querySelector('h2').textContent;
    $('eqpLbName').textContent=row.querySelector('.eqp-name').textContent;
    $('eqpLbWhy').textContent=row.querySelector('.eqp-note').textContent;
    var dl=$('eqpLbSpec'); dl.innerHTML='';
    var d=document.createElement('div'), dt=document.createElement('dt'), dd=document.createElement('dd');
    dt.textContent=$('eqpLbMeasLbl').textContent; dd.textContent=row.querySelector('.eqp-meas').textContent;
    d.appendChild(dt); d.appendChild(dd); dl.appendChild(d);
    var spec=row.querySelector('.eqp-spec'); if(spec) [].forEach.call(spec.children,function(c){ dl.appendChild(c.cloneNode(true)); });
    $('eqpLbCount').textContent=(cur+1)+of+btns.length; }
  function open(i){ last=document.activeElement; show(i); lb.hidden=false; document.body.style.overflow='hidden'; lb.querySelector('.eqp-lb-x').focus(); }
  function close(){ lb.hidden=true; document.body.style.overflow=''; if(last) last.focus(); }
  var rtl=document.documentElement.dir==='rtl';
  btns.forEach(function(b,i){ b.addEventListener('click',function(){ open(i); }); });
  lb.querySelector('.eqp-lb-x').addEventListener('click',close);
  lb.querySelector('.eqp-lb-prev').addEventListener('click',function(){ show(cur-1); });
  lb.querySelector('.eqp-lb-next').addEventListener('click',function(){ show(cur+1); });
  lb.addEventListener('click',function(e){ if(e.target===lb) close(); });
  document.addEventListener('keydown',function(e){ if(lb.hidden) return;
    if(e.key==='Escape') close();
    if(e.key==='ArrowRight') show(cur+(rtl?-1:1));
    if(e.key==='ArrowLeft') show(cur+(rtl?1:-1)); });
})();
