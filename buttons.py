from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QDialog
import sys
from PyQt5 import QtGui, QtCore
class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "push wala button"
        self.top  = 100
        self.left = 100
        self.width =  400
        self.height = 300
        self.InitWindow()



    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("/root/Desktop/test.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.uicomponents()
        self.uicomponents2()

        self.show()

    def uicomponents(self):
        button = QPushButton("SI process",self)
        button.move(50,50)
        button.setToolTip("hi there click me")
        button.clicked.connect(self.click)
    def click(self):
        print("used the button")

    def out(self):
        sys.exit()
    def uicomponents2(self):
        button = QPushButton("Get out", self)
        button.setIcon(QtGui.QIcon("/root/Desktop.test.png"))
        button.clicked.connect(self.out)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window=window()
    sys.exit(app.exec())