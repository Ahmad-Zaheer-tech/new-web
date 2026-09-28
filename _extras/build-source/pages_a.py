# -*- coding: utf-8 -*-
from common import *
from data import *
from registry import TECH, CATS
from common import _icon_html

# ---------------------------------------------------------------- shared blocks
def pf_card(p, compact=False):
    name = L(*p['name'])
    pts = ''.join(f'<li>{esc(L(*x))}</li>' for x in p['points'])
    pts_html = f'<ul class="pf__points">{pts}</ul>' if (pts and not compact) else ''
    tech_html = pf_tech(p['tech']) if p['tech'] and not compact else ''
    detail_btn = (f'<a class="btn btn--ghost" href="{href("projects/" + p["key"])}">{L("Project details", "جزئیات پروژه")}</a>'
                  if p['detail'] else '')
    visit = (f'<a class="btn btn--primary" href="{p["url"]}" target="_blank" rel="noopener noreferrer">'
             f'{L("Visit live site", "دیدن وب‌سایت")}{EXT()}</a>')
    return f'''
    <article class="pf pf--{p['cls']}{' pf--compact' if compact else ''} reveal">
      <div class="pf__preview" aria-hidden="true">
        <div class="browser">
          <div class="browser__bar"><i></i><i></i><i></i><span class="browser__url">{p['domain']}</span></div>
          <div class="browser__body"><b></b><span></span><span></span><span></span>
            <div class="browser__grid"><i></i><i></i><i></i></div></div>
        </div>
      </div>
      <div class="pf__body">
        <div class="pf__meta">{status('live')}<span class="pf__domain">{p['domain']}</span></div>
        <h3>{esc(name)}</h3>
        <p>{esc(L(*p['tagline']))}</p>
        {pts_html}
        {tech_html}
        <div class="pf__actions">{visit}{detail_btn}</div>
      </div>
    </article>'''

def xp_item(e, with_projects=True):
    role, org = L(*e['role']), L(*e['org'])
    chip = f'<span class="chip">{esc(L(*e["dur"]))}</span>' if e['dur'] else ''
    tags_html = ''
    if e.get('tags'):
        tags_html = tags([L(*t) for t in e['tags']])
    proj_html = ''
    if e.get('projects') and with_projects:
        links = ' · '.join(f'<a href="{p["url"]}" target="_blank" rel="noopener noreferrer">{esc(L(*p["name"]))}</a>' for p in PROJECTS)
        proj_html = f'<p>{L("Selected work", "کارهای منتخب")}: {links}</p>'
    return f'''
        <li class="xp-item reveal">
          <div class="xp-item__head"><h4>{esc(role)}</h4><span class="xp-item__org">{esc(org)}</span>{chip}</div>
          <p>{esc(L(*e['desc']))}</p>
          {proj_html}{tags_html}
        </li>'''

def xp_groups():
    out = ''
    for gid in ('tech', 'teach'):
        g = GROUPS[gid]
        items = ''.join(xp_item(e) for e in EXPERIENCE if e['group'] == gid)
        out += f'''
      <div class="xp-group">
        <h3 class="xp-group__title">{ic(g['glyph'])}{L(*g['title'])}</h3>
        <ol class="xp">{items}</ol>
      </div>'''
    return out

def cred_card(cls, glyph, it):
    return f'''
        <article class="cred {cls} reveal">
          <span class="cred__mark">{ic(glyph)}</span>
          <div><h3>{esc(L(*it['t']))}</h3><span class="cred__org"><bdi>{esc(L(*it['org']))}</bdi></span>
          <span class="chip">{esc(L(*it['kind']))}</span></div>
        </article>'''


# ---------------------------------------------------------------- typewriter (home hero)
TYPER_IDS = ['html5', 'css3', 'javascript', 'tailwind', 'php', 'sql', 'sqlserver', 'oracle', 'mysql',
             'java', 'cpp', 'ai-build', 'gen-ai', 'ai-agents', 'canva', 'affinity', 'cit', 'dit']
TYPER_LABEL = {'ai-build': ('AI-assisted development', 'توسعه با هوش مصنوعی'),
               'gen-ai': ('Generative AI', 'هوش مصنوعی مولد'),
               'ai-agents': ('AI agents & automation', 'ایجنت و اتوماسیون')}

