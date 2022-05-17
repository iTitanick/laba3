# Импорт Pyqt
from PyQt5 import QtWidgets
from sympy import *

import re
import sys

from dialog import  Ui_Dialog


class ClssDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(ClssDialog, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.push.clicked.connect(self.btnClicked)

    def btnClicked(self):

        # рекурсивная функция нахождения nod и коэффициентов
        def obr(one,mod):
            if one == 0:
                return (mod,0,1)
            else:
                nod,x,y = obr(mod%one,one)
            return (nod,y-(mod//one)*x,x)

        # функция выполняет в одних скобках действие и возвращает без них
        def skobki(a):
            for i in range(len(a)):
                if a[i] == "(" and a[i + 2] == ")":
                    a[i + 1] = str(eval(a[i + 1]))
                    a[i] = ''
                    a[i + 2] = ''
            # убираем пустые элементы списка
            c = list(filter(None, a))
            c = ''.join(a)
            op = re.split("([()])", c)
            return op


        try:
            stroka = self.ui.txt1.text()
            mod = int(self.ui.txt3.text())
            if "^" in stroka or "**" in stroka:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle('Ошибка!')
                msg.setText('Степень прописывать через умножение само на себя')
                msg.setIcon(msg.Warning)
                msg.exec()
            else:
                if isprime(mod):

                    # разбиваем по скобкам и подаем первый раз
                    a = re.split("([()])", stroka)
                    b = skobki(a)

                    # цикл для повторной подачи
                    while True:
                        if "(" in b:
                            b = skobki(b)
                        else:
                            break

                    stroka = ''.join(b)

                    print(stroka)

                    # разделение по знакам в список

                    spisok = re.split("([*\-+/])", stroka)

                    # замена циклом на обратные и на умножение
                    for i in range(len(spisok)):
                        if spisok[i] == "/":
                            obratni = obr(int(spisok[i + 1]), mod)
                            spisok[i + 1] = str(obratni[1] % mod)
                            spisok[i] = '*'

                    osnSTR = ''.join(spisok)

                    konec = eval(osnSTR) % mod

                    self.ui.label.setText(str(konec))
                else:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Ошибка!')
                    msg.setText('mod должен быть простым!')
                    msg.setIcon(msg.Warning)
                    msg.exec()

        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка!')
            msg.setText('Поля заполнены неправильно!')
            msg.setIcon(msg.Warning)
            msg.exec()


app = QtWidgets.QApplication([])
application = ClssDialog()
application.show()

sys.exit(app.exec())