import requests
import re
from collections import Counter

r = requests.get('http://www.pythonchallenge.com/pc/def/equality.html')

first = r.text.find("<!--")
end = r.text.find("--!>")
mess = r.text[first:end]


cnt = Counter(mess)
print(type(re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', mess)))

print(cnt)


#print(mess)