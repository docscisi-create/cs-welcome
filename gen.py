#!/usr/bin/env python3
"""Builds the static site into ./public. Edit the content here, then run:  python3 gen.py"""
import json, random, os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "public")
ICONS = json.load(open(os.path.join(ROOT, "icons.json")))
YEAR = '<span dir="ltr">2026–2027</span>'

# ---------------------------------------------------------------- official links
U = "https://uomustansiriyah.edu.iq/"
L = {
    "dept": U + "web_center.php?id_dept=156&lang=ar",
    "dept_about": U + "web_info.php?id_dept=156&lang=ar",
    "dept_msg": U + "web_info.php?id_dept=156&type=dept_message&lang=ar",
    "dept_head": U + "web_info.php?id_dept=156&type=dean_word&lang=ar&dept_type=dept_study_of_college",
    "dept_staff": U + "e-learn/show.php?id_dept=156",
    "dept_news": U + "web_archive.php?id_dept=156&t=n&lang=ar",
    "dept_ads": U + "web_archive.php?id_dept=156&t=ads&lang=ar",
    "dept_contact": U + "web_contact.php?id_dept=156&lang=ar",
    "dept_videos": U + "web_videos.php?id_dept=156",
    "dept_gallery": U + "web_galleries.php?id_dept=156",
    "bologna": "https://uomustansiriyah.bis.edu.iq/",
    "stu": U + "e-learn/stu/index.php",
    "elearn": U + "new_elearn2/index.html",
    "uni": U + "?lang=ar",
    "library": U + "web_center.php?id_dept=120&lang=ar",
    "repo": U + "e-learn/globresearch7.php",
    "aware": U + "web_page.php?page_id=3527&id_dept=221&lang=ar",
    "report": "https://req.uomustansiriyah.edu.iq/",
    "newreg": U + "web_page.php?id_dept=102&page_id=1240&lang=ar",
    "phones": U + "web_page.php?id_dept=115&page_id=1239&lang=ar",
    "wiki": "https://wiki.uomustansiriyah.edu.iq/",
    "fb": "https://www.facebook.com/AlMustansiriyahUniversity",
    "yt": "https://www.youtube.com/user/mustansiriyah",
    "ig": "https://www.instagram.com/almustansiriyah_university/",
}


def I(name, cls=""):
    return ICONS[name]


def ext(url, text, cls="btn btn-primary", icon="ExternalLink"):
    return f'<a class="{cls}" href="{url}" target="_blank" rel="noopener">{I(icon)}<span>{text}</span></a>'


def net_svg(seed=7, n=34, w=1200, h=520):
    r = random.Random(seed)
    pts = [(r.uniform(0, w), r.uniform(0, h)) for _ in range(n)]
    lines = []
    for i, (x, y) in enumerate(pts):
        near = sorted(range(n), key=lambda j: (pts[j][0] - x) ** 2 + (pts[j][1] - y) ** 2)[1:3]
        for j in near:
            lines.append(f'<line x1="{x:.0f}" y1="{y:.0f}" x2="{pts[j][0]:.0f}" y2="{pts[j][1]:.0f}"/>')
    circles = "".join(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r.choice([3, 4, 6, 9])}"/>' for x, y in pts)
    return (f'<svg class="net" viewBox="0 0 {w} {h}" preserveAspectRatio="xMidYMid slice" aria-hidden="true">'
            f'<g stroke="#BFD8FF" stroke-width="1.4">{"".join(lines)}</g><g fill="#E6F0FF">{circles}</g></svg>')


PAGES = [("index.html", "الرئيسية"), ("department.html", "القسم"), ("college.html", "الكلية والجامعة"), ("bologna.html", "مسار بولونيا"),
         ("cybersecurity.html", "الأمن السيبراني"), ("portals.html", "البوابات المهمة"), ("email.html", "البريد الجامعي"), ("team.html", "فريق الابتكار")]


def layout(fname, title, desc, body):
    nav = "".join(f'<li><a href="{f}"{" aria-current=\"page\"" if f == fname else ""}>{t}</a></li>' for f, t in PAGES)
    full_title = "مرحباً بطلبة المرحلة الأولى | قسم علوم الحاسوب – الجامعة المستنصرية" if fname == "index.html" else f"{title} | دليل طلبة المرحلة الأولى – علوم الحاسوب"
    return f"""<!doctype html>
<html lang="ar" dir="rtl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(full_title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta name="theme-color" content="#0F2E8C">
<meta property="og:title" content="{html.escape(full_title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:image" content="assets/img/logo-full.jpg">
<link rel="icon" type="image/png" href="assets/img/favicon.png">
<link rel="apple-touch-icon" href="assets/img/logo-180.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cairo:wght@600;700;800&family=Tajawal:wght@400;500;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script>document.documentElement.classList.add("js")</script>
</head>
<body>
<a class="skip" href="#main">تخطَّ إلى المحتوى</a>
<div class="official">
  <div class="container official-in">
    <a href="{L['uni']}" target="_blank" rel="noopener"><img src="assets/img/logo-uni-sm.png" alt="شعار الجامعة المستنصرية" width="40" height="40"><span>الجامعة المستنصرية</span></a>
    <i aria-hidden="true"></i>
    <a href="college.html"><img src="assets/img/logo-college-sm.png" alt="شعار كلية العلوم" width="40" height="40"><span>كلية العلوم</span></a>
    <i aria-hidden="true"></i>
    <a href="{L['dept']}" target="_blank" rel="noopener"><span>قسم علوم الحاسوب</span></a>
  </div>
</div>
<header class="site-header">
  <div class="container nav">
    <a class="brand" href="index.html">
      <img src="assets/img/logo-180.png" alt="شعار فريق الابتكار الرقمي">
      <span><b>فريق الابتكار الرقمي</b><small>قسم علوم الحاسوب · كلية العلوم</small></span>
    </a>
    <button class="menu-btn" aria-label="القائمة" aria-expanded="false" aria-controls="menu">{I("Menu")}</button>
    <ul class="menu" id="menu">{nav}</ul>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer">
  <div class="container">
    <div class="foot-grid">
      <div>
        <div class="foot-logos"><img src="assets/img/logo-uni-sm.png" alt="شعار الجامعة المستنصرية"><img src="assets/img/logo-college-sm.png" alt="شعار كلية العلوم"><img src="assets/img/logo-180.png" alt="شعار فريق الابتكار الرقمي"></div>
        <div class="foot-brand"><div><h4 style="margin:0">فريق الابتكار الرقمي التطوعي</h4><span>Digital Innovation Team</span></div></div>
        <p>دليل ترحيبي لطلبة المرحلة الأولى في قسم علوم الحاسوب – كلية العلوم – الجامعة المستنصرية، للعام الدراسي {YEAR}.</p>
      </div>
      <div>
        <h4>صفحات الدليل</h4>
        <ul>{"".join(f'<li><a href="{f}">{t}</a></li>' for f, t in PAGES[1:])}</ul>
      </div>
      <div>
        <h4>روابط رسمية</h4>
        <ul>
          <li><a href="{L['dept']}" target="_blank" rel="noopener">موقع قسم علوم الحاسوب</a></li>
          <li><a href="{L['bologna']}" target="_blank" rel="noopener">نظام مسار بولونيا</a></li>
          <li><a href="{L['stu']}" target="_blank" rel="noopener">البروفايل الأكاديمي للطلبة</a></li>
          <li><a href="{L['uni']}" target="_blank" rel="noopener">موقع الجامعة المستنصرية</a></li>
          <li><a href="{L['dept_contact']}" target="_blank" rel="noopener">اتصل بالقسم</a></li>
        </ul>
      </div>
    </div>
    <div class="copy">© <span id="year">2026</span> فريق الابتكار الرقمي التطوعي – قسم علوم الحاسوب – كلية العلوم – الجامعة المستنصرية · بغداد، شارع فلسطين</div>
  </div>
</footer>
<button class="to-top" aria-label="العودة إلى الأعلى">{I("ArrowUp")}</button>
<script src="assets/js/main.js" defer></script>
</body>
</html>
"""


def page_hero(title, sub, crumb, seed):
    return f"""<section class="page-hero">{net_svg(seed, 26, 1200, 300)}
  <div class="container">
    <div class="crumbs"><a href="index.html">الرئيسية</a> / {crumb}</div>
    <h1>{title}</h1>
    <p>{sub}</p>
  </div>
</section>"""


