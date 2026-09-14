# BluePrint, Equipment Catalogue.
#
# Instrument TYPES used across the services BluePrint offers, grouped by domain.
# No makes, models or serial numbers appear, and the page does not claim an
# inventory, because no equipment register has been supplied. Where a standard
# is named it is the one the instrument class is defined by.

DOMAINS = [
    ("air", "fa-wind", "Air Quality",
     "Ambient, stack and fugitive emission measurement.",
     "service-air-quality-monitoring.html", [
        ("Reference gravimetric particulate sampler",
         "PM10 and PM2.5 by filter weighing",
         "The reference method most ambient conditions are written against."),
        ("Continuous particulate analyser",
         "PM10, PM2.5, TSP, real time",
         "Beta attenuation or optical, for campaigns needing a time series rather than a daily average."),
        ("Gas analyser set",
         "NO&#8322;, SO&#8322;, CO, O&#8323;",
         "Chemiluminescence, UV fluorescence, NDIR and UV photometry, one technique per determinand."),
        ("VOC sampling train",
         "Volatile organic compounds",
         "Sorbent tubes or canisters, transferred to the laboratory for thermal desorption and analysis."),
        ("Isokinetic stack sampling train",
         "Point source emissions",
         "Sampling at the flue gas velocity, with pitot tube and thermocouple, so the sample represents the stack."),
        ("Portable flue gas analyser",
         "Combustion gases at the stack",
         "For screening and process checks alongside the formal isokinetic run."),
        ("Directional dust deposition gauge",
         "Nuisance and deposited dust",
         "Used where a complaint has been raised and the source direction is in question."),
        ("Automatic weather station",
         "Wind speed and direction, temperature, humidity, pressure, rainfall",
         "Results without wind and weather context are difficult to defend, so both are captured together."),
     ]),

    ("noise", "fa-volume-high", "Noise &amp; Vibration",
     "Boundary, receptor, occupational and blast monitoring.",
     "service-noise-monitoring.html", [
        ("Class 1 integrating sound level meter",
         "L&#8320;&#8337;, L&#8336;&#8336;&#8336;, L&#8339;&#8331;&#8336;&#8320; and percentile indices",
         "Class 1 to IEC 61672 is what regulatory submissions are normally expected to use."),
        ("Acoustic calibrator",
         "Field calibration check",
         "Verified before and after every survey, because an uncalibrated dataset cannot be defended."),
        ("Unattended noise logger",
         "Continuous day, evening and night periods",
         "Deployed where a representative survey has to cover each period rather than a single visit."),
        ("Personal noise dosimeter",
         "Occupational exposure over a shift",
         "A separate obligation from boundary noise, covering the workforce inside the fence."),
        ("Triaxial vibration monitor",
         "Peak particle velocity and airblast",
         "For blasting and piling near communities or sensitive structures."),
     ]),

    ("water", "fa-droplet", "Water &amp; Wastewater",
     "Discharge, process, groundwater and receiving water.",
     "service-water-wastewater-testing.html", [
        ("Multiparameter sonde",
         "pH, dissolved oxygen, conductivity, temperature, turbidity, redox",
         "Several of these change between the sampling point and the laboratory, so they are read in situ."),
        ("Nephelometric turbidity meter",
         "Suspended solids indication",
         "Used at discharge points and in receiving water where a visual assessment is not enough."),
        ("Open channel and ultrasonic flow meter",
         "Discharge rate and volume",
         "Needed wherever the consent limit is load based rather than concentration based."),
        ("Automatic composite sampler",
         "Flow or time proportional samples",
         "A grab sample captures one moment; a composite blends across a period or across flow."),
        ("Groundwater level dipper and interface probe",
         "Standing water level, product thickness",
         "Standard for monitoring wells, including where separate phase product may be present."),
        ("Low flow purge pump",
         "Representative groundwater sampling",
         "Purging at low rate avoids drawing in water that does not represent the formation."),
        ("Chain of custody transport kit",
         "Sample integrity",
         "Insulated boxes, preservation and documented transfer, since holding times are part of the method."),
     ]),

    ("ground", "fa-mountain", "Soil, Sediment &amp; Ground",
     "Site investigation, contamination and geotechnics.",
     "service-soil-sediment-testing.html", [
        ("Hand auger and window sampler",
         "Shallow soil profiles",
         "For shallow investigation and where access will not take a rig."),
        ("Split spoon and core sampler",
         "Undisturbed samples at depth",
         "Recovered through a borehole programme sized to the ground risk."),
        ("Photoionisation detector",
         "Volatile screening in the field",
         "Screening only, used to direct where formal samples are taken rather than to report a number."),
        ("Sediment grab",
         "Bed sediment from water bodies",
         "Van Veen or Ekman pattern, for marine and freshwater sediment characterisation."),
        ("Test sieve stack and shaker",
         "Particle size distribution",
         "Laboratory classification of soils and sediments."),
        ("Drying oven and analytical balance",
         "Moisture content, gravimetric preparation",
         "Sample preparation ahead of analysis."),
     ]),

    ("marine", "fa-water", "Marine &amp; Coastal",
     "Water column, seabed and oceanographic survey.",
     "service-marine-environment.html", [
        ("CTD profiler",
         "Conductivity, temperature, depth through the column",
         "Establishes stratification and salinity structure, which discharge assessment depends on."),
        ("Acoustic Doppler current profiler",
         "Current speed and direction by depth",
         "Provides the current data a hydrodynamic model needs as input."),
        ("Single and multibeam echo sounder",
         "Seabed elevation, bathymetry",
         "High accuracy mapping for dredging, navigation and coastal planning."),
        ("Underwater survey camera and quadrats",
         "Habitat extent and condition",
         "For coral, seagrass and benthic habitat mapping."),
        ("Tide gauge and wave recorder",
         "Water levels, wave height and period",
         "Field investigations supporting coastal development and marine infrastructure."),
     ]),

    ("lab", "fa-flask", "Laboratory Analysis",
     "Accredited analysis and technical interpretation.",
     "service-laboratory-analysis.html", [
        ("Gas chromatograph with mass spectrometer",
         "Volatile and semi-volatile organics",
         "Identification and quantification for hydrocarbon and VOC determinands."),
        ("Inductively coupled plasma spectrometer",
         "Heavy metals and trace elements",
         "Optical emission or mass spectrometry depending on the detection limit required."),
        ("Ion chromatograph",
         "Anions and cations",
         "Chloride, sulphate, nitrate and related determinands in water and leachate."),
        ("UV-visible spectrophotometer",
         "Colorimetric determinands",
         "Established methods for nutrients and a range of water quality parameters."),
        ("BOD incubator and COD digestor",
         "Oxygen demand",
         "BOD takes five days by definition, which is why it sets the reporting schedule."),
        ("Muffle furnace",
         "Loss on ignition, organic content",
         "Thermal preparation and organic matter determination."),
        ("Microbiological incubator and filtration set",
         "Indicator organisms",
         "For potable and amenity water against health based standards."),
     ]),

    ("modelling", "fa-diagram-project", "Modelling Software",
     "Prediction with the assumptions on show.",
     "service-environmental-modelling.html", [
        ("AERMOD and CALPUFF",
         "Atmospheric dispersion",
         "Predicting ground level concentrations from stack and fugitive sources."),
        ("DHI-MIKE and CORMIX",
         "Hydrodynamics and discharge mixing",
         "Thermal and saline plume behaviour, circulation and near field mixing."),
        ("HEC-RAS, HEC-HMS and WMS",
         "Watershed hydrology and hydraulics",
         "Flood routing, runoff and drainage design support."),
        ("MODFLOW",
         "Groundwater flow and quality",
         "Aquifer behaviour and contaminant transport."),
        ("SoundPlan",
         "Noise propagation",
         "Predicting noise at receptors before a facility is built or expanded."),
     ]),
]


