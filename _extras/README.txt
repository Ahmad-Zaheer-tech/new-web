Ahmad Zaheer — Portfolio  |  پورتفولیوی احمد ظهیر
=================================================

ساختار / Structure
  (root)            وب‌سایت کامل — index.html در ریشه است. کل این پوشه را روی Netlify آپلود کنید.
                    The website — index.html is at the root. Upload this whole folder to Netlify.
  fa/               نسخهٔ دری / Dari (RTL) pages
  projects/         English project details
  css/ js/ assets/  styles, scripts, fonts, tech logos, icons, images, CV PDFs
  _redirects        Netlify rule: hides _extras/ from the public web
  _extras/          فایل‌های تکمیلی (منتشر نمی‌شوند / not publicly served)
     cv/                     CV PDFs (Dari + English)
     retired-case-studies/   six earlier case studies not found in your own data
     build-source/           Python scripts that generate every page (python3 build.py)
     set-domain.py           puts your real site address into canonical/sitemap/robots

فورم تماس / Contact form
  از Netlify Forms استفاده می‌کند — نیازی به Formspree یا هیچ شناسه‌ای نیست.
  Uses Netlify Forms: no Formspree or any ID needed. After the first deploy:
    Netlify > your site > Forms  (پیام‌ها اینجا ذخیره می‌شوند / submissions are stored here)
    Forms > Form notifications > Add notification > Email  -> ansarwaqef7@gmail.com
  If "Forms" is not active: Site configuration > Forms > Enable form detection, then redeploy.

آدرس سایت / Site address
  canonical, og:url, sitemap و robots هنوز آدرس نمونهٔ https://ahmadzaheer.dev دارند.
  آدرس واقعی خود را یک‌بار وارد کنید:
    python3 _extras/set-domain.py https://YOUR-SITE.netlify.app
  سپس پوشه را دوباره آپلود کنید.

باقی‌مانده / Still to set (js/config.js): gaMeasurementId (اختیاری / optional), mapQuery (exact coordinates).
