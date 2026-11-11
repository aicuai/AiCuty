# Saki Noire — gpt-2.5-flare 生成台帳

**参照画像は API 収益とロイヤリティに直結します。何をどう生成したか追えない画像を公式素材にしないでください。**

`gpt-image-2.5-flare` に seed はありません。再現性は「プロンプト＋参照画像＋採用した出力」の三点で担保します。

## 生成条件（全カット共通）

| 項目 | 値 |
|---|---|
| モデル | `gpt-image-2.5-flare` |
| quality | `medium` |
| 参照画像 | [`SakiNoire.png`](../SakiNoire.png)（公式シート・`V20260113` / `CHECKED_BY_HAKASE`） |
| 生成日 | 2026-09-22 |
| 経路 | `https://api.aicu.ai/v1/images/generations`（AP は `X-AICU-AP-Cost` の実値） |

## 生成物

| 出力 | サイズ | AP | 生成時間 | プロンプト | 判定 |
|---|---|---|---|---|---|
| [out/01-standing-front.jpg](out/01-standing-front.jpg) | 1024x1024 | 1,600 | 15.9 s | [01-standing-front.txt](prompts/01-standing-front.txt) | ✅ 採用 |
| [out/02-standing-side.jpg](out/02-standing-side.jpg) | 1024x1024 | 1,600 | 14.6 s | [02-standing-side.txt](prompts/02-standing-side.txt) | ✅ 採用 |
| [out/03-standing-back.jpg](out/03-standing-back.jpg) | 1024x1024 | 1,600 | 15.7 s | [03-standing-back.txt](prompts/03-standing-back.txt) | ✅ 採用 |
| [out/04-bust-up.jpg](out/04-bust-up.jpg) | 1024x1024 | 1,600 | 15.4 s | [04-bust-up.txt](prompts/04-bust-up.txt) | ✅ 採用 |
| [out/05-eyes-closeup.jpg](out/05-eyes-closeup.jpg) | 1024x1024 | 1,600 | 17.2 s | [05-eyes-closeup.txt](prompts/05-eyes-closeup.txt) | ✅ 採用（逸脱あり） |
| [out/06-accessories.jpg](out/06-accessories.jpg) | 1536x1024 | 2,300 | 17.8 s | [06-accessories.txt](prompts/06-accessories.txt) | ✅ 採用（逸脱あり） |
| [out/07-expressions.jpg](out/07-expressions.jpg) | 1536x1024 | 2,300 | 15.9 s | [07-expressions.txt](prompts/07-expressions.txt) | ✅ 採用（逸脱あり） |

**計 12,600 AP。**

## 受け入れ基準に照らした確認

| # | 基準 | 結果 |
|---|---|---|
| 1 | 公式シートと同じ頭身（ちび 2-3 頭身） | ✅ 7 カットすべて |
| 2 | NG 事項に抵触していない | ✅ **前髪は左目にかかっている**／ボブの毛先は内巻きでない／瞳はアメジストパープル |
| 3 | 手指が正しい | ✅ 破綻なし（手袋つきの指も含む） |
| 4 | 全身が見切れていない | ✅ |
| 5 | 背景が白・文字の写り込みなし | ✅ |
| 6 | 01〜05 で同一人物に見える | ✅ |
| 7 | 既存の公式シートと並べて同じキャラに見える | ✅ オフショルダー・紫のサイハイ・厚底ブーツまで一致 |
| 8 | プロンプト・参照・出力が追跡できる | ✅ この台帳 |

> **この判定は自動採点ではなく、人の目で公式シートと並べて確認したものです。**
> CEO にも一覧シートを送って確認を依頼しています（2026-09-22）。

## 逸脱

### 05-eyes-closeup — 採用（Mei より良い）

指示は「目元だけのアップ」だが、**全身 ＋ 目元のインセット**になった。
ただし [Mei の同カット](../../MeiSoleil/gpt-2.5-flare/GENERATION-LOG.md)と違い、
**インセットが十分に大きく、瞳の色・ハイライト・まつ毛・目の形が読み取れる**ので採用。

同じプロンプトでもキャラによって構図の寄り方が変わる、という実例になった。

### 06-accessories / 07-expressions — 採用（逸脱あり）

Mei と同じく、`no full figure` と指示しても全身が 1 体入る。
装飾品（イヤリング・手袋・ベルト・サイハイ・ブーツ・リボン）と
5 表情（Normal / Happy / Shy / Surprised / Thinking）は要求どおり揃っているので採用。

**2 キャラで同じ逸脱が出たので、プロンプト側の癖**と判断できる。
次に直すならここ（`no full figure` がこのモデルに効かない）。

## 没にした生成物

| 出力 | 没の理由 |
|---|---|
| （今回なし） | 7 カットとも受け入れ基準 1〜8 を満たした |

## 再現コマンド

```bash
export AICU_API_KEY=...   # images スコープが必要

for f in 01-standing-front 02-standing-side 03-standing-back 04-bust-up 05-eyes-closeup; do
  python3 bench/aicu-api/gen_aicu.py --model gpt-image-2.5-flare --quality medium --size 1024x1024 \
    --prompt-file SakiNoire/gpt-2.5-flare/prompts/$f.txt \
    --reference SakiNoire/SakiNoire.png --label "Saki-$f"
done
for f in 06-accessories 07-expressions; do
  python3 bench/aicu-api/gen_aicu.py --model gpt-image-2.5-flare --quality medium --size 1536x1024 \
    --prompt-file SakiNoire/gpt-2.5-flare/prompts/$f.txt \
    --reference SakiNoire/SakiNoire.png --label "Saki-$f"
done
```
