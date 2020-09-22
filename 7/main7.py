from PIL import Image

img = Image.open("oxygen.png")

print(type(img.getpixel((0,0))))

msg = ""
for x in range(0,img.size[0], 7):
	pix = img.getpixel((x,47))
	if pix[0] == pix[1] ==pix[2]:
		#print(chr(pix[0]), end='')
		msg += (chr(pix[0]))

lst = [105, 110, 116, 101, 103, 114, 105, 116, 121]
[print(chr(l), end='') for l in lst]


