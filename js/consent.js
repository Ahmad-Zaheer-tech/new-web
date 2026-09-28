/* ==========================================================================
   consent.js — minimal, honest analytics consent.
   Google Analytics is NOT loaded until the visitor explicitly accepts.
   The choice is remembered in localStorage so the banner shows once.
   ========================================================================== */
(() => {
  'use strict';

  const STORAGE_KEY = 'az-consent';
  const cfg = window.SITE_CONFIG || {};
  const gaId = cfg.gaMeasurementId;
  const gaConfigured = gaId && !gaId.includes('XXXX');

  function loadGA(){
    if(!gaConfigured) return;
    if(document.getElementById('ga-script')) return;
    const s = document.createElement('script');
    s.id = 'ga-script';
    s.async = true;
    s.src = `https://www.googletagmanager.com/gtag/js?id=${gaId}`;
    document.head.appendChild(s);

    window.dataLayer = window.dataLayer || [];
    function gtag(){ window.dataLayer.push(arguments); }
    window.gtag = gtag;
    gtag('js', new Date());
    gtag('config', gaId, { anonymize_ip: true });
  }

  function getStoredChoice(){
    try { return localStorage.getItem(STORAGE_KEY); }
    catch(e){ return null; }
  }
  function storeChoice(value){
    try { localStorage.setItem(STORAGE_KEY, value); }
    catch(e){ /* private-browsing or storage disabled: banner will just reappear */ }
  }

  const existing = getStoredChoice();
  if(existing === 'accepted'){
    loadGA();
    return; // no banner needed, choice already made
  }
  if(existing === 'declined' || !gaConfigured){
    return; // respected the decline, or analytics isn't set up yet — stay silent
  }

  // No choice yet — show the banner.
  const banner = document.createElement('div');
  banner.className = 'consent-banner';
  banner.setAttribute('role', 'dialog');
  banner.setAttribute('aria-label', 'Cookie notice');
  banner.innerHTML = `
    <p>This site uses Google Analytics to understand traffic. No personal data is sold or shared. You can decline and browsing still works exactly the same.</p>
    <div class="consent-actions">
      <button type="button" class="btn btn--ghost btn--small" data-consent="decline">Decline</button>
      <button type="button" class="btn btn--primary btn--small" data-consent="accept">Accept</button>
    </div>
  `;
  document.body.appendChild(banner);
  requestAnimationFrame(() => banner.classList.add('is-visible'));

  banner.addEventListener('click', (e) => {
    const choice = e.target.dataset.consent;
    if(!choice) return;
    storeChoice(choice === 'accept' ? 'accepted' : 'declined');
    if(choice === 'accept') loadGA();
    banner.classList.remove('is-visible');
    setTimeout(() => banner.remove(), 300);
  });
})();
