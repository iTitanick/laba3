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
















app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())