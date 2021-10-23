import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit

s = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
}


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        self.setGeometry(900, 100, 900, 100)
        c = 10
        self.line = QLineEdit(self)
        self.line.resize(780, 30)
        self.line.move(10, 50)
        self.txt = ''

        for i in s:
            self.btn = QPushButton(i, self)
            self.btn.resize(30, 30)
            self.btn.move(c, 10)
            self.btn.clicked.connect(lambda ch, name=i: self.letter(name))
            c += 30

    def letter(self, name):
        self.txt += s[name]
        self.line.setText(self.txt)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
