# The six Specialist Disciplines.

SPECIALIST = {}

def _S(slug, num, title, tagline, lede, img, fh, fr, meta,
       ptitle, pbody, ppoints, inc_title, inc, proc, app_title, app, faqs, band_quote=None):
    return dict(group="specialist", num=num, slug=slug, title=title, tagline=tagline, lede=lede,
                hero_img=img, detail_img="assets/img/svc-air-detail.jpg",
                band_img="assets/img/svc-air-lab.jpg",
                band_quote=band_quote or "Specialist work is judged on method, not on volume.",
                grid_title="What you get out of it",
                float_head=fh, float_rows=fr, meta=meta,
                problem_title=ptitle, problem_body=pbody, problem_points=ppoints,
                included_title=inc_title, included=inc, process_title="How the work runs",
                process=proc, applies_title=app_title, applies=app,
                faq_title="Common questions", faqs=faqs,
                caps=[
                    ("Scoped to the question",
                     "Specialist studies go wrong when the scope is set before the question is clear. We "
                     "agree what the study has to answer first.",
                     "assets/img/sector-1.jpg", "1st", "time through review"),
                    ("Method stated openly",
                     "Every prediction carries its method and its assumptions, because that is what a "
                     "reviewer examines rather than the conclusion.",
                     "assets/img/sector-2.jpg", "100%", "method-referenced"),
                    ("Delivered to the programme",
                     "Specialist work sits on a project critical path, so the timetable is agreed against "
                     "your milestones rather than ours.",
                     "assets/img/sector-3.jpg", "On time", "to your milestones"),
                    ("Findings you can act on",
                     "Results arrive with their implications stated, not as a technical report requiring "
                     "translation before it can be used.",
                     "assets/img/svc-air-detail.jpg", "Clear", "plain findings"),
                ])

SPECIALIST["climate-sustainability"] = _S(
    "climate-sustainability", "01", "Climate Change &amp; Sustainability",
    "From carbon accounting to credible strategy",
    "Carbon footprinting, ESG reporting and net zero planning built on measured data rather than "
    "estimates — because the numbers now get audited.",
    "assets/img/spec-climate.jpg", ("fa-leaf", "What we quantify"),
    [("Scope 1", "Direct emissions"),
     ("Scope 2", "Purchased energy"),
     ("Scope 3", "Value chain")],
    "Climate change and sustainability consulting in Saudi Arabia — carbon footprinting across Scopes 1, 2 "
    "and 3, ESG reporting, net zero roadmaps and green building certification support.",
    "Estimated numbers do not survive assurance",
    ["Carbon reporting has moved from voluntary disclosure to audited statement. Figures built on industry "
     "averages and rough conversions hold up until somebody asks for the underlying data, and then they do "
     "not.",
     "Scope 3 is where most footprints fall apart. It is usually the largest share of the total and the "
     "hardest to evidence, and a footprint that quietly omits it is not comparable with one that does not."],
    [("Boundary", "What is in and out, stated"),
     ("Data", "Measured, not benchmarked"),
     ("Method", "Which protocol is being followed"),
     ("Assurance", "Whether it will survive audit")],
    "What the work covers",
    [("Carbon footprint assessment", "Scope 1, 2 and 3 emissions quantified against a stated boundary and "
      "protocol, built from operational data rather than sector averages."),
     ("GHG inventory development", "A repeatable inventory with the data sources documented, so next year's "
      "figure is comparable with this year's."),
     ("ESG and sustainability reporting", "Disclosure prepared against the framework your stakeholders "
      "require, with the evidence behind each metric retained."),
     ("Net zero roadmaps", "Reduction pathways with costed interventions and realistic timelines, rather "
      "than a target date without a route to it."),
     ("Green building certification", "LEED, BREEAM and Mostadam support, from early design input through "
      "to submission.")],
    [("Define", "The reporting boundary and protocol are agreed before any data is collected."),
     ("Collect", "Operational data is gathered from source systems, with gaps identified honestly."),
     ("Calculate", "Emissions are quantified with factors and assumptions documented."),
     ("Report", "Findings are compiled with a reduction pathway attached.")],
    "Who needs climate and ESG work",
    [("Large industrial operators", "Energy-intensive operations face the most disclosure pressure and have "
      "the most to gain from reduction, since carbon and energy cost move together."),
     ("Companies with international customers", "Supply chain disclosure requirements increasingly flow "
      "down from multinational buyers, and a missing footprint becomes a commercial problem."),
     ("Businesses seeking finance", "Lenders and investors now ask for climate disclosure as a matter of "
      "course, and unevidenced figures attract scrutiny."),
     ("Developers and property owners", "Green building certification affects both asset value and "
      "leasability, and it is far cheaper to design for than to retrofit."),
     ("Vision 2030-aligned organisations", "National sustainability targets are increasingly reflected in "
      "procurement criteria for public and semi-public contracts."),
     ("Companies starting out", "Organisations with no baseline need one before any target means anything, "
      "and the first inventory is the hardest.")],
    [("What are Scopes 1, 2 and 3?",
      "Scope 1 is emissions you produce directly. Scope 2 is from energy you buy. Scope 3 is everything "
      "else in your value chain — usually the largest share and the hardest to quantify."),
     ("Do we have to report Scope 3?",
      "It depends on the framework and on who is asking. Increasingly yes, and a footprint that omits it is "
      "not comparable with one that includes it."),
     ("How long does a first footprint take?",
      "Weeks to months, and data availability drives it. Organisations with good energy and procurement "
      "records move much faster."),
     ("Is a net zero target realistic for us?",
      "Only if there is a costed pathway behind it. A target without interventions and timelines is a "
      "statement rather than a plan."),
     ("What is Mostadam?",
      "The Saudi green building rating system. It operates alongside LEED and BREEAM and is increasingly "
      "specified for projects in the Kingdom.")])