def typer():
    def label(t):
        return L(*TYPER_LABEL[t]) if t in TYPER_LABEL else tname(t)
    lis = ''.join(
        f'<li class="tc-{t}"{" data-plate" if TECH[t].get("plate") else ""} data-tech="{t}">'
        f'<span class="typer__ico">{_icon_html(t, 22)}</span><span class="typer__name">{esc(label(t))}</span></li>'
        for t in TYPER_IDS)
    summary = L('I work with: ', 'با این‌ها کار می‌کنم: ') + ('، ' if C.lang == 'fa' else ', ').join(label(t) for t in TYPER_IDS)
    return f'''
        <div class="typer" id="typer" data-summary="{esc(summary)}" data-pause="{L('Pause animation', 'توقف انیمیشن')}" data-play="{L('Play animation', 'پخش انیمیشن')}">
          <div class="typer__head">
            <p class="typer__label">{L('I work with', 'با این‌ها کار می‌کنم')}</p>
            <button class="typer__pause" type="button" aria-pressed="false" aria-label="{L('Pause animation', 'توقف انیمیشن')}" hidden>{ic('pause')}{ic('play')}</button>
          </div>
          <div class="typer__row" aria-hidden="true">
            <div class="typer__stage">
              <span class="typer__slot"></span>
              <span class="typer__typed"><span class="typer__text"></span><span class="typer__caret"></span></span>
            </div>
          </div>
          <ul class="typer__list">{lis}</ul>
        </div>'''

