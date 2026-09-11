# The nine remaining Monitoring, Testing & Measurement services.

MONITORING = {}

def _S(slug, num, title, tagline, lede, img, fh, fr, meta,
       ptitle, pbody, ppoints, inc_title, inc, proc, app_title, app, faqs,
       band_quote=None, grid_title=None):
    return dict(group="monitoring", num=num, slug=slug, title=title, tagline=tagline, lede=lede,
                hero_img=img, detail_img="assets/img/svc-air-detail.jpg",
                band_img="assets/img/svc-air-lab.jpg",
                band_quote=band_quote or "A result is only as good as the method behind it.",
                grid_title=grid_title or "What you get out of it",
                float_head=fh, float_rows=fr, meta=meta,
                problem_title=ptitle, problem_body=pbody, problem_points=ppoints,
                included_title=inc_title, included=inc, process_title="How the work runs",
                process=proc, applies_title=app_title, applies=app,
                faq_title="Common questions", faqs=faqs,
                caps=[
                    ("Scoped against your permit",
                     "We read the conditions first and confirm the parameters, methods and frequencies that "
                     "actually apply before any scope is agreed.",
                     "assets/img/sector-1.jpg", "1st", "time through review"),
                    ("Accredited and admissible",
                     "Work is carried out under accreditation, because results from an unaccredited party are "
                     "routinely rejected at review however sound the underlying work.",
                     "assets/img/sector-2.jpg", "100%", "method-referenced"),
                    ("Reported on schedule",
                     "Fieldwork is booked against your reporting calendar so results are ready before the "
                     "submission date, not after it.",
                     "assets/img/sector-3.jpg", "On time", "every cycle"),
                    ("Interpreted, not just measured",
                     "Results arrive compared against the limits that apply to you, with exceedances and "
                     "corrective actions stated plainly.",
                     "assets/img/svc-air-detail.jpg", "Clear", "plain findings"),
                ])

MONITORING["water-wastewater-testing"] = _S(
    "water-wastewater-testing", "02", "Water &amp; Wastewater Testing",
    "Accredited analysis, defensible results",
    "Water, wastewater and effluent analysed to accredited methods, with results reported against the "
    "limits your discharge conditions set.",
    "assets/img/svc-water.jpg", ("fa-tint", "What we analyse"),
    [("Physical", "pH, TDS, turbidity, temperature"),
     ("Chemical", "COD, BOD, nutrients, metals"),
     ("Biological", "Coliforms and indicator organisms")],
    "Accredited water and wastewater testing in Saudi Arabia — physical, chemical and biological analysis "
    "of process water, effluent and receiving waters against discharge limits.",
    "Discharge limits leave no room for interpretation",
    ["A discharge condition names a parameter and a number. Either the result is under it or it is not, "
     "which makes water testing the least ambiguous of all environmental obligations — and the one where "
     "sampling error does the most damage.",
     "Most disputed results trace back to how the sample was taken rather than how it was analysed. "
     "Sampling point, timing, preservation and holding time all affect the number, and all of them are "
     "examined if a result is challenged."],
    [("Parameter", "Which determinands your consent lists"),
     ("Point", "Where the sample must be drawn"),
     ("Method", "The analytical standard referenced"),
     ("Frequency", "How often, and over what period")],
    "What the testing covers",
    [("Effluent and discharge monitoring", "Sampling and analysis at the discharge point against the limits "
      "in your consent, with flow recorded where the condition is load-based rather than concentration-based."),
     ("Process and cooling water", "Analysis of water used in the process, where quality affects both "
      "operations and the character of what is eventually discharged."),
     ("Groundwater monitoring", "Borehole sampling and analysis where a permit requires it, typically around "
      "storage areas, landfills or historically contaminated ground."),
     ("Potable and amenity water", "Testing of drinking and amenity supplies against health-based standards, "
      "including microbiological parameters."),
     ("Interpretation and reporting", "Results set against the applicable limits, with trends highlighted "
      "before they become exceedances.")],
    [("Scope", "Determinands, sampling points and frequency are confirmed against your consent."),
     ("Sample", "Samples are drawn correctly, preserved and transported under chain of custody."),
     ("Analyse", "Analysis is carried out to the referenced method under accreditation."),
     ("Report", "Results are compared against limits and issued for your periodic report.")],
    "Who needs water testing",
    [("Manufacturing", "Any facility discharging process effluent to sewer, to ground or to surface water "
      "carries testing obligations, and the parameter list follows the process rather than the volume."),
     ("Food &amp; beverage", "High organic loads mean COD, BOD and suspended solids dominate the consent, and "
      "seasonal production swings are a frequent cause of exceedance."),
     ("Power &amp; desalination", "Thermal discharge, brine and cooling water each carry separate conditions, "
      "and receiving-water monitoring is commonly required alongside."),
     ("Waste facilities", "Leachate and site drainage are monitored continuously at landfills and treatment "
      "sites, with groundwater boreholes typically forming part of the programme."),
     ("Construction", "Dewatering and site runoff need testing before discharge, and this is routinely "
      "overlooked until a discharge has already taken place."),
     ("Commercial premises", "Larger kitchens, laundries and workshops discharge to sewer under conditions "
      "that specify oils, greases and suspended solids.")],
    [("What is the difference between COD and BOD?",
      "Both measure organic load. COD is a chemical oxidation and returns a result in hours; BOD is "
      "biological and takes five days. Consents commonly specify one or the other, and they are not "
      "interchangeable."),
     ("Can we take our own samples and send them to you?",
      "For results going to a regulator, the sampling itself usually has to fall under the accreditation. "
      "Self-collected samples are useful for internal monitoring but are frequently challenged in submissions."),
     ("How quickly do samples need to reach the laboratory?",
      "It depends on the determinand. Some have holding times measured in hours, which is why transport and "
      "preservation are part of the method rather than an afterthought."),
     ("What if a result exceeds our discharge limit?",
      "Report it, establish the cause and record the corrective action. Repeat sampling to confirm is "
      "normal, but concealing the first result is not defensible."),
     ("Do we need groundwater monitoring?",
      "Only if your permit requires it — typically where there is bulk chemical or fuel storage, a landfill, "
      "or a history of contamination on the site.")],
    band_quote="A discharge limit is a number. The only question is whether your evidence is defensible.")

