import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber
from HM_6 import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.listWidget.clear()
        self.listWidget.addItem('Ваш заказ:')
        self.listWidget.addItem('')
        l = [self.checkBox.isChecked(), self.checkBox_2.isChecked(),
             self.checkBox_3.isChecked(), self.checkBox_4.isChecked()]
        lst = ['Чизбургер', 'Гамбургер',
               'Кока-кола', 'Нагетсы']
        for i in range(len(l)):
            if l[i]:
                self.listWidget.addItem(lst[i])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
