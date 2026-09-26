# Arabic home page.
#
# The Arabic home is built FROM the English home, not beside it. home_new.home()
# renders the English page, then the maps below swap the words. Layout therefore
# lives in one place: change a section in English and the Arabic page follows.
#
# If an English sentence is added or reworded, its Arabic will be missing. The
# build then prints it under "untranslated", so nothing slips through silently.
#
# Wording follows the terminology glossary approved by the client.

import re, json, html as _html
from home_new import home as _english_home

# ---------------------------------------------------------------------------
# Text between tags. Matched as a whole text node, so short words cannot hit
# class names, URLs or longer sentences.
# ---------------------------------------------------------------------------
TEXT = [
 # cover, scene 1
 ("ACCREDITED ENVIRONMENTAL CONSULTANCY &middot; RIYADH", "استشارات بيئية معتمدة &middot; الرياض"),
 ("Compliance,", "الالتزام البيئي،"),
 ("handled", "نُنجزه"),
 ("properly.", "بإتقان."),
 ("Studies, permits and reporting for facilities operating under Saudi environmental regulation.",
  "دراسات وتراخيص وتقارير للمنشآت العاملة وفق الأنظمة البيئية في المملكة العربية السعودية."),
 ("LICENSED", "مرخّصون"), ("REGISTERED", "مسجّلون"), ("ACCREDITED", "معتمدون"), ("CERTIFIED", "حاصلون على الشهادات"),
 ("Book a free consultation", "احجز استشارة مجانية"),
 ("Our services", "خدماتنا"),
 # cover, scene 2
 ("MEASURED TO THE METHOD YOUR PERMIT SPECIFIES", "نقيس وفق الطريقة التي يحددها ترخيصك"),
 ("Air, water, soil and noise, to an accredited standard.", "الهواء والمياه والتربة والضوضاء، وفق معايير معتمدة."),
 ("AQI &middot; US EPA", "مؤشر جودة الهواء &middot; US EPA"),
 ("AMBIENT AIR &middot; RIYADH &middot; PUBLIC DATA", "الهواء المحيط &middot; الرياض &middot; بيانات عامة"),
 ("AMBIENT AIR", "الهواء المحيط"),
 ("COMBUSTION", "الاحتراق"),
 ("FUGITIVE EMISSIONS", "الانبعاثات الهاربة"),
 ("EFFLUENT", "المياه المصرفة"),
 ("Heavy metals", "المعادن الثقيلة"),
 ("WATER &middot; SOIL", "المياه &middot; التربة"),
 ("ACOUSTIC", "الصوتيات"),
 # cover, scene 3
 ("PERMITS &middot; MONITORING &middot; REPORTING", "التراخيص &middot; الرصد &middot; التقارير"),
 ("One consultancy, from first permit to every renewal.", "جهة استشارية واحدة، من أول ترخيص حتى كل تجديد."),
 ("Explore services", "استكشف خدماتنا"),
 ("Talk to a consultant", "تحدث إلى مستشار"),
 ("ROYAL COMMISSION", "الهيئة الملكية"),
 ("APPROVED", "معتمدون"),
 ("COMPLIANCE", "الالتزام"), ("MEASUREMENT", "القياس"), ("ACCREDITATION", "الاعتماد"),
 ("SCROLL &middot; 00%", "مرّر &middot; 00%"),

 # who we are
 ("Who we are", "من نحن"),
 ("Built for the Kingdom&rsquo;s", "نشأنا لمواكبة"),
 ("new rulebook", "الأنظمة البيئية الجديدة في المملكة"),
 ("A Riyadh-based environmental consultancy, formed to meet the demand created by the Kingdom's accelerating environmental regulation, pairing Saudi competencies with international expertise.",
  "شركة استشارات بيئية مقرها الرياض، تأسست لتلبية الطلب الذي أوجده تسارع الأنظمة البيئية في المملكة، وتجمع بين الكفاءات السعودية والخبرة الدولية."),
 ("Clients range from government authorities to industrial and commercial operators, oil and gas, petrochemicals, manufacturing, power and desalination, cement, food, agriculture and urban development.",
  "يتنوع عملاؤنا بين الجهات الحكومية والمنشآت الصناعية والتجارية، في قطاعات النفط والغاز، والبتروكيماويات، والتصنيع، والطاقة والتحلية، والأسمنت، والأغذية، والزراعة، والتطوير العمراني."),
 ("Our mission", "رسالتنا"),
 ("Innovative environmental solutions to the highest quality and safety standards, keeping clients fully compliant.",
  "تقديم حلول بيئية مبتكرة وفق أعلى معايير الجودة والسلامة، بما يضمن الالتزام الكامل لعملائنا."),
 ("Our vision", "رؤيتنا"),
 ("Supporting national policy and growing the Kingdom&rsquo;s environmental sector into a regional reference for green innovation.",
  "دعم السياسات الوطنية وتطوير القطاع البيئي في المملكة ليكون مرجعاً إقليمياً في الابتكار الأخضر."),
 ("NCEC Licensed", "مرخّصون من NCEC"),
 ("MWAN Registered", "مسجّلون لدى MWAN"),
 ("RCJY Approved", "معتمدون لدى RCJY"),
 ("Aligned with Vision 2030", "متوافقون مع رؤية 2030"),
 ("Vibrant Society", "مجتمع حيوي"),
 ("A cleaner, healthier environment that improves quality of life across the Kingdom.",
  "بيئة أنظف وأكثر صحة ترتقي بجودة الحياة في أنحاء المملكة."),
 ("Thriving Economy", "اقتصاد مزدهر"),
 ("Responsible industrial growth through compliant waste and environmental management.",
  "نمو صناعي مسؤول من خلال إدارة ملتزمة للنفايات والبيئة."),
 ("Ambitious Nation", "وطن طموح"),
 ("Advancing circular-economy practice and environmental governance.",
  "تعزيز ممارسات الاقتصاد الدائري والحوكمة البيئية."),

 # carousel heading
 ("OUR SERVICES", "خدماتنا"),
 ("Comprehensive", "حلول"),
 ("Environmental", "بيئية"),
 ("Solutions", "متكاملة"),
 ("From land to sea, accredited studies, permits and monitoring that keep facilities compliant across the Kingdom.",
  "من البر إلى البحر، دراسات معتمدة وتراخيص ورصد يُبقي المنشآت ملتزمة في أنحاء المملكة."),
 ("Trusted Partner", "شريك موثوق"),
 ("for a cleaner and safer future", "لمستقبل أنظف وأكثر أماناً"),
 ("Sustainable Solutions", "حلول مستدامة"),
 ("for a healthier environment", "لبيئة أكثر صحة"),

 # three service cards
 ("What we do", "ما نقوم به"),
 ("Take on any obligation", "نتولى أي التزام"),
 ("Three service lines covering the whole compliance lifecycle.",
  "ثلاثة مسارات خدمة تغطي دورة الالتزام البيئي بالكامل."),
 ("Hover a card to preview &middot; click to open the full list",
  "مرّر فوق البطاقة للمعاينة &middot; انقر لفتح القائمة الكاملة"),
 ("See full detail", "التفاصيل الكاملة"),

 # feature blocks
 ("Before you build", "قبل أن تبني"),
 ("Get licensed without losing a quarter", "احصل على ترخيصك دون أن تخسر ربع عام"),
 ("Most delays are not technical. They come from a misclassified activity or a file missing one supporting study. We classify first, then build the submission around what the reviewer will actually ask for.",
  "معظم التأخير ليس تقنياً، بل سببه تصنيف خاطئ للنشاط أو ملف تنقصه دراسة داعمة واحدة. نبدأ بالتصنيف، ثم نبني ملف التقديم حول ما ستطلبه الجهة المراجعة فعلاً."),
 ("Environmental permits", "التراخيص البيئية"),
 ("While you operate", "أثناء التشغيل"),
 ("Never scramble for an inspection again", "لا ارتباك بعد اليوم عند التفتيش"),
 ("Inspectors ask for the register first. We keep yours current, run the measurements your permit specifies, and file the periodic reports on schedule, so an inspection is a document check, not a fire drill.",
  "يطلب المفتشون السجل البيئي أولاً. نحافظ على سجلك محدّثاً، وننفذ القياسات التي يحددها ترخيصك، ونقدّم التقارير الدورية في موعدها، فيصبح التفتيش مراجعةً للمستندات لا حالة طوارئ."),
 ("Monitoring &amp; reporting", "الرصد والتقارير"),
 ("When it renews", "عند التجديد"),
 ("Renewals decided long before you apply", "قرار التجديد يُحسم قبل تقديم الطلب بوقت طويل"),
 ("Renewal review examines the whole permit term, not the application. Clients on ongoing reporting renew from a record that was maintained throughout, rather than assembled, and audited, at the last minute.",
  "مراجعة التجديد تفحص مدة الترخيص كاملة لا الطلب وحده. والعملاء المشتركون في التقارير المستمرة يجددون تراخيصهم من سجل حُفظ طوال المدة، لا من سجل جُمع ورُوجع في اللحظة الأخيرة."),
 ("Read the renewal guide", "اقرأ دليل التجديد"),

 # insights
 ("INSIGHTS", "رؤى"),
 ("Practical guidance on Saudi", "إرشادات عملية حول"),
 ("environmental", "الأنظمة"),
 ("regulation", "البيئية السعودية"),
 ("What the rules actually require, written for the people who have to comply with them, permit categories, reporting deadlines, inspection findings and what to do about them.",
  "ما تتطلبه الأنظمة فعلاً، مكتوباً لمن يلتزمون بها: فئات التراخيص، ومواعيد التقارير، ونتائج التفتيش، وكيفية التعامل معها."),
 ("Read all articles", "اقرأ جميع المقالات"),
 ("WRITTEN BY PRACTITIONERS", "كتبها ممارسون"),
 ("NOT BY MARKETERS", "لا مسوّقون"),
 ("Quarries & Mining", "المحاجر والتعدين"),
 ("Inspections", "التفتيش"),
 ("Renewals", "التجديد"),
 ("Permitting", "التراخيص"),
 ("Quarry Studies and Rehabilitation: The Obligation That Outlives the Site",
  "دراسات المحاجر وإعادة التأهيل: الالتزام الذي يدوم بعد انتهاء الموقع"),
 ("Extraction sites commit to a rehabilitation obligation years before it comes due. It does not expire because the quarry closed, sat idle, or changed hands.",
  "تلتزم مواقع الاستخراج بإعادة التأهيل قبل سنوات من استحقاقه، ولا يسقط هذا الالتزام بإغلاق المحجر أو توقفه أو انتقال ملكيته."),
 ("The Six Environmental Violations Saudi Inspectors Find Most Often",
  "المخالفات البيئية الست الأكثر رصداً من قِبل المفتشين في المملكة"),
 ("Almost every finding we see falls into the same handful of categories, and nearly all of them are documentation problems rather than engineering failures.",
  "تقع معظم الملاحظات التي نراها ضمن فئات محدودة، وأغلبها مشكلات في التوثيق لا إخفاقات هندسية."),
 ("Renewing Your Environmental Permit: Start Six Months Early",
  "تجديد ترخيصك البيئي: ابدأ قبل ستة أشهر"),
 ("Renewal is not a formality. Reviewers examine your compliance history, and an expired permit puts you in violation immediately, with no grace period in practice.",
  "التجديد ليس إجراءً شكلياً. تراجع الجهة سجل التزامك، والترخيص المنتهي يضعك في حالة مخالفة فوراً دون مهلة فعلية."),
 ("Environmental Permit Categories in Saudi Arabia: Which One Applies to You",
  "فئات الترخيص البيئي في المملكة العربية السعودية: أيها ينطبق عليك"),
 ("Category 1, 2, or 3 determines the studies you need, what you will pay, and how long licensing takes. Misclassifying your activity is the most expensive mistake we see.",
  "تحدد الفئة الأولى أو الثانية أو الثالثة الدراسات المطلوبة والتكلفة ومدة الترخيص، والتصنيف الخاطئ لنشاطك هو أكثر الأخطاء كلفة مما نراه."),
 ("Read more", "اقرأ المزيد"),
 ("Updated as the regulations change", "نحدّثها مع تغيّر الأنظمة"),
 ("All articles", "جميع المقالات"),

 # how we work
 ("How we work", "آلية العمل"),
 ("Compliance without the guesswork", "التزام بيئي دون تخمين"),
 ("A systematic workflow from the first site visit through to reporting that keeps you compliant cycle after cycle",
  "منهجية عمل واضحة من أول زيارة للموقع حتى التقارير التي تُبقيك ملتزماً دورة بعد دورة"),
 ("Project scoping", "تحديد نطاق المشروع"),
 ("Site visit and regulatory review, then a written scope agreed before any fieldwork begins.",
  "زيارة للموقع ومراجعة تنظيمية، ثم نطاق عمل مكتوب يُتفق عليه قبل بدء أي عمل ميداني."),
 ("Site assessment", "تقييم الموقع"),
 ("Field reconnaissance, existing conditions, and the receptor locations that apply to your activity.",
  "استطلاع ميداني للظروف القائمة ومواقع المستقبِلات المعنية بنشاطك."),
 ("Field measurement", "القياس الميداني"),
 ("Sampling and monitoring carried out to the standard your permit requires.",
  "أخذ العينات والرصد وفق المعيار الذي يشترطه ترخيصك."),
 ("Laboratory analysis", "التحليل المختبري"),
 ("Analysis and data validation against the applicable limit values.",
  "التحليل والتحقق من صحة البيانات مقارنةً بالحدود المسموح بها."),
 ("Reporting", "التقارير"),
 ("A submission-ready report, then register upkeep that keeps you compliant cycle after cycle.",
  "تقرير جاهز للتقديم، ثم متابعة السجل البيئي بما يُبقيك ملتزماً دورة بعد دورة."),

 # accreditations
 ("Accredited &amp; trusted", "معتمدون وموثوقون"),
 ("Accredited where it matters", "معتمدون حيث يهم الاعتماد"),
 ("Permit files are only accepted from accredited parties. Every credential below names the authority that issued it.",
  "لا تُقبل ملفات التراخيص إلا من جهات معتمدة، وكل اعتماد أدناه يذكر الجهة التي أصدرته."),
 ("Licensed environmental activities", "نشاطاً بيئياً مرخّصاً"),
 ("Environmental consulting licence", "ترخيص الاستشارات البيئية"),
 ("Waste management provider", "مقدّم خدمات إدارة النفايات"),
 ("Approved service provider", "مقدّم خدمات معتمد"),
 ("Royal Commission, Jubail &amp; Yanbu", "الهيئة الملكية للجبيل وينبع"),
 ("Laboratory &amp; inspection", "المختبرات والتفتيش"),
 ("Environmental management", "الإدارة البيئية"),
 ("ISO 9001 &amp; 45001", "ISO 9001 و45001"),
 ("Quality, health &amp; safety", "الجودة والصحة والسلامة"),
 ("Reports authorities accept", "تقارير تقبلها الجهات الرقابية"),
 ("Government-accredited and NCEC-aligned, so your file clears review the first time.",
  "معتمدة حكومياً ومتوافقة مع متطلبات NCEC، ليجتاز ملفك المراجعة من المرة الأولى."),
 ("Built around your facility", "مصمَّمة حول منشأتك"),
 ("Solutions shaped to your sector and activity, never a generic template.",
  "حلول تُصاغ وفق قطاعك ونشاطك، لا قوالب عامة."),
 ("One partner, whole lifecycle", "شريك واحد لكامل الدورة"),
 ("Licensing, studies and reporting under a single accountable team.",
  "التراخيص والدراسات والتقارير تحت مسؤولية فريق واحد."),

 # clients
 ("Trusted by", "يثق بنا"),
 ("Our partners and clients", "شركاؤنا وعملاؤنا"),
 ("Organisations across industry, energy, infrastructure and government that rely on our environmental work.",
  "جهات في قطاعات الصناعة والطاقة والبنية التحتية والقطاع الحكومي تعتمد على عملنا البيئي."),

 # sectors
 ("Who we serve", "من نخدم"),
 ("Every regulated sector", "كل قطاع خاضع للتنظيم"),
 ("We tailor compliance strategy to the obligations, risks and inspection cycles of your industry.",
  "نُكيّف استراتيجية الالتزام وفق التزامات قطاعك ومخاطره ودورات التفتيش فيه."),
 ("Industrial", "صناعي"), ("Light industry", "الصناعات الخفيفة"), ("Healthcare", "الرعاية الصحية"),
 ("Infrastructure", "البنية التحتية"), ("Commercial", "تجاري"), ("Extraction", "الاستخراج"),
 ("Factories &amp; Manufacturing", "المصانع والتصنيع"),
 ("Workshops &amp; Garages", "الورش ومراكز الصيانة"),
 ("Healthcare &amp; Veterinary", "المنشآت الصحية والبيطرية"),
 ("Construction &amp; Infrastructure", "الإنشاءات والبنية التحتية"),
 ("Commercial &amp; Retail", "التجاري والتجزئة"),
 ("Quarries &amp; Mining Sites", "المحاجر ومواقع التعدين"),
 ("The heaviest environmental obligations in the Kingdom, and the most expensive consequences for getting them wrong.",
  "أثقل الالتزامات البيئية في المملكة، وأعلى كلفة عند الإخلال بها."),
 ("Small premises, real obligations. Most owners find out when a licence renewal is blocked.",
  "منشآت صغيرة والتزامات حقيقية، يكتشفها معظم الملّاك عند تعثّر تجديد الترخيص."),
 ("Medical waste carries the strictest handling rules, enforced from the day a clinic opens.",
  "تخضع النفايات الطبية لأشد قواعد المناولة، وتُطبَّق منذ يوم افتتاح المنشأة."),
 ("Impacts are temporary but intense, and enforcement happens on the ground.",
  "الآثار مؤقتة لكنها شديدة، والرقابة تتم ميدانياً."),
 ("The simplified track still ties the permit to your commercial licence.",
  "حتى المسار المبسّط يربط الترخيص البيئي بسجلك التجاري."),
 ("Rehabilitation is committed to years before it comes due, and does not lapse.",
  "يُلتزم بإعادة التأهيل قبل سنوات من استحقاقها، ولا يسقط الالتزام بمرور الوقت."),
 ("Typically", "عادةً"),
 ("Permit, EMP, periodic reporting", "الترخيص، خطة الإدارة البيئية، التقارير الدورية"),
 ("Simplified permit track", "مسار الترخيص المبسّط"),
 ("MWAN waste permit, manifests", "ترخيص النفايات من MWAN، وبيانات الشحن"),
 ("CEMP, dust and noise monitoring", "خطة الإدارة البيئية للإنشاءات، ورصد الغبار والضوضاء"),
 ("Simplified permit, waste contract", "ترخيص مبسّط، وعقد نفايات"),
 ("EIA, rehabilitation plan", "دراسة تقييم الأثر البيئي، وخطة إعادة التأهيل"),
 ("See the service", "عرض الخدمة"),
]

