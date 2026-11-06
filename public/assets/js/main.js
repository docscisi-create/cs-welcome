(function () {
  "use strict";
  var store = {
    get: function (k) { try { return localStorage.getItem(k); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem(k, v); } catch (e) { /* ignore */ } }
  };

  // mobile menu
  var btn = document.querySelector(".menu-btn"), menu = document.getElementById("menu");
  if (btn && menu) {
    btn.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      btn.setAttribute("aria-expanded", open ? "true" : "false");
    });
  }

  // reveal on scroll
  var els = document.querySelectorAll(".reveal");
  if ("IntersectionObserver" in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add("in"); io.unobserve(e.target); } });
    }, { threshold: 0.08 });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add("in"); }); }

  // back to top
  var top = document.querySelector(".to-top");
  if (top) {
    window.addEventListener("scroll", function () { top.classList.toggle("show", window.scrollY > 600); }, { passive: true });
    top.addEventListener("click", function () { window.scrollTo({ top: 0, behavior: "smooth" }); });
  }

  // first-week checklist (saved in this browser only)
  var todo = document.querySelector(".todo");
  if (todo) {
    var boxes = todo.querySelectorAll("input[type=checkbox]");
    var bar = document.querySelector(".progress i"), count = document.getElementById("todo-count");
    var saved = {};
    try { saved = JSON.parse(store.get("fy-checklist") || "{}"); } catch (e) { saved = {}; }
    var update = function () {
      var done = 0, state = {};
      boxes.forEach(function (b) {
        b.closest("label").classList.toggle("done", b.checked);
        if (b.checked) done++;
        state[b.id] = b.checked;
      });
      if (bar) bar.style.width = (done / boxes.length * 100) + "%";
      if (count) count.textContent = done + " من " + boxes.length;
      store.set("fy-checklist", JSON.stringify(state));
    };
    boxes.forEach(function (b) { if (saved[b.id]) b.checked = true; b.addEventListener("change", update); });
    update();
  }

  // password strength meter (runs only in the browser; nothing is sent anywhere)
  var pw = document.getElementById("pw");
  if (pw) {
    var meter = document.querySelector(".meter i"), label = document.getElementById("pw-label"), tips = document.getElementById("pw-tips");
    pw.addEventListener("input", function () {
      var v = pw.value, s = 0, t = [];
      if (v.length >= 12) s += 2; else if (v.length >= 8) s += 1; else t.push("اجعلها 12 حرفاً أو أكثر");
      if (/[a-z]/.test(v) && /[A-Z]/.test(v)) s++; else t.push("امزج الأحرف الكبيرة والصغيرة");
      if (/\d/.test(v)) s++; else t.push("أضف أرقاماً");
      if (/[^A-Za-z0-9]/.test(v)) s++; else t.push("أضف رمزاً مثل ! أو #");
      if (/^(.)\1+$/.test(v) || /(1234|abcd|qwer|password|admin|0000)/i.test(v)) { s = Math.min(s, 1); t.push("تجنّب الأنماط السهلة مثل 1234 أو password"); }
      var lv = [["ضعيفة جداً", "#D6455D", 15], ["ضعيفة", "#E3742B", 35], ["متوسطة", "#E39B23", 60], ["جيدة", "#2F7BEA", 80], ["قوية", "#12A387", 100]];
      var i = v ? Math.min(4, Math.max(0, s - 1)) : -1;
      if (i < 0) { meter.style.width = "0"; label.textContent = "اكتب كلمة مرور تجريبية (لا تكتب كلمتك الحقيقية)"; label.style.color = ""; tips.textContent = ""; return; }
      meter.style.width = lv[i][2] + "%"; meter.style.background = lv[i][1];
      label.textContent = "القوة: " + lv[i][0]; label.style.color = lv[i][1];
      tips.textContent = t.length ? "اقتراحات: " + t.join(" · ") : "ممتاز! لا تنسَ تفعيل التحقق بخطوتين.";
    });
  }

  // quiz
  document.querySelectorAll(".quiz .q").forEach(function (q) {
    q.querySelectorAll("button").forEach(function (b) {
      b.addEventListener("click", function () {
        if (q.classList.contains("answered")) return;
        q.classList.add("answered");
        q.querySelectorAll("button").forEach(function (x) { if (x.dataset.ok) x.classList.add("right"); });
        if (!b.dataset.ok) b.classList.add("wrong");
      });
    });
  });

  var y = document.getElementById("year");
  if (y) y.textContent = new Date().getFullYear();
})();
