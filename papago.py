#!/usr/local/bin/python3

from urllib import request
from urllib import parse
import base64
import json
import sys

args = sys.argv[1:]
if args:
    en = " ".join(sys.argv[1:])
else:
    sys.exit(1)

url = "https://papago.naver.com/apis/n2mt/translate"
data = '"text":"' + en +'"}'
payload = bytes(str(data), encoding='utf-8')
payload = base64.b64encode(payload)

payload = bytes("rlWxnJA0Vwc0paIyLCJkaWN0RGlzcGxheSI6NSwic291cmNlIjoiZW4iLCJ0YXJnZXQiOiJrbyIs", encoding='utf-8') + payload
payload = str(payload, 'utf-8')
payload = {"data": payload}
payload = bytes(parse.urlencode(payload), encoding ='utf-8')

r = request.urlopen(url, data=payload)
r_body = r.read()
r_txt = r_body.decode('utf-8')
parsed = json.loads(r_txt)

translated = parsed["translatedText"]
print(translated)

