import sys
from functools import partial
from PyQt5.Qt import *


class PushButton(QPushButton):
    def __init__(self, text, parent=None):
        super(PushButton, self).__init__(text, parent)
        self.setText(text)
        self.setMinimumSize(QSize(50, 50))
        self.setMaximumSize(QSize(50, 50))
        self.setText("0")
        self.setStyleSheet("background-color: grey")


class GenerateButton(QPushButton):
    def __init__(self, text, parent=None):
        super(GenerateButton, self).__init__(text, parent)
        self.setText(text)
        self.setMinimumSize(QSize(50, 50))
        self.setMaximumSize(QSize(50, 50))
        self.setText("GO")
        self.setStyleSheet("background-color: orange")


class ClearButton(QPushButton):
    def __init__(self, text, parent=None):
        super(ClearButton, self).__init__(text, parent)
        self.setText(text)
        self.setMinimumSize(QSize(50, 50))
        self.setMaximumSize(QSize(50, 50))
        self.setText("CLEAR")
        self.setStyleSheet("background-color: blue")


class MyWindow(QMainWindow):
    valueHolder = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def __init__(self):
        super(MyWindow, self).__init__()

        self.rows = 8
        self.columns = 8

        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        self.label = QLabel(self, alignment=Qt.AlignRight)
        self.label.setFont(QFont("Times", 12, QFont.Bold))

        self.layout = QGridLayout(centralWidget)
        self.layout.addWidget(self.label, 0, 0, 1, 3)

        _list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        len_list = len(_list)

        i = 0
        for row in range(self.rows):
            for column in range(self.columns):
                button = PushButton(f'{_list[i]}', self)
                button.clicked.connect(partial(self.matrixButtonClick, button, row, column))
                self.layout.addWidget(button, row + 1, column)
                i += 1
                if i == len_list: break

        # create button
        createButton = GenerateButton('Generate button', self);
        self.layout.addWidget(createButton, 1, 10)
        createButton.clicked.connect(partial(self.createButtonClicked, createButton))

        # clear button
        clearButton = ClearButton('Clear button', self);
        self.layout.addWidget(clearButton, 1, 11)
        clearButton.clicked.connect(partial(self.clearButtonClicked, clearButton))

    def matrixButtonClick(self, button, row, column):
        if button.text() == "0":
            button.setStyleSheet("background-color: red")
            button.setText("1")
            self.valueHolder[row][column] = 1
        else:
            button.setStyleSheet("background-color: grey")
            button.setText("0")
            self.valueHolder[row][column] = 0

    def createButtonClicked(self, button):
        print("byte pattern[] = {")
        for row in range(8):
            rowToPrint = "B"
            for column in range(8):
                rowToPrint = rowToPrint + str(self.valueHolder[column][row])
            if row != 8:
                rowToPrint = rowToPrint + ","
            print(rowToPrint)
        print("};")

    def clearButtonClicked(self, button):
        print("TO DO")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.setWindowTitle('Calcolatrice')
    w.show()
    sys.exit(app.exec_())
