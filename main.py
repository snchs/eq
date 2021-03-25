import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog, QLabel, QButtonGroup
from PyQt5.QtGui import QLinearGradient, QColor, QPixmap
import math


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # фон
        fon = QLabel(self)
        fon.setScaledContents(True)
        uic.loadUi('design/des.ui', self)  # Загружаем дизайн главного меню

        # ___Кнопки___
        # воплощай мечты
        self.pushButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.pushButton_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home))
        self.pushButton_18.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home))
        self.pushButton_19.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home))

        self.pushButton_22.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.pushButton_23.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))

        self.pushButton_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.pushButton_17.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        # развиваем эмоциональный интеллект
        self.pushButton_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.pushButton_20.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.pushButton_21.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.home))
        self.pushButton_159.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.pushButton_165.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.pushButton_231.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.pushButton_362.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))
        self.pushButton_449.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page))

        self.pushButton_9.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_5))
        self.pushButton_10.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))
        self.pushButton_11.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_13))
        self.pushButton_12.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_14))
        self.pushButton_13.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_15))
        # эмоции
        self.pushButton_160.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_7))
        self.pushButton_161.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_8))
        self.pushButton_162.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_9))
        self.pushButton_163.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_11))
        self.pushButton_164.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_12))

        self.pushButton_166.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))
        self.pushButton_225.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))
        self.pushButton_226.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))
        self.pushButton_228.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))
        self.pushButton_230.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_6))

        self.pushButton_227.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_10))
        self.pushButton_229.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_11))
        # Управляем эмоциями с помощью тела
        self.pushButton_368.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_52))
        self.pushButton_363.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_68))
        self.pushButton_367.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_69))
        self.pushButton_365.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_70))
        self.pushButton_364.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_71))
        self.pushButton_366.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_72))

        self.pushButton_441.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_14))
        self.pushButton_442.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_14))
        self.pushButton_443.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_14))
        self.pushButton_444.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_14))
        self.pushButton_445.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_14))
        self.pushButton_446.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_14))
        # Управляем эмоциями с помощью дыхания
        self.pushButton_450.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_74))
        self.pushButton_453.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_75))
        self.pushButton_451.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_76))
        self.pushButton_452.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_77))
        self.pushButton_448.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_78))

        self.pushButton_447.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_15))
        self.pushButton_454.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_15))
        self.pushButton_455.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_15))
        self.pushButton_457.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_15))
        self.pushButton_458.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_15))



        # действие кнопок - термины
        self.pushButton_5.clicked.connect(self.show_termin_5)
        self.pushButton_6.clicked.connect(self.show_termin_6)
        self.pushButton_7.clicked.connect(self.show_termin_7)
        self.pushButton_8.clicked.connect(self.show_termin_8)
        # дейсвие кнопок - задание на день
        self.pushButton_50.clicked.connect(self.task_day_50)
        self.pushButton_51.clicked.connect(self.task_day_51)
        self.pushButton_52.clicked.connect(self.task_day_52)
        self.pushButton_53.clicked.connect(self.task_day_53)
        self.pushButton_114.clicked.connect(self.task_day_114)
        self.pushButton_26.clicked.connect(self.task_day_26)
        self.pushButton_28.clicked.connect(self.task_day_28)
        self.pushButton_34.clicked.connect(self.task_day_34)
        self.pushButton_29.clicked.connect(self.task_day_29)
        self.pushButton_33.clicked.connect(self.task_day_33)
        self.pushButton_35.clicked.connect(self.task_day_35)
        self.pushButton_31.clicked.connect(self.task_day_31)
        self.pushButton_30.clicked.connect(self.task_day_30)
        self.pushButton_32.clicked.connect(self.task_day_32)
        self.pushButton_41.clicked.connect(self.task_day_41)
        self.pushButton_36.clicked.connect(self.task_day_36)
        self.pushButton_40.clicked.connect(self.task_day_40)
        self.pushButton_42.clicked.connect(self.task_day_42)
        self.pushButton_38.clicked.connect(self.task_day_38)
        self.pushButton_37.clicked.connect(self.task_day_37)
        self.pushButton_39.clicked.connect(self.task_day_39)
        self.pushButton_48.clicked.connect(self.task_day_48)
        self.pushButton_43.clicked.connect(self.task_day_43)
        self.pushButton_47.clicked.connect(self.task_day_47)
        self.pushButton_49.clicked.connect(self.task_day_49)
        self.pushButton_45.clicked.connect(self.task_day_45)
        self.pushButton_44.clicked.connect(self.task_day_44)
        self.pushButton_46.clicked.connect(self.task_day_46)
        self.pushButton_113.clicked.connect(self.task_day_113)
        self.pushButton_112.clicked.connect(self.task_day_112)
        # _________

    def style_for_termin(self):
        return '''border:0;background-color:#f0f0f0;
        color:black;font-size:12pt;font-family:Arial;border:2px solid #b0b0b0;border-radius:10px;'''

    def show_termin_5(self):
        self.textEdit_3.setStyleSheet(self.style_for_termin())

    def show_termin_6(self):
        self.textEdit_4.setStyleSheet(self.style_for_termin())

    def show_termin_7(self):
        self.textEdit_6.setStyleSheet(self.style_for_termin())

    def show_termin_8(self):
        self.textEdit_7.setStyleSheet(self.style_for_termin())

    # --- показать задание на день - функция
    def task_day_50(self):
        self.textEdit_25.setText('Удиви близкого человека')
        self.textEdit_26.setText('Ты сам выбираешь каким будет твой день')

    def task_day_51(self):
        self.textEdit_25.setText('Наведи порядок в квартире')
        self.textEdit_26.setText('То, во что ты веришь, становится реальностью')

    def task_day_52(self):
        self.textEdit_25.setText('Посмотри любимый фильм')
        self.textEdit_26.setText('Будь свободным и бесконечно влюбленным во что-то')

    def task_day_53(self):
        self.textEdit_25.setText('Выспись')
        self.textEdit_26.setText('Сделай шаг и дорога сама появится')

    def task_day_114(self):
        self.textEdit_25.setText('Встреть рассвет')
        self.textEdit_26.setText('Сегодня я буду лучше, чем вчера')

    def task_day_26(self):
        self.textEdit_25.setText('Купи маме цветы')
        self.textEdit_26.setText('Если ты сомневаешься, сделай еще один шаг вперед')

    def task_day_28(self):
        self.textEdit_25.setText('Приготовь завтрак для всей семьи')
        self.textEdit_26.setText('Трудности показывают тебе, чего ты стоишь')

    def task_day_34(self):
        self.textEdit_25.setText('Сделай 5 комплиментов')
        self.textEdit_26.setText('Нет ничего невозможного')

    def task_day_29(self):
        self.textEdit_25.setText('Займись спортом')
        self.textEdit_26.setText('Мечты не работают, пока не работаешь ты')

    def task_day_33(self):
        self.textEdit_25.setText(' Обними близкого человека')
        self.textEdit_26.setText('Успех – это лестница, на которую нельзя взобраться, держа руки в карманах')

    def task_day_35(self):
        self.textEdit_25.setText('Сходи в кафе')
        self.textEdit_26.setText('Мечтай вчера, действуй сегодня')

    def task_day_31(self):
        self.textEdit_25.setText('Навести бабушку с дедушкой')
        self.textEdit_26.setText('Научись видеть возможности в любых трудностях')

    def task_day_30(self):
        self.textEdit_25.setText('Сделай доброе дело')
        self.textEdit_26.setText('Стремись к прогрессу, а не к совершенству')

    def task_day_32(self):
        self.textEdit_25.setText('Поблагодари кого-нибудь')
        self.textEdit_26.setText('Только при выходе из зоны комфорта начинается развитие')

    def task_day_41(self):
        self.textEdit_25.setText('Попробуй сделать что-то новое')
        self.textEdit_26.setText('Человек должен мечтать, чтобы видеть смысл жизни')

    def task_day_36(self):
        self.textEdit_25.setText('Встреться с близким человеком')
        self.textEdit_26.setText('Верь в себя, и в тебя поверит весь мир')

    def task_day_40(self):
        self.textEdit_25.setText('Потанцуй под любимые песни')
        self.textEdit_26.setText('Превращай мечты в цели')

    def task_day_42(self):
        self.textEdit_25.setText('Проведи день с самим собой')
        self.textEdit_26.setText('Мы становимся тем, о чем мы думаем')

    def task_day_38(self):
        self.textEdit_25.setText('Сделай комплимент незнакомцу')
        self.textEdit_26.setText('Ты уже многое прошел, и не ради того, чтобы бросить')

    def task_day_37(self):
        self.textEdit_25.setText('Посмотри кулинарный мастер-класс и приготовь новое блюдо')
        self.textEdit_26.setText('Живите прямо сейчас')

    def task_day_39(self):
        self.textEdit_25.setText('Выложи пост в социальные сети')
        self.textEdit_26.setText('Когда ты победишь свои страхи, ты победишь свою жизнь')

    def task_day_48(self):
        self.textEdit_25.setText('Сделай смешное фото и отправь друзьям')
        self.textEdit_26.setText('Время не любит, когда его тратят впустую')

    def task_day_43(self):
        self.textEdit_25.setText('Выброси 5 ненужных вещей')
        self.textEdit_26.setText('Помни, целый мир в твоих руках')

    def task_day_47(self):
        self.textEdit_25.setText('Спой в караоке')
        self.textEdit_26.setText(' Нет ничего невозможного')

    def task_day_49(self):
        self.textEdit_25.setText('Составь план и выполни все пункты')
        self.textEdit_26.setText('Мир открывает двери перед тем, кто знает куда идет')

    def task_day_45(self):
        self.textEdit_25.setText('Проведи день без социальных сетей')
        self.textEdit_26.setText('Все победы начинаются с победы над самим собой')

    def task_day_44(self):
        self.textEdit_25.setText('Напиши 15 фактов о себе')
        self.textEdit_26.setText('Каждое испытание дает шанс стать сильнее')

    def task_day_46(self):
        self.textEdit_25.setText('Признайся в чувствах через письмо')
        self.textEdit_26.setText('Не бойся, что не знаешь – бойся, что не учишься')

    def task_day_113(self):
        self.textEdit_25.setText('Удели время своему хобби')
        self.textEdit_26.setText('Сделай свои мечты сильнее своих страхов')

    def task_day_112(self):
        self.textEdit_25.setText('Покорми бездомное животное')
        self.textEdit_26.setText('Если вы решили действовать, закройте двери для сомнений')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    app.setStyle('Fusion')
    ex.show()
    sys.exit(app.exec_())
