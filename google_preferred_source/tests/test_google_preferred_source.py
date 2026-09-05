# -*- coding: utf-8 -*-
from odoo.tests.common import TransactionCase, tagged


@tagged('post_install', '-at_install')
class TestGooglePreferredSource(TransactionCase):

    def setUp(self):
        super(TestGooglePreferredSource, self).setUp()
        self.website = self.env['website'].create({
            'name': 'Test Google Preferred Source Website',
            'domain': 'https://mytestshop.com',
            'has_google_preferred_source': True,
            'google_preferred_source_theme': 'dark',
            'google_preferred_source_lang': 'fr',
            'google_preferred_source_auto_footer': True,
        })

    def test_get_google_preferred_source_url(self):
        """Test URL formatting for Google Preferred Source deeplink."""
        url = self.website.get_google_preferred_source_url()
        self.assertEqual(url, "https://www.google.com/preferences/source?q=mytestshop.com")

    def test_get_google_preferred_source_url_with_port(self):
        """Test URL formatting when website domain contains a port number."""
        self.website.domain = "http://mytestshop.com:8069"
        url = self.website.get_google_preferred_source_url()
        self.assertEqual(url, "https://www.google.com/preferences/source?q=mytestshop.com")

    def test_config_settings_propagation(self):
        """Test propagation of settings from res.config.settings to res.website."""
        config = self.env['res.config.settings'].create({
            'website_id': self.website.id,
            'has_google_preferred_source': True,
            'google_preferred_source_theme': 'light',
            'google_preferred_source_lang': 'de',
        })
        config.execute()
        self.assertEqual(self.website.google_preferred_source_theme, 'light')
        self.assertEqual(self.website.google_preferred_source_lang, 'de')
