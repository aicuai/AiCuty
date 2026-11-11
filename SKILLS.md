# SKILLS.md — 作業の種類ごとの手順と道具

AiCuty の素材や設定を扱うエージェント向けに、**「この作業はどの手順で、どの道具を使うか」**をまとめた索引です。
方針と禁止事項は [AGENTS.md](AGENTS.md) にあります。先にそちらを読んでください。

道具は 2 種類あります。

- **リポジトリに入っている手順とスクリプト** — clone すればどのマシンでも使えます
- **Claude Code のスキル**（`~/.claude/skills/<名前>/`）— マシンごとに入れるもので、**git では移動しません**。
  下の表の名前が自分の環境に無ければ、リポジトリ側の手順だけで進めてください

## 1. 設定を調べる・答える

| やりたいこと | 手順 |
|---|---|
| メンバーの外見・性格・口調を知る | `<CharacterName>/README.md` を読む。6 人の対応表は [AGENTS.md](AGENTS.md) 第 0 節 |
| 楽曲・NG ルール・記事の文体まで知る | `aicuty-bots/shared/characters.yaml` を読む（社内リポジトリ。口調の最も詳しい正本） |
| 表示名・クレジット・URL を確かめる | `aicu-ai` の `apps/site/src/data/characters.json`（主幹） |
| キャラクターの台詞や記事を書く | 書く直前に該当 README の「① 口調」「② 文体のクセ」を読む。AGENTS.md 第 2 節の表記を崩さない |

## 2. 画像をつくる

| やりたいこと | リポジトリの手順 | Claude Code のスキル |
|---|---|---|
| キャラクターシート（Chibi / Standard / Photo） | [docs/character-sheet-workflow.md](docs/character-sheet-workflow.md) | `gpt-image2` |
| GPT-Image-2.5 用リファレンス 7 カット | [docs/CHARACTER-SHEET-STANDARD.md](docs/CHARACTER-SHEET-STANDARD.md)、`<CharacterName>/gpt-2.5-flare/README.md` | `gpt-image2`、`aicu-api` |
| プロンプトからシートを再現生成する | `python3 scripts/generate_charsheet.py --prompt <プロンプト> --out <出力>`（先頭コメントに使い方） | — |
| シートの文字（HEX・ラベル）を後から載せる | `python3 scripts/compose_charsheet_text.py`。文字は画像生成に任せない | — |
| ロゴを載せる | [img/logo/](img/logo/) のファイルをそのまま使う。画像生成でロゴを描かせない | — |
| 6 人の集合キービジュアル | 参照は `img/anime/<slug>.png` と各公式シート | `gpt-image2` |
| 記事カバー・OGP | 参照は各 `<CharacterName>/<CharacterName>.png` | `cover-art`、`gpt-image2` |
| 週刊AICU のヘッダー（横長） | — | `aicu-newsletter-banner` |
| ComfyUI で生成する | `AiCuty-Workflows/AiCuty_<Name>.json`、README「公式AIデザインルール」 | — |

**どの経路でも守ること**

1. **公式シートを参照画像として渡す。** 参照なしの生成物を公式素材にしない
2. **体型を明示する。** 公式シートはちび 2〜3 頭身。参照画像だけでは頭身が移らない（2026-09-21 実測）
3. **肌の色を書く。** Marsha は褐色肌（Positive に `tan skin`、Negative に `pale skin`）
4. **生成後に拡大して検品する。** 手指・見切れ・文字の写り込み。破綻を隠して逃げず、作り直す
5. **プロンプト全文・参照画像・採用した出力を記録する**（`prompts/` と `GENERATION-LOG.md`）
6. 素材を置く前にクレジットを確かめる（AGENTS.md 第 4 節）

## 3. 画像生成を計測する（AiCutyBench）

| やりたいこと | 手順 |
|---|---|
| AICU API 経由で品質・時間・AP を測る | [bench/aicu-api/README.md](bench/aicu-api/README.md)。`gen_aicu.py` で生成、`vscore_aicu.py` で採点 |
| OpenAI に直接出して測る | `bench/gen_flare.py`・`bench/gen_sunburst.py`・`bench/quality_sweep.py`・`bench/vscore.py` |
| 過去の結果を見る | `bench/results/*.csv`、`bench/aicu-api/results.csv` |

- 必要な環境変数は `AICU_API_KEY`（images スコープ）または `OPENAI_API_KEY`。値は `~/.secrets/` に置き、出力やコミットに書かない
- `bench/aicu-api/out/` は生成物の一時置き場で、git に入りません。採用したカットだけを `<CharacterName>/gpt-2.5-flare/out/` に移します
- `bench/prompts/Mei.txt`・`Saki.txt` は 8 頭身の等身大プロンプトで、公式シート（ちび）とは別のデザインです。
  経緯は [docs/CHARACTER-SHEET-STANDARD.md](docs/CHARACTER-SHEET-STANDARD.md) の「既知の不整合」
- `bench/run_yield.sh` は 2026-09-12 に実行したときの記録で、パスが当時のマシンのままです。そのままでは動きません

## 4. 声・動画・記事

| やりたいこと | リポジトリの手順 | Claude Code のスキル |
|---|---|---|
| 公式ボイスで読み上げる | [docs/voices.md](docs/voices.md)。`voice` に slug を渡す。seed は書かない | `aicu-api`、`tts` |
| 公式ボイスの見本を足す・差し替える | `docs/voice/<slug>/<slug>-v<版>-<言語>.mp3` に置き、[docs/voices.md](docs/voices.md) に載せる。**台詞は声の見本として成立させる**（AGENTS.md 第 2 節） | `tts` |
| ちびループダンス・フィギュアの回転動画 | 参照は `<CharacterName>/loop/ref-chibi-green.png`。seed とプロンプトを PR に書く | `video-ops`（投げる前の空き確認と記録） |
| 歌詞からミュージックビデオ | — | `lyric-mv` |
| AiCuty 名義の記事ドラフト | 口調は該当 README。納品先は `aicu-ai-media` の drafts | `media-draft` |
| bot の投稿が良くなかったときの記録 | — | `aicu-feedback` |
| イベントの告知 | — | `aicu-event-promo` |

## 5. 公式サイトに反映する

サイトは別リポジトリ [aicuai/aicuai-aicuty](https://github.com/aicuai/aicuai-aicuty)（`sites/`）にあります。関係は [AGENTS.md](AGENTS.md) 第 8 節。

1. 先に本リポジトリの `<CharacterName>/README.md`（設定）や `img/`・`docs/voice/`（原本）を PR で直す
2. マージ後、サイトの `sites/data.js` の該当メンバーを同じ内容に合わせる（日本語 `ja` と英語 `enT` の両方）
3. 画像は webp、音声は v3 の mp3 を `sites/img/`・`sites/voice/` に書き出す

## 6. 表記をまとめて直す

AGENTS.md 第 5 節のチェックリストに従います。要点だけ再掲します。

1. 先に `grep -rn` で全部のヒットを見る。**Saki Noire・アタシ・ミナさん**が混ざっていないか確かめる
2. 生成プロンプトの中の文字列は触らない（再現性が変わる）
3. slug・ファイル名・ディレクトリ名は変えない。直すのは表示名だけ
4. 過去記事・コンテスト結果など当時の記録は書き換えない
5. 直したあとに、相対リンクと残りを確かめる

## 7. この索引の直し方

- 手順を足したら、ここに 1 行足す。**手順の中身はここに書かず、正本のファイルへリンクする**
- スキルを新しく作ったら、名前だけをここに載せる。スキルの中身は `~/.claude/skills/` にあり、このリポジトリには入れません
