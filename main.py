import sys

from PIL import Image, ImageDraw
from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randrange


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        uic.loadUi('UI.ui', self)
        self.but.clicked.connect(self.a)
        self.setWindowTitle('Кружочки')

    def a(self):
        self.but.hide()
        self.draw()

    def draw(self):
        im = Image.new('RGB', (500, 500), (255, 255, 255))
        dr = ImageDraw.Draw(im)
        a = randrange(50, 300, 10)
        b = randrange(300, 470, 15)
        c = randrange(50, 300, 10)
        d = randrange(300, 470, 15)
        dr.ellipse((a, a, b, b), outline="#FFFF00", width=10)
        dr.ellipse((c, c, d, d), outline="#FFFF00", width=10)
        im.save('res.jpg')
        z = QPixmap('res.jpg')
        self.square.setPixmap(z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())