# ---------------------------------------------------------------------------
# alt text, aria labels and titles
# ---------------------------------------------------------------------------
ATTR = [
 ("Refinery outside Riyadh at sunrise", "مصفاة خارج الرياض عند شروق الشمس"),
 ("Industrial facility at blue hour", "منشأة صناعية عند الغسق"),
 ("Aerial view of a river winding through misty forest at sunrise", "منظر جوي لنهر يتعرج بين غابة يلفها الضباب عند شروق الشمس"),
 ("Refinery and storage tanks in the desert at golden hour", "مصفاة وخزانات في الصحراء وقت الغروب"),
 ("Aerial view of the Saudi Red Sea coastline where desert meets protected shoreline",
  "منظر جوي لساحل البحر الأحمر حيث تلتقي الصحراء بالشاطئ المحمي"),
 ("Previous service", "الخدمة السابقة"), ("Next service", "الخدمة التالية"),
 ("Service list", "قائمة الخدمات"), ("Close", "إغلاق"),
 ("Environmental site assessment with survey pegs marking a project boundary",
  "تقييم بيئي لموقع مع أوتاد مساحية تحدد حدود المشروع"),
 ("Compliance inspection walkthrough with a checklist at an industrial facility",
  "جولة تفتيش على الالتزام البيئي بقائمة تحقق في منشأة صناعية"),
 ("Weathered ambient air quality monitoring station in the field", "محطة رصد لجودة الهواء المحيط في الموقع"),
 ("Project scoping", "تحديد نطاق المشروع"), ("Site assessment", "تقييم الموقع"),
 ("Field measurement", "القياس الميداني"), ("Laboratory analysis", "التحليل المختبري"), ("Reporting", "التقارير"),
 ("National Center for Environmental Compliance", "المركز الوطني للرقابة على الالتزام البيئي"),
 ("National Center for Waste Management", "المركز الوطني لإدارة النفايات"),
 ("Royal Commission for Jubail and Yanbu", "الهيئة الملكية للجبيل وينبع"),
 ("International Accreditation Service", "خدمة الاعتماد الدولية"),
 ("ISO 14001 certified", "حاصل على شهادة ISO 14001"),
 ("ISO certified", "حاصل على شهادات ISO"),
 ("Client logos", "شعارات العملاء"),
]

