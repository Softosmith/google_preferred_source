import { Interaction } from "@web/public/interaction";
import { registry } from "@web/core/registry";

export class GooglePreferredSource extends Interaction {
    static selector = ".s_google_preferred_source";

    setup() {
        const manualBtn = this.el.querySelector(".o_google_pref_manual_trigger");
        if (manualBtn) {
            this.addListener(manualBtn, "click", (ev) => {
                ev.preventDefault();
                if (window.PREFERRED_SOURCE) {
                    if (typeof window.PREFERRED_SOURCE.addPreferredSource === "function") {
                        window.PREFERRED_SOURCE.addPreferredSource();
                    } else if (Array.isArray(window.PREFERRED_SOURCE)) {
                        window.PREFERRED_SOURCE.push((ps) => {
                            if (ps && typeof ps.addPreferredSource === "function") {
                                ps.addPreferredSource();
                            }
                        });
                    }
                }
            });
        }
    }
}

registry.category("public.interactions").add("google_preferred_source.s_google_preferred_source", GooglePreferredSource);
