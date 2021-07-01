import sys

from PIL import Image

import os

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QTextBrowser, QVBoxLayout
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QDialog, QFileDialog
from PyQt5.QtGui import QPixmap


class MainForm(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI\mainpage.ui', self)
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Главная')

        self.pixmap = QPixmap('IMAGE\im.jpg')
        self.label_2.setPixmap(self.pixmap)

        self.action_3.triggered.connect(self.open_reference)
        self.action_4.triggered.connect(self.open_anec)

        self.pushButton.clicked.connect(self.open_pict)


    def open_reference(self):
        '''Открыть справку'''
        self.ref = Reference(self)
        self.ref.show()

    def open_pict(self):
        '''Выбрать изображение для поиска'''
        self.close()
        self.pict = SavePict(self)
        self.pict.show()

    def open_anec(self):
        self.ref = Anec(self)
        self.ref.show()

class Reference(QWidget):
    '''Справка'''
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('UI\info.ui', self)
        self.initUI()
        self.pushButton.clicked.connect(self.close_ref)

    def initUI(self):
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Справка')

        with open('TEXT\info.txt', 'r', encoding='utf-8') as f:
            self.textBrowser.setText(f.read())

    def close_ref(self):
        '''Закрыть справку'''
        self.close()


class Anec(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('UI\info.ui', self)
        self.initUI()
        self.pushButton.clicked.connect(self.close_ref)

    def initUI(self):
        self.setGeometry(300, 300, 700, 500)
        self.setWindowTitle('Анекдот!')

        with open('TEXT\onec.txt', 'r', encoding='utf-8') as f:
            self.textBrowser.setText(f.read())

    def close_ref(self):
        self.close()


class SavePict(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.open_res()

    def open_res(self):
        with open("TEXT\counter.txt", "r") as f:
            count = int(f.readline())

        workfile = QFileDialog.getOpenFileName(filter="Images (*.png *.jpg *.bmp) ")[0]
        count += 1
        with open("TEXT\counter.txt", "w") as f:
            f.write(str(count))
        k = workfile.rfind('.')
        pictname = "data\pic" + str(count) + "." + workfile[k+1:]
        print(pictname)
        os.replace(workfile, pictname)
        prov("\pic" + str(count) + "." + workfile[k+1:])


def prov(pictname):
    pictname = "changed" + pictname
    img = Image.open(pictname)
    img.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainForm()
    ex.show()
    sys.exit(app.exec())

