import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from HM_12 import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.create_file)
        self.pushButton_2.clicked.connect(self.save_file)
        self.pushButton_3.clicked.connect(self.open_file)

    def create_file(self):
        with open(self.lineEdit.text(), 'w+', encoding='utf-8') as f:
            f.write(self.plainTextEdit.toPlainText())
        self.plainTextEdit.setPlainText('')

    def save_file(self):
        with open(self.lineEdit.text(), 'w', encoding='utf-8') as f:
            f.write(self.plainTextEdit.toPlainText())

    def open_file(self):
        with open(self.lineEdit.text(), 'r', encoding='utf-8') as f:
            self.plainTextEdit.setPlainText(f.read())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
