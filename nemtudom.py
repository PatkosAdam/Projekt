# importing libraries 
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5 import QtCore
import sys

# create pyqt5 app 
App = QApplication(sys.argv) 

class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
  
        # setting title 
        self.setWindowTitle("Fájlbeszkennelős izébizé") 
  
        # setting geometry 
        self.setGeometry(100, 100, 300, 300) 
  
        # UI elements 
        file_button = QPushButton("Browse files", self) 
        file_button.setGeometry(100, 130, 100, 30) # setting geometry of button 
        file_button.clicked.connect(self.clickme) # adding action to the button 

        close_button = QPushButton("Exit", self) # creating close button
        close_button.setGeometry(100, 180, 100, 30) #setting geometry to the button
        close_button.clicked.connect(self.closeApp) # action
        close_button.setStyleSheet("border :3px solid blue;" 
                                    "border-radius: 8px;") #button styling

        text = QLabel('choose a file', self)
        text.setGeometry(0, 0, 300, 100)
        text.setStyleSheet("color: blue;"
                            "background-color: lightgray;"
                            "text-align: center;") #label styling
        text.setAlignment(QtCore.Qt.AlignCenter)

        # showing all the widgets 
        self.show() 
  
    # action method 
    def clickme(self): 
        file_to_scan = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "PDF file (*.pdf)") #asking for file / file explorer popping up
        return file_to_scan

    def closeApp(self):
        sys.exit()
        print("exit")
  
# create the instance of our Window 
window = Window() 
  
# start the app 
sys.exit(App.exec()) 