def card(icon, title, text, tone="", extra=""):
    return f'<div class="card reveal"><div class="ico {tone}">{I(icon)}</div><h3>{title}</h3><p>{text}</p>{extra}</div>'


def link_card(href, icon, title, text, tone="", more="اقرأ المزيد", external=False):
    tgt = ' target="_blank" rel="noopener"' if external else ""
    return (f'<a class="card link-card reveal" href="{href}"{tgt}><div class="ico {tone}">{I(icon)}</div><h3>{title}</h3><p>{text}</p>'
            f'<span class="more">{more} {I("ExternalLink" if external else "ArrowLeft")}</span></a>')


def callout(icon, text, kind=""):
    return f'<div class="callout {kind} reveal">{I(icon)}<div>{text}</div></div>'


def head(kicker, title, sub=""):
    return f'<div class="section-head reveal"><span class="kicker">{kicker}</span><h2>{title}</h2>{f"<p>{sub}</p>" if sub else ""}</div>'


# ================================================================ HOME
home = f"""
<section class="hero">{net_svg(3)}
  <div class="container hero-inner">
    <div>
      <span class="eyebrow">{I("Sparkles")} العام الدراسي {YEAR}</span>
      <h1>أهلاً وسهلاً بطلبة المرحلة الأولى</h1>
      <p class="lead">في <b>قسم علوم الحاسوب</b> – كلية العلوم – الجامعة المستنصرية. هذا دليلك الأول لبداية رحلتك الجامعية: تعرّف على قسمك وكليتك، ونظام مسار بولونيا، وبريدك الجامعي، والبوابات الإلكترونية المهمة، وعالم الأمن السيبراني.</p>
      <div class="btns">
        <a class="btn btn-light" href="#start">{I("Rocket")}<span>ابدأ من هنا</span></a>
        <a class="btn btn-ghost" href="department.html">{I("Building2")}<span>تعرّف على القسم</span></a>
      </div>
      <div class="hero-badges">
        <div><img src="assets/img/logo-uni-sm.png" alt="شعار الجامعة المستنصرية" width="60" height="60"><span>الجامعة المستنصرية</span></div>
        <div><img src="assets/img/logo-college-sm.png" alt="شعار كلية العلوم" width="60" height="60"><span>كلية العلوم</span></div>
        <div><img src="assets/img/logo-180.png" alt="شعار فريق الابتكار الرقمي" width="60" height="60"><span>فريق الابتكار الرقمي</span></div>
      </div>
    </div>
    <div class="hero-logo"><img src="assets/img/logo-full.jpg" alt="شعار فريق الابتكار الرقمي – قسم علوم الحاسوب – الجامعة المستنصرية" width="480" height="480"></div>
  </div>
</section>

<section class="block">
  <div class="container grid g2" style="align-items:center">
    <div class="reveal">
      <span class="kicker">رسالة ترحيب</span>
      <h2>مرحباً بكم في عائلة علوم الحاسوب</h2>
      <p>عزيزتي الطالبة، عزيزي الطالب: يسعدنا أن نرحّب بكم في أول خطوة من مسيرتكم الجامعية. السنة الأولى مليئة بالأشياء الجديدة: نظام دراسي جديد، ومنصات إلكترونية، وزملاء وأساتذة جدد. لذلك أعدّ <b>فريق الابتكار الرقمي التطوعي</b> هذا الدليل ليجيب عن أسئلتكم الأولى في مكان واحد.</p>
      <p>تصفّحوا الصفحات بالترتيب، وأكملوا قائمة «خطواتك في الأسبوع الأول»، ولا تترددوا في سؤال أساتذتكم وزملائكم في المراحل المتقدمة. نتمنى لكم سنة دراسية موفقة ومليئة بالإبداع.</p>
      <p class="muted">— فريق الابتكار الرقمي التطوعي، قسم علوم الحاسوب</p>
      <p class="muted" style="margin:0">بإشراف: <b>الأستاذ الدكتور ميثاق طالب كاطع</b> عميد كلية العلوم، و<b>الأستاذ الدكتور ذكرى حيدر علي عباس</b> رئيسة قسم علوم الحاسوب.</p>
    </div>
    <div class="grid g2">
      <div class="stat reveal"><b>4</b><span>سنوات لدرجة البكالوريوس</span></div>
      <div class="stat reveal"><b>60</b><span>وحدة ECTS في السنة</span></div>
      <div class="stat reveal"><b>2</b><span>فصلان: خريفي وربيعي</span></div>
      <div class="stat reveal"><b>1963</b><span>تأسيس الجامعة الحديثة</span></div>
    </div>
  </div>
</section>

<section class="block alt" id="start">
  <div class="container">
    {head("محتويات الدليل", "ماذا تجد في هذا الموقع؟", "سبع صفحات قصيرة تغطي أهم ما يحتاجه طالب المرحلة الأولى.")}
    <div class="grid g4">
      {link_card("department.html", "Building2", "قسم علوم الحاسوب", "ماذا ستدرس، ومسارك خلال أربع سنوات، وروابط القسم الرسمية.")}
      {link_card("college.html", "FlaskConical", "كلية العلوم والجامعة", "تاريخ الجامعة المستنصرية وأقسام كلية العلوم.", "v")}
      {link_card("bologna.html", "GraduationCap", "مسار بولونيا", "الوحدات ECTS، والتقييم، والنجاح، والغياب — بشكل مبسّط.", "m")}
      {link_card("cybersecurity.html", "ShieldCheck", "الأمن السيبراني", "ما هو، ولماذا هو مهم، ومجالات العمل فيه.", "r")}
      {link_card("portals.html", "Link", "البوابات المهمة", "البروفايل الأكاديمي، والتعليم الإلكتروني، والمكتبة وغيرها.", "a")}
      {link_card("email.html", "Mail", "البريد الجامعي", "أهميته، وكيف تحصل عليه، وكيف تحميه من الاختراق.")}
      {link_card("team.html", "HeartHandshake", "فريق الابتكار الرقمي", "من نحن، وأعضاء الفريق الذين أعدّوا هذا الدليل.", "v")}
      {link_card(L["dept"], "Globe", "موقع القسم الرسمي", "الأخبار والتعاميم والبروفايلات الأكاديمية للتدريسيين.", "m", "زيارة الموقع", True)}
    </div>
  </div>
</section>

<section class="block">
  <div class="container grid g2">
    <div class="reveal">
      <span class="kicker">قائمة مهام تفاعلية</span>
      <h2>خطواتك في الأسبوع الأول</h2>
      <p class="muted">ضع علامة على كل خطوة تنجزها. تُحفظ علاماتك في متصفحك فقط.</p>
      <div class="progress" aria-hidden="true"><i></i></div>
      <p><b>أنجزت: <span id="todo-count">0 من 6</span></b></p>
      {callout("Info", "ابدأ بالبريد الجامعي والبروفايل الأكاديمي: معظم المنصات الأخرى تعتمد عليهما.")}
    </div>
    <div class="todo reveal">
      <label><input type="checkbox" id="t1"><span>احصل على بريدك الجامعي وفعّل التحقق بخطوتين</span><a href="email.html">الشرح</a></label>
      <label><input type="checkbox" id="t2"><span>ادخل إلى البروفايل الأكاديمي للطلبة وتأكد من بياناتك</span><a href="{L['stu']}" target="_blank" rel="noopener">البوابة</a></label>
      <label><input type="checkbox" id="t3"><span>اقرأ أساسيات مسار بولونيا (الوحدات والتقييم والغياب)</span><a href="bologna.html">الشرح</a></label>
      <label><input type="checkbox" id="t4"><span>ادخل إلى نظام مسار بولونيا وتعرّف على مقرراتك</span><a href="{L['bologna']}" target="_blank" rel="noopener">النظام</a></label>
      <label><input type="checkbox" id="t5"><span>انضم إلى صفوف موادك الإلكترونية واحفظ الجدول الأسبوعي</span><a href="portals.html">البوابات</a></label>
      <label><input type="checkbox" id="t6"><span>تابع أخبار القسم وتعاميمه على موقعه الرسمي</span><a href="{L['dept_ads']}" target="_blank" rel="noopener">التعاميم</a></label>
    </div>
  </div>
</section>

<section class="block alt">
  <div class="container">
    {head("نصائح سريعة", "كيف تنجح في سنتك الأولى؟")}
    <div class="grid g4">
      {card("Clock", "احضر وتابع أولاً بأول", "الغياب محسوب بنسب واضحة في مسار بولونيا، والتقييم المستمر يشكّل 40% من درجة المادة.")}
      {card("Code", "برمج كل يوم", "البرمجة مهارة تُكتسب بالتمرين. حلّ تمريناً صغيراً يومياً بدل التحضير ليلة الامتحان.", "v")}
      {card("Users", "اصنع مجموعة دراسة", "ادرس مع زملائك، واسأل طلبة المراحل المتقدمة؛ التعلم الجماعي أسرع وأمتع.", "m")}
      {card("ShieldCheck", "احمِ حساباتك", "كلمة مرور قوية لكل حساب، ولا تشارك بيانات دخولك مع أي شخص مهما كان.", "r")}
    </div>
  </div>
</section>
"""

