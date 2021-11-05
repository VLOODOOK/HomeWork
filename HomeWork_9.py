import sys
import random
from PyQt5.QtWidgets import QApplication, QMainWindow
from HM_9 import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        with open('input.txt', 'r', encoding='utf-8') as f:
            self.textEdit.setText(*random.choices(f.readlines()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())

