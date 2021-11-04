import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton
from PyQt5.QtWidgets import QLabel, QLCDNumber
from HM_5 import Ui_MainWindow


class Example(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.count = 0
        self.radioButton.setChecked(True)
        self.lst = ['1', '2', '3',
                    '4', '5', '6',
                    '7', '8', '9']

        self.lst_button = [self.pushButton, self.pushButton_2, self.pushButton_3,
               self.pushButton_4, self.pushButton_5, self.pushButton_6,
               self.pushButton_7, self.pushButton_8, self.pushButton_9]

        for i in self.lst_button:
            i.clicked.connect(lambda ch, name=i: self.run(name))

        self.pushButton_10.clicked.connect(self.newgame)

    def run(self, name):

        self.count += 1
        name.setEnabled(False)

        if self.radioButton.isChecked() and self.count % 2 != 0:
            name.setText('X')
            name.setFont(QFont('Times', 35))
            self.lst[self.lst_button.index(name)] = 'X'
        elif not self.radioButton_2.isChecked():
            name.setText('O')
            name.setFont(QFont('Times', 35))
            self.lst[self.lst_button.index(name)] = 'O'

        if self.radioButton_2.isChecked() and self.count % 2 != 0:
            name.setText('O')
            name.setFont(QFont('Times', 35))
            self.lst[self.lst_button.index(name)] = 'O'
        elif not self.radioButton.isChecked():
            name.setText('X')
            name.setFont(QFont('Times', 35))
            self.lst[self.lst_button.index(name)] = 'X'

        if self.check_win(self.lst):
            self.label.setText(f'Победил {self.check_win(self.lst)}!')
            self.label.setFont(QFont('Times', 40))
            for i in self.lst_button:
                i.setEnabled(False)
            self.lst = ['1', '2', '3',
                        '4', '5', '6',
                        '7', '8', '9']
            self.count = 0

        if self.count == 9:
            self.label.setText('Ничья')
            self.label.setFont(QFont('Times', 40))

    def newgame(self):
        for i in self.lst_button:
            i.setText('')
        self.label.setText('')
        for i in self.lst_button:
            i.setEnabled(True)
        self.lst = ['1', '2', '3',
                    '4', '5', '6',
                    '7', '8', '9']
        self.count = 0

    def check_win(self, board):
        win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for each in win_coord:
            if board[each[0]] == board[each[1]] == board[each[2]]:
                return board[each[0]]
        return False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