# ================================================================ DEPARTMENT
department = page_hero("قسم علوم الحاسوب", "قسم علمي في كلية العلوم بالجامعة المستنصرية، يُعِدّ متخصصين في البرمجة والخوارزميات والشبكات وقواعد البيانات والذكاء الاصطناعي وأمن المعلومات.", "القسم", 11) + f"""
<section class="block">
  <div class="container grid g2" style="align-items:start">
    <div class="reveal">
      <span class="kicker">تعريف بالقسم</span>
      <p><span class="tag">رئيسة القسم</span> <b>الأستاذ الدكتور ذكرى حيدر علي عباس</b></p>
      <h2>ماذا يعني أن تدرس علوم الحاسوب؟</h2>
      <p>علوم الحاسوب هي دراسة كيفية تمثيل المعلومات ومعالجتها باستخدام الحاسوب: كيف نصمّم الخوارزميات، ونكتب البرامج، ونبني قواعد البيانات والشبكات، ونحمي الأنظمة، ونجعل الحواسيب «تتعلّم» من البيانات.</p>
      <p>يمنح القسم شهادة <b>البكالوريوس في علوم الحاسوب</b> بعد أربع سنوات دراسية، وتجمع الدراسة بين المحاضرات النظرية والمختبرات العملية ومشروع التخرج في السنة الرابعة.</p>
      <div class="btns">
        {ext(L["dept"], "موقع القسم الرسمي")}
        {ext(L["dept_msg"], "الرؤية والرسالة والأهداف", "btn btn-outline", "Target")}
      </div>
    </div>
    <div class="card reveal">
      <h3>المهارات التي ستكتسبها</h3>
      <ul class="check">
        <li>التفكير المنطقي وحل المشكلات بالخوارزميات</li>
        <li>البرمجة بلغات متعددة وبناء التطبيقات</li>
        <li>تصميم قواعد البيانات وإدارتها</li>
        <li>فهم الشبكات وأنظمة التشغيل والأمن</li>
        <li>أساسيات الذكاء الاصطناعي وتحليل البيانات</li>
        <li>العمل الجماعي وإدارة المشاريع البرمجية</li>
      </ul>
    </div>
  </div>
</section>

<section class="block alt">
  <div class="container">
    {head("رحلتك الدراسية", "مسارك خلال أربع سنوات", "صورة عامة مبسّطة؛ الخطة الدراسية الرسمية والمقررات المعتمدة تعلنها إدارة القسم.")}
    <div class="timeline">
      <div class="t card reveal"><span class="tag">المرحلة الأولى</span><h3>الأساسيات</h3><p>مبادئ البرمجة، والرياضيات للحاسوب (التراكيب المتقطعة)، وأساسيات علوم الحاسوب وتصميم المنطق، إضافة إلى متطلبات الجامعة مثل اللغة الإنجليزية.</p></div>
      <div class="t card reveal"><span class="tag">المرحلة الثانية</span><h3>البناء</h3><p>هياكل البيانات، والبرمجة الكيانية، وقواعد البيانات، ومعمارية الحاسوب، والخوارزميات.</p></div>
      <div class="t card reveal"><span class="tag">المرحلة الثالثة</span><h3>الأنظمة</h3><p>أنظمة التشغيل، وشبكات الحاسوب، وهندسة البرمجيات، والذكاء الاصطناعي، والرسوم والوسائط المتعددة.</p></div>
      <div class="t card reveal"><span class="tag">المرحلة الرابعة</span><h3>التخصص والتخرج</h3><p>أمن المعلومات، والحوسبة المتقدمة، ومواد اختيارية متخصصة، و<b>مشروع التخرج</b> الذي تطبّق فيه كل ما تعلّمته.</p></div>
    </div>
    {callout("Info", "أسماء المواد أعلاه أمثلة شائعة في أقسام علوم الحاسوب؛ اعتمد دائماً على الخطة الدراسية المعلنة من القسم وعلى نظام مسار بولونيا لمعرفة مقرراتك ووحداتها.")}
  </div>
</section>

<section class="block">
  <div class="container">
    {head("روابط القسم الرسمية", "كل ما يخص القسم في مكان واحد", "روابط مباشرة إلى صفحات القسم على موقع الجامعة المستنصرية.")}
    <div class="grid g4">
      {link_card(L["dept"], "Globe", "الصفحة الرئيسية للقسم", "بوابة القسم على موقع الجامعة.", "", "زيارة", True)}
      {link_card(L["dept_about"], "BookOpen", "نبذة عن القسم", "تعريف رسمي بالقسم وتاريخه.", "v", "زيارة", True)}
      {link_card(L["dept_msg"], "Target", "الرسالة والرؤية والأهداف", "توجهات القسم وأهدافه المعلنة.", "m", "زيارة", True)}
      {link_card(L["dept_head"], "User", "كلمة رئيس القسم", "رسالة رئاسة القسم إلى الطلبة.", "a", "زيارة", True)}
      {link_card(L["dept_staff"], "Users", "البروفايل الأكاديمي للتدريسيين", "تعرّف على أساتذتك واختصاصاتهم وبحوثهم.", "", "زيارة", True)}
      {link_card(L["dept_ads"], "Megaphone", "التعاميم", "الجداول والإعلانات والتوجيهات الرسمية.", "r", "زيارة", True)}
      {link_card(L["dept_news"], "Newspaper", "أخبار القسم", "النشاطات والورش والمؤتمرات.", "v", "زيارة", True)}
      {link_card(L["dept_contact"], "Phone", "اتصل بالقسم", "العنوان: بغداد – شارع فلسطين، ص.ب 14022.", "m", "زيارة", True)}
    </div>
  </div>
</section>

<section class="block alt">
  <div class="container">
    {head("بعد التخرج", "أين يعمل خريج علوم الحاسوب؟")}
    <div class="grid g4">
      {card("Code", "تطوير البرمجيات", "تطبيقات الويب والهاتف وأنظمة المؤسسات.")}
      {card("Database", "البيانات والذكاء الاصطناعي", "تحليل البيانات، وتعلّم الآلة، وأنظمة التوصية.", "v")}
      {card("ShieldCheck", "الأمن السيبراني", "حماية الشبكات والأنظمة والتحقيق الرقمي.", "r")}
      {card("Network", "الشبكات والحوسبة السحابية", "تصميم البنى التحتية وإدارتها في المؤسسات.", "m")}
      {card("Microscope", "البحث العلمي والدراسات العليا", "الماجستير والدكتوراه والعمل الأكاديمي.", "a")}
      {card("Briefcase", "ريادة الأعمال", "تأسيس شركات ناشئة وحلول رقمية محلية.")}
      {card("Monitor", "دعم الأنظمة وإدارتها", "تشغيل الأنظمة الحكومية والمصرفية والصحية.", "v")}
      {card("Award", "التعليم والتدريب", "تدريس الحاسوب وتقديم الدورات المهنية.", "m")}
    </div>
  </div>
</section>
"""