# markup where Arabic needs something other than a straight word swap
RAW = [
 ('<b>20+</b>', '<b dir="ltr">20+</b>'),
]

# technical terms and brand names that stay in Latin script inside Arabic text
ALLOWED = {"NCEC", "MWAN", "IAS", "RCJY", "ISO", "AQI", "US", "EPA", "PM2", "PM10", "PM", "NO", "SO", "CO",
           "VOCs", "COD", "BOD", "L90", "eq", "EIA", "ESIA", "CEMP", "EMP", "ESG", "UTC", "BluePrint", "Environmental",
           "Services"}


# ---------------------------------------------------------------------------
# Text the three scripts draw at runtime
# ---------------------------------------------------------------------------
def _script_data(available):
    def pg(href):
        base = href.split("#")[0]
        return href if base in available else "../" + href

    img = lambda p: "../" + p

    car_s = [
     ("الدراسات البيئية", "fa-seedling",
      "دراسات تقييم الأثر ودراسات الوضع القائم التي تدعم القرار المدروس والموافقة التنظيمية.",
      "service-environmental-studies.html", "assets/img/svc-card-1.webp"),
     ("البيئة البحرية", "fa-water",
      "جودة المياه والرواسب والموائل القاعية والمسح المحيطي للتطوير الساحلي والتصريف.",
      "service-marine-environment-services.html", "assets/img/svc-card-2.webp"),
     ("البيئة البرية", "fa-leaf",
      "رسم خرائط الموائل ودراسات الوضع القائم وتقييم الأنواع المحمية في البيئات الصحراوية والساحلية.",
      "service-terrestrial-environment.html", "assets/img/svc-card-3.webp"),
     ("الاستشارات البيطرية والأمن الحيوي", "fa-paw",
      "تخطيط الأمن الحيوي والاستشارات البيطرية للعمليات التي تلتقي فيها صحة الحيوان بالبيئة.",
      "service-veterinary-biosecurity.html", "assets/img/svc-card-4.webp"),
     ("الجسات الاختبارية", "fa-ruler-vertical",
      "حفر الجسات وأخذ العينات لتحديد ظروف التربة والمياه الجوفية ومدى انتشار التلوث.",
      "service-test-boreholes.html", "assets/img/svc-card-5.webp"),
     ("الهيدروجيولوجيا والجيوتقنية", "fa-tint",
      "تقييم المياه الجوفية والتحريات الجيوتقنية لأغراض التطوير والاستخراج والمعالجة.",
      "service-hydrogeology-geotechnics.html", "assets/img/svc-card-6.webp"),
     ("المعالجة وإعادة التأهيل", "fa-recycle",
      "تصميم معالجة الأراضي الملوثة والمتأثرة وإعادة تأهيلها حتى الإغلاق النهائي.",
      "service-treatment-rehabilitation.html", "assets/img/svc-card-7.webp"),
     ("التدريب البيئي", "fa-graduation-cap",
      "تدريب عملي لفرق المواقع على الرصد واشتراطات الترخيص وحفظ السجلات البيئية.",
      "service-environmental-training.html", "assets/img/svc-card-8.webp"),
    ]
    CAR_S = [{"t": t, "i": i, "d": d, "href": pg(h), "img": img(m)} for t, i, d, h, m in car_s]

    def grp(key, short, num, icon, im, pos, blurb, href, items):
        return {"key": key, "short": short, "num": num, "icon": icon, "img": img(im), "pos": pos,
                "blurb": blurb, "href": pg(href), "items": [[a, b, pg(c)] for a, b, c in items]}

    SVC = [
     grp("الالتزام البيئي والتراخيص", "التراخيص", "01", "fa-stamp", "assets/img/card-1.jpg", "20% 30%",
         "ترخيص منشأتك، والمحافظة عليه.", "service-environmental-permit.html", [
         ("الترخيص البيئي", "ملف الترخيص من البداية حتى الإصدار", "service-environmental-permit.html"),
         ("دراسة تقييم الأثر البيئي", "للمشاريع عالية الأثر (EIA/ESIA)", "service-environmental-impact-assessment.html"),
         ("ترخيص إدارة النفايات", "ترخيص MWAN للنفايات الخاضعة للتنظيم", "service-waste-management-permit.html"),
         ("خطة الإدارة البيئية", "اشتراطات الترخيص في الممارسة اليومية", "service-environmental-management-plan.html"),
         ("السجل البيئي", "إثبات مستمر للالتزام", "service-environmental-register.html"),
         ("التقرير البيئي الدوري", "للمحافظة على الترخيص الذي حصلت عليه", "service-periodic-environmental-report.html")]),
     grp("الرصد والفحص والقياس", "الرصد", "02", "fa-flask", "assets/img/card-2.jpg", "75% 60%",
         "الأرقام التي يقوم عليها كل إثبات للالتزام.", "service-air-quality-monitoring.html", [
         ("رصد جودة الهواء وفحصه", "القياس وفق المعايير السعودية", "service-air-quality-monitoring.html"),
         ("فحص المياه ومياه الصرف", "تحليل معتمد", "service-water-wastewater-testing.html"),
         ("رصد الضوضاء وتقييمها", "مقارنةً بالحدود النظامية", "service-noise-monitoring.html"),
         ("فحص التربة والرواسب", "الخصائص والملوثات", "service-soil-sediment-testing.html"),
         ("الرصد والقياس الميداني", "قياس دقيق للعناصر في الموقع", "service-field-monitoring.html"),
         ("أخذ العينات البيئية", "وفق بروتوكولات سلسلة الحيازة", "service-environmental-sampling.html"),
         ("برامج الرصد", "مجدولة ومتابَعة وموثّقة", "service-monitoring-programmes.html"),
         ("التحليل المختبري", "مع تفسير فني للنتائج", "service-laboratory-analysis.html"),
         ("معدات مكافحة التلوث", "التوريد والتشغيل", "service-pollution-control-equipment.html"),
         ("التقارير والالتزام البيئي", "التقارير التنظيمية الدورية", "service-reporting-compliance.html")]),
     grp("التخصصات المتقدمة", "التخصصات", "03", "fa-layer-group", "assets/img/card-3.jpg", "50% 75%",
         "أعمال فنية متعمقة في ستة تخصصات.", "services.html", [
         ("التغير المناخي والاستدامة", "الحوكمة البيئية والبصمة الكربونية والحياد الكربوني، 17 خدمة", "service-climate-sustainability.html"),
         ("المسوحات البيئية والأحيائية", "دراسة الوضع القائم والموائل والأنواع المحمية، 6 خدمات", "service-ecological-surveys.html"),
         ("البيئة البحرية", "أخذ العينات ورسم الخرائط والنمذجة، 6 خدمات", "service-marine-environment.html"),
         ("المعالجة وإعادة التأهيل", "من التحري حتى الأعمال الموقعية، 5 خدمات", "service-remediation-rehabilitation.html"),
         ("النمذجة البيئية", "الانتشار والهيدرولوجيا والضوضاء، 5 خدمات", "service-environmental-modelling.html"),
         ("خدمات المختبر", "من أخذ العينات حتى تفسير النتائج، 10 خدمات", "service-laboratory-services.html")]),
    ]
    SVC_T = {"services": "خدمات", "openList": "فتح القائمة الكاملة", "more": "أخرى",
             "hint": "مرّر فوق البطاقة للمعاينة · انقر لفتح القائمة الكاملة",
             "kicker": "خدماتنا", "view": "عرض خدمات {k}"}

    COVER_T = {
     # [label, value, x%, y%]: placed in the open left half, clear of the Arabic copy on the right
     "mk": [["جودة الهواء", "الحدود والمداخن", 22, 36], ["الأرصاد", "الرياح &middot; الحرارة", 36, 22],
            ["المياه", "المياه المصرفة والتصريف", 12, 62], ["الضوضاء", "الحدود والمستقبِلات", 38, 70],
            ["التربة", "الملوثات", 30, 50]],
     "scroll": "مرّر", "chapter": "الفصل {n} من 3",
     "bands": ["جيد", "متوسط", "غير صحي للفئات الحساسة", "غير صحي", "غير صحي جداً", "خطر"],
     "aqi": "مؤشر جودة الهواء · ", "src": "الهواء المحيط · الرياض · بيانات عامة · ",
    }
    CAR_T = {"go": "الانتقال إلى الخدمة "}

    j = lambda o: json.dumps(o, ensure_ascii=False)
    return ("<script>/* Arabic text for cover.js, carousel.js and cards.js */\n"
            "window.COVER_T=" + j(COVER_T) + ";\nwindow.CAR_S=" + j(CAR_S) + ";\nwindow.CAR_T=" + j(CAR_T) + ";\n"
            "window.SVC_DATA_AR=" + j(SVC) + ";\nwindow.SVC_T=" + j(SVC_T) + ";\n</script>\n")