def _nav():
    return "\n".join(
        '<a href="#eq-' + key + '" class="eqp-chip"><i class="fas ' + icon + '"></i>'
        + name + '</a>'
        for key, icon, name, _s, _h, _items in DOMAINS)


def _sections():
    out = []
    for key, icon, name, sub, href, items in DOMAINS:
        rows = "\n".join(
            '<div class="eqp-row">'
            '<div class="eqp-name">' + n + '</div>'
            '<div class="eqp-meas">' + m + '</div>'
            '<div class="eqp-note">' + d + '</div>'
            '</div>'
            for n, m, d in items)
        out.append(
            '<section class="eqp-sec" id="eq-' + key + '">'
            '<div class="eqp-sec-head">'
            '<span class="eqp-sec-ic"><i class="fas ' + icon + '"></i></span>'
            '<div><h2>' + name + '</h2><p>' + sub + '</p></div>'
            '<a href="' + href + '" class="eqp-sec-link">Related service '
            '<i class="fas fa-arrow-right" style="font-size:.68rem;"></i></a>'
            '</div>'
            '<div class="eqp-table">'
            '<div class="eqp-row eqp-head"><div>Instrument</div><div>What it measures</div>'
            '<div>Why it is used</div></div>'
            + rows +
            '</div></section>')
    return "\n".join(out)


_TPL = """
<section class="eqp-hero">
  <div class="eqp-wrap">
    <nav class="eqp-crumb" aria-label="Breadcrumb">
      <a href="index.html">Home</a><span>/</span><span>Equipment Catalogue</span>
    </nav>
    <p class="eqp-eyebrow">Instrumentation</p>
    <h1>Equipment catalogue</h1>
    <p class="eqp-lede">The instrument types used across our services, grouped by domain, with what
       each measures and why the method calls for it. Exact models are confirmed at scoping against
       the method your permit conditions name.</p>
    <div class="eqp-chips">{nav}</div>
  </div>
</section>

<div class="eqp-body">
  <div class="eqp-wrap">
    {sections}
    <aside class="eqp-note-box">
      <h3>A note on specification</h3>
      <p>Instruments are selected against the parameter, range and method your conditions reference,
         not against a standing list. Where a condition names a reference method, the equipment used
         has to meet it, and calibration is verified at both ends of the deployment so drift cannot
         invalidate a dataset unnoticed.</p>
      <a href="contact.html" class="eqp-cta">Ask about a specific requirement
         <i class="fas fa-arrow-right" style="font-size:.7rem;"></i></a>
    </aside>
  </div>
</div>
"""


def equipment():
    return _TPL.replace("{nav}", _nav()).replace("{sections}", _sections())
