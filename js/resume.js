/* ==========================================================================
   resume.js — wires the "Print / Save as PDF" button on resume.html.
   ========================================================================== */
(() => {
  'use strict';
  const btn = document.getElementById('print-btn');
  if(btn) btn.addEventListener('click', () => window.print());
})();
