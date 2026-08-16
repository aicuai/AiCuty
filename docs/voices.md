---
layout: default
title: 公式ボイス / Official Voices
---

# AiCuty 公式ボイス

AiCuty メンバーの声は [api.aicu.ai](https://api.aicu.ai) から呼び出せます。
このページは**実際に API が返す音**をそのまま置いたものです。

## 声は毎回おなじです

`eleven_v3` は生成のたびに声質とテンションが変わります。
キャラクターボイスとしてそれでは成立しないので、**メンバーごとに seed を固定**しました。

seed はキャラクターの誕生日（月＋日を連結）を起点に、近傍を聴き比べて決めています。
たとえばミナは10月1日生まれなので `101` が起点です。

`voice` に slug を渡すだけでこの声が返ります。seed を書く必要はありません。

```bash
curl -X POST https://api.aicu.ai/v1/audio/speech \
  -H "Authorization: Bearer $AICU_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"voice": "mina", "model": "eleven_v3", "input": "こんにちは"}' \
  --output mina.mp3
```

OpenAI SDK からも同じように呼べます。

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.aicu.ai/v1", api_key="aicu_live_…")
client.audio.speech.create(model="eleven_v3", voice="mina", input="こんにちは").stream_to_file("mina.mp3")
```

## モデルの選び方

| | `eleven_v3` | `eleven_multilingual_v2` |
|---|---|---|
| 抑揚 | `[cheerfully]` などの audio tag が効く | タグは効かない（**そのまま音読される**） |
| 1リクエストの上限 | 5,000文字 | 10,000文字 |
| 用途 | 台詞・キャラクターボイス | 長文のナレーション |

## 日本語の読み

固有名詞や略語は、送る前に**かな書きへ開く**のが最も確実です。
下のサンプルも「AICU」→「アイキュー」のように開いた文面で送っています。

詳しくは [日本語TTSを使いこなす](https://api.aicu.ai/docs?doc=japanese-tts) を参照してください。

---

## メンバー

### Elena Bloom / エレナ・ブルーム

**落ち着いて聞き取りやすい、標準語の女性ナレーション**

> こんにちは、エレナ・ブルームです。エルエルエムとエスエヌエス活用を担当しています。アイキューティーのセンターとして、みなさんをお迎えします。

| 言語 | eleven_v3（推奨） | eleven_multilingual_v2 |
|---|---|---|
| 日本語 | <audio controls preload="none" src="voice/elena/elena-v3-ja.mp3"></audio> | <audio controls preload="none" src="voice/elena/elena-v2-ja.mp3"></audio> |
| English | <audio controls preload="none" src="voice/elena/elena-v3-en.mp3"></audio> | <audio controls preload="none" src="voice/elena/elena-v2-en.mp3"></audio> |
| Français | <audio controls preload="none" src="voice/elena/elena-v3-fr.mp3"></audio> | <audio controls preload="none" src="voice/elena/elena-v2-fr.mp3"></audio> |

`voice: "elena"` — 既定 seed v3 `330` / v2 `330`

### Mei Soleil / メイ・ソレイユ

**元気で子供でも聴きやすい、明るい少女の声**

> こんにちは、メイ・ソレイユです。メイはキービジュアルと画像を担当しています。一緒に、うちの子を描こうね。

| 言語 | eleven_v3（推奨） | eleven_multilingual_v2 |
|---|---|---|
| 日本語 | <audio controls preload="none" src="voice/mei/mei-v3-ja.mp3"></audio> | <audio controls preload="none" src="voice/mei/mei-v2-ja.mp3"></audio> |
| English | <audio controls preload="none" src="voice/mei/mei-v3-en.mp3"></audio> | <audio controls preload="none" src="voice/mei/mei-v2-en.mp3"></audio> |
| Français | <audio controls preload="none" src="voice/mei/mei-v3-fr.mp3"></audio> | <audio controls preload="none" src="voice/mei/mei-v2-fr.mp3"></audio> |

`voice: "mei"` — 既定 seed v3 `721` / v2 `721`

### Mina Azure / ミナ・アズール

**落ち着いた知的なナレーション。長時間でも聴き疲れしない**

> こんにちは、ミナ・アズールです。調査と分析、そして倫理と法律を担当しています。放送部で、アナウンスの練習をしています。

| 言語 | eleven_v3（推奨） | eleven_multilingual_v2 |
|---|---|---|
| 日本語 | <audio controls preload="none" src="voice/mina/mina-v3-ja.mp3"></audio> | <audio controls preload="none" src="voice/mina/mina-v2-ja.mp3"></audio> |
| English | <audio controls preload="none" src="voice/mina/mina-v3-en.mp3"></audio> | <audio controls preload="none" src="voice/mina/mina-v2-en.mp3"></audio> |
| Français | <audio controls preload="none" src="voice/mina/mina-v3-fr.mp3"></audio> | <audio controls preload="none" src="voice/mina/mina-v2-fr.mp3"></audio> |

`voice: "mina"` — 既定 seed v3 `101` / v2 `105`

### Nao Verde / ナオ・ヴェルデ

**優しい理系男子のソフトボイス**

> やあ、ナオ・ヴェルデだよ。僕は音楽と開発技術担当。ディーティーエムやゲーム開発も好きだな。よろしくね。

| 言語 | eleven_v3（推奨） | eleven_multilingual_v2 |
|---|---|---|
| 日本語 | <audio controls preload="none" src="voice/nao/nao-v3-ja.mp3"></audio> | <audio controls preload="none" src="voice/nao/nao-v2-ja.mp3"></audio> |
| English | <audio controls preload="none" src="voice/nao/nao-v3-en.mp3"></audio> | <audio controls preload="none" src="voice/nao/nao-v2-en.mp3"></audio> |
| Français | <audio controls preload="none" src="voice/nao/nao-v3-fr.mp3"></audio> | <audio controls preload="none" src="voice/nao/nao-v2-fr.mp3"></audio> |

`voice: "nao"` — 既定 seed v3 `55` / v2 `55`

### Saki Noire / サキ・ノワール

**優しさとあやしい魅力がある囁きボイス**

> こんばんは、サキ・ノワールです。動画を担当しています。夜の渋谷を撮るのが、好きなんです。

| 言語 | eleven_v3（推奨） | eleven_multilingual_v2 |
|---|---|---|
| 日本語 | <audio controls preload="none" src="voice/saki/saki-v3-ja.mp3"></audio> | <audio controls preload="none" src="voice/saki/saki-v2-ja.mp3"></audio> |
| English | <audio controls preload="none" src="voice/saki/saki-v3-en.mp3"></audio> | <audio controls preload="none" src="voice/saki/saki-v2-en.mp3"></audio> |
| Français | <audio controls preload="none" src="voice/saki/saki-v3-fr.mp3"></audio> | <audio controls preload="none" src="voice/saki/saki-v2-fr.mp3"></audio> |

`voice: "saki"` — 既定 seed v3 `1033` / v2 `1035`

### Marsha Arancia / マーシャ・アランチャ

**さわやかで聴きやすい元気な女性**

> ¡Hola! はじめまして、マーシャ・アランチャです。アタシは国際文化と書籍出版に興味があるよ〜。まって!? いまのフレーズ、最高じゃない!? 特集にしたいネ！

| 言語 | eleven_v3（推奨） | eleven_multilingual_v2 |
|---|---|---|
| 日本語 | <audio controls preload="none" src="voice/marsha/marsha-v3-ja.mp3"></audio> | <audio controls preload="none" src="voice/marsha/marsha-v2-ja.mp3"></audio> |
| English | <audio controls preload="none" src="voice/marsha/marsha-v3-en.mp3"></audio> | <audio controls preload="none" src="voice/marsha/marsha-v2-en.mp3"></audio> |
| Español | <audio controls preload="none" src="voice/marsha/marsha-v3-es.mp3"></audio> | <audio controls preload="none" src="voice/marsha/marsha-v2-es.mp3"></audio> |
| Italiano | <audio controls preload="none" src="voice/marsha/marsha-v3-it.mp3"></audio> | <audio controls preload="none" src="voice/marsha/marsha-v2-it.mp3"></audio> |

`voice: "marsha"` — 既定 seed v3 `418` / v2 `414`

### LuC4 / Luca / ルカ（全力肯定彼氏くん）

**気持ちのいい低音の男性。裏設定として関西訛りがある**

> おはよう！僕は 全力肯定彼氏くん、コードネーム ルーシーフォウ、ルカって呼んでね。君のペースで英語の勉強を応援するよ。

| 言語 | eleven_v3（推奨） | eleven_multilingual_v2 |
|---|---|---|
| 日本語 | <audio controls preload="none" src="voice/luc4/luc4-v3-ja.mp3"></audio> | <audio controls preload="none" src="voice/luc4/luc4-v2-ja.mp3"></audio> |
| English | <audio controls preload="none" src="voice/luc4/luc4-v3-en.mp3"></audio> | <audio controls preload="none" src="voice/luc4/luc4-v2-en.mp3"></audio> |

`voice: "luc4"` — 既定 seed v3 `1104` / v2 `1104`


---

## ライセンス

AiCuty のキャラクターおよび音声の利用は
[AiCuty ガイドライン](https://www.aicu.jp/terms/aicuty-guideline)に従ってください。
