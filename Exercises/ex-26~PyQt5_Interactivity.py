import os
os.system('cls')
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QCheckBox, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700, 300, 500, 500)
        self.checkbox = QCheckBox("Do you like food?", self)

        self.radio1 = QRadioButton("Visa", self)
        self.radio2 = QRadioButton("MasterCard", self)
        self.radio_group = QButtonGroup(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("PyQt5 Interactivity Example")

        self.label = QLabel("Press the button", self)
        self.label.setGeometry(150, 50, 250, 50)
        self.label.setStyleSheet("font-size: 30px;")

        button = QPushButton("Click Me", self)
        button.setGeometry(150, 200, 200, 100)
        button.setStyleSheet("font-size: 30px;")
        button.clicked.connect(self.on_button_click)

        self.checkbox.setStyleSheet("font-size: 30px;"
                                    "font-family: Arial;")
        self.checkbox.setGeometry(150, 350, 300, 50)
        self.checkbox.stateChanged.connect(self.checkbox_changed)
         

        self.radio1.setStyleSheet("font-size: 30px;"
                                   "font-family: Arial;")
        self.radio1.setGeometry(150, 400, 200, 50)
        self.radio2.setStyleSheet("font-size: 30px;"
                                   "font-family: Arial;")
        self.radio2.setGeometry(300, 400, 200, 50)
        self.radio1.toggled.connect(self.radio_changed)
        self.radio2.toggled.connect(self.radio_changed)
        
        self.radio_group.addButton(self.radio1)
        self.radio_group.addButton(self.radio2)
    
    def radio_changed(self):
        selected_button = self.radio_group.checkedButton()
        if selected_button:
            self.label.setText(f"You selected: {selected_button.text()}")
            
    
    def checkbox_changed(self, state):
        if state == Qt.Checked:
            self.label.setText("You like food!")
        else:
            self.label.setText("You don't like food?")

        
    def on_button_click(self):
        self.label.setText("Button Clicked!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
    