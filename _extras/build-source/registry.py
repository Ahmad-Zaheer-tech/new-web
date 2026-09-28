# -*- coding: utf-8 -*-
"""
Technology registry — the single source of truth for every technology tile
on the site (home, skills, services, CV).

  color : the technology's own brand colour (used for the accent + icon well)
  icon  : file in assets/tech/ (official full-colour logo, from Devicon / Simple Icons)
  glyph : neutral Lucide glyph, used ONLY where no official logo exists
          (concepts, AI categories, SQL as a language, Affinity)
  url   : the technology's official site. None when there is no single owner
          (e.g. SQL, general concepts) — those tiles are not links.
"""

TECH = {
    # ---- Web development --------------------------------------------------
    'html5': dict(en='HTML5', fa='HTML5', color='#E34F26', icon='html5.svg',
                  url='https://html.spec.whatwg.org/multipage/', cat='web'),
    'css3': dict(en='CSS3', fa='CSS3', color='#1572B6', icon='css3.svg',
                 url='https://www.w3.org/Style/CSS/', cat='web'),
    'javascript': dict(en='JavaScript', fa='جاوااسکریپت', color='#F7DF1E', icon='javascript.svg',
                       url='https://developer.mozilla.org/en-US/docs/Web/JavaScript', cat='web'),
    'tailwind': dict(en='Tailwind CSS', fa='Tailwind CSS', color='#06B6D4', icon='tailwindcss.svg',
                     url='https://tailwindcss.com', cat='web'),
    'php': dict(en='PHP', fa='PHP', color='#777BB4', icon='php.svg', plate=True,
                url='https://www.php.net', cat='web'),
    'netlify': dict(en='Netlify', fa='Netlify', color='#00C7B7', icon='netlify.svg',
                    url='https://www.netlify.com', cat='web',
                    note_en='hosting for my live sites', note_fa='میزبانی وب‌سایت‌های فعال من'),

    # ---- Databases --------------------------------------------------------
    'sql': dict(en='SQL', fa='SQL', color='#38BDF8', glyph='database', url=None, cat='data',
                note_en='the query language', note_fa='زبان پرس‌وجو'),
    'sqlserver': dict(en='SQL Server', fa='SQL Server', color='#CC2927', icon='microsoftsqlserver.svg', plate=True,
                      url='https://www.microsoft.com/sql-server', cat='data'),
    'oracle': dict(en='Oracle Database', fa='Oracle Database', color='#F80000', icon='oracle.svg', plate=True,
                   url='https://www.oracle.com/database/', cat='data'),
    'mysql': dict(en='MySQL', fa='MySQL', color='#4479A1', icon='mysql.svg', plate=True,
                  url='https://www.mysql.com', cat='data',
                  note_en='taught in my academy', note_fa='تدریس‌شده در اکادمی من'),

    # ---- Programming fundamentals ----------------------------------------
    'java': dict(en='Java', fa='جاوا', color='#ED8B00', icon='java.svg', plate=True,
                 url='https://www.oracle.com/java/', cat='lang',
                 note_en='fundamentals', note_fa='مبانی'),
    'cpp': dict(en='C++', fa='C++', color='#00599C', icon='cplusplus.svg', plate=True,
                url='https://isocpp.org', cat='lang',
                note_en='fundamentals', note_fa='مبانی'),

    # ---- AI & automation (no vendor logos: none were named) --------------
    'ai-tools': dict(en='AI tools', fa='ابزارهای هوش مصنوعی', color='#A78BFA', glyph='sparkles',
                     url=None, cat='ai'),
    'ai-build': dict(en='AI-assisted development', fa='توسعه با کمک هوش مصنوعی', color='#F59E0B',
                     glyph='wand-sparkles', url=None, cat='ai',
                     note_en='apps, dynamic & static sites', note_fa='اپلیکیشن، سایت پویا و ایستا'),
    'ai-office': dict(en='AI for office work', fa='هوش مصنوعی برای کارهای اداری', color='#60A5FA',
                      glyph='file-text', url=None, cat='ai',
                      note_en='Word & documents', note_fa='ورد و اسناد'),
    'gen-ai': dict(en='Generative AI', fa='هوش مصنوعی مولد', color='#F472B6', glyph='clapperboard',
                   url=None, cat='ai', note_en='image & video', note_fa='تصویر و ویدیو'),
    'ai-agents': dict(en='AI agents & automation', fa='ایجنت‌های هوش مصنوعی و اتوماسیون', color='#34D399',
                      glyph='bot', url=None, cat='ai'),

    # ---- Design & media ---------------------------------------------------
    'canva': dict(en='Canva', fa='Canva', color='#00C4CC', icon='canva.svg',
                  url='https://www.canva.com', cat='design'),
    'affinity': dict(en='Affinity', fa='Affinity', color='#7E4DD2', monogram='Af',
                     url='https://affinity.serif.com', cat='design'),
    'image-edit': dict(en='Image editing', fa='ویرایش تصویر', color='#FB7185', glyph='image',
                       url=None, cat='design'),

    # ---- IT fundamentals: the CIT and DIT programs of ICDL ------------------
    'cit': dict(en='CIT', fa='CIT', color='#3B82F6', glyph='monitor', url=None, cat='icdl',
                note_en='ICDL program', note_fa='برنامهٔ ICDL'),
    'dit': dict(en='DIT', fa='DIT', color='#6366F1', glyph='laptop', url=None, cat='icdl',
                note_en='ICDL program', note_fa='برنامهٔ ICDL'),
    'office-pkg': dict(en='Office package', fa='بستهٔ آفیس', color='#F97316', glyph='files', url=None, cat='icdl'),
    'practical-project': dict(en='Practical project', fa='پروژهٔ عملی', color='#14B8A6', glyph='clipboard-check', url=None, cat='icdl'),
    'internet': dict(en='Network basics & internet use', fa='مبانی شبکه و استفاده از انترنت', color='#0EA5E9', glyph='globe', url=None, cat='icdl'),
    'typography': dict(en='Typography', fa='تایپوگرافی', color='#EC4899', glyph='type', url=None, cat='icdl'),
    'computer-tech': dict(en='Computer techniques', fa='تکنیک‌های کمپیوتر', color='#84CC16', glyph='cpu', url=None, cat='icdl'),

    # ---- Foundations ------------------------------------------------------
    'db-concepts': dict(en='Database concepts', fa='مفاهیم پایگاه‌داده', color='#22D3EE',
                        glyph='database', url=None, cat='found'),
    'net-concepts': dict(en='Networking concepts', fa='مفاهیم شبکه', color='#4ADE80',
                         glyph='network', url=None, cat='found'),
    'roadmaps': dict(en='Tech roadmaps', fa='نقشه‌های راه تکنالوژی', color='#FBBF24', glyph='route',
                     url='https://zaheer-tech.netlify.app/paths', cat='found',
                     note_en='learning paths in my academy', note_fa='مسیرهای یادگیری در اکادمی من'),

    # ---- Taught subjects (About page + academy detail page) ----------------
    'basics': dict(en='Computer basics', fa='مبانی کمپیوتر', color='#94A3B8', glyph='monitor', url=None, cat='taught'),
    'english': dict(en='English language', fa='زبان انگلیسی', color='#F59E0B', glyph='languages', url=None, cat='taught',
                    note_en='IPA & CEFR-based course', note_fa='دورهٔ مبتنی بر IPA و CEFR'),
    'windows11': dict(en='Windows 11', fa='ویندوز ۱۱', color='#0078D4', icon='windows11.svg',
                      url='https://www.microsoft.com/windows/windows-11', cat='taught'),
}

