/* ==========================================================================
   skills.js — category filter for skills.html.
   Toggles the `hidden` attribute on each skill section (no inline styles).
   ========================================================================== */
(() => {
  'use strict';
  const buttons = document.querySelectorAll('.filter-btn[data-filter]');
  const sections = document.querySelectorAll('.skill-section[data-cat]');
  if(!buttons.length || !sections.length) return;

  function apply(cat){
    buttons.forEach(b => {
      const on = b.dataset.filter === cat;
      b.classList.toggle('is-active', on);
      b.setAttribute('aria-pressed', String(on));
    });
    sections.forEach(s => { s.hidden = !(cat === 'all' || s.dataset.cat === cat); });
  }
  buttons.forEach(b => b.addEventListener('click', () => {
    apply(b.dataset.filter);
    if(history.replaceState) history.replaceState(null, '', b.dataset.filter === 'all' ? location.pathname : '#' + b.dataset.filter);
  }));
  const fromHash = location.hash.replace('#', '');
  if(fromHash && document.querySelector(`.skill-section[data-cat="${fromHash}"]`)) apply(fromHash);
})();
