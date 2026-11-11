(() => {
const { lang, base } = window.AICUTY;
const D = window.AICUTY_DATA;
const U = D.ui[lang];
const L = m => lang === "ja" ? m.ja : m.enT;
const A = p => base + p;                       // asset path
const ext = h => h.startsWith("http");
const $ = s => document.querySelector(s);
const store = { get(k){ try { return localStorage.getItem(k) } catch(e){ return null } }, set(k,v){ try { localStorage.setItem(k,v) } catch(e){} } };
const reduced = () => matchMedia("(prefers-reduced-motion: reduce)").matches;

/* 推し色 / favorite color */
function setOshi(id){
  const r = document.documentElement.style;
  r.setProperty("--oshi", D.hex[id]);
  const dark = document.documentElement.dataset.theme === "dark" || (!document.documentElement.dataset.theme && matchMedia("(prefers-color-scheme: dark)").matches);
  r.setProperty("--oshi-ink", dark ? D.hex[id] : D.ink[id]);
  document.querySelectorAll("[data-oshi]").forEach(b => b.setAttribute("aria-pressed", b.dataset.oshi === id));
  store.set("aicuty-oshi", id);
}
document.querySelectorAll("[data-oshi]").forEach(b => b.addEventListener("click", () => setOshi(b.dataset.oshi)));
setOshi(D.hex[store.get("aicuty-oshi")] ? store.get("aicuty-oshi") : "elena");

/* hero carousel */
const S = D.slides, sl = $("#slides");
let cur = 0, timer;
sl.innerHTML = S.map((s,i) => `<div class="slide${i ? "" : " on"}" role="group" aria-roledescription="slide" aria-label="${i+1} / ${S.length}"><img src="${A(s.img)}" alt="${s[lang].alt}" ${i ? 'loading="lazy"' : 'fetchpriority="high"'}></div>`).join("") +
  `<div class="cap"><div class="wrap"><div><div class="tag" id="ctag"></div><h2><a id="ctitle"></a></h2></div><div class="hctl"><div class="dots">${S.map((_,i) => `<button aria-label="${U.slide} ${i+1}"></button>`).join("")}</div><button class="arw" id="prev" aria-label="${U.prev}">‹</button><button class="arw" id="next" aria-label="${U.nextS}">›</button></div></div></div>`;
function go(i){
  cur = (i + S.length) % S.length;
  sl.querySelectorAll(".slide").forEach((e,j) => e.classList.toggle("on", j === cur));
  sl.querySelectorAll(".dots button").forEach((e,j) => e.classList.toggle("on", j === cur));
  const s = S[cur], a = $("#ctitle");
  $("#ctag").textContent = s[lang].tag; a.textContent = s[lang].title; a.href = s.href;
  if (ext(s.href)) { a.target = "_blank"; a.rel = "noopener" } else a.removeAttribute("target");
}
function auto(){ clearInterval(timer); if (!reduced()) timer = setInterval(() => go(cur + 1), 6000) }
$("#prev").onclick = () => { go(cur - 1); auto() };
$("#next").onclick = () => { go(cur + 1); auto() };
sl.querySelectorAll(".dots button").forEach((b,i) => b.onclick = () => { go(i); auto() });
go(0); auto();

/* news */
const cats = ["all", ...new Set(D.news.map(n => n.cat))];
let curCat = "all";
const catLabel = c => c === "all" ? U.all : D.categories[c][lang];
$("#filters").setAttribute("aria-label", U.filter);
function renderNews(){
  $("#filters").innerHTML = cats.map(c => `<button data-c="${c}" aria-pressed="${c === curCat}">${catLabel(c)}</button>`).join("");
  $("#filters").querySelectorAll("button").forEach(b => b.onclick = () => { curCat = b.dataset.c; renderNews() });
  $("#newsList").innerHTML = D.news.filter(n => curCat === "all" || n.cat === curCat).map(n =>
    `<a class="ncard" href="${n.href}" ${ext(n.href) ? 'target="_blank" rel="noopener"' : ""}><div class="thumb"><img src="${A(n.img)}" alt="" loading="lazy"></div><div class="body"><div class="meta"><span class="cat">${catLabel(n.cat)}</span><span class="mono">${n.date}</span></div><h3>${n[lang]}</h3></div></a>`).join("");
}
renderNews();

/* members */
const M = D.members;
$("#mgrid").innerHTML = M.map(m => `<button class="mcard" style="--c:${D.hex[m.id]}" data-id="${m.id}" aria-label="${L(m).name}${U.profile}"><span class="no">No.${m.no}</span><div class="pic"><img src="${A(`img/${m.id}.webp`)}" alt="${L(m).name}" loading="lazy"></div><div class="txt"><span class="en">${m.en}</span><span class="ja">${m.ja.name}</span><span class="role">${L(m).role}</span></div></button>`).join("");
$("#mgrid").querySelectorAll(".mcard").forEach(b => b.onclick = () => { location.hash = b.dataset.id });
$("#fMembers").innerHTML = M.map(m => `<li><a href="#${m.id}">${L(m).name}</a></li>`).join("");

const dlg = $("#dlg");
let audio = null;
function openMember(id){
  const m = M.find(x => x.id === id); if (!m) return;
  const t = L(m), i = M.indexOf(m), prev = M[(i + 5) % 6], next = M[(i + 1) % 6];
  const transcript = lang === "ja" ? m.ja.voice : "";
  dlg.style.setProperty("--c", D.hex[m.id]);
  dlg.innerHTML = `<button class="dclose" id="dclose" aria-label="${U.close}">×</button><div class="dl">
   <div class="art"><img src="${A(`img/${m.id}-fig.webp`)}" alt="${t.name}"></div>
   <div class="info">
    <div class="kicker">${U.member} No.${m.no} ・ ${t.color}</div>
    <h3 id="dName">${m.en}<small>${m.ja.name}</small></h3>
    <p style="margin:0">${t.about}</p>
    <dl class="prof"><dt>${U.role}</dt><dd>${t.role}</dd><dt>${U.band}</dt><dd>${t.inst}</dd><dt>${U.bday}</dt><dd>${U.date(m.bd[0], m.bd[1])}（${t.bdn}）</dd><dt>${U.fp}</dt><dd>${t.fp}</dd></dl>
    ${lang === "ja" ? `<blockquote class="quote">${m.ja.talk}</blockquote>` : ""}
    <div class="voice"><button id="vplay" aria-label="${t.name}${U.listen}">▶</button><div class="vt"><b>${U.voice} ・ ${t.vdesc}</b>${transcript}</div></div>
    <div class="dnav"><a class="more" href="https://github.com/aicuai/AiCuty/tree/main/${m.dir}" target="_blank" rel="noopener">${U.sheet}</a>${m.x ? `<a class="more" href="${m.x}" target="_blank" rel="noopener">X →</a>` : ""}<a class="more" href="#${prev.id}">‹ ${L(prev).name}</a><a class="more" href="#${next.id}">${L(next).name} ›</a></div>
   </div></div>`;
  if (!dlg.open) dlg.showModal();
  $("#dclose").onclick = () => dlg.close();
  const vb = $("#vplay");
  vb.onclick = () => {
    if (audio && !audio.paused) { audio.pause(); vb.textContent = "▶"; return }
    if (audio) audio.pause();
    audio = new Audio(A(`voice/${m.id}-v3-${lang}.mp3`));
    audio.onended = () => vb.textContent = "▶";
    audio.play().then(() => vb.textContent = "❚❚").catch(() => vb.textContent = "▶");
  };
}
const isMemberHash = () => M.some(m => "#" + m.id === location.hash);
dlg.addEventListener("close", () => { if (audio) audio.pause(); if (isMemberHash()) history.replaceState(null, "", location.pathname + location.search + "#members") });
dlg.addEventListener("click", e => { if (e.target === dlg) dlg.close() });
function route(){ const id = location.hash.slice(1); if (M.some(m => m.id === id)) openMember(id); else if (dlg.open) dlg.close() }
addEventListener("hashchange", route); route();

/* birthday calendar */
const now = new Date(), today = new Date(now.getFullYear(), now.getMonth(), now.getDate()), y = today.getFullYear();
const nb = M.map(m => { let d = new Date(y, m.bd[0]-1, m.bd[1]); if (d < today) d = new Date(y+1, m.bd[0]-1, m.bd[1]); return { m, d } }).sort((a,b) => a.d - b.d)[0];
const days = Math.round((nb.d - today) / 864e5);
$("#calNext").style.setProperty("--c", D.hex[nb.m.id]);
$("#calNext").innerHTML = `<img src="${A(`img/${nb.m.id}.webp`)}" alt=""><div><div class="lbl">${U.next}</div><div style="font-weight:700">${L(nb.m).name}　${U.date(nb.m.bd[0], nb.m.bd[1])}</div></div><div style="margin-left:auto;text-align:right"><div class="lbl">${days ? U.left : ""}</div><div class="big mono">${days === 0 ? U.today : days + `<span style="font-size:1rem"> ${U.days}</span>`}</div></div>`;
$("#months").innerHTML = Array.from({ length: 12 }, (_, i) => {
  const bs = M.filter(m => m.bd[0] === i + 1);
  return `<div class="mo${i === now.getMonth() ? " now" : ""}"><span class="m">${U.month(i+1)}</span>${bs.map(m => `<a class="bd" href="#${m.id}" style="--c:${D.hex[m.id]};text-decoration:none"><span>${m.bd[0]}/${m.bd[1]}</span>${L(m).short}</a>`).join("")}</div>`;
}).join("");

$("#totop").onclick = () => scrollTo({ top: 0, behavior: reduced() ? "auto" : "smooth" });
})();
