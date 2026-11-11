# Elena Bloom — gpt-image-2.5-flare 用リファレンス

`gpt-image-2.5-flare` に渡すための、Elena Bloom（エレナ・ブルーム）のキャラクターリファレンス一式です。
規格は [../../docs/CHARACTER-SHEET-STANDARD.md](../../docs/CHARACTER-SHEET-STANDARD.md)。

| 項目 | 内容 |
|---|---|
| 名前 | Elena Bloom / エレナ・ブルーム |
| メンバーカラー | ピンク |
| 正本 | [../README.md](../README.md) |

## 体型（最重要）

**ちび 2〜3 頭身。** 公式シートに `Style: Chibi, 2-3 head proportions` と明記されています。
参照画像を渡すだけでは頭身が移らず、プロンプトにも明示が必要です（2026-09-21 実測）。

> **参照画像は必ず `ElenaBloom/ElenaBloom.png`（AICU 公式キャラクターシート・`V20260113` / `CHECKED_BY_HAKASE`）を渡します。**
> 参照画像なしで生成したものを公式素材にしないでください。

## 外見の核（変えてはいけない部分）

- ピンク色のツインテール
- 両側の結び目に髪飾り
- 前髪にピン
- 大きなピンク／マゼンタの瞳
- 白とピンクを基調に金のトリムを入れたアイドルドレス

## NG 事項

- ツインテールを他の髪型にしない
- 瞳の色をピンク／マゼンタ以外にしない
- ドレスの金のトリムを省略しない

## 必要なカット

| ファイル | カット | サイズ | 確認できること |
|---|---|---|---|
| `prompts/01-standing-front.txt` | 立ち絵 正面（基準） | 1024x1024 | 全身が見切れない・白背景・直立に近いポーズ |
| `prompts/02-standing-side.txt` | 立ち絵 側面 | 1024x1024 | 髪の長さと衣装の構造が横から分かること |
| `prompts/03-standing-back.txt` | 立ち絵 背面 | 1024x1024 | 背面デザインと後ろ髪が分かること |
| `prompts/04-bust-up.txt` | バストアップ | 1024x1024 | 顔立ち・首まわり・肩まわり・前髪の分かれ方 |
| `prompts/05-eyes-closeup.txt` | 目元のアップ | 1024x1024 | 瞳の色・ハイライト・まつ毛・目の形 |
| `prompts/06-accessories.txt` | 装飾品の個別アップ | 1536x1024 | 髪飾り・靴・エンブレム等を個別に（2,300 AP） |
| `prompts/07-expressions.txt` | 表情差分（5 種） | 1536x1024 | **公式シートと同じ** Normal / Happy / Shy / Surprised / Thinking |

## プロンプトの構成（三段構成）

`prompts/00-base-fixed.txt` が**固定の土台**、各カットのファイルは土台＋**見せ方**だけを足したものです。
> ⚠️ **この土台は README のビジュアル記述から起こした暫定版です。**
> このキャラクターの正本プロンプトはリポジトリに残っていません（`bench/prompts/` にあるのは Mei と Saki のみ）。
> **デザイン担当の確認を受けてから確定**してください。

外見を直すときは **`00-base-fixed.txt` だけを直し、全カットを再生成**してください。
カット側のファイルを個別にいじると、どこで見た目が変わったのか追えなくなります。

## 受け入れ基準

[../../docs/CHARACTER-SHEET-STANDARD.md](../../docs/CHARACTER-SHEET-STANDARD.md) の「受け入れ基準」を満たすこと。
採用・不採用は [GENERATION-LOG.md](GENERATION-LOG.md) に理由まで記録します。
