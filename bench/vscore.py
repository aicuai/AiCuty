import base64, json, os, sys, urllib.request
img, feats_file = sys.argv[1], sys.argv[2]
b64 = base64.b64encode(open(img,'rb').read()).decode()
feats = open(feats_file).read()
payload = {"model":"gpt-4o","max_tokens":700,"messages":[{"role":"user","content":[
  {"type":"text","text":feats},
  {"type":"image_url","image_url":{"url":"data:image/png;base64,"+b64}}]}]}
req = urllib.request.Request("https://api.openai.com/v1/chat/completions",
  data=json.dumps(payload).encode(), method="POST")
req.add_header("Authorization","Bearer "+os.environ["OPENAI_API_KEY"])
req.add_header("Content-Type","application/json")
d = json.load(urllib.request.urlopen(req, timeout=120))
print(d["choices"][0]["message"]["content"])