# ================================================================ COLLEGE
college = page_hero("كلية العلوم والجامعة المستنصرية", "تعرّف على الجامعة العريقة التي تنتمي إليها، وعلى كلية العلوم وأقسامها العلمية.", "الكلية والجامعة", 21) + f"""
<section class="block">
  <div class="container">
    <div class="stats">
      <div class="stat reveal"><b>1227م</b><span>تأسيس المدرسة المستنصرية في العهد العباسي</span></div>
      <div class="stat reveal"><b>1963م</b><span>تأسيس الجامعة المستنصرية الحديثة</span></div>
      <div class="stat reveal"><b>8</b><span>أقسام علمية في كلية العلوم</span></div>
      <div class="stat reveal"><b>بغداد</b><span>شارع فلسطين</span></div>
    </div>
  </div>
</section>

<section class="block alt">
  <div class="container grid g2" style="align-items:start">
    <div class="reveal">
      <img class="sec-logo" src="assets/img/logo-uni.png" alt="شعار الجامعة المستنصرية" width="150" height="150">
      <span class="kicker">الجامعة المستنصرية</span>
      <h2>جامعة بجذور تمتد ثمانية قرون</h2>
      <p>تحمل الجامعة اسم <b>المدرسة المستنصرية</b> التي أنشأها الخليفة العباسي <b>المستنصر بالله</b> في بغداد سنة 1227م (اكتمل بناؤها نحو 1233م)، وكانت من أقدم الجامعات في العالم، تُدرَّس فيها علوم الدين واللغة والطب والرياضيات والفلك.</p>
      <p>أما الجامعة المستنصرية الحديثة فقد تأسست عام <b>1963م</b>، وتضم اليوم كليات متعددة، منها: الطب، وطب الأسنان، والصيدلة، والهندسة، والعلوم، والقانون، والآداب، والتربية، والإدارة والاقتصاد، والعلوم السياسية، والتربية الأساسية، والتربية البدنية، والعلوم السياحية، والتمريض.</p>
      <div class="btns">{ext(L["uni"], "موقع الجامعة المستنصرية")}{ext(L["wiki"], "موسوعة الجامعة", "btn btn-outline", "BookOpen")}</div>
    </div>
    <div class="reveal">
      <img class="sec-logo" src="assets/img/logo-college.png" alt="شعار كلية العلوم – الجامعة المستنصرية" width="150" height="150">
      <span class="kicker">كلية العلوم</span>
      <h2>كلية العلوم</h2>
      <p><span class="tag">عميد الكلية</span> <b>الأستاذ الدكتور ميثاق طالب كاطع</b></p>
      <p>كلية العلوم من الكليات العلمية العريقة في الجامعة، وتعود بداياتها إلى السنوات الأولى للجامعة الحديثة؛ فقسم الرياضيات مثلاً تأسس عام 1963 ضمن الكلية. تهتم الكلية بالعلوم الأساسية والتطبيقية، وتجمع بين الدراسة النظرية والمختبرات والبحث العلمي، وتقدّم الدراسات الأولية والعليا.</p>
      {callout("Lightbulb", "دراستك في كلية العلوم تعني أن الرياضيات والتفكير العلمي جزء أساسي من تكوينك كعالم حاسوب — وهذا ما يميّز خريج «علوم» الحاسوب.", "ok")}
    </div>
  </div>
</section>

<section class="block">
  <div class="container">
    {head("أقسام الكلية", "الأقسام العلمية الثمانية في كلية العلوم")}
    <div class="grid g4">
      {card("Code", "قسم علوم الحاسوب", "قسمك! البرمجة والخوارزميات والشبكات والذكاء الاصطناعي والأمن.", "", '<a class="more" href="department.html">صفحة القسم ' + I("ArrowLeft") + '</a>')}
      {card("Sigma", "قسم الرياضيات", "الرياضيات البحتة والتطبيقية والإحصاء وبحوث العمليات.", "v")}
      {card("Atom", "قسم الفيزياء", "الفيزياء النظرية والتطبيقية والإلكترونيات والليزر.", "a")}
      {card("FlaskConical", "قسم الكيمياء", "الكيمياء العضوية واللاعضوية والتحليلية والحياتية.", "m")}
      {card("Dna", "قسم علوم الحياة", "علم الحيوان والنبات والتقانة الحياتية والوراثة.", "r")}
      {card("CloudSun", "قسم علوم الجو", "الأرصاد الجوية والمناخ والتنبؤ بالطقس.")}
      {card("Microscope", "قسم الأحياء المجهرية", "البكتيريا والفطريات والفيروسات والمناعة.", "m")}
      {card("BrainCircuit", "قسم الذكاء الاصطناعي", "تعلّم الآلة والتعلّم العميق ومعالجة البيانات والرؤية الحاسوبية.", "v")}
    </div>
  </div>
</section>

<section class="block alt">
  <div class="container">
    {head("خدمات للطلبة", "مرافق وخدمات جامعية تفيدك")}
    <div class="grid g4">
      {link_card(L["library"], "Library", "المكتبة المركزية", "كتب ومراجع وقاعات مطالعة.", "", "زيارة", True)}
      {link_card(L["repo"], "Database", "المستودع الرقمي", "بحوث ورسائل وأطاريح منشورة.", "v", "زيارة", True)}
      {link_card(L["aware"], "Lightbulb", "إرشادات توعوية", "توجيهات رسمية للطلبة.", "a", "زيارة", True)}
      {link_card(L["phones"], "Phone", "الهواتف الداخلية", "أرقام التواصل مع تشكيلات الجامعة.", "m", "زيارة", True)}
    </div>
  </div>
</section>
"""

# ================================================================ BOLOGNA
GR = [("A", "امتياز", "Excellent", "90 – 100", "#12A387"), ("B", "جيد جداً", "Very Good", "80 – 89", "#2F9E5B"), ("C", "جيد", "Good", "70 – 79", "#2F7BEA"),
      ("D", "متوسط", "Satisfactory", "60 – 69", "#7B5CE6"), ("E", "مقبول", "Sufficient", "50 – 59", "#E39B23"),
      ("FX", "راسب (قيد المعالجة)", "Fail", "45 – 49", "#E3742B"), ("F", "راسب", "Fail", "0 – 44", "#D6455D")]
