# Content for the six Compliance & Permitting service pages.
# Factual about KSA environmental regulation. No claims about BluePrint's
# history, clients, project count or scale.

PERMITTING = {}

PERMITTING["environmental-permit"] = dict(
    group="permitting", num="01", slug="environmental-permit",
    title="Environmental Permit",
    tagline="From classification to issuance",
    lede="The NCEC environmental permit that stands between your activity and a valid licence — "
         "classified correctly, filed completely, and carried through review.",
    hero_img="assets/img/svc-permit.jpg",
    float_head=("fa-file-signature", "What the file contains"),
    float_rows=[
                ("3", "Permit categories", "Classification decides the scope"),
                ("6+", "Documents required", "Before a file is accepted"),
                ("1", "Review cycle", "If the classification is right")
    ],
    float2=("fa-stamp", "NCEC aligned", "Filed to the current framework"),
    meta="NCEC environmental permit applications in Saudi Arabia — activity classification, supporting "
         "studies, technical documentation and coordination with the regulator through to issuance.",
    problem_title="Most delays are not technical",
    problem_body=[
        "In our experience the applications that stall are rarely the ones with a difficult process behind "
        "them. They are the ones where the activity was classified into the wrong category, or where a "
        "supporting study the category required was simply not commissioned.",
        "Classification follows the activity itself — the process, its capacity, the waste streams it "
        "generates and the sensitivity of the site. It does not follow company size or floor area, which "
        "is the assumption that most often puts a file into the wrong tier.",
    ],
    problem_points=[("Category", "Which tier the activity actually falls into"),
                    ("Studies", "What the tier obliges you to submit"),
                    ("Evidence", "Process, capacity and emissions, documented"),
                    ("Timeline", "Review cycles, and what triggers another one")],
    included_title="What the application involves",
    included=[
        ("Activity classification", "We establish the correct category before anything is quoted, because it "
         "determines the entire scope and cost of what follows."),
        ("Technical documentation", "Process description, production capacity, raw materials, emissions points "
         "and waste streams, prepared in the structure reviewers expect."),
        ("Supporting studies", "Whichever studies the category requires — impact assessment, waste "
         "characterisation, baseline measurement — scoped to the activity rather than over-specified."),
        ("Submission and follow-up", "The file is submitted and tracked, and reviewer queries are answered "
         "directly rather than passed back to you to interpret."),
        ("Conditions handover", "When the permit issues we walk you through its conditions, because those "
         "conditions become your reporting obligations from that day."),
    ],
    process_title="From first call to issued permit",
    process=[("Classify", "A short scoping conversation about your activity, capacity and location places you "
                          "in the right category."),
             ("Prepare", "Technical documentation and any required studies are produced together, so the file "
                         "is internally consistent."),
             ("Submit", "The application is filed and tracked, with queries answered as they arise."),
             ("Hand over", "The issued permit is explained condition by condition, with the reporting calendar "
                           "it creates.")],
    applies_title="Who needs an environmental permit",
    applies=[
        ("Industrial facilities", "Any manufacturing or processing activity on the scheduled list needs a permit "
         "before it operates. The category depends on the process and its capacity, not the size of the company, "
         "so small facilities running certain processes can find themselves in a higher tier than they expect."),
        ("Workshops &amp; small premises", "Garages, paint shops, metalworking and similar premises usually sit in "
         "the simplified tier, but a permit is still a precondition. Most owners discover the requirement when a "
         "municipal or commercial licence renewal is blocked rather than at the point of opening."),
        ("Healthcare &amp; veterinary", "Clinics, laboratories and veterinary practices generate regulated waste "
         "streams from the day they open, and are inspected against them. The permit and the waste obligations "
         "are usually handled as one exercise."),
        ("Construction &amp; infrastructure", "Projects above defined thresholds require environmental approval "
         "before works begin, with impacts assessed at the design stage rather than after mobilisation."),
        ("Quarries &amp; extraction", "Extraction activities sit in the upper tier and require full impact "
         "assessment together with a rehabilitation commitment that outlives the working life of the site."),
        ("Commercial &amp; services", "Warehousing, food service and larger retail operations fall into the "
         "simplified route, but the permit remains a condition of the commercial registration."),
    ],
    grid_title="What you get out of it",
    caps=[
        ("Reviewed before you commit",
         "We read the conditions and tell you what actually applies before any scope is agreed, so you are "
         "not paying for work the regulator never asked for.",
         "assets/img/sector-1.jpg", "1st", "time through review"),
        ("Defensible documentation",
         "Everything is produced to the standard the condition references, with the method and evidence "
         "recorded alongside the result.",
         "assets/img/sector-2.jpg", "100%", "method-referenced"),
        ("Nothing filed at the last minute",
         "Work is scheduled against your obligations so the deadline is met from a maintained record "
         "rather than a scramble.",
         "assets/img/sector-3.jpg", "On time", "every cycle"),
        ("One accountable team",
         "The people who scoped the work carry it through submission and answer the reviewer's questions "
         "directly.",
         "assets/img/svc-air-detail.jpg", "Single", "point of contact"),
    ],
    faqs=[
        ("How do I know which category my activity is in?",
         "Classification follows the activity, its capacity, its waste streams and the sensitivity of the site. "
         "Some activities are assigned a category by name regardless of scale. We establish this before quoting."),
        ("How long does a permit application take?",
         "Simplified applications with complete documentation clear review in weeks. Upper-tier applications "
         "requiring impact assessment and baseline data run to months, most of which is study time rather than "
         "review time."),
        ("What happens if my application is rejected?",
         "Rejections are usually classification or completeness issues rather than refusals in principle. The "
         "file is corrected and resubmitted, but a review cycle has been lost — which is the argument for "
         "getting the classification right first."),
        ("Do I need a permit if I already have a commercial licence?",
         "Yes. They are separate instruments, and the environmental permit is frequently a precondition for "
         "renewing the commercial one."),
        ("What happens after the permit is issued?",
         "The conditions become live obligations: an environmental register to maintain, periodic reports to "
         "file and, in most cases, monitoring to carry out. Renewal review examines that record."),
    ],
)

