# AiCuty キャラクターリファレンス規格（gpt-2.5-flare）

各キャラクターディレクトリの `gpt-2.5-flare/` に置く参照資料の規格です。
**「AICU API の Character API プリセットとして出せる品質」**を基準にしています。

## 正本は、すでにある公式キャラクターシートです

**新しくデザインを起こすディレクトリではありません。** AiCuty には既に公式シートがあります。

| キャラクター | 公式シート | 規格 |
|---|---|---|
| Elena Bloom | [ElenaBloom/ElenaBloom.png](../ElenaBloom/ElenaBloom.png) | ✅ 準拠 |
| Mei Soleil | [MeiSoleil/MeiSoleil.png](../MeiSoleil/MeiSoleil.png) | ✅ 準拠 |
| Mina Azure | [MinaAzure/MinaAzure.png](../MinaAzure/MinaAzure.png) | ✅ 準拠 |
| Nao Verde | [NaoVerde/NaoVerde.png](../NaoVerde/NaoVerde.png) | ✅ 準拠 |
| Saki Noire | [SakiNoire/SakiNoire.png](../SakiNoire/SakiNoire.png) | ✅ 準拠 |
| **Marsha Arancia** | **なし**（原案イラストのみ） | ❌ **未整備** |

5 人のシートは同一フォーマット（`V20260113` / `CHECKED_BY_HAKASE`）で、
**Front / Side / Back の 3 面図 ＋ 5 表情（Normal / Happy / Shy / Surprised / Thinking）＋ CHARACTER DETAILS** が
1 枚に収まっています。書籍
『[【キャラクターを創り動かす】画像・動画生成AI スタートガイド](https://www.sbcr.jp/product/4815637675/)』
（SBクリエイティブ・2026-09-19・ISBN 978-4-8156-3767-5）第 4 章が説くキャラクターシートの構成要素を、
**すでに満たしています。**

そして各シートには、こう書かれています。

> **Style: Chibi, 2-3 head proportions**

**AiCuty の公式体型は、ちび 2〜3 頭身です。** ここが本規格でいちばん重要な一行です。

## ⚠️ 既知の不整合: ベンチの「正本プロンプト」は公式シートと一致していません

[`bench/prompts/Mei.txt`](../bench/prompts/Mei.txt) と [`bench/prompts/Saki.txt`](../bench/prompts/Saki.txt) は
`anime idol girl, full body` と書かれた **8 頭身の等身大アイドル**を生成するプロンプトです。
公式シートのちび 2-3 頭身とは別のデザインになります。

[AiCutyBench](https://api.aicu.ai/docs/blog/aicutybench-gpt-image-2-5) が「歩留まり 100%」と報告したのは、
**判定軸に頭身が入っていなかったため**です。髪色・サイドポニー・星ヘアピン・瞳・そばかす・衣装・靴の
8 項目はすべて 8 頭身でも満たせます。**公式デザインとの一致は、測られていませんでした。**

Character API のプリセットを作るときは、この件を必ず踏まえてください。

## 公式デザインを再現する条件（実測・2026-09-21）

`gpt-image-2.5-flare` / medium / 1024x1024 で、Mei を 3 通り生成して比較しました。

| 条件 | 結果 |
|---|---|
| (A) プロンプトのみ（参照画像なし） | **8 頭身の別人**。公式に似ていない |
| (B) 参照画像あり・体型指示なし | 衣装と靴は公式に近づくが、**6〜7 頭身のまま** |
| (C) **参照画像あり ＋ ちび 2-3 頭身を明示** | **公式にかなり近い**。3 頭身・星ヘアピン・白プリーツ＋黄ショーツ・厚底スニーカー |

**参照画像と頭身指定は、両方必要です。どちらか一方では公式デザインになりません。**

比較画像: `bench/aicu-api/out/` の `pilot-Mei-01-front.png`（A）/ `ref-Mei-01-front.png`（B）/ `ref-Mei-01-chibi.png`（C）

## 生成のしかた

```bash
export AICU_API_KEY=...   # images スコープが必要

python3 bench/aicu-api/gen_aicu.py \
  --model gpt-image-2.5-flare --quality medium --size 1024x1024 \
  --prompt-file MeiSoleil/gpt-2.5-flare/prompts/01-standing-front.txt \
  --reference MeiSoleil/MeiSoleil.png \
  --label Mei-01-standing-front
```

**`--reference` は必須です。** 各 `gpt-2.5-flare/REFERENCE.txt` に、そのキャラで渡すべき公式シートを書いています。
参照画像なしで生成したものを公式素材にしないでください。

## 必要なカット（7 種）

| # | カット | サイズ | 何が確認できること |
|---|---|---|---|
| 01 | 立ち絵 正面（**基準**） | 1024x1024 | 全体のシルエット。ここが曖昧だと資料全体が不安定になる |
| 02 | 立ち絵 側面 | 1024x1024 | 髪の長さ、衣装の構造 |
| 03 | 立ち絵 背面 | 1024x1024 | 背面デザイン、後ろ髪 |
| 04 | バストアップ | 1024x1024 | 顔立ち、首まわり、肩まわり、前髪の分かれ方 |
| 05 | 目元のアップ | 1024x1024 | 瞳の色、ハイライト、まつ毛、目の形 |
| 06 | 装飾品の個別アップ | 1536x1024 | 髪飾り、エンブレム、靴。「らしさ」を決める部分 |
| 07 | 表情差分（5 種） | 1536x1024 | **公式シートと同じ Normal / Happy / Shy / Surprised / Thinking** |

表情の名前と順番は**公式シートに合わせています**。勝手に増やしたり呼び方を変えたりしないでください。
既存の出力との互換性が切れます。

## プロンプトの三段構成

```
prompts/00-base-fixed.txt      … 固定された要素（キャラの土台＋体型＋参照追従の指示）
prompts/01-standing-front.txt  … 土台 ＋ 見せ方（画角・構図）
prompts/07-expressions.txt     … 土台 ＋ 描写したい内容（表情）＋ 見せ方
```

**外見を直すときは `00-base-fixed.txt` だけを直し、全カットを再生成します。**
カット側を個別にいじると、どこで見た目が変わったのか追えなくなります。

## 受け入れ基準

採用前に、次をすべて満たしているか確認します。

1. **公式シートと同じ頭身（ちび 2-3 頭身）である**
2. 各キャラの `gpt-2.5-flare/README.md` の **NG 事項に 1 つも抵触していない**
3. **手指が正しい**（4 本に見える・融合している生成物は不採用）
4. 全身カットで**全身が見切れていない**
5. 背景が白または無地で、**文字が写り込んでいない**（画像モデルは文字を崩します）
6. 01〜05 を並べたとき、**同一人物に見える**
7. **既存の公式シートと並べて、同じキャラに見える**（互換性）
8. プロンプト・参照画像・出力が [GENERATION-LOG.md](../MarshaArancia/GENERATION-LOG.md) 形式で追跡できる

**破綻を「隠す」で回避しないこと。** 生成して、精査して、駄目なら作り直します。

## コストの目安（2026-09-21 実測・AICU API 経由）

AP はレスポンスの `X-AICU-AP-Cost` ヘッダで 1 回ごとに取れます（残高差分と一致を確認済み）。

| サイズ / quality | AP | 生成時間 |
|---|---|---|
| 1024x1024 / low | 700 | 10.4 s |
| 1024x1024 / **medium** | **1,600** | 11.6 s |
| 1024x1024 / high | 6,400 | 22.1 s |
| 1536x1024 / medium | 2,300 | 12.5 s |

- **既定は `medium`**。quality を上げても忠実度が上がる兆候は出ていません
- `xhigh` / `max` は AICU API では `400 quality_not_priced` で使えません
- **横長は被写体が小さくなります**（余白が足される）。立ち絵は正方形で

1 キャラ 7 カットで約 **12,700 AP**、6 キャラで約 **76,000 AP**。

計測の根拠と再現手順は [../bench/aicu-api/](../bench/aicu-api/) にあります。

## 未確定事項（CEO 判断待ち）

1. **Marsha Arancia に公式シートがありません。** 他 5 人と同じフォーマットのシートを先に作る必要があります。
   Character API に未登録なのはこれが理由と思われます
2. **Elena / Mina / Nao / Marsha の正本プロンプトがリポジトリに残っていません**
   （`bench/prompts/` にあるのは Mei と Saki だけ）。各 `00-base-fixed.txt` は
   公式シートと README から起こした暫定版です。デザイン担当の確認後に確定してください
3. `bench/prompts/Mei.txt` / `Saki.txt` の 8 頭身プロンプトを、公式準拠に**差し替えるか併存させるか**。
   併存させる場合は「等身大版」と明記が必要です
4. Character API のプリセット（`GET /v1/images/characters`）は 2026-09-21 時点で 10 件すべて `gpt-image-2` です。
   **この規格のリファレンスが揃ってから**プリセットの向き先を変更します