MONITORING["noise-monitoring"] = _S(
    "noise-monitoring", "03", "Noise Monitoring &amp; Assessment",
    "Measured against the limits that apply to you",
    "Environmental and occupational noise measured and assessed against regulated limits, with the survey "
    "designed before the meter comes out of the case.",
    "assets/img/svc-noise.jpg", ("fa-volume-up", "What we assess"),
    [("Boundary noise", "At the site perimeter"),
     ("Receptor noise", "At the nearest sensitive use"),
     ("Occupational", "Exposure inside the works")],
    "Environmental and occupational noise monitoring in Saudi Arabia — boundary and receptor surveys, "
    "occupational exposure assessment and noise impact studies against regulated limits.",
    "The survey design carries more weight than the meter",
    ["Noise results depend on when you measure, where you stand and what else was happening at the time. "
     "Two competent surveys of the same site can produce very different numbers if the design differs, "
     "which is why the method is scrutinised more closely than the instrument.",
     "Complaints complicate it further. A measurement taken after a complaint has to answer a specific "
     "question about a specific source at a specific time, and a general boundary survey rarely does that."],
    [("Position", "Boundary, receptor, or both"),
     ("Period", "Day, evening, night — each has a limit"),
     ("Duration", "Long enough to be representative"),
     ("Source", "Which noise is actually being assessed")],
    "What the survey covers",
    [("Boundary noise surveys", "Measurement at the site perimeter against the limits your permit sets, "
      "across the periods the condition specifies."),
     ("Receptor assessment", "Measurement at the nearest noise-sensitive locations, which is where a "
      "complaint will be judged rather than at your fence."),
     ("Occupational noise exposure", "Personal and area measurement inside the works, assessed against "
      "exposure limits and used to set hearing protection requirements."),
     ("Construction and blasting", "Short-term monitoring for works phases, including vibration where "
      "blasting or piling is involved."),
     ("Noise impact assessment", "Predictive modelling for new or expanding facilities, where the question "
      "is what the noise will be rather than what it is.")],
    [("Design", "Positions, periods and duration are set against the condition or the complaint."),
     ("Measure", "Calibrated instruments are deployed, with observations logged alongside the readings."),
     ("Analyse", "Results are processed, with extraneous noise identified and accounted for."),
     ("Report", "Findings are set against the applicable limits with the method fully stated.")],
    "Who needs noise monitoring",
    [("Manufacturing", "Boundary limits apply to most permitted facilities, and occupational exposure "
      "assessment is a separate obligation covering the workforce inside."),
     ("Quarries &amp; mining", "Blasting brings vibration and airblast alongside conventional noise, and "
      "these sites tend to be the most complaint-exposed of all."),
     ("Construction", "Works-phase limits are usually tied to a management plan, with monitoring triggered "
      "by proximity to residential areas."),
     ("Power generation", "Continuous plant noise is assessed at night, which is when the limits are "
      "tightest and complaints are most likely."),
     ("Commercial premises", "Plant, generators and delivery activity at commercial sites generate most of "
      "the noise complaints that reach municipalities."),
     ("Facilities facing a complaint", "A complaint changes the question from compliance to attribution, "
      "and the survey has to be designed for that specifically.")],
    [("What is the difference between boundary and receptor monitoring?",
      "Boundary measures at your perimeter; receptor measures where people actually are. Your permit "
      "usually specifies one, but a complaint will be judged at the receptor."),
     ("How long does a noise survey take?",
      "Assessment against day, evening and night limits requires coverage of all three, so a representative "
      "survey normally runs over at least one full day-night cycle."),
     ("Is environmental noise the same as occupational noise?",
      "No. They use different metrics, different limits and different instruments. A facility usually has "
      "obligations under both."),
     ("What if a neighbour complains?",
      "The survey has to isolate your contribution from background and other sources. That is a different "
      "design from routine compliance monitoring."),
     ("Can noise be predicted before we build?",
      "Yes, through modelling. That is normally part of the impact assessment, and it is far cheaper to "
      "change a layout on paper than to mitigate after commissioning.")])

