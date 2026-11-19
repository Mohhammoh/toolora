# Toolora

منصة أدوات مجانية بالعربية والإنجليزية. صفحات HTML مستقلة، CSS وJavaScript، ومعالجة الملفات داخل المتصفح. لا حاجة إلى خادم خلفي أو قاعدة بيانات أو مدير حزم لتشغيل الموقع.

## ما تم تنفيذه

- ست أدوات: QR (روابط، نصوص وبطاقة اتصال)، ضغط الصور، تغيير أبعاد الصور، عدّ الكلمات، تنسيق النصوص، ودمج PDF مع تغيير الترتيب.
- 12 صفحة للأدوات + صفحتان رئيسيتان + 6 صفحات للخصوصية والشروط والتواصل.
- RTL/LTR، بحث وتصنيفات، عرض متجاوب، تعليمات وأسئلة شائعة وأدوات مرتبطة.
- المكتبات مضمنة محلياً؛ لا تُحمّل من CDN أثناء الاستخدام، ولا توجد خطوط خارجية.
- لا تحليلات أو إعلانات أو ملفات ارتباط تتبع في النسخة الحالية.
- Canonical وhreflang وخريطة الموقع تُولّد عند ضبط رابط الإنتاج الحقيقي.
- إعداد ترويسات الحماية لـ Cloudflare Pages.

## تشغيل محلي

من جذر المشروع، باستخدام Python 3.9 أو أحدث:

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8765 --directory dist
```

افتح `http://localhost:8765/ar/` أو `/en/`. لا تفتح الملفات عبر `file://` لأن مسارات الأصول تبدأ من جذر الموقع.

## نشر Cloudflare Pages وربط GitHub

1. أنشئ مستودع GitHub وارفع ملفات المشروع، بما فيها `dist` و`scripts`.
2. من Cloudflare اختر Workers & Pages ثم أنشئ مشروع Pages مع ربط المستودع.
3. إعدادات البناء: بدون إطار عمل؛ Build command: `python3 scripts/build.py`؛ Build output directory: `dist`.
4. أضف متغيرَي البيئة: `SITE_URL` = رابط الإنتاج الحقيقي بصيغة HTTPS دون مسار أو شرطة نهائية؛ `CONTACT_EMAIL` = بريد الدعم الذي تتابعه. اضبط Python 3.12 إذا لزم عبر إعدادات بيئة البناء.
5. إذا لم تعرف الرابط بعد، انشر أولاً، ثم أضف الرابط الذي أعطاك Cloudflare وأعد البناء والنشر؛ بذلك تظهر canonical وhreflang و`sitemap.xml` بالرابط الصحيح. لا تستخدم عنواناً افتراضياً أو رابط Preview في SITE_URL.
6. راجع صفحات الأدوات والتنزيل والتواصل والسياسات على رابط الإنتاج، ثم أرسل `sitemap.xml` إلى Search Console بعد إثبات ملكية الموقع.

للنشر اليدوي البديل، أعد البناء بالمتغيرات الصحيحة ثم ارفع **محتويات `dist`** (أو ملف ZIP يحتويها في الجذر) باستخدام Direct Upload. اختيار مشروع ربط Git أو Direct Upload له قيود انتقال؛ راجع وثائق Cloudflare قبل الاختيار.

```sh
SITE_URL=https://YOUR-ACTUAL-PROJECT.pages.dev CONTACT_EMAIL=YOUR-SUPPORT-EMAIL python3 scripts/build.py
SITE_URL=https://YOUR-ACTUAL-PROJECT.pages.dev python3 scripts/check.py
```

القيم أعلاه أمثلة يجب استبدالها. الحزمة مبنية بعنوان الإنتاج الموجود في site.json ودعم عام عبر GitHub Issues. لا يوجد بريد شخصي منشور.

مراجع النشر الرسمية:
- https://developers.cloudflare.com/pages/get-started/git-integration/
- https://developers.cloudflare.com/pages/get-started/direct-upload/
- https://developers.cloudflare.com/pages/configuration/build-configuration/

## الحالة قبل الإطلاق العام

نُشر الموقع على https://toolora-d0f.pages.dev باستخدام Cloudflare Pages Direct Upload. المستودع: https://github.com/Mohhammoh/toolora. لا يوجد نطاق مدفوع أو API مدفوع. إعدادات عنوان الإنتاج ورابط الدعم العام محفوظة في site.json. التحديثات لا تُنشر تلقائياً من GitHub حالياً؛ أعد البناء وارفع dist إلى مشروع Pages الحالي.

