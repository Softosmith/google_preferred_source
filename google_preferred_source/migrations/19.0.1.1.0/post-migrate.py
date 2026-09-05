# -*- coding: utf-8 -*-
def migrate(cr, version):
    # google_preferred_source_mode was removed in 19.0.2.0.0 - guard against
    # upgrades that already dropped the column before this step runs.
    cr.execute("""
        SELECT 1 FROM information_schema.columns
         WHERE table_name = 'website' AND column_name = 'google_preferred_source_mode'
    """)
    if not cr.fetchone():
        return
    cr.execute("""
        UPDATE website SET google_preferred_source_mode = 'js'
         WHERE google_preferred_source_mode = 'advanced_js'
    """)