MONITORING["soil-sediment-testing"] = _S(
    "soil-sediment-testing", "04", "Soil &amp; Sediment Testing",
    "Characteristics and contaminants, established",
    "Soil and sediment sampled and analysed to establish what is present, at what concentration, and what "
    "it means for the site.",
    "assets/img/svc-soil.jpg", ("fa-mountain", "What we establish"),
    [("Contaminants", "Metals, hydrocarbons, organics"),
     ("Characteristics", "pH, texture, organic content"),
     ("Extent", "Depth and lateral spread")],
    "Soil and sediment testing in Saudi Arabia — contamination assessment, geotechnical characterisation "
    "and sediment analysis for site investigation, due diligence and remediation planning.",
    "The sampling plan determines the answer",
    ["Contamination is rarely uniform. A plan that samples in the wrong places produces a clean result on a "
     "contaminated site, or an alarming one on a site that is broadly fine. The number of points, their "
     "positions and their depths decide what you learn.",
     "This matters most in transactions. Buyers who accept a thin investigation regularly inherit "
     "liabilities far larger than any discount they negotiated, and the cost of finding out later is "
     "measured in remediation rather than survey fees."],
    [("Strategy", "Targeted or systematic, and why"),
     ("Depth", "Surface, profile, or to groundwater"),
     ("Determinands", "What the site history suggests"),
     ("Comparison", "Which assessment criteria apply")],
    "What the investigation covers",
    [("Contaminated land assessment", "Sampling and analysis to establish whether contamination is present, "
      "what it is and how far it extends, designed around the site's history."),
     ("Due diligence investigation", "Pre-transaction assessment so that liability is understood before it "
      "transfers with the asset."),
     ("Sediment analysis", "Analysis of marine, coastal and watercourse sediments where dredging, discharge "
      "or coastal works are involved."),
     ("Agricultural and soil quality", "Characterisation for agricultural and landscaping purposes, where "
      "the question is suitability rather than contamination."),
     ("Remediation support", "Validation sampling during and after remediation, which is the evidence that "
      "the work achieved what it set out to.")],
    [("Review", "Site history and previous use are reviewed to target the investigation."),
     ("Plan", "Sampling positions, depths and determinands are set against that history."),
     ("Sample", "Fieldwork is carried out under chain of custody, with logs kept for every point."),
     ("Assess", "Results are compared against the applicable criteria and the implications set out.")],
    "Who needs soil testing",
    [("Industrial facilities", "Storage areas, process zones and historical spill locations are the usual "
      "focus, and a permit condition sometimes requires periodic investigation."),
     ("Property transactions", "Buyers and lenders increasingly require environmental due diligence, and "
      "contamination is one of the few liabilities that cannot be walked away from."),
     ("Fuel and chemical storage", "Tank farms and fuel stations carry a recognised risk of hydrocarbon "
      "contamination, and leaks are frequently historical rather than current."),
     ("Quarries &amp; extraction", "Soil characterisation supports the rehabilitation plan, and stripped "
      "topsoil has to be assessed before reinstatement."),
     ("Construction", "Ground conditions are established before works begin, both for contamination and for "
      "disposal classification of arisings."),
     ("Remediation projects", "Validation sampling is what closes a remediation out, and without it the "
      "work is difficult to demonstrate.")],
    [("How many samples does a site need?",
      "It depends on the site area, its history and what you are trying to establish. A targeted "
      "investigation of known risk areas differs entirely from a systematic grid across a whole site."),
     ("What contaminants do you test for?",
      "The site's history determines the list. Fuel storage points to hydrocarbons; metalworking to metals; "
      "an unknown industrial history usually justifies a broad initial screen."),
     ("How deep do you sample?",
      "Depth follows the suspected source and pathway. Surface contamination and a leaking underground tank "
      "call for very different profiles."),
     ("What if contamination is found?",
      "The result establishes what is present and where. Whether remediation is required depends on the "
      "concentration, the pathway and the intended use of the site."),
     ("Is soil testing required for a property purchase?",
      "It is not always mandatory, but it is increasingly expected by lenders and is the only reliable way "
      "to understand what you are acquiring.")])

