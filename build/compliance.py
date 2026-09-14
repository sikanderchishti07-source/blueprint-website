# BluePrint, Compliance Hub.
#
# Regulation entries carried across from the AECON environmental portal build.
# Each entry is a plain summary, NOT the legal text, and the references, limits,
# deadlines and penalty notes are reproduced as supplied. They have not been
# verified against the official instruments, which is why the page states that
# the official text governs.
#
# To add an entry, append a dict to REGS with the same keys.

CAT_META = {
    "air": ("fa-wind", "Air quality"),
    "water": ("fa-droplet", "Water"),
    "waste": ("fa-trash-can", "Waste management"),
    "noise": ("fa-volume-high", "Noise"),
    "eia": ("fa-clipboard-check", "EIA / ESIA"),
    "industrial": ("fa-industry", "Industrial"),
    "marine": ("fa-water", "Marine &amp; coastal"),
    "climate": ("fa-earth-americas", "Climate &amp; Vision 2030"),
}

CAT_ORDER = ["air", "water", "waste", "noise", "eia", "industrial", "marine", "climate"]

REGS = [
    {
        "id": "AIR-001", "category": "air", "article": "GAMEP Article 12", "year": 2021,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Ongoing — Annual reporting by 31 March",
        "penalty": "SAR 100,000–1,000,000 per violation",
        "title_en": "Ambient Air Quality Standards for Industrial Zones",
        "title_ar": "معايير جودة الهواء المحيط للمناطق الصناعية",
        "summary_en": "Industrial facilities must not exceed established ambient air quality limits for PM2.5, PM10, NO₂, SO₂, CO, and O₃. Continuous monitoring required at all major emission points.",
        "summary_ar": "يجب ألا تتجاوز المنشآت الصناعية الحدود المحددة لجودة الهواء المحيط لـ PM2.5 وPM10 وثاني أكسيد النيتروجين وثاني أكسيد الكبريت وأول أكسيد الكربون والأوزون.",
        "keywords": "air emission pm2.5 pm10 industrial monitoring pollution ambient",
        "details": [
            ("PM2.5 Limit", "35 µg/m³ (24h avg)"),
            ("PM10 Limit", "70 µg/m³ (24h avg)"),
            ("NO₂ Limit", "200 µg/m³ (hourly)"),
            ("SO₂ Limit", "350 µg/m³ (hourly)"),
            ("Monitoring", "Continuous CEMS"),
            ("Report Submission", "Monthly to GAMEP portal"),
        ],
    },
    {
        "id": "AIR-002", "category": "air", "article": "GAMEP Article 18", "year": 2022,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Compliance by Q1 2025",
        "penalty": "Facility shutdown order possible",
        "title_en": "Stack Emission Limits for Power Generation Facilities",
        "title_ar": "حدود انبعاثات المداخن لمنشآت توليد الكهرباء",
        "summary_en": "Power plants and cogeneration facilities must install certified stack emission monitoring systems and comply with NOₓ, SO₂, and particulate limits defined by GAMEP.",
        "summary_ar": "يجب على محطات الطاقة ومنشآت التوليد المشترك تركيب أنظمة مراقبة انبعاثات مداخن معتمدة والالتزام بالحدود المحددة من قبل الهيئة.",
        "keywords": "air stack emission power plant NOx SO2 cems",
        "details": [
            ("NOₓ Limit", "400 mg/Nm³"),
            ("SO₂ Limit", "600 mg/Nm³"),
            ("Particulates", "50 mg/Nm³"),
            ("CEMS Required", "Yes — certified by GAMEP"),
            ("Calibration", "Quarterly"),
        ],
    },
    {
        "id": "AIR-003", "category": "air", "article": "Royal Decree M/165", "year": 2020,
        "authority": "GAMEP", "severity": "medium",
        "deadline": "Ongoing — Biennial vehicle inspection",
        "penalty": "SAR 500–5,000 per vehicle",
        "title_en": "Vehicle Emission Standards and Inspection Requirements",
        "title_ar": "معايير انبعاثات المركبات ومتطلبات الفحص",
        "summary_en": "All vehicles operating in Saudi Arabia must comply with Euro 5 emission standards. Commercial fleet operators must maintain emission inspection records.",
        "summary_ar": "يجب أن تلتزم جميع المركبات العاملة في المملكة العربية السعودية بمعايير الانبعاثات اليورو 5.",
        "keywords": "air vehicle emission transport fleet inspection euro",
        "details": [
            ("Standard", "Euro 5 minimum"),
            ("CO Limit", "1.0 g/km"),
            ("NOₓ Limit", "0.06 g/km"),
            ("Inspection Cycle", "Every 2 years"),
            ("Fleet > 50 vehicles", "Internal audit required"),
        ],
    },
    {
        "id": "WAT-001", "category": "water", "article": "GAMEP Article 34", "year": 2021,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Ongoing — Quarterly lab testing required",
        "penalty": "SAR 200,000 + facility suspension",
        "title_en": "Industrial Wastewater Discharge Standards",
        "title_ar": "معايير تصريف مياه الصرف الصناعي",
        "summary_en": "Industrial facilities discharging wastewater into municipal networks or water bodies must comply with maximum permissible limits for BOD, COD, TSS, heavy metals, and pH.",
        "summary_ar": "يجب على المنشآت الصناعية التي تصرف مياه الصرف في شبكات الصرف البلدي أو المسطحات المائية الالتزام بالحدود القصوى.",
        "keywords": "wastewater industrial discharge water quality BOD COD TSS treatment",
        "details": [
            ("BOD Limit", "50 mg/L"),
            ("COD Limit", "150 mg/L"),
            ("TSS Limit", "60 mg/L"),
            ("pH Range", "6.0 – 9.0"),
            ("Oil & Grease", "10 mg/L max"),
            ("Testing Frequency", "Monthly minimum"),
        ],
    },
    {
        "id": "WAT-002", "category": "water", "article": "GAMEP Article 41", "year": 2022,
        "authority": "MEWA", "severity": "medium",
        "deadline": "New projects: compliance before commissioning",
        "penalty": "SAR 50,000–300,000",
        "title_en": "Treated Sewage Effluent Reuse Standards",
        "title_ar": "معايير إعادة استخدام مياه الصرف الصحي المعالجة",
        "summary_en": "Treated wastewater reused for irrigation, construction, or industrial cooling must meet tertiary treatment standards including microbial limits and nutrient thresholds.",
        "summary_ar": "يجب أن تستوفي مياه الصرف المعالجة المعادة للاستخدام في الري أو البناء معايير المعالجة الثلاثية.",
        "keywords": "wastewater reuse treated sewage irrigation recycled water TSE",
        "details": [
            ("Treatment Level", "Tertiary minimum"),
            ("E.coli Limit", "< 2.2 MPN/100mL"),
            ("Turbidity", "< 2 NTU"),
            ("Residual Chlorine", "0.5 – 1.5 mg/L"),
        ],
    },
    {
        "id": "WAT-003", "category": "water", "article": "Royal Decree M/34", "year": 2019,
        "authority": "MEWA", "severity": "high",
        "deadline": "Permit renewal every 3 years",
        "penalty": "SAR 500,000 + extraction suspension",
        "title_en": "Groundwater Protection and Extraction Permits",
        "title_ar": "حماية المياه الجوفية وتصاريح الاستخراج",
        "summary_en": "Any groundwater extraction exceeding 50 m³/day requires a permit from MEWA. Environmental impact assessment of aquifer depletion is mandatory for industrial operations.",
        "summary_ar": "يتطلب أي استخراج للمياه الجوفية يتجاوز 50 م³ يومياً الحصول على تصريح من وزارة البيئة والمياه والزراعة.",
        "keywords": "groundwater water extraction permit aquifer depletion MEWA",
        "details": [
            ("Permit Threshold", "> 50 m³/day"),
            ("EIA Required", "Yes for > 500 m³/day"),
            ("Monitoring Wells", "Min. 2 per site"),
            ("Permit Validity", "3 years"),
        ],
    },
    {
        "id": "WAT-004", "category": "water", "article": "GAMEP Article 52", "year": 2023,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Pre-commissioning + Annual update",
        "penalty": "Commissioning permit withheld",
        "title_en": "Desalination Plant Environmental Impact Requirements",
        "title_ar": "متطلبات الأثر البيئي لمحطات التحلية",
        "summary_en": "Desalination plants must submit brine disposal plans, thermal discharge assessments, and chemical additive registers to GAMEP before commissioning.",
        "summary_ar": "يجب على محطات التحلية تقديم خطط التخلص من المحلول الملحي وتقييمات التصريف الحراري إلى الهيئة قبل التشغيل.",
        "keywords": "desalination brine marine coastal water discharge thermal",
        "details": [
            ("Brine Temp Limit", "≤ 5°C above ambient"),
            ("Dilution Zone", "300m radius max"),
            ("Chlorine Residual", "< 0.1 mg/L"),
            ("Marine Survey", "Annual coral & seagrass"),
        ],
    },
    {
        "id": "WST-001", "category": "waste", "article": "GAMEP Article 60", "year": 2021,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Ongoing — 90-day max on-site storage",
        "penalty": "SAR 500,000 + criminal prosecution",
        "title_en": "Hazardous Waste Classification and Storage",
        "title_ar": "تصنيف النفايات الخطرة وتخزينها",
        "summary_en": "All hazardous waste generators must classify waste per GAMEP Schedule H, maintain manifests, and store in GAMEP-approved facilities not exceeding 90-day limits.",
        "summary_ar": "يجب على جميع منتجي النفايات الخطرة تصنيف النفايات وفقاً للجدول الزمني H من الهيئة والاحتفاظ بوثائق التتبع.",
        "keywords": "hazardous waste storage classification manifest toxic chemical industrial",
        "details": [
            ("Max On-site Storage", "90 days"),
            ("Container Labelling", "Arabic + English + UN code"),
            ("Manifest System", "GAMEP E-Manifest (mandatory)"),
            ("Emergency Plan", "Required — updated annually"),
        ],
    },
    {
        "id": "WST-002", "category": "waste", "article": "Royal Decree M/201", "year": 2024,
        "authority": "GAMEP", "severity": "medium",
        "deadline": "Applicable from 01 January 2024",
        "penalty": "SAR 100,000 per violation",
        "title_en": "Construction and Demolition Waste Recycling Requirements",
        "title_ar": "متطلبات إعادة تدوير نفايات البناء والهدم",
        "summary_en": "Construction projects exceeding 5,000 m² must implement a Waste Management Plan achieving minimum 70% diversion of C&D waste from landfill.",
        "summary_ar": "يجب على مشاريع البناء التي تتجاوز 5000 م² تطبيق خطة إدارة النفايات لتحقيق الحد الأدنى 70٪ من تحويل نفايات البناء.",
        "keywords": "construction demolition waste recycling CDW building NEOM giga project",
        "details": [
            ("Project Threshold", "> 5,000 m² GFA"),
            ("Diversion Target", "70% from landfill"),
            ("WMP Submission", "Before construction permit"),
            ("NEOM / Giga Projects", "85% diversion target"),
        ],
    },
    {
        "id": "WST-003", "category": "waste", "article": "GAMEP Article 67", "year": 2020,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Ongoing — Monthly audit log required",
        "penalty": "SAR 300,000 + license revocation",
        "title_en": "Medical and Clinical Waste Disposal Standards",
        "title_ar": "معايير التخلص من النفايات الطبية والسريرية",
        "summary_en": "Healthcare facilities must segregate, treat, and dispose of clinical waste using licensed contractors. Incineration must meet temperature and emission standards.",
        "summary_ar": "يجب على المنشآت الرعاية الصحية فصل النفايات السريرية ومعالجتها والتخلص منها عبر مقاولين مرخصين فقط.",
        "keywords": "medical waste clinical hospital healthcare disposal incineration",
        "details": [
            ("Incineration Temp", "850°C minimum"),
            ("Segregation", "4-stream minimum"),
            ("Contractor", "GAMEP licensed only"),
            ("Storage Time", "72 hours maximum"),
        ],
    },
    {
        "id": "NOI-001", "category": "noise", "article": "GAMEP Article 78", "year": 2021,
        "authority": "GAMEP", "severity": "medium",
        "deadline": "Ongoing — Quarterly monitoring",
        "penalty": "SAR 20,000–200,000",
        "title_en": "Industrial Noise Emission Limits",
        "title_ar": "حدود انبعاث الضوضاء الصناعية",
        "summary_en": "Industrial facilities must not exceed 70 dB(A) LAeq at the nearest receptor. Noise impact assessments required for new developments within 500m of residential zones.",
        "summary_ar": "يجب ألا تتجاوز المنشآت الصناعية 70 ديسيبل عند أقرب مستقبل. تُطلب تقييمات أثر الضوضاء ضمن 500 م من المناطق السكنية.",
        "keywords": "noise industrial emission dB limit residential buffer sound",
        "details": [
            ("Daytime Limit", "70 dB(A) at boundary"),
            ("Night Limit", "60 dB(A) (22:00–06:00)"),
            ("Residential Buffer", "500m NIA trigger"),
            ("Monitoring", "Quarterly at 4 cardinal points"),
        ],
    },
    {
        "id": "NOI-002", "category": "noise", "article": "GAMEP Article 82", "year": 2021,
        "authority": "GAMEP", "severity": "medium",
        "deadline": "Required before planning approval",
        "penalty": "Planning permit refused",
        "title_en": "Noise Impact Assessment for New Developments",
        "title_ar": "تقييم أثر الضوضاء للمشاريع الجديدة",
        "summary_en": "A baseline noise survey and predictive impact model is required for industrial, infrastructure, and mixed-use developments exceeding 2 hectares or within 1km of sensitive receptors.",
        "summary_ar": "يُطلب إجراء مسح للضوضاء الخلفية ونموذج تأثير تنبؤي للتطويرات الصناعية التي تتجاوز 2 هكتار.",
        "keywords": "noise assessment NIA baseline survey planning development impact",
        "details": [
            ("Survey Duration", "Min. 7 days continuous"),
            ("Model Standard", "ISO 9613-2 / CadnaA"),
            ("Trigger Distance", "1km from sensitive receptors"),
            ("Mitigation Plan", "Required if limits exceeded"),
        ],
    },
    {
        "id": "NOI-003", "category": "noise", "article": "GAMEP Article 85", "year": 2020,
        "authority": "GAMEP", "severity": "low",
        "deadline": "Permit required for night work",
        "penalty": "SAR 5,000–50,000",
        "title_en": "Construction Site Noise Control Requirements",
        "title_ar": "متطلبات التحكم في ضوضاء مواقع البناء",
        "summary_en": "Construction activities generating noise above 75 dB(A) at 10m must restrict operations to permitted hours. Night work requires prior GAMEP permit.",
        "summary_ar": "يجب على أنشطة البناء التي تولد ضوضاء تتجاوز 75 ديسيبل تقييد العمليات خلال ساعات العمل المسموح بها.",
        "keywords": "noise construction site building hours night work piling",
        "details": [
            ("Permitted Hours", "07:00 – 21:00 weekdays"),
            ("Weekend Hours", "09:00 – 18:00 (Fri/Sat)"),
            ("Night Work Permit", "GAMEP approval required"),
            ("Noise Barrier", "Required if > 75 dB(A)"),
        ],
    },
    {
        "id": "EIA-001", "category": "eia", "article": "Royal Decree M/34 + GAMEP EIA Regs", "year": 2021,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Before any construction permit",
        "penalty": "Construction permit null and void",
        "title_en": "Environmental Impact Assessment — Mandatory Threshold Projects",
        "title_ar": "تقييم الأثر البيئي — المشاريع الخاضعة للاشتراط الإلزامي",
        "summary_en": "All projects classified under GAMEP Category A or B require a full EIA before permits. Category A includes power plants, desalination, refineries, airports, and developments > 100 ha.",
        "summary_ar": "تتطلب جميع المشاريع المصنفة ضمن الفئة A أو B من الهيئة إجراء تقييم شامل للأثر البيئي قبل إصدار التصاريح.",
        "keywords": "EIA ESIA environmental impact assessment baseline scoping GAMEP permit",
        "details": [
            ("Category A Projects", "Power, desalination, refineries"),
            ("EIA Study Period", "Min. 12 months baseline"),
            ("Scoping Required", "Pre-EIA scoping meeting"),
            ("Public Consultation", "30-day comment period"),
        ],
    },
    {
        "id": "EIA-002", "category": "eia", "article": "GAMEP EIA Guidelines 2023", "year": 2023,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Ongoing throughout project lifecycle",
        "penalty": "Project suspension + SAR 5,000,000",
        "title_en": "Environmental and Social Impact Assessment for Giga-Projects",
        "title_ar": "تقييم الأثر البيئي والاجتماعي للمشاريع العملاقة",
        "summary_en": "NEOM, Red Sea Project, Qiddiya, and Diriyah Gate must conduct full ESIA aligned with IFC Performance Standards and Saudi GAMEP requirements, including biodiversity impact assessment.",
        "summary_ar": "يجب على المشاريع العملاقة إجراء تقييم شامل للأثر البيئي والاجتماعي وفقاً لمعايير أداء IFC.",
        "keywords": "ESIA EIA giga projects NEOM Red Sea Qiddiya IFC social impact biodiversity",
        "details": [
            ("Standard", "IFC Performance Standards"),
            ("Biodiversity", "Full IBAT screening required"),
            ("Stakeholder Engagement", "Continuous — IFC PS1"),
            ("Monitoring Plan", "ESMP with KPIs"),
        ],
    },
    {
        "id": "EIA-003", "category": "eia", "article": "GAMEP Article 29", "year": 2021,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Throughout construction & operation phases",
        "penalty": "SAR 300,000 per non-compliance event",
        "title_en": "Environmental Management Plan Implementation Requirements",
        "title_ar": "متطلبات تنفيذ خطة الإدارة البيئية",
        "summary_en": "All projects with approved EIA must implement an Environmental Management Plan (EMP) with monthly monitoring, quarterly audits, and annual third-party verification.",
        "summary_ar": "يجب على جميع المشاريع ذات تقييم الأثر البيئي المعتمد تطبيق خطة الإدارة البيئية مع المراقبة الشهرية.",
        "keywords": "EMP environmental management plan EIA construction monitoring audit compliance",
        "details": [
            ("Monthly Monitoring", "All EMP KPIs tracked"),
            ("Quarterly Audit", "Internal EHS team"),
            ("Annual Audit", "Third-party accredited firm"),
            ("Corrective Actions", "30-day closure required"),
        ],
    },
    {
        "id": "IND-001", "category": "industrial", "article": "GAMEP Article 95", "year": 2020,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Ongoing — SDS updated within 3 years",
        "penalty": "SAR 200,000 per facility",
        "title_en": "Chemical Inventory and Safety Data Sheet Requirements",
        "title_ar": "متطلبات جرد المواد الكيميائية وبطاقات بيانات السلامة",
        "summary_en": "All industrial facilities handling hazardous chemicals must maintain a complete chemical inventory with updated GHS-compliant Safety Data Sheets accessible to all employees.",
        "summary_ar": "يجب على جميع المنشآت الصناعية التي تتعامل مع المواد الكيميائية الخطرة الاحتفاظ بجرد كيميائي كامل.",
        "keywords": "chemical inventory SDS MSDS industrial hazardous GHS safety data sheet",
        "details": [
            ("GHS Standard", "UN GHS Rev. 8 compliant"),
            ("SDS Language", "Arabic + English required"),
            ("Review Period", "Every 3 years or on change"),
            ("Emergency Services", "Copy lodged with Civil Defence"),
        ],
    },
    {
        "id": "IND-002", "category": "industrial", "article": "Royal Decree M/42", "year": 2021,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Before any industrial operations begin",
        "penalty": "SAR 1,000,000 + criminal prosecution",
        "title_en": "Environmental Permit for Industrial Facility Operation",
        "title_ar": "التصريح البيئي لتشغيل المنشأة الصناعية",
        "summary_en": "No industrial facility may commence operations without a valid Environmental Operation Permit from GAMEP. Permits are sector-specific with binding environmental conditions.",
        "summary_ar": "لا يجوز لأي منشأة صناعية البدء في التشغيل دون تصريح تشغيل بيئي صالح من الهيئة.",
        "keywords": "industrial permit operation GAMEP license facility environmental approval",
        "details": [
            ("Application Lead Time", "Min. 6 months before ops"),
            ("Permit Validity", "5 years (renewable)"),
            ("Renewal Application", "12 months before expiry"),
            ("Permit Conditions", "Legally binding"),
        ],
    },
    {
        "id": "IND-003", "category": "industrial", "article": "GAMEP Article 101", "year": 2022,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Plan required before permit issuance",
        "penalty": "SAR 500,000 + criminal liability",
        "title_en": "Spill Prevention and Emergency Response Plan",
        "title_ar": "خطة منع الانسكابات والاستجابة للطوارئ",
        "summary_en": "Industrial facilities handling > 1,000 litres of liquid hazardous materials must maintain a certified SPCC plan updated every 2 years with annual drills.",
        "summary_ar": "يجب على المنشآت الصناعية التي تتعامل مع أكثر من 1000 لتر من المواد الخطرة السائلة الاحتفاظ بخطة معتمدة للوقاية من الانسكابات.",
        "keywords": "spill emergency response plan SPCC hazardous liquid containment industrial",
        "details": [
            ("Volume Threshold", "> 1,000 L hazardous liquid"),
            ("Plan Validity", "2 years"),
            ("Drill Frequency", "Minimum annually"),
            ("Secondary Containment", "110% of largest vessel"),
        ],
    },
    {
        "id": "MAR-001", "category": "marine", "article": "GAMEP Article 112", "year": 2021,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Permit required before any coastal works",
        "penalty": "SAR 2,000,000 + demolition order",
        "title_en": "Coastal Development Setback and Buffer Zone Requirements",
        "title_ar": "متطلبات حظر البناء الساحلي ومناطق الحماية",
        "summary_en": "No permanent structures may be built within 200m of the mean high-water mark along Red Sea and Arabian Gulf coastlines without GAMEP coastal zone permit.",
        "summary_ar": "لا يجوز إنشاء منشآت دائمة على بعد 200 م من مستوى الماء المرتفع المتوسط على طول سواحل البحر الأحمر وخليج العرب دون تصريح.",
        "keywords": "coastal marine setback buffer zone development Red Sea MPA protected area",
        "details": [
            ("Setback Distance", "200m from mean high water"),
            ("MPA Buffer", "500m from Marine Protected Areas"),
            ("Permit Type", "Coastal Zone Development Permit"),
            ("EIA Requirement", "Full marine EIA mandatory"),
        ],
    },
    {
        "id": "MAR-002", "category": "marine", "article": "MARPOL / Royal Decree", "year": 2020,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Ongoing — MARPOL Annex compliance",
        "penalty": "SAR 1,000,000 + vessel detention",
        "title_en": "Ship and Port Discharge Regulations",
        "title_ar": "لوائح التصريف من السفن والموانئ",
        "summary_en": "All vessels in Saudi territorial waters must comply with MARPOL. Ports must provide waste reception facilities. Bilge water and ballast water discharge strictly regulated.",
        "summary_ar": "يجب على جميع السفن في المياه الإقليمية السعودية الامتثال للوائح ماربول.",
        "keywords": "marine ship port discharge MARPOL ballast water bilge coastal",
        "details": [
            ("Oily Water", "< 15 ppm (open sea)"),
            ("Bilge Water", "No discharge within 12nm"),
            ("Ballast Water", "D-2 standard treatment"),
            ("IOPP Certificate", "Required for vessels > 400 GT"),
        ],
    },
    {
        "id": "MAR-003", "category": "marine", "article": "GAMEP Article 118", "year": 2023,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Pre-works biological survey required",
        "penalty": "SAR 5,000,000 + project suspension",
        "title_en": "Coral Reef and Seagrass Protection in Development Zones",
        "title_ar": "حماية الشعاب المرجانية والأعشاب البحرية",
        "summary_en": "Any development or dredging near coral reef or seagrass habitats requires a Marine Biological Survey, compensation plan, and ongoing ecological monitoring.",
        "summary_ar": "يتطلب أي نشاط تطوير أو حفر بالقرب من موائل الشعاب المرجانية إجراء مسح بيولوجي بحري وخطة تعويض.",
        "keywords": "coral reef marine seagrass protection dredging development biological survey",
        "details": [
            ("Survey Requirement", "Pre-works marine biological"),
            ("No-go Zones", "50m radius from live coral"),
            ("Compensation Ratio", "3:1 (restored : impacted)"),
            ("Monitoring Period", "5 years post-construction"),
        ],
    },
    {
        "id": "CLI-001", "category": "climate", "article": "Saudi Green Initiative Framework", "year": 2023,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Annual report by 30 June each year",
        "penalty": "SAR 500,000 per year unreported",
        "title_en": "Carbon Emission Reporting — Large Industrial Emitters",
        "title_ar": "متطلبات الإبلاغ عن انبعاثات الكربون",
        "summary_en": "Industrial facilities emitting > 25,000 tCO₂e annually must register with GAMEP National Carbon Registry, submit verified GHG inventory, and report Scope 1 and 2 emissions using ISO 14064.",
        "summary_ar": "يجب على المنشآت الصناعية التي تنبعث منها أكثر من 25000 طن من ثاني أكسيد الكربون سنوياً التسجيل في سجل الكربون الوطني.",
        "keywords": "carbon emission GHG greenhouse gas reporting CO2 climate Vision 2030 Scope",
        "details": [
            ("Reporting Threshold", "> 25,000 tCO₂e/year"),
            ("Scope Required", "Scope 1 + Scope 2"),
            ("Scope 3", "Voluntary (2026 target)"),
            ("Verification", "Third-party ISO 14064"),
        ],
    },
    {
        "id": "CLI-002", "category": "climate", "article": "Vision 2030 Circular Carbon Economy", "year": 2024,
        "authority": "MEWA", "severity": "medium",
        "deadline": "All new parks from 2024 onwards",
        "penalty": "Development license conditions",
        "title_en": "Renewable Energy Integration for Industrial Parks",
        "title_ar": "متطلبات دمج الطاقة المتجددة للمناطق الصناعية",
        "summary_en": "New industrial parks and special economic zones must demonstrate a minimum 30% renewable energy share in their master energy plan as part of Vision 2030 green economy.",
        "summary_ar": "يجب على المناطق الصناعية الجديدة والمناطق الاقتصادية الخاصة إظهار حصة طاقة متجددة تبلغ 30٪ على الأقل.",
        "keywords": "renewable energy solar wind industrial Vision 2030 carbon net zero climate",
        "details": [
            ("Renewable Share", "Minimum 30%"),
            ("Preferred Sources", "Solar PV, wind, geothermal"),
            ("Energy Audit", "Required every 3 years"),
            ("Target 2030", "50% renewable nationally"),
        ],
    },
    {
        "id": "CLI-003", "category": "climate", "article": "GAMEP Circular 2024/08", "year": 2024,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Net-zero target by 2030",
        "penalty": "Project license conditions",
        "title_en": "Environmental Requirements for NEOM and Giga-Project Developers",
        "title_ar": "المتطلبات البيئية لمطوري مشروع نيوم والمشاريع العملاقة",
        "summary_en": "NEOM and all Vision 2030 giga-project developers must achieve net-zero carbon operations by 2030, implement circular economy principles, and publish annual sustainability reports.",
        "summary_ar": "يجب على مطوري مشروع نيوم وجميع المشاريع العملاقة تحقيق الحياد الكربوني بحلول عام 2030.",
        "keywords": "NEOM giga project net zero carbon circular economy Vision 2030 sustainability",
        "details": [
            ("Carbon Target", "Net-zero by 2030"),
            ("Circular Economy", "Zero waste to landfill"),
            ("Water Efficiency", "100% water recycling"),
            ("Annual Report", "Public sustainability disclosure"),
        ],
    },
    {
        "id": "AIR-004", "category": "air", "article": "GAMEP Article 22", "year": 2022,
        "authority": "GAMEP", "severity": "high",
        "deadline": "LDAR program: quarterly inspection",
        "penalty": "SAR 150,000 per event",
        "title_en": "Volatile Organic Compound (VOC) Emission Controls",
        "title_ar": "ضوابط انبعاثات المركبات العضوية المتطايرة",
        "summary_en": "Petrochemical, paint, and solvent-using facilities must install VOC capture systems and comply with total VOC emission thresholds. Leak Detection and Repair (LDAR) programs are mandatory.",
        "summary_ar": "يجب على مرافق البتروكيماويات والطلاء تركيب أنظمة التقاط VOC والامتثال للحدود الإجمالية.",
        "keywords": "VOC volatile organic compound petrochemical LDAR benzene BTEX emission control",
        "details": [
            ("Total VOC Limit", "50 mg/Nm³ (process vent)"),
            ("Benzene Limit", "5 mg/Nm³"),
            ("LDAR Program", "Quarterly component survey"),
            ("Capture Efficiency", "≥ 95% for thermal oxidizers"),
        ],
    },
    {
        "id": "AIR-005", "category": "air", "article": "GAMEP Article 27", "year": 2023,
        "authority": "GAMEP", "severity": "medium",
        "deadline": "Plan required before site clearance",
        "penalty": "SAR 30,000 per violation",
        "title_en": "Dust and Particulate Matter Control for Construction Sites",
        "title_ar": "التحكم في الغبار والجسيمات الدقيقة في مواقع البناء",
        "summary_en": "All construction sites > 1,000 m² must implement a Dust Management Plan including water spraying, hoarding, and real-time PM10 monitoring at site boundaries.",
        "summary_ar": "يجب على جميع مواقع البناء التي تزيد على 1000 م² تنفيذ خطة إدارة الغبار.",
        "keywords": "dust construction PM10 particulate matter site control spraying hoarding",
        "details": [
            ("Site Threshold", "> 1,000 m²"),
            ("PM10 Monitoring", "Continuous at boundaries"),
            ("Water Spraying", "≥ 2× daily in dry season"),
            ("Hoarding", "3m min. height on perimeter"),
        ],
    },
    {
        "id": "WAT-005", "category": "water", "article": "MEWA Regulation 2022/14", "year": 2022,
        "authority": "MEWA", "severity": "medium",
        "deadline": "New buildings: comply at commissioning",
        "penalty": "SAR 50,000 per audit cycle",
        "title_en": "Water Conservation Requirements for Commercial Buildings",
        "title_ar": "متطلبات ترشيد المياه للمباني التجارية",
        "summary_en": "Commercial buildings > 10,000 m² must install smart metering, greywater recycling systems, and achieve minimum 30% water use reduction versus 2020 baseline.",
        "summary_ar": "يجب على المباني التجارية التي تزيد على 10000 م² تركيب أنظمة قياس ذكية وأنظمة إعادة تدوير المياه الرمادية.",
        "keywords": "water conservation commercial building greywater smart metering efficiency",
        "details": [
            ("Building Threshold", "> 10,000 m² GFA"),
            ("Smart Metering", "Sub-metering per floor"),
            ("Greywater Recycling", "Toilets + irrigation"),
            ("Water Reduction Target", "30% vs 2020 baseline"),
        ],
    },
    {
        "id": "WST-004", "category": "waste", "article": "GAMEP Article 72", "year": 2022,
        "authority": "GAMEP", "severity": "medium",
        "deadline": "Ongoing — Annual e-waste audit",
        "penalty": "SAR 75,000 per disposal event",
        "title_en": "E-Waste and Electrical Equipment Disposal Requirements",
        "title_ar": "متطلبات التخلص من النفايات الإلكترونية والمعدات الكهربائية",
        "summary_en": "Businesses disposing of electronic equipment, batteries, and fluorescent lamps must use GAMEP-registered e-waste recyclers. Take-back schemes mandatory for manufacturers.",
        "summary_ar": "يجب على الشركات التي تتخلص من المعدات الإلكترونية والبطاريات استخدام معيدي تدوير النفايات الإلكترونية المسجلين.",
        "keywords": "e-waste electronic equipment recycling battery lamp WEEE disposal",
        "details": [
            ("Covered Items", "ICT, batteries, lamps, HVAC"),
            ("Recycler", "GAMEP registered only"),
            ("Manufacturer", "Take-back scheme required"),
            ("Data Destruction", "Certified before disposal"),
        ],
    },
    {
        "id": "IND-004", "category": "industrial", "article": "GAMEP Article 108", "year": 2023,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Annual — Submit within 60 days",
        "penalty": "SAR 200,000 per missed audit",
        "title_en": "Environmental Auditing Requirements for Industrial Facilities",
        "title_ar": "متطلبات المراجعة البيئية للمنشآت الصناعية",
        "summary_en": "Category A industrial facilities must conduct annual third-party environmental compliance audits with certified auditors. Results submitted to GAMEP within 60 days of completion.",
        "summary_ar": "يجب على المنشآت الصناعية من الفئة A إجراء تدقيقات امتثال بيئي سنوية من طرف ثالث.",
        "keywords": "environmental audit compliance industrial third party GAMEP certification",
        "details": [
            ("Audit Frequency", "Annual (Category A)"),
            ("Auditor", "GAMEP approved third-party"),
            ("Submission", "60 days post-completion"),
            ("Corrective Actions", "90-day closure plan"),
        ],
    },
    {
        "id": "MAR-004", "category": "marine", "article": "NCEC Marine Regulation 2023", "year": 2023,
        "authority": "NCEC", "severity": "high",
        "deadline": "Clearance before any marine activity",
        "penalty": "SAR 3,000,000 + activity suspension",
        "title_en": "Marine Protected Area Buffer Zone Management",
        "title_ar": "إدارة منطقة الحماية البحرية",
        "summary_en": "Activities within 1km of Marine Protected Areas (MPAs) require GAMEP environmental clearance. Anchoring, dredging, and underwater works are prohibited within MPA boundaries.",
        "summary_ar": "تتطلب الأنشطة ضمن 1 كم من المناطق البحرية المحمية الحصول على تصريح بيئي من الهيئة.",
        "keywords": "MPA marine protected area buffer zone anchoring dredging clearance NCEC",
        "details": [
            ("MPA Buffer", "1km activity restriction zone"),
            ("Prohibited Activities", "Anchoring, dredging, dumping"),
            ("Environmental Clearance", "Required for all works"),
            ("Monitoring", "Real-time AIS vessel tracking"),
        ],
    },
    {
        "id": "CLI-004", "category": "climate", "article": "Saudi Green Initiative 2023", "year": 2023,
        "authority": "MEWA", "severity": "high",
        "deadline": "BMP before construction approval",
        "penalty": "SAR 2,000,000 + project suspension",
        "title_en": "Biodiversity Conservation and Natural Habitat Protection",
        "title_ar": "حفظ التنوع البيولوجي وحماية الموائل الطبيعية",
        "summary_en": "The Saudi Green Initiative mandates no-net-loss of biodiversity for all major developments. Biodiversity Management Plans with offset schemes required for projects in sensitive habitats.",
        "summary_ar": "تُلزم مبادرة السعودية الخضراء بعدم خسارة صافية للتنوع البيولوجي لجميع التطويرات الكبرى.",
        "keywords": "biodiversity habitat conservation offset Saudi Green Initiative nature ecology",
        "details": [
            ("Principle", "No-net-loss of biodiversity"),
            ("BMP Required", "For sensitive habitat projects"),
            ("Offset Ratio", "Minimum 2:1"),
            ("Baseline Survey", "Full ecological assessment"),
        ],
    },
    {
        "id": "EIA-004", "category": "eia", "article": "GAMEP Article 33", "year": 2022,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Before cluster master plan approval",
        "penalty": "Development license withheld",
        "title_en": "Cumulative Impact Assessment for Industrial Cluster Developments",
        "title_ar": "تقييم التأثير التراكمي لتطوير التجمعات الصناعية",
        "summary_en": "Industrial clusters and economic zones with multiple co-located facilities must commission a Cumulative Environmental Impact Assessment (CEIA) covering shared infrastructure impacts.",
        "summary_ar": "يجب على المجمعات الصناعية والمناطق الاقتصادية إجراء تقييم تراكمي للأثر البيئي يغطي تأثيرات البنية التحتية المشتركة.",
        "keywords": "cumulative impact assessment industrial cluster economic zone CEIA infrastructure",
        "details": [
            ("CEIA Scope", "All facilities + shared infrastructure"),
            ("Air Quality Model", "Dispersion modelling required"),
            ("Groundwater", "Cumulative extraction assessment"),
            ("Traffic", "Cumulative vehicle emissions"),
        ],
    },
    {
        "id": "WST-005", "category": "waste", "article": "GAMEP Article 75", "year": 2023,
        "authority": "GAMEP", "severity": "high",
        "deadline": "Design compliance before licensing",
        "penalty": "Operating license revoked",
        "title_en": "Landfill Design and Leachate Management Standards",
        "title_ar": "معايير تصميم مدافن النفايات وإدارة الراشح",
        "summary_en": "Engineered landfills must include compacted clay and HDPE liner systems, leachate collection, and landfill gas capture. Environmental monitoring wells required at all permitted landfills.",
        "summary_ar": "يجب أن تتضمن مدافن النفايات الهندسية أنظمة بطانة HDPE وجمع الراشح والتقاط غاز المدفن.",
        "keywords": "landfill liner leachate gas capture groundwater monitoring municipal solid waste",
        "details": [
            ("Liner System", "Compacted clay + 1.5mm HDPE"),
            ("Leachate Collection", "Engineered drainage layer"),
            ("Gas Capture", "Required for Class I & II"),
            ("Monitoring Wells", "Minimum 4 (up-/downgradient)"),
        ],
    },
    {
        "id": "IND-005", "category": "industrial", "article": "GAMEP Article 115", "year": 2021,
        "authority": "GAMEP", "severity": "medium",
        "deadline": "EHS Officer certified before operations",
        "penalty": "SAR 50,000 per non-compliant facility",
        "title_en": "Environmental Training and Competency Requirements",
        "title_ar": "متطلبات التدريب البيئي والكفاءة",
        "summary_en": "All industrial facilities must have at least one certified Environmental Health & Safety (EHS) officer per site. Annual environmental awareness training is mandatory for all operational staff.",
        "summary_ar": "يجب أن تمتلك جميع المنشآت الصناعية مسؤول صحة وسلامة وبيئة معتمداً واحداً على الأقل لكل موقع.",
        "keywords": "EHS training environmental officer competency NEBOSH IEMA industrial facility",
        "details": [
            ("EHS Officer", "Certified — NEBOSH / IEMA"),
            ("Staff Training", "Annual minimum 8 hours"),
            ("Emergency Drills", "Twice yearly minimum"),
            ("Training Records", "Retained 5 years"),
        ],
    },
    {
        "id": "AIR-006", "category": "air", "article": "GAMEP Article 25", "year": 2023,
        "authority": "GAMEP", "severity": "medium",
        "deadline": "OMP required before permit renewal",
        "penalty": "SAR 30,000 per complaint upheld",
        "title_en": "Odour Management Requirements for Industrial Facilities",
        "title_ar": "متطلبات إدارة الروائح للمنشآت الصناعية",
        "summary_en": "Industrial facilities generating detectable odours must quantify emissions in odour units using EN 13725, prepare an Odour Management Plan, and investigate complaints within 48 hours.",
        "summary_ar": "يجب على المنشآت الصناعية التي تولد روائح قابلة للكشف قياس الانبعاثات بوحدات الرائحة.",
        "keywords": "odour smell management industrial EN 13725 olfactometry complaint",
        "details": [
            ("Measurement", "EN 13725 olfactometry"),
            ("Limit", "5 ouE/m³ at receptor"),
            ("Complaint Response", "48 hours investigation"),
            ("Buffer Zone", "Site-specific dispersion model"),
        ],
    },
    {
        "id": "EIA-005", "category": "eia", "article": "GAMEP Article 37", "year": 2022,
        "authority": "GAMEP", "severity": "medium",
        "deadline": "HIA before any ground disturbance",
        "penalty": "SAR 1,000,000 + works stopped",
        "title_en": "Heritage and Archaeological Impact Assessment Requirements",
        "title_ar": "متطلبات تقييم الأثر على التراث والآثار",
        "summary_en": "Developments in proximity to heritage sites or areas of archaeological potential must commission a Heritage Impact Assessment (HIA) before ground disturbance permits are issued.",
        "summary_ar": "يجب على المشاريع القريبة من المواقع التراثية إجراء تقييم أثر تراثي قبل إصدار تصاريح الحفر.",
        "keywords": "heritage archaeology HIA impact assessment ground disturbance cultural",
        "details": [
            ("Trigger", "Within 2km of heritage site"),
            ("Walkover Survey", "Certified archaeologist"),
            ("SAU Approval", "Saudi Heritage Authority sign-off"),
            ("Chance Finds", "Stop-work procedure required"),
        ],
    },
    {
        "id": "CLI-005", "category": "climate", "article": "Vision 2030 / NCCC", "year": 2024,
        "authority": "NCEC", "severity": "medium",
        "deadline": "Annual — within 4 months of fiscal year end",
        "penalty": "Stock exchange disclosure penalty",
        "title_en": "Corporate Sustainability Reporting Requirements",
        "title_ar": "متطلبات تقارير الاستدامة للشركات",
        "summary_en": "Listed companies and large enterprises with turnover > SAR 500M must publish annual ESG/Sustainability reports aligned with GRI Standards and Saudi Exchange Sustainability Reporting Guide.",
        "summary_ar": "يجب على الشركات المدرجة والمؤسسات الكبرى نشر تقارير ESG سنوية متوافقة مع معايير GRI.",
        "keywords": "ESG sustainability reporting GRI corporate disclosure climate social governance",
        "details": [
            ("Reporting Standard", "GRI Standards 2021"),
            ("Company Threshold", "Listed or > SAR 500M revenue"),
            ("ESG Topics", "E: emissions, water, waste; S: diversity, safety"),
            ("Assurance", "Independent assurance recommended"),
        ],
    },
]