PERMITTING["environmental-impact-assessment"] = dict(
    group="permitting", num="02", slug="environmental-impact-assessment",
    title="Environmental Impact Assessment",
    tagline="Answering the questions reviewers actually ask",
    lede="EIA and ESIA studies for projects where the environmental approval decides whether the "
         "project proceeds at all.",
    hero_img="assets/img/svc-eia.jpg",
    float_head=("fa-clipboard-check", "What an EIA covers"),
    float_rows=[
                ("4", "Study stages", "Scope, baseline, assess, report"),
                ("12", "Months typical", "Where seasonal baseline applies"),
                ("1", "Approval", "Required before works begin")
    ],
    float2=("fa-clipboard-check", "EIA &amp; ESIA", "Environmental and social scope"),
    meta="Environmental and social impact assessment (EIA/ESIA) in Saudi Arabia — baseline surveys, "
         "impact prediction, modelling, mitigation design and stakeholder engagement for regulated projects.",
    problem_title="An assessment is an argument, not a description",
    problem_body=[
        "A weak EIA describes the environment and describes the project, then asserts that the impact is "
        "acceptable. A strong one predicts specific impacts, quantifies them against a baseline the reviewer "
        "can check, and shows how each will be controlled and verified.",
        "The difference matters because reviewers examine the reasoning, not the page count. Studies are "
        "returned for gaps in the logic far more often than for missing data.",
    ],
    problem_points=[("Baseline", "Measured conditions, not assumed ones"),
                    ("Prediction", "Quantified impacts with stated method"),
                    ("Mitigation", "Specific measures, not intentions"),
                    ("Monitoring", "How the mitigation will be proved")],
    included_title="What the study contains",
    included=[
        ("Scoping", "Which impacts genuinely need assessment for this project, agreed early so effort is not "
         "spent on questions the reviewer will not ask."),
        ("Baseline surveys", "Field measurement of the parameters the assessment will rely on — air, noise, "
         "water, soil, ecology — before the project exists."),
        ("Impact prediction and modelling", "Dispersion, hydrological, noise or marine modelling where the "
         "impact needs quantifying rather than describing."),
        ("Mitigation design", "Measures specified in enough detail to be built and verified, with residual "
         "impact stated honestly after mitigation."),
        ("Environmental management plan", "The mitigation turned into an operating document, with monitoring, "
         "responsibilities and reporting attached."),
    ],
    process_title="How an assessment runs",
    process=[("Scope", "The assessment boundary and the impacts requiring study are set and agreed."),
             ("Baseline", "Field surveys establish existing conditions, timed to capture seasonal variation "
                          "where it matters."),
             ("Assess", "Impacts are predicted and modelled, and mitigation is designed against them."),
             ("Report", "The study is compiled, submitted and defended through review.")],
    applies_title="Projects requiring impact assessment",
    applies=[
        ("Heavy industry", "Petrochemicals, cement, metals and chemicals sit in the upper tier by activity type "
         "and require full assessment, usually with dispersion modelling of air emissions and a detailed "
         "mitigation and monitoring programme."),
        ("Power &amp; desalination", "Thermal and desalination plant carry air, marine and thermal discharge "
         "impacts that generally need quantitative modelling rather than qualitative description."),
        ("Quarries &amp; mining", "Extraction requires assessment of dust, noise, vibration, groundwater and "
         "landscape, together with the rehabilitation commitment that follows the site to closure."),
        ("Major infrastructure", "Roads, ports and large developments are assessed at the design stage, where "
         "alignment and layout can still be changed in response to the findings."),
        ("Coastal &amp; marine projects", "Anything at the shoreline attracts marine ecology and water quality "
         "assessment, and habitat surveys are typically the long pole in the programme."),
        ("Waste facilities", "Treatment, landfill and recycling facilities are assessed for emissions, leachate, "
         "odour and groundwater, with the containment design central to the argument."),
    ],
    grid_title="What you get out of it",
    caps=[
        ("Reviewed before you commit",
         "We read the conditions and tell you what actually applies before any scope is agreed, so you are "
         "not paying for work the regulator never asked for.",
         "assets/img/sector-1.jpg", "1st", "time through review"),
        ("Defensible documentation",
         "Everything is produced to the standard the condition references, with the method and evidence "
         "recorded alongside the result.",
         "assets/img/sector-2.jpg", "100%", "method-referenced"),
        ("Nothing filed at the last minute",
         "Work is scheduled against your obligations so the deadline is met from a maintained record "
         "rather than a scramble.",
         "assets/img/sector-3.jpg", "On time", "every cycle"),
        ("One accountable team",
         "The people who scoped the work carry it through submission and answer the reviewer's questions "
         "directly.",
         "assets/img/svc-air-detail.jpg", "Single", "point of contact"),
    ],
    faqs=[
        ("Does my project need a full EIA or a simplified study?",
         "That follows the activity category. Upper-tier activities require full assessment; middle-tier "
         "projects often need a targeted study addressing specific impacts rather than a complete EIA."),
        ("How long does an EIA take?",
         "Months rather than weeks, and baseline surveys drive the timeline. Where seasonal coverage is "
         "required, that alone can set the programme."),
        ("Can the assessment be done after construction starts?",
         "No. Environmental approval is a precondition for works. Retrospective assessment carries penalties "
         "and a considerably harder review."),
        ("What is the difference between EIA and ESIA?",
         "ESIA adds social impact — communities, livelihoods, land use — to the environmental scope. Lenders "
         "and international partners commonly require it even where the regulator does not."),
        ("What if the assessment finds an unacceptable impact?",
         "Better found in the study than after construction. In most cases the answer is a design change or "
         "additional mitigation; identifying it early is the entire purpose of the exercise."),
    ],
)

