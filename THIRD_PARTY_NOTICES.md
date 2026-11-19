# Third-party notices

- **pdf-lib 1.17.1** — MIT — https://github.com/Hopding/pdf-lib. License in `dist/assets/pdf-lib-LICENSE.txt`. Vendor bundle retrieved from https://cdn.jsdelivr.net/npm/pdf-lib@1.17.1/dist/pdf-lib.min.js.
- **qrcode-generator 1.4.4** — MIT — Kazuhiko Arase — https://github.com/kazuhikoarase/qrcode-generator. Copyright and license declaration retained in `dist/assets/qrcode.js`; MIT text in `dist/assets/qrcode-LICENSE.txt`. Vendor source retrieved from https://cdn.jsdelivr.net/npm/qrcode-generator@1.4.4/qrcode.js.

Both files are served from this site, with no CDN calls during use. Toolora's custom code uses browser Canvas, File, Blob, URL, Clipboard, createImageBitmap and Intl.Segmenter APIs. Test-only Playwright and jsQR were used in development; they are not runtime dependencies or included in the published site.