# ---------------------------------------------------------------------------
def _translate(html):
    missing = []
    for en, ar in RAW:
        if en in html:
            html = html.replace(en, ar)
        else:
            missing.append(("raw", en))
    for en, ar in sorted(TEXT, key=lambda p: -len(p[0])):
        pat = re.compile(r">(\s*)" + r"\s+".join(re.escape(w) for w in en.split()) + r"(\s*)<")
        html, n = pat.subn(lambda m: ">" + m.group(1) + ar + m.group(2) + "<", html)
        if not n:
            missing.append(("text", en))
    for en, ar in ATTR:
        pat = re.compile(r'((?:alt|aria-label|title|placeholder)=")' + re.escape(en) + '"')
        html, n = pat.subn(lambda m: m.group(1) + ar + '"', html)
        if not n:
            missing.append(("attr", en))
    return html, missing


def untranslated(html):
    """Visible text on the page that still contains English."""
    body = re.sub(r"<script.*?</script>", "", html, flags=re.S)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.S)
    left = []
    for m in re.finditer(r">([^<>]+)<", body):
        s = " ".join(_html.unescape(m.group(1)).split())
        words = re.findall(r"[A-Za-z][A-Za-z.]*", s)
        if [w for w in words if w.strip(".") not in ALLOWED and len(w) > 1]:
            left.append(s)
    return sorted(set(left))


def home(available):
    html = _english_home()
    html, missing = _translate(html)
    for kind, s in missing:
        print("  [home_ar] no longer on the English page (%s): %s" % (kind, s[:70]))
    for s in untranslated(html):
        print("  [home_ar] untranslated: " + s[:90])
    return _script_data(available) + html


# Compliance Finder promo block on the home page
import finder as _FD
TEXT.extend(_FD.PROMO_AR.items())


# Live environmental map section
import livemap as _LM
TEXT.extend(_LM.AR_TEXT)
ATTR.extend(_LM.AR_ATTR)
ALLOWED |= {"Open", "Meteo", "Open-Meteo", "CAMS"}