MONITORING["field-monitoring"] = _S(
    "field-monitoring", "05", "Field Monitoring &amp; Measurement",
    "Precise on-site parameters",
    "In-situ measurement of environmental parameters where the reading has to be taken at the source "
    "rather than in a laboratory.",
    "assets/img/svc-field.jpg", ("fa-satellite-dish", "Measured in place"),
    [("Continuous", "Logged over time"),
     ("Spot readings", "At defined points"),
     ("Meteorological", "Recorded alongside")],
    "Field environmental monitoring in Saudi Arabia — in-situ measurement, data logging and meteorological "
    "recording for parameters that must be measured at source.",
    "Some parameters cannot survive the journey",
    ["Dissolved oxygen, pH, temperature and conductivity change between the sampling point and the "
     "laboratory bench. For these, the measurement has to happen in the field, which puts the burden on "
     "calibration and technique rather than on laboratory conditions.",
     "Continuous logging raises a different question: what the data means. A month of readings is only "
     "useful if the deployment was designed around a question, and if the meteorological context needed to "
     "interpret it was recorded at the same time."],
    [("In-situ", "Parameters that change on transport"),
     ("Calibration", "Verified before and after"),
     ("Context", "Met data logged alongside"),
     ("Duration", "Long enough to be representative")],
    "What field monitoring covers",
    [("In-situ water parameters", "Dissolved oxygen, pH, conductivity, temperature and turbidity measured "
      "at the point of interest with calibrated field instruments."),
      ("Continuous data logging", "Deployed loggers recording over days or months where a single reading "
      "would not answer the question."),
     ("Meteorological measurement", "Wind speed and direction, temperature, humidity and pressure recorded "
      "alongside other parameters so results can be interpreted."),
     ("Flow and discharge measurement", "Flow rates at discharge points, needed wherever a condition is "
      "expressed as a load rather than a concentration."),
     ("Rapid site screening", "Field screening to establish where more detailed investigation should focus, "
      "before committing to laboratory work.")],
    [("Define", "The question the deployment has to answer is set out first."),
     ("Calibrate", "Instruments are calibrated and the calibration is recorded."),
     ("Deploy", "Measurement or logging is carried out, with observations logged."),
     ("Interpret", "Data is processed and set in context rather than handed over raw.")],
    "Where field measurement applies",
    [("Discharge monitoring", "In-situ parameters are measured at the discharge point alongside samples "
      "taken for laboratory analysis, because several determinands cannot wait."),
     ("Receiving waters", "Upstream and downstream measurement establishes what effect a discharge is "
      "actually having, which a single point cannot show."),
     ("Construction dewatering", "Water pumped from excavations needs checking before discharge, and the "
      "quality changes as the works progress."),
     ("Baseline surveys", "Impact assessments need field data over a representative period before the "
      "project exists."),
     ("Incident response", "When something has gone into the ground or water, rapid field measurement "
      "establishes the extent while it still matters."),
     ("Process troubleshooting", "Measurement at points through a treatment process identifies where "
      "performance is being lost.")],
    [("Why measure in the field rather than the laboratory?",
      "Several parameters change between sampling and analysis. Dissolved oxygen and pH in particular are "
      "not reliable once a sample has travelled."),
     ("How long should a logger be deployed?",
      "Long enough to capture the variation that matters — operational cycles, tidal cycles or weather "
      "patterns depending on what is being assessed."),
     ("Do you record weather data as well?",
      "Where it affects interpretation, yes. Air quality and noise results in particular are difficult to "
      "defend without the meteorological context."),
     ("Can field results be used for compliance reporting?",
      "Yes, provided the instruments are calibrated and the method matches what the condition references."),
     ("What happens if equipment fails mid-deployment?",
      "Gaps are identified and the affected period is re-run. A dataset with an unexplained gap is a "
      "problem at review, so it is better to repeat it.")])

