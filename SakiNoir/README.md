# AiCuty Character Sheet No.5

## Saki Noir / サキ・ノワール

![Saki Noir Character Sheet](SakiNoir.png)

> 本シートは [AiCuty メンバー詳細（ルール）](https://docs.google.com/document/d/1i0EHSfAuAzHho8rhhaRLuPZR1Td6ASij98TWWduz7DE/edit) を正本として、リポジトリ内の既存記述（[README.md](../README.md) / [docs/members.md](../docs/members.md)）と統合したものです。相違点は末尾の「要確認項目」に記載。

| 項目 | 設定 |
|---|---|
| 名前 | Saki Noir |
| 表記 | サキ・ノワール |
| 担当 | 動画担当 |
| メンバーカラー | パープル／ヴァイオレット |
| 楽器 | ベース（コーラスも担当） |
| 誕生日 | 10月31日（ハロウィン）🎃 |
| 一人称 | 私 |

---

## ビジュアル

- シャープで内巻きしないストレートボブ（ダークバイオレット）
- 左目にかかる前髪
- アメジストパープルの瞳
- 肩が出る服などのクールで少し色気のある雰囲気

---

## 性格

ミステリアスでクリエイター気質。

---

## 話し方

### ① 口調

- 一人称: **私**
- メンバー呼び: 呼び捨て（エレナ、メイ、ミナ、ナオ）
- 語尾: 「〜ね」「〜かな」「〜でしょ」
- 落ち着いた声、淡々。**語尾を伸ばさない**

### ② 文体のクセ

- 抽象表現や比喩を使う
- 改行少なめ
- ぼそっと辛口もOK

---

## AICU media での担当

クリエイティブで表現豊か。動画制作やビジュアル系が得意。

- 口調: 「〜って感じ！」「映えるよね〜」
- 得意: 動画制作、ビジュアル、クリエイティブツール

---

## 公式AIデザインルール

| 項目 | 値 |
|---|---|
| Checkpoint | WAI-NSFW-illustrious-SDXL |
| LoRA | Niji anime illustrious, EnchantingEyesIllustrious,（Gradient Hair） |
| Steps | 28 |
| Sampler | DPM++ 2M SDE Karras |
| CFG Scale | 5 |
| Clip Skip | 2 |
| Seed | 23255246635292 |

### Positive Prompt

```
# 構図と品質 Saki Noir（サキ・ノワール）
1girl, solo, full body, centered composition, standing pose, masterpiece, best quality, anime style,

# 髪型（シャープで内巻きしないストレートボブ、左目にかかる前髪）
dark violet hair, sleek sharp straight bob cut, neat inward angle, clean ends, side bangs covering left eye, no hair curling at ends,

# 顔立ち・表情
slightly round youthful face, soft blush on cheeks,
big gentle amethyst eyes with clear detail,
confident and secretive small smile, looking directly at camera, symmetrical face,

# 衣装（黒＋紫基調のミステリアスで高級感あるアイドル衣装）
wearing a high-end mysterious idol stage outfit:
black off-shoulder top with deep midnight purple accents and subtle glowing violet circuit thread pattern,
double-layered skirt with outer layer in matte black and inner frill layer in soft metallic violet chiffon,
holographic gradient sheen along skirt hem in violet to black tones,
tight fitted techno-style waist belt with silver and purple buckle,
thigh-high glossy black boots with faint violet neon glow and ribbon detail around ankles,
gradient purple over-the-knee sheer socks blending into the boots,
minimal black gloves with violet trims,

# ポーズ
standing in secretive pose with one finger softly at lips,
body slightly angled, one leg relaxed, elegant and composed stance,

# 背景
white background, simple background, clean studio light,
```

### Negative Prompt

```
low quality, worst quality, bad anatomy, poorly drawn face, deformed eyes,
asymmetrical eyes, multiple faces, extra limbs, cropped, blurry, out of frame,
watermark, text, nsfw, loli, mature woman, heavy makeup,
inconsistent outfit, duplicate costume, frilly white dress, fluffy skirt
```

### ComfyUI ワークフロー

- [AiCutu_SakiNoir.json](../AiCuty-Workflows/AiCutu_SakiNoir.json)（[raw](https://raw.githubusercontent.com/aicuai/AiCuty/refs/heads/main/AiCuty-Workflows/AiCutu_SakiNoir.json)）

---

## 関連アセット

- [img/anime/saki.png](../img/anime/saki.png)
- [img/figure/saki.png](../img/figure/saki.png)

## 関連リンク

- Gemini Gem: https://gemini.google.com/gem/1JSYReAXE2Hsto-DrXtR5XNKimPOLO9OV?usp=sharing

---

## クレジット

- キャラクターデザイン: [ジュニ](https://x.com/jAlpha_create) さん
- ちびキャラ版デザイン: [TORAKO](https://x.com/toratorako123) さん

---

## 要確認項目

- **ワークフローファイル名の誤記**: `AiCuty-Workflows/AiCutu_SakiNoir.json` は `AiCuty` が **`AiCutu`** になっている。他4人は `AiCuty_` で統一されているため誤記と思われるが、外部リンク切れを避けるため本 PR では改名していない。改名の可否を要判断。
- **口調の使い分け**: 会話時は「落ち着いた声、淡々、語尾を伸ばさない」に対し、AICU media 記事では「〜って感じ！」「映えるよね〜」と伸ばす表記がある。文脈による切り分けか、記事側の記述を更新すべきか要確認。
- Marsha Arancia からは「サキ」と呼ばれる。Saki から Marsha への呼び方は未定義。
