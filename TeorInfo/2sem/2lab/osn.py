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










app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())