PERMITTING["waste-management-permit"] = dict(
    group="permitting", num="03", slug="waste-management-permit",
    title="Waste Management Permit",
    tagline="MWAN permits for generators, carriers and treaters",
    lede="Waste characterisation, procedures and permit files for facilities that generate, transport, "
         "store or treat waste in the Kingdom.",
    hero_img="assets/img/svc-waste.jpg",
    float_head=("fa-recycle", "Who needs one"),
    float_rows=[
                ("100%", "Streams characterised", "Before the file is prepared"),
                ("5", "Core documents", "Characterisation to response plan"),
                ("0", "Duty transferred", "Generator obligations stay with you")
    ],
    float2=("fa-recycle", "MWAN framework", "Generators, carriers, treaters"),
    meta="MWAN waste management permits in Saudi Arabia — waste characterisation studies, storage and "
         "handling procedures, manifesting systems and permit applications for generators, carriers and treaters.",
    problem_title="Outsourcing collection does not transfer the obligation",
    problem_body=[
        "The most common misunderstanding we encounter is the belief that contracting a licensed carrier "
        "discharges the duty. It does not. Generator obligations — characterisation, manifesting, "
        "record-keeping — remain with the facility that produced the waste.",
        "The second is classification. The most frequent rejection reason we see is a mismatch between the "
        "declared waste classification and what the facility actually produces. Everything else in the file "
        "is built on that characterisation, so an error there invalidates the rest.",
    ],
    problem_points=[("Characterisation", "What the waste actually is"),
                    ("Storage", "Segregation, containment, duration"),
                    ("Transfer", "Licensed carriers and manifests"),
                    ("Records", "Evidence the chain held")],
    included_title="What the permit file requires",
    included=[
        ("Waste characterisation study", "Analysis and classification of every stream the facility produces, "
         "which is the foundation the rest of the application rests on."),
        ("Storage and handling procedures", "Documented arrangements aligned with MWAN technical guidance — "
         "segregation, containment, labelling and duration limits."),
        ("Contractor verification", "Confirmation that every carrier and treatment facility you use holds "
         "current authorisation for the classes you transfer."),
        ("Manifesting and records", "A manifest and record-keeping system that produces the evidence an "
         "inspection asks for, rather than a folder assembled afterwards."),
        ("Emergency response plan", "Response arrangements proportionate to the waste classes held on site."),
    ],
    process_title="How a waste permit is prepared",
    process=[("Characterise", "Waste streams are identified, sampled where necessary and classified."),
             ("Document", "Storage, handling and transfer procedures are written against the classification."),
             ("Verify", "Carrier and treatment facility authorisations are checked and evidenced."),
             ("Submit", "The file is filed with MWAN and carried through review and any site inspection.")],
    applies_title="Who needs a waste management permit",
    applies=[
        ("Manufacturing", "Industrial waste beyond household quantities triggers generator obligations, and "
         "hazardous streams raise the requirement substantially. Facilities often discover streams they had "
         "not declared once characterisation is done properly."),
        ("Healthcare &amp; veterinary", "Medical and veterinary waste carries the strictest handling rules in "
         "the Kingdom. Clinics are inspected against them from the day they open, and the permit is normally "
         "handled together with the environmental permit."),
        ("Waste contractors", "Transporters, sorting facilities, recyclers and treatment operators need permits "
         "for the classes they handle, and their clients depend on that authorisation remaining current."),
        ("Construction", "Demolition and construction waste requires segregation and licensed disposal, and "
         "site-generated hazardous streams are frequently overlooked in the planning."),
        ("Oil, gas &amp; petrochemicals", "Sludges, spent catalysts, contaminated soils and chemical residues "
         "each carry their own classification and disposal route, and cannot be handled as a single stream."),
        ("Commercial premises", "Larger commercial and food service operations generate regulated streams "
         "including waste oils and packaging, which fall under the permit regime above defined thresholds."),
    ],
    grid_title="What you get out of it",
    caps=[
        ("Reviewed before you commit",
         "We read the conditions and tell you what actually applies before any scope is agreed, so you are "
         "not paying for work the regulator never asked for.",
         "assets/img/sector-1.jpg", "1st", "time through review"),
        ("Defensible documentation",
         "Everything is produced to the standard the condition references, with the method and evidence "
         "recorded alongside the result.",
         "assets/img/sector-2.jpg", "100%", "method-referenced"),
        ("Nothing filed at the last minute",
         "Work is scheduled against your obligations so the deadline is met from a maintained record "
         "rather than a scramble.",
         "assets/img/sector-3.jpg", "On time", "every cycle"),
        ("One accountable team",
         "The people who scoped the work carry it through submission and answer the reviewer's questions "
         "directly.",
         "assets/img/svc-air-detail.jpg", "Single", "point of contact"),
    ],
    faqs=[
        ("We use a licensed contractor — do we still need a permit?",
         "Almost certainly yes. Generator duties stay with you: characterising the waste, manifesting "
         "transfers and keeping records. The contractor's licence covers the contractor's activity, not yours."),
        ("What is a waste characterisation study?",
         "Identification and classification of every stream you produce, with laboratory analysis where the "
         "classification is not obvious. It determines your storage, transfer and disposal obligations."),
        ("How long does a permit take?",
         "Straightforward applications with complete documentation clear in weeks. Complex facilities with "
         "hazardous streams or on-site treatment take longer, plus time for any site inspection."),
        ("What if we start producing a new waste stream?",
         "It must be characterised and declared. Producing a stream not covered by your permit is a "
         "violation, and it is a common inspection finding."),
        ("Do permits need renewing?",
         "Yes, and renewal review examines your compliance history — manifest gaps, late reports and "
         "unresolved findings all surface at that point."),
    ],
)

