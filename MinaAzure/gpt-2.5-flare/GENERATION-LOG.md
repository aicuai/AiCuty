# Mina Azure — gpt-2.5-flare 生成台帳

**参照画像は API 収益とロイヤリティに直結します。何をどう生成したか追えない画像を公式素材にしないでください。**
（[MarshaArancia/GENERATION-LOG.md](../../MarshaArancia/GENERATION-LOG.md) の方式を踏襲）

`gpt-image-2.5-flare` に seed はありません。再現性は「プロンプト＋参照画像＋採用した出力」の三点で担保します。

## 採用した生成物

| 出力 | カット | サイズ | quality | AP | プロンプト | 生成日 |
|---|---|---|---|---|---|---|
| （未生成） | | | | | | |

## 没にした生成物

| 出力 | カット | 没の理由 |
|---|---|---|
| （なし） | | |

## 生成コマンド

```bash
export AICU_API_KEY=...   # images スコープが必要
python3 bench/aicu-api/gen_aicu.py \
  --model gpt-image-2.5-flare --quality medium \
  --prompt-file MinaAzure/gpt-2.5-flare/prompts/01-standing-front.txt \
  --label MinaAzure-01-standing-front
```

AP の目安は 1024x1024 / medium = **1,600 AP**、1536x1024 / medium = **2,300 AP**（2026-09-21 実測）。
1 キャラ 7 カットで **約 12,700 AP**、6 キャラで **約 76,000 AP** です。
