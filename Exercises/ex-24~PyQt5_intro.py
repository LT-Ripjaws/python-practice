import os
os.system('cls')
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QIcon # Import QIcon for setting window icon
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtCore import Qt # used for alignments

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My First PyQt5 App")
        self.setGeometry(0,0,500,500) # x, y, width, height
        self.setWindowIcon(QIcon("./data/icon.png")) #Setting the window icon path.
        
        Label = QLabel("Hello, PyQt5!", self) # self refers to the window object we are instantiating
        Label.setFont(QFont("Arial", 30))
        Label.setGeometry(0,0,500,100)
        Label.setStyleSheet("color: black;"
                            '''background-color: qlineargradient(
                                                                x1: 0, y1: 0, 
                                                                x2: 1, y2: 0, 
                                                                stop: 0 #ffcccc, 
                                                                stop: 1 #66ccff
                                                            );'''
                            "border: 2px solid black;"
                            "border-radius: 10px;"
                            "padding: 10px;"
                            "font-weight: bold;"
                            "font-style: italic;")

        Label.setAlignment(Qt.AlignCenter) # Center the text within the label
        
        label2 = QLabel(self)
        label2.setGeometry(50,150,400,300)
        pixmap = QPixmap("./data/pp.jpg")
        label2.setPixmap(pixmap)
        label2.setScaledContents(True) # Scale the pixmap to fit the label size
        
        label2.setGeometry((self.width() - label2.width()) // 2,
                           (self.height() - label2.height()) // 2,
                           label2.width(),
                           label2.height()) # Center the image label within the main window


def main():
    app = QApplication(sys.argv) # Create an instance of QApplication
    window = MainWindow() # Create an instance of MainWindow
    window.show()
    sys.exit(app.exec_()) # Start the application's event loop and exit cleanly
if __name__ == "__main__":
    main()