{
    'name': 'Google Preferred Source - SEO & AI Search (GEO) Booster',
    'version': '18.0.1.0.0',
    'category': 'Website/Website',
    'summary': 'SEO & GEO booster: get picked as a Preferred Source in Google SERP, Top Stories & AI Overviews',
    'description': """
Google Preferred Source - SEO & AI Search (GEO) Booster for Odoo 18
===================================================================
An SEO and GEO (Generative Engine Optimization) tool for your Odoo Website. It adds
Google's official Preferred Sources button to your site so readers can tell Google:
"show me more from this site". Depends only on the Website app - no eCommerce or
Invoicing required.

Running an online store? Use the separate "Google Preferred Source - eCommerce Product
Pages" add-on instead, built specifically for website_sale product pages.

Why it matters for SEO and AI search:
-------------------------------------
* **Google SERP ranking signal**: Visitors who mark you as a preferred source see your
  pages surface higher and more often in their Google Search results (SERP).
* **Top Stories placement**: Publishers and news sites get repeated Top Stories
  visibility with the readers who opted in.
* **AI Overviews / GEO / AEO**: Google's AI Overviews and AI Mode draw on the sources a
  user prefers. Being a preferred source is one of the few direct levers you have on
  AI search visibility - Generative Engine Optimization and Answer Engine Optimization.
* **Brand-loyal organic traffic**: Zero ad spend. Each opt-in is a long-lived organic
  search signal for that reader.
* **Great for**: news and magazine publishers, blogs, content marketing sites,
  eCommerce brands, SaaS sites, and any Odoo website doing serious SEO.

Key Features:
-------------
* **Per-Website Configuration**: Configure integration mode, theme, and language per website in Website Settings.
* **Standard JavaScript SDK**: Automatic rendering of Google's official localized badge, with an automatic fallback link if the SDK doesn't render in time.
* **Drag-and-Drop Website Building Block**: Add the "Google Preferred Source" snippet anywhere on your pages via Website Builder.
* **Automatic Placement Options**: Optionally display in Website Footer or eCommerce Product Pages.
* **Responsive & Localized**: Supports Light and Dark themes and automatic or manual language overrides.
* **SEO safe**: No layout shift, no render blocking, no impact on Core Web Vitals.

Keywords: SEO, GEO, AEO, Google SERP, AI Overviews, AI Mode, generative engine
optimization, answer engine optimization, AI search visibility, Google Search, Top
Stories, organic traffic, website SEO, publisher SEO.

Developed by Asad Ali at Softosmith (https://softosmith.com).
    """,
    'author': 'Asad Ali (Softosmith)',
    'website': 'https://softosmith.com',
    'support': 'support@softosmith.com',
    'license': 'LGPL-3',
    'price': 0.0,
    'currency': 'EUR',
    'depends': [
        'website',
    ],
    'data': [
        'views/res_config_settings_views.xml',
        'views/snippets/s_google_preferred_source.xml',
        'views/snippets/snippets.xml',
        'views/website_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'google_preferred_source/static/src/snippets/s_google_preferred_source/000.scss',
            'google_preferred_source/static/src/snippets/s_google_preferred_source/000.js',
        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/screenshot_settings.png',
        'static/description/screenshot_badge_footer.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
