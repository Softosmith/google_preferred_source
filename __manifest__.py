{
    'name': 'Google Preferred Source',
    'version': '19.0.1.0.0',
    'category': 'Website/Website',
    'summary': 'Help readers and shoppers find your publication/store as a preferred source in Google Search, Top Stories & AI Overviews',
    'description': """
Google Preferred Sources for Odoo 19 Website & eCommerce
=========================================================
Integrate Google's official Preferred Sources SDK and Deeplink flow into your Odoo Website and eCommerce store.

Developed by Asad Ali at Softosmith (https://softosmith.com).

Key Features:
-------------
* **Per-Website Configuration**: Configure integration mode, theme, and language per website in Website Settings.
* **Standard JavaScript SDK**: Automatic rendering of Google's official localized badge.
* **Advanced JavaScript Mode**: Programmatic initialization and custom trigger handling.
* **Deeplink Direct URL**: Direct fallback to Google's Source Preferences tool (`https://www.google.com/preferences/source?q=DOMAIN`).
* **Drag-and-Drop Website Building Block**: Add the "Google Preferred Source" snippet anywhere on your pages via Website Builder.
* **Automatic Placement Options**: Optionally display in Website Footer or eCommerce Product Pages.
* **Responsive & Localized**: Supports Light and Dark themes and automatic or manual language overrides.
    """,
    'author': 'Asad Ali (Softosmith)',
    'website': 'https://softosmith.com',
    'support': 'support@softosmith.com',
    'license': 'LGPL-3',
    'price': 0.0,
    'currency': 'EUR',
    'depends': [
        'website',
        'website_sale',
    ],
    'data': [
        'views/res_config_settings_views.xml',
        'views/snippets/s_google_preferred_source.xml',
        'views/snippets/snippets.xml',
        'views/website_templates.xml',
        'views/website_sale_templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'google_preferred_source/static/src/snippets/s_google_preferred_source/000.scss',
            'google_preferred_source/static/src/snippets/s_google_preferred_source/000.js',
        ],
    },
    'images': [
        'static/description/banner.png',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