MONITORING["environmental-sampling"] = _S(
    "environmental-sampling", "06", "Environmental Sampling",
    "Chain-of-custody from point to laboratory",
    "Collection, preservation and transfer of environmental samples under documented chain of custody, "
    "so the result is defensible.",
    "assets/img/svc-sampling.jpg", ("fa-vial", "What the chain records"),
    [("Collection", "Who, when, where, how"),
     ("Preservation", "Method and holding time"),
     ("Transfer", "Every handover, signed")],
    "Environmental sampling services in Saudi Arabia — sampling plans, collection, preservation and "
    "chain-of-custody transfer for air, water, soil and waste analysis.",
    "The result is only as strong as the chain behind it",
    ["Laboratory analysis is rarely what gets challenged. The sample is. Where it was taken, when, by whom, "
     "how it was preserved and who handled it before it reached the bench — that is what a reviewer or an "
     "opposing expert examines.",
     "A break anywhere in that chain undermines the number at the end of it, however good the analysis. "
     "This is why sampling is treated as a documented procedure rather than a task."],
    [("Plan", "Where and how many, decided in advance"),
     ("Technique", "Matched to the determinand"),
     ("Preservation", "Correct container, correct treatment"),
     ("Custody", "Documented at every handover")],
    "What the service covers",
    [("Sampling plan design", "Locations, frequency, technique and determinands set out before fieldwork, "
      "so the campaign answers the question it was commissioned for."),
     ("Water and effluent sampling", "Grab, composite and flow-proportional sampling as the condition "
      "requires, with preservation applied at the point of collection."),
     ("Soil and waste sampling", "Representative sampling of solid matrices, including waste "
      "characterisation sampling for classification."),
     ("Air and stack sampling", "Collection onto appropriate media for laboratory analysis, with the "
      "sampling train documented."),
     ("Chain of custody", "Documented transfer from collection to laboratory receipt, which is the record "
      "that makes the result defensible.")],
    [("Plan", "The sampling design is set against the question and the applicable method."),
     ("Collect", "Samples are taken using the correct technique, container and preservation."),
     ("Transfer", "Custody documentation follows the sample to the laboratory."),
     ("Verify", "Receipt condition and holding times are checked and recorded.")],
    "Who needs formal sampling",
    [("Permitted facilities", "Any sample supporting a compliance submission needs a defensible chain, "
      "because the submission can be challenged years later."),
     ("Waste generators", "Characterisation sampling determines waste classification, and the whole permit "
      "file rests on that classification being right."),
     ("Site investigations", "Contamination results drive remediation decisions and transaction values, so "
      "the sampling record is examined closely."),
     ("Legal and insurance matters", "Where a result may be disputed, the chain of custody is often "
      "examined before the analysis is."),
     ("Due diligence", "Buyers rely on sampling results to price risk, and a weak chain undermines the "
      "whole assessment."),
     ("Incident investigation", "Samples taken after a spill or release establish what happened, and the "
      "documentation has to withstand scrutiny.")],
    [("What is chain of custody?",
      "A documented record of everyone who handled a sample between collection and analysis, with times and "
      "signatures. It is what demonstrates the sample was not compromised."),
     ("Can our own staff take samples?",
      "For internal monitoring, yes. For results submitted to a regulator, the sampling usually has to fall "
      "under accreditation, and self-collected samples are commonly challenged."),
     ("What is the difference between grab and composite sampling?",
      "A grab sample captures one moment; a composite blends over a period or across flow. Which is "
      "appropriate depends on what your condition specifies."),
     ("How many samples do we need?",
      "Enough to be representative of what you are assessing. That is a design question, and it should be "
      "settled before anyone goes on site."),
     ("What if a sample exceeds its holding time?",
      "The result is not defensible and the sample should be retaken. Holding times are part of the method, "
      "not a guideline.")])

