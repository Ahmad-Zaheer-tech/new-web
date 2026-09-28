# -*- coding: utf-8 -*-
import os, re, html, hashlib, json
from registry import TECH, CATS

SITE = '/home/claude/out'
SRC_OLD = '/home/claude/site'
SITE_URL = 'https://ahmadzaheer.dev'        # placeholder domain (kept from the previous build) — see config note
LUCIDE = '/home/claude/tools/node_modules/lucide-static/icons'

PHONE_DISPLAY = '0773 484 541'
PHONE_HREF = 'tel:0773484541'
EMAIL = 'ansarwaqef7@gmail.com'
WA_NUMBER = '93773484541'
SITES = [
    ('zaheer-tech.netlify.app', 'https://zaheer-tech.netlify.app'),
    ('online-exam-tech.netlify.app', 'https://online-exam-tech.netlify.app'),
    ('gaming-tech1.netlify.app', 'https://gaming-tech1.netlify.app'),
]
MAP_QUERY = 'Khair Khana, Kabul, Afghanistan'
ACCENTS = {'web': '#E34F26', 'data': '#38BDF8', 'teach': '#F59E0B', 'ai': '#A78BFA', 'design': '#00C4CC', 'office': '#60A5FA'}

# ---- current page context -------------------------------------------------
class Ctx:
    lang = 'en'
    key = 'index'          # canonical page key, e.g. 'about', 'projects/examina'
    abs_root = False       # True for 404 pages (root-absolute URLs)

C = Ctx()

def L(en, fa):
    return fa if C.lang == 'fa' else en

_FA_DIGITS = '۰۱۲۳۴۵۶۷۸۹'
def n(s):
    """Localise digits in prose (never in phone numbers / URLs)."""
    s = str(s)
    if C.lang != 'fa':
        return s
    return re.sub(r'[0-9]', lambda m: _FA_DIGITS[int(m.group(0))], s)

def esc(s):
    return html.escape(s, quote=True)

# ---- paths ----------------------------------------------------------------
def out_path(lang=None, key=None):
    lang = lang or C.lang
    key = key or C.key
    return ('fa/' if lang == 'fa' else '') + key + '.html'

def rel(target):
    """Relative URL from the current page to a site-root-relative path."""
    if C.abs_root:
        return '/' + target
    here = os.path.dirname(out_path()) or '.'
    return os.path.relpath(target, here).replace(os.sep, '/')

def href(key, frag=''):
    p = out_path(C.lang, key)
    return rel(p) + frag

def asset(p):
    return rel('assets/' + p)

def other_lang_href():
    other = 'en' if C.lang == 'fa' else 'fa'
    return rel(out_path(other, C.key))

