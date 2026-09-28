# -*- coding: utf-8 -*-
from common import *
from data import *
from registry import TECH, CATS
from pages_a import pf_card, cred_card, xp_item

# ---------------------------------------------------------------- SERVICES
SERVICES = [
    dict(ac='web', glyph='layout-dashboard',
         t=('Websites & web apps', 'وب‌سایت و اپلیکیشن وب'),
         d=('Static and dynamic websites, landing pages, and web platforms — hand-coded in HTML, CSS, JavaScript, and Tailwind CSS, with PHP where a server side is needed. Right-to-left (Dari) layouts built natively.',
            'وب‌سایت‌های ایستا و پویا، صفحات فرود و پلتفورم‌های وب — با کد دستی در HTML، CSS، جاوااسکریپت و Tailwind CSS، و با PHP در جایی که سمت سرور لازم است. چیدمان راست‌به‌چپ (دری) از پایه ساخته می‌شود.'),
         tags=(('Static & dynamic sites', 'سایت ایستا و پویا'), ('Web apps', 'اپلیکیشن وب'), ('RTL / bilingual', 'راست‌به‌چپ / دوزبانه')),
         ids=['html5', 'css3', 'javascript', 'tailwind', 'php']),
    dict(ac='data', glyph='database',
         t=('Database design & administration', 'طراحی و مدیریت پایگاه‌داده'),
         d=('Database design, SQL queries, and day-to-day administration in SQL Server, Oracle, and SQL — with the discipline of a year running a university\'s PHEMIS database system.',
            'طراحی پایگاه‌داده، کوئری‌نویسی SQL و مدیریت روزمره در SQL Server، Oracle و SQL — با انضباط یک سال مدیریت سیستم پایگاه‌دادهٔ PHEMIS یک پوهنتون.'),
         tags=(('Design', 'طراحی'), ('SQL queries', 'کوئری SQL'), ('Administration', 'مدیریت')),
         ids=['sql', 'sqlserver', 'oracle']),
    dict(ac='teach', glyph='graduation-cap',
         t=('IT & English training', 'آموزش آی‌تی و انگلیسی'),
         d=('Structured courses in computer basics, Windows, web development, databases, and English — taught in the classroom or as self-paced online lessons with exercises and quizzes.',
            'دوره‌های منظم در مبانی کمپیوتر، ویندوز، توسعهٔ وب، پایگاه‌داده و انگلیسی — در صنف درس یا به‌صورت درس‌های آنلاین خودآموز همراه با تمرین و کوییز.'),
         tags=(('Course design', 'طراحی دوره'), ('Classroom teaching', 'تدریس حضوری'), ('Online lessons', 'درس‌های آنلاین')),
         ids=['basics', 'windows11', 'mysql', 'english']),
    dict(ac='ai', glyph='bot',
         t=('AI-assisted development & automation', 'توسعه با کمک هوش مصنوعی و اتوماسیون'),
         d=('Faster builds of apps and websites with AI tools, plus AI agents and automations that take over repeat tasks.',
            'ساخت سریع‌تر اپلیکیشن و وب‌سایت با ابزارهای هوش مصنوعی، به‌علاوهٔ ایجنت‌ها و اتوماسیون‌هایی که کارهای تکراری را بر عهده می‌گیرند.'),
         tags=(('AI-built apps & sites', 'اپ و سایت با هوش مصنوعی'), ('Agents', 'ایجنت‌ها'), ('Workflow automation', 'اتوماسیون کار')),
         ids=['ai-build', 'ai-agents', 'ai-tools']),
    dict(ac='design', glyph='palette',
         t=('Design & image editing', 'طراحی و ویرایش تصویر'),
         d=('Graphic layouts and image editing in Canva and Affinity, plus generative AI for image and video when a project calls for it.',
            'طراحی گرافیکی و ویرایش تصویر با Canva و Affinity، به‌علاوهٔ هوش مصنوعی مولد برای تصویر و ویدیو در جایی که پروژه نیاز دارد.'),
         tags=(('Graphic layouts', 'چیدمان گرافیکی'), ('Image editing', 'ویرایش تصویر'), ('Generative media', 'رسانهٔ مولد')),
         ids=['canva', 'affinity', 'gen-ai']),
    dict(ac='office', glyph='file-text',
         t=('Office documents with AI', 'اسناد اداری با هوش مصنوعی'),
         d=('Word documents and other office files prepared faster with AI assistance — formatted, consistent, and ready to use.',
            'اسناد ورد و دیگر فایل‌های اداری با کمک هوش مصنوعی سریع‌تر آماده می‌شوند — قالب‌بندی‌شده، یکدست و آمادهٔ استفاده.'),
         tags=(('Word documents', 'اسناد ورد'), ('Formatting', 'قالب‌بندی')),
         ids=['ai-office']),
]