MONITORING["monitoring-programmes"] = _S(
    "monitoring-programmes", "07", "Environmental Monitoring Programmes",
    "Scheduled, tracked, reported",
    "Ongoing monitoring run as a programme rather than a series of one-off jobs — scheduled against your "
    "obligations and tracked to completion.",
    "assets/img/svc-programme.jpg", ("fa-calendar-alt", "Programme covers"),
    [("Schedule", "Built from your conditions"),
     ("Tracking", "Every cycle logged"),
     ("Reporting", "Filed against the deadline")],
    "Ongoing environmental monitoring programmes for Saudi facilities — scheduled sampling, tracked "
    "completion and periodic reporting managed as a single service.",
    "One-off jobs create the gaps",
    ["Facilities that commission monitoring job by job are the ones that develop gaps in the record. A "
     "quarter gets missed because nobody owned the calendar, and it surfaces two years later at renewal "
     "review when there is no way to fill it.",
     "A programme removes the decision. The schedule comes from the permit, the fieldwork is booked against "
     "it in advance, and the reporting follows automatically. The facility stops having to remember."],
    [("Ownership", "One party responsible for the calendar"),
     ("Lead time", "Booked before the deadline, not after"),
     ("Continuity", "Same methods, comparable results"),
     ("Evidence", "A complete, auditable record")],
    "What a programme includes",
    [("Obligations mapping", "Every monitoring condition in your permit turned into a dated schedule, so "
      "nothing depends on institutional memory."),
     ("Scheduled fieldwork", "Campaigns booked in advance against that schedule, with seasonal requirements "
      "planned around rather than discovered."),
     ("Consistent methodology", "The same methods and locations each cycle, so results are comparable and "
      "trends mean something."),
     ("Register maintenance", "Results filed to your environmental register as they are produced rather "
      "than assembled later."),
     ("Periodic reporting", "Reports compiled and submitted on the required cycle, from a record that was "
      "maintained throughout.")],
    [("Map", "Permit conditions are turned into a monitoring calendar."),
     ("Schedule", "Fieldwork is booked against the calendar with lead time built in."),
     ("Execute", "Each cycle is carried out, logged and filed."),
     ("Report", "Periodic submissions are prepared and filed on time.")],
    "Who benefits from a programme",
    [("Multi-parameter facilities", "Where air, water, noise and waste all carry separate frequencies, "
      "coordinating them centrally is the difference between a complete record and a patchy one."),
     ("Facilities approaching renewal", "Renewal examines the whole term, so a programme started now still "
      "improves the position that will be reviewed."),
     ("Multi-site operators", "Consistency across sites matters, because an inspection at one prompts "
      "questions about the others."),
     ("Facilities with a compliance history", "Where there has been a finding, a documented programme is "
      "often the corrective action the regulator expects to see."),
     ("Operations without an environmental function", "Facilities with no dedicated environmental staff are "
      "the most exposed to gaps, and the most helped by outsourcing the calendar."),
     ("Sites with seasonal requirements", "Where a parameter needs seasonal coverage, missing the window "
      "means waiting a year, so forward planning is the whole game.")],
    [("How is a programme different from one-off monitoring?",
      "Ownership of the calendar. A programme means somebody is responsible for the schedule being met, "
      "rather than each cycle depending on someone remembering to commission it."),
     ("Can you take over an existing programme?",
      "Yes. We audit the historical record first, because gaps and method inconsistencies in past data are "
      "what surface at renewal."),
     ("What if our process changes mid-programme?",
      "The schedule is revised. A new line or a capacity increase can change both the parameters and their "
      "frequency, and the programme has to reflect that."),
     ("Do you handle the reporting as well?",
      "Yes. Monitoring and reporting in one service is the point — it is the handover between the two where "
      "cycles usually get lost."),
     ("What happens if a result is out of limit?",
      "You are told immediately rather than at report stage, so the corrective action can begin and be "
      "documented alongside the exceedance.")])

MONITORING["laboratory-analysis"] = _S(
    "laboratory-analysis", "08", "Laboratory Analysis &amp; Data Interpretation",
    "Results with the meaning attached",
    "Accredited laboratory analysis, reported with the interpretation that turns a column of numbers into "
    "a decision.",
    "assets/img/svc-lab.jpg", ("fa-microscope", "Analysis covers"),
    [("Water &amp; effluent", "Physical, chemical, biological"),
     ("Soil &amp; waste", "Contaminants and classification"),
     ("Air samples", "Collected media analysis")],
    "Accredited environmental laboratory analysis in Saudi Arabia — water, soil, waste and air sample "
    "analysis with technical interpretation against regulatory limits.",
    "A results table is not a finding",
    ["Most laboratory reports hand over a table and leave the reader to work out what it means. For a "
     "facility that has to act on the result, that is the least useful half of the job.",
     "What matters is which numbers breached which limit, what the likely cause was, whether the trend is "
     "moving in the wrong direction, and what should happen next. That requires someone who understands "
     "both the analysis and the regulatory context it sits in."],
    [("Accreditation", "Which scope the method sits under"),
     ("Limits", "Which criteria apply to you"),
     ("Trend", "Where the numbers are heading"),
     ("Action", "What the result requires you to do")],
    "What the service covers",
    [("Water and effluent analysis", "Physical, chemical and microbiological determinands analysed to "
      "accredited methods against your discharge conditions."),
     ("Soil and waste analysis", "Contaminant screening and waste classification analysis, including the "
      "determinands that decide disposal routing."),
     ("Air sample analysis", "Laboratory analysis of media collected during sampling campaigns, reported "
      "with the field conditions attached."),
     ("Data interpretation", "Results compared against applicable criteria, with exceedances, likely causes "
      "and recommended actions stated."),
     ("Trend analysis", "Results tracked across cycles so a drift toward a limit is visible before it "
      "becomes an exceedance.")],
    [("Receive", "Samples are checked on receipt against custody records and holding times."),
     ("Analyse", "Analysis is carried out to the referenced method under accreditation."),
     ("Verify", "Quality control checks are applied before any result is released."),
     ("Interpret", "Results are set against the applicable limits and reported with findings.")],
    "Who uses laboratory analysis",
    [("Permitted facilities", "Compliance monitoring generates a continuous stream of samples, and the "
      "interpretation is what makes the data useful rather than merely filed."),
     ("Waste producers", "Classification analysis determines disposal routing, and getting it wrong is "
      "both a compliance and a cost problem."),
     ("Site investigations", "Contamination assessment depends on analysis, and the interpretation drives "
      "remediation decisions worth far more than the testing."),
     ("Process operators", "Analysis through a treatment process shows where performance is being lost, "
      "which routine compliance sampling alone will not reveal."),
     ("Due diligence", "Transaction decisions rest on analytical results, and the interpretation is what "
      "the buyer is actually paying for."),
     ("Incident response", "Rapid analysis after a release establishes extent and severity while the "
      "response can still be adjusted.")],
    [("Is your analysis accredited?",
      "Work supporting regulatory submissions is carried out under accreditation. We confirm the scope "
      "covering your specific determinands before work begins."),
     ("How long do results take?",
      "It varies by determinand. Some are same-day; BOD takes five days by definition; specialist organics "
      "take longer. The reporting schedule is set from the slowest determinand."),
     ("Can you analyse samples we collected ourselves?",
      "Yes, though for regulatory submissions the sampling itself usually needs to fall under accreditation "
      "as well, and self-collected samples are frequently challenged."),
     ("What does interpretation add?",
      "It tells you which results matter, why, and what to do. A table of numbers without that leaves the "
      "hardest part of the job with you."),
     ("Do you track results over time?",
      "Yes, where we run the programme. Trends are frequently more useful than any single result, because "
      "they show a problem before the limit is breached.")])

