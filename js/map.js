/* ==========================================================================
   map.js — points the map card at SITE_CONFIG.mapQuery.
   The HTML already contains a working default (Khair Khana, Kabul), so the
   map still shows if this script does not run. To pin the exact spot, paste
   its coordinates (e.g. "34.5700,69.1300") into mapQuery in js/config.js.
   ========================================================================== */
(() => {
  'use strict';
  const q = window.SITE_CONFIG && window.SITE_CONFIG.mapQuery;
  if(!q) return;
  const enc = encodeURIComponent(q);
  const frame = document.getElementById('map-frame');
  const open = document.getElementById('map-open');
  const dir = document.getElementById('map-directions');
  if(frame) frame.src = `https://www.google.com/maps?q=${enc}&output=embed`;
  if(open) open.href = `https://www.google.com/maps/search/?api=1&query=${enc}`;
  if(dir) dir.href = `https://www.google.com/maps/dir/?api=1&destination=${enc}`;
})();