def services():
    C.key = 'services'
    title = L('Services — Web, Databases, Training & AI | Ahmad Zaheer', 'خدمات — وب، پایگاه‌داده، آموزش و هوش مصنوعی | احمد ظهیر')
    desc = L('Services by Ahmad Zaheer: websites and web apps, database design and administration, IT & English training, AI-assisted development and automation, and design.',
             'خدمات احمد ظهیر: وب‌سایت و اپلیکیشن وب، طراحی و مدیریت پایگاه‌داده، آموزش آی‌تی و انگلیسی، توسعه با کمک هوش مصنوعی و اتوماسیون، و طراحی.')
    h = head(title, desc, jsonld=[person_jsonld()]) + header()
    cards = ''.join(f'''
      <article class="svc ac-{s['ac']} reveal">
        <span class="svc__icon">{ic(s['glyph'])}</span>
        <h3>{L(*s['t'])}</h3>
        <p>{L(*s['d'])}</p>
        {tags([L(*x) for x in s['tags']])}
        {minis(s['ids'])}
      </article>''' for s in SERVICES)
    steps = [
        (L('Discovery', 'آشنایی'), L('A short conversation (or a written brief) about what you need built, fixed, or taught — and whether I am the right fit.',
                                       'یک گفتگوی کوتاه (یا شرح مکتوب) دربارهٔ اینکه چه چیزی باید ساخته، اصلاح یا آموزش داده شود — و اینکه آیا من فرد مناسب هستم.')),
        (L('Scope & plan', 'محدوده و برنامه'), L('A plain-language outline of what will be delivered, in what order, and roughly how long it takes — before either side commits.',
                                                  'یک طرح به زبان ساده از آنچه تحویل داده می‌شود، به چه ترتیبی و تقریباً در چه مدتی — پیش از تعهد هر دو طرف.')),
        (L('Build', 'ساخت'), L('Regular check-ins instead of silence until the end, so feedback arrives while it can still change the work.',
                               'بررسی‌های منظم به‌جای سکوت تا پایان، تا بازخورد وقتی برسد که هنوز بتواند کار را تغییر دهد.')),
        (L('Handover', 'تحویل'), L('Clear documentation of what was built and how to maintain it, plus a defined window of after-launch support.',
                                   'مستندات روشن از آنچه ساخته شده و چگونگی نگهداری آن، به‌همراه یک بازهٔ مشخص پشتیبانی پس از راه‌اندازی.')),
    ]
    st = ''.join(f'<article class="step reveal"><h3>{t}</h3><p>{d}</p></article>' for t, d in steps)
    main = f'''
  <section class="page-head">
    <div class="wrap reveal">
      <div class="label">{L('Services', 'خدمات')}</div>
      <h1>{L('Six ways I can help — each backed by work I have already done.', 'شش راه برای کمک — هرکدام با پشتوانهٔ کاری که پیش‌تر انجام داده‌ام.')}</h1>
      <p class="lede">{L('Scoped to fit anything from a single fix to an ongoing engagement. Every project starts with a conversation about what you actually need.',
                         'قابل تنظیم برای هرچیز از یک اصلاح ساده تا یک همکاری مداوم. هر پروژه با یک گفتگو دربارهٔ آنچه واقعاً نیاز دارید شروع می‌شود.')}</p>
    </div>
  </section>
  <section class="section section--tight">
    <div class="wrap"><h2 class="visually-hidden">{L('Services', 'خدمات')}</h2><div class="svc-grid reveal-group">{cards}</div></div>
  </section>
  <section class="section section--raised">
    <div class="wrap">
      <div class="section-head section-head--wide reveal">
        <h2>{L('How an engagement works', 'یک همکاری چگونه پیش می‌رود')}</h2>
        <p>{L('The same four steps whether the job takes two days or two months.', 'همان چهار مرحله، چه کار دو روز طول بکشد چه دو ماه.')}</p>
      </div>
      <div class="steps reveal-group">{st}</div>
    </div>
  </section>
  <section class="section section--tight">
    <div class="wrap notes">
      <div class="note reveal"><h3>{L('On cost', 'دربارهٔ هزینه')}</h3><p>{L('Pricing depends on scope, timeline, and whether the work is a one-off build or ongoing support, so it is not listed here. Every quote is given in writing, after the discovery call and before work starts.',
                                                                              'قیمت به محدودهٔ کار، زمان‌بندی و یک‌باره‌بودن یا مداوم‌بودن کار بستگی دارد، پس اینجا فهرست نشده است. هر پیشنهاد قیمت به‌صورت مکتوب، پس از گفتگوی آشنایی و پیش از شروع کار ارائه می‌شود.')}</p></div>
      <div class="note reveal"><h3>{L('On availability', 'دربارهٔ دسترسی')}</h3><p>{L('Working remotely in English and Dari, on Kabul time (UTC+4:30). New inquiries are usually answered within 1–2 business days.',
                                                                                    'کار از راه دور، به دو زبان دری و انگلیسی، با وقت کابل (UTC+4:30). به درخواست‌های جدید معمولاً ظرف ۱ تا ۲ روز کاری پاسخ داده می‌شود.')}</p></div>
    </div>
  </section>
'''
    cta = cta_band(L('Not sure which service fits?', 'مطمئن نیستید کدام خدمت مناسب است؟'),
                   primary=('contact', L('Describe what you need', 'نیازتان را شرح دهید')),
                   secondary=('projects', L('See past work first', 'ابتدا کارهای قبلی را ببینید')))
    return h + main + cta + footer()

