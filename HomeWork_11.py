import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from HM_11 import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        with open('input.txt', 'r', encoding='utf-8') as f:
            count = 0
            lst_ch = []
            lst_nch = []
            for i in f.readlines():
                count += 1
                if count % 2 == 0:
                    lst_ch.append(i)
                else:
                    lst_nch.append(i)

        for i in lst_nch:
            self.listWidget.addItem(' '.join(i.split()))
        for i in lst_ch:
            self.listWidget.addItem(' '.join(i.split()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
