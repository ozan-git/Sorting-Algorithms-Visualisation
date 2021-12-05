# Introduction to Algorithm course graphical interface design project help page.
# 5 December 2021.

# Written by Orhan Ozan Yildiz.
from uiqt_help import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtGui import QIntValidator
from PyQt5.QtCore import Qt
import sys

class HelpWindow(QMainWindow):
    def __init__(self):
       super().__init__() 
       self.ui = Ui_MainWindow()                                         
       self.ui.setupUi(self)
       
       
       
     
       
  #%% Initialization       
if __name__ == "__main__":
    app = QApplication([])
    window = HelpWindow()
    window.show()
    sys.exit(app.exec_())