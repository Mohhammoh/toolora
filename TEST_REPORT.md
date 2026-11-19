# Toolora validation — 19 November 2026

Status: published on Cloudflare Pages at https://toolora-d0f.pages.dev on 19 November 2026. Source repository: https://github.com/Mohhammoh/toolora. Local checks below describe the implementation before publication.

43 browser assertions passed in headless Google Chrome on macOS. No application JavaScript errors were captured. This is an MVP validation, not an exhaustive audit.

Verified:

- Search and category filtering return the expected tool cards.
- Arabic and English sample yields four words, two sentences and two paragraphs.
- Whitespace cleanup, duplicate removal and undo behave as expected.
- URL validation blocks invalid QR downloads.
- PNG QR download works. An independent jsQR decoder recovers `مرحبا Toolora` from generated image pixels. Contact vCard preview/download becomes available after entering a name.
- Two fixture PDFs with one and two pages merge to three pages. After reordering, page widths confirm the exact requested page order. Invalid PDF signature is rejected.
- Aspect ratio lock updates the second dimension. Resized PNG download is confirmed to be 240 pixels wide from the file header. Oversized dimensions are rejected.
- Arabic WebP compression results render and image results use local blob URLs.
- English and Arabic home and all six tool pages fit a 390 × 844 viewport without horizontal overflow (14 page checks).
- QR/PDF vendor libraries load on their respective pages only; home loads the shared application script only.
- During a fixture image conversion, browser request capture contains only localhost GET and blob GET requests; no external requests or POST file uploads occurred.

Additional structural checks pass for 20 localized pages: internal targets and fragment IDs exist, IDs are unique, language/direction match, vendor bundles are present. Production build configuration was exercised with a reserved test origin and test email: canonical links, hreflang, sitemap generation and contact email generation work. The delivered build intentionally omits test values.

Not verified: production HTTPS/security headers, real Cloudflare deployment, Safari/Firefox, physical mobile devices, assistive technology, malicious file resilience, all PDF form/signature variants, real-world scan performance for all QR colors, GA4, Search Console and AdSense integration. These services are not enabled.

Structural checks can be rerun with `python3 scripts/check.py`. Browser assertions used Playwright Core 1.56.1 and a locally installed Google Chrome. PDF fixture outputs were read back with pdf-lib; QR output was independently decoded with jsQR 1.4.0. Development fixtures and browser screenshots are excluded from the deliverable.

## PDF expansion and footer credit — 19 November 2026

Added five tools, bringing the total to 11, with 30 localized pages. The footer on each page now reads `Developed by Kush`.

19 additional browser assertions passed:
- Page extraction output was read back and verified to preserve requested page order.
- Out-of-range requests and removal of every page are rejected.
- Arabic page-number input works for removal.
- Rotation changes selected pages only, verified from the resulting PDF page dictionaries.
- Images produce a correctly ordered, dimensioned multi-page PDF.
- A DOCX fixture with English and Arabic text, an explicit page break and an embedded PNG exports to two PDF pages. Actual embedded PDF image content was visually reviewed. Processing requests were restricted to local assets and data/blob resources.
- Unsupported Word input is rejected.
- All five new tool pages fit a 390px viewport in both languages.

The Word renderer is isolated in a sandboxed iframe without same-origin permissions. Only that document renderer allows generated inline styles; the main site policy stays unchanged. The new renderer-specific hosting header must be checked on production.

Word conversion limitations are explicit in the UI: DOCX only, 15 MiB input, up to 30 rendered pages and 100 MiB expanded content; image-based PDF output, approximate layout and no selectable text. Legacy DOC, exact Microsoft Word fidelity and broad document corpus compatibility are not claimed. This release has been tested in Chrome; Safari/Firefox remain unverified.
