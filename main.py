from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap
import sys
from PIL.ImageQt import ImageQt
from PIL import Image
from design import Ui_Form as Design
from PyQt5 import QtGui
from PyQt5.QtGui import QCursor
from PyQt5 import QtCore


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updater)
        self.image = Image.open("data\\car.png")
        self.label.setPixmap(QPixmap.fromImage(ImageQt(self.image)))
        self.timer.start(1)
        self.status = 0

    def updater(self):
        try:
            if QCursor.pos().x() - 625 <= 0 or QCursor.pos().y() - 300 <= 0 or QCursor.pos().x() - 625 >= 727 - 50 or QCursor.pos().y() - 300 >= 469 - 24:
                pass
            else:
                self.label.move(QCursor.pos().x() - 625, QCursor.pos().y() - 300)
        except:
            print(1)

    def keyPressEvent(self, a0: QtGui.QKeyEvent) -> None:
        if a0.key() == 32:
            if self.status == 0:
                self.image = Image.open("data\\car3.png")
                self.label.setPixmap(QPixmap.fromImage(ImageQt(self.image)))
                self.status = 1
            else:
                self.image = Image.open("data\\car.png")
                self.label.setPixmap(QPixmap.fromImage(ImageQt(self.image)))
                self.status = 0


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())