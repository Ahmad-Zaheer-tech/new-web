/* ==========================================================================
   contact-fa.js — Dari-localized version of contact.js.
   Same logic and behavior as js/contact.js; only user-facing strings
   are translated so the Persian contact page doesn't mix languages.
   ========================================================================== */
(() => {
  'use strict';

  const form = document.querySelector('#contact-form');
  if(!form) return;

  const waLink = document.querySelector('#contact-whatsapp-link');
  if(waLink && window.SITE_CONFIG && window.SITE_CONFIG.whatsappNumber){
    const msg = encodeURIComponent(window.SITE_CONFIG.whatsappDefaultMessage || 'Hello!');
    waLink.href = `https://wa.me/${window.SITE_CONFIG.whatsappNumber}?text=${msg}`;
  }

  const social = (window.SITE_CONFIG && window.SITE_CONFIG.socialLinks) || {};
  document.querySelectorAll('#social-row [data-social]').forEach(link => {
    const url = social[link.dataset.social];
    if(url){
      link.href = url;
      link.target = '_blank';
      link.rel = 'noopener';
    } else {
      link.remove();
    }
  });
  const socialRow = document.querySelector('#social-row');
  if(socialRow && !socialRow.children.length) socialRow.remove();

  const status = document.querySelector('#form-status');
  const submitBtn = form.querySelector('[type="submit"]');

  const validators = {
    name: (v) => v.trim().length >= 2 || 'نام کامل خود را وارد کنید.',
    email: (v) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim()) || 'یک ایمیل معتبر وارد کنید.',
    subject: (v) => v.trim().length >= 3 || 'موضوع کوتاهی برای پیام بنویسید.',
    message: (v) => v.trim().length >= 12 || 'کمی بیشتر بنویسید — حداقل ۱۲ حرف.',
  };

  function fieldWrap(input){
    return input.closest('.field');
  }

  function validateField(input){
    const rule = validators[input.name];
    if(!rule) return true;
    const result = rule(input.value);
    const wrap = fieldWrap(input);
    const errorEl = wrap.querySelector('.field-error');
    if(result === true){
      wrap.classList.remove('has-error');
      input.setAttribute('aria-invalid', 'false');
      return true;
    } else {
      wrap.classList.add('has-error');
      input.setAttribute('aria-invalid', 'true');
      if(errorEl) errorEl.textContent = result;
      return false;
    }
  }

  form.querySelectorAll('input, textarea').forEach(input => {
    input.addEventListener('blur', () => validateField(input));
    input.addEventListener('input', () => {
      if(fieldWrap(input).classList.contains('has-error')) validateField(input);
    });
  });

  function submitForm(data){
    const cfg = window.SITE_CONFIG || {};

    // Optional: Formspree, only if explicitly chosen in js/config.js.
    if(cfg.formBackend === 'formspree'){
      const formId = cfg.formspreeFormId;
      if(!formId || formId === 'YOUR_FORM_ID') return Promise.reject(new Error('NOT_CONFIGURED'));
      return fetch(`https://formspree.io/f/${formId}`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
        body: JSON.stringify(data),
      }).then(res => {
        if(!res.ok) throw new Error('SEND_FAILED');
        return res;
      });
    }

    // Default: Netlify Forms. Netlify finds the form (data-netlify) in the static HTML at
    // deploy time and stores each submission in the site's Forms tab. No third-party ID needed.
    const body = new URLSearchParams(new FormData(form)).toString();
    return fetch('/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body,
    }).then(res => {
      if(!res.ok) throw new Error('SEND_FAILED');
      return res;
    });
  }

  form.addEventListener('submit', async (e) => {
    e.preventDefault();

    const honeypot = form.querySelector('input[name="company"]');
    if(honeypot && honeypot.value){ return; }

    const inputs = Array.from(form.querySelectorAll('input[name], textarea[name]'))
      .filter(el => validators[el.name]);
    const results = inputs.map(validateField);
    const allValid = results.every(Boolean);

    if(!allValid){
      status.className = 'form-status is-error';
      status.textContent = 'لطفاً فیلدهای مشخص‌شده را پیش از ارسال اصلاح کنید.';
      const firstInvalid = form.querySelector('.field.has-error input, .field.has-error textarea');
      if(firstInvalid) firstInvalid.focus();
      return;
    }

    submitBtn.disabled = true;
    submitBtn.textContent = 'در حال ارسال…';

    const data = Object.fromEntries(new FormData(form).entries());
    try {
      await submitForm(data);
      status.className = 'form-status is-success';
      status.textContent = 'پیام ارسال شد — سپاسگزارم. احمد معمولاً ظرف چند روز پاسخ می‌دهد.';
      form.reset();
    } catch (err) {
      if(err && err.message === 'NOT_CONFIGURED'){
        status.className = 'form-status is-error';
        status.innerHTML = `فورم پیام هنوز وصل نشده است. لطفاً مستقیماً از طریق
          <a href="mailto:${(window.SITE_CONFIG && window.SITE_CONFIG.contactEmail) || 'ansarwaqef7@gmail.com'}">ایمیل</a>
          یا <a href="${(window.SITE_CONFIG && window.SITE_CONFIG.contactPhoneHref) || 'tel:'}">تلیفون</a> تماس بگیرید.`;
      } else {
        status.className = 'form-status is-error';
        status.textContent = 'مشکلی در ارسال پیش آمد. لطفاً دوباره تلاش کنید یا از شماره تلیفون بالا استفاده کنید.';
      }
    } finally {
      submitBtn.disabled = false;
      submitBtn.textContent = 'ارسال پیام';
    }
  });
})();
