/* ==========================================================================
   whatsapp-widget.js — injects a floating WhatsApp button using the number
   and default message set in config.js. One place to edit, every page
   updates automatically.
   ========================================================================== */
(() => {
  'use strict';

  const cfg = window.SITE_CONFIG || {};
  if(!cfg.whatsappNumber) return;

  const isFa = document.documentElement.lang === 'fa';
  const message = encodeURIComponent((isFa && cfg.whatsappDefaultMessageFa) || cfg.whatsappDefaultMessage || 'Hello!');
  const href = `https://wa.me/${cfg.whatsappNumber}?text=${message}`;

  // Floating widgets live inside one labelled landmark so screen-reader users can find (or skip) them.
  function fabDock(){
    let d = document.getElementById('fab-dock');
    if(!d){
      d = document.createElement('aside');
      d.id = 'fab-dock';
      d.setAttribute('aria-label', document.documentElement.lang === 'fa' ? 'تماس سریع' : 'Quick contact');
      document.body.appendChild(d);
    }
    return d;
  }
  const link = document.createElement('a');
  link.href = href;
  link.className = 'whatsapp-fab';
  link.target = '_blank';
  link.rel = 'noopener noreferrer';
  link.setAttribute('aria-label', isFa ? 'گفتگو در واتساپ' : 'Chat on WhatsApp');
  link.innerHTML = `
    <svg viewBox="0 0 24 24" width="26" height="26" fill="currentColor" aria-hidden="true">
      <path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91c0 1.75.46 3.48 1.32 5L2 22l5.24-1.37a9.9 9.9 0 0 0 4.8 1.22h.01c5.46 0 9.9-4.45 9.9-9.91 0-2.65-1.03-5.14-2.9-7.01A9.87 9.87 0 0 0 12.04 2m0 1.67a8.2 8.2 0 0 1 5.83 2.42 8.2 8.2 0 0 1 2.4 5.82c0 4.55-3.7 8.24-8.24 8.24a8.2 8.2 0 0 1-4.19-1.15l-.3-.18-3.11.81.83-3.03-.2-.31a8.18 8.18 0 0 1-1.26-4.38c0-4.55 3.7-8.24 8.24-8.24M8.53 6.9c-.17 0-.45.06-.68.32-.23.25-.9.87-.9 2.13 0 1.25.92 2.46 1.04 2.63.13.17 1.78 2.85 4.42 3.89 2.19.86 2.63.69 3.11.65.48-.04 1.55-.63 1.77-1.24.21-.61.21-1.14.15-1.24-.06-.11-.23-.17-.48-.3-.25-.13-1.5-.74-1.73-.82-.23-.09-.4-.13-.57.13-.17.25-.65.82-.8.99-.14.17-.29.19-.54.06-.25-.13-1.04-.38-1.98-1.22-.73-.65-1.23-1.46-1.37-1.71-.14-.25-.02-.38.11-.51.11-.11.25-.29.38-.44.12-.14.16-.25.24-.42.08-.17.04-.31-.02-.44C9.9 8.9 9.42 7.66 9.2 7.15c-.18-.42-.37-.4-.51-.41-.13-.01-.28-.01-.16-.01" />
    </svg>
  `;
  fabDock().appendChild(link);
})();