SEV_LABEL = {"high": "High", "medium": "Medium", "low": "Low"}


def _counts():
    out = {}
    for r in REGS:
        out[r["category"]] = out.get(r["category"], 0) + 1
    out["all"] = len(REGS)
    return out


def _chips():
    c = _counts()
    out = ['<button class="cmp-chip active" data-cat="all" type="button">'
           '<i class="fas fa-layer-group"></i><span>All regulations</span>'
           '<em>' + str(c["all"]) + '</em></button>']
    for key in CAT_ORDER:
        n = c.get(key, 0)
        if not n:
            continue
        icon, name = CAT_META[key]
        out.append(
            '<button class="cmp-chip" data-cat="' + key + '" type="button">'
            '<i class="fas ' + icon + '"></i><span>' + name + '</span>'
            '<em>' + str(n) + '</em></button>')
    return "\n".join(out)


def _authbtns():
    auths = []
    for r in REGS:
        if r["authority"] not in auths:
            auths.append(r["authority"])
    out = ['<button class="cmp-pill active" data-auth="all" type="button">All authorities</button>']
    for a in auths:
        out.append('<button class="cmp-pill" data-auth="' + a + '" type="button">' + a + '</button>')
    return "\n".join(out)


def _details(rows, rid):
    if not rows:
        return ""
    cells = "\n".join(
        '<div class="cmp-kv"><dt>' + k + '</dt><dd>' + v + '</dd></div>'
        for k, v in rows)
    return (
        '<div class="cmp-detail" id="d-' + rid + '" hidden>'
        '<dl class="cmp-kvs">' + cells + '</dl>'
        '</div>')


