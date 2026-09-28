/* ==========================================================================
   config.js — every value that's likely to change lives here, once.
   Edit this file when you get real accounts/IDs; nothing else needs to change.
   Must load BEFORE main.js, contact.js, consent.js on every page.
   ========================================================================== */
window.SITE_CONFIG = {
  // WhatsApp number in international format, no "+", no leading 0.
  // Afghanistan country code is 93; local 0773 484 541 -> 93773484541.
  whatsappNumber: '93773484541',
  whatsappDefaultMessage: 'Hi Ahmad, I found your portfolio and would like to talk about a project.',
  whatsappDefaultMessageFa: 'سلام احمد، پورتفولیوی شما را دیدم و می‌خواهم دربارهٔ یک پروژه صحبت کنم.',

  // Formspree: sign up free at https://formspree.io, create a form, and
  // paste the form ID here (the part after /f/ in your form's endpoint).
  // Until this is a real ID, the contact form will show a clear setup
  // notice instead of silently pretending to send.
  // Contact form backend. 'netlify' (default) = Netlify Forms: nothing to configure, submissions appear
  // in Netlify > Forms. Use 'formspree' only if you prefer it (then set formspreeFormId below).
  formBackend: 'netlify',
  formspreeFormId: 'YOUR_FORM_ID',

  // Google Analytics 4 Measurement ID, e.g. 'G-ABC1234XYZ'.
  // Create a free GA4 property at https://analytics.google.com to get one.
  // Analytics only loads after the visitor accepts the cookie notice.
  gaMeasurementId: 'G-XXXXXXXXXX',

  // Map on the Contact page. A place name works; for the exact spot, paste
  // coordinates from Google Maps (right-click the spot -> click the numbers), e.g. '34.5700,69.1300'.
  mapQuery: 'Khair Khana, Kabul, Afghanistan',

  contactEmail: 'ansarwaqef7@gmail.com',
  contactPhoneDisplay: '0773 484 541',
  contactPhoneHref: 'tel:0773484541',

  // Leave any of these empty ('') to hide that icon on the Contact page
  // until you have a real profile URL to put there.
  socialLinks: {
    linkedin: '',
    github: '',
    twitter: '',
  },
};