# ---------------------------------------------------------------- PROJECTS
def projects():
    C.key = 'projects'
    title = L('Projects — Ahmad Zaheer Academy, Examina & PULSAR', 'پروژه‌ها — آکادمی احمد ظهیر، Examina و پالسار')
    desc = L('Three live websites by Ahmad Zaheer: a free programming academy with 450+ lessons, an online and offline exam platform, and PULSAR, a Persian online store for gaming hardware.',
             'سه وب‌سایت فعال از احمد ظهیر: یک اکادمی رایگان برنامه‌نویسی با بیش از ۴۵۰ درس، یک پلتفورم امتحان آنلاین و آفلاین، و پالسار، یک فروشگاه آنلاین فارسی برای تجهیزات گیمینگ.')
    h = head(title, desc, jsonld=[person_jsonld()]) + header()
    cards = ''.join(pf_card(p) for p in PROJECTS)
    main = f'''
  <section class="page-head">
    <div class="wrap reveal">
      <div class="label">{L('Projects', 'پروژه‌ها')}</div>
      <h1>{L('Three sites, all live — open them and judge for yourself.', 'سه وب‌سایت، همه فعال — باز کنید و خودتان قضاوت کنید.')}</h1>
      <p class="lede">{L('Built from scratch with plain HTML, CSS, and JavaScript and published on Netlify. Descriptions below match what is on the live sites.',
                         'از پایه با HTML، CSS و جاوااسکریپت خالص ساخته و روی Netlify منتشر شده‌اند. توضیحات زیر با آنچه در وب‌سایت‌های فعال است مطابقت دارد.')}</p>
    </div>
  </section>
  <section class="section section--tight">
    <div class="wrap"><h2 class="visually-hidden">{L('Projects', 'پروژه‌ها')}</h2><div class="pf-list">{cards}</div></div>
  </section>
'''
    cta = cta_band(L('Want something like this built for you?', 'می‌خواهید چیزی مشابه برای شما ساخته شود؟'))
    return h + main + cta + footer()

