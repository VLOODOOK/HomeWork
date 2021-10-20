import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber
from HM_2 import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.func = lambda x: x.show() if x.isHidden() else x.hide()

        self.checkBox_1.stateChanged.connect(lambda: self.func(self.textBrowser))
        self.checkBox_2.stateChanged.connect(lambda: self.func(self.textBrowser_2))
        self.checkBox_3.stateChanged.connect(lambda: self.func(self.textBrowser_3))
        self.checkBox_4.stateChanged.connect(lambda: self.func(self.textBrowser_4))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
