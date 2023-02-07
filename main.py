import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit, QPushButton


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a grid layout
        grid = QGridLayout()
        self.setLayout(grid)

        # Create the display and buttons
        self.display = QLineEdit()
        grid.addWidget(self.display, 0, 0, 1, 4)
        buttons = ['AC', '+', '-', '*', '/', '7', '8', '9', '(', ')', '4', '5', '6', '%', '1/x', '1', '2', '3', '=',
                   '0', '.']
        positions = [(i, j) for i in range(1, 6) for j in range(4)]
        for position, button in zip(positions, buttons):
            if button == '':
                continue
            button = QPushButton(button)
            grid.addWidget(button, *position)

        # Set the window properties
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 300, 300, 300)

    def calculate(self, num1, num2, operator):
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            return num1 / num2
        else:
            return 'Invalid operator'


if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())