def project_detail(p):
    C.key = 'projects/' + p['key']
    name = L(*p['name'])
    title = f'{name} — ' + L('Project details | Ahmad Zaheer', 'جزئیات پروژه | احمد ظهیر')
    desc = L(*p['tagline'])
    h = head(title, desc, jsonld=[person_jsonld()]) + header()
    pts = ''.join(f'<li>{esc(L(*x))}</li>' for x in p['points'])
    visit = f'<a class="btn btn--primary" href="{p["url"]}" target="_blank" rel="noopener noreferrer">{L("Visit live site", "دیدن وب‌سایت")}{EXT()}</a>'
    back = f'<a class="btn btn--ghost" href="{href("projects")}">{L("All projects", "همهٔ پروژه‌ها")}</a>'
    top = f'''
  <section class="page-head">
    <div class="wrap reveal">
      <a class="crumb" href="{href('projects')}">{L('← All projects', '→ همهٔ پروژه‌ها')}</a>
      <div class="pf__meta">{status('live')}<span class="pf__domain">{p['domain']}</span></div>
      <h1 class="mt-09">{esc(name)}</h1>
      <p class="lede">{esc(L(*p['tagline']))}</p>
      <div class="flex-actions flex-actions--mt">{visit}{back}</div>
    </div>
  </section>
'''
    if p['key'] == 'zaheer-academy':
        glance = [(n(11), L('courses', 'دوره')), (n('450+'), L('lessons', 'درس')), (n(3), L('languages: Dari, Pashto, English', 'زبان: دری، پشتو، انگلیسی')), (L('Free', 'رایگان'), L('no cost, ever to start', 'شروع بدون هزینه'))]
        glance = [glance[0], glance[1], glance[2], (L('Free', 'رایگان'), L('all courses and quizzes', 'همهٔ دوره‌ها و کوییزها'))]
        gl = ''.join(f'<div class="detail-card"><h3>{a}</h3><p>{b}</p></div>' for a, b in glance)
        courses = ['basics', 'windows11', 'html5', 'css3', 'javascript', 'php', 'cpp', 'mysql', 'ai-tools', 'english']
        lesson = [
            (L('Read the explanation', 'خواندن توضیح درس'), L('Each lesson starts from the basics and builds toward more advanced examples.', 'هر درس از مفاهیم پایه شروع می‌شود و به مثال‌های پیشرفته‌تر می‌رسد.')),
            (L('Run the code example', 'اجرای مثال کد'), L('Examples are written to current standards: HTML5, CSS3, ES6+, and PHP 8.', 'مثال‌ها مطابق استانداردهای فعلی نوشته شده‌اند: HTML5، CSS3، ES6+ و PHP 8.')),
            (L('Practice in the playground', 'تمرین در پلی‌گراند'), L('For HTML, CSS, and JavaScript, write code right in the lesson and see the result.', 'برای HTML، CSS و جاوااسکریپت، کد را مستقیم در همان درس بنویسید و نتیجه را ببینید.')),
            (L('Answer the quiz', 'پاسخ به کوییز'), L('A short quiz shows straight away how much you have learned.', 'یک کوییز کوتاه بلافاصله نشان می‌دهد چقدر یاد گرفته‌اید.')),
        ]
        ls = ''.join(f'<article class="step reveal"><h3>{a}</h3><p>{b}</p></article>' for a, b in lesson)
        also = [L('Learning paths', 'مسیرهای یادگیری'), L('Practice exercises', 'تمرین‌های عملی'), L('Articles', 'مقالات'), L('Glossary', 'واژه‌نامه'),
                L('Image gallery', 'گالری تصاویر'), L('AI models overview', 'معرفی مدل‌های هوش مصنوعی'), L('Personal dashboard', 'داشبورد شخصی'), L('Site-wide search (Ctrl + K)', 'جست‌وجو در کل سایت (Ctrl + K)')]
        body = f'''
  <section class="section section--tight">
    <div class="wrap">
      <h2 class="visually-hidden">{L('At a glance', 'در یک نگاه')}</h2><div class="detail-cols glance reveal-group">{gl}</div>
    </div>
  </section>
  <section class="section section--raised">
    <div class="wrap">
      <div class="section-head section-head--wide reveal"><h2>{L('Courses', 'دوره‌ها')}</h2>
        <p>{L('From a first computer to web development and databases — plus a language course built on the IPA and CEFR frameworks.', 'از اولین کمپیوتر تا توسعهٔ وب و پایگاه‌داده — به‌علاوهٔ یک دورهٔ زبان مبتنی بر چارچوب‌های IPA و CEFR.')}</p></div>
      <div class="tile-grid tile-grid--compact reveal">{''.join(tile(t) for t in courses)}</div>
    </div>
  </section>
  <section class="section">
    <div class="wrap">
      <div class="section-head section-head--wide reveal"><h2>{L('How a lesson works', 'یک درس چگونه پیش می‌رود')}</h2></div>
      <div class="steps reveal-group">{ls}</div>
    </div>
  </section>
  <section class="section section--raised">
    <div class="wrap detail-cols">
      <div class="detail-card reveal"><h3>{L('Also on the site', 'بخش‌های دیگر سایت')}</h3>
        <div class="pf__tech">{''.join(f'<span class="chip">{esc(x)}</span>' for x in also)}</div></div>
      <div class="detail-card reveal"><h3>{L('Progress & certificates', 'پیشرفت و گواهینامه')}</h3>
        <ul class="pf__points"><li>{L('Progress is saved in your browser; a free account lets you continue on other devices.', 'پیشرفت در مرورگر شما ذخیره می‌شود؛ با یک حساب رایگان می‌توانید از دستگاه‌های دیگر ادامه دهید.')}</li>
        <li>{L('Finish 100% of a course to unlock its certificate.', 'با تکمیل ۱۰۰٪ یک دوره، گواهینامهٔ همان دوره در دسترس شما قرار می‌گیرد.')}</li></ul></div>
      <div class="detail-card reveal"><h3>{L('Built with', 'ساخته‌شده با')}</h3>
        <p>{L('Plain HTML, CSS, and JavaScript — no frameworks.', 'HTML، CSS و جاوااسکریپت خالص — بدون فریم‌ورک.')}</p>{pf_tech(p['tech'])}</div>
    </div>
  </section>
'''
    elif p['key'] == 'pulsar':
        cats = [L('Gaming PCs', 'کامپیوتر گیمینگ'), L('Gaming laptops', 'لپ‌تاپ گیمینگ'), L('Monitors', 'مانیتور'), L('Keyboards', 'کیبورد'),
                L('Mice', 'ماوس'), L('Headsets', 'هدست'), L('Gaming chairs', 'صندلی گیمینگ'), L('RGB accessories', 'لوازم جانبی RGB')]
        tools = [L('Shop & search', 'فروشگاه و جست‌وجو'), L('Deals & flash sale', 'تخفیف‌ها و فلش‌سیل'), L('Ready-made PC builds', 'بیلدهای آمادهٔ کامپیوتر'),
                 L('Wishlist', 'علاقه‌مندی‌ها'), L('Cart', 'سبد خرید'), L('Sign in & register', 'ورود و ثبت‌نام'), L('Profile & orders', 'پروفایل و سفارش‌ها'),
                 L('Product comparison', 'مقایسهٔ محصولات'), L('FAQ', 'سوالات متداول'), L('About & contact', 'درباره و تماس')]
        body = f'''
  <section class="section section--tight">
    <div class="wrap">
      <h2 class="visually-hidden">{L('What the store includes', 'فروشگاه شامل چه چیزهایی است')}</h2>
      <div class="detail-cols reveal-group">
        <div class="detail-card reveal"><h3>{L('What it includes', 'شامل چه چیزهایی است')}</h3><ul class="pf__points">{pts}</ul></div>
        <div class="detail-card reveal"><h3>{L('Product categories', 'دسته‌بندی محصولات')}</h3>
          <div class="pf__tech">{''.join(f'<span class="chip">{esc(x)}</span>' for x in cats)}</div>
          <h3 class="block-title">{L('Store features', 'امکانات فروشگاه')}</h3>
          <div class="pf__tech">{''.join(f'<span class="chip">{esc(x)}</span>' for x in tools)}</div></div>
        <div class="detail-card reveal"><h3>{L('Language & hosting', 'زبان و میزبانی')}</h3>
          <p>{L('The whole store is written in Persian with a native right-to-left layout, and it is published on Netlify.', 'کل فروشگاه به فارسی و با چیدمان اصیل راست‌به‌چپ نوشته شده و روی Netlify منتشر شده است.')}</p>{pf_tech(p['tech'])}</div>
      </div>
    </div>
  </section>
'''
    else:  # examina
        modes = [
            (L('Online exams', 'امتحان آنلاین'), L('Interactive, timed assessments with a live countdown, a question navigator, and instant auto-graded results — the full exam experience in the browser.',
                                                    'ارزیابی‌های تعاملی و زمان‌دار با شمارندهٔ زنده، ناوبر سوالات و نتیجهٔ خودکار و فوری — تجربهٔ کامل امتحان در مرورگر.'), 'monitor'),
            (L('Offline exams', 'امتحان آفلاین'), L('The same exam banks as print-ready paper tests, each with a separate answer key — for classrooms without devices or take-home practice.',
                                                    'همان بانک‌های سوال به شکل امتحان کاغذی آمادهٔ چاپ، هرکدام با کلید پاسخ جداگانه — برای صنف‌های بدون دستگاه یا تمرین در خانه.'), 'printer'),
        ]
        md = ''.join(f'<article class="detail-card reveal"><span class="pillar__icon ac-web">{ic(g)}</span><h3>{a}</h3><p>{b}</p></article>' for a, b, g in modes)
        pages = [L('Home & exam list', 'خانه و فهرست امتحان‌ها'), L('About', 'درباره'), L('FAQ', 'پرسش‌های متداول'), L('Contact', 'تماس'), L('Privacy policy', 'سیاست حریم خصوصی'), L('Terms of use', 'شرایط استفاده')]
        body = f'''
  <section class="section section--tight">
    <div class="wrap"><h2 class="visually-hidden">{L('Two modes', 'دو حالت')}</h2><div class="detail-cols reveal-group">{md}</div></div>
  </section>
  <section class="section section--raised">
    <div class="wrap detail-cols">
      <div class="detail-card reveal"><h3>{L('What it includes', 'شامل چه چیزهایی است')}</h3><ul class="pf__points">{pts}</ul></div>
      <div class="detail-card reveal"><h3>{L('Pages', 'صفحات')}</h3><div class="pf__tech">{''.join(f'<span class="chip">{esc(x)}</span>' for x in pages)}</div>
        <h3 class="block-title">{L('Built with', 'ساخته‌شده با')}</h3>
        <p>{L('Plain HTML, CSS, and JavaScript — no frameworks, no tracking.', 'HTML، CSS و جاوااسکریپت خالص — بدون فریم‌ورک، بدون ردیابی.')}</p>{pf_tech(p['tech'])}</div>
    </div>
  </section>
'''
    cta = cta_band(L('Want a platform like this?', 'پلتفورمی مشابه می‌خواهید؟'), primary=('contact', None), secondary=('projects', L('All projects', 'همهٔ پروژه‌ها')))
    return h + top + body + cta + footer()

