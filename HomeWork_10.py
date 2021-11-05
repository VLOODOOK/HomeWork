import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from HM_10 import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.run)

    def run(self):
        st = self.lineEdit.text()
        self.label_5.setText("")
        try:
            with open(st, 'r') as f:
                lst = [float(i) for i in f.read().split()]
                mx = str(max(lst))
                mn = str(min(lst))
                medium = str(sum(lst) / len(lst))
            with open('output.txt', 'w') as f:
                f.write('\n')
                f.write(mx + '\n')
                f.write(mn + '\n')
                f.write(medium + '\n')
            self.lineEdit_2.setText(mx)
            self.lineEdit_3.setText(mn)
            self.lineEdit_4.setText(medium)
        except FileNotFoundError:
            self.label_5.setText(f"Файл '{st}' не наден")
        except ValueError:
            self.label_5.setText(f"В файле ''{st}' некорректная информация")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
