import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow
from PyQt5.QtWidgets import QLabel, QLCDNumber
from HM1 import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.st = '->'
        self.pushButton.setText(self.st)
        self.pushButton.clicked.connect(self.inc_click)
        self.textBrowser_2.setText('Фокус')

    def inc_click(self):
        if self.st == '->':
            self.st = '<-'
            self.pushButton.setText(self.st)
            self.textBrowser.setText('Фокус')
            self.textBrowser_2.clear()
        else:
            self.st = '->'
            self.pushButton.setText(self.st)
            self.textBrowser_2.setText('Фокус')
            self.textBrowser.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