# ---------------------------------------------------------------- CERTIFICATES
def certifications():
    C.key = 'certifications'
    title = L('Certificates & Education — Ahmad Zaheer', 'گواهینامه‌ها و تحصیلات — احمد ظهیر')
    desc = L('A computer science diploma and transcript from AIT, computer certificates, English diploma and certificates, and school graduation.',
             'دیپلوم و ترانسکریپت کمپیوتر ساینس از AIT، گواهینامه‌های کمپیوتر، دیپلوم و گواهینامه‌های انگلیسی، و فراغت از لیسه.')
    h = head(title, desc, jsonld=[person_jsonld()]) + header()
    secs = ''
    for s in CRED_SECTIONS:
        secs += f'''
      <section class="cred-section" aria-labelledby="cs-{s['id']}">
        <div class="cred-section__head reveal"><h2 id="cs-{s['id']}">{L(*s['title'])}</h2><p>{L(*s['desc'])}</p></div>
        <div class="cred-grid reveal-group">{''.join(cred_card(s['cls'], s['glyph'], it) for it in s['items'])}</div>
      </section>'''
    main = f'''
  <section class="page-head">
    <div class="wrap reveal">
      <div class="label">{L('Certificates & education', 'گواهینامه‌ها و تحصیلات')}</div>
      <h1>{L('A computer science diploma, backed by certificates in computing and English.', 'یک دیپلوم کمپیوتر ساینس، با پشتوانهٔ گواهینامه‌های کمپیوتر و انگلیسی.')}</h1>
      <p class="lede">{L('Grouped by subject. The diploma and transcript come from AIT; the certificates come from academies and educational centers.',
                         'دسته‌بندی‌شده بر اساس موضوع. دیپلوم و ترانسکریپت از AIT است؛ گواهینامه‌ها از اکادمی‌ها و مراکز آموزشی.')}</p>
    </div>
  </section>
  <section class="section section--tight"><div class="wrap">{secs}</div></section>
'''
    cta = cta_band(L('Want the full picture, skills and experience together?', 'تصویر کامل، مهارت‌ها و تجربه را با هم می‌خواهید؟'),
                   primary=('resume', L('Open the CV', 'باز کردن رزومه')), secondary=('about', L('Read the profile', 'خواندن پروفایل')))
    return h + main + cta + footer()

