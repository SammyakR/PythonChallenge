import re
import requests
from collections import Counter

r = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
#doc = html5lib.parse(r)

i = len(r.text)

first = r.text.find("<!--")
end = r.text.find("--!>")
mess = r.text[first:end]

#removed first comment
mess2 = mess[50:]

print(mess2)
cnt = Counter(mess2)

print(cnt)
