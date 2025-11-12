import os
os.system("cls" if os.name == "nt" else "clear")
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.setWindowTitle("QLineEdit Example")
        self.initUI()

    def initUI(self):
        self.line_edit.setPlaceholderText("Enter your text here...")
        self.line_edit.setGeometry(50, 50, 400, 40)
        self.line_edit.textChanged.connect(self.on_text_changed)
        self.line_edit.setStyleSheet("font-size: 16px; padding: 5px;")

        self.button.setGeometry(200, 120, 100, 40)
        self.button.setStyleSheet("font-size: 16px;")
        self.button.clicked.connect(self.on_button_click)

    def on_button_click(self):
        text = self.line_edit.text()
        print(f"Button clicked! Text entered: {text}")
        
    def on_text_changed(self, text):
        print(f"Current text: {text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())