def _cards():
    out = []
    for r in REGS:
        sev = r["severity"]
        hay = " ".join([
            r["id"], r["article"], r["title_en"], r["title_ar"],
            r["summary_en"], r["summary_ar"], r["keywords"], r["authority"],
        ]).lower().replace('"', "")
        icon, catname = CAT_META.get(r["category"], ("fa-file", r["category"]))
        toggle = ""
        if r["details"]:
            toggle = ('<button class="cmp-more" type="button" data-target="d-' + r["id"] + '">'
                      '<span>Limits &amp; requirements</span>'
                      '<i class="fas fa-chevron-down"></i></button>')
        penalty = ""
        if r["penalty"]:
            penalty = ('<p class="cmp-penalty"><i class="fas fa-triangle-exclamation"></i>'
                       + r["penalty"] + '</p>')
        out.append(
            '<article class="cmp-card" data-cat="' + r["category"] + '" data-sev="' + sev + '" '
            'data-auth="' + r["authority"] + '" data-text="' + hay + '">'
            '<div class="cmp-meta">'
            '<span class="cmp-ref">' + r["article"] + '</span>'
            '<span class="cmp-tag"><i class="fas ' + icon + '"></i>' + catname + '</span>'
            '<span class="cmp-tag">' + r["authority"] + '</span>'
            '<span class="cmp-tag">' + str(r["year"]) + '</span>'
            '<span class="cmp-sev cmp-sev-' + sev + '">' + SEV_LABEL.get(sev, sev) + '</span>'
            '</div>'
            '<h3>' + r["title_en"] + '</h3>'
            '<p class="cmp-ar" dir="rtl" lang="ar">' + r["title_ar"] + '</p>'
            '<p class="cmp-desc">' + r["summary_en"] + '</p>'
            '<div class="cmp-foot">'
            '<span class="cmp-deadline"><i class="fas fa-calendar-day"></i>' + r["deadline"] + '</span>'
            + toggle +
            '</div>'
            + _details(r["details"], r["id"])
            + penalty +
            '</article>')
    return "\n".join(out)