# ---------------------------------------------------------------- HOME
def home():
    C.key = 'index'
    title = L('Ahmad Zaheer — Computer & Technology Specialist | Web, Databases, Training',
              'احمد ظهیر — متخصص کمپیوتر و تکنالوژی | وب، پایگاه‌داده، آموزش')
    desc = L('Ahmad Zaheer is a computer & technology specialist in Kabul: web developer, database manager, and IT & English instructor. Builder of a free programming academy and an online exam platform; works in English and Dari.',
             'احمد ظهیر، متخصص کمپیوتر و تکنالوژی در کابل: توسعه‌دهندهٔ وب، مدیر پایگاه‌داده و مدرس آی‌تی و انگلیسی. سازندهٔ یک اکادمی رایگان برنامه‌نویسی و یک پلتفورم امتحان آنلاین؛ فعال به دو زبان دری و انگلیسی.')
    h = head(title, desc, jsonld=[person_jsonld(), website_jsonld()]) + header()

    orbit_ids = ['html5', 'css3', 'javascript', 'php', 'sqlserver', 'tailwind']
    orbit = ''.join(
        f'<span class="tech-icon tech-icon--{i+1}{" tech-icon--plate" if TECH[t].get("plate") else ""}" title="{esc(tname(t))}"><img src="{asset("tech/" + TECH[t]["icon"])}" alt="" width="22" height="22"></span>'
        for i, t in enumerate(orbit_ids))

    hero = f'''
  <section class="hero">
    <div class="grid-texture" aria-hidden="true"></div>
    <div class="hero-inner">
      <div class="hero-copy">
        <p class="hero-kicker mono">{L('Kabul, Afghanistan · Open to remote work', 'کابل، افغانستان · آمادهٔ همکاری از راه دور')}</p>
        <h1>
          <span class="line"><span>{NAME()}</span></span>
          <span class="line"><span>{ROLE()}</span></span>
        </h1>
        <p class="hero-role">{L('Web developer, database manager, and IT & English instructor', 'توسعه‌دهندهٔ وب، مدیر پایگاه‌داده و مدرس آی‌تی و انگلیسی')}</p>
        {typer()}
        <p class="lede">{L('I build websites and learning platforms, manage databases, and teach computer science and English. Computer science graduate of AIT, with hands-on work at Payam University, several academies, and live projects of my own — in English and Dari.',
                          'وب‌سایت و پلتفورم‌های آموزشی می‌سازم، پایگاه‌داده مدیریت می‌کنم و کمپیوتر و انگلیسی تدریس می‌کنم. فارغ‌التحصیل کمپیوتر ساینس از انستیتوت تکنالوژی افغانستان (AIT)، با تجربهٔ عملی در پوهنتون پیام، چندین اکادمی و پروژه‌های فعال خودم — به دو زبان دری و انگلیسی.')}</p>
        <div class="hero-actions">
          <a class="btn btn--primary" href="{href('projects')}">{L('View projects', 'مشاهدهٔ پروژه‌ها')}</a>
          <a class="btn btn--ghost" href="{href('resume')}">{L('View CV', 'مشاهدهٔ رزومه')}</a>
        </div>
        <div class="hero-meta">
          <div><strong>{n(6)}</strong><span>{L('roles held', 'نقش کاری')}</span></div>
          <div><strong>{n(3)}</strong><span>{L('live websites', 'وب‌سایت فعال')}</span></div>
          <div><strong>{n('450+')}</strong><span>{L('free lessons published', 'درس رایگان منتشرشده')}</span></div>
        </div>
      </div>
      <div class="hero-visual">
        <div class="chip-frame">
          <img src="{asset('ahmad-zaheer-640.jpg')}" alt="{L('Portrait of Ahmad Zaheer', 'عکس احمد ظهیر')}" width="640" height="640">
        </div>
        <div class="chip-pins" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
        <div class="tech-orbit" aria-hidden="true">{orbit}</div>
        <div class="hero-badge"><span class="dot"></span> {L('Open to new work', 'آمادهٔ کار جدید')}</div>
      </div>
    </div>
    <div class="scroll-cue" aria-hidden="true"><span>{L('Scroll', 'پیمایش')}</span><span class="wire"></span></div>
  </section>
'''

    profile = f'''
  <section class="section" id="profile">
    <div class="wrap profile-grid">
      <div class="reveal">
        <h2>{L('Where the classroom, the database, and the codebase meet.', 'جایی که صنف درس، پایگاه‌داده و کد به هم می‌رسند.')}</h2>
        <div class="stack mt-2">
          <p>{L("I'm Ahmad Zaheer, a computer science graduate based in Khairkhana, Kabul. My work moves between three places: a university database, the classroom, and the code editor.",
                'من احمد ظهیر هستم، فارغ‌التحصیل کمپیوتر ساینس ساکن خیرخانهٔ کابل. کارم بین سه جا در رفت‌وآمد است: پایگاه‌دادهٔ یک پوهنتون، صنف درس، و ویرایشگر کد.')}</p>
          <p>{L("I've managed the PHEMIS database system at Payam University, taught English and computer courses at several academies and educational centers, and built and published platforms of my own: a free programming academy and an online exam system.",
                'سیستم پایگاه‌دادهٔ PHEMIS را در پوهنتون پیام مدیریت کرده‌ام، در چندین اکادمی و مرکز آموزشی انگلیسی و کمپیوتر تدریس کرده‌ام، و پلتفورم‌های خودم را ساخته و منتشر کرده‌ام: یک اکادمی رایگان برنامه‌نویسی و یک سیستم امتحان آنلاین.')}</p>
          <p>{L('AI is now part of how I work: I use AI tools to build apps and websites, produce images and video, handle office documents, and set up agents and automation.',
                'هوش مصنوعی اکنون بخشی از روش کار من است: از ابزارهای آن برای ساخت اپلیکیشن و وب‌سایت، تولید تصویر و ویدیو، کارهای اسنادی و راه‌اندازی ایجنت‌ها و اتوماسیون استفاده می‌کنم.')}</p>
        </div>
        <p class="mt-2"><a class="link-arrow" href="{href('about')}">{L('Read the full profile', 'خواندن پروفایل کامل')}{ic('arrow-right')}</a></p>
      </div>
      <aside class="facts reveal" aria-label="{L('Key facts', 'اطلاعات کلیدی')}">
        <dl>
          <div><dt>{L('Location', 'موقعیت')}</dt><dd>{L('Khairkhana, Kabul, Afghanistan', 'خیرخانه، کابل، افغانستان')}</dd></div>
          <div><dt>{L('Education', 'تحصیلات')}</dt><dd>{L('Computer science diploma — AIT (Afghanistan Institute of Technology)', 'دیپلوم کمپیوتر ساینس — AIT (انستیتوت تکنالوژی افغانستان)')}</dd></div>
          <div><dt>{L('Focus', 'تمرکز')}</dt><dd>{L('Web development, databases, IT & English training, AI-assisted work', 'توسعهٔ وب، پایگاه‌داده، آموزش آی‌تی و انگلیسی، کار با کمک هوش مصنوعی')}</dd></div>
          <div><dt>{L('Languages', 'زبان‌ها')}</dt><dd>{L('Dari / Persian, English', 'دری / فارسی، انگلیسی')}</dd></div>
          <div><dt>{L('Working hours', 'ساعات کاری')}</dt><dd>{L('Kabul time (UTC+4:30), remote', 'وقت کابل (UTC+4:30)، از راه دور')}</dd></div>
        </dl>
      </aside>
    </div>
  </section>
'''

    pillars = [
        dict(id='web', color='#E34F26', glyph='layout-dashboard',
             t=('Web development', 'توسعهٔ وب'),
             d=('Static and dynamic websites and web apps in HTML, CSS, JavaScript, Tailwind CSS, and PHP — including a learning platform with 450+ lessons and an online exam system, both live.',
                'وب‌سایت‌ها و اپلیکیشن‌های وب ایستا و پویا با HTML، CSS، جاوااسکریپت، Tailwind CSS و PHP — از جمله یک پلتفورم آموزشی با بیش از ۴۵۰ درس و یک سیستم امتحان آنلاین، هر دو فعال.'),
             ids=['html5', 'css3', 'javascript', 'tailwind', 'php']),
        dict(id='data', color='#38BDF8', glyph='database',
             t=('Databases', 'پایگاه‌داده'),
             d=('Design, queries, and administration in SQL, SQL Server, and Oracle — backed by a year managing the PHEMIS database at Payam University.',
                'طراحی، کوئری‌نویسی و مدیریت با SQL، SQL Server و Oracle — با پشتوانهٔ یک سال مدیریت پایگاه‌دادهٔ PHEMIS در پوهنتون پیام.'),
             ids=['sql', 'sqlserver', 'oracle']),
        dict(id='teach', color='#F59E0B', glyph='graduation-cap',
             t=('Teaching & training', 'تدریس و آموزش'),
             d=('English and computer instruction at five institutions, plus a free online academy — from computer basics and Windows to web development and MySQL.',
                'تدریس انگلیسی و کمپیوتر در پنج نهاد آموزشی، به‌علاوهٔ یک اکادمی آنلاین رایگان — از مبانی کمپیوتر و ویندوز تا توسعهٔ وب و MySQL.'),
             ids=['windows11', 'mysql', 'cpp', 'php', 'javascript']),
        dict(id='ai', color='#A78BFA', glyph='sparkles',
             t=('AI & automation', 'هوش مصنوعی و اتوماسیون'),
             d=('AI tools for building apps and sites, for office work, and for image and video generation — plus agents that automate repeat tasks.',
                'ابزارهای هوش مصنوعی برای ساخت اپلیکیشن و وب‌سایت، کارهای اداری، و تولید تصویر و ویدیو — به‌علاوهٔ ایجنت‌هایی که کارهای تکراری را خودکار می‌کنند.'),
             ids=['ai-tools', 'ai-build', 'gen-ai', 'ai-agents']),
    ]
    pcards = ''
    for p in pillars:
        pcards += f'''
      <article class="pillar ac-{p['id']} reveal">
        <span class="pillar__icon">{ic(p['glyph'])}</span>
        <h3>{L(*p['t'])}</h3>
        <p>{L(*p['d'])}</p>
        {minis(p['ids'])}
      </article>'''
    expertise = f'''
  <section class="section section--raised" id="expertise">
    <div class="wrap">
      <div class="section-head section-head--wide reveal">
        <h2>{L('What I do', 'کارهایی که انجام می‌دهم')}</h2>
        <p>{L('Four areas, each backed by real work — hover an icon to see the technology, click it to open its official site.', 'چهار حوزه، هرکدام با کار واقعی پشتوانه‌دار — روی آیکن‌ها بروید تا نام تکنالوژی را ببینید، روی آن بزنید تا سایت رسمی‌اش باز شود.')}</p>
      </div>
      <div class="pillar-grid reveal-group">{pcards}</div>
    </div>
  </section>
'''

    feat = ''.join(pf_card(p, compact=True) for p in PROJECTS)
    projects = f'''
  <section class="section" id="featured-projects">
    <div class="wrap">
      <div class="section-head section-head--wide reveal">
        <h2>{L('Live projects', 'پروژه‌های فعال')}</h2>
        <p>{L('Three websites I built and published — open any of them right now.', 'سه وب‌سایت که ساخته و منتشر کرده‌ام — هرکدام را همین حالا باز کنید.')}</p>
      </div>
      <div class="pf-list">{feat}</div>
      <div class="center-actions"><a class="btn btn--ghost" href="{href('projects')}">{L('All project details', 'جزئیات همهٔ پروژه‌ها')}</a></div>
    </div>
  </section>
'''

    xp_rows = ''
    for e in EXPERIENCE:
        d = f'<span class="chip">{esc(L(*e["dur"]))}</span>' if e['dur'] else '<span></span>'
        xp_rows += f'<li><strong>{esc(L(*e["role"]))}</strong><span>{esc(L(*e["org"]))}</span>{d}</li>'
    experience = f'''
  <section class="section section--raised" id="experience">
    <div class="wrap">
      <div class="section-head section-head--wide reveal">
        <h2>{L('Experience at a glance', 'مرور تجربهٔ کاری')}</h2>
        <p>{L('Six roles across database administration, freelance development, and teaching.', 'شش نقش در مدیریت پایگاه‌داده، توسعهٔ مستقل و تدریس.')}</p>
      </div>
      <ul class="xp-compact reveal">{xp_rows}</ul>
      <p class="mt-2 reveal"><a class="link-arrow" href="{href('about', '#experience')}">{L('Full experience and details', 'تجربهٔ کامل و جزئیات')}{ic('arrow-right')}</a></p>
    </div>
  </section>
'''

    core = ['html5', 'css3', 'javascript', 'tailwind', 'php', 'sqlserver', 'oracle', 'mysql', 'java', 'cpp', 'canva', 'netlify']
    stack = f'''
  <section class="section" id="technologies">
    <div class="wrap">
      <div class="section-head section-head--wide reveal">
        <h2>{L('Technologies I work with', 'تکنالوژی‌هایی که با آن‌ها کار می‌کنم')}</h2>
        <p>{L("Each tile carries the technology's own colour and logo and links to its official site.", 'هر کاشی رنگ و لوگوی خود آن تکنالوژی را دارد و به وب‌سایت رسمی‌اش لینک می‌شود.')}</p>
      </div>
      <div class="tile-grid tile-grid--compact reveal">{''.join(tile(t) for t in core)}</div>
      <p class="mt-2 reveal"><a class="link-arrow" href="{href('skills')}">{L('See every skill and tool', 'دیدن همهٔ مهارت‌ها و ابزارها')}{ic('arrow-right')}</a></p>
    </div>
  </section>
'''

    cred_items = [
        ('cred--cs', 'cpu', CRED_SECTIONS[0]['items'][0]),
        ('cred--en', 'languages', CRED_SECTIONS[1]['items'][1]),
        ('cred--gen', 'badge-check', dict(t=('Computer & English certificates', 'گواهینامه‌های کمپیوتر و انگلیسی'),
                                          org=('Ashley Roshan, Amozesh, Atarud Alingua', 'اشلی روشان، آموزش، Atarud Alingua'),
                                          kind=('Certificates', 'گواهینامه‌ها'))),
    ]
    creds = f'''
  <section class="section section--raised" id="credentials">
    <div class="wrap">
      <div class="section-head section-head--wide reveal">
        <h2>{L('Education & certificates', 'تحصیلات و گواهینامه‌ها')}</h2>
        <p>{L('A computer science diploma from AIT, and certificates in computing and English from several academies.', 'یک دیپلوم کمپیوتر ساینس از AIT و گواهینامه‌های کمپیوتر و انگلیسی از چندین اکادمی.')}</p>
      </div>
      <div class="cred-strip reveal-group">{''.join(cred_card(c, g, it) for c, g, it in cred_items)}</div>
      <p class="mt-2 reveal"><a class="link-arrow" href="{href('certifications')}">{L('All certificates', 'همهٔ گواهینامه‌ها')}{ic('arrow-right')}</a></p>
    </div>
  </section>
'''

    cta = cta_band(L('Have a website, a database, or a training program in mind?', 'وب‌سایت، پایگاه‌داده یا برنامهٔ آموزشی در نظر دارید؟'))
    return h + hero + profile + expertise + projects + experience + stack + creds + cta + footer(['typewriter'])

