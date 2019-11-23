import sys
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QMovie, QPainter,QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget


class UItab(QWidget):
    def __init__(self,parent=None):
        super(UItab,self).__init__(parent)
        self.resize(QSize(600,750))
        self.ToolsBTN = QPushButton('tab_check',self)
        self.ToolsBTN.resize(100, 40)
        self.ToolsBTN.move(60,300)

        self.CPS = QPushButton('tab_check1',self)
        self.ToolsBTN.resize(100,40)
        self.ToolsBTN.move(130,300)

        self.CPS = QPushButton('tab_check2', self)
        self.ToolsBTN.resize(100, 40)
        self.ToolsBTN.move(260, 50)

class MainWindow(QMainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setGeometry(50,50,300,500)
        self.setFixedSize(600,750)
        self.startUItab()

        self.movie = QMovie("giphy.gif")
        self.movie.frameChanged.connect(self.repaint)
        self.movie.start()


    def startUItab(self):
        self.Window = UItab(self)
        self.setWindowTitle("GiF work")
        self.show()


    def PaintEvent(self, event):
        currentFrame = self.movie.currentPixmap()
        framerect = currentFrame.rect()
        framerect.moveCenter(self.rect().center())
        if framerect.intersects(event.rect()):
            painter = QPainter(self)
            painter.drawPixmap(framerect.left(),framerect.top(), currentFrame)


if __name__=='__main__':
    app = QApplication(sys.argv)
    W = MainWindow()
    sys.exit(app.exec())

