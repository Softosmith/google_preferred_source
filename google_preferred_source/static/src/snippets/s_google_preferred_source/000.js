import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";

const SDK_RENDER_TIMEOUT = 3000;

export class GooglePreferredSource extends Interaction {
    static selector = ".s_google_preferred_source";

    setup() {
        this.slotEl = this.el.querySelector(".o_google_pref_sdk_slot");
        this.fallbackEl = this.el.querySelector(".o_google_pref_fallback");
        this._timeoutId = null;
    }

    start() {
        if (this.slotEl && this.fallbackEl) {
            this._timeoutId = setTimeout(
                () => this.showFallbackIfEmpty(),
                SDK_RENDER_TIMEOUT
            );
        }
    }

    destroy() {
        if (this._timeoutId) {
            clearTimeout(this._timeoutId);
            this._timeoutId = null;
        }
        super.destroy();
    }

    showFallbackIfEmpty() {
        const rendered = this.slotEl.shadowRoot
            || this.slotEl.childElementCount > 0
            || this.slotEl.getBoundingClientRect().height > 0;
        if (!rendered) {
            this.slotEl.classList.add("d-none");
            this.fallbackEl.classList.remove("d-none");
        }
    }
}

registry.category("public.interactions").add(
    "google_preferred_source.s_google_preferred_source", GooglePreferredSource);
