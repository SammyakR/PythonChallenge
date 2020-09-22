from PIL import Image

evil = open("evil2.gfx", 'rb')

evil1 = evil.read()

for i in range(5):
	open('%d.jpg' % i ,'wb').write(evil1[i::5])

