from PyQt5.QtWidgets import QApplication, QLabel, QDialog, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap

class window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "checking image"
        self.top = 100
        self.left = 100
        self.width = 400
        self.height = 300
        self.iconName = "DOOM.png"
        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)

        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap("gaiphy.gif")
        labelImage.setPixmap(pixmap)
        vbox.addWidget(labelImage)
        self.setLayout(vbox)
        self.show()




App = QApplication(sys.argv)
window = window()
sys.exit(App.exec())