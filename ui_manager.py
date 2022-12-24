import sys
import time

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QWidget, QGraphicsColorizeEffect, \
    QGraphicsOpacityEffect
from converter import Ui_Converter
from data_refiner import currency_names, currency_refined_data


class Window(QDialog, Ui_Converter):
    """Main window."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__()
        self.setupUi(self)
        self.currency_picker.setMaxCount(1000)
        for item in currency_names:
            self.currency_picker.addItem(item)
            self.currency_picker_2.addItem(item)
        self.currency_picker.currentIndexChanged.connect(self.currency_chosen)
        self.currency_picker_2.currentIndexChanged.connect(self.currency_2_chosen)
        self.more_btn.toggled.connect(self.more_btn_clicked)
        self.setWindowIcon(QIcon('icon.png'))

    def currency_chosen(self):
        chosen_currency_name = self.currency_picker.currentText()
        chosen_currency_data = currency_refined_data[chosen_currency_name]
        chosen_currency_rate = float(chosen_currency_data[-1])

        usd_rate = float(currency_refined_data['Доллар США'][-1])
        self.USD_rate.setText(str(format(usd_rate / chosen_currency_rate / int(chosen_currency_data[2]), '.4f')))

        eur_rate = float(currency_refined_data['Евро'][-1])
        self.Euro_rate.setText(str(format(eur_rate / chosen_currency_rate / int(chosen_currency_data[2]), '.4f')))

        pound_rate = float(currency_refined_data['Фунт стерлингов Соединенного королевства'][-1])
        self.Pound_rate.setText(str(format(pound_rate / chosen_currency_rate / int(chosen_currency_data[2]), '.4f')))

        yen_rate = float(currency_refined_data['Японских иен'][-1])
        self.Yen_rate.setText(str(format(yen_rate / chosen_currency_rate / int(chosen_currency_data[2]), '.4f')))

        yuan_rate = float(currency_refined_data['Китайских юаней'][-1])
        self.Yuan_rate.setText(str(format(yuan_rate / chosen_currency_rate / int(chosen_currency_data[2]), '.4f')))

        self.currency_picker_2.setEnabled(True)

    def currency_2_chosen(self):
        chosen_currency_name = self.currency_picker_2.currentText()
        chosen_currency_data = currency_refined_data[chosen_currency_name]
        chosen_currency_rate = float(chosen_currency_data[-1])
        print(chosen_currency_data)
        currency_base = self.currency_picker.currentText()
        currency_base_data = currency_refined_data[currency_base]
        currency_base_rate = float(currency_base_data[-1])
        rate_output = str(format(chosen_currency_rate / currency_base_rate / int(chosen_currency_data[2]), '.4f'))
        self.currency_2_rate.setText(f'1 {currency_base_data[1]} равен {rate_output} {chosen_currency_data[1]}')

        font_name = self.currency_2_rate.font().key().split(',')[0]
        self.currency_2_rate.setFont(QFont(font_name, 16))

    def more_btn_clicked(self):
        self.more_btn.setWindowOpacity(0)
        self.child = self
        self.anim = QPropertyAnimation(self.child, b'size')
        self.anim.setDuration(1000)
        self.anim.setEasingCurve(QEasingCurve.OutBounce)
        self.anim.setStartValue(QSize(self.child.size().width(), self.child.size().height()))
        self.child_2 = self.more_block
        effect = QGraphicsOpacityEffect(self.child_2)
        self.child_2.setGraphicsEffect(effect)
        self.anim_2 = QPropertyAnimation(effect, b"opacity")
        self.anim_2.setDuration(1000)
        if self.more_btn.isChecked():
            self.anim.setEndValue(QSize(self.child.size().width(), self.child.size().height() + 400))
            self.anim_2.setStartValue(0)
            self.anim_2.setEndValue(1)
        else:
            self.anim.setDuration(500)
            self.anim.setEndValue(QSize(self.child.size().width(), self.child.size().height() - 400))
            self.anim_2.setStartValue(1)
            self.anim_2.setEndValue(0)
        self.anim.start()
        self.anim_2.start()








if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.setWindowTitle('converter')
    w.show()
    app.exec()