# ---- icons ----------------------------------------------------------------
_icon_cache = {}
def ic(name, cls='ic'):
    if name not in _icon_cache:
        raw = open(f'{LUCIDE}/{name}.svg', encoding='utf8').read()
        inner = re.search(r'<svg[^>]*>(.*)</svg>', raw, re.S).group(1)
        inner = re.sub(r'\s+', ' ', inner).strip()
        _icon_cache[name] = inner
    return (f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{_icon_cache[name]}</svg>')

EXT = lambda: ic('arrow-up-right')

# ---- technology tiles -----------------------------------------------------
def tname(tid):
    t = TECH[tid]
    return t['fa'] if C.lang == 'fa' else t['en']

def tnote(tid):
    t = TECH[tid]
    return t.get('note_fa' if C.lang == 'fa' else 'note_en', '')

def _icon_html(tid, size=26):
    t = TECH[tid]
    if t.get('icon'):
        return f'<img src="{asset("tech/" + t["icon"])}" alt="" width="{size}" height="{size}" loading="lazy">'
    if t.get('monogram'):
        return f'<span class="tech-tile__mono" aria-hidden="true">{t["monogram"]}</span>'
    return ic(t['glyph'])

def tile(tid):
    t = TECH[tid]
    note = tnote(tid)
    note_html = f'<span class="tech-tile__note">{esc(note)}</span>' if note else ''
    plate = ' tech-tile__icon--plate' if t.get('plate') else ''
    inner = (f'<span class="tech-tile__icon{plate}">{_icon_html(tid)}</span>'
             f'<span class="tech-tile__text"><span class="tech-tile__name">{esc(tname(tid))}</span>{note_html}</span>')
    if t.get('url'):
        label = L(f'{t["en"]} — official site (opens in a new tab)', f'{t["fa"]} — وب‌سایت رسمی (در تب جدید باز می‌شود)')
        return (f'<a class="tech-tile tc-{tid}" href="{t["url"]}" target="_blank" rel="noopener noreferrer" aria-label="{esc(label)}">'
                f'{inner}<span class="tech-tile__go">{EXT()}</span></a>')
    return f'<div class="tech-tile tc-{tid}">{inner}</div>'

def mini(tid):
    t = TECH[tid]
    inner = _icon_html(tid, 20)
    plate = ' mini-icon--plate' if t.get('plate') else ''
    if t.get('url'):
        label = L(f'{t["en"]} — official site (opens in a new tab)', f'{t["fa"]} — وب‌سایت رسمی (در تب جدید باز می‌شود)')
        return (f'<a class="mini-icon{plate} tc-{tid}" href="{t["url"]}" target="_blank" rel="noopener noreferrer" '
                f'aria-label="{esc(label)}" title="{esc(tname(tid))}">{inner}</a>')
    return f'<span class="mini-icon{plate} tc-{tid}" role="img" aria-label="{esc(tname(tid))}" title="{esc(tname(tid))}">{inner}</span>'

def minis(ids):
    return '<div class="mini-icons">' + ''.join(mini(i) for i in ids) + '</div>'

def tags(items):
    return '<div class="project-tags">' + ''.join(f'<span class="tag">{esc(i)}</span>' for i in items) + '</div>'

def pf_tech(ids):
    return '<div class="pf__tech">' + ''.join(tile(i) for i in ids) + '</div>'

# ---- head / header / footer ----------------------------------------------
def theme_script():
    s = open(f'{SRC_OLD}/index.html', encoding='utf8').read()
    m = re.search(r'<script>(.*?)</script>', s, re.S)
    return m.group(1)

def csp():
    h = base64_sha256(theme_script())
    return ("default-src 'self'; "
            f"script-src 'self' 'sha256-{h}' https://www.googletagmanager.com; "
            "style-src 'self'; font-src 'self'; img-src 'self' data: https://www.google.com https://maps.gstatic.com; "
            "connect-src 'self' https://formspree.io https://www.google-analytics.com https://region1.google-analytics.com; "
            "frame-src https://www.google.com; base-uri 'self'; form-action 'self' https://formspree.io;")

def base64_sha256(text):
    import base64
    return base64.b64encode(hashlib.sha256(text.encode('utf8')).digest()).decode()

NAV = [
    ('index',          ('Home', 'خانه')),
    ('about',          ('About', 'درباره')),
    ('skills',         ('Skills', 'مهارت‌ها')),
    ('services',       ('Services', 'خدمات')),
    ('projects',       ('Projects', 'پروژه‌ها')),
    ('certifications', ('Certificates', 'گواهینامه‌ها')),
    ('contact',        ('Contact', 'تماس')),
]

def nav_current(key):
    if C.key == key: return True
    if key == 'projects' and C.key.startswith('projects/'): return True
    return False

ROLE = lambda: L('Computer & Technology Specialist', 'متخصص کمپیوتر و تکنالوژی')
NAME = lambda: L('Ahmad Zaheer', 'احمد ظهیر')

def head(title, desc, extra_css=(), jsonld=None, og_type='website', noindex=False):
    lang = C.lang
    dir_attr = ' dir="rtl"' if lang == 'fa' else ''
    canonical = f'{SITE_URL}/{out_path(lang)}'.replace('/index.html', '/')
    en_url = f'{SITE_URL}/{out_path("en")}'.replace('/index.html', '/')
    fa_url = f'{SITE_URL}/{out_path("fa")}'.replace('/index.html', '/')
    css = ['fonts', 'base', 'layout', 'components', 'pages', 'tech-brands'] + list(extra_css)
    css_links = '\n'.join(f'<link rel="stylesheet" href="{rel("css/" + c + ".css")}">' for c in css)
    ld = ''
    for block in (jsonld or []):
        ld += f'<script type="application/ld+json">\n{json.dumps(block, ensure_ascii=False, indent=2)}\n</script>\n'
    robots = 'noindex, follow' if noindex else 'index, follow'
    locale = 'fa_AF' if lang == 'fa' else 'en_US'
    alternates = '' if noindex else (
        f'<link rel="alternate" hreflang="en" href="{en_url}">\n'
        f'<link rel="alternate" hreflang="fa" href="{fa_url}">\n'
        f'<link rel="alternate" hreflang="x-default" href="{en_url}">\n')
    return f'''<!DOCTYPE html>
<html lang="{lang}"{dir_attr}>
<head>
<meta charset="UTF-8">
<script>{theme_script()}</script>
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="color-scheme" content="dark light">
<meta http-equiv="Content-Security-Policy" content="{csp()}">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<meta name="theme-color" content="#0B1210">
<meta name="robots" content="{robots}">
<meta property="og:type" content="{og_type}">
<meta property="og:url" content="{canonical}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:image" content="{SITE_URL}/assets/og-image.jpg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{locale}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE_URL}/assets/og-image.jpg">
<link rel="icon" type="image/svg+xml" href="{asset('favicon.svg')}">
<link rel="icon" type="image/png" sizes="32x32" href="{asset('icons/favicon-32x32.png')}">
<link rel="icon" type="image/png" sizes="16x16" href="{asset('icons/favicon-16x16.png')}">
<link rel="apple-touch-icon" sizes="180x180" href="{asset('icons/apple-touch-icon.png')}">
<link rel="manifest" href="{rel('manifest.json')}">
<link rel="canonical" href="{canonical}">
{alternates}<link rel="preload" href="{asset('fonts/' + ('Vazirmatn-Variable.woff2' if lang == 'fa' else 'ibm-plex-sans-latin-400-normal.woff2'))}" as="font" type="font/woff2" crossorigin>
{css_links}
{ld}</head>
<body>
'''

def person_jsonld():
    return {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Ahmad Zaheer",
        "alternateName": "احمد ظهیر",
        "url": f"{SITE_URL}/",
        "image": f"{SITE_URL}/assets/og-image.jpg",
        "jobTitle": "Computer & Technology Specialist",
        "description": "Web developer, database manager, and IT & English instructor based in Kabul, Afghanistan.",
        "email": f"mailto:{EMAIL}",
        "telephone": "+93773484541",
        "address": {"@type": "PostalAddress", "streetAddress": "Khairkhana, near Argentina Hotel",
                    "addressLocality": "Kabul", "addressCountry": "AF"},
        "alumniOf": {"@type": "EducationalOrganization", "name": "Afghanistan Institute of Technology (AIT)"},
        "knowsLanguage": ["fa", "en"],
        "knowsAbout": ["Web development", "HTML", "CSS", "JavaScript", "Tailwind CSS", "PHP", "SQL",
                       "SQL Server", "Oracle Database", "Database administration", "AI-assisted development",
                       "Generative AI", "AI agents and automation", "IT education", "English language teaching"],
        "sameAs": [u for _, u in SITES],
    }

def website_jsonld():
    return {"@context": "https://schema.org", "@type": "WebSite", "name": "Ahmad Zaheer — Portfolio",
            "url": f"{SITE_URL}/", "inLanguage": C.lang}

MM_ICON = {'index': 'house', 'about': 'user', 'skills': 'layers', 'services': 'briefcase',
           'projects': 'folder-kanban', 'certifications': 'award', 'contact': 'mail'}

def cur(k):
    return ' aria-current="page"' if nav_current(k) else ''

def header():
    links = ''.join(f'<a href="{href(k)}"{cur(k)}>{L(*label)}</a>' for k, label in NAV)
    mlinks = ''.join(
        f'<li><a class="mm-link mm-i-{k}" href="{href(k)}"{cur(k)}><span class="mm-ico">{ic(MM_ICON[k])}</span>'
        f'<span class="mm-label">{L(*label)}</span><span class="mm-go">{ic("chevron-right")}</span></a></li>'
        for k, label in NAV)
    switch = (f'<a class="lang-toggle" href="{other_lang_href()}" hreflang="en" lang="en" dir="ltr">EN</a>'
              if C.lang == 'fa' else
              f'<a class="lang-toggle" href="{other_lang_href()}" hreflang="fa" lang="fa">دری</a>')
    return f'''<a class="skip-link" href="#main">{L('Skip to content', 'رفتن به محتوا')}</a>
<div class="scroll-progress"></div>

<header class="site-header">
  <div class="nav-inner">
    <a class="brand" href="{href('index')}">
      <img class="brand-mark" src="{asset('brand-mark.png')}" alt="" aria-hidden="true">
      <span>{NAME()}<small>{ROLE()}</small></span>
    </a>
    <nav class="nav-links" aria-label="{L('Primary', 'اصلی')}">{links}</nav>
    <div class="nav-cta">
      <a class="btn btn--primary btn--small" href="{href('resume')}">{L('View CV', 'مشاهدهٔ رزومه')}</a>
      {switch}
      <button type="button" class="theme-toggle" id="theme-toggle" aria-label="{L('Switch between light and dark theme', 'تبدیل بین حالت روشن و تاریک')}" aria-pressed="false">
        <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.93 4.93l1.41 1.41M17.66 17.66l1.41 1.41M2 12h2M20 12h2M6.34 17.66l-1.41 1.41M19.07 4.93l-1.41 1.41"/></svg>
      </button>
      <button type="button" class="nav-toggle" aria-label="{L('Open menu', 'باز کردن منو')}" aria-expanded="false" aria-controls="mobile-menu">
        <span class="nav-toggle-lines"><span></span><span></span><span></span></span>
      </button>
    </div>
  </div>
</header>

<nav id="mobile-menu" class="mobile-menu" aria-label="{L('Mobile', 'موبایل')}">
  <ul class="mm-list">{mlinks}</ul>
  <a class="btn btn--primary btn--block mm-cta" href="{href('resume')}">{ic('file-text')}{L('View CV', 'مشاهدهٔ رزومه')}</a>
  <div class="mm-quick">
    <a class="mm-q mm-q--phone" href="{PHONE_HREF}">{ic('phone')}<span>{L('Call', 'تماس')}</span></a>
    <a class="mm-q mm-q--wa" href="https://wa.me/{WA_NUMBER}" target="_blank" rel="noopener noreferrer">{ic('message-circle')}<span>WhatsApp</span></a>
    <a class="mm-q mm-q--mail" href="mailto:{EMAIL}">{ic('mail')}<span>{L('Email', 'ایمیل')}</span></a>
  </div>
</nav>

<main id="main">
'''

def footer(scripts=()):
    fnav = ''.join(f'<li><a href="{href(k)}">{L(*label)}</a></li>' for k, label in NAV)
    fnav += f'<li><a href="{href("resume")}">{L("CV / Résumé", "رزومه (CV)")}</a></li>'
    site_links = ''.join(f'<li><a href="{u}" target="_blank" rel="noopener noreferrer"><span class="ltr">{d}</span></a></li>' for d, u in SITES)
    js = ['config', 'main', 'theme', 'whatsapp-widget', 'ask-ahmad-data', 'ask-ahmad', 'consent'] + list(scripts)
    script_tags = '\n'.join(f'<script src="{rel("js/" + j + ".js")}"></script>' for j in js)
    return f'''
</main>

<footer class="site-footer">
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <a class="brand" href="{href('index')}">
          <img class="brand-mark" src="{asset('brand-mark.png')}" alt="" aria-hidden="true">
          <span>{NAME()}</span>
        </a>
        <p>{L('Computer & technology specialist in Kabul — web development, databases, and IT & English instruction, in English and Dari.',
              'متخصص کمپیوتر و تکنالوژی در کابل — توسعهٔ وب، پایگاه‌داده و آموزش آی‌تی و انگلیسی، به دو زبان دری و انگلیسی.')}</p>
      </div>
      <div class="footer-col">
        <h2 class="footer-h">{L('Navigate', 'صفحات')}</h2>
        <ul>{fnav}</ul>
      </div>
      <div class="footer-col">
        <h2 class="footer-h">{L('Contact', 'تماس')}</h2>
        <ul>
          <li><a href="{PHONE_HREF}"><span class="ltr">{PHONE_DISPLAY}</span></a></li>
          <li><a href="mailto:{EMAIL}"><span class="ltr">{EMAIL}</span></a></li>
          <li>{L('Khairkhana, Kabul', 'خیرخانه، کابل')}</li>
        </ul>
      </div>
      <div class="footer-col">
        <h2 class="footer-h">{L('Live websites', 'وب‌سایت‌های فعال')}</h2>
        <ul>{site_links}</ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© <span data-year>2026</span> {NAME()}. {L('All rights reserved.', 'تمام حقوق محفوظ است.')}</p>
      <div class="footer-bottom-right">
        <div class="footer-social"></div>
        <a href="#top" class="to-top" data-to-top>{L('Back to top ↑', 'بازگشت به بالا ↑')}</a>
      </div>
    </div>
  </div>
</footer>

{script_tags}
</body>
</html>
'''

def status(kind='live'):
    label = {'live': L('Live', 'فعال')}[kind]
    return f'<span class="project-status" data-status="{kind}"><span class="dot"></span>{label}</span>'

def cta_band(title, primary=('contact', None), secondary=('resume', None)):
    p_label = primary[1] or L('Get in touch', 'در تماس شوید')
    s_label = secondary[1] or L('View CV', 'مشاهدهٔ رزومه')
    return f'''
  <section class="cta-band section--tight">
    <div class="wrap cta-band-inner">
      <h2 class="reveal">{title}</h2>
      <div class="reveal flex-actions">
        <a class="btn btn--primary" href="{href(primary[0])}">{p_label}</a>
        <a class="btn btn--ghost" href="{href(secondary[0])}">{s_label}</a>
      </div>
    </div>
  </section>
'''

def brand_css():
    """One class per technology: `.tc-<id>{--tc:<brand colour>}`."""
    out = ['/* generated from build/registry.py — one brand colour per technology */']
    for tid, t in TECH.items():
        out.append(f'.tc-{tid}{{ --tc: {t["color"]}; }}')
    for c in CATS:
        out.append(f'.sc-{c["id"]}{{ --sc: {c["color"]}; }}')
    for name, col in ACCENTS.items():
        out.append(f'.ac-{name}{{ --pc: {col}; }}')
    return '\n'.join(out) + '\n'
