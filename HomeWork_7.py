import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber
from HM_7 import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.line_lst = [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4]
        self.l = [self.checkBox, self.checkBox_2,
                  self.checkBox_3, self.checkBox_4]
        self.listWidget.setEnabled(False)
        self.pushButton.clicked.connect(self.run)
        for i in range(len(self.l)):
            self.line_lst[i].setEnabled(False)
            self.l[i].clicked.connect(self.run_check)

    def run(self):
        self.listWidget.clear()
        self.listWidget.addItem('Ваш заказ:')
        self.listWidget.addItem('')
        lst = ['Чизбургер', 'Гамбургер',
               'Кока-кола', 'Нагетсы']
        lst_price = [15, 25, 15, 10]
        final_price = 0
        for i in range(len(self.l)):
            final_price += int(self.line_lst[i].text()) * lst_price[i]
            if self.l[i].isChecked():
                self.listWidget.addItem(f'{lst[i]}-----{self.line_lst[i].text()}---'
                                        f'--{int(self.line_lst[i].text()) * lst_price[i]}')
        self.listWidget.addItem('')
        self.listWidget.addItem(f'Итог: {final_price}')

    def run_check(self):
        for i in range(len(self.l)):
            if self.l[i].isChecked():
                self.line_lst[i].setText('1')
                self.line_lst[i].setEnabled(True)
            else:
                self.line_lst[i].setText('0')
                self.line_lst[i].setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
