import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog, QLabel
from PyQt5.QtGui import QLinearGradient, QColor, QPixmap
import math


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # фон
        fon = QLabel(self)
        # pixmap = QPixmap('photoshop-abr-psd-smoke-brush-013.jpg')
        # fon.resize(730, 520)
        # fon.move(0, 0)
        # fon.setPixmap(pixmap)
        fon.setScaledContents(True)
        uic.loadUi('design/des.ui', self)  # Загружаем дизайн главного меню
        #___Кнопки___
        # воплощай мечты
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home))
        self.pushButton_18.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home))
        self.pushButton_19.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home))

        self.pushButton_22.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.pushButton_23.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))

        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.pushButton_17.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        # self.pushButton_20.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_XXXX))


        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    app.setStyle('Fusion')
    ex.show()
    sys.exit(app.exec_())
