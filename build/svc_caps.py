# Per-service capability items. Replaces the shared block so no two pages
# carry the same four statements.
# Each entry: (title, one-sentence body, badge, badge_sub)

CAPS = {

"environmental-permit": [
 ("Classified before it is quoted", "The category is established first, because it decides the scope, the studies and the cost of everything that follows.", "1st", "step, every time"),
 ("A file that holds together", "Process description, capacity and emissions are prepared as one set, so the reviewer does not find internal contradictions.", "One", "consistent file"),
 ("Queries answered directly", "Reviewer questions come to us and are answered from the file, rather than being forwarded to you to interpret.", "Direct", "to the reviewer"),
 ("Conditions explained on issue", "When the permit arrives you get a walkthrough of what it now obliges you to do, not just the certificate.", "Day 1", "obligations clear")],

"environmental-impact-assessment": [
 ("Scoped to what will be asked", "Effort goes into the impacts a reviewer will actually question, not into padding the document.", "Focused", "scope agreed early"),
 ("Baseline you can defend", "Predictions rest on measured field data, because assumed baselines are the first thing challenged.", "Measured", "not assumed"),
 ("Method stated openly", "Every prediction carries its methodology and assumptions, since that is what review examines.", "100%", "method stated"),
 ("Mitigation that can be built", "Measures are specified in enough detail to be constructed and verified, with residual impact stated honestly.", "Buildable", "not aspirational")],

"waste-management-permit": [
 ("Characterisation done properly", "Every stream is identified and classified first, because the whole file rests on that being right.", "All", "streams declared"),
 ("Contractors verified", "Carrier and treatment authorisations are checked and evidenced, not assumed from an invoice.", "Checked", "not assumed"),
 ("Records that survive inspection", "The manifest system is set up to produce evidence on request rather than be reconstructed afterwards.", "Audit", "ready"),
 ("Gaps closed before filing", "Storage and containment shortfalls are identified and closed before an inspector finds them.", "Before", "not after")],

"environmental-management-plan": [
 ("Short enough to be read", "A plan nobody opens controls nothing, so it is written for the supervisor rather than the file.", "Usable", "on site"),
 ("Assigned to roles", "Responsibilities attach to positions, so the plan survives the people who wrote it leaving.", "Roles", "not names"),
 ("Built from a site walk", "Controls are designed against how the site actually runs, not how the process diagram says it does.", "Real", "operations"),
 ("Kept alive", "Training and review are set up so the plan changes when the process does.", "Live", "document")],

"environmental-register": [
 ("Audited before it is built", "The existing record is reviewed first, because historical gaps are what surface at renewal.", "History", "checked first"),
 ("Structured to your conditions", "Every obligation has a defined place where its evidence lives, so nothing is held only in memory.", "1:1", "with conditions"),
 ("Filed as it happens", "Results and events are recorded on a cadence, not gathered when someone asks.", "Continuous", "not retrospective"),
 ("Producible without notice", "The register can be handed over during an inspection rather than prepared for one.", "On", "request")],

"periodic-environmental-report": [
 ("Calendar built from the permit", "The schedule comes from your conditions, so no cycle depends on anyone remembering it.", "Every", "cycle mapped"),
 ("Monitoring booked ahead", "Fieldwork is scheduled with lead time, so data is ready before the deadline rather than after.", "Ahead", "of deadline"),
 ("Exceedances handled, not hidden", "Where a limit was breached, the cause and corrective action are recorded alongside it.", "Documented", "response"),
 ("Submission evidenced", "The filing itself is recorded, because the reporting record is what renewal review examines.", "Proof", "of filing")],

"air-quality-monitoring": [
 ("Parameters confirmed first", "We read the conditions and confirm which pollutants, methods and frequencies actually apply before quoting.", "4", "things checked"),
 ("Points chosen to the standard", "Boundary, receptor and stack positions follow the method rather than site convenience.", "Method", "led siting"),
 ("Meteorology recorded alongside", "Results without wind and weather context are difficult to defend, so both are captured together.", "Context", "captured"),
 ("Exceedances flagged immediately", "You hear about a breach when it happens, not when the report lands weeks later.", "Same", "day alert")],

"water-wastewater-testing": [
 ("Sampling technique matched", "Grab, composite or flow-proportional is chosen against your consent, since the wrong one invalidates the result.", "Correct", "by condition"),
 ("Preservation at the point", "Samples are preserved where they are taken, because holding time is part of the method.", "In", "holding time"),
 ("Accredited analysis", "Determinands are analysed under accreditation, which is what makes the result admissible.", "Accredited", "scope confirmed"),
 ("Trends flagged early", "A drift toward a limit is visible in the data long before it becomes an exceedance.", "Early", "warning")],

"noise-monitoring": [
 ("Survey designed first", "Positions, periods and duration are set before fieldwork, because the design decides the number.", "Design", "before meter"),
 ("All periods covered", "Day, evening and night carry different limits, so a representative survey covers each.", "3", "periods assessed"),
 ("Extraneous noise identified", "Observations are logged during measurement so other sources can be separated from yours.", "Sources", "separated"),
 ("Complaints answered specifically", "Where there has been a complaint, the survey is designed to answer that question, not a general one.", "Targeted", "to the issue")],

"soil-sediment-testing": [
 ("History drives the plan", "Previous site use determines where we sample and what we look for, rather than a generic grid.", "Targeted", "by history"),
 ("Depth matched to the source", "Surface contamination and a leaking tank need very different sampling profiles.", "Profiled", "by risk"),
 ("Every point logged", "Position, depth and conditions are recorded for each sample, which is what makes the result defensible.", "All", "points logged"),
 ("Implications stated", "Results arrive with what they mean for the site and its intended use, not just concentrations.", "Findings", "not tables")],

"field-monitoring": [
 ("Calibrated before and after", "Calibration is verified at both ends of the deployment, so drift cannot invalidate the dataset unnoticed.", "2x", "verification"),
 ("Deployed to a question", "Loggers are placed to answer something specific rather than to accumulate data.", "Purpose", "led"),
 ("Context captured", "Meteorological and operational conditions are recorded alongside, because readings alone rarely explain themselves.", "Context", "logged"),
 ("Gaps re-run, not explained away", "Where equipment failed, the affected period is repeated rather than presented with a footnote.", "Complete", "datasets")],

"environmental-sampling": [
 ("Plan agreed in advance", "Locations, technique and determinands are settled before anyone goes on site.", "Planned", "not improvised"),
 ("Correct container and preservation", "Each determinand has its own requirements, and getting them wrong invalidates the sample.", "Per", "determinand"),
 ("Custody documented throughout", "Every handover is recorded, because that chain is what a challenge examines first.", "Unbroken", "chain"),
 ("Holding times respected", "Samples reach the laboratory inside their window, which is part of the method rather than a target.", "Within", "holding time")],

"monitoring-programmes": [
 ("One party owns the calendar", "Responsibility for the schedule sits in one place, which is what stops cycles being missed.", "Single", "owner"),
 ("Seasonal windows planned around", "Where a parameter needs a season, it is booked a year out rather than discovered too late.", "Planned", "a year out"),
 ("Methods held constant", "The same methods and locations each cycle, so trends are real rather than artefacts of changed technique.", "Comparable", "across cycles"),
 ("Record maintained as it goes", "Results reach the register when produced, so reporting is compilation rather than reconstruction.", "Filed", "on receipt")],

"laboratory-analysis": [
 ("QC before release", "Quality control checks are applied before any result leaves the laboratory.", "Verified", "before release"),
 ("Compared against your limits", "Results arrive set against the criteria that apply to you, not as an unreferenced table.", "Against", "your criteria"),
 ("Cause identified", "Where a result is out of limit, the likely cause is stated rather than left as an exercise.", "Cause", "stated"),
 ("Tracked across cycles", "Results are held so a developing trend is visible before any single result breaches.", "Trend", "visible")],

"pollution-control-equipment": [
 ("Specified to the requirement", "Instruments are selected against the parameter, range and method your conditions reference.", "Matched", "to method"),
 ("Sited to the standard", "Installation position follows the method rather than what is convenient to reach.", "Method", "led siting"),
 ("Calibration scheduled", "Servicing runs on a schedule and is recorded, because uncalibrated data is not defensible.", "Scheduled", "not reactive"),
 ("Performance checked, not assumed", "Abatement plant is verified against the limit it was specified to achieve, not merely observed running.", "Verified", "performance")],

"reporting-compliance": [
 ("Record audited first", "The existing compliance history is reviewed before anything else, because that is what renewal examines.", "History", "reviewed"),
 ("Register matched to conditions", "The structure mirrors your permit, so every obligation has a place where its evidence sits.", "1:1", "with conditions"),
 ("Filed on cadence", "Records are maintained continuously rather than assembled when an inspector asks.", "Continuous", "maintenance"),
 ("Ready without notice", "An inspection can be answered from the record as it stands, with no preparation period required.", "Inspection", "ready")],

"climate-sustainability": [
 ("Boundary fixed first", "What is in and out of scope is agreed before data collection, because it determines everything after.", "Defined", "boundary"),
 ("Operational data, not averages", "Figures are built from your own records, since benchmarked numbers do not survive assurance.", "Measured", "not benchmarked"),
 ("Assumptions documented", "Every factor and assumption is recorded, so next year's figure is comparable with this year's.", "Repeatable", "inventory"),
 ("Pathway, not just a target", "Reduction routes are costed with timelines attached, rather than a date without a plan behind it.", "Costed", "pathway")],

"ecological-surveys": [
 ("Seasonal windows respected", "Surveys are scheduled when the ecology is actually present, because outside the window they are not valid.", "In", "season"),
 ("Scoped by desk study first", "A walkover and records search establish which surveys are genuinely needed before any are commissioned.", "Scoped", "before survey"),
 ("Recognised methodology", "Fieldwork follows established method, since reviewers examine how a survey was done before what it found.", "Standard", "methods"),
 ("Commissioned early", "Ecology is the item most likely to delay a programme, so we flag the windows at the outset.", "Off", "critical path")],

"marine-environment": [
 ("Hydrodynamics measured", "Current and wave data underpin any dispersion prediction, so they are collected rather than assumed.", "Measured", "not modelled blind"),
 ("Representative period", "Tidal and seasonal variation is captured, because a short deployment can mislead entirely.", "Full", "variation"),
 ("Sensitive habitat mapped", "Coral and seagrass carry the highest scrutiny in Saudi waters and are surveyed accordingly.", "Mapped", "before works"),
 ("Models calibrated", "Dispersion predictions are checked against measured conditions rather than left uncalibrated.", "Calibrated", "to site data")],

"remediation-rehabilitation": [
 ("Risk assessed before action", "Contamination does not automatically require remediation; the pathway and end use decide.", "Assessed", "before spend"),
 ("Options tested against the site", "The chosen approach has to be deliverable on the ground as it stands, not in principle.", "Deliverable", "on site"),
 ("Validation designed at the start", "What will be sampled to prove completion is agreed before works begin, not afterwards.", "Planned", "from day one"),
 ("Closure that holds", "Post-works sampling demonstrates the criteria were met, which is what actually closes the liability.", "Evidenced", "closure")],

"environmental-modelling": [
 ("Inputs sourced and stated", "Emission rates and their origin are documented, because reviewers examine inputs before conclusions.", "Sourced", "inputs"),
 ("Representative meteorology", "Met data covers a period long enough to reflect typical conditions, not a convenient window.", "Representative", "period"),
 ("Assumptions on show", "Where data was missing, the assumption made is declared rather than buried in an appendix.", "Declared", "not buried"),
 ("Limitations stated", "Results are presented with their confidence and limits, not as certainties.", "Honest", "confidence")],

"laboratory-services": [
 ("One chain, no handovers", "Design, collection, analysis and interpretation sit with one party, so nothing is lost between them.", "1", "accountable party"),
 ("Design reflects the question", "The sampling plan is built around what the interpretation will need to conclude.", "Purpose", "built plan"),
 ("Field context reaches the analyst", "What the sampling team observed is available when the results are interpreted.", "Context", "carried through"),
 ("Comparable across cycles", "Methods and locations stay constant, so trends across a programme mean something.", "Consistent", "methodology")],
}
