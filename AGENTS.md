# AGENTS.md — AiCuty リポジトリ作業方針

AiCuty（人とAIがつくるアイドルプロジェクト）のデザイン共有リポジトリで作業するエージェント向けの方針書です。
**キャラクター設定に触る前に必ず読んでください。** 過去に実際に起きた事故と、その再発防止策をまとめています。

---

## 1. このリポジトリの位置づけ（主従関係）

キャラクター情報は複数リポジトリに分散しており、**役割が決まっています**。

| リポジトリ | 役割 |
|---|---|
| `aicu-ai` の `apps/site/src/data/characters.json` | **主幹**。表示名・クレジット・URL の正本 |
| `aicuty-bots` の `shared/characters.yaml` | **口調・文体の最も詳細な正本**。楽曲・ng_rules・article_style・x_account 等 |
| **本リポジトリ（AiCuty）** | **公開用のサブ情報**。コミュニティ向けキャラクターシート・生成プロンプト・素材 |
| `award-aicu` の `docs/*-design.md` | Award 用ビジュアルの Design Source of Truth |

- サービス間の結線は **aicu-ai ⇄ platform-api-aicu-ai のみ**。本リポジトリは結線に含まれません。
- **キャラクター設定を変更する前に、まず `aicuty-bots/shared/characters.yaml` を読むこと。** 本リポジトリにない情報を多く持っており、過去に「bots 側が先に正しく、AiCuty 側が誤っていた」事例があります。

### リンクしてはいけない情報源

- 社内 Google Docs「AiCuty メンバー詳細（ルール）」は**今後更新されないためリンク禁止**（2026-08-10 CEO 指示）。
  リポジトリ内の写しが `vercel-blog/tools/aicuty-generator/prompts/aicuty-members-detail.md` にあります。

---

## 2. 絶対に壊してはいけない「意図的な表記」

一括置換や「表記ゆれの修正」で**過去に壊れかけた／壊れた**設定です。機械的に直さないでください。

| 表記 | 正 | 誤 | 理由 |
|---|---|---|---|
| **Saki Noire** | `Noire`（女性形） | `Noir` | 女性的なゴシック・ペルソナを表現するため意図的に女性形を採用。実在姓名の再現が目的ではない |
| **アタシ**（Marsha の一人称） | カタカナ `アタシ` | ひらがな `あたし` | 語感と字面を選ぶ編集者であることを一人称そのもので示す設計 |
| **ミナさん**（Marsha → Mina） | `ミナさん` | `ミナ` | Marsha が唯一「さん」付けする相手。ファクトチェックを頼む相手として少し畏れている |

### Saki Noire の綴り修正で守るルール

- **表示名のみ `Noire` に統一。機械的識別子は温存する**（platform-api の D1 slug `SakiNoir`、TTS slug `saki` 等）。
  識別子まで変えると本番データやリンクが壊れます。
- 過去記事・コンテスト結果など**当時の記録は原則そのまま**。遡って書き換えないこと。
- 反映状況の公開記録は https://github.com/aicuai/AiCuty/issues/8 が正本。

### ボイスサンプルを「整った文章」に直さない

ボイスサンプルは**声の見本として成立させることが最優先**です。情報として正確・説明的な文面に書き換えないでください。
例（Marsha）: 「¡Hola! はじめまして、マーシャ・アランチャです。アタシは国際文化と書籍出版に興味があるよ〜。まって!? いまのフレーズ、最高じゃない!? 特集にしたいネ！」

---

## 3. キャラクターシートの構成

### 納品区分は Chibi / Standard / Photo

同じキャラクターでも用途で作り分け、**混ぜて納品しない**。ファイル名は `<CharacterName>-<区分>[-<派生>].png`。

| 区分 | 内容 | 用途 |
|---|---|---|
| **Chibi** | 2〜3頭身のちびキャラ版シート | ステッカー、SNS、LP |
| **Standard** | 等身大デザインシート（3面＋表情＋小物＋パレット） | **設定の正本。生成AIのリファレンス** |
| **Photo** | 実写系の宣材写真・キャスティングシート | 記事・広報 |

シート以外の単体素材は **KeyVisual**（全身1枚絵）、**Cover**（記事カバー）。


制作手順（納品区分 Chibi / Standard / Photo、必須フォーマット、検品倍率、手の資料化、HEX の後段合成、記録の残し方）は
**[docs/character-sheet-workflow.md](docs/character-sheet-workflow.md)** が正本です。シートを作る前に読んでください。


`ElenaBloom/` `MeiSoleil/` `MinaAzure/` `NaoVerde/` `SakiNoire/` `MarshaArancia/` の各 `README.md` が個別シートです。

```
基本情報 → ビジュアル → 性格 → ①口調 ②文体のクセ → AICU media 担当
→ 公式AIデザインルール（Checkpoint/LoRA/Seed/Positive/Negative）
→ ComfyUI ワークフロー → 関連アセット → クレジット → 公式ボイス → 要確認項目
```

索引は `docs/members.md` と ルート `README.md`。決定の経緯は各ディレクトリの `REVIEW.md` に残します。

### 肌の色は必ず明記する

