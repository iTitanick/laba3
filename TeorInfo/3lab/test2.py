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


def spisok(self):
    for i in range(len(kod)):
        if kod[i]% 2 == 0:
            kod[i] = 0
        if kod[i] > 1 and kod[i] % 2 != 0:
            kod[i] = 1
    return kod

def oshibki2(self):
    spisok = [0, 1, 2, 3, 4, 5, 6, 7,8,9,10,11,12,13,14,15,16,17,18]
    ind = random.sample(spisok, 2)
    for i in range(len(ind)):
        if int(kod[ind[i]]) == 0:
            kod[ind[i]] = 1
        else:
            kod[ind[i]] = 0
    return kod

def decoder(a1,matrix2_t,matrica,matrix_t_S,matrix_c):
    # Вектор
    vectrospis = []
    vectrospisOsn = []
    vectrospis.append(a1)
    for i in vectrospis:
        qw = list(i)
        qw = list(map(int, qw))
        vectrospisOsn.append(qw)

    s_ = np.dot(vectrospisOsn, matrix2_t)
    for i in range(len(s_)):
        for j in range(len(s_[i])):
            if s_[i][j] % 2 == 0:
                s_[i][j] = 0
            if s_[i][j] % 2 != 0:
                s_[i][j] = 1


    opa = 0
    for i in range(len(matrica)):
        if (s_[0] == matrix_t_S[i]).all():
            opa = matrica[i]
    opa = np.array([opa])

    # Находим c': складываем векторы
    Cspis = []
    for i in range(len(vectrospisOsn)):
        for j in range(len(vectrospisOsn[i])):
            Cspis.append((vectrospisOsn[i][j] + opa[i][j]))
    c_ = np.array([Cspis])
    for i in range(len(c_)):
        for j in range(len(c_[i])):
            if c_[i][j] % 2 == 0:
                c_[i][j] = 0
            if c_[i][j] % 2 != 0:
                c_[i][j] = 1


    iii = 0
    for i in range(len(matrix_c)):
        if (c_[0] == matrix_c[i]).all():
            iii = ogoSpis2[i]
    iiM = np.array(int(''.join(map(str,iii)),2))
    return iiM


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

#Вторая часть(Вывод зашумленной)
for i in range(height):
    for j in range(width):
        popa = []
        for l in range(3):
            a = bin(numpydata[i][j][l])[2:].zfill(8)
            c = ''.join(oshibki(list(a)))
            popa.append(int(c,2))
        draw.point((j,i),(popa[0],popa[1],popa[2]))

img.show()


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

matrix = delite(matrix)
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




print("ЛИДЕРНОЕ ДЕКОДИРОВАНИЕ")
print("")

matrix2_t = np.transpose(matrix2)
print("Hsys-T")


print("")



print("e")
ogoSpis12 = []
for i in range(2**(19)):
    s = bin(i)[2:]
    ogoSpis12.append(s.zfill(19))

ogoSpis22 = []
for i in range(len(ogoSpis12)):
    if ogoSpis12[i].count("1") == 1:
        ogoSpis22.append(ogoSpis12[i])
    if ogoSpis12[i].count("1") == 2:
        ogoSpis22.append(ogoSpis12[i])

ogoSpis23 = []
for i in ogoSpis22:
    vot = list(i)
    vot = list(map(int,vot))
    ogoSpis23.append(vot)
matrica = np.array(ogoSpis23)



matrix_t_S =np.dot(matrica,matrix2_t)

for i in range(len(matrix_t_S)):
    for j in range(len(matrix_t_S[i])):
        if matrix_t_S[i][j] % 2 == 0:
            matrix_t_S[i][j] = 0
        if matrix_t_S[i][j] > 1 and matrix_t_S[i][j] % 2 !=0:
            matrix_t_S[i][j] = 1
print("S")

print("")


infSlovKodOSHI = []
infSlovKod =[]
infSlov = []
for i in range(height):
    for j in range(width):
        pop = []
        for l in range(3):
            a = bin(numpydata[i][j][l])[2:].zfill(8)
            infSlov.append(a)
            a = list(map(int, a))
            kod = np.dot(a, matrix3)
            kod1 = spisok(kod).tolist()
            infSlovKod.append(kod1)
            a1 = oshibki2(kod1).tolist()
            infSlovKodOSHI.append(oshibki2(kod1).tolist())
            pop.append((decoder(a1,matrix2_t,matrica,matrix_t_S,matrix_c)).tolist())
        draw.point((j,i),(pop[0],pop[1],pop[2]))
img.show()



# print("Информационные слова:\n",infSlov)
# print("Закодированные информационные слова:\n",infSlovKod)
# print("Закодированные информационные слова с ошибкой:\n",infSlovKodOSHI)

