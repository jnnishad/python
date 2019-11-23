from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QDialog,QVBoxLayout
import sys
from PyQt5 import QtGui,QtCore
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap


class window(QDialog):
        def __init__(self):
            super().__init__()
            self.title = "Atom process"
            self.top = 50
            self.left = 50
            self.width = 300
            self.height = 150
            self.iconName="DOOM.png"
            self.InitWindow()

        def InitWindow(self):
            self.setWindowIcon(QtGui.QIcon(self.iconName))
            self.setGeometry(self.left,self.top,self.width,self.height)
            self.setWindowTitle(self.title)

            #image = QtGui.QImage("background.jpg")
            #layout = QVBoxLayout()
            #layout.addWidget(image)
            #self.setLayout(layout)
            #vbox = QVBoxLayout()
            #labelImage = QLabel(self)
            #pixmap = QPixmap("floppy.jpg")
            #labelImage.setPixmap(pixmap)
            #vbox.addWidget(labelImage)
            #self.setAutoFillBackground(True)
            #self.setLayout(vbox)

            self.Uicomponent()
            self.Uicomponent1()
            self.Uicomponent2()
            self.Uicomponent3()
            self.show()

        def Uicomponent(self):
            button = QPushButton("LOGS",self)
            button.setGeometry(QRect(100,20,111,28))
            button.setIcon(QtGui.QIcon("gaiphy.gif"))
            button.setIconSize(QtCore.QSize(20,20))


        def Uicomponent1(self):
            button = QPushButton("PG",self)
            button.setGeometry(QRect(100,50,111,28))
            button.setIcon(QtGui.QIcon("gaiphy.gif"))
            button.setIconSize(QtCore.QSize(20,20))

        def Uicomponent2(self):
            button = QPushButton("SI",self)
            button.setGeometry(QRect(100,80,111,28))
            button.setIcon(QtGui.QIcon("gaiphy.gif"))
            button.setIconSize(QtCore.QSize(20,20))


        def Uicomponent3(self):
            button = QPushButton("EXIT",self)
            button.setGeometry(QRect(100,110,111,28))
            button.setIcon(QtGui.QIcon("gaiphy.gif"))
            button.setIconSize(QtCore.QSize(20,20))
            sys.exit

App = QApplication(sys.argv)
window = window()
sys.exit(App.exec())
