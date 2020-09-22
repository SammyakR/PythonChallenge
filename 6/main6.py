import re
import zipfile

num = "90052"
lst = []
comments = []
file = zipfile.ZipFile("channel.zip")

while True:
	text = file.read(num+".txt").decode("utf-8")
	#print(fread)
	comments.append(file.getinfo(num + ".txt").comment.decode("utf-8"))
	num = re.search(r'[0-9]+', text)
	if num == None:
		break;
	num = num.group()


print("".join(comments))

   







