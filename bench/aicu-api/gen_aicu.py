#!/usr/bin/env python3
"""AICU API 経由で GPT-Image-2.5 の model / quality / AP を実測する。

使い方:
  AICU_API_KEY=aicu_live_... python3 bench_aicu.py --model gpt-image-2.5-flare --quality medium --label mei
結果は results.csv に追記、画像は out/<label>.png。
AP は X-AICU-AP-Cost ヘッダ（1 回ごとの実費）を正とする。
"""
import argparse, base64, csv, json, os, pathlib, sys, time, urllib.error, urllib.request

API = "https://api.aicu.ai/v1"
HERE = pathlib.Path(__file__).parent
OUT = HERE / "out"; OUT.mkdir(exist_ok=True)
CSV = HERE / "results.csv"

def call(path, key, body=None, method="GET", timeout=300):
    req = urllib.request.Request(API + path, method=method,
                                 data=json.dumps(body).encode() if body else None)
    req.add_header("Authorization", "Bearer " + key)
    if body: req.add_header("Content-Type", "application/json")
    res = urllib.request.urlopen(req, timeout=timeout)
    return json.load(res), dict(res.headers)

def balance(key):
    d, _ = call("/usage/credits", key)
    return d["available"]

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", default="gpt-image-2.5-flare")
    p.add_argument("--quality", default="medium")
    p.add_argument("--size", default="1024x1024")
    p.add_argument("--prompt-file"); p.add_argument("--prompt")
    p.add_argument("--character", help="登録プリセットの slug（model より優先される）")
    p.add_argument("--label", required=True)
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()

    key = os.environ.get("AICU_API_KEY")
    if not key: sys.exit("AICU_API_KEY 未設定")
    prompt = a.prompt or pathlib.Path(a.prompt_file).read_text(encoding="utf-8").strip()

    body = {"prompt": prompt, "size": a.size, "quality": a.quality, "force": True}
    if a.character: body["character"] = a.character
    else: body["model"] = a.model

    before = balance(key)
    tag = a.character or a.model
    print(f"[{a.label}] {tag} quality={a.quality} size={a.size}  残高 {before} AP")
    if a.dry_run: return

    t0 = time.time()
    try:
        d, h = call("/images/generations", key, body, "POST")
    except urllib.error.HTTPError as e:
        # 524 等でも生成は続いている。直近の 1 件を拾い直す（逐次実行前提）
        print(f"  HTTP {e.code}: {e.read()[:200]!r} — /images/recent で回収を試みます")
        time.sleep(20)
        rec, _ = call("/images/recent?limit=1", key)
        d = {"id": rec["data"][0]["id"], "recovered": True}; h = {}
    dt = time.time() - t0
    after = balance(key)

    ap = int(h.get("X-AICU-AP-Cost") or (before - after))
    b64 = (d.get("data") or [{}])[0].get("b64_json")
    png = OUT / f"{a.label}.png"
    if b64: png.write_bytes(base64.b64decode(b64))

    row = {"label": a.label, "model": tag, "quality": a.quality, "size": a.size,
           "ap_cost": ap, "latency_ms": h.get("X-AICU-Latency-Ms") or int(dt*1000),
           "wall_s": round(dt,1), "bytes": png.stat().st_size if png.exists() else 0,
           "image_id": d.get("id",""), "cached": d.get("cached"),
           "balance_after": after, "ts": time.strftime("%Y-%m-%d %H:%M:%S")}
    new = not CSV.exists()
    with CSV.open("a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(row)); 
        if new: w.writeheader()
        w.writerow(row)
    print(f"  -> {ap} AP / {row['latency_ms']} ms / {row['bytes']:,} bytes  残高 {after} AP")

if __name__ == "__main__": main()