# ---------------------------------------------------------------- ABOUT
def about():
    C.key = 'about'
    title = L('About Ahmad Zaheer — Profile, Experience & Education', 'دربارهٔ احمد ظهیر — پروفایل، تجربه و تحصیلات')
    desc = L('Professional profile of Ahmad Zaheer: computer science graduate, database manager at Payam University, freelance web developer, and English & computer instructor in Kabul.',
             'پروفایل حرفه‌ای احمد ظهیر: فارغ‌التحصیل کمپیوتر ساینس، مدیر پایگاه‌داده در پوهنتون پیام، توسعه‌دهندهٔ مستقل وب و مدرس انگلیسی و کمپیوتر در کابل.')
    h = head(title, desc, jsonld=[person_jsonld()]) + header()

    top = f'''
  <section class="section hero-offset">
    <div class="wrap">
      <div class="grid cols-2 items-center">
        <div class="reveal">
          <div class="label">{L('Professional profile', 'پروفایل حرفه‌ای')}</div>
          <h1 class="title-lg">{L('A computer science graduate who builds systems — and teaches people to use them.', 'فارغ‌التحصیل کمپیوتر ساینس که سیستم می‌سازد — و استفاده از آن را آموزش می‌دهد.')}</h1>
          <p class="lede mt-2">{L('Computer & technology specialist based in Kabul: web development, database administration, and IT & English education — delivered in English and Dari.',
                                 'متخصص کمپیوتر و تکنالوژی مقیم کابل: توسعهٔ وب، مدیریت پایگاه‌داده و آموزش آی‌تی و انگلیسی — به دو زبان دری و انگلیسی.')}</p>
          <div class="flex-actions flex-actions--mt">
            <a class="btn btn--primary" href="{href('resume')}">{L('View CV', 'مشاهدهٔ رزومه')}</a>
            <a class="btn btn--ghost" href="{href('contact')}">{L('Get in touch', 'در تماس شوید')}</a>
          </div>
        </div>
        <div class="reveal">
          <div class="hero-visual max-w-sm mx-auto">
            <div class="chip-frame static-visible"><img src="{asset('ahmad-zaheer-640.jpg')}" alt="{L('Portrait of Ahmad Zaheer', 'عکس احمد ظهیر')}" width="640" height="640"></div>
            <div class="chip-pins" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span><span></span><span></span><span></span></div>
          </div>
        </div>
      </div>
    </div>
  </section>
'''

    summary = f'''
  <section class="section section--raised" id="profile">
    <div class="wrap profile-grid">
      <div class="reveal">
        <h2>{L('Summary', 'خلاصه')}</h2>
        <div class="stack mt-2">
          <p>{L("I hold a computer science diploma from the Afghanistan Institute of Technology (AIT) and work at the point where data, software, and teaching meet. I administered the PHEMIS database system at Payam University for a year, and I have taught English and computer courses at five institutions: Abraj, Ganja and Amozesh Educational Centers, Badr Academy, and Andisha-e-Noor Academy.",
                'دیپلوم کمپیوتر ساینس را از انستیتوت تکنالوژی افغانستان (AIT) دارم و در نقطهٔ تلاقی داده، نرم‌افزار و آموزش کار می‌کنم. یک سال سیستم پایگاه‌دادهٔ PHEMIS را در پوهنتون پیام مدیریت کرده‌ام و در پنج نهاد — ابراج، مراکز آموزشی گنجه و آموزش، اکادمی بدر و اکادمی اندیشه نور — انگلیسی و کمپیوتر تدریس کرده‌ام.')}</p>
          <p>{L('As a developer I build with HTML, CSS, JavaScript, Tailwind CSS, and PHP, and I work with SQL, SQL Server, and Oracle. I created and published two platforms of my own: Ahmad Zaheer Academy, a free programming academy with 11 courses and 450+ lessons, and Examina, an online and offline exam platform.',
                'به‌عنوان توسعه‌دهنده با HTML، CSS، جاوااسکریپت، Tailwind CSS و PHP می‌سازم و با SQL، SQL Server و Oracle کار می‌کنم. دو پلتفورم خودم را ساخته و منتشر کرده‌ام: آکادمی احمد ظهیر، یک اکادمی رایگان برنامه‌نویسی با ۱۱ دوره و بیش از ۴۵۰ درس، و Examina، یک پلتفورم امتحان آنلاین و آفلاین.')}</p>
          <p>{L('I also use AI tools, generative AI, and AI agents to speed up building software, producing media, and handling office work.',
                'همچنین از ابزارهای هوش مصنوعی، هوش مصنوعی مولد و ایجنت‌ها برای سرعت‌بخشیدن به ساخت نرم‌افزار، تولید رسانه و کارهای اداری استفاده می‌کنم.')}</p>
        </div>
      </div>
      <aside class="facts reveal" aria-label="{L('Key facts', 'اطلاعات کلیدی')}">
        <dl>
          <div><dt>{L('Title', 'عنوان')}</dt><dd>{ROLE()}</dd></div>
          <div><dt>{L('Based in', 'مقیم')}</dt><dd>{L('Khairkhana, Kabul, Afghanistan', 'خیرخانه، کابل، افغانستان')}</dd></div>
          <div><dt>{L('Education', 'تحصیلات')}</dt><dd>{L('Computer science diploma, AIT', 'دیپلوم کمپیوتر ساینس، AIT')}</dd></div>
          <div><dt>{L('Languages', 'زبان‌ها')}</dt><dd>{L('Dari / Persian, English', 'دری / فارسی، انگلیسی')}</dd></div>
          <div><dt>{L('Live sites', 'وب‌سایت‌های فعال')}</dt><dd>{''.join(f'<a class="ltr" href="{u}" target="_blank" rel="noopener noreferrer">{d}</a><br>' for d, u in SITES)}</dd></div>
        </dl>
      </aside>
    </div>
  </section>
'''

    experience = f'''
  <section class="section" id="experience">
    <div class="wrap">
      <div class="section-head section-head--wide reveal">
        <h2>{L('Experience', 'تجربهٔ کاری')}</h2>
        <p>{L('Six roles, grouped by kind of work. Durations are shown only where I have them.', 'شش نقش، دسته‌بندی‌شده بر اساس نوع کار. مدت فقط در جایی که موجود است نشان داده شده.')}</p>
      </div>
      {xp_groups()}
    </div>
  </section>
'''

    taught_ids = ['basics', 'windows11', 'html5', 'css3', 'javascript', 'php', 'cpp', 'mysql', 'ai-tools', 'english']
    teaching = f'''
  <section class="section section--raised" id="teaching">
    <div class="wrap">
      <div class="section-head section-head--wide reveal">
        <h2>{L('What I teach', 'آنچه تدریس می‌کنم')}</h2>
        <p>{L('The subjects covered by my free online academy, from a first computer to web development and databases — plus English.', 'موضوعاتی که در اکادمی آنلاین رایگان من پوشش داده می‌شود، از اولین کمپیوتر تا توسعهٔ وب و پایگاه‌داده — به‌علاوهٔ انگلیسی.')}</p>
      </div>
      <div class="tile-grid tile-grid--compact reveal">{''.join(tile(t) for t in taught_ids)}</div>
      <p class="mt-2 reveal"><a class="link-arrow" href="{href('projects/zaheer-academy')}">{L('About the academy', 'دربارهٔ اکادمی')}{ic('arrow-right')}</a></p>
    </div>
  </section>
'''

    education = f'''
  <section class="section" id="education">
    <div class="wrap">
      <div class="section-head section-head--wide reveal">
        <h2>{L('Education', 'تحصیلات')}</h2>
        <p>{L('A computer science diploma from AIT, supported by computer and English certificates.', 'دیپلوم کمپیوتر ساینس از AIT، به‌همراه گواهینامه‌های کمپیوتر و انگلیسی.')}</p>
      </div>
      <div class="cred-grid reveal-group">{''.join(cred_card(s['cls'], s['glyph'], it) for s in CRED_SECTIONS[:1] for it in s['items'][:1])}
        {cred_card('cred--en', 'languages', CRED_SECTIONS[1]['items'][1])}
        {cred_card('cred--gen', 'school', CRED_SECTIONS[2]['items'][0])}</div>
      <p class="mt-2 reveal"><a class="link-arrow" href="{href('certifications')}">{L('See all certificates', 'دیدن همهٔ گواهینامه‌ها')}{ic('arrow-right')}</a></p>
    </div>
  </section>
'''

    languages = f'''
  <section class="section section--raised" id="languages">
    <div class="wrap">
      <div class="section-head section-head--wide reveal"><h2>{L('Languages', 'زبان‌ها')}</h2></div>
      <div class="lang-rows reveal-group">
        <div class="lang-row reveal"><span class="chip">{L('Native', 'مادری')}</span><h3>{L('Dari / Persian', 'دری / فارسی')}</h3>
          <p>{L('Daily working language: teaching, documentation, and right-to-left web design.', 'زبان کاری روزمره: تدریس، مستندسازی و طراحی وب راست‌به‌چپ.')}</p></div>
        <div class="lang-row reveal"><span class="chip">{L('Professional', 'حرفه‌ای')}</span><h3>{L('English', 'انگلیسی')}</h3>
          <p>{L('Taught as an instructor; TECOL diploma and further English certificates.', 'به‌عنوان استاد تدریس شده؛ دارای دیپلوم TECOL و گواهینامه‌های بیشتر انگلیسی.')}</p></div>
      </div>
    </div>
  </section>
'''

    principles = [
        (L('Clarity beats cleverness', 'وضوح بر زیرکی برتری دارد'),
         L('A good lesson and a good interface share one rule: the person on the other side should never have to guess.',
           'یک درس خوب و یک رابط خوب یک قاعده دارند: کسی که آن طرف است هرگز نباید مجبور به حدس‌زدن شود.'), 'compass'),
        (L('Plain tools, lasting pages', 'ابزار ساده، صفحات ماندگار'),
         L('My live sites are built with plain HTML, CSS, and JavaScript — no framework to maintain, and nothing that breaks when a dependency changes.',
           'وب‌سایت‌های فعال من با HTML، CSS و جاوااسکریپت خالص ساخته شده‌اند — بدون فریم‌ورکی که نگهداری شود و بدون چیزی که با تغییر یک وابستگی خراب شود.'), 'code-xml'),
        (L('Two languages, one standard', 'دو زبان، یک استاندارد'),
         L('I write and teach in Dari and English, and I build right-to-left layouts natively instead of flipping an English template.',
           'به دری و انگلیسی می‌نویسم و تدریس می‌کنم، و چیدمان راست‌به‌چپ را از پایه می‌سازم، نه با وارونه‌کردن یک قالب انگلیسی.'), 'languages'),
    ]
    pr = ''.join(f'<article class="step reveal"><span class="pillar__icon">{ic(g)}</span><h3>{t}</h3><p>{d}</p></article>' for t, d, g in principles)
    how = f'''
  <section class="section" id="how-i-work">
    <div class="wrap">
      <div class="section-head section-head--wide reveal"><h2>{L('How I work', 'روش کار من')}</h2></div>
      <div class="steps steps--plain reveal-group">{pr}</div>
    </div>
  </section>
'''
    cta = cta_band(L('Want the full picture on one page?', 'تصویر کامل را در یک صفحه می‌خواهید؟'),
                   primary=('resume', L('Open the CV', 'باز کردن رزومه')), secondary=('contact', L('Get in touch', 'در تماس شوید')))
    return h + top + summary + experience + teaching + education + languages + how + cta + footer()

