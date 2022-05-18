from PIL import Image, ImageDraw
from numpy import asarray
import random
import numpy as np
from sympy import *
import math

matrix = np.array([[1,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0],
 [0 ,1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]])


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

# img.show()

#Вторая часть(Вывод зашумленной)
for i in range(height):
    for j in range(width):
        popa = []
        for l in range(3):
            a = bin(numpydata[i][j][l])[2:].zfill(8)
            c = ''.join(oshibki(list(a)))
            popa.append(int(c,2))
        draw.point((j,i),(popa[0],popa[1],popa[2]))

# img.show()


#Третья часть

#Gsys
matrix3 = np.array([[1,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0],
 [0 ,1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]])

#Hsys
matrix2 = matrix.transpose()
ed = np.eye(len(matrix2))
matrix2 = np.append(matrix2, ed, axis=1)
# print("Матрица Hsys")
# vivodMAT(matrix2)

#i нахождение
ogoSpis = []
for i in range(2**(len(matrix3))):
    s = bin(i)[2:]
    ogoSpis.append(s.zfill(len(matrix3)))
#print(ogoSpis)

ogoSpis2 = []
for i in ogoSpis:
    vot = list(i)
    vot = list(map(int,vot))
    ogoSpis2.append(vot)
# print(ogoSpis2)