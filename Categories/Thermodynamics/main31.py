import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox

class AreaCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Rectangle Area Calculator')
        self.setGeometry(100, 100, 300, 200)

        # Create widgets
        self.length_label = QLabel('Length:', self)
        self.length_input = QLineEdit(self)
        
        self.width_label = QLabel('Width:', self)
        self.width_input = QLineEdit(self)

        self.calculate_button = QPushButton('Calculate Area', self)
        self.calculate_button.clicked.connect(self.calculate_area)

        # Create layout
        layout = QVBoxLayout()
        layout.addWidget(self.length_label)
        layout.addWidget(self.length_input)
        layout.addWidget(self.width_label)
        layout.addWidget(self.width_input)
        layout.addWidget(self.calculate_button)

        self.setLayout(layout)

    def calculate_area(self):
        try:
            length = float(self.length_input.text())
            width = float(self.width_input.text())
            area = length * width
            QMessageBox.information(self, 'Area Calculation', f'The area of the rectangle is: {area}')
        except ValueError:
            QMessageBox.warning(self, 'Input Error', 'Please enter valid numeric values.')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AreaCalculator()
    window.show()
    sys.exit(app.exec_())
