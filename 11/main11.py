
from PIL import Image

cave = Image.open("cave.jpeg")
print(cave)

odd = Image.new('RGB', cave.size)
even = Image.new('RGB', cave.size)

for x in range(cave.size[0]):
	for y in range(cave.size[1]):
		if (x*y)%2==0:
			even.putpixel((x,y), cave.getpixel((x,y)))
		else:
			odd.putpixel((x,y), cave.getpixel((x,y)))

odd.show()
even.show()

#evil