grade_rows = "".join(f'<tr><td><span class="grade" style="background:{c}">{g}</span></td><td>{a}</td><td>{e}</td><td dir="ltr" style="text-align:right">{r}</td></tr>' for g, a, e, r, c in GR)
bologna = page_hero("نظام مسار بولونيا", "النظام الدراسي الذي تدرس وفقه: وحدات ECTS، والفصول الدراسية، والتقييم المستمر، وشروط النجاح والحضور — بشرح مبسّط.", "مسار بولونيا", 31) + f"""
<section class="block">
  <div class="container grid g2" style="align-items:center">
    <div class="reveal">
      <span class="kicker">ما هو مسار بولونيا؟</span>
      <h2>نظام دراسي معترف به دولياً</h2>
      <p>انطلقت «عملية بولونيا» بإعلان وقّعته الدول الأوروبية في مدينة بولونيا الإيطالية عام 1999، لتوحيد أنظمة التعليم العالي وجعل الشهادات قابلة للمقارنة والاعتراف بين الدول. واعتمدت وزارة التعليم العالي والبحث العلمي في العراق تطبيق <b>مسار بولونيا</b> في الجامعات العراقية، ويدرس طلبة المرحلة الأولى وفقه.</p>
      <p>الفكرة الأساسية: كل مادة لها «وزن» يُقاس بـ<b>وحدات ECTS</b> بحسب الجهد الكامل الذي تبذله فيها — داخل القاعة وخارجها — وليس بعدد ساعات المحاضرة فقط.</p>
      <div class="btns">{ext(L["bologna"], "الدخول إلى نظام مسار بولونيا – الجامعة المستنصرية")}</div>
    </div>
    <div class="grid g2">
      <div class="stat reveal"><b>25</b><span>ساعة جهد = وحدة ECTS واحدة</span></div>
      <div class="stat reveal"><b>30</b><span>وحدة في الفصل الدراسي</span></div>
      <div class="stat reveal"><b>60</b><span>وحدة في السنة الدراسية</span></div>
      <div class="stat reveal"><b>50</b><span>درجة النجاح الصغرى في المادة</span></div>
    </div>
  </div>
</section>

<section class="block alt">
  <div class="container">
    {head("المفاهيم الأساسية", "ما تحتاج معرفته من اليوم الأول")}
    <div class="grid g3">
      {card("Layers", "وحدات ECTS", "النظام الأوروبي لتجميع الوحدات ونقلها. الوحدة الواحدة تعادل نحو 25 ساعة من جهد الطالب، ولا يتجاوز مجموع وحدات الفصل 30 وحدة، أي 60 وحدة في السنة.")}
      {card("Clock", "العبء الدراسي SWL", "مجموع الوقت الذي تحتاجه لتحقيق مخرجات التعلم: المحاضرات والمختبرات (ساعات منتظمة) والدراسة الذاتية والواجبات والتحضير (ساعات غير منتظمة).", "v")}
      {card("CalendarDays", "فصلان دراسيان", "تُقسَّم السنة إلى فصل خريفي وفصل ربيعي، ولكل فصل مواده وامتحاناته ونتائجه ومعدله.", "m")}
      {card("ClipboardCheck", "التقييم التكويني 40%", "تقييم مستمر طوال الفصل: اختبارات قصيرة، وتقارير، وواجبات، ومشاريع، ومشاركة، وأعمال مختبر.", "a")}
      {card("FileText", "التقييم التلخيصي 60%", "امتحان نصف الفصل (10%) والامتحان النهائي (50%). المشاركة في الامتحان النهائي شرط للنجاح.", "r")}
      {card("Award", "ملحق الشهادة", "وثيقة تُمنح للخريج مع الشهادة توضح البرنامج ومخرجات التعلم والمواد ووحداتها والدرجات والمعدل التراكمي، فتسهّل الاعتراف بشهادتك خارج العراق.")}
    </div>
  </div>
</section>

<section class="block">
  <div class="container grid g2" style="align-items:start">
    <div class="reveal">
      {head("سلّم التقديرات", "كيف تُقرأ درجتك؟")}
      <div class="table-wrap"><table>
        <thead><tr><th>الرمز</th><th>التقدير</th><th>English</th><th>الدرجة</th></tr></thead>
        <tbody>{grade_rows}</tbody>
      </table></div>
      <p class="muted" style="margin-top:12px">FX تعني أن الطالب قريب من النجاح ويحتاج إلى عمل إضافي محدود لاجتياز المادة.</p>
    </div>
    <div class="reveal">
      {head("مثال محلول", "كيف يُحسب معدل الفصل؟", "يُضرب درجة كل مادة في عدد وحداتها، ثم يُقسم المجموع على مجموع الوحدات.")}
      <div class="table-wrap"><table>
        <thead><tr><th>المادة (مثال)</th><th>الوحدات</th><th>الدرجة</th><th>الوحدات × الدرجة</th></tr></thead>
        <tbody>
          <tr><td>مبادئ البرمجة</td><td>8</td><td>85</td><td>680</td></tr>
          <tr><td>رياضيات الحاسوب</td><td>6</td><td>72</td><td>432</td></tr>
          <tr><td>اللغة الإنجليزية</td><td>2</td><td>90</td><td>180</td></tr>
          <tr><td><b>المجموع</b></td><td><b>16</b></td><td></td><td><b>1292</b></td></tr>
        </tbody>
      </table></div>
      {callout("Sigma", "المعدل = 1292 ÷ 16 = <b>80.75</b> ← تقدير «جيد جداً». لاحظ أن المادة ذات الوحدات الأكثر (البرمجة) تؤثر في المعدل أكثر من غيرها.", "ok")}
    </div>
  </div>
</section>

<section class="block alt">
  <div class="container">
    {head("الحضور والامتحانات", "قواعد مهمة لا تتجاهلها")}
    <div class="grid g3">
      {card("TriangleAlert", "إنذار أول عند 7%", "غياب بنسبة 7% من ساعات المادة (نحو أسبوع دراسي) يعني إنذاراً تحريرياً وإلكترونياً.", "a")}
      {card("Siren", "إنذار نهائي عند 14%", "غياب 14% (نحو أسبوعين) دون عذر رسمي يعني إنذاراً نهائياً. ويجوز لمجلس الكلية رفع الحد إلى 21% بعذر مقبول، وتجاوزه يعني الرسوب بالغياب.", "r")}
      {card("RefreshCw", "محاولات الامتحان", "محاولتان امتحانيتان في كل فصل، و4 محاولات كحد أعلى للمادة الواحدة؛ والطالب الراسب يعيد المادة دواماً وامتحاناً في فصل لاحق.", "")}
    </div>
    {callout("Info", "هذه القواعد ملخّصة من التعليمات العامة لمسار بولونيا في الجامعات العراقية. قد تصدر تعليمات أو تعديلات خاصة بالجامعة أو الكلية، لذا تابع دائماً <a href='" + L['dept_ads'] + "' target='_blank' rel='noopener'>تعاميم القسم</a> ونظام مسار بولونيا الخاص بالجامعة.")}
  </div>
</section>

<section class="block">
  <div class="container">
    {head("لماذا بولونيا؟", "فوائد النظام لك")}
    <div class="grid g4">
      {card("Globe", "اعتراف دولي", "شهادة قابلة للمقارنة مع جامعات الدول التي تعتمد النظام.")}
      {card("Rocket", "تنقّل أسهل", "إمكانية أكبر للانتقال والدراسات العليا والمنح خارج العراق.", "v")}
      {card("Target", "تعلّم متمحور حولك", "مخرجات تعلم واضحة لكل مادة، وتقييم مستمر لا يعتمد على امتحان واحد.", "m")}
      {card("Briefcase", "قرب من سوق العمل", "تركيز على المهارات العملية التي يطلبها أصحاب العمل.", "a")}
    </div>
  </div>
</section>
"""

