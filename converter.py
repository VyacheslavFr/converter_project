# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'converter.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QWidget)

class Ui_Converter(object):
    def setupUi(self, Converter):
        if not Converter.objectName():
            Converter.setObjectName(u"Converter")
        Converter.resize(737, 199)
        Converter.setStyleSheet(u"QWidget#Converter {background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 #DCDCDC, stop:1 #75DBA4);\n"
"width: 200px;\n"
"}\n"
"")
        self.currency_picker = QComboBox(Converter)
        self.currency_picker.setObjectName(u"currency_picker")
        self.currency_picker.setGeometry(QRect(70, 40, 371, 22))
        font = QFont()
        font.setPointSize(10)
        self.currency_picker.setFont(font)
        self.currency_picker.setCursor(QCursor(Qt.PointingHandCursor))
        self.currency_picker.setStyleSheet(u"QComboBox{\n"
"background-color:#D3CE9B;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #413F33;\n"
"}\n"
"QComboBox:on {\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"QComboBox::drop-down \n"
"{\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"color: #000;	\n"
"background-color: #D3CE9B;\n"
"selection-background-color: #D3CE9B;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #413F33;\n"
"}\n"
"QScrollBar:vertical {\n"
"background-color: #AEA86B;\n"
"padding: 4px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #958F5A;         \n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background-color: #AEA86B;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
" "
                        "   background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {\n"
"	background-color: #fff;\n"
"    height: 0px;\n"
"    width: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: #88DAAE;\n"
"	color: #000;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:focus {\n"
"	background-color: #88DAAE;\n"
"	color: #000;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"background-color:#AEA76B;\n"
"}")
        self.currency_picker_2 = QComboBox(Converter)
        self.currency_picker_2.setObjectName(u"currency_picker_2")
        self.currency_picker_2.setEnabled(False)
        self.currency_picker_2.setGeometry(QRect(70, 130, 371, 22))
        self.currency_picker_2.setFont(font)
        self.currency_picker_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.currency_picker_2.setStyleSheet(u"QComboBox{\n"
"background-color:#D3CE9B;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #413F33;\n"
"}\n"
"QComboBox:on {\n"
"    border-bottom-right-radius: 0px;\n"
"    border-bottom-left-radius: 0px;\n"
"}\n"
"QComboBox::drop-down \n"
"{\n"
"    width: 0px;\n"
"    height: 0px;\n"
"}\n"
"QComboBox QAbstractItemView {\n"
"color: #000;	\n"
"background-color: #D3CE9B;\n"
"selection-background-color: #D3CE9B;\n"
"border-radius: 0px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #413F33;\n"
"}\n"
"QScrollBar:vertical {\n"
"background-color: #AEA86B;\n"
"padding: 4px;\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: #958F5A;         \n"
"    min-height: 5px;\n"
"    border-radius: 4px;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"    background-color: #AEA86B;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
" "
                        "   background: none;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical, QScrollBar::add-line:vertical {\n"
"	background-color: #fff;\n"
"    height: 0px;\n"
"    width: 0px;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:hover {\n"
"	background-color: #88DAAE;\n"
"	color: #000;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item:focus {\n"
"	background-color: #88DAAE;\n"
"	color: #000;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"background-color:#AEA76B;\n"
"}")
        self.currency_2_rate = QLabel(Converter)
        self.currency_2_rate.setObjectName(u"currency_2_rate")
        self.currency_2_rate.setGeometry(QRect(460, 10, 281, 81))
        font1 = QFont()
        font1.setPointSize(16)
        self.currency_2_rate.setFont(font1)
        self.currency_2_rate.setAlignment(Qt.AlignCenter)
        self.currency_2_rate.setWordWrap(True)
        self.more_block = QGroupBox(Converter)
        self.more_block.setObjectName(u"more_block")
        self.more_block.setGeometry(QRect(20, 210, 721, 291))
        font2 = QFont()
        font2.setPointSize(18)
        self.more_block.setFont(font2)
        self.more_block.setStyleSheet(u"border: 0;")
        self.USD_name = QLabel(self.more_block)
        self.USD_name.setObjectName(u"USD_name")
        self.USD_name.setGeometry(QRect(80, 250, 200, 30))
        self.USD_name.setFont(font1)
        self.USD_name.setStyleSheet(u"QLabel {\n"
"padding-left: 20px;\n"
"padding-bottom: 3px;\n"
"background-color: #D3CE9B;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: #AEA86B;\n"
"}")
        self.USD_name.setMargin(0)
        self.Yen_name = QLabel(self.more_block)
        self.Yen_name.setObjectName(u"Yen_name")
        self.Yen_name.setGeometry(QRect(80, 130, 200, 30))
        self.Yen_name.setFont(font1)
        self.Yen_name.setStyleSheet(u"QLabel {\n"
"padding-left: 20px;\n"
"padding-bottom: 3px;\n"
"background-color: #D3CE9B;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: #AEA86B;\n"
"}")
        self.Yen_name.setMargin(0)
        self.Euro_name = QLabel(self.more_block)
        self.Euro_name.setObjectName(u"Euro_name")
        self.Euro_name.setGeometry(QRect(80, 190, 200, 30))
        self.Euro_name.setFont(font1)
        self.Euro_name.setStyleSheet(u"QLabel {\n"
"padding-left: 20px;\n"
"padding-bottom: 3px;\n"
"background-color: #D3CE9B;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: #AEA86B;\n"
"}")
        self.Euro_name.setMargin(0)
        self.Pound_name = QLabel(self.more_block)
        self.Pound_name.setObjectName(u"Pound_name")
        self.Pound_name.setGeometry(QRect(80, 10, 200, 30))
        self.Pound_name.setFont(font1)
        self.Pound_name.setStyleSheet(u"QLabel {\n"
"padding-left: 20px;\n"
"padding-bottom: 3px;\n"
"background-color: #D3CE9B;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: #AEA86B;\n"
"}")
        self.Pound_name.setMargin(0)
        self.Yuan_name = QLabel(self.more_block)
        self.Yuan_name.setObjectName(u"Yuan_name")
        self.Yuan_name.setGeometry(QRect(80, 70, 200, 30))
        self.Yuan_name.setFont(font1)
        self.Yuan_name.setStyleSheet(u"QLabel {\n"
"padding-left: 20px;\n"
"padding-bottom: 3px;\n"
"background-color: #D3CE9B;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: #AEA86B;\n"
"}")
        self.Yuan_name.setMargin(0)
        self.Yen_rate = QLabel(self.more_block)
        self.Yen_rate.setObjectName(u"Yen_rate")
        self.Yen_rate.setGeometry(QRect(550, 130, 151, 30))
        font3 = QFont()
        font3.setPointSize(16)
        font3.setBold(True)
        self.Yen_rate.setFont(font3)
        self.Yen_rate.setStyleSheet(u"color: #313131;\n"
"")
        self.Yen_rate.setAlignment(Qt.AlignCenter)
        self.USD_rate = QLabel(self.more_block)
        self.USD_rate.setObjectName(u"USD_rate")
        self.USD_rate.setGeometry(QRect(550, 250, 151, 30))
        self.USD_rate.setFont(font3)
        self.USD_rate.setStyleSheet(u"color: #313131;\n"
"")
        self.USD_rate.setAlignment(Qt.AlignCenter)
        self.Pound_rate = QLabel(self.more_block)
        self.Pound_rate.setObjectName(u"Pound_rate")
        self.Pound_rate.setGeometry(QRect(550, 10, 151, 30))
        self.Pound_rate.setFont(font3)
        self.Pound_rate.setStyleSheet(u"color: #313131;")
        self.Pound_rate.setAlignment(Qt.AlignCenter)
        self.Yuan_rate = QLabel(self.more_block)
        self.Yuan_rate.setObjectName(u"Yuan_rate")
        self.Yuan_rate.setGeometry(QRect(550, 70, 151, 30))
        self.Yuan_rate.setFont(font3)
        self.Yuan_rate.setStyleSheet(u"color: #313131;\n"
"")
        self.Yuan_rate.setAlignment(Qt.AlignCenter)
        self.Euro_rate = QLabel(self.more_block)
        self.Euro_rate.setObjectName(u"Euro_rate")
        self.Euro_rate.setGeometry(QRect(550, 190, 151, 30))
        self.Euro_rate.setFont(font3)
        self.Euro_rate.setStyleSheet(u"color: #313131;\n"
"")
        self.Euro_rate.setAlignment(Qt.AlignCenter)
        self.Pound_icon = QLabel(self.more_block)
        self.Pound_icon.setObjectName(u"Pound_icon")
        self.Pound_icon.setGeometry(QRect(50, 0, 50, 50))
        font4 = QFont()
        font4.setPointSize(25)
        self.Pound_icon.setFont(font4)
        self.Pound_icon.setStyleSheet(u"QLabel {\n"
"background-color: #D3CE9B;\n"
"border-radius: 25px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: #AEA86B;\n"
"padding-bottom: 2px;\n"
"}")
        self.Pound_icon.setAlignment(Qt.AlignCenter)
        self.Yuan_icon = QLabel(self.more_block)
        self.Yuan_icon.setObjectName(u"Yuan_icon")
        self.Yuan_icon.setGeometry(QRect(50, 60, 50, 50))
        self.Yuan_icon.setFont(font4)
        self.Yuan_icon.setStyleSheet(u"QLabel {\n"
"background-color: #D3CE9B;\n"
"border-radius: 25px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: #AEA86B;\n"
"padding-bottom: 2px;\n"
"}")
        self.Yuan_icon.setAlignment(Qt.AlignCenter)
        self.Yen_icon = QLabel(self.more_block)
        self.Yen_icon.setObjectName(u"Yen_icon")
        self.Yen_icon.setGeometry(QRect(50, 120, 50, 50))
        self.Yen_icon.setFont(font4)
        self.Yen_icon.setStyleSheet(u"QLabel {\n"
"background-color: #D3CE9B;\n"
"border-radius: 25px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: #AEA86B;\n"
"padding-bottom: 2px;\n"
"}")
        self.Yen_icon.setAlignment(Qt.AlignCenter)
        self.Euro_icon = QLabel(self.more_block)
        self.Euro_icon.setObjectName(u"Euro_icon")
        self.Euro_icon.setGeometry(QRect(50, 180, 50, 50))
        self.Euro_icon.setFont(font4)
        self.Euro_icon.setStyleSheet(u"QLabel {\n"
"background-color: #D3CE9B;\n"
"border-radius: 25px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: #AEA86B;\n"
"padding-bottom: 2px;\n"
"padding-right: 2px;\n"
"}")
        self.Euro_icon.setAlignment(Qt.AlignCenter)
        self.USD_icon = QLabel(self.more_block)
        self.USD_icon.setObjectName(u"USD_icon")
        self.USD_icon.setGeometry(QRect(50, 240, 50, 50))
        self.USD_icon.setFont(font4)
        self.USD_icon.setStyleSheet(u"QLabel {\n"
"background-color: #D3CE9B;\n"
"border-radius: 25px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"border-color: #AEA86B;\n"
"padding-bottom: 2px;\n"
"}")
        self.USD_icon.setAlignment(Qt.AlignCenter)
        self.more_btn = QPushButton(Converter)
        self.more_btn.setObjectName(u"more_btn")
        self.more_btn.setGeometry(QRect(500, 130, 161, 24))
        self.more_btn.setFont(font)
        self.more_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.more_btn.setStyleSheet(u"QPushButton{\n"
"background-color:#D3CE9B;\n"
"border-radius: 10px;\n"
"border-style: solid;\n"
"border-width: 1px;\n"
"border-color: #413F33;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover {\n"
"background-color:#AEA76B;\n"
"}\n"
"QPushButton:checked {\n"
"background-color:#AEA76B;\n"
"}")
        self.more_btn.setCheckable(True)

        self.retranslateUi(Converter)

        QMetaObject.connectSlotsByName(Converter)
    # setupUi

    def retranslateUi(self, Converter):
        Converter.setWindowTitle(QCoreApplication.translate("Converter", u"Form", None))
        self.currency_picker.setPlaceholderText(QCoreApplication.translate("Converter", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0432\u0430\u043b\u044e\u0442\u0443, \u043a\u043e\u0442\u043e\u0440\u0443\u044e \u0445\u043e\u0442\u0438\u0442\u0435 \u043f\u0435\u0440\u0435\u0432\u0435\u0441\u0442\u0438", None))
        self.currency_picker_2.setPlaceholderText(QCoreApplication.translate("Converter", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0432\u0430\u043b\u044e\u0442\u0443 \u0434\u043b\u044f \u0441\u0440\u0430\u0432\u043d\u0435\u043d\u0438\u044f", None))
        self.currency_2_rate.setText(QCoreApplication.translate("Converter", u"\u0417\u0434\u0435\u0441\u044c \u043f\u043e\u044f\u0432\u0438\u0442\u0441\u044f \u043a\u0443\u0440\u0441", None))
        self.more_block.setTitle("")
        self.USD_name.setText(QCoreApplication.translate("Converter", u"\u0414\u043e\u043b\u043b\u0430\u0440 \u0421\u0428\u0410", None))
        self.Yen_name.setText(QCoreApplication.translate("Converter", u"\u042f\u043f\u043e\u043d\u0441\u043a\u0430\u044f \u0419\u0435\u043d\u0430", None))
        self.Euro_name.setText(QCoreApplication.translate("Converter", u"\u0415\u0432\u0440\u043e", None))
        self.Pound_name.setText(QCoreApplication.translate("Converter", u"\u0424\u0443\u043d\u0442 \u0441\u0442\u0435\u0440\u043b\u0438\u043d\u0433\u043e\u0432", None))
        self.Yuan_name.setText(QCoreApplication.translate("Converter", u"\u041a\u0438\u0442\u0430\u0439\u0441\u043a\u0438\u0439 \u042e\u0430\u043d\u044c", None))
        self.Yen_rate.setText(QCoreApplication.translate("Converter", u"?", None))
        self.USD_rate.setText(QCoreApplication.translate("Converter", u"?", None))
        self.Pound_rate.setText(QCoreApplication.translate("Converter", u"?", None))
        self.Yuan_rate.setText(QCoreApplication.translate("Converter", u"?", None))
        self.Euro_rate.setText(QCoreApplication.translate("Converter", u"?", None))
        self.Pound_icon.setText(QCoreApplication.translate("Converter", u"\u00a3", None))
        self.Yuan_icon.setText(QCoreApplication.translate("Converter", u"\u5713", None))
        self.Yen_icon.setText(QCoreApplication.translate("Converter", u"\u00a5", None))
        self.Euro_icon.setText(QCoreApplication.translate("Converter", u"\u20ac", None))
        self.USD_icon.setText(QCoreApplication.translate("Converter", u"$", None))
        self.more_btn.setText(QCoreApplication.translate("Converter", u"\u041f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u044b\u0435 \u043a\u043e\u0442\u0438\u0440\u043e\u0432\u043a\u0438", None))
    # retranslateUi

