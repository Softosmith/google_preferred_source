# -*- coding: utf-8 -*-
def migrate(cr, version):
    cr.execute("""
        UPDATE website SET google_preferred_source_mode = 'js'
         WHERE google_preferred_source_mode = 'advanced_js'
    """)
