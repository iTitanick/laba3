from PIL import Image, ImageDraw
from numpy import asarray
import random
import numpy as np
from sympy import *
import math
ogoSpis =[]
esheSpis =[]
matrix = np.array([[1,0,0,0,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0],
 [0 ,1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
 [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0],
 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0],
 [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 1, 1],
 [0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1],
 [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0]])

popa = []

# УДАЛЕНИЕ ИЗ МАТРИЦЫ СТОЛБЦОВ ДЛЯ ЕДИНИЧНОЙ
def delite(matrix):
    pomoh = []
    stolbik = 0
    stolbik2 = 0
    ed = np.eye(len(matrix))
    for i in range(len(matrix)):
        stolbik = ed[:,i]
        for j in range(len(matrix[0])):
            stolbik2 = matrix[:,j]
            if (stolbik == stolbik2).all():
                pomoh.append(j)
                stolbik = 0
    matrix = np.delete(matrix,np.s_[pomoh],axis=1)
    return matrix


def oshibki(a):
    spisok = [0, 1, 2, 3, 4, 5, 6, 7]
    ind = random.sample(spisok, 2)
    for i in range(len(ind)):
        if int(a[ind[i]]) == 0:
            a[ind[i]] = "1"
        else:
            a[ind[i]] = '0'
    return a

def oshibki2(kod):
    spisok = [0, 1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17,18]
    ind = random.sample(spisok, 2)
    for i in range(len(ind)):
        if int(kod[ind[i]]) == 0:
            kod[ind[i]] = 1
        else:
            kod[ind[i]] = 0
    return kod

def spisok(kod):
    for i in range(len(kod)):
        if kod[i]% 2 == 0:
            kod[i] = 0
        if kod[i] > 1 and kod[i] % 2 != 0:
            kod[i] = 1
    return kod

img = Image.open('one.jpg')
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

wthSpis = []
matrix_c = np.dot(ogoSpis2,matrix3)
for i in range(len(matrix_c)):
    wth = 0
    for j in range(len(matrix_c[i])):
        if matrix_c[i][j] == 1:
            wth = wth + 1
        if matrix_c[i][j] % 2 == 0:
            matrix_c[i][j] = 0
        if matrix_c[i][j] > 1 & matrix_c[i][j] % 2 !=0:
            matrix_c[i][j] = 1
    wthSpis.append(wth)


#Выводы
# print("i",'     ',"C","               ","Wth")
# for i in range(len(ogoSpis)):
#     print(ogoSpis[i] ," ", matrix_c[i]," ",wthSpis[i])
# print("")

print("n =",len(matrix3[0])," ","k =",len(matrix3)," ","d =",min(wthSpis[1:]))
dmin = min(wthSpis[1:])
print("")

#Решение уровенения
x = Symbol('x')
t = solve(2*x + 1 - dmin, x)
t = math.floor(t[0])
ro = solve(x + 1 - dmin, x)
print("t =",t," ", "p =",ro[0])
print("")
if t == 0:
    print("Нечего исправлять")
    exit()

kodirovani = []
for i in range(height):
    for j in range(width):
        for l in range(3):
            a = bin(numpydata[i][j][l])[2:].zfill(8)
            a = list(map(int,a))
            kod = np.dot(a,matrix3)
            kod = spisok(kod)
            kodirovani.append(kod)

            sOshib = oshibki2(kod)
            print(sOshib)

#Вывод закодированных информационных слов
print("Вывод закодированных информационных слов:")
for i in kodirovani:
    print(i)