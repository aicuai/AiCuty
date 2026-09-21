# Mei Soleil — gpt-2.5-flare 生成台帳

**参照画像は API 収益とロイヤリティに直結します。何をどう生成したか追えない画像を公式素材にしないでください。**
（[MarshaArancia/GENERATION-LOG.md](../../MarshaArancia/GENERATION-LOG.md) の方式を踏襲）

`gpt-image-2.5-flare` に seed はありません。再現性は「プロンプト＋参照画像＋採用した出力」の三点で担保します。

## 生成条件（全カット共通）

| 項目 | 値 |
|---|---|
| モデル | `gpt-image-2.5-flare` |
| quality | `medium` |
| 参照画像 | [`MeiSoleil.png`](../MeiSoleil.png)（公式シート・`V20260113` / `CHECKED_BY_HAKASE`） |
| 生成日 | 2026-09-21 |
| 経路 | `https://api.aicu.ai/v1/images/generations`（AP はレスポンスの `X-AICU-AP-Cost` の実値） |

## 生成物

| 出力 | サイズ | AP | 生成時間 | プロンプト | 判定 |
|---|---|---|---|---|---|
| [out/01-standing-front.jpg](out/01-standing-front.jpg) | 1024x1024 | 1,600 | 23.7 s | [01-standing-front.txt](prompts/01-standing-front.txt) | ✅ 採用 |
| [out/02-standing-side.jpg](out/02-standing-side.jpg) | 1024x1024 | 1,600 | 16.5 s | [02-standing-side.txt](prompts/02-standing-side.txt) | ✅ 採用 |
| [out/03-standing-back.jpg](out/03-standing-back.jpg) | 1024x1024 | 1,600 | 20.2 s | [03-standing-back.txt](prompts/03-standing-back.txt) | ✅ 採用 |
| [out/04-bust-up.jpg](out/04-bust-up.jpg) | 1024x1024 | 1,600 | 19.4 s | [04-bust-up.txt](prompts/04-bust-up.txt) | ✅ 採用 |
| [out/05-eyes-closeup.jpg](out/05-eyes-closeup.jpg) | 1024x1024 | 1,600 | 40.6 s | [05-eyes-closeup.txt](prompts/05-eyes-closeup.txt) | ⚠️ **要再生成** |
| [out/06-accessories.jpg](out/06-accessories.jpg) | 1536x1024 | 2,300 | 18.0 s | [06-accessories.txt](prompts/06-accessories.txt) | ✅ 採用（逸脱あり） |
| [out/07-expressions.jpg](out/07-expressions.jpg) | 1536x1024 | 2,300 | 18.4 s | [07-expressions.txt](prompts/07-expressions.txt) | ✅ 採用（逸脱あり） |

**計 12,600 AP。**

## 受け入れ基準に照らした確認

[規格](../../docs/CHARACTER-SHEET-STANDARD.md)の 8 項目です。

| # | 基準 | 結果 |
|---|---|---|
| 1 | 公式シートと同じ頭身（ちび 2-3 頭身） | ✅ **7 カットすべて** |
| 2 | NG 事項に抵触していない | ✅ サイドポニー／星のヘアピン／スカート下のショートパンツ／そばかす、すべて再現 |
| 3 | 手指が正しい | ✅ 破綻なし |
| 4 | 全身が見切れていない | ✅ |
| 5 | 背景が白・文字の写り込みなし | ✅ |
| 6 | 01〜05 で同一人物に見える | ✅ |
| 7 | 既存の公式シートと並べて同じキャラに見える | ✅ 背面の王冠エンブレムまで一致 |
| 8 | プロンプト・参照・出力が追跡できる | ✅ この台帳 |

**参照画像と「ちび 2-3 頭身」の明示を、両方入れた効果が出ています。**
どちらか一方だけでは 8 頭身または 6〜7 頭身になることを事前に確認済みです
（[規格](../../docs/CHARACTER-SHEET-STANDARD.md)の「公式デザインを再現する条件」）。

> **この判定は自動採点ではなく、人の目で公式シートと並べて確認したものです。**
> CEO にも一覧シートを送って確認を依頼しています（2026-09-21）。

## 逸脱・要再生成

### ⚠️ 05-eyes-closeup — 要再生成

**目元だけのアップ**を指示したが、**全身 ＋ 小さな目元のインセット**になった。
瞳のハイライト・まつ毛・目の形を確認する資料としては、インセットが小さすぎる。

- 次の手: プロンプトから全身を誘発する語を外し、`extreme close-up` をさらに強調する。
  それでも直らなければ、04-bust-up をトリミングして代用する
- 生成時間が **40.6 秒**と他カットの 2 倍かかっている。構図に迷った可能性がある

### 06-accessories — 採用（逸脱あり）

`no full figure` と指示したが、**左端に全身が入った**。ただし装飾品の内訳
（髪・ポニーテール・星ピン・リボン・ジャケット・クロップトップ・スカート・カラビナ・
スニーカー・袖）は要求どおり個別に並んでおり、**資料としての価値は損なわれていない**ため採用。

### 07-expressions — 採用（逸脱あり）

**5 表情（Normal / Happy / Shy / Surprised / Thinking）**を指示したが、
**上段に全身 3 カット、下段に 5 表情**という構成になった。下段は公式シートと同じ並び・同じ表情で、
上段は余分だが害がないため採用。次回は「顔のみ・1 行」をより強く指定する。

## 没にした生成物

| 出力 | 没の理由 |
|---|---|
| （今回なし） | 7 カットとも受け入れ基準 1〜8 を満たした。05 のみ目的を果たしていないため要再生成 |

## 再現コマンド

```bash
export AICU_API_KEY=...   # images スコープが必要

for f in 01-standing-front 02-standing-side 03-standing-back 04-bust-up 05-eyes-closeup; do
  python3 bench/aicu-api/gen_aicu.py --model gpt-image-2.5-flare --quality medium --size 1024x1024 \
    --prompt-file MeiSoleil/gpt-2.5-flare/prompts/$f.txt \
    --reference MeiSoleil/MeiSoleil.png --label "Mei-$f"
done
for f in 06-accessories 07-expressions; do
  python3 bench/aicu-api/gen_aicu.py --model gpt-image-2.5-flare --quality medium --size 1536x1024 \
    --prompt-file MeiSoleil/gpt-2.5-flare/prompts/$f.txt \
    --reference MeiSoleil/MeiSoleil.png --label "Mei-$f"
done
```

AP の目安は 1024x1024 / medium = **1,600 AP**、1536x1024 / medium = **2,300 AP**。
1 キャラ 7 カットで **12,600 AP**、6 キャラで **約 76,000 AP** です。