SPECIALIST["ecological-surveys"] = _S(
    "ecological-surveys", "02", "Ecological &amp; Biological Surveys",
    "Baseline, habitat and protected species",
    "Terrestrial and aquatic ecology surveys establishing what is present before a project proceeds — and "
    "what that means for it.",
    "assets/img/spec-ecology.jpg", ("fa-seedling", "What we survey"),
    [("Habitat", "Extent, condition, value"),
     ("Species", "Including protected status"),
     ("Seasonality", "Timed to when it is visible")],
    "Ecological and biological surveys in Saudi Arabia — habitat mapping, baseline ecology, protected "
    "species assessment and bird surveys for impact assessment and project approval.",
    "Ecology runs on the calendar, not the programme",
    ["Ecological surveys can only be done when the ecology is there to be surveyed. Breeding birds, "
     "flowering plants and migratory species each have a window, and missing it means waiting a year rather "
     "than paying more.",
     "This is why ecology so often ends up on a project's critical path. Commissioned early it is "
     "straightforward; commissioned late it delays everything behind it."],
    [("Season", "When the survey is valid"),
     ("Scope", "Which groups need assessing"),
     ("Status", "Whether anything is protected"),
     ("Mitigation", "What the finding requires")],
    "What the surveys cover",
    [("Habitat mapping and condition", "Extent, type and condition of habitats across the site, which forms "
      "the baseline every later assessment refers back to."),
     ("Protected species assessment", "Targeted survey for species with legal protection, where presence "
      "changes what a project is permitted to do."),
     ("Bird surveys", "Breeding, wintering and migratory surveys, timed to the relevant season — "
      "particularly important along migration corridors."),
     ("Aquatic and marine ecology", "Benthic, intertidal and freshwater surveys where a project affects "
      "water bodies or the coastline."),
     ("Ecological impact assessment", "Predicted effects on habitats and species, with mitigation designed "
      "against them and residual impact stated.")],
    [("Scope", "Desk study and site walkover establish which surveys are actually needed."),
     ("Time", "Surveys are scheduled into the correct seasonal windows."),
     ("Survey", "Fieldwork is carried out to recognised methodology and fully recorded."),
     ("Assess", "Findings are evaluated and mitigation designed where required.")],
    "Which projects need ecology",
    [("Coastal and marine developments", "Anything at the shoreline attracts marine and intertidal survey "
      "requirements, and habitat work is typically the longest lead item in the programme."),
     ("Large infrastructure", "Roads, pipelines and transmission corridors cross habitats, and route "
      "selection can often avoid the worst of it if the survey comes early enough."),
     ("Quarries and extraction", "Both the operational footprint and the rehabilitation plan need an "
      "ecological baseline to work from."),
     ("Renewable energy projects", "Wind and solar developments in particular attract bird and bat survey "
      "requirements, and these are seasonal."),
     ("Developments near protected areas", "Proximity to a designated area raises the assessment threshold "
      "considerably, whatever the project's own footprint."),
     ("Sites with restoration commitments", "Restoration targets need a baseline to be measured against, or "
      "there is no way to demonstrate success.")],
    [("When can ecological surveys be done?",
      "It depends on the group. Breeding birds have a defined season, and some plants are only identifiable "
      "when flowering. Surveys done outside the window are not valid."),
     ("What happens if a protected species is found?",
      "It does not necessarily stop a project, but it changes what is permitted — timing restrictions, "
      "buffer zones, mitigation or, occasionally, a design change."),
     ("How long is a survey valid?",
      "Typically one to two years depending on the receptor and how much the site has changed. Older data "
      "is commonly challenged at review."),
     ("Can desk study replace field survey?",
      "It can scope the work but rarely replaces it. Reviewers expect field data where the assessment "
      "depends on what is actually present."),
     ("When should ecology be commissioned?",
      "As early as possible. Seasonal constraints mean it is the item most likely to delay a programme if "
      "it is left late.")])

