/* ==========================================================================
   ask-ahmad.js — a floating "Ask Ahmad" search widget.

   HONESTY NOTE (by design, not an afterthought): this is keyword/token
   search over js/ask-ahmad-data.js, not a language model. It never invents
   an answer — if nothing in the knowledge base matches well enough, it
   says so plainly and offers real topic suggestions plus a way to reach
   Ahmad directly. See ask-ahmad-data.js for the only content it can draw
   from.
   ========================================================================== */
(() => {
  'use strict';

  const KB = window.ASK_AHMAD_KB || [];
  if(!KB.length) return;

  const LANG = document.documentElement.getAttribute('lang') === 'fa' ? 'fa' : 'en';

  const STRINGS = {
    en: {
      fabLabel: 'Ask Ahmad — search this site',
      title: 'Ask Ahmad',
      subtitle: "Searches this site's real content — not a general AI, so it won't catch everything.",
      close: 'Close',
      placeholder: 'Ask about services, skills, projects…',
      send: 'Send',
      greeting: "Hi — ask me about Ahmad's services, skills, projects, or how to get in touch.",
      thinking: 'Looking that up…',
      noMatch: "I don't have a good match for that in the site's content yet. Try one of these, rephrase your question, or reach Ahmad directly:",
      noMatchLink: 'Open the contact page',
      suggestedHeading: 'Popular questions',
      chips: {
        services: 'What services do you offer?',
        skills: 'What technologies do you use?',
        projects: 'Show me your projects',
        contact: 'How do I contact you?',
        pricing: 'How much does it cost?',
        process: 'How does a project start?',
      },
    },
    fa: {
      fabLabel: 'پرسش از احمد — جستجو در این سایت',
      title: 'پرسش از احمد',
      subtitle: 'در محتوای واقعی این سایت جستجو می‌کند — یک هوش مصنوعی عمومی نیست، پس ممکن است همه‌چیز را پوشش ندهد.',
      close: 'بستن',
      placeholder: 'درباره خدمات، مهارت‌ها، پروژه‌ها بپرسید…',
      send: 'ارسال',
      greeting: 'سلام — درباره خدمات، مهارت‌ها، پروژه‌ها، یا راه تماس با احمد بپرسید.',
      thinking: 'در حال جستجو…',
      noMatch: 'برای این پرسش هنوز تطابق خوبی در محتوای سایت پیدا نکردم. یکی از این‌ها را امتحان کنید، سوال را طور دیگری بپرسید، یا مستقیم با احمد تماس بگیرید:',
      noMatchLink: 'رفتن به صفحه تماس',
      suggestedHeading: 'پرسش‌های پرتکرار',
      chips: {
        services: 'چه خدماتی ارائه می‌دهید؟',
        skills: 'با چه تکنولوژی‌هایی کار می‌کنید؟',
        projects: 'پروژه‌هایتان را نشان دهید',
        contact: 'چطور با شما تماس بگیرم؟',
        pricing: 'هزینه‌اش چقدر است؟',
        process: 'یک پروژه چطور شروع می‌شود؟',
      },
    },
  }[LANG];

  const SUGGESTED = ['services', 'skills', 'projects', 'contact', 'pricing', 'process'];

  // ---- Light text normalization for matching (not for display) ----------
  // Unifies common Arabic/Persian glyph variants and strips punctuation so
  // "می‌کنی؟" and "می کنی" both match the same keyword.
  function normalize(str){
    return str
      .toLowerCase()
      .replace(/[\u064A]/g, '\u06CC')   // Arabic yeh -> Persian yeh
      .replace(/[\u0643]/g, '\u06A9')   // Arabic kaf -> Persian kaf
      .replace(/[\u200C\u200F\u200E]/g, ' ') // ZWNJ / directional marks -> space
      .replace(/[؟?!.,،؛;:()"'«»]/g, ' ')
      .replace(/\s+/g, ' ')
      .trim();
  }

  // ---- Build the widget DOM -------------------------------------------
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
  const fab = document.createElement('button');
  fab.className = 'ask-ahmad-fab';
  fab.setAttribute('aria-label', STRINGS.fabLabel);
  fab.setAttribute('aria-expanded', 'false');
  fab.setAttribute('aria-controls', 'ask-ahmad-panel');
  fab.innerHTML = `
    <svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true">
      <path d="M12 3a7 7 0 0 0-7 7c0 2.4 1.2 4.5 3 5.8V19l2.8-1.5c.4.07.8.1 1.2.1a7 7 0 0 0 0-14Z"/>
      <circle cx="9.5" cy="10" r=".9" fill="currentColor" stroke="none"/>
      <circle cx="12.5" cy="10" r=".9" fill="currentColor" stroke="none"/>
      <circle cx="15.5" cy="10" r=".9" fill="currentColor" stroke="none"/>
    </svg>`;

  const panel = document.createElement('div');
  panel.className = 'ask-ahmad-panel';
  panel.id = 'ask-ahmad-panel';
  panel.setAttribute('role', 'dialog');
  panel.setAttribute('aria-label', STRINGS.title);
  panel.innerHTML = `
    <div class="ask-ahmad-head">
      <div class="ask-ahmad-head-id">
        <span class="ask-ahmad-avatar" aria-hidden="true">AZ</span>
        <div>
          <h3>${STRINGS.title}</h3>
          <p>${STRINGS.subtitle}</p>
        </div>
      </div>
      <button class="ask-ahmad-close" aria-label="${STRINGS.close}">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M6 6l12 12M18 6L6 18"/></svg>
      </button>
    </div>
    <div class="ask-ahmad-body" id="ask-ahmad-body" aria-live="polite"></div>
    <div class="ask-ahmad-chips" id="ask-ahmad-chips"></div>
    <form class="ask-ahmad-form" id="ask-ahmad-form">
      <label for="ask-ahmad-input" class="visually-hidden">${STRINGS.placeholder}</label>
      <input type="text" id="ask-ahmad-input" autocomplete="off" placeholder="${STRINGS.placeholder}">
      <button type="submit" aria-label="${STRINGS.send}">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 2 11 13"/><path d="M22 2 15 22l-4-9-9-4 20-7z"/></svg>
      </button>
    </form>
  `;

  fabDock().appendChild(fab);
  fabDock().appendChild(panel);

  const body = panel.querySelector('#ask-ahmad-body');
  const chipsWrap = panel.querySelector('#ask-ahmad-chips');
  const form = panel.querySelector('#ask-ahmad-form');
  const input = panel.querySelector('#ask-ahmad-input');
  const closeBtn = panel.querySelector('.ask-ahmad-close');

  // ---- Matching: token-overlap + phrase scoring, tolerant of natural
  // phrasing and punctuation, still fully transparent/inspectable. -------
  function tokenize(str){
    return normalize(str).split(' ').filter(w => w.length > 1);
  }

  const STOPWORDS = new Set([
    'what', 'do', 'you', 'your', 'the', 'is', 'are', 'how', 'can', 'me', 'my', 'to', 'of', 'a', 'for', 'with', 'about', 'tell',
    'چه', 'چی', 'شما', 'خود', 'را', 'با', 'به', 'از', 'در', 'که', 'است', 'کنی', 'کنید', 'می',
  ]);

  function findMatch(query){
    const qNorm = normalize(query);
    const qTokens = tokenize(query);
    if(!qTokens.length) return null;

    let best = null;
    let bestScore = 0;

    KB.forEach(entry => {
      // Best single keyword-phrase match wins — summing across many generic
      // keyword variants would let an entry with lots of short/filler
      // phrases ("what do you do") outscore a more specific single match.
      let entryBest = 0;
      entry.keywords.forEach(kw => {
        const kwNorm = normalize(kw);
        const kwTokens = kwNorm.split(' ').filter(Boolean);
        let kwScore = 0;
        // Full-phrase substring match: strong signal, weighted by phrase length.
        if(kwTokens.length > 1 && qNorm.includes(kwNorm)){
          kwScore += kwNorm.length * 1.5;
        }
        // Token-level overlap: catches reordered / partial natural phrasing.
        // Stopwords count for very little, so generic overlap alone can't win.
        kwTokens.forEach(kwTok => {
          if(qTokens.includes(kwTok)) kwScore += STOPWORDS.has(kwTok) ? 0.4 : kwTok.length;
        });
        if(kwScore > entryBest) entryBest = kwScore;
      });
      if(entryBest > bestScore){ bestScore = entryBest; best = entry; }
    });

    // Threshold scales gently with query length so short exact hits
    // ("pricing?") still match, but noise doesn't.
    const threshold = qTokens.length <= 2 ? 3 : 4;
    return bestScore >= threshold ? best : null;
  }

  function resolveHref(href){
    // Case-study links are one level deep; adjust when the widget runs
    // from within /projects/. The fa/ tree mirrors the same depth rules.
    const inSubdir = location.pathname.includes('/projects/');
    if(!inSubdir) return href;
    if(href.startsWith('projects/')) return href.replace('projects/', '');
    return '../' + href;
  }

  function addMessage(text, kind, link){
    const msg = document.createElement('div');
    msg.className = `ask-ahmad-msg ask-ahmad-msg--${kind}`;
    msg.textContent = text;
    if(link){
      const a = document.createElement('a');
      a.className = 'link-btn';
      a.href = resolveHref(link.href);
      const label = LANG === 'fa' ? (link.label_fa || link.label_en) : (link.label_en || link.label_fa);
      a.textContent = LANG === 'fa' ? '← ' + label : label + ' →';
      msg.appendChild(document.createElement('br'));
      msg.appendChild(a);
    }
    body.appendChild(msg);
    body.scrollTop = body.scrollHeight;
    return msg;
  }

  function addTyping(){
    const el = document.createElement('div');
    el.className = 'ask-ahmad-msg ask-ahmad-msg--bot ask-ahmad-msg--typing';
    el.innerHTML = '<span></span><span></span><span></span>';
    el.setAttribute('aria-label', STRINGS.thinking);
    body.appendChild(el);
    body.scrollTop = body.scrollHeight;
    return el;
  }

  function handleQuery(text){
    addMessage(text, 'user');
    const typingEl = addTyping();
    const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    const respond = () => {
      typingEl.remove();
      const match = findMatch(text);
      if(match){
        const answer = LANG === 'fa' ? (match.answer_fa || match.answer_en) : (match.answer_en || match.answer_fa);
        addMessage(answer, 'bot', match.link);
      } else {
        const msg = addMessage(STRINGS.noMatch, 'bot', { href: 'contact.html', label_en: STRINGS.noMatchLink, label_fa: STRINGS.noMatchLink });
        const chips = document.createElement('div');
        chips.className = 'ask-ahmad-chips ask-ahmad-chips--inline';
        SUGGESTED.slice(0, 3).forEach(id => {
          const entry = KB.find(e => e.id === id);
          if(!entry) return;
          const chip = document.createElement('button');
          chip.type = 'button';
          chip.className = 'ask-ahmad-chip';
          chip.textContent = STRINGS.chips[id] || id;
          chip.addEventListener('click', () => handleQuery(STRINGS.chips[id] || id));
          chips.appendChild(chip);
        });
        body.appendChild(chips);
        body.scrollTop = body.scrollHeight;
      }
    };

    // A brief, honest "thinking" pause — this is local search, not a
    // network call, so keep it short; skip entirely for reduced motion.
    window.setTimeout(respond, prefersReduced ? 0 : 420);
  }

  function renderChips(){
    chipsWrap.innerHTML = '';
    const heading = document.createElement('span');
    heading.className = 'ask-ahmad-chips-heading';
    heading.textContent = STRINGS.suggestedHeading;
    chipsWrap.appendChild(heading);
    const row = document.createElement('div');
    row.className = 'ask-ahmad-chips-row';
    SUGGESTED.forEach(id => {
      const entry = KB.find(e => e.id === id);
      if(!entry) return;
      const chip = document.createElement('button');
      chip.type = 'button';
      chip.className = 'ask-ahmad-chip';
      chip.textContent = STRINGS.chips[id] || id;
      chip.addEventListener('click', () => handleQuery(STRINGS.chips[id] || id));
      row.appendChild(chip);
    });
    chipsWrap.appendChild(row);
  }

  let opened = false;
  function openPanel(){
    panel.classList.add('is-open');
    fab.setAttribute('aria-expanded', 'true');
    if(!opened){
      addMessage(STRINGS.greeting, 'bot');
      renderChips();
      opened = true;
    }
    input.focus();
  }
  function closePanel(){
    panel.classList.remove('is-open');
    fab.setAttribute('aria-expanded', 'false');
    fab.focus();
  }

  fab.addEventListener('click', () => {
    if(panel.classList.contains('is-open')) closePanel(); else openPanel();
  });
  closeBtn.addEventListener('click', closePanel);
  document.addEventListener('keydown', (e) => {
    if(e.key === 'Escape' && panel.classList.contains('is-open')) closePanel();
  });
  document.addEventListener('click', (e) => {
    if(!panel.classList.contains('is-open')) return;
    if(panel.contains(e.target) || fab.contains(e.target)) return;
    closePanel();
  });

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    const val = input.value.trim();
    if(!val) return;
    handleQuery(val);
    input.value = '';
  });
})();
