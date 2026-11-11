#!/bin/bash
export OPENAI_API_KEY
OUT=/Users/aki/git.local/AiCuty/GPT-Image-2.5-trial/yield; mkdir -p "$OUT"
THRESH=85; RESULT=/tmp/yield/results.csv; echo "char,n,score,pass" > "$RESULT"
for name in Mei Saki; do
  for i in $(seq 1 10); do
    if python3 /tmp/yield/gen.py /tmp/yield/$name.prompt "$OUT/$name-$i.png" >/dev/null 2>&1; then
      SC=$(python3 /tmp/vscore.py "$OUT/$name-$i.png" /tmp/yield/$name.feats 2>/dev/null | python3 -c "import sys,re;t=sys.stdin.read();m=re.search(r'overall_score\"?\s*:\s*(\d+)',t);print(m.group(1) if m else 'NA')")
      PASS=$([ "$SC" != "NA" ] && [ "$SC" -ge $THRESH ] 2>/dev/null && echo 1 || echo 0)
      echo "$name,$i,$SC,$PASS" >> "$RESULT"
    else echo "$name,$i,GENFAIL,0" >> "$RESULT"; fi
  done
done
python3 -c "
import csv; from collections import defaultdict
d=defaultdict(list)
for r in csv.DictReader(open('$RESULT')):
    s=r['score']; d[r['char']].append((int(s) if s.isdigit() else 0, int(r['pass'])))
print('=== YIELD (threshold=85) ===')
for c,v in d.items():
    sc=[s for s,_ in v]; p=sum(pp for _,pp in v)
    print(f'{c}: pass={p}/{len(v)} yield={100*p/len(v):.0f}%  avg={sum(sc)/len(sc):.0f}')
" >> "$RESULT"
touch /tmp/yield/DONE