# ---------------------------------------------------------------- CONTACT
def contact():
    C.key = 'contact'
    title = L('Contact — Ahmad Zaheer | Kabul, Afghanistan', 'تماس — احمد ظهیر | کابل، افغانستان')
    desc = L('Contact Ahmad Zaheer by phone, WhatsApp, email, or the contact form. Based in Khairkhana, Kabul — see the map.',
             'با احمد ظهیر از طریق تلیفون، واتساپ، ایمیل یا فورم تماس در ارتباط شوید. خیرخانه، کابل — نقشه را ببینید.')
    h = head(title, desc, jsonld=[person_jsonld()]) + header()
    q = MAP_QUERY.replace(' ', '+')
    embed = f'https://www.google.com/maps?q={q}&output=embed'
    open_url = f'https://www.google.com/maps/search/?api=1&query={q}'
    dir_url = f'https://www.google.com/maps/dir/?api=1&destination={q}'
    addr = L('Khairkhana, <bdi>Golayee Khoja Bushma</bdi>, near Argentina Hotel, Kabul, Afghanistan',
             'خیرخانه، <bdi>Golayee Khoja Bushma</bdi>، نزدیک هوتل ارجنتاین، کابل، افغانستان')
    ct = f'''
        <div class="ct-list">
          <a class="ct ct--phone" href="{PHONE_HREF}"><span class="ct__icon">{ic('phone')}</span><span><span class="ct__label">{L('Phone', 'تلیفون')}</span><span class="ct__value ltr">{PHONE_DISPLAY}</span></span></a>
          <a class="ct ct--wa" id="contact-whatsapp-link" href="https://wa.me/{WA_NUMBER}" target="_blank" rel="noopener noreferrer"><span class="ct__icon">{ic('message-circle')}</span><span><span class="ct__label">WhatsApp</span><span class="ct__value">{L('Message me directly', 'مستقیم پیام بدهید')}</span></span></a>
          <a class="ct ct--mail" href="mailto:{EMAIL}"><span class="ct__icon">{ic('mail')}</span><span><span class="ct__label">{L('Email', 'ایمیل')}</span><span class="ct__value ltr">{EMAIL}</span></span></a>
          <div class="ct ct--pin"><span class="ct__icon">{ic('map-pin')}</span><span><span class="ct__label">{L('Address', 'آدرس')}</span><span class="ct__value">{addr}</span></span></div>
        </div>
        <div class="map-card reveal">
          <div class="map-card__frame">
            <iframe id="map-frame" title="{L('Map of Khairkhana, Kabul', 'نقشهٔ خیرخانه، کابل')}" src="{embed}" loading="lazy" referrerpolicy="no-referrer-when-downgrade" allowfullscreen></iframe>
          </div>
          <div class="map-card__body">
            <h3>{L('Find me on the map', 'مرا روی نقشه پیدا کنید')}</h3>
            <p>{addr}</p>
            <p class="text-sm">{L('The map is centred on the Khairkhana area; the landmark above is the closest reference.', 'نقشه روی منطقهٔ خیرخانه متمرکز است؛ نشانی بالا نزدیک‌ترین مرجع است.')}</p>
            <div class="map-card__actions">
              <a class="btn btn--primary btn--small" id="map-open" href="{open_url}" target="_blank" rel="noopener noreferrer">{ic('map-pin')}{L('Open in Google Maps', 'باز کردن در Google Maps')}</a>
              <a class="btn btn--ghost btn--small" id="map-directions" href="{dir_url}" target="_blank" rel="noopener noreferrer">{ic('route')}{L('Get directions', 'مسیریابی')}</a>
            </div>
          </div>
        </div>
        <h3 class="block-title">{L('My live websites', 'وب‌سایت‌های فعال من')}</h3>
        <div class="sites-list">{''.join(f'<a href="{u}" target="_blank" rel="noopener noreferrer"><span>{d}</span>{EXT()}</a>' for d, u in SITES)}</div>
'''
    form = f'''
        <div class="form-panel reveal">
          <h2>{L('Send a message', 'ارسال پیام')}</h2>
          <div class="form-status" id="form-status" role="status"></div>
          <form id="contact-form" name="contact" method="POST" data-netlify="true" data-netlify-honeypot="company" novalidate>
            <input type="hidden" name="form-name" value="contact">
            <div class="field-honeypot" aria-hidden="true">
              <label for="company">Company</label>
              <input type="text" id="company" name="company" tabindex="-1" autocomplete="off">
            </div>
            <div class="field-row">
              <div class="field">
                <label for="name">{L('Full name', 'نام کامل')} <span class="req">*</span></label>
                <input type="text" id="name" name="name" required aria-required="true" aria-describedby="name-error" autocomplete="name">
                <p class="field-error" id="name-error"></p>
              </div>
              <div class="field">
                <label for="email">{L('Email', 'ایمیل')} <span class="req">*</span></label>
                <input type="email" id="email" name="email" required aria-required="true" aria-describedby="email-error" autocomplete="email" dir="ltr">
                <p class="field-error" id="email-error"></p>
              </div>
            </div>
            <div class="field">
              <label for="subject">{L('Subject', 'موضوع')} <span class="req">*</span></label>
              <input type="text" id="subject" name="subject" required aria-required="true" aria-describedby="subject-error">
              <p class="field-error" id="subject-error"></p>
            </div>
            <div class="field">
              <label for="message">{L('Message', 'پیام')} <span class="req">*</span></label>
              <textarea id="message" name="message" required aria-required="true" aria-describedby="message-error"></textarea>
              <p class="field-error" id="message-error"></p>
            </div>
            <button type="submit" class="btn btn--primary btn--block">{L('Send message', 'ارسال پیام')}</button>
          </form>
          <p class="text-sm mt-1">{L('Prefer a direct reply? Use WhatsApp or the phone number — I usually respond within 1–2 business days.', 'پاسخ مستقیم می‌خواهید؟ از واتساپ یا شمارهٔ تلیفون استفاده کنید — معمولاً ظرف ۱ تا ۲ روز کاری پاسخ می‌دهم.')}</p>
        </div>
'''
    main = f'''
  <section class="page-head">
    <div class="wrap reveal">
      <div class="label">{L('Contact', 'تماس')}</div>
      <h1>{L("Tell me what you're building — or teaching.", 'بگویید چه چیزی می‌سازید — یا آموزش می‌دهید.')}</h1>
      <p class="lede">{L('A website, a database, a course, or something in between: call, message on WhatsApp, email, or use the form.',
                         'وب‌سایت، پایگاه‌داده، دوره یا چیزی بین این‌ها: تلیفون بزنید، در واتساپ پیام بدهید، ایمیل بفرستید یا از فورم استفاده کنید.')}</p>
    </div>
  </section>
  <section class="section section--tight">
    <div class="wrap contact-layout">
      <div class="reveal"><h2 class="visually-hidden">{L('Contact details', 'اطلاعات تماس')}</h2>{ct}</div>
      {form}
    </div>
  </section>
'''
    return h + main + footer(['map', 'contact-fa' if C.lang == 'fa' else 'contact'])

