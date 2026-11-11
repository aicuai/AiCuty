#!/usr/bin/env python3
"""生成画像を AICU API の gpt-4o Vision で n 回採点し、判定軸ごとに集計する。"""
import base64, io, json, os, sys, urllib.request, collections, statistics
from PIL import Image

img_path, feats_file, n = sys.argv[1], sys.argv[2], int(sys.argv[3] if len(sys.argv)>3 else 3)
im = Image.open(img_path).convert("RGB"); im.thumbnail((768,768))
buf = io.BytesIO(); im.save(buf,"JPEG",quality=88)
b64 = base64.b64encode(buf.getvalue()).decode()
feats = open(feats_file).read()

def score_once():
    payload={"model":"gpt-4o","max_tokens":700,"temperature":0,"messages":[{"role":"user","content":[
        {"type":"text","text":feats},
        {"type":"image_url","image_url":{"url":"data:image/jpeg;base64,"+b64}}]}]}
    req=urllib.request.Request("https://api.aicu.ai/v1/chat/completions",
        data=json.dumps(payload).encode(),method="POST")
    req.add_header("Authorization","Bearer "+os.environ["AICU_API_KEY"])
    req.add_header("Content-Type","application/json")
    res=urllib.request.urlopen(req,timeout=180); h=dict(res.headers); d=json.load(res)
    t=d["choices"][0]["message"]["content"]
    j=json.loads(t[t.index("{"):t.rindex("}")+1])
    return j, int(h.get("X-AICU-AP-Cost",0))

scores=[]; ap=0; miss=collections.Counter()
for _ in range(n):
    try: j,a=score_once()
    except Exception as e: print("  採点失敗:",str(e)[:80]); continue
    ap+=a; scores.append(j.get("overall_score"))
    for f in j.get("features",[]):
        name=f.get("feature") or f.get("name") or "?"
        st=(f.get("status") or f.get("state") or "").lower()
        if st and st!="present": miss[f"{name} [{st}]"]+=1
name=os.path.basename(img_path)
avg=statistics.mean(scores) if scores else 0
print(f"{name:20s} n={len(scores)} scores={scores} 平均={avg:.1f} 採点AP計={ap}")
for k,v in miss.most_common(): print(f"    落ちた軸: {k} x{v}/{len(scores)}")
