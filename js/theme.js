/* ==========================================================================
   theme.js — light/dark toggle button behavior.
   The initial theme is already applied by a tiny inline script in <head>
   (before CSS paints, to avoid a flash of the wrong theme). This file only
   wires up the toggle button and keeps localStorage in sync.
   ========================================================================== */
(() => {
  'use strict';

  const STORAGE_KEY = 'az-theme';
  const root = document.documentElement;
  const toggle = document.querySelector('#theme-toggle');
  if(!toggle) return;

  function currentTheme(){
    return root.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
  }

  function applyTheme(theme){
    if(theme === 'light'){
      root.setAttribute('data-theme', 'light');
    } else {
      root.removeAttribute('data-theme');
    }
    toggle.setAttribute('aria-pressed', String(theme === 'light'));
  }

  toggle.setAttribute('aria-pressed', String(currentTheme() === 'light'));

  toggle.addEventListener('click', () => {
    const next = currentTheme() === 'light' ? 'dark' : 'light';
    applyTheme(next);
    try { localStorage.setItem(STORAGE_KEY, next); }
    catch(e){ /* private browsing: preference just won't persist */ }
  });
})();
