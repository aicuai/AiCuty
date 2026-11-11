#!/usr/bin/env python3
"""AiCuty キャラクター設計シートを「正本プロンプト」から再現生成する。

方針（aki 2026-09-12）:
  - **プロンプトが正本**（画像でなくテキストプロンプトで生成する）。各キャラの正本プロンプトは
    この AiCuty リポジトリに置き、ここから再現できるように管理する。
  - 既定は text-to-image（参照画像なし）。レイアウト参照が要る時だけ --ref で画像を渡す。
  - 文字が崩れて情報が欠落するのを避けたい用途では、絵はここで作り、ラベル等は
    scripts/compose_charsheet_text.py（PIL）で後付け合成する二段構えにできる。

必要: 環境変数 OPENAI_API_KEY（~/.zshrc に export 済み）。モデルは GPT-Image-2.5。

使い方:
  export OPENAI_API_KEY=...   # aki の ~/.zshrc に有り
  python3 scripts/generate_charsheet.py \
    --prompt MarshaArancia/prompts/platform-api-designsheet-prompt.txt \
    --out MarshaArancia/MarshaArancia-DesignSheet-2.5.png \
    --size 1536x1024 --model gpt-image-2.5-flare
  # 参照画像も併用するなら: --ref MarshaArancia/MarshaArancia-Illustration-Reference.png
"""
import argparse, base64, json, os, sys, urllib.request

OPENAI = "https://api.openai.com/v1/images"


def post_multipart(url, fields, files, token):
    boundary = "----aicuty" + base64.urlsafe_b64encode(os.urandom(9)).decode()
    body = bytearray()
    for k, v in fields.items():
        body += f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"\r\n\r\n{v}\r\n".encode()
    for k, path in files:
        fn = os.path.basename(path)
        body += f"--{boundary}\r\nContent-Disposition: form-data; name=\"{k}\"; filename=\"{fn}\"\r\n".encode()
        body += b"Content-Type: image/png\r\n\r\n" + open(path, "rb").read() + b"\r\n"
    body += f"--{boundary}--\r\n".encode()
    req = urllib.request.Request(url, data=bytes(body), method="POST")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)


def post_json(url, payload, token):
    req = urllib.request.Request(url, data=json.dumps(payload).encode(), method="POST")
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "application/json")
    with urllib.request.urlopen(req, timeout=180) as r:
        return json.load(r)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--prompt", required=True, help="正本プロンプトの .txt")
    ap.add_argument("--out", required=True)
    ap.add_argument("--model", default="gpt-image-2.5-flare",
                    help="gpt-image-2.5-flare / gpt-image-2.5-sunburst / gpt-image-2")
    ap.add_argument("--size", default="1536x1024")
    ap.add_argument("--quality", default="high")
    ap.add_argument("--ref", nargs="*", default=[], help="参照画像（省略時 text-to-image）")
    a = ap.parse_args()

    token = os.environ.get("OPENAI_API_KEY")
    if not token:
        sys.exit("OPENAI_API_KEY が未設定です（~/.zshrc を source してください）")
    prompt = open(a.prompt, encoding="utf-8").read().strip()

    if a.ref:
        d = post_multipart(f"{OPENAI}/edits",
                           {"model": a.model, "size": a.size, "quality": a.quality, "prompt": prompt},
                           [("image[]", p) for p in a.ref], token)
    else:
        d = post_json(f"{OPENAI}/generations",
                      {"model": a.model, "size": a.size, "quality": a.quality, "prompt": prompt}, token)

    open(a.out, "wb").write(base64.b64decode(d["data"][0]["b64_json"]))
    u = d.get("usage", {})
    print(f"[ok] {a.out}  (model={a.model} size={a.size} tokens={u.get('total_tokens')})")


if __name__ == "__main__":
    main()
