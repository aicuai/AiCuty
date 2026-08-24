---
layout: default
title: AiCuty キャラクターシート制作手順
---

# AiCuty キャラクターシート制作手順

AiCuty のキャラクターシートを画像生成AIで作るときの、**納品区分・フォーマット・検品手順**をまとめたものです。
Marsha Arancia（No.6）の制作で確立した手順を、他メンバーにも適用できる形で記録しています。

---

## 1. 納品区分は Chibi / Standard / Photo の3系統

同じキャラクターでも、用途によって作り分けます。**それぞれ別物なので、混ぜて納品しません。**

| 区分 | 内容 | 主な用途 |
|---|---|---|
| **Chibi** | 2〜3頭身のちびキャラ版シート | ステッカー、SNS、LP のキーヴィジュアル |
| **Standard** | 等身大のデザインシート（3面＋表情＋小物＋パレット） | **キャラクター設定の正本。生成AIのリファレンス** |
| **Photo** | 実写系の宣材写真・キャスティングシート | 記事・広報、実写コラボ検討 |

このほか、シートではない単体素材として **KeyVisual**（全身1枚絵）、**Cover**（記事カバー）があります。

ファイル名は `<CharacterName>-<区分>[-<派生>].png` に揃えます。

```
MarshaArancia-Chibi.png
MarshaArancia-Standard.png
MarshaArancia-Standard-Expression-Cheeks.png
MarshaArancia-Photo-Headshot.png
MarshaArancia-KeyVisual.png
```

---

## 2. Standard シートの必須フォーマット

**勝手に省略しない。** 文字が崩れるのを嫌ってラベルを消すのはフォーマット違反です。

- 左上に **キャラクター名**（大文字・太字）
- 全身3面に **`FRONT` / `3/4` / `BACK`** のラベル
- **`EXPRESSIONS`** ブロック（罫線つき見出し＋表情パネル）
- **`ACCESSORIES`** ブロック（罫線つき見出し＋小物を枠で囲って個別に）
- **`COLOR PALETTE`** ブロック（罫線つき見出し＋色見本＋**HEXコード**）
- 白背景

---

## 3. 手順

### 3.1 承認済みシートを参照画像にして生成する

新規に描き起こすのではなく、**承認済みの公式シートを参照画像として渡し、レイアウトと同一性を再現させます。**
プロンプトには「参照画像のレイアウト・ラベル・キャラクターの外見を厳密に再現すること」を明記します。

キャラクター固有の**外しやすい要素は必ず明示**します。Marsha の場合は褐色肌がそれで、
指定しないと生成のたびに明るい肌へ転びます。

```
WARM MEDIUM-BROWN GOLDEN SKIN TONE (tan skin). Essential in EVERY panel.
Never pale or white skin.
```

### 3.2 生成後、必ず拡大して検品する

**「たぶん大丈夫」で通さない。** 破綻しやすい箇所は決まっているので、順に潰します。

| 対象 | 倍率 | 見るところ |
|---|---|---|
| 手・指 | **5〜10倍** | 指の本数（4本＋親指＝5本）、関節、爪 |
| 小物 | 3〜4倍 | 設定どおりの形状か、部品が省略されていないか |
| ラベル・タイトル | 3倍 | 綴りが正しいか |
| 全パネル | 等倍 | 同一人物・同一衣装・同一配色になっているか |

検品用の切り出しはスクリプトで機械的に行い、**必ず目視します。**

```python
from PIL import Image
img = Image.open("sheet.png")
c = img.crop((x0, y0, x1, y1))
c.resize((c.width*5, c.height*5), Image.LANCZOS).save("review_hand.png")
```

### 3.3 駄目なら作り直す。隠して回避しない

破綻した部位を物や画角で隠して逃げると、**その部位の設定が資料に残りません。**
キャラクターシートは全部が仕様なので、隠したら資料として成立しません。作り直します。

ただし、**衣装設定として元々隠れている**のは別です。Marsha はオーバーサイズジャケットの
長い袖が手を覆うのが公式仕様なので、全身3面ではそのまま袖で覆います。
逃げなのか仕様なのかは、**承認済みの公式シートを見れば分かります。**

---

## 4. 手をどう資料化するか

全身ビューでは手が小さすぎて（1536x1024 のシート上で 40px 程度）、指を正しく描く解像度がありません。
かといって袖で覆うだけでは手の設定が残りません。

**表情パネルのスケールで手を描かせます。** 顔と同じ大きさなら指は正しく描けます。

Marsha では「両手を頬にあて、美味しそうにしている表情」を1枚生成し、
**表情パネルと手のリファレンスを兼用**させました。これをシートの `EXPRESSIONS` に組み込みます。

プロンプトの要点は「指をまとめて描かせない」ことです。

```
On EACH hand, all FOUR fingers must be drawn slightly fanned apart with a visible
gap between them, so that every individual finger and its own rounded fingernail is
separately readable — do not let the fingers merge into a single mass.
The THUMB is clearly separate, curving down along the jawline.
```

指を密着させると輪郭が融合し、本数が読めなくなります（実際に一度これで没にしました）。

---

## 5. 正確さが要る文字は、後段で合成する

**HEXコードのように値の正しさが要る文字は、生成AIに書かせません。**
生成後にスウォッチの実ピクセルを採取し、プログラムで描き込みます。こうすると値が実際の色と必ず一致し、
文字も崩れません。

```python
# スウォッチ中央の平均色を採取して HEX を描き込む
c = avg_color(img, x0, x1, y0, y1)
draw.text(pos, f"#{c[0]:02X}{c[1]:02X}{c[2]:02X}", font=font, fill=(40,40,40))
```

合成時は**対象領域の座標を実測してから**描画します。目分量で白塗りすると、
見出しや罫線を削ってしまいます（実際にやりました）。

パネルを貼り込むときは、近白背景をマスクして輪郭だけを合成します。
矩形のまま貼るとシート背景との色差で継ぎ目が出ます。

---

## 6. 記録する

生成AIの出力は同じ条件でも再現しません（`gpt-image-2` に seed パラメータはありません）。
再現性は **「プロンプト全文 ＋ 参照画像 ＋ 採用した出力」の三点を固定**して担保します。

- プロンプト全文を `prompts/<用途>-prompt.txt` に保存する
- 生成台帳に 出力・サイズ・quality・プロンプト・参照画像・生成日 を記録する
- **没にしたものは理由つきで残す**（同じ失敗を繰り返さないため）
- ComfyUI など seed のある系統では seed を必ず併記する

実例: [MarshaArancia/GENERATION-LOG.md](https://github.com/aicuai/AiCuty/blob/main/MarshaArancia/GENERATION-LOG.md)

---

## 7. 実写系（Photo）を作るときの注意

**実写版のキャラクターは実在しない架空の人物です。**
人物写真をムードリファレンスに使う場合も、**実在の人物を再現・特定してはなりません。**
プロンプトにこの制約を明記します。

```
Create a wholly original adult face. Do not copy or identify any real person.
No celebrity likeness.
```

---

[Back to Home](index.md)
