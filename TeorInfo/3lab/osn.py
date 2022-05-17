from PIL import Image, ImageDraw
from numpy import asarray
import random
popa = []

def oshibki(a):
    spisok = [0, 1, 2, 3, 4, 5, 6, 7]
    ind = random.sample(spisok, 2)
    for i in range(len(ind)):
        if int(a[ind[i]]) == 0:
            a[ind[i]] = "1"
        else:
            a[ind[i]] = '0'
    return a


img = Image.open('two.jpg')
numpydata = asarray(img)

draw = ImageDraw.Draw(img)
width = img.size[0]
height = img.size[1]


for i in range(height):
    for j in range(width):
        popa = []
        for l in range(3):
            a = bin(numpydata[i][j][l])[2:].zfill(8)
            c = ''.join(oshibki(list(a)))
            popa.append(int(c,2))
        draw.point((j,i),(popa[0],popa[1],popa[2]))

img.show()