SPECIALIST["marine-environment"] = _S(
    "marine-environment", "03", "Marine Environment",
    "Coastal and offshore assessment",
    "Marine water quality, sediment, habitat and oceanographic survey for coastal development and "
    "discharge assessment along the Kingdom's shorelines.",
    "assets/img/spec-marine.jpg", ("fa-water", "What we assess"),
    [("Water column", "Quality and stratification"),
     ("Seabed", "Sediment and benthic habitat"),
     ("Dynamics", "Currents, waves, dispersion")],
    "Marine environmental services in Saudi Arabia — water and sediment sampling, benthic habitat survey, "
    "oceanographic measurement and marine dispersion modelling for coastal projects.",
    "The receiving environment decides the answer",
    ["A discharge that is unremarkable in an open, well-flushed setting can be significant in a sheltered "
     "bay with limited exchange. The same load produces different outcomes depending entirely on where it "
     "goes.",
     "That is why marine assessment needs oceanographic data rather than water quality alone. Without "
     "currents and dispersion behaviour, a prediction about where something ends up is guesswork."],
    [("Baseline", "Conditions before the project"),
     ("Hydrodynamics", "How water actually moves"),
     ("Sensitivity", "What habitats are present"),
     ("Dispersion", "Where the plume travels")],
    "What the work covers",
    [("Marine water quality", "Sampling and analysis through the water column, including stratification "
      "where thermal or saline layering affects the outcome."),
     ("Sediment sampling and analysis", "Seabed sediment characterisation and contaminant analysis, which "
      "is central to any dredging or disposal assessment."),
     ("Benthic habitat survey", "Mapping and assessment of seabed habitats including coral and seagrass, "
      "which carry the highest sensitivity in Saudi waters."),
     ("Oceanographic measurement", "Current, wave, tide and temperature measurement providing the physical "
      "data any dispersion assessment depends on."),
     ("Marine dispersion modelling", "Prediction of how discharges, thermal plumes and sediment behave once "
      "released, calibrated against measured conditions.")],
    [("Scope", "The receiving environment and the question are established first."),
     ("Measure", "Water, sediment and oceanographic data are collected over a representative period."),
     ("Model", "Dispersion and impact are predicted using the measured data."),
     ("Report", "Findings and mitigation are set out for submission.")],
    "Who needs marine assessment",
    [("Coastal developments", "Reclamation, marinas and waterfront projects change hydrodynamics as well as "
      "occupying seabed, and both effects need assessing."),
     ("Desalination plants", "Brine discharge assessment is the central environmental question for these "
      "facilities, and it depends on dispersion behaviour rather than concentration alone."),
     ("Ports and dredging", "Sediment characterisation determines disposal options, and plume modelling is "
      "normally required before dredging is approved."),
     ("Outfall discharges", "Any marine outfall requires assessment of where the discharge goes and what it "
      "reaches, particularly near sensitive habitat."),
     ("Offshore operations", "Platforms, pipelines and subsea works require baseline survey and, in many "
      "cases, ongoing monitoring."),
     ("Tourism developments", "Projects near coral and seagrass face the highest scrutiny, since these "
      "habitats are both sensitive and slow to recover.")],
    [("Why is oceanographic data needed?",
      "Because dispersion depends on how water moves. Without current and wave data, any prediction about "
      "where a discharge ends up is unsupported."),
     ("What makes coral and seagrass surveys different?",
      "They are highly sensitive and slow to recover, so assessment thresholds are lower and mitigation "
      "expectations higher than for other habitats."),
     ("How long does marine baseline work take?",
      "Longer than terrestrial, because tidal and seasonal variation has to be captured. Oceanographic "
      "deployment alone typically runs over weeks."),
     ("Is brine discharge always a problem?",
      "Not inherently. The question is the receiving environment — an open coast with strong exchange "
      "behaves very differently from a sheltered embayment."),
     ("Do we need ongoing marine monitoring?",
      "Frequently yes, where a permit requires confirmation that predicted impacts have not been "
      "exceeded.")])

