import requests
import re

link = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num = "71301"

"""r = requests.get(link+num)
num = re.search(r'[0-9]+', r.text).group()
print(r.text)
print(num)
"""

for i in range(400):
	r = requests.get(link+ num)
	print(r.text)
	num = str(re.search(r'[0-9]+', r.text).group())
	if(num == ""):
		break



