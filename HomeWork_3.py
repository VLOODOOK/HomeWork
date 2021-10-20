import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber
from HM_3 import Ui_mainWindow


class Example(QMainWindow, Ui_mainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit_3.setReadOnly(True)
        self.pushButton.clicked.connect(self.click_plus)
        self.pushButton_2.clicked.connect(self.click_minus)
        self.pushButton_3.clicked.connect(self.click_multiply)

    def click_plus(self):
        if self.lineEdit_1.text() != '' and self.lineEdit_2.text() != '':
            self.lineEdit_3.setText(f'{int(self.lineEdit_1.text()) + int(self.lineEdit_2.text())}')

    def click_minus(self):
        if self.lineEdit_1.text() != '' and self.lineEdit_2.text() != '':
            self.lineEdit_3.setText(f'{int(self.lineEdit_1.text()) - int(self.lineEdit_2.text())}')

    def click_multiply(self):
        if self.lineEdit_1.text() != '' and self.lineEdit_2.text() != '':
            self.lineEdit_3.setText(f'{int(self.lineEdit_1.text()) * int(self.lineEdit_2.text())}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
