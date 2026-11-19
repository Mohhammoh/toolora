# Third-party notices

- **pdf-lib 1.17.1** — MIT — https://github.com/Hopding/pdf-lib. License in `dist/assets/pdf-lib-LICENSE.txt`. Vendor bundle retrieved from https://cdn.jsdelivr.net/npm/pdf-lib@1.17.1/dist/pdf-lib.min.js.
- **qrcode-generator 1.4.4** — MIT — Kazuhiko Arase — https://github.com/kazuhikoarase/qrcode-generator. Copyright and license declaration retained in `dist/assets/qrcode.js`; MIT text in `dist/assets/qrcode-LICENSE.txt`. Vendor source retrieved from https://cdn.jsdelivr.net/npm/qrcode-generator@1.4.4/qrcode.js.

Both files are served from this site, with no CDN calls during use. Toolora's custom code uses browser Canvas, File, Blob, URL, Clipboard, createImageBitmap and Intl.Segmenter APIs. Test-only Playwright and jsQR were used in development; they are not runtime dependencies or included in the published site.

Additional document conversion dependencies:

- **docx-preview 0.3.6** — Apache-2.0 — https://github.com/VolodymyrBaydalka/docxjs. License retained in `dist/assets/docx-preview-LICENSE.txt`.
- **JSZip 3.10.1** — dual MIT / GPLv3; used under MIT — https://github.com/Stuk/jszip. License retained in `dist/assets/jszip-LICENSE.txt`.

Both bundles are local assets, loaded only by the isolated Word document preview. DOCX pages are rasterized with browser SVG/Canvas APIs before being embedded in a PDF with pdf-lib. No conversion API or external font service is used.
