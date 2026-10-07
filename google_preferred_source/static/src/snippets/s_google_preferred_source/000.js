import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";

const SDK_RENDER_TIMEOUT = 3000;

const GOOGLE_G_SVG = `<svg class="o_google_g_logo me-2" width="18" height="18" viewBox="0 0 18 18" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path fill="#4285F4" d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844c-.209 1.125-.843 2.078-1.796 2.717v2.258h2.908c1.702-1.567 2.684-3.874 2.684-6.616z"/><path fill="#34A853" d="M9 18c2.43 0 4.467-.806 5.956-2.184l-2.908-2.258c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332C2.438 15.983 5.482 18 9 18z"/><path fill="#FBBC05" d="M3.964 10.707c-.18-.54-.282-1.117-.282-1.707s.102-1.167.282-1.707V4.961H.957C.347 6.175 0 7.55 0 9s.348 2.825.957 4.039l3.007-2.332z"/><path fill="#EA4335" d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0 5.482 0 2.438 2.017.957 4.961L3.964 7.293C4.672 5.166 6.656 3.58 9 3.58z"/></svg>`;

export class GooglePreferredSource extends Interaction {
    static selector = ".s_google_preferred_source";

    setup() {
        this.slotEl = this.el.querySelector(".o_google_pref_sdk_slot");
        this.fallbackEl = this.el.querySelector(".o_google_pref_fallback");
        this.cleanLegacyElements();
    }

    cleanLegacyElements() {
        if (!this.fallbackEl) return;
        const ext = this.fallbackEl.querySelector(".fa-external-link");
        if (ext) ext.remove();

        const faGoogle = this.fallbackEl.querySelector(".fa-google");
        if (faGoogle && !this.fallbackEl.querySelector(".o_google_g_logo")) {
            faGoogle.insertAdjacentHTML("beforebegin", GOOGLE_G_SVG);
            faGoogle.remove();
        }

        const span = this.fallbackEl.querySelector("span");
        if (span && span.textContent.includes("Add as Preferred Source")) {
            span.textContent = "Add to Preferred Sources";
            span.classList.add("o_google_pref_text");
        }
    }

    start() {
        if (document.body.classList.contains("editor_enable") || document.documentElement.classList.contains("editor_enable")) {
            return;
        }
        if (this.slotEl && this.fallbackEl) {
            this.waitForTimeout(this.showFallbackIfEmpty, SDK_RENDER_TIMEOUT);
        }
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