# ================================================================ CYBERSECURITY
cyber = page_hero("الأمن السيبراني", "ما هو الأمن السيبراني، ولماذا أصبح من أهم تخصصات الحاسوب اليوم، وما مجالات العمل فيه؟", "الأمن السيبراني", 41) + f"""
<section class="block">
  <div class="container grid g2" style="align-items:center">
    <div class="reveal">
      <span class="kicker">التعريف</span>
      <h2>ما هو الأمن السيبراني؟</h2>
      <p><b>الأمن السيبراني</b> هو مجموعة الوسائل التقنية والإدارية والبشرية التي تحمي الأنظمة والشبكات والبرامج والبيانات من الهجمات الرقمية والوصول غير المصرّح به والتلف.</p>
      <p>كل شيء اليوم متصل بالإنترنت: حساباتك الجامعية، والمصارف، والمستشفيات، ومحطات الكهرباء. لذلك أصبح حماية هذا العالم الرقمي ضرورة لكل فرد ومؤسسة ودولة.</p>
    </div>
    <div class="grid g3">
      <div class="card reveal" style="text-align:center"><div class="ico" style="margin-inline:auto">{I("Lock")}</div><h3>السرية</h3><p class="muted">Confidentiality: لا يطّلع على المعلومة إلا المخوَّل.</p></div>
      <div class="card reveal" style="text-align:center"><div class="ico v" style="margin-inline:auto">{I("BadgeCheck")}</div><h3>السلامة</h3><p class="muted">Integrity: المعلومة لم تُعدَّل دون إذن.</p></div>
      <div class="card reveal" style="text-align:center"><div class="ico m" style="margin-inline:auto">{I("Server")}</div><h3>التوافر</h3><p class="muted">Availability: النظام متاح عندما نحتاجه.</p></div>
    </div>
  </div>
</section>

<section class="block alt">
  <div class="container">
    {head("الأهمية", "لماذا الأمن السيبراني مهم؟")}
    <div class="grid g4">
      {card("User", "لك شخصياً", "حماية حساباتك وصورك ومعلوماتك المالية وسمعتك من السرقة والابتزاز.")}
      {card("Building2", "للمؤسسات", "استمرار عمل الجامعات والمصارف والشركات وحماية بيانات عملائها.", "v")}
      {card("Globe", "للدولة", "حماية البنى التحتية الحيوية: الكهرباء والاتصالات والصحة والحكومة الإلكترونية.", "m")}
      {card("Briefcase", "لمستقبلك المهني", "الطلب على المتخصصين أكبر من عددهم عالمياً، ما يجعله مجالاً واعداً للعمل.", "a")}
    </div>
  </div>
</section>

<section class="block">
  <div class="container">
    {head("التهديدات الشائعة", "ممّا نحمي أنفسنا؟")}
    <div class="grid g3">
      {card("Mail", "التصيّد الاحتيالي Phishing", "رسائل أو روابط مزيفة تطلب كلمة مرورك أو بياناتك متظاهرةً بأنها جهة موثوقة.", "r")}
      {card("Bug", "البرمجيات الخبيثة Malware", "فيروسات وأحصنة طروادة وبرامج تجسس تُثبَّت من ملفات أو تطبيقات غير موثوقة.", "r")}
      {card("LockKeyhole", "برامج الفدية Ransomware", "تشفّر ملفات الضحية وتطلب مالاً لإعادتها.", "r")}
      {card("Users", "الهندسة الاجتماعية", "خداع الأشخاص نفسياً لكشف معلومات أو تنفيذ أفعال، مثل انتحال صفة صديق أو موظف.", "a")}
      {card("KeyRound", "كلمات المرور الضعيفة", "تكرار كلمة المرور نفسها أو سهولة تخمينها يفتح الباب لاختراق جميع حساباتك.", "a")}
      {card("Wifi", "الشبكات العامة غير الآمنة", "شبكات الواي فاي المفتوحة قد يراقبها مهاجم لالتقاط بياناتك.", "a")}
    </div>
  </div>
</section>

<section class="block alt">
  <div class="container">
    {head("مجالات العمل", "ماذا يمكن أن تعمل في الأمن السيبراني؟", "بعض أهم المسارات المهنية التي يمكن لخريج علوم الحاسوب التخصص فيها.")}
    <div class="grid g4">
      {card("Eye", "محلل مركز العمليات الأمنية SOC", "يراقب الشبكات على مدار الساعة ويكتشف الهجمات ويستجيب لها.")}
      {card("Terminal", "مختبر الاختراق الأخلاقي", "يهاجم الأنظمة بإذن رسمي ليكتشف الثغرات قبل المهاجمين.", "r")}
      {card("Server", "مهندس أمن الشبكات", "يصمّم الجدران النارية وأنظمة كشف التسلل ويؤمّن البنى التحتية.", "v")}
      {card("Search", "التحقيق الجنائي الرقمي", "يجمع الأدلة الرقمية ويحللها بعد الحوادث والجرائم الإلكترونية.", "a")}
      {card("Code", "أمن التطبيقات والبرمجيات", "يراجع الشيفرات ويضمن تطوير برامج آمنة من البداية.", "m")}
      {card("Cloud", "أمن الحوسبة السحابية", "يحمي الخدمات والبيانات المخزّنة في السحابة.")}
      {card("ShieldAlert", "الاستجابة للحوادث", "يقود فريق احتواء الهجوم وإعادة الأنظمة إلى العمل.", "r")}
      {card("Gavel", "الحوكمة والامتثال وإدارة المخاطر", "يضع السياسات الأمنية ويقيس المخاطر ويتابع الالتزام بالمعايير.", "v")}
    </div>
  </div>
</section>

<section class="block">
  <div class="container grid g2" style="align-items:start">
    <div class="reveal">
      {head("خارطة طريق", "كيف تبدأ وأنت في المرحلة الأولى؟")}
      <ol class="steps">
        <li><b>أتقن الأساسيات</b>البرمجة (Python وC++)، وأنظمة التشغيل، خصوصاً Linux.</li>
        <li><b>افهم الشبكات</b>نموذج TCP/IP وعناوين IP والبروتوكولات الأساسية.</li>
        <li><b>تدرّب عملياً بأمان</b>منصات تعليمية مثل TryHackMe وتحديات CTF ومشروع OWASP.</li>
        <li><b>احصل على شهادة مهنية</b>مثل CompTIA Security+ أو Cisco CCNA في المراحل المتقدمة.</li>
        <li><b>تخصّص</b>اختر مساراً واحداً وابنِ فيه مشاريع ومشروع تخرج.</li>
      </ol>
    </div>
    <div class="reveal">
      {callout("Gavel", "<b>الأخلاقيات أولاً:</b> اختبار أي نظام أو شبكة دون إذن مكتوب من مالكها عمل غير قانوني حتى لو كان بقصد التعلّم. تدرّب فقط في المختبرات والمنصات المخصصة لذلك.", "warn")}
      <div class="card quiz" style="margin-top:22px">
        <h3>{I("MessageCircleQuestion")} اختبر نفسك</h3>
        <div class="q"><p><b>1. وصلتك رسالة: «حسابك الجامعي سيُغلق خلال ساعة، اضغط هنا للتحقق». ماذا تفعل؟</b></p>
          <div class="opts"><button>أضغط الرابط بسرعة قبل إغلاق الحساب</button><button data-ok="1">لا أضغط، وأتحقق من الجهة الرسمية مباشرة</button><button>أرسل كلمة المرور بالرد على الرسالة</button></div>
          <p class="why">الاستعجال والتهديد علامتان شائعتان للتصيّد. ادخل دائماً من الرابط الرسمي الذي تعرفه.</p></div>
        <div class="q"><p><b>2. أيّ كلمات المرور أقوى؟</b></p>
          <div class="opts"><button>Ahmed2007</button><button>12345678</button><button data-ok="1">Qamar!Shay-Baghdad#47</button></div>
          <p class="why">الطول والمزج بين الأحرف والأرقام والرموز يجعلان التخمين أصعب بكثير.</p></div>
        <div class="q"><p><b>3. مبدأ «لا يطّلع على المعلومة إلا المخوَّل» هو…</b></p>
          <div class="opts"><button data-ok="1">السرية</button><button>التوافر</button><button>السلامة</button></div>
          <p class="why">السرية Confidentiality أحد أركان الأمن الثلاثة مع السلامة والتوافر.</p></div>
      </div>
    </div>
  </div>
</section>
"""

# ================================================================ PORTALS
def portal(url, icon, title, text, tone=""):
    return (f'<a class="card link-card portal reveal" href="{url}" target="_blank" rel="noopener"><div class="ico {tone}">{I(icon)}</div>'
            f'<div><h3>{title}</h3><p>{text}</p><span class="url">{html.escape(url)}</span></div></a>')

portals = page_hero("البوابات الإلكترونية المهمة", "روابط رسمية ستحتاجها طوال دراستك. احفظ هذه الصفحة في المفضلة.", "البوابات المهمة", 51) + f"""
<section class="block">
  <div class="container">
    {head("للطالب", "بوابات الدراسة اليومية")}
    <div class="grid g2">
      {portal(L["stu"], "UserCheck", "البروفايل الأكاديمي للطلبة – نظام التعليم الإلكتروني", "بوابة الطلبة في نظام التعليم الإلكتروني للجامعة: التسجيل، والبروفايل الأكاديمي للطالب، وبياناتك الدراسية.")}
      {portal(L["bologna"], "GraduationCap", "نظام مسار بولونيا", "نظام الجامعة الخاص بمسار بولونيا: المقررات ووحداتها ومتابعة دراستك وفق النظام.", "m")}
      {portal(L["elearn"], "Monitor", "منصة التعليم الإلكتروني", "بوابة التعليم الإلكتروني في الجامعة للمحاضرات والصفوف الإلكترونية.", "v")}
      {portal(L["dept_staff"], "Users", "البروفايل الأكاديمي للتدريسيين", "تعرّف على أساتذة القسم، وطرق التواصل معهم، واختصاصاتهم وبحوثهم.", "a")}
    </div>
  </div>
</section>

<section class="block alt">
  <div class="container">
    {head("القسم والجامعة", "مواقع رسمية للمتابعة")}
    <div class="grid g3">
      {portal(L["dept"], "Building2", "موقع قسم علوم الحاسوب", "أخبار القسم وتعاميمه وصفحاته الرسمية.")}
      {portal(L["dept_ads"], "Megaphone", "تعاميم القسم", "الجداول والإعلانات والقرارات.", "r")}
      {portal(L["uni"], "Globe", "موقع الجامعة المستنصرية", "الموقع الرسمي للجامعة.", "v")}
      {portal(L["newreg"], "ClipboardCheck", "تسجيل الطلبة الجدد", "تعليمات تسجيل الطلبة المقبولين حديثاً.", "m")}
      {portal(L["library"], "Library", "المكتبة المركزية", "المصادر والمراجع والخدمات المكتبية.", "a")}
      {portal(L["repo"], "Database", "المستودع الرقمي", "بحوث ومنشورات الجامعة.")}
      {portal(L["aware"], "Lightbulb", "إرشادات توعوية", "توجيهات رسمية للطلبة.", "a")}
      {portal(L["report"], "Siren", "بوابة الإبلاغ", "الإبلاغ الرسمي عن المشكلات.", "r")}
      {portal(L["phones"], "Phone", "الهواتف الداخلية", "أرقام تشكيلات الجامعة.", "m")}
    </div>
  </div>
</section>

<section class="block">
  <div class="container">
    {head("تابع الجامعة", "الحسابات الرسمية على مواقع التواصل")}
    <div class="grid g3">
      {portal(L["fb"], "Facebook", "فيسبوك", "الصفحة الرسمية للجامعة المستنصرية.")}
      {portal(L["ig"], "Instagram", "إنستغرام", "صور وأخبار الحياة الجامعية.", "v")}
      {portal(L["yt"], "Youtube", "يوتيوب", "فيديوهات الجامعة وفعالياتها.", "r")}
    </div>
    {callout("ShieldCheck", "<b>نصيحة أمنية:</b> قبل كتابة كلمة المرور في أي بوابة تأكد أن العنوان في المتصفح ينتهي بالنطاق الرسمي <b dir='ltr'>uomustansiriyah.edu.iq</b> أو أحد نطاقاته الفرعية الموثوقة، وأن الاتصال آمن (https).", "warn")}
  </div>
</section>
"""