SPECIALIST["remediation-rehabilitation"] = _S(
    "remediation-rehabilitation", "04", "Remediation &amp; Rehabilitation",
    "From investigation to verified closure",
    "Site investigation, remediation design and rehabilitation of contaminated and disturbed land, closed "
    "out with validation that stands up.",
    "assets/img/spec-remediation.jpg", ("fa-recycle", "The sequence"),
    [("Investigate", "Establish what is there"),
     ("Design", "Select the workable option"),
     ("Validate", "Prove it was achieved")],
    "Land remediation and site rehabilitation in Saudi Arabia — contaminated land investigation, "
    "remediation design and implementation, and quarry and extraction site rehabilitation.",
    "Remediation without validation is just earthworks",
    ["The most common failure in remediation is not technical. It is a scheme carried out without the "
     "sampling needed to demonstrate it worked, leaving the operator with cost incurred and nothing "
     "defensible to show for it.",
     "Validation has to be designed at the start, not added at the end. What gets sampled, where and "
     "against which criteria determines whether the remediation can be signed off at all."],
    [("Extent", "How far the contamination reaches"),
     ("Criteria", "What target has to be met"),
     ("Option", "What is deliverable on this site"),
     ("Validation", "The evidence of completion")],
    "What the work covers",
    [("Site investigation", "Intrusive investigation establishing the nature, extent and depth of "
      "contamination, designed around the site's history."),
     ("Risk assessment", "Whether contamination presents an actual risk given the pathways and the intended "
      "use, which determines whether remediation is required at all."),
     ("Remediation design", "Selection and design of an approach that is deliverable on the site as it "
      "stands, with target criteria stated."),
     ("Implementation oversight", "Supervision during the works so that what is delivered matches what was "
      "designed and is documented as it happens."),
     ("Validation and closure", "Post-remediation sampling demonstrating that criteria were met — the "
      "evidence that closes the liability.")],
    [("Investigate", "Extent and severity are established and the risk assessed."),
     ("Design", "A remediation approach and target criteria are selected and agreed."),
     ("Implement", "Works are carried out under supervision and documented."),
     ("Validate", "Sampling confirms the criteria were achieved and the work is closed out.")],
    "Where remediation applies",
    [("Fuel and chemical storage sites", "Tank farms and fuel stations are the most common source of "
      "hydrocarbon contamination, and leaks are frequently historical rather than current."),
     ("Former industrial land", "Redevelopment of previously industrial sites requires investigation and, "
      "often, remediation before a change of use is approved."),
     ("Quarries and extraction sites", "Rehabilitation is committed at licensing and does not expire "
      "because the site stopped producing or changed hands."),
     ("Spill and incident sites", "Response after a release determines how far the contamination travels, "
      "and early action is dramatically cheaper than late action."),
     ("Property transactions", "Buyers need to understand contamination liability before it transfers, "
      "because it is one of the few that cannot be disclaimed."),
     ("Sites under regulatory notice", "Where a regulator has required action, the remediation and its "
      "validation have to meet criteria that are usually stated explicitly.")],
    [("How do we know if remediation is needed?",
      "Investigation establishes what is present; risk assessment determines whether it matters given the "
      "pathways and intended use. Contamination does not automatically require remediation."),
     ("What remediation options exist?",
      "Excavation and disposal, in-situ treatment, containment, or monitored natural attenuation. Which is "
      "appropriate depends on the contaminant, the setting and the timeline."),
     ("How long does remediation take?",
      "Excavation can be weeks. In-situ treatment runs to months or years. Investigation determines which "
      "is realistic before anything is committed."),
     ("What is validation sampling?",
      "Post-works sampling demonstrating that target criteria were met. Without it, the remediation cannot "
      "be signed off and the liability does not close."),
     ("Does quarry rehabilitation expire?",
      "No. The commitment made at licensing survives closure, dormancy and change of ownership.")])

