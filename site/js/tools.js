/* ============================================================
   BluePrint — tools.js
   Inspection booking modal, compliance checker, carbon calculator.
   ============================================================ */
(function () {
  'use strict';
  var C = window.BP_CONFIG || {};

  /* ── Booking modal ───────────────────────────────────────── */
  window.openBookingModal = function () {
    openModal('bookingModal');
    var tomorrow = new Date(); tomorrow.setDate(tomorrow.getDate() + 1);
    var dateInput = document.getElementById('bkDate');
    if (dateInput) dateInput.min = tomorrow.toISOString().split('T')[0];
    var form = document.getElementById('bookingForm'); if (form) form.reset();
    document.getElementById('bookingFormContainer').style.display = 'block';
    document.getElementById('bookingSuccess').style.display = 'none';
  };

  window.submitBooking = async function (event) {
    event.preventDefault();
    var btn = document.getElementById('bkSubmitBtn');
    var originalText = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Submitting...'; btn.disabled = true;

    var v = function (id) { var el = document.getElementById(id); return el ? el.value.trim() : ''; };
    var formData = {
      companyName: v('bkCompanyName'), contactName: v('bkContactName'), contactEmail: v('bkEmail'), contactPhone: v('bkPhone'),
      serviceType: v('bkServiceType'), siteLocation: v('bkLocation'), city: v('bkCity'),
      preferredDate: v('bkDate'), preferredTime: v('bkTime'), serviceDescription: v('bkDescription')
    };
    try {
      var response = await fetch(C.BOOKINGS_URL, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(formData) });
      var result = await response.json();
      if (response.ok && result.success) {
        document.getElementById('bookingFormContainer').style.display = 'none';
        document.getElementById('bookingSuccess').style.display = 'block';
        document.getElementById('bookingRefNumber').textContent = result.booking.bookingRef;
      } else {
        alert('Booking failed: ' + (result.error || 'Please try again'));
      }
    } catch (err) {
      console.error('Booking error:', err);
      alert('Connection error. Please try again later.');
    } finally {
      btn.innerHTML = originalText; btn.disabled = false;
    }
  };

  window.resetBookingForm = function () {
    var form = document.getElementById('bookingForm'); if (form) form.reset();
    document.getElementById('bookingFormContainer').style.display = 'block';
    document.getElementById('bookingSuccess').style.display = 'none';
  };

  /* ── Calculator modal ────────────────────────────────────── */
  window.openCalculator = function (tab) { openModal('calcModal'); switchCalcTab(tab || 'compliance'); };
  window.switchCalcTab = function (tab) {
    var isC = tab === 'compliance';
    document.getElementById('calc-compliance').classList.toggle('hidden', !isC);
    document.getElementById('calc-carbon').classList.toggle('hidden', isC);
    document.getElementById('calcTab-compliance').classList.toggle('calc-tab-active', isC);
    document.getElementById('calcTab-carbon').classList.toggle('calc-tab-active', !isC);
  };

  /* ── Compliance data ─────────────────────────────────────── */
  var complianceData = {
    cement:       { ksa: ['NCEC Ambient Air Quality Standards (SAAQS)', 'NCEC Emission Limits for Cement Plants', 'US EPA Method 5 — Particulate Stack Testing', 'PM10, PM2.5, NOx, SO₂, CO monitoring required', 'Continuous Emission Monitoring System (CEMS) recommended'], uae: ['UAE Federal Law No. 24 on Environment Protection', 'Abu Dhabi EHS Cement Regulations', 'PM, NOx, SO₂ emission monitoring'], intl: ['IFC EHS Guidelines for Cement & Lime', 'WHO Air Quality Guidelines 2021', 'GHG Protocol — Scope 1 & 2 Reporting'] },
    power:        { ksa: ['NCEC SAAQS for power generation zones', 'NCEC NOx, SO₂ stack emission standards', 'CEMS installation mandatory >50MW', 'Saudi Electricity Company grid compliance', 'Water discharge monitoring if cooling towers'], uae: ['DEWA/ADWEA environmental compliance', 'UAE Cabinet Decision No. 37/2001'], intl: ['IFC EHS for Thermal Power Plants', 'World Bank Pollution Prevention Guidelines', 'GHG emissions reporting (ISO 14064)'] },
    oil:          { ksa: ['NCEC / Saudi Aramco HSE Standards', 'NCEC VOC and H₂S emission limits', 'Continuous flare monitoring', 'Saudi Aramco Safety Standards (SAES)', 'BTEX ambient monitoring around facilities'], uae: ['ADNOC HSE Management System', 'UAE Federal Law No. 24'], intl: ['IFC EHS for Oil & Gas Upstream', 'GHG Protocol Oil & Gas Sector Guidance', 'MARPOL Annex VI (marine operations)'] },
    construction: { ksa: ['NCEC Dust Management Guidelines', 'Saudi Vision 2030 Sustainability Requirements', 'PM10/TSP monitoring at site boundary', 'Water quality monitoring for runoff'], uae: ['Dubai Municipality Construction Noise/Dust', 'UAE Environment Regulations for Construction Sites'], intl: ['IFC General EHS Guidelines', 'Equator Principles for project finance', 'ISO 14001 Environmental Management System'] },
    food:         { ksa: ['NCEC Emission Standards for Food Processing', 'Saudi Food & Drug Authority (SFDA) compliance', 'Wastewater discharge standards (NCEC)', 'Refrigerant management (F-Gas)'], uae: ['Dubai Municipality Food Safety', 'UAE Cabinet Resolution No. 12/2016'], intl: ['IFC EHS for Food & Beverage', 'WHO Good Manufacturing Practices'] },
    pharma:       { ksa: ['NCEC Air Quality & Chemical Emissions', 'SFDA GMP Facility Requirements', 'ISO 14644 Cleanroom Air Standards', 'HAPs and VOC emission limits'], uae: ['UAE Ministry of Health GMP', 'Dubai Health Authority regulations'], intl: ['ICH Q7 Active Pharmaceutical Ingredients', 'IFC EHS for Pharmaceuticals', 'ISO 14001 EMS'] }
  };

  window.updateCompliance = function () {
    var ind = document.getElementById('compIndustry').value;
    var reg = document.getElementById('compRegion').value;
    var results = document.getElementById('complianceResults');
    var placeholder = document.getElementById('compliancePlaceholder');
    if (!ind || !reg) { results.classList.add('hidden'); placeholder.classList.remove('hidden'); return; }
    var standards = (complianceData[ind] && complianceData[ind][reg]) || [];
    placeholder.classList.add('hidden'); results.classList.remove('hidden');
    document.getElementById('complianceList').innerHTML = standards.map(function (s) {
      return '<div class="flex items-start gap-2"><i class="fas fa-check-circle text-bp-primary mt-0.5 flex-shrink-0"></i><span class="text-sm text-gray-700">' + s + '</span></div>';
    }).join('');
  };

  /* ── Carbon calculator ───────────────────────────────────── */
  window.updateCarbon = function () {
    var g = function (id) { return +document.getElementById(id).value; };
    var elec = g('electricity'), dies = g('diesel'), trav = g('travel'), proc = g('procGas');
    document.getElementById('elecVal').textContent    = elec.toLocaleString() + ' MWh';
    document.getElementById('dieselVal').textContent  = dies.toLocaleString() + ' L';
    document.getElementById('travelVal').textContent  = trav.toLocaleString() + ' km';
    document.getElementById('processVal').textContent = proc.toLocaleString() + ' tCO₂e';
    var s1 = Math.round(dies * 0.00268 + proc);
    var s2 = Math.round(elec * 0.45);
    var s3 = Math.round(trav * 0.00019);
    var total = s1 + s2 + s3;
    document.getElementById('scope1').textContent = s1.toLocaleString();
    document.getElementById('scope2').textContent = s2.toLocaleString();
    document.getElementById('totalCarbon').textContent = total.toLocaleString();
    var tip = document.getElementById('carbonTip');
    if (total > 0) {
      tip.classList.remove('hidden');
      tip.textContent = '💡 ' + (s2 > s1
        ? 'Your largest source is electricity (Scope 2: ' + s2.toLocaleString() + ' tCO₂e). Consider renewable energy procurement or solar PV.'
        : 'Your largest source is direct fuel use (Scope 1: ' + s1.toLocaleString() + ' tCO₂e). Fleet electrification or fuel switching can drive major reductions.');
    }
  };
  if (document.getElementById('electricity')) updateCarbon();

  window.goToContact = function (modalId) {
    closeModal(modalId);
    window.location.href = 'contact.html';
  };
})();