# ================================================================ EMAIL
email = page_hero("البريد الإلكتروني الجامعي", "هويتك الرقمية الرسمية في الجامعة: لماذا هو مهم، وكيف تحصل عليه، وكيف تحميه.", "البريد الجامعي", 61) + f"""
<section class="block">
  <div class="container grid g2" style="align-items:center">
    <div class="reveal">
      <span class="kicker">التعريف</span>
      <h2>ما هو البريد الجامعي؟</h2>
      <p>البريد الجامعي حساب بريد إلكتروني رسمي تمنحه الجامعة لكل طالب، ويحمل نطاق الجامعة (مثل <b dir="ltr">…@uomustansiriyah.edu.iq</b>). هو هويتك الرقمية الرسمية طوال سنوات الدراسة، وبه تدخل إلى كثير من الخدمات التعليمية.</p>
      <p>تعامل معه كما تتعامل مع هويتك الجامعية: لا تعيره لأحد، ولا تهمله.</p>
      <div class="btns">{ext(L["stu"], "نظام التعليم الإلكتروني – بوابة الطلبة")}</div>
    </div>
    <div class="grid g2">
      {card("Megaphone", "تواصل رسمي", "تصلك عليه الإعلانات والتعاميم ورسائل الأساتذة.")}
      {card("Monitor", "الصفوف الإلكترونية", "الدخول إلى صفوف المواد ورفع الواجبات والاختبارات.", "v")}
      {card("Award", "مزايا الطلبة", "كثير من الشركات تمنح الطلبة برامج وخدمات مجانية أو مخفّضة عند التسجيل بالبريد الأكاديمي.", "m")}
      {card("Briefcase", "مظهر مهني", "استخدمه في المراسلات الأكاديمية والتقديم على المنح والتدريب.", "a")}
    </div>
  </div>
</section>

<section class="block alt">
  <div class="container grid g2" style="align-items:start">
    <div class="reveal">
      {head("الحصول عليه", "كيف تحصل على بريدك الجامعي؟")}
      <ol class="steps">
        <li><b>أكمل تسجيلك في القسم</b>يُنشأ الحساب للطلبة المسجّلين رسمياً.</li>
        <li><b>استلم بيانات الدخول</b>من الجهة المختصة في الكلية أو القسم (وحدة التعليم الإلكتروني أو شعبة التسجيل) أو حسب التعليمات المعلنة.</li>
        <li><b>غيّر كلمة المرور فوراً</b>عند أول دخول، واختر كلمة قوية لم تستخدمها في أي مكان آخر.</li>
        <li><b>أضف وسائل الاسترداد</b>رقم هاتف وبريد احتياطي، لتستعيد حسابك إذا نسيت كلمة المرور.</li>
        <li><b>فعّل التحقق بخطوتين</b>رمز يصل إلى هاتفك عند كل دخول جديد.</li>
      </ol>
    </div>
    <div class="reveal">
      {head("أداة تفاعلية", "جرّب قوة كلمة المرور", "الأداة تعمل داخل متصفحك فقط ولا ترسل أي شيء. لا تكتب كلمة مرورك الحقيقية.")}
      <div class="card meter-box">
        <label for="pw"><b>كلمة مرور تجريبية</b></label>
        <input id="pw" type="text" autocomplete="off" spellcheck="false" placeholder="Try: Baghdad!Code-2026">
        <div class="meter"><i></i></div>
        <div class="meter-label" id="pw-label">اكتب كلمة مرور تجريبية (لا تكتب كلمتك الحقيقية)</div>
        <p class="muted" id="pw-tips" style="margin:6px 0 0"></p>
      </div>
      {callout("Lightbulb", "فكرة سهلة: استخدم «عبارة مرور» من 3–4 كلمات لا رابط بينها مع رقم ورمز، مثل <b dir='ltr'>Qamar!Shay-Baghdad#47</b> — طويلة وسهلة التذكّر.", "ok")}
    </div>
  </div>
</section>

<section class="block">
  <div class="container">
    {head("الحماية", "كيف تحافظ على بريدك الجامعي؟")}
    <div class="grid g2">
      <div class="card reveal"><h3 style="color:var(--mint)">افعل</h3><ul class="check">
        <li>كلمة مرور طويلة وفريدة لهذا الحساب فقط</li>
        <li>فعّل التحقق بخطوتين</li>
        <li>سجّل الخروج من أجهزة المختبر والأجهزة المشتركة</li>
        <li>حدّث متصفحك ونظام هاتفك باستمرار</li>
        <li>تحقق من اسم المرسل والرابط قبل الضغط</li>
        <li>راجع نشاط الدخول الأخير بين حين وآخر</li>
      </ul></div>
      <div class="card reveal"><h3 style="color:var(--red)">لا تفعل</h3><ul class="check cross">
        <li>لا تشارك كلمة المرور حتى مع الأصدقاء</li>
        <li>لا ترسل كلمة المرور أو رمز التحقق لأي شخص يدّعي أنه من الجامعة</li>
        <li>لا تفتح مرفقات غير متوقعة (.exe أو .zip)</li>
        <li>لا تحفظ كلمة المرور في متصفح جهاز عام</li>
        <li>لا تستخدم البريد الجامعي للتسجيل في مواقع غير موثوقة</li>
        <li>لا تدخل حسابك عبر شبكات واي فاي مفتوحة دون حماية</li>
      </ul></div>
    </div>
  </div>
</section>

<section class="block alt">
  <div class="container grid g2" style="align-items:start">
    <div class="reveal">
      {head("مثال تعليمي", "اكتشف رسالة التصيّد", "رسالة وهمية لأغراض التدريب. لاحظ العلامات الحمراء.")}
      <div class="card" style="border:2px dashed #F3B5C0">
        <p class="muted" style="margin:0 0 6px">من: <span dir="ltr">it-help@uomus-verify.net</span> &nbsp;<span class="tag" style="background:#FDECEF;color:var(--red)">1 نطاق غريب</span></p>
        <p style="margin:0 0 10px"><b>عاجل!! سيتم إيقاف بريدك الجامعي خلال 60 دقيقة</b> <span class="tag" style="background:#FDECEF;color:var(--red)">2 استعجال وتهديد</span></p>
        <p style="margin:0 0 10px">عزيزي المستخدم، لتجنب الإيقاف يرجى إدخال اسم المستخدم وكلمة المرور ورمز التحقق عبر الرابط أدناه. <span class="tag" style="background:#FDECEF;color:var(--red)">3 طلب كلمة المرور</span></p>
        <p style="margin:0"><u dir="ltr">http://uomus-login-check.xyz/verify</u> <span class="tag" style="background:#FDECEF;color:var(--red)">4 رابط غير رسمي</span></p>
      </div>
    </div>
    <div class="reveal">
      {head("عند الاختراق", "ماذا أفعل إذا شككت أن حسابي اختُرق؟")}
      <ol class="steps">
        <li><b>غيّر كلمة المرور فوراً</b>من جهاز موثوق، وغيّرها في أي حساب آخر يستخدم الكلمة نفسها.</li>
        <li><b>سجّل الخروج من جميع الأجهزة</b>وفعّل التحقق بخطوتين إن لم يكن مفعّلاً.</li>
        <li><b>أبلغ الجهة المختصة</b>في الكلية أو وحدة التعليم الإلكتروني، أو عبر <a href="{L['report']}" target="_blank" rel="noopener">بوابة الإبلاغ</a>.</li>
        <li><b>نبّه زملاءك</b>إذا أُرسلت رسائل مشبوهة من حسابك إليهم.</li>
      </ol>
    </div>
  </div>
</section>
"""

