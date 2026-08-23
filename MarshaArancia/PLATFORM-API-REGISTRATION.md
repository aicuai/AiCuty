# Marsha Arancia — platform-api キャラクター登録の準備

`platform-api-aicu-ai` へ Marsha Arancia を登録するための素材とメモです。
関連 Issue: [#17 Marsha を aicuty-bots / aicu-ai のキャラクターデータに登録する](https://github.com/aicuai/AiCuty/issues/17)

> ⚠️ **登録作業そのものは本リポジトリでは行いません。** platform-api への変更は必ず PR 経由で、本番 D1 への適用はユーザーが手動で実施する運用です（一般利用者のデータを破壊しないため）。

---

## 1. 現状

`https://api.aicu.ai/v1/images/characters` を実測したところ、**Marsha Arancia は未登録**です。

| slug | reference | size | original_author |
|---|---|---|---|
| ElenaBloom | true | 1024x1024 | AICU Inc. |
| MeiSoleil | true | 1024x1024 | AICU Inc. |
| MinaAzure | true | 1024x1024 | AICU Inc. |
| NaoVerde | true | 1024x1024 | AICU Inc. |
| SakiNoir | true | 1024x1024 | AICU Inc. |
| **MarshaArancia** | — | — | **未登録** |
| youkai | true | 1536x1024 | 殻尾・しらいはかせ |

分かったこと。

- **リファレンス画像は 1024x1024** が既存5人の標準
- slug は **CamelCase**（`MarshaArancia` が自然）
- `SakiNoir`（e 無し）は**機械的識別子として温存**する方針のため変更しない（[AGENTS.md](../AGENTS.md) 参照）
- **`original_author` は AICU 以外も設定可能**。`youkai` に「殻尾・しらいはかせ」の前例あり

---

## 2. 登録案

> **提案 PR: https://github.com/aicuai/platform-api-aicu-ai/pull/298**（未マージ）
>
> ⚠️ **`character_rights.original_author` は `royalty_pct`（40%・margin ベース）の支払先**です。
> AICU Inc. 以外を設定すると**ロイヤリティ支払いの対象が発生します**。技術判断ではなく事業判断のため、
> CEO 承認を得るまでマージしないでください。

```json
{
  "slug": "MarshaArancia",
  "name": "Marsha Arancia",
  "model": "gpt-image-2",
  "size": "1024x1024",
  "quality": "high",
  "reference": true,
  "rights": {
    "holder": "AICU Inc.",
    "original_author": "抹茶オレンジ (@MATCHA_ORANGE_)",
    "credit": "© AICU Inc. / Marsha Arancia — 原案: 抹茶オレンジ",
    "source_url": "https://aicu.ai/character/marsha_arancia"
  }
}
```

**`original_author` は要確認事項です。** Marsha の原案は外部クリエイターである抹茶オレンジさんのコンテスト受賞作（C2606 ざすこ賞、認定証 https://cert.aicu.ai/v?id=C2606-3 ）です。既存5人の `AICU Inc.` とは権利の経緯が異なるため、`youkai` の前例にならって原案者名を入れる案としています。**最終的な表記は権利まわりの判断が必要**なので、CEO 確認をお願いします。

`ap_cost` は既存の gpt-image-2 キャラクターに合わせるなら `6400` / `private_ap_cost` `12800` です。

---

## 3. 素材

### リファレンス画像（登録用・本命）

| ファイル | サイズ | 用途 |
|---|---|---|
| [MarshaArancia-PlatformRef.png](MarshaArancia-PlatformRef.png) | **1024x1536** | **platform-api 登録用**。既存5人と同体裁（縦・全身・世界観背景） |
| [MarshaArancia-Illustration-Reference.png](MarshaArancia-Illustration-Reference.png) | 1024x1024 | 白背景版。汎用リファレンス |

プロンプト: [prompts/platform-api-reference-prompt.txt](prompts/platform-api-reference-prompt.txt) ／ [illustration-reference-prompt.txt](prompts/illustration-reference-prompt.txt)

> **参照画像のサイズは 1024x1536（縦）です。** `GET /v1/images/characters` が返す `size: 1024x1024` は
> **出力サイズ**であり、参照画像の寸法ではありません。実体は `platform-api-aicu-ai` の
> `docs/character/*.png` にあり、既存5人はいずれも 1024x1536 の縦構図・世界観背景つき全身イラストです。

### 実写系フォト（宣材・営業写真）

| ファイル | サイズ | 用途 |
|---|---|---|
| [MarshaArancia-Photo-Headshot.png](MarshaArancia-Photo-Headshot.png) | 1024x1536 | **宣材バストアップ**。顔がはっきり分かる営業写真 |
| [MarshaArancia-Photo-Hero.png](MarshaArancia-Photo-Hero.png) | 1024x1536 | 全身ヒーローショット（award-aicu 由来） |
| [MarshaArancia-Photo-Sheet.png](MarshaArancia-Photo-Sheet.png) | 1536x1024 | キャスティングシート（HERO / FRONT / 3-4 / PROFILE / 表情 / 小物） |

プロンプト: [prompts/photo-headshot-prompt.txt](prompts/photo-headshot-prompt.txt) ／ [photo-hero-prompt.txt](prompts/photo-hero-prompt.txt) ／ [photo-sheet-prompt.txt](prompts/photo-sheet-prompt.txt)

> **実写版の Marsha は実在しない架空の人物**です。生成時に参照した人物写真はムードリファレンスとしてのみ使用しており、実在の人物を再現・特定してはなりません。プロンプトにもこの制約を明記しています。

### イラスト（既存）

| ファイル | サイズ | 用途 |
|---|---|---|
| [MarshaArancia-FullBody.png](MarshaArancia-FullBody.png) | 1536x1024 | 等身大キャラクターシート（カラーパレット付き） |
| [MarshaArancia.png](MarshaArancia.png) | 1672x941 | ちびキャラ版シート |
| [MarshaArancia-Original.png](MarshaArancia-Original.png) | 1023x1537 | 原案「本を買った帰り道」（抹茶オレンジ さん） |
| [MarshaArancia-Cover-AICUStudy.png](MarshaArancia-Cover-AICUStudy.png) | 1910x1000 | AICU STUDY 記事カバー |

プロンプト: [prompts/character-sheet-prompt.txt](prompts/character-sheet-prompt.txt)

---

## 4. 生成時の必須指定

すべてのプロンプトに共通で入れること。

- **褐色肌を明示する** — Positive に `warm medium-brown golden complexion` / `tan skin`、Negative に `pale skin` / `white skin`。**指定しないと明るい肌に転びます**
- 抹茶グリーンのショートボブ＋前髪と毛先のオレンジ、頭頂のアホ毛
- 黄緑色の瞳、オレンジ＆黒のヘッドホン、耳に挿した**赤鉛筆**（校正用）
- パッチだらけのオーバーサイズジャケット、ZINE の詰まった黒いバックパック
- **手を描かせない／物に隠す** — 開いた手のひらは指が破綻しやすいため、手はポケット・ZINE の後ろ・フレーム外に逃がす
- 文字・ロゴ・透かしを入れない

---

## 5. 未確定事項

- [ ] **`original_author` = 抹茶オレンジ 氏 の可否（ロイヤリティ 40% の支払先になる。CEO 承認必須）**
- [ ] 料率を既存キャラと同じ 40.0 にしてよいか
- [ ] `source_url` = `https://aicu.ai/character/marsha_arancia` のページを aicu-ai 側に用意する必要があるか
- [ ] リファレンス画像を `MarshaArancia-Illustration-Reference.png` で確定してよいか
- [ ] `ap_cost` / `private_ap_cost` を既存キャラと同額（6400 / 12800）にしてよいか