CATS = [
    dict(id='web', glyph='code-xml', color='#E34F26',
         en='Web development', fa='توسعه وب',
         desc_en='Everything I use to design, build, and publish websites and web apps.',
         desc_fa='همهٔ آنچه برای طراحی، ساخت و انتشار وب‌سایت و اپلیکیشن وب به کار می‌برم.',
         items=['html5', 'css3', 'javascript', 'tailwind', 'php', 'netlify']),
    dict(id='data', glyph='database', color='#CC2927',
         en='Databases', fa='پایگاه‌داده',
         desc_en='Design, queries, and day-to-day administration.',
         desc_fa='طراحی، کوئری‌نویسی و مدیریت روزمره.',
         items=['sql', 'sqlserver', 'oracle', 'mysql']),
    dict(id='lang', glyph='terminal', color='#3B9BE0',
         en='Programming fundamentals', fa='مبانی برنامه‌نویسی',
         desc_en='Working knowledge of two general-purpose languages.',
         desc_fa='آشنایی کاری با دو زبان برنامه‌نویسی عمومی.',
         items=['java', 'cpp']),
    dict(id='ai', glyph='sparkles', color='#A78BFA',
         en='AI & automation', fa='هوش مصنوعی و اتوماسیون',
         desc_en='AI applied to building software, office work, media, and repeat tasks.',
         desc_fa='هوش مصنوعی برای ساخت نرم‌افزار، کارهای اداری، رسانه و کارهای تکراری.',
         items=['ai-tools', 'ai-build', 'ai-office', 'gen-ai', 'ai-agents']),
    dict(id='design', glyph='palette', color='#00C4CC',
         en='Design & media', fa='طراحی و رسانه',
         desc_en='Graphics and image work.',
         desc_fa='طراحی گرافیک و کار با تصویر.',
         items=['canva', 'affinity', 'image-edit']),
    dict(id='icdl', glyph='monitor', color='#3B82F6',
         en='IT fundamentals (ICDL)', fa='مبانی آی‌تی (ICDL)',
         desc_en='The CIT and DIT programs of ICDL: the Office package, a practical project, network basics and internet use, typography, and computer techniques.',
         desc_fa='برنامه‌های CIT و DIT از ICDL: بستهٔ آفیس، پروژهٔ عملی، مبانی شبکه و استفاده از انترنت، تایپوگرافی و تکنیک‌های کمپیوتر.',
         items=['cit', 'dit', 'office-pkg', 'practical-project', 'internet', 'typography', 'computer-tech']),
    dict(id='found', glyph='layers', color='#4ADE80',
         en='Foundations', fa='مفاهیم پایه',
         desc_en='Concepts that sit underneath every project.',
         desc_fa='مفاهیمی که زیربنای هر پروژه‌اند.',
         items=['db-concepts', 'net-concepts', 'roadmaps']),
]
