import base64, json, os, sys, time, urllib.request
q, out = sys.argv[1], sys.argv[2]
prompt = open('/tmp/yield/Mei.prompt', encoding='utf-8').read().strip()
body = json.dumps({"model":"gpt-image-2.5-flare","size":"1024x1024","quality":q,"prompt":prompt}).encode()
req = urllib.request.Request("https://api.openai.com/v1/images/generations", data=body, method="POST")
req.add_header("Authorization","Bearer "+os.environ["OPENAI_API_KEY"]); req.add_header("Content-Type","application/json")
t=time.time()
try:
    d=json.load(urllib.request.urlopen(req, timeout=300)); dt=time.time()-t
    open(out,"wb").write(base64.b64decode(d["data"][0]["b64_json"]))
    u=d.get("usage",{}); print(f"{q},{u.get('output_tokens_details',{}).get('image_tokens')},{u.get('total_tokens')},{dt:.1f}")
except Exception as e: print(f"{q},ERR,{str(e)[:80]},")