SPECIALIST["environmental-modelling"] = _S(
    "environmental-modelling", "05", "Environmental Modelling",
    "Prediction with the assumptions on show",
    "Dispersion, hydrological and noise modelling that quantifies impacts before they exist — with the "
    "method and assumptions stated openly.",
    "assets/img/spec-modelling.jpg", ("fa-chart-line", "What we model"),
    [("Air dispersion", "Plumes and ground concentrations"),
     ("Hydrology", "Flow, flooding, drainage"),
     ("Noise", "Propagation to receptors")],
    "Environmental modelling in Saudi Arabia — air dispersion, hydrological, noise propagation and marine "
    "dispersion modelling for impact assessment and permit applications.",
    "A model is only as good as what you tell it",
    ["Modelling output looks authoritative — contours on a map, concentrations at receptors. But the result "
     "depends entirely on the input: emission rates, meteorological data, terrain, and the assumptions "
     "chosen where data was missing.",
     "Reviewers know this, which is why they examine the inputs before the conclusions. A model presented "
     "without its assumptions is difficult to accept, however sophisticated the software behind it."],
    [("Inputs", "Emission rates and their source"),
     ("Meteorology", "Representative period, stated"),
     ("Assumptions", "Declared, not buried"),
     ("Validation", "Checked against measurement")],
    "What we model",
    [("Air dispersion modelling", "Prediction of ground-level concentrations from stack and fugitive "
      "emissions, using recognised models and site-representative meteorological data."),
     ("Odour dispersion", "Modelling of odour propagation to receptors, which is usually required where "
      "complaints have been raised or are anticipated."),
     ("Noise propagation modelling", "Prediction of noise levels at receptors from proposed plant, "
      "accounting for terrain, barriers and ground effects."),
     ("Hydrological modelling", "Surface water flow, drainage capacity and flood risk, including the effect "
      "of proposed development on existing regimes."),
     ("Marine dispersion modelling", "Discharge, thermal plume and sediment behaviour in coastal waters, "
      "calibrated against measured oceanographic data.")],
    [("Define", "The question and the receptors that matter are established."),
     ("Gather", "Emission, meteorological and terrain inputs are assembled and checked."),
     ("Model", "Predictions are run with the method and assumptions documented."),
     ("Report", "Results are presented with inputs, limitations and confidence stated.")],
    "Where modelling is required",
    [("Impact assessments", "Upper-tier EIAs usually require quantitative prediction rather than "
      "qualitative description, and modelling is how that is produced."),
     ("Permit applications", "Where a facility must demonstrate that emissions will not breach limits at "
      "receptors, modelling is the evidence."),
     ("Facility expansions", "Additional capacity changes the emission profile, and the cumulative effect "
      "has to be assessed rather than the increment alone."),
     ("Complaint investigations", "Modelling can establish whether a facility could plausibly be the source "
      "of a reported effect, which measurement alone sometimes cannot."),
     ("Site layout decisions", "Stack heights, plant positions and barrier design are far cheaper to "
      "resolve in a model than after construction."),
     ("Cumulative assessments", "Where several sources affect the same receptors, only modelling can "
      "combine them meaningfully.")],
    [("Which dispersion model do you use?",
      "The model is selected against the application and what the regulator accepts. What matters more is "
      "that the inputs are site-representative and the assumptions are declared."),
     ("What meteorological data is used?",
      "Site-representative data covering a period long enough to capture typical conditions. Using "
      "unrepresentative data is one of the most common reasons a model is challenged."),
     ("How accurate is modelling?",
      "It predicts within a stated confidence, not exactly. That is why results are presented with "
      "limitations attached rather than as certainties."),
     ("Can modelling replace monitoring?",
      "No. Modelling predicts what will happen; monitoring confirms what did. Most permits require both at "
      "different stages."),
     ("When should modelling be done?",
      "During design, while layout, stack height and plant selection can still respond to the findings.")])

