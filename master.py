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

    def paintCenter(self, painter):
        color = QColor(162,
                       78,
                       0)
        painter.setPen(color)
        painter.setBrush(color)

        centerRaduis = 25
        painter.drawEllipse((self.__width /2 )- (centerRaduis/2),(self.__height - self.__border)-centerRaduis,centerRaduis, centerRaduis)

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
        
        #self.paintCenter(painter)
        self.paintTurtleMove(painter)
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    width = QApplication.desktop().screenGeometry().width()
    height = QApplication.desktop().screenGeometry().height()
    turtle = Turtle(
        start=[width - 800, height - 200],
        stepLength=10,
        fractal=Examples.example3
    )
    turtle.run()

    widget = Painter("Turtle",turtle)

    print(width, height)
    app.exec_()
 