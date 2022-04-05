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












app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())