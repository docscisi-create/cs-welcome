# موقع الترحيب بطلبة المرحلة الأولى – قسم علوم الحاسوب

إعداد **فريق الابتكار الرقمي التطوعي** – كلية العلوم – الجامعة المستنصرية.

## محتوى المجلد

| الملف | الوظيفة |
|---|---|
| `public/` | الموقع الجاهز للرفع: 8 صفحات وصفحة 404، مع ملفات CSS وJS والشعار |
| `gen.py` + `icons.json` | يبنيان صفحات `public/`. عدّل المحتوى في `gen.py` ثم شغّل `python3 gen.py` |
| `firebase.json` + `.firebaserc` | إعدادات Firebase Hosting |
| `server.js` + `package.json` + `railway.json` | خادم بسيط بلا مكتبات خارجية للتشغيل على Railway |

## صفحات الموقع

- `index.html`: الرئيسية، وفيها رسالة الترحيب وقائمة مهام الأسبوع الأول.
- `department.html`: قسم علوم الحاسوب وروابطه الرسمية.
- `college.html`: كلية العلوم والجامعة المستنصرية.
- `bologna.html`: مسار بولونيا، مع رابط نظام الجامعة.
- `cybersecurity.html`: الأمن السيبراني ومجالات العمل فيه.
- `portals.html`: البوابات المهمة، ومنها البروفايل الأكاديمي للطلبة.
- `email.html`: البريد الجامعي وطرق حمايته.
- `team.html`: فريق الابتكار الرقمي.

---

## 1) الرفع على Firebase Hosting

1. ثبّت Node.js، ثم ثبّت أدوات Firebase:
   ```bash
   npm install -g firebase-tools
   firebase login
   ```
2. أنشئ مشروعاً من [console.firebase.google.com](https://console.firebase.google.com) وانسخ **Project ID**.
3. ضع الـ Project ID بدل `YOUR-FIREBASE-PROJECT-ID` في ملف `.firebaserc`. ويمكنك بدلاً من ذلك تشغيل الأمر `firebase use --add`.
4. من داخل هذا المجلد شغّل:
   ```bash
   firebase deploy --only hosting
   ```
   يظهر الرابط بعد الرفع بهذا الشكل: `https://<project-id>.web.app`

## 2) الرفع على Railway

**الطريقة الأولى، عبر GitHub (الأسهل):**
1. ارفع هذا المجلد إلى مستودع على GitHub.
2. من [railway.com](https://railway.com) اختر **New Project ← Deploy from GitHub repo** ثم اختر المستودع.
3. يكتشف Railway أن المشروع Node.js ويشغّل الأمر `node server.js` تلقائياً.
4. من **Settings ← Networking** اضغط **Generate Domain** لتحصل على رابط عام.

**الطريقة الثانية، عبر سطر الأوامر:**
```bash
npm install -g @railway/cli
railway login
railway init
railway up
railway domain
```

## التعديل لاحقاً

- **النصوص والروابط:** عدّلها في `gen.py`، فالروابط الرسمية كلها مجمّعة في القاموس `L` أعلى الملف. بعد التعديل شغّل `python3 gen.py`، ثم أعد الرفع بالأمر `firebase deploy` أو بعمل push إلى GitHub لـ Railway.
- **الألوان:** موجودة في أعلى ملف `public/assets/css/style.css`.

## للتجربة على جهازك

```bash
node server.js
# ثم افتح http://localhost:3000
```