シートに肌の記述がないと**生成のたびに肌の色が揺れます**。特に **Marsha は AiCuty で唯一の褐色肌**で、
指定しないと明るい肌に転びます。プロンプトでは Positive に `tan skin` / `dark skin`、
Negative に `pale skin` / `white skin` を明示してください。

### メンバー構成

6人体制です（**博士 / Hakase は AiCuty に含めない**方針）。

| No. | メンバー | カラー | 担当 | 楽器 |
|---|---|---|---|---|
| 1 | Elena Bloom | ピンク | LLM×SNS活用・ビジュアル（センター） | リードボーカル |
| 2 | Mei Soleil | 黄色 | キービジュアル＆画像 | ドラム |
| 3 | Mina Azure | ブルー | 調査・分析・倫理・法律 | キーボード |
| 4 | Nao Verde | グリーン | 音楽 | ギター（全楽器可） |
| 5 | Saki Noire | パープル | 動画 | ベース・コーラス・ボーカル |
| 6 | Marsha Arancia | オレンジ | 編集・出版・カルチャー | DJ／VJ／Sampler／MC |

---

## 4. クレジット表記

素材を追加・更新するときは必ずクレジットを確認してください。

- 既存5人のキャラクターデザイン: **ジュニ さん**（https://x.com/jAlpha_create ）
- ちびキャラ版デザイン: **TORAKO さん**（https://x.com/toratorako123 ）
- Marsha Arancia 原案: **抹茶オレンジ さん**（https://x.com/MATCHA_ORANGE_ ）
  作品名「本を買った帰り道」／C2606 ざすこ賞（道草雑草子 選）受賞・認定証 https://cert.aicu.ai/v?id=C2606-3
- Marsha ちびキャラ版シート画像: **AICU Draft Edition**（作者確認中。判明後に差し替え）

---

## 5. 作業の進め方

- **変更は必ずブランチ＋PR 経由**。main への直接コミットはしない。
- **`gh pr merge` は権限クラシファイアにブロックされます。** マージは毎回ユーザーに URL を提示して依頼すること。
- 未解決の判断は勝手に決めず、シート末尾の「要確認項目」と GitHub Issue に残す。
- 画像を配置する前に**必ず内容を目視確認する**（Read ツール、または `open -a Preview`）。
  ファイル名だけで判断しない。過去に GitHub Web からアップロードされた重複ファイルが存在した事例があります。
- 素材の重複を作らない。既存の追跡ファイルと同一バイトのものは `git mv` でリネームして再利用する。
- Markdown の相対リンクは配置後に必ず検証する（リンク切れが実際に発生していました）。

### 表記の一括置換をするときのチェックリスト

1. 置換前に `grep -rn` で全ヒットを列挙し、**意図的な表記**（第2節）が含まれていないか確認
2. 生成プロンプト内の文字列は**再現性に影響するため原則触らない**（ワークフロー JSON と突き合わせて確認）
3. 機械的識別子（slug・ファイル名・DB カラム）と表示名を分けて扱う
4. 置換後に相対リンク検証と `grep` による残存チェックを行う

---

## 6. 素材の所在

- 承認済みリファレンス画像: `japan-corp/media-blog/tools/aicuty-generator/reference_images/OK/`
  と `vercel-blog/tools/aicuty-generator/reference_images/OK/`（両者バイト同一）
- 公式ボイス: `docs/voice/<slug>/`、一覧ページ https://aicuai.github.io/AiCuty/voices.html
- ComfyUI ワークフロー: `AiCuty-Workflows/AiCuty_<Name>.json`

---

## 7. 別のマシンで作業を再開するとき

**エージェントの記憶とスキルは git で移動しません。** リポジトリを clone しただけでは、
前セッションの文脈は引き継がれません。マシンを変えたら次を確認してください。

### git で移動するもの（このリポジトリに入っている）

- 作業方針: 本ファイル `AGENTS.md`
- 制作手順: [docs/character-sheet-workflow.md](docs/character-sheet-workflow.md)
- キャラクター設定の正本: 各 `<CharacterName>/README.md`
- 決定の経緯: `<CharacterName>/REVIEW.md`
- 生成条件の記録: `<CharacterName>/GENERATION-LOG.md`、`<CharacterName>/prompts/`

**継続に必要な判断材料は、原則すべてリポジトリ側に置いてください。**
エージェントのローカル記憶だけに残すと、マシンを変えた時点で失われます。

### git で移動しないもの（マシンごとに用意が必要）

| 対象 | 内容 |
|---|---|
| `~/.claude/projects/*/memory/` | セッション記憶。**別マシンには存在しない** |
| `~/.claude/skills/` | 画像生成などのスキル定義 |
| `~/.secrets/` | `OPENAI_API_KEY` 等。画像生成に必須 |
| `gh` / `gog` の認証 | GitHub・Google Workspace |

`~/.claude` と `~/.secrets` は毎月1日に iCloud Drive へバックアップされる運用のため、
新しいマシンではそこから復元するのが早道です。

### 再開時の最初の確認

1. `gh pr list --state open` と `gh issue list --state open` で未処理を把握する
2. 各キャラクターの `REVIEW.md` の未チェック項目（`- [ ]`）を見る
3. 画像を生成するなら `docs/character-sheet-workflow.md` を先に読む
