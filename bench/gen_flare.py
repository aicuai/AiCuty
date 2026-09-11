import base64, json, os, sys, urllib.request
prompt_file, out_png = sys.argv[1], sys.argv[2]
prompt = open(prompt_file, encoding="utf-8").read().strip()
body = json.dumps({"model":"gpt-image-2.5-flare","size":"1024x1024","quality":"high","prompt":prompt}).encode()
req = urllib.request.Request("https://api.openai.com/v1/images/generations", data=body, method="POST")
req.add_header("Authorization","Bearer "+os.environ["OPENAI_API_KEY"]); req.add_header("Content-Type","application/json")
try:
    d = json.load(urllib.request.urlopen(req, timeout=170))
    open(out_png,"wb").write(base64.b64decode(d["data"][0]["b64_json"])); print("OK")
except Exception as e:
    print("FAIL", str(e)[:150]); sys.exit(1)