def _statblock():
    c = _counts()
    sev = {}
    for r in REGS:
        sev[r["severity"]] = sev.get(r["severity"], 0) + 1
    auths = len(set(r["authority"] for r in REGS))
    stats = [
        (str(c["all"]), "Regulations listed"),
        (str(len([k for k in c if k != "all"])), "Categories"),
        (str(auths), "Issuing authorities"),
        (str(sev.get("high", 0)), "High severity"),
    ]
    return "\n".join(
        '<div><strong>' + v + '</strong><span>' + l + '</span></div>' for v, l in stats)


_TPL = """
<section class="cmp-hero">
  <div class="cmp-wrap">
    <nav class="cmp-crumb" aria-label="Breadcrumb">
      <a href="index.html">Home</a><span>/</span><span>Compliance Hub</span>
    </nav>
    <p class="cmp-eyebrow">Saudi Arabia &middot; GAMEP &middot; MEWA &middot; NCEC</p>
    <h1>Compliance hub</h1>
    <p class="cmp-lede">The environmental obligations that apply to regulated facilities in the
       Kingdom, in one searchable place. Filter by category, authority or severity, and open any
       entry for the limits and requirements attached to it.</p>
    <div class="cmp-stats">{stats}</div>
  </div>
</section>

<div class="cmp-body">
  <div class="cmp-wrap">

    <div class="cmp-tools">
      <div class="cmp-search">
        <i class="fas fa-magnifying-glass"></i>
        <input type="search" id="cmpSearch" autocomplete="off"
               placeholder="Search by keyword, article reference or Arabic text"
               aria-label="Search regulations" />
      </div>
      <div class="cmp-sevfilter">
        <button class="cmp-sev-btn active" data-sev="all" type="button">All</button>
        <button class="cmp-sev-btn" data-sev="high" type="button">High</button>
        <button class="cmp-sev-btn" data-sev="medium" type="button">Medium</button>
        <button class="cmp-sev-btn" data-sev="low" type="button">Low</button>
      </div>
    </div>

    <div class="cmp-chips">{chips}</div>
    <div class="cmp-pills">{auths}</div>

    <div class="cmp-countbar">
      <p class="cmp-count" id="cmpCount"></p>
      <button class="cmp-reset" id="cmpReset" type="button">
        <i class="fas fa-rotate-left"></i> Reset filters</button>
    </div>

    <div class="cmp-list" id="cmpList">{cards}</div>
    <p class="cmp-empty" id="cmpEmpty" hidden>No regulation matches that search.</p>

    <aside class="cmp-disclaimer">
      <h3>How to use this list</h3>
      <p>Each entry is a plain summary prepared for orientation, not the legal text. Limits,
         deadlines and penalties are reproduced for reference and the official instrument governs in
         every case. Which obligations apply to a particular facility depends on its activity,
         capacity and location, so confirm any reference against the published text before relying
         on it in a submission.</p>
      <a href="contact.html" class="cmp-cta">Ask which of these apply to your facility
         <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
    </aside>

  </div>
</div>

<script>
(function () {
  var search = document.getElementById('cmpSearch');
  var list   = document.getElementById('cmpList');
  var count  = document.getElementById('cmpCount');
  var empty  = document.getElementById('cmpEmpty');
  var reset  = document.getElementById('cmpReset');
  if (!list) return;

  var cards = Array.prototype.slice.call(list.querySelectorAll('.cmp-card'));
  var cat = 'all', sev = 'all', auth = 'all';

  function apply() {
    var q = (search && search.value ? search.value : '').toLowerCase().trim();
    var shown = 0;
    cards.forEach(function (c) {
      var ok = (cat === 'all' || c.getAttribute('data-cat') === cat)
            && (sev === 'all' || c.getAttribute('data-sev') === sev)
            && (auth === 'all' || c.getAttribute('data-auth') === auth)
            && (!q || c.getAttribute('data-text').indexOf(q) !== -1);
      c.hidden = !ok;
      if (ok) shown++;
    });
    count.textContent = shown + (shown === 1 ? ' regulation' : ' regulations');
    empty.hidden = shown !== 0;
  }

  function group(sel, attr, set) {
    document.querySelectorAll(sel).forEach(function (b) {
      b.addEventListener('click', function () {
        document.querySelectorAll(sel).forEach(function (x) { x.classList.remove('active'); });
        b.classList.add('active');
        set(b.getAttribute(attr));
        apply();
      });
    });
  }

  if (search) search.addEventListener('input', apply);
  group('.cmp-chip', 'data-cat', function (v) { cat = v; });
  group('.cmp-sev-btn', 'data-sev', function (v) { sev = v; });
  group('.cmp-pill', 'data-auth', function (v) { auth = v; });

  document.querySelectorAll('.cmp-more').forEach(function (b) {
    b.addEventListener('click', function () {
      var t = document.getElementById(b.getAttribute('data-target'));
      if (!t) return;
      t.hidden = !t.hidden;
      b.classList.toggle('open', !t.hidden);
    });
  });

  if (reset) reset.addEventListener('click', function () {
    cat = 'all'; sev = 'all'; auth = 'all';
    if (search) search.value = '';
    document.querySelectorAll('.cmp-chip').forEach(function (x) {
      x.classList.toggle('active', x.getAttribute('data-cat') === 'all'); });
    document.querySelectorAll('.cmp-sev-btn').forEach(function (x) {
      x.classList.toggle('active', x.getAttribute('data-sev') === 'all'); });
    document.querySelectorAll('.cmp-pill').forEach(function (x) {
      x.classList.toggle('active', x.getAttribute('data-auth') === 'all'); });
    apply();
  });

  apply();
})();
</script>
"""


def compliance():
    return (_TPL
            .replace("{stats}", _statblock())
            .replace("{chips}", _chips())
            .replace("{auths}", _authbtns())
            .replace("{cards}", _cards()))
