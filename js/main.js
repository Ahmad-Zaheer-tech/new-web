/* ==========================================================================
   main.js — shared site behavior (runs on every page)
   ========================================================================== */
(() => {
  'use strict';

  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const root = document.documentElement;

  /* ---- Scroll progress bar --------------------------------------------- */
  const progress = document.querySelector('.scroll-progress');
  function updateProgress(){
    if(!progress) return;
    const h = document.documentElement;
    const scrolled = h.scrollTop;
    const height = h.scrollHeight - h.clientHeight;
    const pct = height > 0 ? (scrolled / height) * 100 : 0;
    progress.style.width = pct + '%';
  }

  /* ---- Header: scroll-aware show/hide + scrolled state ------------------ */
  const header = document.querySelector('.site-header');
  let lastY = window.scrollY;
  function updateHeader(){
    if(!header) return;
    const y = window.scrollY;
    header.classList.toggle('is-scrolled', y > 12);
    if(y > lastY && y > var_navH()){
      header.classList.add('is-hidden');
    } else {
      header.classList.remove('is-hidden');
    }
    lastY = y;
  }
  function var_navH(){
    return parseInt(getComputedStyle(root).getPropertyValue('--nav-h')) || 76;
  }

  let ticking = false;
  function onScroll(){
    if(!ticking){
      window.requestAnimationFrame(() => {
        updateProgress();
        updateHeader();
        ticking = false;
      });
      ticking = true;
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  updateProgress();
  updateHeader();

  /* ---- Mobile menu -------------------------------------------------- */
  const navToggle = document.querySelector('.nav-toggle');
  const mobileMenu = document.querySelector('.mobile-menu');
  if(navToggle && mobileMenu){
    navToggle.addEventListener('click', () => {
      const open = navToggle.getAttribute('aria-expanded') === 'true';
      navToggle.setAttribute('aria-expanded', String(!open));
      mobileMenu.classList.toggle('is-open', !open);
      document.body.style.overflow = !open ? 'hidden' : '';
    });
    mobileMenu.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        navToggle.setAttribute('aria-expanded', 'false');
        mobileMenu.classList.remove('is-open');
        document.body.style.overflow = '';
      });
    });
    // If the window grows past the menu breakpoint while it is open, close it and release the scroll lock.
    const desktopNav = window.matchMedia('(min-width: 1121px)');
    const closeOnDesktop = (e) => {
      if(e.matches){
        navToggle.setAttribute('aria-expanded', 'false');
        mobileMenu.classList.remove('is-open');
        document.body.style.overflow = '';
      }
    };
    if(desktopNav.addEventListener) desktopNav.addEventListener('change', closeOnDesktop);
    window.addEventListener('keydown', (e) => {
      if(e.key === 'Escape' && mobileMenu.classList.contains('is-open')){
        navToggle.setAttribute('aria-expanded', 'false');
        mobileMenu.classList.remove('is-open');
        document.body.style.overflow = '';
        navToggle.focus();
      }
    });
  }

  /* ---- Scroll reveal (IntersectionObserver) ------------------------------ */
  const revealEls = document.querySelectorAll('.reveal');
  if('IntersectionObserver' in window && revealEls.length){
    const io = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if(entry.isIntersecting){
          entry.target.classList.add('is-visible');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.15, rootMargin: '0px 0px -60px 0px' });
    revealEls.forEach(el => io.observe(el));
  } else {
    revealEls.forEach(el => el.classList.add('is-visible'));
  }

  /* ---- Hero stat count-up (numbers animate in once visible) --------------
     Handles both Latin and Persian-Arabic digits, and a "+" on either
     side, so it works unmodified on the English and Dari homepages. */
  const heroStats = document.querySelectorAll('.hero-meta strong');
  if(heroStats.length){
    const faDigits = '۰۱۲۳۴۵۶۷۸۹';
    const toLatinDigits = (s) => s.replace(/[۰-۹]/g, (d) => faDigits.indexOf(d));
    const toFaDigits = (n) => String(n).replace(/[0-9]/g, (d) => faDigits[+d]);

    heroStats.forEach((el) => {
      const raw = el.textContent.trim();
      const isFa = /[۰-۹]/.test(raw);
      const hasPlus = raw.includes('+');
      const plusBefore = hasPlus && raw.indexOf('+') === 0;
      const target = parseInt(toLatinDigits(raw.replace('+', '')), 10);
      if(Number.isNaN(target)) return;

      const format = (n) => {
        let s = isFa ? toFaDigits(n) : String(n);
        if(hasPlus) s = plusBefore ? '+' + s : s + '+';
        return s;
      };

      if(prefersReduced){
        el.textContent = format(target);
        return;
      }

      el.textContent = format(0);
      const io = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if(!entry.isIntersecting) return;
          io.unobserve(el);
          const duration = 1100;
          const start = performance.now();
          function tick(now){
            const p = Math.min((now - start) / duration, 1);
            const eased = 1 - Math.pow(1 - p, 3);
            el.textContent = format(Math.round(eased * target));
            if(p < 1) requestAnimationFrame(tick);
          }
          requestAnimationFrame(tick);
        });
      }, { threshold: 0.5 });
      io.observe(el);
    });
  }

  /* ---- Skill bar fill on reveal ------------------------------------------ */
  const skillBars = document.querySelectorAll('.skill-bar-fill');
  if('IntersectionObserver' in window && skillBars.length){
    const io2 = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if(entry.isIntersecting){
          const target = entry.target;
          target.style.width = target.dataset.level + '%';
          io2.unobserve(target);
        }
      });
    }, { threshold: 0.4 });
    skillBars.forEach(el => io2.observe(el));
  } else {
    skillBars.forEach(el => el.style.width = el.dataset.level + '%');
  }

  /* ---- Magnetic buttons (desktop, pointer-fine only) --------------------- */
  const magnets = document.querySelectorAll('.magnetic');
  if(!prefersReduced && window.matchMedia('(hover: hover) and (pointer: fine)').matches){
    magnets.forEach(el => {
      el.addEventListener('mousemove', (e) => {
        const r = el.getBoundingClientRect();
        const mx = (e.clientX - r.left - r.width / 2) * 0.25;
        const my = (e.clientY - r.top - r.height / 2) * 0.35;
        el.style.setProperty('--mx', mx + 'px');
        el.style.setProperty('--my', my + 'px');
      });
      el.addEventListener('mouseleave', () => {
        el.style.setProperty('--mx', '0px');
        el.style.setProperty('--my', '0px');
      });
    });
  }

  /* ---- Custom cursor (desktop only) --------------------------------------- */
  if(!prefersReduced && window.matchMedia('(hover: hover) and (pointer: fine)').matches){
    const dot = document.createElement('div');
    dot.className = 'cursor-dot';
    document.body.appendChild(dot);
    let shown = false;
    window.addEventListener('mousemove', (e) => {
      if(!shown){ dot.classList.add('is-active'); shown = true; }
      dot.style.left = e.clientX + 'px';
      dot.style.top = e.clientY + 'px';
    });
    document.querySelectorAll('a, button, .project-card, input, textarea').forEach(el => {
      el.addEventListener('mouseenter', () => dot.classList.add('is-hover'));
      el.addEventListener('mouseleave', () => dot.classList.remove('is-hover'));
    });
    document.addEventListener('mouseleave', () => dot.classList.remove('is-active'));
  }

  /* ---- Subtle hero parallax on pointer move ------------------------------- */
  const heroVisual = document.querySelector('.hero-visual');
  const heroSection = document.querySelector('.hero');
  if(heroVisual && heroSection && !prefersReduced && window.matchMedia('(hover: hover) and (pointer: fine)').matches){
    heroSection.addEventListener('mousemove', (e) => {
      const r = heroSection.getBoundingClientRect();
      const px = (e.clientX - r.left) / r.width - 0.5;
      const py = (e.clientY - r.top) / r.height - 0.5;
      heroVisual.style.transform = `translate(${px * 14}px, ${py * 14}px)`;
    });
    heroSection.addEventListener('mouseleave', () => {
      heroVisual.style.transform = 'translate(0,0)';
    });
  }

  /* ---- Back to top -------------------------------------------------------- */
  document.querySelectorAll('[data-to-top]').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({ top: 0, behavior: prefersReduced ? 'auto' : 'smooth' });
    });
  });

  /* ---- Footer year --------------------------------------------------------- */
  const yearEl = document.querySelector('[data-year]');
  if(yearEl) yearEl.textContent = new Date().getFullYear();

  /* ---- Footer social links (honest empty state) -------------------------
     Same pattern as the Contact page: an icon only appears once a real
     profile URL exists in config.js. Nothing is ever a placeholder link. */
  const footerSocial = document.querySelector('.footer-social');
  if(footerSocial && window.SITE_CONFIG && window.SITE_CONFIG.socialLinks){
    const social = window.SITE_CONFIG.socialLinks;
    footerSocial.querySelectorAll('[data-social]').forEach(link => {
      const url = social[link.dataset.social];
      if(url){
        link.href = url;
        link.target = '_blank';
        link.rel = 'noopener';
      } else {
        link.remove();
      }
    });
    if(!footerSocial.children.length) footerSocial.remove();
  }
})();