# ---------------------------------------------------------------- CV
def cv_skill_rows():
    rows = []
    sep = '، ' if C.lang == 'fa' else ', '
    for c in CATS:
        parts = []
        for t in c['items']:
            label = esc(tname(t)) + (f' ({esc(tnote(t))})' if t in ('java', 'cpp') else '')
            parts.append(f'<bdi>{label}</bdi>')
        rows.append((esc(L(c['en'], c['fa'])), sep.join(parts)))
    return rows

def resume():
    C.key = 'resume'
    title = L('CV — Ahmad Zaheer, Computer & Technology Specialist', 'رزومه — احمد ظهیر، متخصص کمپیوتر و تکنالوژی')
    desc = L('Curriculum vitae of Ahmad Zaheer: professional profile, experience, education, technical skills, projects, and languages. Downloadable PDF.',
             'رزومهٔ احمد ظهیر: پروفایل حرفه‌ای، تجربهٔ کاری، تحصیلات، مهارت‌های فنی، پروژه‌ها و زبان‌ها. فایل PDF قابل دانلود.')
    h = head(title, desc, extra_css=['cv'], jsonld=[person_jsonld()]) + header()
    pdf = asset('ahmad-zaheer-resume-fa.pdf' if C.lang == 'fa' else 'ahmad-zaheer-resume.pdf')
    comp = [
        L('Web development: static & dynamic sites, web apps', 'توسعهٔ وب: سایت ایستا و پویا، اپلیکیشن وب'),
        L('Database administration and SQL', 'مدیریت پایگاه‌داده و SQL'),
        L('Course design for IT and English', 'طراحی دوره برای آی‌تی و انگلیسی'),
        L('Classroom and online instruction', 'تدریس حضوری و آنلاین'),
        L('AI-assisted development and automation', 'توسعه با کمک هوش مصنوعی و اتوماسیون'),
        L('Generative AI for image and video', 'هوش مصنوعی مولد برای تصویر و ویدیو'),
        L('Image editing and graphic design', 'ویرایش تصویر و طراحی گرافیک'),
        L('Right-to-left, bilingual (Dari/English) interfaces', 'رابط‌های راست‌به‌چپ و دوزبانه (دری/انگلیسی)'),
        L('Office package and typography (ICDL CIT/DIT)', 'بستهٔ آفیس و تایپوگرافی (ICDL — CIT/DIT)'),
        L('Network basics and internet use (ICDL)', 'مبانی شبکه و استفاده از انترنت (ICDL)'),
    ]
    def cv_entry(e):
        chip = f'<span class="cv-entry__when">{esc(L(*e["dur"]))}</span>' if e['dur'] else ''
        extra = ''
        if e.get('tags'):
            extra = f'<div class="cv-entry__tags">{esc(" · ".join(L(*t) for t in e["tags"]))}</div>'
        if e.get('projects'):
            names = ('، ' if C.lang == 'fa' else ', ').join(esc(L(*x['name'])) for x in PROJECTS)
            extra = f'<div class="cv-entry__tags">{L("Selected work", "کارهای منتخب")}: {names}</div>'
        return f'''
      <div class="cv-entry"><div class="cv-entry__head"><h4>{esc(L(*e['role']))} — <span class="cv-entry__org"><bdi>{esc(L(*e['org']))}</bdi></span></h4>{chip}</div>
        <p>{esc(L(*e['desc']))}</p>{extra}</div>'''
    exp = ''
    for gid in ('tech', 'teach'):
        exp += f'<div class="cv-group"><h3>{L(*GROUPS[gid]["title"])}</h3>' + ''.join(cv_entry(e) for e in EXPERIENCE if e['group'] == gid) + '</div>'
    edu = ''
    for s in CRED_SECTIONS:
        for it in s['items']:
            edu += f'<li><strong>{esc(L(*it["t"]))}</strong><span><bdi>{esc(L(*it["org"]))}</bdi></span></li>'
    skills = ''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a, b in cv_skill_rows())
    projs = ''.join(
        f'<li><b>{esc(L(*p["name"]))}</b> — <a class="ltr" href="{p["url"]}">{p["domain"]}</a><p>{esc(L(*p["tagline"]))}</p></li>' for p in PROJECTS)
    contact_rows = f'''
          <li><b>{L('Phone', 'تلیفون')}</b><span class="ltr">{PHONE_DISPLAY}</span></li>
          <li><b>{L('Email', 'ایمیل')}</b><span class="ltr">{EMAIL}</span></li>
          <li><b>{L('Address', 'آدرس')}</b><span>{L('Khairkhana, Kabul, Afghanistan', 'خیرخانه، کابل، افغانستان')}</span></li>
          <li><b>{L('Web', 'وب')}</b><span class="ltr">zaheer-tech.netlify.app</span></li>'''
    summary = L('Computer science graduate (AIT) and technology specialist based in Kabul, Afghanistan. Experienced in database administration (PHEMIS system, Payam University), web development with HTML, CSS, JavaScript, Tailwind CSS, and PHP, and teaching English and computer skills across five institutions. Creator of two live platforms: a free online programming academy (11 courses, 450+ lessons) and an online and offline exam platform. Applies AI tools, generative AI, and AI agents to speed up software development, media production, and office work. Works in Dari and English.',
                'فارغ‌التحصیل کمپیوتر ساینس (AIT) و متخصص تکنالوژی مقیم کابل، افغانستان. دارای تجربه در مدیریت پایگاه‌داده (سیستم PHEMIS، پوهنتون پیام)، توسعهٔ وب با HTML، CSS، جاوااسکریپت، Tailwind CSS و PHP، و تدریس انگلیسی و مهارت‌های کمپیوتری در پنج نهاد آموزشی. سازندهٔ دو پلتفورم فعال: یک اکادمی آنلاین رایگان برنامه‌نویسی (۱۱ دوره، بیش از ۴۵۰ درس) و یک پلتفورم امتحان آنلاین و آفلاین. از ابزارهای هوش مصنوعی، هوش مصنوعی مولد و ایجنت‌ها برای سرعت‌بخشیدن به توسعهٔ نرم‌افزار، تولید رسانه و کارهای اداری استفاده می‌کند. به دو زبان دری و انگلیسی کار می‌کند.')
    doc = f'''
  <section class="section hero-offset cv-page">
    <div class="wrap">
      <div class="cv-toolbar">
        <p>{L('Curriculum vitae — also available as a PDF.', 'رزومه — به‌صورت PDF هم موجود است.')}</p>
        <div class="cv-toolbar__actions">
          <a class="btn btn--primary btn--small" href="{pdf}" download>{ic('download')}{L('Download PDF', 'دانلود PDF')}</a>
          <button class="btn btn--ghost btn--small" id="print-btn" type="button">{ic('printer')}{L('Print', 'چاپ')}</button>
        </div>
      </div>
      <article class="cv-sheet" aria-label="{L('Curriculum vitae of Ahmad Zaheer', 'رزومهٔ احمد ظهیر')}">
        <header class="cv-head">
          <div><h1>{NAME()}</h1><p class="cv-head__title">{L('Computer & Technology Specialist — Web Development, Database Administration & IT Education', 'متخصص کمپیوتر و تکنالوژی — توسعهٔ وب، مدیریت پایگاه‌داده و آموزش آی‌تی')}</p></div>
          <ul class="cv-contact">{contact_rows}</ul>
        </header>
        <section class="cv-sec"><h2>{L('Professional profile', 'پروفایل حرفه‌ای')}</h2><p class="cv-summary">{summary}</p></section>
        <section class="cv-sec"><h2>{L('Core competencies', 'شایستگی‌های اصلی')}</h2><ul class="cv-comp">{''.join(f'<li>{c}</li>' for c in comp)}</ul></section>
        <section class="cv-sec"><h2>{L('Professional experience', 'تجربهٔ کاری')}</h2>{exp}</section>
        <section class="cv-sec"><h2>{L('Education & certificates', 'تحصیلات و گواهینامه‌ها')}</h2><ul class="cv-edu cv-two">{edu}</ul></section>
        <section class="cv-sec"><h2>{L('Technical skills', 'مهارت‌های فنی')}</h2><dl class="cv-skills">{skills}</dl></section>
        <section class="cv-sec"><h2>{L('Selected projects', 'پروژه‌های منتخب')}</h2><ul class="cv-projects">{projs}</ul></section>
        <section class="cv-sec"><h2>{L('Languages', 'زبان‌ها')}</h2>
          <ul class="cv-langs"><li><span>{L('Dari / Persian', 'دری / فارسی')}</span><span>{L('Native', 'مادری')}</span></li>
          <li><span>{L('English', 'انگلیسی')}</span><span>{L('Professional', 'حرفه‌ای')}</span></li></ul></section>
      </article>
    </div>
  </section>
'''
    return h + doc + footer(['resume'])

