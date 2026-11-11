#!/usr/bin/env python3
"""AiCuty キャラクターシートの文字を PIL で合成する。

方針（aki 2026-09-12）: 絵は画像生成（GPT-Image-2.5 等）で「作り直さず高画質化」し、
**文字は画像生成に任せず PIL で後付け合成**する。画像モデルは文字を崩す/誤字を出すので、
情報の欠落ゼロを守るにはこれが確実。

入力: 文字を消した高画質アートシート（例: refsheet-<name>-enhanced-notext.png・1536x1024 前提）
      ＋ キャラデータ JSON（下の Elena 例と同じキー）。
出力: 文字を合成した最終シート PNG。

使い方:
  python3 compose_charsheet_text.py --art art.png --data elena.json --out sheet.png
  # data 省略時は下の ELENA_DEMO を使う（動作確認用）

座標は LAYOUT（相対 0..1）で調整できる。アートの視点・表情の配置に合わせて微調整して。
"""
import argparse, json, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

# ── フォント（macOS 既定。無ければ引数で差し替え）──────────────────────
FONT_BOLD = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_JP = "/System/Library/Fonts/Hiragino Sans GB.ttc"  # 日本語混在に備えて

INK = (60, 60, 66)
MUTED = (120, 120, 128)

# ── レイアウト（相対座標 0..1。アートの構図に合わせて調整）──────────────
LAYOUT = {
    "title":        {"xy": (0.50, 0.03), "size": 34, "anchor": "ma", "font": FONT_REG, "color": INK},
    # 全身ターンアラウンドのラベル（Front / Side / Back）
    "view_labels":  {"y": 0.585, "xs": [0.19, 0.50, 0.81], "size": 26, "anchor": "ma", "font": FONT_REG, "color": INK},
    # 表情ラベル（下段5つ）
    "expr_labels":  {"y": 0.955, "xs": [0.075, 0.235, 0.395, 0.545, 0.70], "size": 20, "anchor": "ma", "font": FONT_REG, "color": INK},
    # 右下のキャラ情報ブロック
    "info":         {"xy": (0.605, 0.625), "size": 19, "leading": 1.32, "font": FONT_REG, "color": INK, "width_px": 560},
    # 左上ロゴ（画像があれば logo で差し込む。無ければテキスト）
    "logo_text":    {"xy": (0.015, 0.015), "size": 40, "anchor": "la", "font": FONT_BOLD, "color": (233, 30, 140)},
    # 右下フッター
    "footer":       {"xy": (0.985, 0.985), "size": 14, "anchor": "rd", "font": FONT_REG, "color": MUTED},
}

ELENA_DEMO = {
    "title": "Elena Bloom Character Sheet",
    "views": ["Front", "Side", "Back"],
    "expressions": ["Normal", "Happy", "Shy", "Surprised", "Thinking"],
    "info": [
        "Character: Elena Bloom.",
        "Visual: Pink twin-tails with ribbons and roses, large pink/magenta eyes, "
        "white and pink idol dress with gold trim.",
        "Personality: Center of AiCuty. Hardworking but shy. Influencer & visual specialist.",
        "Instrument: Lead Vocal.",
        "Style: Chibi, 2-3 head proportions.",
    ],
    "logo": "AiCuty",
    "footer": "© AICU Inc. / AICU JAPAN",
}


def font(path, size):
    try:
        return ImageFont.truetype(path, size)
    except Exception:
        return ImageFont.truetype(FONT_REG, size)


def wrap(draw, text, fnt, max_w):
    words, lines, cur = text.split(" "), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def compose(art_path, data, out_path):
    im = Image.open(art_path).convert("RGB")
    W, H = im.size
    d = ImageDraw.Draw(im)

    def place(cfg, text):
        d.text((cfg["xy"][0] * W, cfg["xy"][1] * H), text,
               font=font(cfg["font"], cfg["size"]), fill=cfg["color"], anchor=cfg.get("anchor", "la"))

    place(LAYOUT["title"], data["title"])
    place(LAYOUT["logo_text"], data.get("logo", "AiCuty"))
    place(LAYOUT["footer"], data.get("footer", "© AICU Inc."))

    for x, label in zip(LAYOUT["view_labels"]["xs"], data["views"]):
        c = LAYOUT["view_labels"]
        d.text((x * W, c["y"] * H), label, font=font(c["font"], c["size"]), fill=c["color"], anchor=c["anchor"])
    for x, label in zip(LAYOUT["expr_labels"]["xs"], data["expressions"]):
        c = LAYOUT["expr_labels"]
        d.text((x * W, c["y"] * H), label, font=font(c["font"], c["size"]), fill=c["color"], anchor=c["anchor"])

    # 情報ブロック（自動折り返し）
    ic = LAYOUT["info"]
    fnt = font(ic["font"], ic["size"])
    x0, y = ic["xy"][0] * W, ic["xy"][1] * H
    lh = int(ic["size"] * ic["leading"])
    for para in data["info"]:
        for line in wrap(d, para, fnt, ic["width_px"]):
            d.text((x0, y), line, font=fnt, fill=ic["color"], anchor="la")
            y += lh

    im.save(out_path)
    print(f"[ok] {out_path} ({W}x{H})")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--art", required=True)
    ap.add_argument("--data", help="character JSON (省略時 Elena デモ)")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    data = json.loads(Path(a.data).read_text()) if a.data else ELENA_DEMO
    compose(a.art, data, a.out)