MONITORING["pollution-control-equipment"] = _S(
    "pollution-control-equipment", "09", "Monitoring &amp; Pollution Control Equipment",
    "Supply, installation and operation",
    "Environmental monitoring instruments and pollution control equipment supplied, installed and kept "
    "producing data that is actually usable.",
    "assets/img/svc-equipment.jpg", ("fa-tools", "What we supply"),
    [("Monitoring", "Fixed and portable instruments"),
     ("Control", "Abatement and treatment plant"),
     ("Support", "Calibration and maintenance")],
    "Environmental monitoring instruments and pollution control equipment in Saudi Arabia — supply, "
    "installation, calibration and ongoing operational support.",
    "Equipment that nobody calibrates produces data nobody can use",
    ["An instrument installed and then forgotten generates readings, but not defensible ones. Drift is "
     "invisible until a calibration check reveals it, and by then the whole intervening dataset is in "
     "question.",
     "The same applies to abatement plant. A scrubber or filter that is not maintained continues to run "
     "while its performance falls away, and the first sign is usually a failed compliance test rather than "
     "a maintenance alert."],
    [("Specification", "Matched to the parameter and range"),
     ("Installation", "Sited to the method, not convenience"),
     ("Calibration", "Scheduled and recorded"),
     ("Maintenance", "Before performance falls, not after")],
    "What we supply and support",
    [("Fixed monitoring instruments", "Continuous monitors for air, water and noise, specified against the "
      "parameters and ranges your conditions require."),
     ("Portable instruments", "Field instruments for spot measurement and survey work, supplied with "
      "calibration and training."),
     ("Pollution control plant", "Abatement and treatment equipment specified against the emission or "
      "discharge limit it has to achieve."),
     ("Installation and commissioning", "Siting to the requirements of the method, with commissioning "
      "records that form part of your compliance evidence."),
     ("Calibration and maintenance", "Scheduled servicing and calibration, recorded so the data the "
      "instrument produced remains defensible.")],
    [("Specify", "Equipment is selected against the parameter, range and method required."),
     ("Install", "Siting and commissioning follow the method, and are documented."),
     ("Calibrate", "Calibration is carried out and recorded before operational use."),
     ("Maintain", "Servicing runs on a schedule so performance does not drift unnoticed.")],
    "Who needs equipment support",
    [("Facilities with continuous monitoring", "Permits requiring continuous data depend entirely on the "
      "instrument being maintained, because a drift invalidates the whole period."),
     ("Sites with abatement plant", "Scrubbers, filters and treatment systems have to keep achieving the "
      "limit they were specified for, not merely keep running."),
     ("Operations doing their own monitoring", "In-house monitoring is viable, but only with calibrated "
      "instruments and a documented calibration record."),
     ("New installations", "Equipment specified before commissioning avoids the far more expensive problem "
      "of retrofitting after a failed compliance test."),
     ("Facilities after an exceedance", "Where a limit was breached, equipment performance is one of the "
      "first things examined and often the first thing to fix."),
     ("Remote sites", "Unattended installations need a maintenance regime precisely because nobody is there "
      "to notice a fault.")],
    [("Do we need our own monitoring equipment?",
      "Only where your permit requires continuous monitoring. Periodic obligations are usually better met "
      "through campaigns than through owned instruments."),
     ("How often does equipment need calibrating?",
      "The method and the manufacturer set the interval. What matters is that it is scheduled and recorded, "
      "because uncalibrated data is not defensible."),
     ("Can you maintain equipment we already have?",
      "Yes. We assess the existing installation first, since siting and configuration problems are common "
      "and affect every result the instrument produces."),
     ("What happens if an instrument fails?",
      "The affected period is identified and, where possible, covered by alternative measurement. An "
      "undeclared gap is a worse position than a declared one."),
     ("Do you supply abatement as well as monitoring?",
      "Yes, specified against the limit it has to achieve rather than against a generic performance "
      "figure.")])