# ---------------------------------------------------------------- 404
def not_found():
    C.key = '404'
    C.abs_root = True
    try:
        title = L('Page not found — Ahmad Zaheer', 'صفحه پیدا نشد — احمد ظهیر')
        h = head(title, L('The page you asked for does not exist.', 'صفحهٔ درخواستی وجود ندارد.'), noindex=True) + header()
        body = f'''
  <section class="section error-page hero-offset">
    <div class="wrap">
      <div class="error-code mono" aria-hidden="true">404</div>
      <h1>{L('That page does not exist.', 'این صفحه وجود ندارد.')}</h1>
      <p class="lede mt-2">{L('The link may be old or mistyped. These pages do exist:', 'ممکن است لینک قدیمی یا اشتباه تایپ شده باشد. این صفحات وجود دارند:')}</p>
      <div class="flex-actions flex-actions--mt">
        <a class="btn btn--primary" href="{href('index')}">{L('Home', 'خانه')}</a>
        <a class="btn btn--ghost" href="{href('projects')}">{L('Projects', 'پروژه‌ها')}</a>
        <a class="btn btn--ghost" href="{href('contact')}">{L('Contact', 'تماس')}</a>
      </div>
    </div>
  </section>
'''
        return h + body + footer()
    finally:
        C.abs_root = False
