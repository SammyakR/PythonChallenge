from PIL import Image

wire = Image.open('wire.png','r')

new_wire = Image.new('RGB', (100,100))

xmin,xmax = 0,99
ymin,ymax = 0,99
i,j,k = 0,0,0

while xmin<=xmax and ymin<=ymax:
	while j<=xmax:
		print(i, j, k)
		color = wire.getpixel((k,0))
		new_wire.putpixel((i,j), color)
		j=j+1
		k=k+1
	ymin=ymin+1
	i=ymin
	j=j-1

	while i<=ymax:
		print(i, j, k)
		color = wire.getpixel((k,0))
		new_wire.putpixel((i,j), color)
		i=i+1
		k=k+1
	xmax = xmax-1
	j=xmax
	i=i-1

	while j>=xmin:
		print(i, j, k)
		color = wire.getpixel((k,0))
		new_wire.putpixel((i,j), color)
		j=j-1
		k=k+1

	ymax=ymax-1
	i=ymax
	j=j+1

	while i>=ymin:
		print(i, j, k)
		color = wire.getpixel((k,0))
		new_wire.putpixel((i,j), color)
		i=i-1
		k=k+1
	xmin =xmin+1
	j=xmin
	i = i+1

new_wire.save("result.png")
new_wire.show()
