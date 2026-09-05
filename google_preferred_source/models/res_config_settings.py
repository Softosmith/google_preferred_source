# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
# Copyright (C) 2026 Asad Ali (https://softosmith.com)

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    has_google_preferred_source = fields.Boolean(
        related='website_id.has_google_preferred_source',
        readonly=False,
    )
    google_preferred_source_theme = fields.Selection(
        related='website_id.google_preferred_source_theme',
        readonly=False,
    )
    google_preferred_source_lang = fields.Char(
        related='website_id.google_preferred_source_lang',
        readonly=False,
    )
    google_preferred_source_auto_footer = fields.Boolean(
        related='website_id.google_preferred_source_auto_footer',
        readonly=False,
    )
