


string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj. "
string1 = string.replace(" ","")

url = "map"
print(string1)
print("\n")
abc = "abcdefghijklmnopqrstuvwxyz"
#x = "".join([abc[(abc.find(c)+28)%26] for c in string])
x1 = ""

for itr in url:
	if(itr == ' ' or itr == '(' or itr == ')' or itr == '.'):
		 x1 = x1 + itr

	else:
		x1 = x1 + abc[(abc.find(itr)+28)%26]


print(x1)
#print(x1.maketrans())