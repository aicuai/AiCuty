# AiCuty 公式サイト（aicu.ai/aicuty）

「人とAIがつくるアイドル」AiCuty の公式サイトです。日本語と英語に対応しています。

| URL | 言語 |
|---|---|
| https://aicu.ai/aicuty/ | 日本語（既定） |
| https://aicu.ai/aicuty/en/ | English |

## ビルド

依存パッケージはありません（Node.js 18 以上）。

```bash
node site/build.mjs   # → site/dist/
npx serve site/dist   # ローカル確認（任意）
```

`site/dist/` はビルド成果物なのでコミットしません。

## 構成

```
site/
  build.mjs          テンプレート × i18n → dist/index.html, dist/en/index.html
  src/template.html  ページの骨格（{{t.key}} が i18n.json、{{base}} が相対パス）
  src/i18n.json      静的テキスト（ja / en）
  src/data.js        メンバー・ニュース・スライド（ja / en）
  src/app.js         カルーセル、ニュース絞り込み、メンバー詳細、誕生日カレンダー、推し色
  src/style.css
  assets/img/        WebP に最適化した素材（元画像はリポジトリ内の各メンバーディレクトリ）
```

ボイスはビルド時に `docs/voice/<slug>/<slug>-v3-{ja,en}.mp3` からコピーします。

アセットはすべて相対パスなので、`/aicuty/` 以外のパスに置いても動きます。

## ニュースを追加する

`src/data.js` の `news` 配列の先頭に追加します。`ja` と `en` の両方を書いてください。
日付は確定しているものだけ書きます（未確定なら年のみ）。

## 公開（aicu.ai/aicuty）

`aicu.ai` 本体は `aicu-ai` リポジトリ（`apps/site`）が配信しているため、次のどちらかで `/aicuty/` に載せます。
**どちらもルーティング／DNS に触る作業なので、実行前に人が確認してください。**

1. **aicu-ai に静的ファイルとして同梱**：`site/dist/` の中身を `apps/site/public/aicuty/` にコピーしてデプロイ。最も簡単。
2. **Cloudflare Pages ＋ Worker ルート**：このリポジトリを Pages に接続（Build command `node site/build.mjs`、Output `site/dist`）し、
   `aicu.ai/aicuty/*` を Pages の `*.pages.dev` へプロキシする Worker ルートを追加。AiCuty 側だけで更新できる。

## 公開前の確認事項

- [ ] 問い合わせ先 URL（`build.mjs` の `CONTACT_URL`。現在は仮に aicu.ai トップ）
- [ ] 日付が年のみのニュース（ボイス公開、英語版配信、マーシャ加入、マガジン Vol.15）
- [ ] グループ公式 X アカウントの有無（現在は @SakiNoire のみ掲載）
- [ ] 英語版の楽曲名「人工現実モラトリアム」の公式英題

## 表記ルール

[AGENTS.md](../AGENTS.md) の第2節に従います。表示名は **Saki Noire**、Marsha の一人称は **アタシ**。
博士（Hakase）は AiCuty メンバーに含めません。