# ---------------------------------------------------------------- SKILLS
def skills():
    C.key = 'skills'
    title = L('Skills & Technologies — Ahmad Zaheer', 'مهارت‌ها و تکنالوژی‌ها — احمد ظهیر')
    desc = L('Web development, databases, programming fundamentals, AI and automation, design, and core concepts — every technology with its own brand colour, logo, and link to its official site.',
             'توسعهٔ وب، پایگاه‌داده، مبانی برنامه‌نویسی، هوش مصنوعی و اتوماسیون، طراحی و مفاهیم پایه — هر تکنالوژی با رنگ و لوگوی خودش و لینک به سایت رسمی‌اش.')
    h = head(title, desc, jsonld=[person_jsonld()]) + header()
    filters = f'<button type="button" class="filter-btn is-active" data-filter="all" aria-pressed="true">{L("All", "همه")}</button>' + ''.join(
        f'<button type="button" class="filter-btn" data-filter="{c["id"]}" aria-pressed="false">{esc(L(c["en"], c["fa"]))}</button>' for c in CATS)
    sections = ''
    for c in CATS:
        sections += f'''
      <section class="skill-section sc-{c['id']}" id="{c['id']}" data-cat="{c['id']}" aria-labelledby="cat-{c['id']}">
        <div class="skill-section__head">
          <span class="skill-section__icon">{ic(c['glyph'])}</span>
          <h2 id="cat-{c['id']}">{esc(L(c['en'], c['fa']))}</h2>
          <p>{esc(L(c['desc_en'], c['desc_fa']))}</p>
        </div>
        <div class="tile-grid">{''.join(tile(t) for t in c['items'])}</div>
      </section>'''
    main = f'''
  <section class="page-head">
    <div class="wrap">
      <div class="reveal">
        <div class="label">{L('Skills & technologies', 'مهارت‌ها و تکنالوژی‌ها')}</div>
        <h1>{L('Everything I build with, in one place.', 'همهٔ آنچه با آن می‌سازم، یک‌جا.')}</h1>
        <p class="lede">{L("Grouped by kind of work. Every tile carries the technology's own colour and logo, and links to its official site.", 'دسته‌بندی‌شده بر اساس نوع کار. هر کاشی رنگ و لوگوی خود آن تکنالوژی را دارد و به وب‌سایت رسمی‌اش لینک می‌شود.')}</p>
      </div>
      <div class="filter-bar filter-bar--skills reveal" role="group" aria-label="{L('Filter skills by category', 'فیلتر مهارت‌ها بر اساس دسته')}">
        <div class="filter-group">{filters}</div>
      </div>
    </div>
  </section>
  <section class="section section--tight">
    <div class="wrap">{sections}
      <p class="footnote">{L('Java and C++ are listed as fundamentals. Tiles without a brand logo (SQL as a language, the AI categories, image editing, and concepts) use a neutral icon, because no single official logo exists for them; Affinity is shown as a monogram.',
                             'جاوا و C++ به‌عنوان مبانی ذکر شده‌اند. کاشی‌های بدون لوگوی برند (SQL به‌عنوان زبان، دسته‌های هوش مصنوعی، ویرایش تصویر و مفاهیم) آیکن خنثی دارند، چون لوگوی رسمی واحدی برای آن‌ها وجود ندارد؛ Affinity با تک‌حرفی نشان داده شده است.')}</p>
    </div>
  </section>
'''
    cta = cta_band(L('Need one of these skills on your project?', 'روی پروژهٔ خود به یکی از این مهارت‌ها نیاز دارید؟'),
                   primary=('contact', None), secondary=('services', L('See services', 'دیدن خدمات')))
    return h + main + cta + footer(['skills'])
