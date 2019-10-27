from PyQt5.QtWidgets import QMainWindow,QLineEdit, QWidget,QApplication,QHBoxLayout,QLabel
import sys
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QRect


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "pyqt5 line edit testing"
        self.top  = 100
        self.left = 100
        self.width =  400
        self.height = 300
        self.IconName = "/root/Desktop/test.png"

        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left,self.top,self.width,self.height)

        hbox = QHBoxLayout()
        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont("sanserif,15"))
        self.lineedit.returnPressed.connect(self.onPressed)
        hbox.addWidget(self.lineedit)
        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("sanserif,15"))
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.show()
        #self.InitWindow()

    def onPressed(self):
        self.label.setText(self.lineedit.text())




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = window()
    sys.exit(app.exec())