# ================================================================ TEAM
MEMBERS = [("m-ithar.jpg", "الأستاذ المساعد الدكتور إيثار عبد الوهاب حاجم", "رئيسة الفريق", True),
           ("m-yasmin.jpg", "الأستاذ المساعد ياسمين مكي محي الدين", "عضو الفريق", False),
           ("m-salah.jpg", "الأستاذ صلاح طه علاوي", "عضو الفريق", False),
           ("m-basim.jpg", "الأستاذ المساعد باسم أخضير عباس", "عضو الفريق", False)]
AV_BOX = "width:112px;height:112px;overflow:hidden;padding:0;background:#EEF4FF"
AV_IMG = "width:112px;height:112px;max-width:none;object-fit:cover;object-position:center top;border-radius:50%;display:block"
mem_html = "".join(
    f'<div class="card member reveal{" lead" if lead else ""}">{"<span class=badge>رئيسة الفريق</span>" if lead else ""}'
    f'<div class="avatar photo" style="{AV_BOX}"><img style="{AV_IMG}" src="assets/img/{photo}" alt="{name}" width="112" height="112"></div>'
    f'<h3>{name}</h3><p class="role">{role}</p><p class="muted">قسم علوم الحاسوب – كلية العلوم</p></div>' for photo, name, role, lead in MEMBERS)
team = page_hero("فريق الابتكار الرقمي التطوعي", "Digital Innovation Team — فريق تطوعي من تدريسيي قسم علوم الحاسوب يعمل على مبادرات رقمية تخدم الطلبة والقسم.", "فريق الابتكار", 71) + f"""
<section class="block">
  <div class="container grid g2" style="align-items:center">
    <div class="reveal">
      <span class="kicker">من نحن</span>
      <h2>فريق يؤمن بأن التقنية في خدمة الطالب</h2>
      <p><b>فريق الابتكار الرقمي</b> فريق تطوعي في قسم علوم الحاسوب – كلية العلوم – الجامعة المستنصرية. يعمل الفريق على تقديم حلول ومبادرات رقمية تسهّل حياة الطلبة الجامعية، وتنشر الوعي التقني والأمني، وتشجع روح الابتكار والعمل الجماعي.</p>
      <p>هذا الموقع إحدى مبادرات الفريق لاستقبال طلبة المرحلة الأولى للعام الدراسي {YEAR}، ليجد كل طالب جديد المعلومات الأساسية والروابط الرسمية في مكان واحد.</p>
    </div>
    <div class="hero-logo" style="width:min(300px,70vw)"><img src="assets/img/logo-full.jpg" alt="شعار فريق الابتكار الرقمي" width="480" height="480"></div>
  </div>
</section>

<section class="block alt">
  <div class="container">
    {head("الإشراف", "بإشراف")}
    <div class="grid g2" style="max-width:820px;margin-bottom:46px">
      <div class="card member lead reveal"><div class="avatar photo" style="width:132px;height:132px;overflow:hidden;padding:0;background:#EEF4FF"><img style="width:132px;height:132px;max-width:none;object-fit:cover;object-position:center top;border-radius:50%;display:block" src="assets/img/dean.jpg" alt="الأستاذ الدكتور ميثاق طالب كاطع" width="132" height="132"></div><h3>الأستاذ الدكتور ميثاق طالب كاطع</h3><p class="role">عميد كلية العلوم</p><p class="muted">كلية العلوم – الجامعة المستنصرية</p></div>
      <div class="card member lead reveal"><div class="avatar photo" style="width:132px;height:132px;overflow:hidden;padding:0;background:#EEF4FF"><img style="width:132px;height:132px;max-width:none;object-fit:cover;object-position:center top;border-radius:50%;display:block" src="assets/img/head-cs.jpg" alt="الأستاذ الدكتور ذكرى حيدر علي عباس" width="132" height="132"></div><h3>الأستاذ الدكتور ذكرى حيدر علي عباس</h3><p class="role">رئيسة قسم علوم الحاسوب</p><p class="muted">قسم علوم الحاسوب – كلية العلوم</p></div>
    </div>
    {head("أعضاء الفريق", "أعدّ هذا الدليل")}
    <div class="grid g4">{mem_html}</div>
  </div>
</section>

<section class="block">
  <div class="container">
    {head("قيمنا", "ما الذي يحركنا؟")}
    <div class="grid g4">
      {card("Lightbulb", "الابتكار", "أفكار رقمية جديدة تحل مشكلات حقيقية في البيئة الجامعية.")}
      {card("HeartHandshake", "التطوع", "نعمل بروح العطاء لخدمة الطلبة والقسم.", "v")}
      {card("ShieldCheck", "الوعي الرقمي", "نشر ثقافة الاستخدام الآمن والمسؤول للتقنية.", "m")}
      {card("Users", "العمل الجماعي", "نؤمن بأن الفريق المتعاون يحقق ما لا يحققه الفرد.", "a")}
    </div>
  </div>
</section>
"""

notfound = page_hero("الصفحة غير موجودة", "ربما تغيّر الرابط أو كُتب بشكل خاطئ.", "404", 81) + f"""
<section class="block"><div class="container" style="text-align:center">
<p>عُد إلى الصفحة الرئيسية لتصفح دليل طلبة المرحلة الأولى.</p>
<div class="btns" style="justify-content:center"><a class="btn btn-primary" href="index.html">{I("House")}<span>الصفحة الرئيسية</span></a></div>
</div></section>"""

SITE = [
    ("index.html", "الرئيسية", "دليل ترحيبي لطلبة المرحلة الأولى في قسم علوم الحاسوب – كلية العلوم – الجامعة المستنصرية، من إعداد فريق الابتكار الرقمي التطوعي.", home),
    ("department.html", "قسم علوم الحاسوب", "تعريف بقسم علوم الحاسوب في الجامعة المستنصرية: الدراسة، والمسار خلال أربع سنوات، والروابط الرسمية.", department),
    ("college.html", "كلية العلوم والجامعة المستنصرية", "تعريف بالجامعة المستنصرية وكلية العلوم وأقسامها.", college),
    ("bologna.html", "نظام مسار بولونيا", "شرح مبسّط لنظام مسار بولونيا: وحدات ECTS والتقييم والنجاح والحضور ورابط نظام الجامعة.", bologna),
    ("cybersecurity.html", "الأمن السيبراني", "تعريف بالأمن السيبراني وأهميته والتهديدات الشائعة ومجالات العمل فيه.", cyber),
    ("portals.html", "البوابات المهمة", "روابط البوابات الإلكترونية المهمة لطلبة الجامعة المستنصرية مثل البروفايل الأكاديمي للطلبة.", portals),
    ("email.html", "البريد الجامعي", "أهمية البريد الإلكتروني الجامعي وكيفية الحصول عليه وحمايته.", email),
    ("team.html", "فريق الابتكار الرقمي", "تعريف بفريق الابتكار الرقمي التطوعي في قسم علوم الحاسوب وأعضائه.", team),
    ("404.html", "الصفحة غير موجودة", "الصفحة غير موجودة.", notfound),
]

for fname, title, desc, body in SITE:
    with open(os.path.join(OUT, fname), "w", encoding="utf-8") as f:
        f.write(layout(fname, title, desc, body))
print("built", len(SITE), "pages")
