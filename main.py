import sys
from random import randrange

from PIL import Image, ImageDraw
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QWidget


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.b = A()
        self.b.show()


class A(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Кружочки')
        self.resize(500, 500)
        self.square = QLabel(self)
        self.square.resize(581, 421)
        self.square.move(0, 0)
        self.but = QPushButton(self)
        self.but.resize(131, 81)
        self.but.move(210, 150)
        self.but.setText('Показать круги')
        self.but.clicked.connect(self.a)

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
        dr.ellipse((a, a, b, b), outline=(randrange(0, 256), randrange(0, 256), randrange(0, 256)),
                   width=10)
        dr.ellipse((c, c, d, d), outline=(randrange(0, 256), randrange(0, 256), randrange(0, 256)),
                   width=10)
        im.save('res.jpg')
        z = QPixmap('res.jpg')
        self.square.setPixmap(z)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = A()
    wnd.show()
    sys.exit(app.exec())
