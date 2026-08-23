# Marsha Arancia 生成台帳（シード・プロンプト管理）

生成物の再現に必要な条件を記録します。**参照画像は API 収益とロイヤリティに直結するため、
何をどう生成したかを追えない画像を公式素材にしないでください。**

---

## 1. gpt-image-2（`images.edit`）

**gpt-image-2 には seed パラメータがありません。** 同一プロンプト・同一参照でも出力は毎回変わるため、
再現性の担保は「プロンプト＋参照画像＋採用した出力」の三点セットを固定することで行います。
プロンプトは必ず [prompts/](prompts/) に保存し、採用した出力だけをリポジトリに残します。

| 出力 | サイズ | quality | プロンプト | 参照画像 | 生成日 |
|---|---|---|---|---|---|
| [MarshaArancia-DesignSheet.png](MarshaArancia-DesignSheet.png) | 1536x1024 | high | [platform-api-designsheet-prompt.txt](prompts/platform-api-designsheet-prompt.txt) | MarshaArancia-FullBody.png | 2026-08-24 |
| [MarshaArancia-PlatformRef.png](MarshaArancia-PlatformRef.png) | 1024x1536 | high | [platform-api-reference-prompt.txt](prompts/platform-api-reference-prompt.txt) | MarshaArancia-FullBody.png | 2026-08-23 |
| [MarshaArancia-Photo-Headshot.png](MarshaArancia-Photo-Headshot.png) | 1024x1536 | high | [photo-headshot-prompt.txt](prompts/photo-headshot-prompt.txt) | MarshaArancia-Photo-Hero.png ＋ MarshaArancia-FullBody.png | 2026-08-23 |
| [MarshaArancia-Illustration-Reference.png](MarshaArancia-Illustration-Reference.png) | 1024x1024 | high | [illustration-reference-prompt.txt](prompts/illustration-reference-prompt.txt) | MarshaArancia-FullBody.png | 2026-08-23 |
| [MarshaArancia-Cover-AICUStudy.png](MarshaArancia-Cover-AICUStudy.png) | 1536x1024→1910x1000 | high | [cover-aicu-study-prompt.txt](prompts/cover-aicu-study-prompt.txt) | MarshaArancia-FullBody.png ＋ MarshaArancia-Original.png | 2026-08-23 |
| [MarshaArancia-Photo-Hero.png](MarshaArancia-Photo-Hero.png) | 1024x1536 | high | [photo-hero-prompt.txt](prompts/photo-hero-prompt.txt) | award-aicu 由来 | — |
| [MarshaArancia-Photo-Sheet.png](MarshaArancia-Photo-Sheet.png) | 1536x1024 | high | [photo-sheet-prompt.txt](prompts/photo-sheet-prompt.txt) | award-aicu 由来 | — |
| [MarshaArancia-FullBody.png](MarshaArancia-FullBody.png) | 1536x1024 | high | [character-sheet-prompt.txt](prompts/character-sheet-prompt.txt) | award-aicu 由来 | — |

### 没にした生成物

| 出力 | 没の理由 |
|---|---|
| カバーアート第1稿（招くポーズ） | **差し出した手の指が4本**に見える破綻 |
| カバーアート第2稿（両手で誌面を掲げる） | 誌面の縁越しに指先3本＋親指で、同じく4本に見える曖昧さ |
| `MarshaArancia-Cover-AICUStudy-full.png` | ボディの造形が不十分 |

**教訓: 開いた手のひらは必ず破綻します。** 手はポケット・ZINE の後ろ・フレーム外に逃がし、
プロンプトに「指を描画しない」を明記すること。生成後は必ず手の領域を3〜5倍に拡大して検品する。

---

## 2. ComfyUI（SDXL）Seed

既存5人は各シートに Seed を持ちますが、**Marsha はまだ未策定**です（[Issue #16](https://github.com/aicuai/AiCuty/issues/16)）。

| メンバー | Seed |
|---|---|
| Elena Bloom | 798458095628920 |
| Mina Azure | 798458095628920（Elena と共通・意図的） |
| Mei Soleil | 23255246635205 |
| Nao Verde | 23255246635273 |
| Saki Noire | 23255246635292 |
| **Marsha Arancia** | **未策定** |

策定時は `23255246635xxx` 系列で採番し、確定した Seed・Checkpoint・LoRA・Positive / Negative を
[README.md](README.md) の「公式AIデザインルール」節と本台帳の両方に記録してください。
**褐色肌の明示（Positive: `tan skin` / Negative: `pale skin`）は必須**です。

---

## 3. リファレンス画像の方針

**キャラクターリファレンスは「デザインシート」を本命とします。** 全身1枚では複数視点・表情を参照できず、
別アングルや別表情を生成させたときに破綻します。

| 用途 | 使うもの |
|---|---|
| API のキャラクター参照 | [MarshaArancia-DesignSheet.png](MarshaArancia-DesignSheet.png)（3面＋表情5種＋小物） |
| キーヴィジュアル・記事カバー | [MarshaArancia-PlatformRef.png](MarshaArancia-PlatformRef.png) 等の全身1枚 |
| 公式設定シート（人間が読む用） | [MarshaArancia-FullBody.png](MarshaArancia-FullBody.png)（ラベルつき） |

デザインシートを作るときの必須条件。

- **文字ラベルを入れない。** 参照画像に読めない文字が入ると、生成物に garbled text が混入する
- **全パネルで褐色肌を維持**する
- **全パネルで手を袖・物の後ろに隠す**
- 3面は同じスケール・同じ目線高さで揃える

## 4. 記録のルール

新しく公式素材を生成したら、次を必ず残します。

1. プロンプト全文を `prompts/<用途>-prompt.txt` に保存
2. 本台帳の表に 出力ファイル・サイズ・quality・プロンプト・参照画像・生成日 を追記
3. 没にした場合は理由とともに「没にした生成物」へ記録（同じ失敗を繰り返さないため）
4. ComfyUI 系は Seed を必ず併記
