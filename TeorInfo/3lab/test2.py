from PIL import Image, ImageDraw
from numpy import asarray
import random
import numpy as np
from sympy import *
import math

def oshibki(a):
    spisok = [0, 1, 2, 3, 4, 5, 6, 7]
    ind = random.sample(spisok, 2)
    for i in range(len(ind)):
        if int(a[ind[i]]) == 0:
            a[ind[i]] = "1"
        else:
            a[ind[i]] = '0'
    return a


img = Image.open('one1.jpg')
numpydata = asarray(img)

draw = ImageDraw.Draw(img)
width = img.size[0]
height = img.size[1]
#Первая часть(вывод обычной картинки)
for i in range(height):
    for j in range(width):
        draw.point((j,i),(numpydata[i][j][0],numpydata[i][j][1],numpydata[i][j][2]))

img.show()

