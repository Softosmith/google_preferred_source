# Store assets — copy, paste, done

`index.html` references these files by plain relative filename. All 9 must exist in
`static/description/` before publishing, or the listing shows broken-image icons.
Only **png / gif / jpeg** are accepted by the Odoo Apps store.

| File | Size | How |
|---|---|---|
| `banner.png` | 1200×630 | Prompt 1 — has text |
| `hero.png` | 1200×500 | Prompt 2 — has text |
| `icon.png` | 256×256 | Prompt 3 — no text |
| `feature_sdk.png` | 256×256 transparent | Prompt 4 — no text |
| `feature_ecommerce.png` | 256×256 transparent | Prompt 5 — no text |
| `feature_snippet.png` | 256×256 transparent | Prompt 6 — no text |
| `logo_softosmith.png` | ~520×180 transparent | Your **dark-text** logo (page is white) |
| `screenshot_settings.png` | ~1600px wide | Real screenshot |
| `screenshot_badge.png` | ~1600px wide | Real screenshot |

Each prompt below is self-contained — paste it as-is, save the result under the
filename in its heading. Spell-check every generated image before saving; if a word
comes out wrong, regenerate rather than shipping it.

**Logo:** use the charcoal-text Softosmith logo with the red bar, not the white
knockout version. The store description renders on a white background, so the white
version would be invisible. Keep it a transparent PNG, wide (not square) — the page
sizes it to 260px wide and lets the height follow.

---

## Prompt 1 — `banner.png` (1200×630, the store card image)

> A 1200×630 landscape marketing banner for a software plugin, flat vector
> illustration style, clean and professional SaaS aesthetic.
>
> LAYOUT: Split into two halves. The LEFT half is text on a solid light grey #F1F5F9
> background. The RIGHT half is an illustration.
>
> LEFT HALF TEXT, left-aligned, bold geometric sans-serif, generous line spacing,
> spelled exactly as written:
> - Headline, very large, dark slate #1E293B: "Google Preferred Source"
> - Subheadline below it, medium size, purple #714B67: "SEO + AI GEO for Odoo"
> - Small line below that, grey #64748B: "Website and eCommerce"
> - A small rounded pill badge at the bottom, purple #714B67 fill with white text:
>   "Odoo 19 - Free"
>
> RIGHT HALF ILLUSTRATION: a simplified white search-results panel floating on the grey
> background, showing three stacked result cards. The top card is lifted forward with a
> soft shadow and marked with a four-colour underline bar in blue #4285F4, red #EA4335,
> yellow #FBBC05, green #34A853, conveying that this result is promoted to the top. A
> small purple #714B67 rounded pill button sits beside it.
>
> Keep all text at least 60px away from the outer edges. No logos, no brand marks, no
> watermark, no extra text anywhere. Crisp edges, even lighting, no background
> gradients. Text must be perfectly spelled and clearly legible.

## Prompt 2 — `hero.png` (1200×500)

> A 1200×500 landscape flat vector infographic, three panels side by side, connected
> left to right by thin purple #714B67 arrows. Clean SaaS marketing style on a solid
> white background. Palette: purple #714B67, dark slate #1E293B, light grey #F1F5F9,
> plus Google's four accent colours blue #4285F4, red #EA4335, yellow #FBBC05,
> green #34A853 used sparingly.
>
> PANEL 1: a laptop showing a simple webpage with one rounded purple pill button
> highlighted. Caption underneath in bold dark slate sans-serif, spelled exactly:
> "1. Reader clicks the button"
>
> PANEL 2: a large circular badge with a white checkmark inside, ringed by four small
> dots in blue, red, yellow and green. Caption underneath, spelled exactly:
> "2. You become a preferred source"
>
> PANEL 3: a phone showing a search results screen where the top result card is pinned
> and lifted with a four-colour accent bar. Caption underneath, spelled exactly:
> "3. You rank higher in Google and AI Overviews"
>
> Captions are short, one line each, equal font size, perfectly spelled. No other text
> anywhere. No logos, no watermark, no shadows on the background.

## Prompt 3 — `icon.png` (256×256, app icon)

> A 256×256 square app icon, flat vector, centred composition, no text and no letters
> of any kind. A rounded-square badge filled in Odoo purple #714B67 containing a simple
> white bookmark outline with a small white star at its centre. Arcing above the badge,
> four small dots in blue #4285F4, red #EA4335, yellow #FBBC05 and green #34A853.
> Solid light grey #F1F5F9 background with 12 percent padding on all sides. Bold, high
> contrast, still legible when shrunk to 64×64. No words, no logos, no watermark.

## Prompt 4 — `feature_sdk.png` (256×256, transparent background)

> A 256×256 flat vector icon on a fully transparent background, no text and no letters.
> A rounded rectangle button outline drawn in Odoo purple #714B67, with a small
> angle-bracket code glyph to its left and three tiny dots above it in blue #4285F4,
> red #EA4335 and green #34A853. Consistent 4px stroke weight, 16 percent padding,
> minimal two-colour design. No words, no logos, no watermark, no background.

## Prompt 5 — `feature_ecommerce.png` (256×256, transparent background)

> A 256×256 flat vector icon on a fully transparent background, no text and no letters.
> A simple shopping bag outline drawn in Odoo purple #714B67, with a small rounded pill
> badge overlapping its lower-right corner accented by a single blue #4285F4 dot.
> Consistent 4px stroke weight, 16 percent padding, minimal design. No words, no logos,
> no watermark, no background.

## Prompt 6 — `feature_snippet.png` (256×256, transparent background)

> A 256×256 flat vector icon on a fully transparent background, no text and no letters.
> A dashed-outline drop-zone rectangle in grey #94A3B8, with a solid Odoo purple
> #714B67 rounded pill block being dragged into it, and a small cursor arrow beside the
> pill. Consistent 4px stroke weight, 16 percent padding, minimal design. No words,
> no logos, no watermark, no background.

---

## Do NOT generate the Google "G" logo

Even a good model reproduces the Google G subtly wrong, and a distorted trademark is a
fast way to get a listing pulled. That is exactly what `screenshot_badge.png` is for —
the real badge, photographed from your own running module. Accurate, permitted
nominative use. The trademark disclaimer is already at the bottom of `index.html`.

## The two real screenshots

Crop tight. No browser chrome, no desktop, no personal data, no customer names.
~1600px wide, saved as PNG.

**`screenshot_settings.png`** — Website ▸ Configuration ▸ Settings, scrolled to the
Google Preferred Source block, toggle switched on, mode / theme / language options all
visible.

**`screenshot_badge.png`** — switch the module to Standard JS Badge mode, open your
website front-end, and capture the real Google badge rendered on a product page or in
the footer, with a little of the surrounding page for context. This is the shot that
carries the genuine Google branding and proves the module works.