صفحة التواصل تستخدم بلاغات GitHub للدعم العام. يمكن استبدالها ببريد عبر `CONTACT_EMAIL`. نصوص السياسات تصف السلوك التقني الحالي؛ يجب أن يراجعها المالك ويضيف هويته ووسيلة تواصله وما ينطبق على تشغيله قبل الإطلاق التجاري.

GA4 وSearch Console وAdSense غير مفعّلة: تحتاج معرفات وملكية الحساب والموقع. لا تُضف GA4/AdSense قبل إعداد سياسة محدثة وموافقة مناسبة عند الحاجة؛ لإعلانات Google استخدم آلية موافقة متوافقة مع متطلباتها الحالية في البلدان المعنية. لا ترسل أسماء الملفات أو محتواها أو النصوص أو الروابط التي يكتبها المستخدم إلى التحليلات. لا توجد ضمانات لقبول الإعلانات أو الإيرادات.

## حدود الأدوات

- الصور: JPEG/PNG/WebP؛ 20 MiB للملف؛ 25 مليون بكسل؛ 10,000 بكسل لكل ضلع. الملفات الكبيرة أو غير الموثوقة قد تضغط على ذاكرة الجهاز؛ الفحص ليس برنامج مكافحة فيروسات. SVG وGIF غير مدعومتين. PNG دون فقد وقد يزيد حجمها؛ JPEG يضيف خلفية بيضاء للشفافية. الترميز يعيد بناء الصورة ولا يحتفظ عادةً ببيانات EXIF أو كامل معلومات الألوان.
- PDF: حتى 30 ملفاً، 50 MiB إجمالاً و1,000 صفحة. الملفات المشفرة أو التالفة ترفض. لا يُضمن الاحتفاظ بالتوقيعات الرقمية والنماذج والإشارات المرجعية.
- QR: ثابت، تصحيح خطأ M، هامش أبيض/خلفية بمقدار 4 وحدات؛ حد محتوى 1,400 بايت UTF-8. اختبر المسح عند تخصيص الألوان.
- الكلمات: `Intl.Segmenter` عند توفره؛ القراءة على أساس 200 كلمة/دقيقة؛ الجمل والفقرات إحصاءات تقديرية. الأحرف نقاط Unicode؛ الأسطر المفصولة بسطر فارغ تُعدّ فقرات.
- تغيير حالة الأحرف يخص اللاتينية؛ التنظيف والأسطر يعملان بالعربية والإنجليزية. حذف التكرار يعتمد التطابق الحرفي.

## الاختبارات

راجع `TEST_REPORT.md` للنتائج الفعلية. `scripts/check.py` يفحص البنية والروابط واتجاه اللغة. إجراء GitHub المرفق يكرر البناء والفحص البنيوي عند الرفع. لم يُختبر Safari أو Firefox أو هاتف حقيقي؛ يجب فحصها قبل إطلاق واسع.

## التوسع

تعريف الأدوات ومحتوى الصفحات موجودان في `scripts/build.py`. الواجهة المشتركة في `dist/assets/style.css` والمنطق في `dist/assets/app.js`. أضف تعريفاً وصفحة واجهة ومعالجاً للأداة الجديدة، ثم شغّل البناء والفحص. `dist` جزء من المصدر هنا ويحتوي الأصول اليدوية؛ لا تحذفه أثناء إعادة البناء.

المكتبات: pdf-lib 1.17.1 وqrcode-generator 1.4.4، كلاهما بترخيص MIT. راجع `THIRD_PARTY_NOTICES.md` وملفات LICENSE في الأصول. حقوق كود Toolora المخصص تبقى لمالك المشروع؛ لم يُفرض ترخيص عام على المشروع.

## PDF expansion

The site now has 11 tools: the original six plus Word (.docx) to PDF, images to PDF, PDF page extraction, page removal and rotation. The new bilingual page definitions are in `scripts/pdf_tools.py`; browser logic is in `dist/assets/pdf-tools.js`.

DOCX preview runs inside `word-frame.html`, sandboxed without same-origin access. Its scoped `_headers` policy is necessary for document styles and local assets; do not replace it with the main page policy. Conversion creates image-based PDF pages, preserving the visual preview approximately. Text is not selectable/searchable in this output. Complex Office formatting and legacy .doc are unsupported; review the preview.

New PDF operations accept up to 50 MiB and 1,000 pages. Images to PDF accepts up to 20 images, 50 MiB total, 20 MiB each, with the same 25-megapixel limits as the image tools. No new backend, paid APIs, analytics or advertising scripts were introduced.

Footer credit: Developed by Kush.
