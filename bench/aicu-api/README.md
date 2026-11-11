# AICU API 経由のベンチ（2026-09-21〜）

`bench/` 直下の既存スクリプト（`gen_flare.py` / `quality_sweep.py` / `vscore.py`）は
**`api.openai.com` を直接叩きます**（`OPENAI_API_KEY` を使用）。OpenAI に直接出したときの
トークン数・レイテンシを測るためのもので、**AICU API を使ったときのコストは測れません**。

このディレクトリは **すべて `https://api.aicu.ai/v1` 経由**で測るための版です。
コストの単位は AP（AICU Points）で、推定ではなくレスポンスの `X-AICU-AP-Cost`
ヘッダ（1 回ごとの実費）を記録します。

## 使い方

```bash
export AICU_API_KEY=aicu_live_...      # images スコープが必要

# quality を 3 段階振る
for q in low medium high; do
  python3 gen_aicu.py --model gpt-image-2.5-flare --quality $q \
    --prompt-file ../prompts/Mei.txt --label "flare-$q"
done
# -> results.csv に ap_cost / latency_ms / image_id が追記され、out/ に PNG が出ます

# 忠実度採点（同じ画像を n 回採点して judge のぶれを均す）
python3 vscore_aicu.py out/flare-medium.png ../features/Mei.txt 3
```

## 測定済みの結果

`../results/aicu_api_quality_flare_20260921.csv`

| quality | AP | 生成時間 |
|---|---|---|
| low | 700 | 10.4 s |
| medium | 1,600 | 11.6 s |
| high | 6,400 | 22.1 s |

AP は出力画像トークンに **約 3.6 AP/token** で比例します。

## 注意

- **`xhigh` / `max` は AICU API では使えません**。`400 quality_not_priced` が返ります
  （弾かれた要求は課金されません）。選べるのは `low` / `medium` / `high` の 3 つです。
- `gpt-image-2.5-*` は Cloudflare のエッジ制限 100 秒を超えることがあります。**HTTP が切れても
  生成は続いていて、課金は 1 回だけ**です。再送せず、`X-AICU-Image-Id` の id で
  `GET /v1/images/status/{id}` から回収してください。

解説記事: https://api.aicu.ai/docs/blog/gpt-image-2-5-ap-cost-remeasured
