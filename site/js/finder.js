/* ============================================================
   BluePrint — finder.js
   Compliance Finder: three questions -> the permits, studies and
   monitoring that typically apply. Indicative only; confirmed at scoping.
   Reads the page language from <html lang>. Needs #cfWrap on the page.
   ============================================================ */
(function () {
  var root = document.getElementById('cfWrap');
  if (!root) return;
  var AR = document.documentElement.lang === 'ar';
  var pre = '';  /* Arabic pages link to their Arabic twins */

  var T = AR ? {
    step: 'السؤال {n} من 3', back: 'رجوع', next: 'عرض النتيجة', restart: 'ابدأ من جديد',
    q1: 'في أي مرحلة مشروعك؟',
    q2: 'ما نوع النشاط؟',
    q3: 'ماذا يتضمن موقعك؟', q3h: 'اختر كل ما ينطبق، أو «لا شيء مما سبق».',
    resTitle: 'ما ينطبق على الأرجح على منشأتك',
    resLede: 'بناءً على إجاباتك، هذه التراخيص والدراسات وأعمال الرصد التي تُطلب عادةً. نؤكد القائمة النهائية في مكالمة تحديد النطاق المجانية.',
    must: 'مطلوب عادةً', likely: 'مطلوب غالباً', check: 'يُتحقق منه عند تحديد النطاق',
    more: 'تفاصيل الخدمة', wa: 'أرسل إجاباتي عبر واتساب', book: 'احجز استشارة مجانية',
    note: 'نتيجة استرشادية وليست رأياً تنظيمياً. يحدد التصنيف النهائي الجهةُ المختصة وفق نشاطك وطاقته وموقعه.',
    waHead: 'مرحباً بلوبرنت، استخدمت أداة تحديد المتطلبات:', waStage: 'المرحلة', waAct: 'النشاط', waSite: 'الموقع يتضمن', waRes: 'النتيجة'
  } : {
    step: 'Question {n} of 3', back: 'Back', next: 'Show my result', restart: 'Start again',
    q1: 'Where is your project right now?',
    q2: 'What is the activity?',
    q3: 'What does your site involve?', q3h: 'Pick everything that applies, or "None of these".',
    resTitle: 'What most likely applies to your facility',
    resLede: 'Based on your answers, these are the permits, studies and monitoring normally asked for. We confirm the final list in a free scoping call.',
    must: 'Normally required', likely: 'Often required', check: 'Checked at scoping',
    more: 'Service details', wa: 'Send my answers on WhatsApp', book: 'Book a free consultation',
    note: 'An indicative result, not a regulatory opinion. The authority sets the final classification from your activity, capacity and location.',
    waHead: 'Hello BluePrint, I used the Compliance Finder:', waStage: 'Stage', waAct: 'Activity', waSite: 'Site involves', waRes: 'Result'
  };

  var STAGES = [
    ['new', 'fa-compass-drafting', AR ? 'مشروع جديد أو توسعة' : 'Planning a new facility or expansion', AR ? 'قبل الإنشاء أو قبل زيادة الطاقة' : 'Before construction, or before adding capacity'],
    ['operating', 'fa-industry', AR ? 'منشأة قائمة تعمل حالياً' : 'Already operating', AR ? 'تحتاج إلى الالتزام أو تصحيح الوضع' : 'Need to stay compliant or regularise'],
    ['renewal', 'fa-rotate', AR ? 'تجديد ترخيص قائم' : 'Renewing an existing permit', AR ? 'اقتراب انتهاء الترخيص البيئي' : 'Environmental permit is coming up for renewal']
  ];
  var ACTS = [
    ['heavy', 'fa-oil-well', AR ? 'صناعات ثقيلة وبتروكيماويات' : 'Heavy industry & petrochemicals'],
    ['manufacturing', 'fa-gears', AR ? 'تصنيع وصناعات خفيفة' : 'Manufacturing & light industry'],
    ['quarry', 'fa-mountain', AR ? 'محاجر وتعدين وكسارات' : 'Quarries, mining & crushers'],
    ['waste', 'fa-recycle', AR ? 'جمع النفايات أو معالجتها أو تدويرها' : 'Waste collection, treatment or recycling'],
    ['construction', 'fa-helmet-safety', AR ? 'مشاريع إنشاءات وبنية تحتية' : 'Construction & infrastructure projects'],
    ['health', 'fa-hospital', AR ? 'منشآت صحية ومختبرات' : 'Healthcare & laboratories'],
    ['agri', 'fa-cow', AR ? 'مزارع وثروة حيوانية وأغذية' : 'Farms, livestock & food'],
    ['marine', 'fa-water', AR ? 'أعمال ساحلية أو موانئ أو بحرية' : 'Coastal, port or marine works'],
    ['commercial', 'fa-store', AR ? 'تجارية وخدمية (فنادق، مراكز، ورش)' : 'Commercial & services (hotels, malls, workshops)']
  ];
  var FEATS = [
    ['stacks', 'fa-smog', AR ? 'مداخن أو احتراق (مولدات، غلايات، أفران)' : 'Stacks or combustion (generators, boilers, kilns)'],
    ['water', 'fa-droplet', AR ? 'تصريف مياه صرف أو مياه معالجة' : 'Wastewater or treated effluent discharge'],
    ['haz', 'fa-biohazard', AR ? 'نفايات خطرة أو طبية' : 'Hazardous or medical waste'],
    ['wells', 'fa-arrow-down-up-across-line', AR ? 'آبار مياه جوفية أو أعمال حفر' : 'Groundwater wells or excavation'],
    ['noise', 'fa-volume-high', AR ? 'ضوضاء قرب مساكن أو مستقبِلات حساسة' : 'Noise near homes or sensitive receptors'],
    ['rcjy', 'fa-location-dot', AR ? 'داخل مدينتي الجبيل أو ينبع الصناعيتين' : 'Inside Jubail or Yanbu industrial cities'],
    ['none', 'fa-circle-minus', AR ? 'لا شيء مما سبق' : 'None of these']
  ];

  /* result items: id -> [title, regulator, why, link] */
  var R = AR ? {
    eia: ['دراسة تقييم الأثر البيئي', 'NCEC', 'تحدد فئة المشروع حجم الدراسة، من إقرار بسيط إلى دراسة كاملة ببيانات ميدانية.', 'service-environmental-impact-assessment.html'],
    permitNew: ['الترخيص البيئي للإنشاء ثم للتشغيل', 'NCEC', 'يُطلب قبل البدء بالإنشاء، ثم ترخيص التشغيل قبل بدء النشاط.', 'service-environmental-permit.html'],
    permitOp: ['الترخيص البيئي للتشغيل', 'NCEC', 'المنشأة العاملة دون ترخيص سارٍ تحتاج إلى تصحيح وضعها أولاً.', 'service-environmental-permit.html'],
    renewal: ['تجديد الترخيص البيئي', 'NCEC', 'ابدأ قبل ستة أشهر تقريباً، فبعض القياسات تحتاج وقتاً أو مواسم محددة.', 'service-environmental-permit.html'],
    rcjy: ['موافقة الهيئة الملكية البيئية', 'RCJY', 'داخل الجبيل وينبع تتولى الهيئة الملكية الترخيص البيئي بدلاً من المركز الوطني.', 'service-environmental-permit.html'],
    mwan: ['ترخيص إدارة النفايات', 'MWAN', 'مطلوب لكل من يجمع النفايات أو ينقلها أو يعالجها أو يخزن نفايات خطرة.', 'service-waste-management-permit.html'],
    emp: ['خطة الإدارة البيئية', 'NCEC', 'تحوّل اشتراطات الترخيص إلى ضوابط يومية ومسؤوليات وجدول رصد.', 'service-environmental-management-plan.html'],
    register: ['السجل البيئي', 'NCEC', 'سجل محدث بالانبعاثات والنفايات والحوادث يُطلب عند التفتيش.', 'service-environmental-register.html'],
    periodic: ['التقرير البيئي الدوري', 'NCEC', 'يُقدَّم وفق الجدول المحدد في الترخيص ويُراجع عند التجديد.', 'service-periodic-environmental-report.html'],
    air: ['رصد جودة الهواء والانبعاثات', 'NCEC', 'قياس انبعاثات المداخن وجودة الهواء المحيط وفق الطرق المرجعية.', 'service-air-quality-monitoring.html'],
    model: ['نمذجة التشتت', 'NCEC', 'تُطلب عادةً مع دراسة تقييم الأثر البيئي لمصادر الانبعاث الكبيرة (AERMOD).', 'service-environmental-modelling.html'],
    water: ['فحص المياه ومياه الصرف', 'NCEC / MEWA', 'تحليل التصريف مقابل حدود الترخيص في مختبر معتمد.', 'service-water-wastewater-testing.html'],
    ground: ['دراسة المياه الجوفية والتربة', 'MEWA', 'تُطلب للآبار وأعمال الحفر وحين يوجد احتمال تلوث.', 'service-hydrogeology-geotechnics.html'],
    noise: ['رصد الضوضاء وتقييمها', 'NCEC', 'قياس عند حدود الموقع والمستقبِلات القريبة وفق الفترات المحددة.', 'service-noise-monitoring.html'],
    rehab: ['خطة إعادة التأهيل', 'NCEC', 'تلتزم مواقع الاستخراج بإعادة التأهيل قبل الإغلاق، ويُراجع ذلك مع الترخيص.', 'service-remediation-rehabilitation.html'],
    marine: ['دراسات البيئة البحرية', 'NCEC', 'بيانات المياه والرواسب والموائل التي تحتاجها الأعمال الساحلية.', 'service-marine-environment.html'],
    vet: ['الاستشارات البيطرية والأمن الحيوي', 'MEWA', 'ضوابط الأمن الحيوي والنفايات الحيوانية لمنشآت الثروة الحيوانية.', 'service-veterinary-biosecurity.html'],
    lab: ['التحليل المخبري', 'IAS', 'نتائج من مختبر معتمد تُقبل عند المراجعة.', 'service-laboratory-analysis.html']
  } : {
    eia: ['Environmental impact assessment', 'NCEC', 'The project category sets its size, from a short declaration to a full study with field baseline data.', 'service-environmental-impact-assessment.html'],
    permitNew: ['Environmental permit to construct, then to operate', 'NCEC', 'Needed before construction starts, and an operating permit before the activity begins.', 'service-environmental-permit.html'],
    permitOp: ['Environmental operating permit', 'NCEC', 'A facility running without a valid permit needs to regularise first.', 'service-environmental-permit.html'],
    renewal: ['Environmental permit renewal', 'NCEC', 'Start about six months ahead: some measurements take time or need a particular season.', 'service-environmental-permit.html'],
    rcjy: ['Royal Commission environmental approval', 'RCJY', 'Inside Jubail and Yanbu, the Royal Commission issues environmental approvals instead of NCEC.', 'service-environmental-permit.html'],
    mwan: ['Waste management permit', 'MWAN', 'Needed by anyone who collects, transports, treats or stores hazardous waste.', 'service-waste-management-permit.html'],
    emp: ['Environmental management plan', 'NCEC', 'Turns permit conditions into daily controls, named roles and a monitoring schedule.', 'service-environmental-management-plan.html'],
    register: ['Environmental register', 'NCEC', 'An up-to-date record of emissions, waste and incidents, asked for at inspection.', 'service-environmental-register.html'],
    periodic: ['Periodic environmental report', 'NCEC', 'Submitted on the schedule your permit sets, and reviewed at renewal.', 'service-periodic-environmental-report.html'],
    air: ['Air quality and stack emission monitoring', 'NCEC', 'Stack emissions and ambient air measured to the reference methods.', 'service-air-quality-monitoring.html'],
    model: ['Dispersion modelling', 'NCEC', 'Usually asked for with the impact assessment for significant emission sources (AERMOD).', 'service-environmental-modelling.html'],
    water: ['Water and wastewater testing', 'NCEC / MEWA', 'Discharge analysed against your permit limits in an accredited laboratory.', 'service-water-wastewater-testing.html'],
    ground: ['Groundwater and soil investigation', 'MEWA', 'Needed for wells, excavation, and wherever contamination is possible.', 'service-hydrogeology-geotechnics.html'],
    noise: ['Noise monitoring and assessment', 'NCEC', 'Measured at the boundary and nearby receptors, across the periods the condition names.', 'service-noise-monitoring.html'],
    rehab: ['Rehabilitation plan', 'NCEC', 'Extraction sites commit to rehabilitation before closure, and it is reviewed with the permit.', 'service-remediation-rehabilitation.html'],
    marine: ['Marine environmental studies', 'NCEC', 'The water, sediment and habitat data coastal works are asked for.', 'service-marine-environment.html'],
    vet: ['Veterinary and biosecurity advisory', 'MEWA', 'Biosecurity controls and animal waste handling for livestock operations.', 'service-veterinary-biosecurity.html'],
    lab: ['Laboratory analysis', 'IAS', 'Results from an accredited laboratory that hold up at review.', 'service-laboratory-analysis.html']
  };

  function compute(stage, act, feats) {
    var out = [], seen = {};
    function add(id, level) { if (seen[id]) return; seen[id] = 1; out.push([id, level]); }
    var f = function (k) { return feats.indexOf(k) > -1; };
    var industrial = ['heavy', 'manufacturing', 'quarry', 'waste', 'marine'].indexOf(act) > -1;

    if (f('rcjy')) add('rcjy', 'must');
    if (stage === 'new') {
      add('eia', 'must'); if (!f('rcjy')) add('permitNew', 'must');
      if (industrial || act === 'construction') add('emp', 'likely');
    } else if (stage === 'operating') {
      if (!f('rcjy')) add('permitOp', 'must');
      add('register', 'must'); add('periodic', 'likely');
      if (industrial) add('emp', 'likely');
    } else {
      if (!f('rcjy')) add('renewal', 'must');
      add('periodic', 'must'); add('register', 'likely');
    }
    if (act === 'waste' || f('haz') || act === 'health') add('mwan', 'must');
    if (f('stacks') || act === 'heavy') add('air', stage === 'new' ? 'likely' : 'must');
    if (act === 'quarry') { add('air', 'likely'); add('rehab', 'must'); }
    if (stage === 'new' && (act === 'heavy' || (f('stacks') && industrial))) add('model', 'likely');
    if (f('water')) add('water', 'must');
    if (f('wells')) add('ground', 'likely');
    if (f('noise') || act === 'construction' || act === 'quarry') add('noise', f('noise') ? 'must' : 'likely');
    if (act === 'marine') add('marine', 'must');
    if (act === 'agri') add('vet', 'likely');
    if (f('water') || f('haz') || act === 'health') add('lab', 'check');
    var order = { must: 0, likely: 1, check: 2 };
    return out.sort(function (a, b) { return order[a[1]] - order[b[1]]; });
  }

  var st = { step: 1, stage: null, act: null, feats: [] };
  function esc(s) { var d = document.createElement('div'); d.textContent = s; return d.innerHTML; }
  function opt(list, sel, multi) {
    return '<div class="cf-opts' + (list.length > 4 ? ' cf-opts-grid' : '') + '">' + list.map(function (o) {
      var on = multi ? sel.indexOf(o[0]) > -1 : sel === o[0];
      return '<button type="button" class="cf-opt' + (on ? ' on' : '') + '" data-v="' + o[0] + '" aria-pressed="' + on + '">' +
        '<i class="fas ' + o[1] + '"></i><span><b>' + esc(o[2]) + '</b>' + (o[3] ? '<small>' + esc(o[3]) + '</small>' : '') + '</span>' +
        (multi ? '<em class="cf-tick"><i class="fas fa-check"></i></em>' : '') + '</button>';
    }).join('') + '</div>';
  }
  function label(list, v) { for (var i = 0; i < list.length; i++) if (list[i][0] === v) return list[i][2]; return v; }

  function render() {
    var h = '';
    if (st.step <= 3) {
      h += '<div class="cf-prog"><span>' + T.step.replace('{n}', st.step) + '</span><i><b style="width:' + (st.step * 33.34) + '%"></b></i></div>';
      if (st.step === 1) h += '<h2 class="cf-q">' + T.q1 + '</h2>' + opt(STAGES, st.stage);
      if (st.step === 2) h += '<h2 class="cf-q">' + T.q2 + '</h2>' + opt(ACTS, st.act);
      if (st.step === 3) h += '<h2 class="cf-q">' + T.q3 + '</h2><p class="cf-hint">' + T.q3h + '</p>' + opt(FEATS, st.feats, true);
      h += '<div class="cf-nav">' + (st.step > 1 ? '<button type="button" class="cf-back"><i class="fas fa-arrow-left"></i> ' + T.back + '</button>' : '<span></span>') +
        (st.step === 3 ? '<button type="button" class="cf-go"' + (st.feats.length ? '' : ' disabled') + '>' + T.next + ' <i class="fas fa-arrow-right"></i></button>' : '') + '</div>';
    } else {
      var res = compute(st.stage, st.act, st.feats);
      h += '<p class="cf-sum">' + esc(label(STAGES, st.stage)) + ' &middot; ' + esc(label(ACTS, st.act)) + '</p>';
      h += '<h2 class="cf-q">' + T.resTitle + '</h2><p class="cf-lede">' + T.resLede + '</p><ol class="cf-res">';
      res.forEach(function (r, i) {
        var it = R[r[0]];
        h += '<li class="cf-item cf-' + r[1] + '"><span class="cf-n">' + String(i + 1).padStart(2, '0') + '</span><div>' +
          '<div class="cf-item-top"><b>' + esc(it[0]) + '</b><span class="cf-reg">' + it[1] + '</span><span class="cf-lvl">' + T[r[1]] + '</span></div>' +
          '<p>' + esc(it[2]) + '</p><a href="' + pre + it[3] + '">' + T.more + ' <i class="fas fa-arrow-right"></i></a></div></li>';
      });
      h += '</ol><p class="cf-note"><i class="fas fa-circle-info"></i> ' + T.note + '</p>';
      var C = window.BP_CONFIG || {};
      var msg = [T.waHead, T.waStage + ': ' + label(STAGES, st.stage), T.waAct + ': ' + label(ACTS, st.act),
        T.waSite + ': ' + st.feats.map(function (f) { return label(FEATS, f); }).join(', '),
        T.waRes + ': ' + res.map(function (r) { return R[r[0]][0]; }).join('; ')].join('\n');
      h += '<div class="cf-cta"><a class="cf-go" target="_blank" rel="noopener" href="https://wa.me/' + (C.WHATSAPP || '966543470109') + '?text=' + encodeURIComponent(msg) + '"><i class="fab fa-whatsapp"></i> ' + T.wa + '</a>' +
        '<a class="cf-ghost" href="' + pre + 'contact.html">' + T.book + '</a>' +
        '<button type="button" class="cf-back cf-restart"><i class="fas fa-rotate-left"></i> ' + T.restart + '</button></div>';
    }
    root.innerHTML = h;
    var q = root.querySelector('.cf-q'); if (q && render.moved) q.focus && (q.setAttribute('tabindex', '-1'), q.focus({ preventScroll: true }));
    render.moved = true;
  }

  root.addEventListener('click', function (e) {
    var b = e.target.closest('button'); if (!b) return;
    if (b.classList.contains('cf-restart')) { st = { step: 1, stage: null, act: null, feats: [] }; render(); return; }
    if (b.classList.contains('cf-back')) { st.step--; render(); return; }
    if (b.classList.contains('cf-go')) { st.step = 4; render(); root.scrollIntoView({ behavior: 'smooth', block: 'start' }); return; }
    var v = b.getAttribute('data-v'); if (!v) return;
    if (st.step === 1) { st.stage = v; st.step = 2; }
    else if (st.step === 2) { st.act = v; st.step = 3; }
    else if (st.step === 3) {
      if (v === 'none') st.feats = st.feats.indexOf('none') > -1 ? [] : ['none'];
      else {
        st.feats = st.feats.filter(function (x) { return x !== 'none'; });
        var i = st.feats.indexOf(v); if (i > -1) st.feats.splice(i, 1); else st.feats.push(v);
      }
    }
    render();
  });
  render();
})();
