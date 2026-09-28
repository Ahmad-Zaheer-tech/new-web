# -*- coding: utf-8 -*-
import os, re, json, shutil, sys
sys.path.insert(0, os.path.dirname(__file__))
from common import *
import pages_a, pages_b
from data import PROJECTS

_SCRIPT = re.compile(r'(<script\b[^>]*>.*?</script>)', re.S)
_AMP = re.compile(r'&(?!(?:[a-zA-Z][a-zA-Z0-9]*|#[0-9]+|#x[0-9a-fA-F]+);)')

def sanitize(doc):
    """Encode stray '&' and keep phone numbers on one line — outside <script> blocks only
    (the inline theme script is CSP-hashed and JSON-LD must stay raw JSON)."""
    parts = _SCRIPT.split(doc)
    for i in range(0, len(parts), 2):
        s = _AMP.sub('&amp;', parts[i])
        parts[i] = s.replace(PHONE_DISPLAY, PHONE_DISPLAY.replace(' ', '&nbsp;'))
    return ''.join(parts)

def write(path, content):
    if path.endswith('.html'):
        content = sanitize(content)
    full = os.path.join(SITE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w', encoding='utf8').write(content)

PAGES = [
    ('index', pages_a.home), ('about', pages_a.about), ('skills', pages_a.skills),
    ('services', pages_b.services), ('projects', pages_b.projects),
    ('certifications', pages_b.certifications), ('contact', pages_b.contact),
    ('resume', pages_b.resume), ('404', pages_b.not_found),
]

# ---- Ask-Ahmad knowledge base (search over REAL site content only) ---------
KB = [
 dict(id='who', kw=['who is ahmad','who are you','about you','introduce yourself','tell me about ahmad','ahmad zaheer','کیست','معرفی','شما کی هستید','احمد کیست','درباره احمد','خودت را معرفی کن'],
      en='Ahmad Zaheer is a computer and technology specialist in Kabul, Afghanistan: a computer science graduate (AIT) working in web development, database administration, and IT & English instruction, in English and Dari.',
      fa='احمد ظهیر متخصص کمپیوتر و تکنالوژی در کابل، افغانستان است: فارغ‌التحصیل کمپیوتر ساینس (AIT) که در توسعهٔ وب، مدیریت پایگاه‌داده و تدریس آی‌تی و انگلیسی کار می‌کند، به زبان‌های دری و انگلیسی.',
      link=('about.html','Read the full profile','خواندن پروفایل کامل')),
 dict(id='services', kw=['services','what do you do','what can you build','offer','what services','what can you help with','خدمات','چه کار می کنی','چیکار میکنی','چه خدماتی','چه می سازی'],
      en='Six services: websites and web apps, database design and administration, IT & English training, AI-assisted development and automation, design and image editing, and office documents with AI.',
      fa='شش خدمت: وب‌سایت و اپلیکیشن وب، طراحی و مدیریت پایگاه‌داده، آموزش آی‌تی و انگلیسی، توسعه با کمک هوش مصنوعی و اتوماسیون، طراحی و ویرایش تصویر، و اسناد اداری با هوش مصنوعی.',
      link=('services.html','See the services','مشاهدهٔ خدمات')),
 dict(id='skills', kw=['skills','technologies','tech stack','stack','tools','what technologies','مهارت','تکنالوژی','تکنولوژی','ابزار','با چی کار می کنی'],
      en='Web: HTML5, CSS3, JavaScript, Tailwind CSS, PHP. Databases: SQL, SQL Server, Oracle (and MySQL, taught in his academy). Java and C++ at fundamentals level. Plus AI tools, generative AI, AI agents and automation, Canva, Affinity, and the ICDL programs CIT and DIT.',
      fa='وب: HTML5، CSS3، جاوااسکریپت، Tailwind CSS، PHP. پایگاه‌داده: SQL، SQL Server، Oracle (و MySQL که در اکادمی او تدریس می‌شود). جاوا و C++ در سطح مبانی. به‌علاوهٔ ابزارهای هوش مصنوعی، هوش مصنوعی مولد، ایجنت‌ها و اتوماسیون، Canva، Affinity و برنامه‌های CIT و DIT از ICDL.',
      link=('skills.html','See all skills','مشاهدهٔ همهٔ مهارت‌ها')),
 dict(id='icdl', kw=['icdl','cit','dit','office','office package','typography','internet','network basics','computer techniques','practical project','آیسی دی ال','آفیس','تایپوگرافی','انترنت','مبانی شبکه','پروژه عملی','تکنیک'],
      en='CIT and DIT are programs of ICDL. They cover the Office package, a practical project, network basics and internet use, typography, and computer techniques.',
      fa='CIT و DIT بخش‌هایی از ICDL هستند و بستهٔ آفیس، پروژهٔ عملی، مبانی شبکه و استفاده از انترنت، تایپوگرافی و تکنیک‌های کمپیوتر را در بر می‌گیرند.',
      link=('skills.html#icdl','See the ICDL skills','مشاهدهٔ مهارت‌های ICDL')),
 dict(id='web', kw=['web development','website','html','css','javascript','php','tailwind','وب','وب سایت','جاوااسکریپت'],
      en='Ahmad builds static and dynamic websites and web apps with HTML, CSS, JavaScript, Tailwind CSS, and PHP — including two live platforms, a programming academy and an exam system.',
      fa='احمد وب‌سایت‌ها و اپلیکیشن‌های وب ایستا و پویا را با HTML، CSS، جاوااسکریپت، Tailwind CSS و PHP می‌سازد — از جمله دو پلتفورم فعال: یک اکادمی برنامه‌نویسی و یک سیستم امتحان.',
      link=('projects.html','See the projects','مشاهدهٔ پروژه‌ها')),
 dict(id='database', kw=['database','sql','sql server','oracle','phemis','payam','پایگاه داده','پایگاه‌داده','دیتابیس','پیام'],
      en='Ahmad managed the PHEMIS database system at Payam University for one year, and works with SQL, SQL Server, and Oracle.',
      fa='احمد یک سال سیستم پایگاه‌دادهٔ PHEMIS را در پوهنتون پیام مدیریت کرده و با SQL، SQL Server و Oracle کار می‌کند.',
      link=('about.html#experience','See the experience','مشاهدهٔ تجربهٔ کاری')),
 dict(id='human-languages', kw=['languages','what languages','dari','persian','english','speak','زبان','دری','فارسی','انگلیسی','به چه زبان'],
      en='Ahmad works in Dari/Persian (native) and English (professional; he has taught it). This site is available in both.',
      fa='احمد به دری/فارسی (مادری) و انگلیسی (حرفه‌ای؛ آن را تدریس هم کرده) کار می‌کند. این سایت به هر دو زبان موجود است.'),
 dict(id='location', kw=['where','location','based','kabul','address','map','khairkhana','کجا','موقعیت','آدرس','کابل','خیرخانه','نقشه'],
      en='Ahmad is based in Khairkhana, Kabul, Afghanistan, and works remotely on Kabul time (UTC+4:30). The Contact page has a map and directions link.',
      fa='احمد در خیرخانهٔ کابل، افغانستان مقیم است و از راه دور با وقت کابل (UTC+4:30) کار می‌کند. صفحهٔ تماس نقشه و لینک مسیریابی دارد.',
      link=('contact.html','Open the Contact page','رفتن به صفحهٔ تماس')),
 dict(id='contact', kw=['contact','reach','email','phone','whatsapp','get in touch','how do i contact','phone number','تماس','ایمیل','شماره','واتساپ','چطور تماس بگیرم','تلیفون'],
      en=f'Phone/WhatsApp: {PHONE_DISPLAY}. Email: {EMAIL}. Or use the contact form.',
      fa=f'تلیفون/واتساپ: {PHONE_DISPLAY}. ایمیل: {EMAIL}. یا از فورم تماس استفاده کنید.',
      link=('contact.html','Open the Contact page','رفتن به صفحهٔ تماس')),
 dict(id='resume', kw=['resume','cv','curriculum vitae','download resume','do you have a resume','رزومه','سی وی','دانلود رزومه'],
      en='Yes — a structured CV page with a downloadable PDF in English and Dari.',
      fa='بله — یک صفحهٔ رزومهٔ منظم با فایل PDF قابل دانلود به زبان‌های انگلیسی و دری.',
      link=('resume.html','View the CV','مشاهدهٔ رزومه')),
 dict(id='certifications', kw=['certifications','certificates','credentials','certified','qualifications','diploma','ait','education','گواهینامه','مدرک','گواهی','دیپلوم','تحصیلات'],
      en='A computer science diploma and transcript from AIT (Afghanistan Institute of Technology); computer certificates from Ashley Roshan Academy and Amozesh Educational Center; English certificates and diploma from Atarud Alingua, TECOL, and Amozesh; plus school graduation.',
      fa='دیپلوم و ترانسکریپت کمپیوتر ساینس از AIT (انستیتوت تکنالوژی افغانستان)؛ گواهینامه‌های کمپیوتر از اکادمی اشلی روشان و مرکز آموزشی آموزش؛ گواهینامه‌ها و دیپلوم انگلیسی از Atarud Alingua، TECOL و آموزش؛ به‌علاوهٔ فراغت از لیسه.',
      link=('certifications.html','See the certificates','مشاهدهٔ گواهینامه‌ها')),
 dict(id='experience', kw=['experience','work history','worked','jobs','career','teacher','instructor','تجربه','سابقه','کار کرده','معلم','استاد','مدرس'],
      en='Database manager at Payam University (1 year); freelance web and database developer; English teacher and image editor at Abraj (6 months); English and computer teacher at Ganja and Amozesh Educational Centers; English instructor at Badr Academy; computer instructor at Andisha-e-Noor Academy.',
      fa='مدیر پایگاه‌داده در پوهنتون پیام (۱ سال)؛ توسعه‌دهندهٔ مستقل وب و پایگاه‌داده؛ معلم انگلیسی و ویرایشگر تصویر در ابراج (۶ ماه)؛ معلم انگلیسی و کمپیوتر در مراکز آموزشی گنجه و آموزش؛ استاد انگلیسی در اکادمی بدر؛ استاد کمپیوتر در اکادمی اندیشه نور.',
      link=('about.html#experience','See the experience','مشاهدهٔ تجربهٔ کاری')),
 dict(id='projects', kw=['projects','portfolio','work samples','past work','live sites','websites','پروژه','پروژه ها','نمونه کار','وب سایت ها'],
      en='Three live websites: Ahmad Zaheer Academy (a free programming academy with 11 courses and 450+ lessons), Examina (an online and offline exam platform), and PULSAR (Gaming Tech), a Persian online store for gaming hardware.',
      fa='سه وب‌سایت فعال: آکادمی احمد ظهیر (اکادمی رایگان برنامه‌نویسی با ۱۱ دوره و بیش از ۴۵۰ درس)، Examina (پلتفورم امتحان آنلاین و آفلاین) و پالسار (Gaming Tech)، یک فروشگاه آنلاین فارسی برای تجهیزات گیمینگ.',
      link=('projects.html','See the projects','مشاهدهٔ پروژه‌ها')),
 dict(id='project-academy', kw=['academy','ahmad zaheer academy','zaheer tech','courses','lessons','learn programming','free courses','اکادمی','آکادمی','دوره','درس','یادگیری برنامه نویسی'],
      en='Ahmad Zaheer Academy is a free online academy: 11 courses and 450+ lessons from computer basics and Windows 11 to HTML, CSS, JavaScript, PHP, C++, and MySQL, with a code playground and a quiz in every lesson. Available in Dari, Pashto, and English.',
      fa='آکادمی احمد ظهیر یک اکادمی آنلاین رایگان است: ۱۱ دوره و بیش از ۴۵۰ درس از مبانی کمپیوتر و ویندوز ۱۱ تا HTML، CSS، جاوااسکریپت، PHP، C++ و MySQL، با پلی‌گراند کد و کوییز در هر درس. به سه زبان دری، پشتو و انگلیسی.',
      link=('projects/zaheer-academy.html','Academy details','جزئیات اکادمی')),
 dict(id='project-examina', kw=['examina','exam','exams','online exam','offline exam','test platform','امتحان','آزمون','امتحان آنلاین','ایگزامینا'],
      en='Examina is an exam platform with timed online exams (live countdown, question navigator, instant grading) and print-ready offline exams with answer keys. Answers stay in the browser; nothing is uploaded.',
      fa='Examina یک پلتفورم امتحان است با امتحان‌های آنلاین زمان‌دار (شمارندهٔ زنده، ناوبر سوالات، نمره‌دهی فوری) و امتحان‌های آفلاین آمادهٔ چاپ همراه با کلید پاسخ. پاسخ‌ها در مرورگر می‌مانند؛ چیزی آپلود نمی‌شود.',
      link=('projects/examina.html','Examina details','جزئیات Examina')),
 dict(id='project-gaming', kw=['gaming','gaming tech','pulsar','store','shop','games','game website','بازی','گیمینگ','پالسار','فروشگاه'],
      en='PULSAR (Gaming Tech) is a Persian, right-to-left online store for gaming hardware — PCs, laptops, monitors, keyboards, mice, headsets — with deals, wishlist, cart, sign-in, and product comparison. Live at gaming-tech1.netlify.app.',
      fa='پالسار (Gaming Tech) یک فروشگاه آنلاین فارسی و راست‌به‌چپ برای تجهیزات گیمینگ است — کامپیوتر، لپ‌تاپ، مانیتور، کیبورد، ماوس و هدست — با تخفیف‌ها، علاقه‌مندی‌ها، سبد خرید، ورود و مقایسهٔ محصولات. در gaming-tech1.netlify.app فعال است.',
      link=('projects/pulsar.html','PULSAR details','جزئیات پالسار')),
 dict(id='teaching', kw=['teach','teaching','training','courses you teach','what do you teach','instruction','تدریس','آموزش','چه تدریس می کنی'],
      en='English and computer courses at five institutions, and a free online academy covering computer basics, Windows 11, HTML, CSS, JavaScript, PHP, C++, MySQL, AI tools, and English.',
      fa='تدریس انگلیسی و کمپیوتر در پنج نهاد آموزشی، و یک اکادمی آنلاین رایگان که مبانی کمپیوتر، ویندوز ۱۱، HTML، CSS، جاوااسکریپت، PHP، C++، MySQL، ابزارهای هوش مصنوعی و انگلیسی را پوشش می‌دهد.',
      link=('about.html#teaching','What I teach','آنچه تدریس می‌کنم')),
 dict(id='ai', kw=['ai','artificial intelligence','generative ai','ai agents','automation','هوش مصنوعی','اتوماسیون','ایجنت'],
      en='AI is used in four ways: AI-assisted development (apps and sites), AI for office documents, generative AI for image and video, and AI agents and automation.',
      fa='هوش مصنوعی در چهار حوزه استفاده می‌شود: توسعه با کمک هوش مصنوعی (اپلیکیشن و سایت)، هوش مصنوعی برای اسناد اداری، هوش مصنوعی مولد برای تصویر و ویدیو، و ایجنت‌ها و اتوماسیون.',
      link=('skills.html','See the AI skills','مشاهدهٔ مهارت‌های هوش مصنوعی')),
 dict(id='pricing', kw=['pricing','price','cost','how much','rates','fee','هزینه','قیمت','چقدر','نرخ'],
      en='Pricing depends on scope and timeline, so it is not listed. Every quote is given in writing after a short discovery call and before work starts.',
      fa='قیمت به محدوده و زمان‌بندی کار بستگی دارد، پس فهرست نشده است. هر پیشنهاد قیمت به‌صورت مکتوب پس از یک گفتگوی کوتاه و پیش از شروع کار ارائه می‌شود.',
      link=('services.html','See how it works','دیدن روند کار')),
 dict(id='availability', kw=['availability','available','hire','remote','timezone','time zone','response time','دسترسی','در دسترس','استخدام','از راه دور','ساعت کاری'],
      en='Ahmad is open to new work, remotely, on Kabul time (UTC+4:30). New inquiries are usually answered within 1–2 business days.',
      fa='احمد برای کار جدید و از راه دور، با وقت کابل (UTC+4:30) آماده است. به درخواست‌های جدید معمولاً ظرف ۱ تا ۲ روز کاری پاسخ داده می‌شود.',
      link=('contact.html','Open the Contact page','رفتن به صفحهٔ تماس')),
 dict(id='process', kw=['process','how does a project start','how do we start','steps','workflow','روند','مراحل','چطور شروع','یک پروژه چطور شروع می شود'],
      en='Four steps: a discovery conversation, a scope and plan, the build with regular check-ins, and a documented handover with a support window.',
      fa='چهار مرحله: گفتگوی آشنایی، محدوده و برنامه، ساخت همراه با بررسی‌های منظم، و تحویل مستند همراه با بازهٔ پشتیبانی.',
      link=('services.html','See the process','دیدن روند کار')),
 dict(id='site-language', kw=['is this site in persian','dari version','switch language','persian site','نسخه دری','سایت به دری','تعویض زبان'],
      en='Yes — the whole site has a Dari (right-to-left) version. Use the language button in the header to switch.',
      fa='بله — کل سایت نسخهٔ دری (راست‌به‌چپ) دارد. برای تعویض از دکمهٔ زبان در هدر استفاده کنید.'),
]

def kb_js():
    entries = []
    for e in KB:
        h, le, lf = e.get('link', (None, None, None))
        link = f"link: {{ href: {json.dumps(h)}, label_en: {json.dumps(le, ensure_ascii=False)}, label_fa: {json.dumps(lf, ensure_ascii=False)} }}," if h else ''
        entries.append(f"""  {{
    id: {json.dumps(e['id'])},
    keywords: {json.dumps(e['kw'], ensure_ascii=False)},
    answer_en: {json.dumps(e['en'], ensure_ascii=False)},
    answer_fa: {json.dumps(e['fa'], ensure_ascii=False)},
    {link}
  }},""")
    return ("""/* ==========================================================================
   ask-ahmad-data.js — the ONLY source of truth for what "Ask Ahmad" can
   answer. Every entry restates real content that exists elsewhere on this
   site (About, Skills, Projects, Certificates, Contact). No invented facts.
   Generated by the site build; edit build/build.py, not this file.
   ========================================================================== */
window.ASK_AHMAD_KB = [
""" + '\n'.join(entries) + "\n];\n")

def sitemap():
    keys = [k for k, _ in PAGES if k != '404'] + ['projects/' + p['key'] for p in PROJECTS if p['detail']]
    urls = []
    for k in keys:
        loc_en = f'{SITE_URL}/' + ('' if k == 'index' else k + '.html')
        loc_fa = f'{SITE_URL}/fa/' + ('' if k == 'index' else k + '.html')
        pr = '1.0' if k == 'index' else '0.8'
        for loc in (loc_en, loc_fa):
            urls.append(f'''  <url>
    <loc>{loc}</loc>
    <xhtml:link rel="alternate" hreflang="en" href="{loc_en}"/>
    <xhtml:link rel="alternate" hreflang="fa" href="{loc_fa}"/>
    <lastmod>2026-09-20</lastmod>
    <priority>{pr}</priority>
  </url>''')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<!-- Replace https://ahmadzaheer.dev with the real domain once deployed (search build/common.py SITE_URL). -->\n'
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
            + '\n'.join(urls) + '\n</urlset>\n')

def main():
    # pages
    for lang in ('en', 'fa'):
        C.lang = lang
        for key, fn in PAGES:
            C.abs_root = False
            html_out = fn()
            write(out_path(lang, key), html_out)
        for p in PROJECTS:
            if p['detail']:
                C.abs_root = False
                write(out_path(lang, 'projects/' + p['key']), pages_b.project_detail(p))
    # generated assets
    write('css/tech-brands.css', brand_css())
    write('js/ask-ahmad-data.js', kb_js())
    write('sitemap.xml', sitemap())
    # manifest
    m = json.load(open(f'{SITE}/manifest.json', encoding='utf8'))
    m['name'] = 'Ahmad Zaheer — Computer & Technology Specialist'
    m['description'] = 'Portfolio and CV of Ahmad Zaheer: web development, database administration, and IT & English education.'
    write('manifest.json', json.dumps(m, ensure_ascii=False, indent=2) + '\n')
    print('built OK')

if __name__ == '__main__':
    main()
