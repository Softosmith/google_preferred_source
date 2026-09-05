# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Copyright (C) 2026 Asad Ali (https://softosmith.com)

from odoo import api, fields, models
from urllib.parse import quote, urlparse


class Website(models.Model):
    _inherit = 'website'

    has_google_preferred_source = fields.Boolean(
        string="Google Preferred Source",
        help="Allow website visitors to add your site as a preferred source in Google Search."
    )
    google_preferred_source_theme = fields.Selection([
        ('light', 'Light'),
        ('dark', 'Dark'),
    ], string="Button Theme", default='light', required=True)

    google_preferred_source_lang = fields.Char(
        string="Button Language Override",
        help="Language code override (e.g. en, es, fr). Leave blank to match browser/page language."
    )

    google_preferred_source_auto_footer = fields.Boolean(
        string="Show in Footer",
        help="Automatically display the Preferred Source button in the website footer."
    )

    def get_google_preferred_source_url(self):
        """Build the Google Source Preferences deeplink URL for the current website domain."""
        self.ensure_one()
        domain = self.domain or self.get_base_url()
        if domain:
            parsed = urlparse(domain if '://' in domain else f'https://{domain}')
            host = parsed.netloc or parsed.path
            clean_domain = host.split(':')[0] if ':' in host else host
            if clean_domain:
                return f"https://www.google.com/preferences/source?q={quote(clean_domain)}"
        return "https://www.google.com/preferences/source"
