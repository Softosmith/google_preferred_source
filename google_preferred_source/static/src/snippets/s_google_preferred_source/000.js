/** @odoo-module **/

import publicWidget from "@web/legacy/js/public/public_widget";

const SDK_RENDER_TIMEOUT = 3000;

publicWidget.registry.GooglePreferredSource = publicWidget.Widget.extend({
    selector: ".s_google_preferred_source",
    disabledInEditableMode: false,

    start: function () {
        this.slotEl = this.el.querySelector(".o_google_pref_sdk_slot");
        this.fallbackEl = this.el.querySelector(".o_google_pref_fallback");
        this._timeoutId = null;

        if (this.slotEl && this.fallbackEl) {
            this._timeoutId = setTimeout(
                () => this.showFallbackIfEmpty(),
                SDK_RENDER_TIMEOUT
            );
        }
        return this._super.apply(this, arguments);
    },

    destroy: function () {
        if (this._timeoutId) {
            clearTimeout(this._timeoutId);
            this._timeoutId = null;
        }
        this._super.apply(this, arguments);
    },

    showFallbackIfEmpty: function () {
        if (!this.slotEl || !this.fallbackEl) {
            return;
        }
        const rendered = this.slotEl.shadowRoot
            || this.slotEl.childElementCount > 0
            || this.slotEl.getBoundingClientRect().height > 0;
        if (!rendered) {
            this.slotEl.classList.add("d-none");
            this.fallbackEl.classList.remove("d-none");
        }
    },
});

export default publicWidget.registry.GooglePreferredSource;