PERMITTING["environmental-management-plan"] = dict(
    group="permitting", num="04", slug="environmental-management-plan",
    title="Environmental Management Plan",
    tagline="Permit conditions turned into daily practice",
    lede="The document that translates what your permit requires into what your site actually does — "
         "with named roles, defined controls and a monitoring schedule.",
    hero_img="assets/img/svc-emp.jpg",
    float_head=("fa-tasks", "What an EMP fixes"),
    float_rows=[
                ("1", "Document", "Short enough to actually be used"),
                ("12", "Month review", "Minimum, or on any process change"),
                ("0", "Named individuals", "Roles assigned by position")
    ],
    float2=("fa-tasks", "Inspection ready", "The controls, evidenced"),
    meta="Environmental management plans for Saudi facilities — turning permit conditions into documented "
         "controls, named responsibilities, monitoring schedules and emergency response arrangements.",
    problem_title="The plan that nobody follows",
    problem_body=[
        "An EMP written to satisfy a permit condition and then filed is one of the most common findings we "
        "see at inspection. Site staff cannot describe the controls it specifies, and the roles it names "
        "belong to people who have since left.",
        "A plan that works is short enough to be read, tied to positions rather than individuals, and built "
        "into induction and refresher training. That is a different document from one written purely to "
        "close out a condition.",
    ],
    problem_points=[("Usable", "Short enough that staff actually read it"),
                    ("Assigned", "Tied to roles, not named individuals"),
                    ("Trained", "Built into induction and refreshers"),
                    ("Live", "Reviewed when the process changes")],
    included_title="What the plan sets out",
    included=[
        ("Obligations register", "Every condition your permit imposes, extracted and listed, so nothing is "
         "carried only in someone's memory."),
        ("Operational controls", "The specific measures for each impact — emissions, discharges, waste, "
         "noise, storage — described at the level of what a supervisor does."),
        ("Roles and responsibilities", "Assigned by position rather than by name, so the plan survives staff "
         "turnover."),
        ("Monitoring and inspection schedule", "What is measured or checked, how often, by whom, and where "
         "the result is recorded."),
        ("Emergency response", "Spill, release and incident procedures proportionate to what the site "
         "actually holds."),
    ],
    process_title="How the plan is built",
    process=[("Extract", "Permit conditions are turned into a plain register of obligations."),
             ("Walk the site", "Controls are designed against how the site actually operates, not how the "
                               "process diagram says it does."),
             ("Write", "The plan is drafted to be usable — short, specific and assigned."),
             ("Embed", "Training and the reporting calendar are set up so the plan stays live.")],
    applies_title="Where an EMP is required",
    applies=[
        ("Permitted industrial facilities", "Most environmental permits above the simplified tier require an "
         "EMP as a condition, and inspectors ask to see it alongside the register."),
        ("Construction projects", "A construction EMP covers the works phase, where impacts are temporary but "
         "intensive and controls depend entirely on crews following them."),
        ("Waste facilities", "Handling, storage and treatment operations need documented controls for each "
         "waste class, and the plan is examined closely at inspection."),
        ("Quarries &amp; extraction", "Operational controls run alongside the rehabilitation commitment, and "
         "the plan usually carries both."),
        ("Facilities after an inspection finding", "Where a finding relates to control or documentation, a "
         "revised EMP is frequently the corrective action the regulator expects."),
        ("Sites with changed processes", "A new line, a new solvent or an increase in capacity changes the "
         "controls required, and the plan has to change with it."),
    ],
    grid_title="What you get out of it",
    caps=[
        ("Reviewed before you commit",
         "We read the conditions and tell you what actually applies before any scope is agreed, so you are "
         "not paying for work the regulator never asked for.",
         "assets/img/sector-1.jpg", "1st", "time through review"),
        ("Defensible documentation",
         "Everything is produced to the standard the condition references, with the method and evidence "
         "recorded alongside the result.",
         "assets/img/sector-2.jpg", "100%", "method-referenced"),
        ("Nothing filed at the last minute",
         "Work is scheduled against your obligations so the deadline is met from a maintained record "
         "rather than a scramble.",
         "assets/img/sector-3.jpg", "On time", "every cycle"),
        ("One accountable team",
         "The people who scoped the work carry it through submission and answer the reviewer's questions "
         "directly.",
         "assets/img/svc-air-detail.jpg", "Single", "point of contact"),
    ],
    faqs=[
        ("Is an EMP the same as an EIA?",
         "No. The EIA predicts impacts before a project proceeds. The EMP is how you control them once you "
         "are operating, and it usually derives from the mitigation the EIA set out."),
        ("How long should an EMP be?",
         "Short enough that site staff read it. A plan running to hundreds of pages usually indicates it was "
         "written for the file rather than for the site."),
        ("How often should it be reviewed?",
         "Annually at minimum, and immediately whenever the process, capacity or waste streams change."),
        ("Who should own the plan?",
         "A named position with the authority to act on it. Plans owned by an external consultant with no "
         "site presence tend not to be followed."),
        ("What does an inspector look for?",
         "Whether the controls described are actually happening, whether staff can describe them, and whether "
         "the monitoring schedule has been kept."),
    ],
)

