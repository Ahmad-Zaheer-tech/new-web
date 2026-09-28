/* ==========================================================================
   typewriter.js — hero line that types one technology at a time, holds,
   deletes it, then moves to the next (in a fixed, deliberate order).

   - Reads its items from the static <ul class="typer__list"> in the HTML, so
     there is one source of truth and a no-JS fallback for free.
   - Respects prefers-reduced-motion: nothing animates, the static list stays.
   - Offers a pause/play button (WCAG 2.2.2) and pauses while off-screen or
     while the tab is hidden.
   - Works in both LTR and RTL: direction is set per item so the caret always
     sits at the end of the text being typed.
   ========================================================================== */
(() => {
  'use strict';

  const root = document.getElementById('typer');
  if(!root) return;
  if(window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

  const items = Array.from(root.querySelectorAll('.typer__list li')).map(li => ({
    id: li.dataset.tech,
    name: li.querySelector('.typer__name').textContent.trim(),
    icon: li.querySelector('.typer__ico').innerHTML,
    plate: li.hasAttribute('data-plate'),
  }));
  if(!items.length) return;

  const slot = root.querySelector('.typer__slot');
  const typed = root.querySelector('.typer__typed');
  const text = root.querySelector('.typer__text');
  const pauseBtn = root.querySelector('.typer__pause');

  // Announce the whole list once, instead of every keystroke.
  root.setAttribute('role', 'group');
  root.setAttribute('aria-label', root.dataset.summary || '');
  root.classList.add('is-active');
  pauseBtn.hidden = false;

  const segment = ('Segmenter' in Intl)
    ? (s) => Array.from(new Intl.Segmenter(undefined, { granularity: 'grapheme' }).segment(s), x => x.segment)
    : (s) => Array.from(s);
  const isRtlText = (s) => /[\u0590-\u08FF]/.test(s);
  const sleep = (ms) => new Promise(r => setTimeout(r, ms));

  let userPaused = false;
  let inView = true;
  const halted = () => userPaused || !inView || document.hidden;
  async function gate(){ while(halted()){ setState('paused'); await sleep(150); } }
  function setState(s){ if(root.dataset.state !== s) root.dataset.state = s; }

  function apply(it){
    root.className = root.className.replace(/\btc-[\w-]+/g, '').trim() + ' tc-' + it.id;
    slot.innerHTML = it.icon;
    slot.classList.toggle('is-plate', it.plate);
    typed.setAttribute('dir', isRtlText(it.name) ? 'rtl' : 'ltr');
  }

  pauseBtn.addEventListener('click', () => {
    userPaused = !userPaused;
    pauseBtn.setAttribute('aria-pressed', String(userPaused));
    pauseBtn.setAttribute('aria-label', userPaused ? root.dataset.play : root.dataset.pause);
  });

  if('IntersectionObserver' in window){
    new IntersectionObserver((entries) => { inView = entries[0].isIntersecting; }, { threshold: 0.05 }).observe(root);
  }

  (async function run(){
    let n = 0;
    await sleep(500);
    for(;;){
      const it = items[n % items.length];
      const chars = segment(it.name);
      apply(it);
      setState('typing');
      for(let k = 1; k <= chars.length; k++){
        await gate(); setState('typing');
        text.textContent = chars.slice(0, k).join('');
        await sleep(62 + Math.random() * 48);
      }
      setState('idle');
      await sleep(1500);
      for(let k = chars.length - 1; k >= 0; k--){
        await gate(); setState('deleting');
        text.textContent = chars.slice(0, k).join('');
        await sleep(28);
      }
      setState('idle');
      await sleep(340);
      n++;
    }
  })();
})();
