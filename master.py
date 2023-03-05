import sys, time
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt
from turtle import Turtle
from examples import Examples


class Painter(QWidget):

    def __init__(self, title: str, turtle: Turtle):
        super().__init__()
        self.__title = title
        self.__border = 50
        self.__width = QApplication.desktop().screenGeometry().width()
        self.__height = QApplication.desktop().screenGeometry().height()
        self.__turtle = turtle
        self.initUI()
        self.__paint = False

    def quit(self):
        exit()

    def initUI(self):
        # set full screen
        self.showFullScreen()
        # set title from constructor
        self.setWindowTitle(self.__title)        

        # create layout
        layout = QVBoxLayout()
        # create Close button
        closeButton = QPushButton('Close',self)
        closeButton.resize(75, 38)
        closeButton.move(self.__width - 75, 0)
        closeButton.clicked.connect(self.quit)
        closeButton.setStyleSheet("background-color: red; color: white;")
        closeButton.show()
        # add it to the Layout
        layout.addWidget(closeButton)
        # set layout
        self.setLayout = (layout)
        # render
        self.show()

    

    def paintTurtleMove(self,painter):
        pen = QPen()
        pen.setColor(Qt.black)
        pen.setWidth(2)
        painter.setPen(pen)
        for step in self.__turtle:
            painter.drawLine(*step)

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        
        pen = QPen()
        pen.setWidth(5)
        pen.setColor(Qt.black)
        painter.setPen(pen)
        self.paintTurtleMove(painter)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    width = QApplication.desktop().screenGeometry().width()
    height = QApplication.desktop().screenGeometry().height()
    turtle = Turtle(
        start=[0, height],
        #start=[0,0],
        stepLength=4,
        fractal=Examples.example1
    )
    turtle.run()

    widget = Painter("Turtle",turtle)

    print(width, height)
    app.exec_()
 