PERMITTING["environmental-register"] = dict(
    group="permitting", num="05", slug="environmental-register",
    title="Environmental Register",
    tagline="Proof you were compliant every day since",
    lede="The record an inspector asks for first — maintained continuously rather than assembled the "
         "week before it is needed.",
    hero_img="assets/img/svc-register.jpg",
    float_head=("fa-folder-open", "What the register holds"),
    float_rows=[
                ("1st", "Document requested", "At almost every inspection"),
                ("100%", "Period coverage", "Gaps read as non-compliance"),
                ("0", "Reconstruction", "Maintained, not assembled")
    ],
    float2=("fa-folder-open", "Audit ready", "Produced on request"),
    meta="Environmental register setup and maintenance for Saudi facilities — monitoring results, waste "
         "manifests, chemical inventories, incident records and permit correspondence, kept audit-ready.",
    problem_title="The first document requested, and the least maintained",
    problem_body=[
        "The register is where an inspection starts, because it is the fastest way to establish whether a "
        "facility has been compliant continuously or only recently. Gaps in it are read as gaps in "
        "compliance, whether or not that is fair.",
        "The common failures are mundane: monitoring results sitting in an inbox rather than the register, "
        "manifests missing for a period when someone was on leave, and a chemical inventory that no longer "
        "matches what is on site.",
    ],
    problem_points=[("Complete", "No gaps in any period"),
                    ("Current", "Updated as events happen"),
                    ("Consistent", "Matches your submitted reports"),
                    ("Retrievable", "Produced on request, not reconstructed")],
    included_title="What we set up and maintain",
    included=[
        ("Register structure", "A structure matched to your permit conditions, so every obligation has a "
         "place where its evidence lives."),
        ("Monitoring results", "Every measurement filed on receipt, with the method and location recorded "
         "alongside the number."),
        ("Waste records", "Manifests, transfer notes and contractor authorisations kept as a continuous "
         "chain rather than a pile."),
        ("Chemical and materials inventory", "What is held on site, in what quantity, kept current as "
         "materials change."),
        ("Incidents and corrective actions", "What happened, what was done and what evidence closes it — the "
         "part inspectors examine most closely."),
    ],
    process_title="How the register is kept",
    process=[("Audit", "The existing record is reviewed first, because historical gaps are what surface at "
                       "renewal."),
             ("Structure", "The register is organised against your actual permit conditions."),
             ("Populate", "Existing records are filed and gaps are identified and, where possible, closed."),
             ("Maintain", "New results and events are filed as they occur, on a defined cadence.")],
    applies_title="Who has to keep a register",
    applies=[
        ("Permitted facilities", "Register maintenance is a standard permit condition, and it is the first "
         "thing requested at inspection. Facilities without one rarely pass the documentary stage."),
        ("Waste generators", "Manifest and transfer records form the core of the register for any facility "
         "producing regulated waste, and gaps here are among the most common findings."),
        ("Facilities approaching renewal", "Renewal review examines the record across the whole permit term, "
         "so a register assembled in the final month is transparently that."),
        ("Multi-site operators", "Consistency across sites matters, because an inspection at one site "
         "frequently prompts questions about the others."),
        ("Facilities after a finding", "Where an inspection identified a documentation gap, a properly "
         "structured register is usually the corrective action required."),
        ("Facilities changing ownership", "Buyers inherit the compliance record along with the asset, and "
         "the register is the primary evidence of what they are taking on."),
    ],
    grid_title="What you get out of it",
    caps=[
        ("Reviewed before you commit",
         "We read the conditions and tell you what actually applies before any scope is agreed, so you are "
         "not paying for work the regulator never asked for.",
         "assets/img/sector-1.jpg", "1st", "time through review"),
        ("Defensible documentation",
         "Everything is produced to the standard the condition references, with the method and evidence "
         "recorded alongside the result.",
         "assets/img/sector-2.jpg", "100%", "method-referenced"),
        ("Nothing filed at the last minute",
         "Work is scheduled against your obligations so the deadline is met from a maintained record "
         "rather than a scramble.",
         "assets/img/sector-3.jpg", "On time", "every cycle"),
        ("One accountable team",
         "The people who scoped the work carry it through submission and answer the reviewer's questions "
         "directly.",
         "assets/img/svc-air-detail.jpg", "Single", "point of contact"),
    ],
    faqs=[
        ("What has to be in the register?",
         "Your permit conditions define it, but in practice: monitoring results, waste manifests, chemical "
         "inventory, incident records, training records and correspondence with the regulator."),
        ("Can it be electronic?",
         "Yes, and it is easier to maintain and search. What matters is that it is complete, current and can "
         "be produced when asked."),
        ("How far back does it need to go?",
         "Retention is set by your permit conditions, but renewal review looks across the whole term — so "
         "the practical answer is the full permit period."),
        ("What if there are gaps in our historical record?",
         "Better to identify and document them before an inspector does. A disclosed gap with an explanation "
         "is a far better position than one discovered during review."),
        ("Who should maintain it?",
         "A named position on site, with a defined filing cadence. Registers that depend on someone "
         "remembering tend to develop exactly the gaps that cause problems."),
    ],
)