SPECIALIST["laboratory-services"] = _S(
    "laboratory-services", "06", "Environmental Laboratory Services",
    "Sampling through to interpretation",
    "The full analytical chain — sampling design, collection, accredited analysis and interpretation — "
    "handled as one service rather than three.",
    "assets/img/spec-lab.jpg", ("fa-flask", "The full chain"),
    [("Design", "What to sample, and where"),
     ("Analysis", "Under accreditation"),
     ("Meaning", "What the numbers require")],
    "Environmental laboratory services in Saudi Arabia — sampling design, collection, accredited analysis "
    "and technical interpretation of water, soil, waste and air samples.",
    "Three handovers, three places to lose the thread",
    ["Splitting sampling, analysis and interpretation across different parties creates gaps at each "
     "handover. The sampler does not know what the analysis will be used for; the laboratory does not know "
     "the site; the person reading the results was involved in neither.",
     "Handled as one chain, the sampling design reflects what the interpretation will need, and the "
     "interpretation is informed by what the field team actually saw."],
    [("Continuity", "One party across the chain"),
     ("Context", "Field observations reach the analyst"),
     ("Accreditation", "Covering the whole scope"),
     ("Interpretation", "Informed by the site")],
    "What the service covers",
    [("Sampling design", "The plan that decides what the campaign can tell you — locations, frequency, "
      "technique and determinands, set against the question."),
     ("Field collection", "Sampling carried out under accreditation with chain of custody, and field "
      "observations recorded alongside."),
     ("Accredited analysis", "Laboratory analysis to referenced methods, with quality control applied "
      "before results are released."),
     ("Technical interpretation", "Results compared against applicable criteria, with exceedances, likely "
      "causes and recommended actions."),
     ("Programme continuity", "Where testing is ongoing, the same methods and locations each cycle so "
      "trends are real rather than artefacts of changed technique.")],
    [("Design", "The sampling plan is built around what the results have to answer."),
     ("Collect", "Fieldwork is carried out with custody and observations documented."),
     ("Analyse", "Analysis is completed under accreditation with QC verification."),
     ("Interpret", "Findings are reported against criteria with actions identified.")],
    "Who uses the full chain",
    [("Permitted facilities", "Ongoing compliance testing benefits most from continuity, because "
      "comparability across cycles is what makes the data meaningful."),
     ("Site investigations", "Where sampling design drives what you learn, having the same party design, "
      "collect and interpret avoids the gaps that cause re-work."),
     ("Waste classification", "Characterisation determines disposal routing, and the interpretation matters "
      "as much as the analysis."),
     ("Due diligence", "Transaction decisions rest on results, and buyers need findings rather than tables."),
     ("Incident response", "Speed matters, and a single party across the chain removes the delay at each "
      "handover."),
     ("Operations without technical staff", "Facilities with no in-house environmental capability need the "
      "interpretation most, since the numbers alone are not actionable.")],
    [("Why use one party for the whole chain?",
      "Because information is lost at each handover. The sampling design should reflect what the "
      "interpretation needs, and the interpretation should know what the field team saw."),
     ("Is the analysis accredited?",
      "Work supporting regulatory submissions is carried out under accreditation, and we confirm the scope "
      "covers your specific determinands before starting."),
     ("Can you work with samples we collected?",
      "Yes, though for regulatory submissions the sampling itself usually needs to be accredited too."),
     ("How quickly are results available?",
      "It varies by determinand — some same-day, some five days by definition, some longer for specialist "
      "organics. The schedule is set from the slowest."),
     ("Do you keep results for trend analysis?",
      "Yes, where we run the programme. Trends usually reveal a developing problem well before any single "
      "result breaches a limit.")])
