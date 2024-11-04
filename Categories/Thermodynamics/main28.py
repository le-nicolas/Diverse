import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Set the title and size of the window
        self.setWindowTitle('Simple PyQt5 App')
        self.setGeometry(100, 100, 300, 200)

        # Create a button
        self.button = QPushButton('Click Me', self)
        self.button.clicked.connect(self.show_message)

        # Create a layout and add the button to it
        layout = QVBoxLayout()
        layout.addWidget(self.button)

        # Set the layout for the window
        self.setLayout(layout)

    def show_message(self):
        # Show a message box when the button is clicked
        QMessageBox.information(self, 'Message', 'Button Clicked!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
