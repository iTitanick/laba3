import numpy
import binascii
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from main import  Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QInputDialog

import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('C:/Users/doner/Downloads/icon.png'))
        self.ui.pushButton_3.clicked.connect(self.summatori)
        self.ui.pushButton.clicked.connect(self.kodirovanie)
        self.ui.pushButton_2.clicked.connect(self.dekodirovanie)
        self.ui.pushButton_7.clicked.connect(self.zdorovo)


    def zdorovo(self):
        msg = QtWidgets.QMessageBox()
        ret = QMessageBox.question(self, 'Вопрос', "Здорово?",
                                   QMessageBox.Yes | QMessageBox.No)
        if ret == QMessageBox.Yes:
            ret = QMessageBox.question(self, 'Вопрос', "Великолепно?",
                                       QMessageBox.Yes | QMessageBox.No)
            if ret == QMessageBox.Yes:
                ret = QMessageBox.question(self, 'Вопрос', "По факту?",
                                           QMessageBox.Yes | QMessageBox.No)
                if ret == QMessageBox.Yes:
                    ret = QMessageBox.question(self, 'Утверждение', "Тогда поставьте 5+ (´･ᴗ･ )",
                                               QMessageBox.Yes)
                    if ret == QMessageBox.Yes:
                        sys.exit()

    def summatori(self):
        try:
            global kolvo
            global razrad
            global sum

            # Количество сумматоров
            kolvo = int(self.ui.txt1.text())
            razrad = [0,0,0]
            spisick =[]
            pomosh = True
            #Ввод сумматоров
            for i in range(kolvo):
                spisi, ok = QInputDialog.getText(self, 'Input Dialog',
                                         'Введите индексы через запятую:')
                spisi2 = spisi.split(',')
                for j in range(len(spisi2)):
                    spisi2[j] = int(spisi2[j])
                    if spisi2[j] > 3:
                        pomosh = False
                if pomosh == False:
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle('Ошибка!')
                    msg.setText('Индекс вышел за рамки')
                    msg.setIcon(msg.Warning)
                    msg.exec()
                    break

                spisick.append(spisi2)

                # Сумматоры в списке списков
                sum = numpy.array(spisick)
                print("Сумматоры:\n", sum)
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка!')
            msg.setText('Поля заполнены неправильно!')
            msg.setIcon(msg.Warning)
            msg.exec()


    def kodirovanie(self):
        try:
            global slov
            global kodirov
            # Перевод в бинарную
            def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
                bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
                return bits.zfill(8 * ((len(bits) + 7) // 8))

            # Ввод строки
            vvodText = self.ui.txt1_2.text()

            # Бинарное представление текста
            binText = text_to_bits(vvodText)
            print("Бинарное представление текста:\n", binText)
            kodirov = []

            spisok2 = list(binText)
            print("Список бинарный:\n", spisok2)

            slov = {}
            pomogite1 = []  # список с состояниями регистра
            pomogite2 = []  # список с суммами регистров

            # Кодирование
            for i in range(len(spisok2)):
                spisok2[i] = int(spisok2[i])
                razrad.insert(0, spisok2[i])
                razrad.pop(-1)
                pomogite1.append("".join(map(str, razrad)))
                razrad2 = numpy.array(razrad)
                for j in range(len(sum)):
                    sum2 = numpy.array(sum[j])
                    kodirov.append(str(razrad2[sum2 - 1].sum() % 2))
            print("Закодированная последовательность:\n", kodirov)
            self.ui.label.setText(''.join(kodirov))

            for i in range(0, len(kodirov), kolvo):
                pomogite2.append(''.join(map(str, kodirov[i:i + kolvo])))

            for i in range(len(pomogite1)):
                slov[pomogite1[i]] = pomogite2[i]
            print("Словарь:\n", slov)
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка!')
            msg.setText('Поля заполнены неправильно!')
            msg.setIcon(msg.Warning)
            msg.exec()


    def dekodirovanie(self):
        def vslovare(registrdec):
            for i in slov.keys():
                if list(i) == registrdec:
                    return i

        decodirov = ""

        # Декодирование
        registrdec = []
        for i in range(3):
            registrdec.append('0')
        for i in range(0, len(kodirov), kolvo):
            del registrdec[-1]
            registrdec.insert(0, '1')

            if "".join(map(str, kodirov[i:i + int(kolvo)])) == slov.get(vslovare(registrdec)):
                decodirov += '1'
            else:
                del registrdec[0]
                registrdec.insert(0, '0')
                if "".join(map(str, kodirov[i:i + int(kolvo)])) == slov.get(vslovare(registrdec)):
                    decodirov += '0'

        print("Декодирование:\n", decodirov)

        # перевод обратный
        def text_from_bits(binstring, encoding='utf-8', errors='surrogatepass'):
            n = int(binstring, 2)
            return int2bytes(n).decode(encoding, errors)

        def int2bytes(i):
            hex_string = '%x' % i
            n = len(hex_string)
            return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

        konec = text_from_bits(decodirov)

        print("Перевод обратно в строку:\n", konec)

        self.ui.label_2.setText(''.join(konec))



app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())