// Build the AiCuty official site into dist/ (served at https://aicu.ai/aicuty/).
//   node site/build.mjs
// Output:
//   dist/index.html      Japanese (default)
//   dist/en/index.html   English
//   dist/{style.css,data.js,app.js,img/,voice/}
import { readFileSync, writeFileSync, mkdirSync, cpSync, rmSync, readdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const repo = join(here, "..");
const dist = join(here, "dist");
const SITE = "https://aicu.ai/aicuty/";
// TODO: 正式な問い合わせフォームの URL に差し替える
const CONTACT_URL = "https://aicu.ai/";

const tpl = readFileSync(join(here, "src/template.html"), "utf8");
const i18n = JSON.parse(readFileSync(join(here, "src/i18n.json"), "utf8"));

rmSync(dist, { recursive: true, force: true });
mkdirSync(join(dist, "en"), { recursive: true });

function render(lang, base) {
  const t = i18n[lang];
  const vars = {
    lang, base,
    canonical: lang === "ja" ? SITE : SITE + "en/",
    jaHref: lang === "ja" ? "./" : "../",
    enHref: lang === "ja" ? "en/" : "./",
    isJa: String(lang === "ja"), isEn: String(lang === "en"),
    contactUrl: CONTACT_URL,
  };
  return tpl.replace(/\{\{(t\.)?(\w+)\}\}/g, (m, isT, k) => {
    const v = isT ? t[k] : vars[k];
    if (v === undefined) throw new Error(`missing ${lang}: ${m}`);
    return v;
  });
}

writeFileSync(join(dist, "index.html"), render("ja", ""));
writeFileSync(join(dist, "en/index.html"), render("en", "../"));
for (const f of ["style.css", "data.js", "app.js"]) cpSync(join(here, "src", f), join(dist, f));
cpSync(join(here, "assets/img"), join(dist, "img"), { recursive: true });

// voices: official v3 samples (ja/en) from docs/voice/<slug>/
mkdirSync(join(dist, "voice"));
for (const slug of ["elena", "mei", "mina", "nao", "saki", "marsha"]) {
  for (const lang of ["ja", "en"]) {
    const f = `${slug}-v3-${lang}.mp3`;
    cpSync(join(repo, "docs/voice", slug, f), join(dist, "voice", f));
  }
}
console.log("built", readdirSync(dist));
