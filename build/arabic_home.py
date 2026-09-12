# Arabic home page body, mirrors the current English home structure.

BODY = """
<!-- HERO, full-bleed video cover -->
<section class="hero-cover relative flex items-center overflow-hidden">
  <video class="hero-cover-video" autoplay muted loop playsinline preload="metadata"
         poster="assets/video/hero-poster.jpg"
         aria-label="لقطة جوية لساحل البحر الأحمر السعودي">
    <source src="assets/video/hero.mp4" type="video/mp4" />
  </video>
  <div class="hero-cover-scrim" aria-hidden="true"></div>

  <div class="relative z-10 w-full max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-32">
    <div class="max-w-2xl text-white animate-slide-up">
      <div class="inline-flex items-center gap-2 px-4 py-1.5 bg-white/15 rounded-full backdrop-blur-sm border border-white/25 mb-8">
        <span class="w-1.5 h-1.5 bg-green-400 rounded-full animate-pulse"></span>
        <span class="text-xs font-medium tracking-wide">معتمدون لدى المركز الوطني للرقابة على الالتزام البيئي والمركز الوطني لإدارة النفايات &middot; الرياض</span>
      </div>
      <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold leading-[1.15] tracking-tight mb-6">مخططك نحو<br><span class="text-bp-sage">الامتثال البيئي.</span></h1>
      <p class="text-lg text-white/85 max-w-md leading-relaxed mb-10">دراسات وتصاريح وتقارير تُبقي منشأتك ملتزمة في جميع أنحاء المملكة.</p>
      <div class="flex flex-wrap gap-4">
        <a href="contact.html" class="px-8 py-4 bg-white text-bp-ink rounded-full font-bold hover:bg-bp-sage transition-all transform hover:scale-105 shadow-xl">احجز استشارة مجانية</a>
        <a href="services.html" class="px-8 py-4 border border-white/50 text-white rounded-full font-bold backdrop-blur-sm hover:bg-white/15 transition-all flex items-center gap-2">خدماتنا <i class="fas fa-arrow-left" style="font-size:.75rem;"></i></a>
      </div>
    </div>
  </div>

  <div class="hero-cover-fade z-10" aria-hidden="true"></div>
</section>

<!-- من نحن -->
<section id="overview" class="py-20 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="grid lg:grid-cols-2 gap-12 items-center">
      <div class="scroll-reveal">
        <div class="inline-block px-4 py-1.5 bg-bp-light text-bp-primary rounded-full text-sm font-semibold mb-4">من نحن</div>
        <h2 class="text-2xl lg:text-3xl font-bold text-bp-ink mb-4 leading-tight">شركة مبنية على <span class="text-bp-olive">أنظمة المملكة الجديدة</span></h2>
        <p class="text-gray-600 text-sm leading-relaxed mb-3">شركة استشارات بيئية مقرّها الرياض، تأسست استجابةً للطلب المتنامي الذي أوجدته الأنظمة البيئية المتسارعة في المملكة، وتجمع بين الكفاءات السعودية والخبرات الدولية.</p>
        <p class="text-gray-600 text-sm leading-relaxed mb-5">يشمل عملاؤنا الجهات الحكومية والمنشآت الصناعية والتجارية: النفط والغاز، والبتروكيماويات، والتصنيع، والطاقة والتحلية، والأسمنت، والأغذية، والزراعة، والتطوير العمراني.</p>
        <div class="space-y-3 mb-6">
          <div class="flex items-start gap-3">
            <div class="w-5 h-5 rounded-full bg-bp-primary flex-shrink-0 mt-1"></div>
            <div><div class="font-display font-bold text-bp-ink">رسالتنا</div>
            <div class="text-sm text-gray-600">تقديم حلول بيئية مبتكرة بأعلى معايير الجودة والسلامة، تحافظ على امتثال عملائنا الكامل.</div></div>
          </div>
          <div class="flex items-start gap-3">
            <div class="w-5 h-5 rounded-full bg-bp-olive flex-shrink-0 mt-1"></div>
            <div><div class="font-display font-bold text-bp-ink">رؤيتنا</div>
            <div class="text-sm text-gray-600">دعم السياسات البيئية الوطنية والارتقاء بالقطاع البيئي السعودي ليكون مرجعاً إقليمياً في الابتكار الأخضر.</div></div>
          </div>
        </div>
        <div class="flex flex-wrap gap-2">
          <span class="px-4 py-2 bg-bp-light text-bp-primary rounded-lg text-sm font-medium">مرخّص من المركز الوطني</span>
          <span class="px-4 py-2 bg-bp-light text-bp-primary rounded-lg text-sm font-medium">مسجّل لدى المركز الوطني لإدارة النفايات</span>
          <span class="px-4 py-2 bg-bp-light text-bp-primary rounded-lg text-sm font-medium">معتمد من الهيئة الملكية</span>
        </div>
      </div>
      <div class="bg-white rounded-3xl shadow-xl overflow-hidden scroll-reveal">
        <img src="assets/img/about.jpg" alt="ساحل البحر الأحمر السعودي" class="w-full h-52 object-cover" loading="lazy" />
        <div class="p-7">
          <h3 class="text-xl font-bold text-bp-ink mb-5">منسجمون مع رؤية 2030</h3>
          <div class="space-y-2.5">
            <div class="flex items-start gap-3 p-3.5 bg-gray-50 rounded-xl"><span class="font-display font-extrabold text-bp-primary">٠١</span>
              <div><div class="font-bold text-bp-ink text-sm">مجتمع حيوي</div><div class="text-xs text-gray-600">بيئة أنظف وأصحّ ترفع جودة الحياة في أنحاء المملكة.</div></div></div>
            <div class="flex items-start gap-3 p-3.5 bg-gray-50 rounded-xl"><span class="font-display font-extrabold text-bp-primary">٠٢</span>
              <div><div class="font-bold text-bp-ink text-sm">اقتصاد مزدهر</div><div class="text-xs text-gray-600">نمو صناعي مسؤول عبر إدارة ملتزمة للنفايات والبيئة.</div></div></div>
            <div class="flex items-start gap-3 p-3.5 bg-gray-50 rounded-xl"><span class="font-display font-extrabold text-bp-primary">٠٣</span>
              <div><div class="font-bold text-bp-ink text-sm">وطن طموح</div><div class="text-xs text-gray-600">تعزيز ممارسات الاقتصاد الدائري والحوكمة البيئية.</div></div></div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- الخدمات, ثلاث بطاقات -->
<section id="services" class="svc-section" style="background:var(--bp-page);">
  <div class="svc-container mx-auto px-4 sm:px-6 lg:px-8">
    <div class="svc-head text-center scroll-reveal">
      <div class="showcase-eyebrow">ما نقدمه</div>
      <h2 class="svc-h2 font-bold text-bp-ink mb-3 tracking-tight">نتولّى أي التزام بيئي</h2>
      <p class="text-gray-600 text-sm max-w-lg mx-auto leading-relaxed">ثلاثة خطوط خدمة تغطي دورة الامتثال كاملة.</p>
    </div>

    <div class="svc-showcase scroll-reveal">
      <div class="svc-stage" id="svcStage"></div>
      <p class="svc-hint">مرّر فوق البطاقة للمعاينة &middot; اضغط لعرض القائمة كاملة</p>
    </div>
  </div>
</section>

<!-- FULL-SCREEN SERVICE OVERLAY -->
<div class="svc-overlay" id="svcOverlay" role="dialog" aria-modal="true" aria-hidden="true" aria-label="قائمة الخدمات">
  <div class="svc-ov-bg" id="svcOvBg" aria-hidden="true"></div>
  <div class="svc-ov-scrim" aria-hidden="true"></div>
  <button class="svc-ov-close" id="svcOvClose" onclick="closeSvcOverlay()" aria-label="إغلاق">&times;</button>
  <div class="svc-ov-inner">
    <div class="svc-ov-head">
      <div class="svc-ov-kicker" id="svcOvKicker"></div>
      <h2 id="svcOvTitle"></h2>
      <p id="svcOvBlurb"></p>
    </div>
    <div class="svc-ov-grid" id="svcOvGrid"></div>
    <div class="svc-ov-foot">
      <a href="services.html" class="svc-ov-btn" id="svcOvLink">التفاصيل الكاملة <i class="fas fa-arrow-left" style="font-size:.7rem;"></i></a>
      <a href="contact.html" class="svc-ov-btn ghost">تحدّث مع مستشار</a>
    </div>
  </div>
</div>

<!-- ماذا يعني ذلك لك -->
<section class="py-28 bg-white">
  <div class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 space-y-20">

    <div class="grid lg:grid-cols-2 gap-12 items-center scroll-reveal">
      <div>
        <div class="showcase-eyebrow">قبل أن تبني</div>
        <h3 class="text-2xl lg:text-3xl font-bold text-bp-ink mb-4 leading-tight">احصل على الترخيص دون خسارة ربع سنة</h3>
        <p class="text-gray-600 leading-relaxed mb-5">معظم التأخير ليس تقنياً، بل ينشأ من تصنيف خاطئ للنشاط أو ملف تنقصه دراسة داعمة واحدة. نبدأ بالتصنيف الصحيح، ثم نبني الملف حول ما سيطلبه المراجع فعلاً.</p>
        <a href="services.html" class="btn-ghost">التصاريح البيئية <i class="fas fa-arrow-left" style="font-size:.7rem;"></i></a>
      </div>
      <div class="rounded-2xl overflow-hidden shadow-lg"><img src="assets/img/feature-1.jpg" alt="منشأة صناعية ساحلية" class="w-full h-72 object-cover" loading="lazy" /></div>
    </div>

    <div class="grid lg:grid-cols-2 gap-12 items-center scroll-reveal">
      <div class="rounded-2xl overflow-hidden shadow-lg lg:order-1"><img src="assets/img/feature-2.jpg" alt="موقع تحت الرصد البيئي" class="w-full h-72 object-cover" loading="lazy" /></div>
      <div class="lg:order-2">
        <div class="showcase-eyebrow">أثناء التشغيل</div>
        <h3 class="text-2xl lg:text-3xl font-bold text-bp-ink mb-4 leading-tight">لا استعجال قبل أي تفتيش</h3>
        <p class="text-gray-600 leading-relaxed mb-5">المفتّش يطلب السجل البيئي أولاً. نُبقي سجلك محدّثاً، وننفّذ القياسات التي يحددها تصريحك، ونقدّم التقارير الدورية في موعدها, فيتحوّل التفتيش إلى مراجعة مستندات لا إلى أزمة.</p>
        <a href="technology.html" class="btn-ghost">الرصد والتقارير <i class="fas fa-arrow-left" style="font-size:.7rem;"></i></a>
      </div>
    </div>

    <div class="grid lg:grid-cols-2 gap-12 items-center scroll-reveal">
      <div>
        <div class="showcase-eyebrow">عند التجديد</div>
        <h3 class="text-2xl lg:text-3xl font-bold text-bp-ink mb-4 leading-tight">التجديد يُحسم قبل تقديمه بوقت طويل</h3>
        <p class="text-gray-600 leading-relaxed mb-5">مراجعة التجديد تفحص مدة التصريح كاملة لا الطلب وحده. من يلتزم بالتقارير الدورية يجدّد من سجل حُفظ طوال المدة، لا من سجل جُمّع, ودُقّق, في اللحظة الأخيرة.</p>
        <a href="blog.html" class="btn-ghost">اقرأ دليل التجديد <i class="fas fa-arrow-left" style="font-size:.7rem;"></i></a>
      </div>
      <div class="rounded-2xl overflow-hidden shadow-lg"><img src="assets/img/feature-3.jpg" alt="ساحل ونباتات محمية" class="w-full h-72 object-cover" loading="lazy" /></div>
    </div>

  </div>
</section>

<!-- منهجية العمل -->
<section class="py-28 text-white relative overflow-hidden" style="background:var(--bp-grad);">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
    <div class="text-center mb-16 scroll-reveal">
      <div class="showcase-eyebrow" style="color:var(--bp-sage);">كيف نعمل</div>
      <h2 class="text-4xl lg:text-5xl font-bold mb-5 tracking-tight">امتثال بلا تخمين</h2>
      <p class="text-gray-300 text-base max-w-xl mx-auto leading-relaxed">أربع مراحل واضحة من أول مكالمة حتى التصريح الصادر.</p>
    </div>
    <div class="grid md:grid-cols-4 gap-6">
      <div class="p-7 rounded-2xl scroll-reveal" style="background:rgba(255,255,255.06);border:1px solid rgba(255,255,255.12);">
        <div class="font-display text-2xl font-extrabold mb-3" style="color:var(--bp-soft);">٠١</div>
        <h3 class="font-display font-bold mb-2">التقييم</h3>
        <p class="text-sm text-white/70 leading-relaxed">نقرأ نشاطك وموقعك وطاقتك الإنتاجية، ونحدد التصنيف الصحيح قبل أي عرض سعر.</p>
      </div>
      <div class="p-7 rounded-2xl scroll-reveal" style="background:rgba(255,255,255.06);border:1px solid rgba(255,255,255.12);">
        <div class="font-display text-2xl font-extrabold mb-3" style="color:var(--bp-soft);">٠٢</div>
        <h3 class="font-display font-bold mb-2">الدراسات</h3>
        <p class="text-sm text-white/70 leading-relaxed">ننفّذ ما تتطلبه الفئة من دراسات وقياسات ميدانية، لا أكثر ولا أقل.</p>
      </div>
      <div class="p-7 rounded-2xl scroll-reveal" style="background:rgba(255,255,255.06);border:1px solid rgba(255,255,255.12);">
        <div class="font-display text-2xl font-extrabold mb-3" style="color:var(--bp-soft);">٠٣</div>
        <h3 class="font-display font-bold mb-2">التقديم</h3>
        <p class="text-sm text-white/70 leading-relaxed">نقدّم الملف ونتابعه، ونردّ على استفسارات المراجع مباشرة.</p>
      </div>
      <div class="p-7 rounded-2xl scroll-reveal" style="background:rgba(255,255,255.06);border:1px solid rgba(255,255,255.12);">
        <div class="font-display text-2xl font-extrabold mb-3" style="color:var(--bp-soft);">٠٤</div>
        <h3 class="font-display font-bold mb-2">الاستمرارية</h3>
        <p class="text-sm text-white/70 leading-relaxed">نشرح شروط التصريح ونبني منها تقويم الرصد والتقارير الذي يليه.</p>
      </div>
    </div>
  </div>
</section>

<!-- الاعتمادات -->
<section class="py-28 bg-white">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 scroll-reveal">
      <div class="showcase-eyebrow">الاعتمادات</div>
      <h2 class="text-4xl lg:text-5xl font-bold text-bp-ink mb-5 tracking-tight">معتمدون حيث يهمّ الأمر</h2>
      <p class="text-gray-600 text-base max-w-xl mx-auto leading-relaxed">الاعتماد هو ما يجعل نتائجنا مقبولة لدى الجهات التنظيمية.</p>
    </div>
    <div class="grid md:grid-cols-3 gap-6">
      <div class="p-8 rounded-2xl scroll-reveal" style="background:var(--bp-page);">
        <div class="w-12 h-12 rounded-xl flex items-center justify-center mb-5" style="background:var(--bp-grad-blue);"><i class="fas fa-certificate text-white"></i></div>
        <h3 class="font-display text-lg font-bold text-bp-ink mb-2">المركز الوطني للرقابة على الالتزام البيئي</h3>
        <p class="text-sm text-gray-600 leading-relaxed">مرخّصون لإعداد ملفات التصاريح البيئية ودراسات تقييم الأثر وتقديمها.</p>
      </div>
      <div class="p-8 rounded-2xl scroll-reveal" style="background:var(--bp-page);">
        <div class="w-12 h-12 rounded-xl flex items-center justify-center mb-5" style="background:var(--bp-grad-blue);"><i class="fas fa-recycle text-white"></i></div>
        <h3 class="font-display text-lg font-bold text-bp-ink mb-2">المركز الوطني لإدارة النفايات</h3>
        <p class="text-sm text-gray-600 leading-relaxed">مسجّلون لإعداد تصاريح إدارة النفايات للمنتجين والناقلين ومنشآت المعالجة.</p>
      </div>
      <div class="p-8 rounded-2xl scroll-reveal" style="background:var(--bp-page);">
        <div class="w-12 h-12 rounded-xl flex items-center justify-center mb-5" style="background:var(--bp-grad-blue);"><i class="fas fa-industry text-white"></i></div>
        <h3 class="font-display text-lg font-bold text-bp-ink mb-2">الهيئة الملكية</h3>
        <p class="text-sm text-gray-600 leading-relaxed">معتمدون للعمل داخل المدن الصناعية الخاضعة لإشراف الهيئة الملكية.</p>
      </div>
    </div>
  </div>
</section>

<!-- القطاعات -->
<section class="py-28" style="background:var(--bp-page);">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center mb-16 scroll-reveal">
      <div class="showcase-eyebrow">من نخدم</div>
      <h2 class="text-4xl lg:text-5xl font-bold text-bp-ink mb-5 tracking-tight">كل قطاع خاضع للتنظيم</h2>
    </div>
    <div class="grid md:grid-cols-3 gap-4">
      <div class="p-6 bg-white rounded-2xl scroll-reveal"><h3 class="font-display font-bold text-bp-ink mb-1">المصانع والتصنيع</h3><p class="text-sm text-gray-600">انبعاثات التشغيل، والمذيبات، ومصادر الاحتراق</p></div>
      <div class="p-6 bg-white rounded-2xl scroll-reveal"><h3 class="font-display font-bold text-bp-ink mb-1">الأسمنت والمحاجر</h3><p class="text-sm text-gray-600">ترسّب الغبار والجسيمات عند حدود الموقع</p></div>
      <div class="p-6 bg-white rounded-2xl scroll-reveal"><h3 class="font-display font-bold text-bp-ink mb-1">الطاقة والتحلية</h3><p class="text-sm text-gray-600">انبعاثات المداخن والتزامات الرصد المستمر</p></div>
      <div class="p-6 bg-white rounded-2xl scroll-reveal"><h3 class="font-display font-bold text-bp-ink mb-1">البتروكيماويات والتكرير</h3><p class="text-sm text-gray-600">المركبات العضوية المتطايرة والانبعاثات الهاربة</p></div>
      <div class="p-6 bg-white rounded-2xl scroll-reveal"><h3 class="font-display font-bold text-bp-ink mb-1">الإنشاءات والبنية التحتية</h3><p class="text-sm text-gray-600">آثار مؤقتة لكنها مكثّفة من الغبار والمعدات</p></div>
      <div class="p-6 bg-white rounded-2xl scroll-reveal"><h3 class="font-display font-bold text-bp-ink mb-1">إدارة النفايات</h3><p class="text-sm text-gray-600">الروائح وغاز المرادم وانبعاثات الاحتراق</p></div>
    </div>
  </div>
</section>

<!-- دعوة للتواصل -->
<section class="py-20 text-white" style="background:var(--bp-grad);">
  <div class="max-w-3xl mx-auto px-4 text-center">
    <h2 class="font-display text-3xl md:text-4xl font-bold mb-4">لست متأكداً مما يتطلبه تصريحك؟</h2>
    <p class="text-white/80 mb-8">أرسل لنا الشروط وسنحدد لك بدقة المعايير والطرق والتكرارات المطلوبة. مراجعة بلا مقابل.</p>
    <div class="flex flex-wrap justify-center gap-3">
      <a href="contact.html" class="px-7 py-3.5 bg-white text-bp-ink rounded-xl font-bold">احجز استشارة مجانية</a>
      <a data-wa="السلام عليكم، لديّ استفسار عن الامتثال البيئي" class="px-7 py-3.5 border-2 border-white/60 text-white rounded-xl font-bold inline-flex items-center gap-2"><i class="fab fa-whatsapp"></i> واتساب</a>
    </div>
  </div>
</section>
"""
