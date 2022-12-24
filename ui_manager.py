import sys

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
        self.currency_picker.setPlaceholderText('Выберите валюту')
        self.currency_picker_2.setPlaceholderText('Выберите валюту')
        for item in currency_names:
            self.currency_picker.addItem(item)
            self.currency_picker_2.addItem(item)
        self.currency_picker.currentIndexChanged.connect(self.currency_chosen)
        self.currency_picker_2.currentIndexChanged.connect(self.currency_2_chosen)
        self.more_btn.toggled.connect(self.more_btn_clicked)

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
        self.currency_2_rate.setText(str(format(chosen_currency_rate / currency_base_rate / int(chosen_currency_data[2]), '.4f')))

    def more_btn_clicked(self):
        if self.more_btn.isChecked():
            print('развёрнуто')
            self.child = self
        else:
            print('свёрнуто')





if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.setWindowTitle('converter')
    w.show()
    app.exec()