MONITORING["reporting-compliance"] = _S(
    "reporting-compliance", "10", "Environmental Reporting &amp; Compliance",
    "The record, kept ready",
    "Compliance reporting and record-keeping managed as an ongoing service, so submissions are prepared "
    "from a maintained record rather than assembled under deadline.",
    "assets/img/svc-reporting.jpg", ("fa-file-alt", "What we maintain"),
    [("Register", "Current and complete"),
     ("Reports", "Filed every cycle"),
     ("Evidence", "Retrievable on request")],
    "Environmental reporting and compliance management for Saudi facilities — register maintenance, "
    "periodic reporting, exceedance documentation and inspection readiness.",
    "Inspections are documentary before they are technical",
    ["An inspection starts with paperwork. Register, reports, manifests, calibration records — whether "
     "those are complete decides the tone of everything that follows, long before anyone walks the site.",
     "Facilities that maintain the record continuously find inspections uneventful. Facilities that "
     "assemble it on request find that the gaps they had forgotten are the first thing noticed."],
    [("Continuous", "Maintained, not reconstructed"),
     ("Consistent", "Register matches submissions"),
     ("Complete", "No unexplained periods"),
     ("Ready", "Producible without notice")],
    "What the service covers",
    [("Register maintenance", "Results, manifests, inventories and incident records filed as they occur, "
      "against a structure matched to your permit conditions."),
     ("Periodic report preparation", "Each reporting cycle compiled from that record and submitted against "
      "the deadline the condition sets."),
     ("Exceedance documentation", "Where a limit was breached, the cause and corrective action recorded "
      "alongside it — which is what changes an exceedance from a finding into a handled event."),
     ("Inspection support", "Preparation before an inspection and support during it, so requests are "
      "answered from the record rather than from memory."),
     ("Renewal preparation", "The compliance record audited ahead of renewal, so gaps are found while there "
      "is still time to address them.")],
    [("Audit", "The existing record is reviewed and gaps identified."),
     ("Structure", "The register is organised against your actual conditions."),
     ("Maintain", "Records are filed on a defined cadence as events occur."),
     ("Report", "Submissions are prepared and filed on schedule, and evidenced.")],
    "Who needs reporting support",
    [("Permitted facilities", "Reporting and register conditions apply to nearly every permit, and they are "
      "the obligations most often allowed to slip because nothing happens immediately."),
     ("Facilities without environmental staff", "Where no one owns the calendar, cycles get missed. That is "
      "the single most common cause of a poor compliance record."),
     ("Operations approaching renewal", "Renewal examines the whole term. Auditing the record now is the "
      "only way to address a gap before it is reviewed."),
     ("Facilities after an inspection finding", "Findings usually require documented corrective action and "
      "often additional reporting until closed out."),
     ("Multi-site operators", "Coordinating reporting across sites prevents one site's late submission "
      "drawing scrutiny onto the rest."),
     ("Facilities changing ownership", "Buyers inherit the compliance record, and the register is the main "
      "evidence of what is being taken on.")],
    [("What does the register have to contain?",
      "Your conditions define it, but in practice monitoring results, waste manifests, chemical inventory, "
      "incident records, training records and regulator correspondence."),
     ("How often do we have to report?",
      "The frequency is set by your permit, and different parameters within one permit can carry different "
      "frequencies."),
     ("What if we have gaps in our historical record?",
      "Identify and document them before an inspector does. A disclosed gap with an explanation is far "
      "better than one discovered during review."),
     ("Can you support us during an inspection?",
      "Yes. Preparation beforehand matters more, but having someone who knows the record present during "
      "the inspection helps considerably."),
     ("What happens at renewal?",
      "The reviewer examines the compliance record across the whole permit term — reporting timeliness, "
      "exceedances and how they were handled, and whether the register is complete.")])
