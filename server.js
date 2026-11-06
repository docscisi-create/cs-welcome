// Minimal static server for Railway (no dependencies). Railway provides PORT.
const http = require("http");
const fs = require("fs");
const path = require("path");

const ROOT = path.join(__dirname, "public");
const PORT = process.env.PORT || 3000;
const TYPES = {
  ".html": "text/html; charset=utf-8", ".css": "text/css; charset=utf-8", ".js": "text/javascript; charset=utf-8",
  ".png": "image/png", ".jpg": "image/jpeg", ".svg": "image/svg+xml", ".ico": "image/x-icon", ".json": "application/json",
  ".woff2": "font/woff2", ".txt": "text/plain; charset=utf-8"
};

function send(res, file, status) {
  fs.readFile(file, (err, data) => {
    if (err) { res.writeHead(500); return res.end("Server error"); }
    const ext = path.extname(file).toLowerCase();
    res.writeHead(status, {
      "Content-Type": TYPES[ext] || "application/octet-stream",
      "Cache-Control": ext === ".html" ? "no-cache" : "public, max-age=604800",
      "X-Content-Type-Options": "nosniff",
      "Referrer-Policy": "strict-origin-when-cross-origin"
    });
    res.end(data);
  });
}

http.createServer((req, res) => {
  let p;
  try { p = decodeURIComponent(new URL(req.url, "http://x").pathname); } catch (e) { res.writeHead(400); return res.end(); }
  if (p.endsWith("/")) p += "index.html";
  let file = path.normalize(path.join(ROOT, p));
  if (!file.startsWith(ROOT)) { res.writeHead(403); return res.end(); }
  // clean URLs: /bologna -> /bologna.html
  if (!path.extname(file) && fs.existsSync(file + ".html")) file += ".html";
  fs.stat(file, (err, st) => {
    if (!err && st.isFile()) return send(res, file, 200);
    send(res, path.join(ROOT, "404.html"), 404);
  });
}).listen(PORT, "0.0.0.0", () => console.log("Site running on port " + PORT));