PERMITTING["periodic-environmental-report"] = dict(
    group="permitting", num="06", slug="periodic-environmental-report",
    title="Periodic Environmental Report",
    tagline="The obligation most facilities let slip",
    lede="Scheduled regulatory reporting prepared from a maintained record — filed on time, every cycle, "
         "in the form the regulator expects.",
    hero_img="assets/img/svc-report.jpg",
    float_head=("fa-calendar-check", "Every cycle needs"),
    float_rows=[
                ("1", "Missed cycle", "Is enough to surface at renewal"),
                ("100%", "On-time filing", "The target, every cycle"),
                ("3", "Report elements", "Results, exceedances, changes")
    ],
    float2=("fa-calendar-check", "Never late", "Calendar built from conditions"),
    meta="Periodic environmental reporting for Saudi facilities — compiling monitoring results, exceedances "
         "and corrective actions into the regulatory reports your permit conditions require.",
    problem_title="A missed cycle does not stay missed",
    problem_body=[
        "Late or missing periodic reports are the most frequent finding we encounter, by a wide margin. "
        "They are also the easiest to verify — an inspector can check submission dates in minutes, which is "
        "precisely why it is checked first.",
        "The consequence arrives later. Renewal review examines the reporting record across the entire "
        "permit term, so a cycle missed two years ago surfaces at exactly the point when there is no time "
        "left to explain it.",
    ],
    problem_points=[("Schedule", "Built from the permit, not from memory"),
                    ("Data", "Measurements timed to be ready"),
                    ("Interpretation", "Results read against the limits"),
                    ("Submission", "Filed, and the filing evidenced")],
    included_title="What each report covers",
    included=[
        ("Reporting calendar", "Built directly from your permit conditions, with the measurements each cycle "
         "depends on scheduled far enough ahead to be ready."),
        ("Results compilation", "Monitoring data assembled and compared against the limits that apply to your "
         "activity, with the method and location stated."),
        ("Exceedance reporting", "Where a limit was exceeded, the report states it, gives the likely cause "
         "and records the corrective action taken."),
        ("Operational changes", "Any change to process, capacity or waste streams during the period, declared "
         "rather than left to surface at renewal."),
        ("Submission and evidence", "The report is filed and the submission evidenced, so the record itself "
         "is defensible."),
    ],
    process_title="How a reporting cycle runs",
    process=[("Schedule", "The calendar is set from your conditions, and monitoring is booked against it."),
             ("Collect", "Results arrive and are filed to the register as they are produced."),
             ("Compile", "Data is assembled, compared against limits and interpreted."),
             ("Submit", "The report is filed on time and the submission recorded.")],
    applies_title="Who has periodic reporting obligations",
    applies=[
        ("Permitted industrial facilities", "Nearly every permit above the simplified tier carries a reporting "
         "frequency. It is the condition most often overlooked because nothing happens immediately when a "
         "cycle is missed."),
        ("Waste facilities", "Generators, carriers and treatment operators report on volumes, classifications "
         "and transfers, and the figures must reconcile with the manifests in the register."),
        ("Power &amp; desalination", "Continuous monitoring obligations generate substantial data volumes, so "
         "the reporting workflow matters as much as the measurement."),
        ("Facilities under a condition", "Where an inspection produced a finding, additional or more frequent "
         "reporting is a common requirement until the issue is closed."),
        ("Quarries &amp; extraction", "Operational reporting continues alongside rehabilitation progress, and "
         "both are examined at renewal."),
        ("Multi-site operators", "Coordinating cycles across sites avoids the situation where one site's late "
         "submission draws attention to the rest."),
    ],
    grid_title="What you get out of it",
    caps=[
        ("Reviewed before you commit",
         "We read the conditions and tell you what actually applies before any scope is agreed, so you are "
         "not paying for work the regulator never asked for.",
         "assets/img/sector-1.jpg", "1st", "time through review"),
        ("Defensible documentation",
         "Everything is produced to the standard the condition references, with the method and evidence "
         "recorded alongside the result.",
         "assets/img/sector-2.jpg", "100%", "method-referenced"),
        ("Nothing filed at the last minute",
         "Work is scheduled against your obligations so the deadline is met from a maintained record "
         "rather than a scramble.",
         "assets/img/sector-3.jpg", "On time", "every cycle"),
        ("One accountable team",
         "The people who scoped the work carry it through submission and answer the reviewer's questions "
         "directly.",
         "assets/img/svc-air-detail.jpg", "Single", "point of contact"),
    ],
    faqs=[
        ("How often do we have to report?",
         "Your permit conditions state the frequency. It varies by activity and category, and different "
         "parameters within one permit can carry different frequencies."),
        ("What happens if we miss a cycle?",
         "It becomes part of your compliance record and surfaces at renewal review. Repeated gaps are treated "
         "considerably more seriously than a single late submission with an explanation."),
        ("What if a result exceeds a limit?",
         "Report it, with the cause and the corrective action. An exceedance with a documented response is a "
         "much stronger position than an exceedance that appears to have gone unnoticed."),
        ("Can you take over reporting from another provider?",
         "Yes. We audit the existing record first, because gaps in previous cycles are what cause problems "
         "later, and they are better identified now."),
        ("Does reporting continue if the site is idle?",
         "Usually yes. A facility that has stopped producing has not ceased to be permitted, and obligations "
         "continue until the permit is formally surrendered."),
    ],
)
