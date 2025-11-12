import os
os.system('cls')
import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget,
                            QVBoxLayout, QHBoxLayout, QGridLayout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("PyQt5 Layouts Example")
        
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        
        top_label = QLabel("Top Label")
        top_label.setStyleSheet("background-color: lightblue;")
        main_layout.addWidget(top_label)
        
        middle_layout = QHBoxLayout()
        
        left_label = QLabel("Left Label")
        left_label.setStyleSheet("background-color: lightgreen;")
        middle_layout.addWidget(left_label)
        
        center_label = QLabel("Center Label")
        center_label.setStyleSheet("background-color: lightyellow;")
        middle_layout.addWidget(center_label)
        
        right_label = QLabel("Right Label")
        right_label.setStyleSheet("background-color: lightcoral;")
        middle_layout.addWidget(right_label)
        
        main_layout.addLayout(middle_layout)
        
        bottom_grid = QGridLayout()
        
        for i in range(2):
            for j in range(2):
                grid_label = QLabel(f"Grid {i},{j}")
                grid_label.setStyleSheet("background-color: lightgray; border: 1px solid black;")
                bottom_grid.addWidget(grid_label, i, j)
        
        main_layout.addLayout(bottom_grid)
        
        central_widget.setLayout(main_layout)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()