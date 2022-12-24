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
    QPushButton, QSizePolicy, QSplitter, QWidget)

class Ui_Converter(object):
    def setupUi(self, Converter):
        if not Converter.objectName():
            Converter.setObjectName(u"Converter")
        Converter.resize(890, 179)
        self.currency_picker = QComboBox(Converter)
        self.currency_picker.setObjectName(u"currency_picker")
        self.currency_picker.setGeometry(QRect(120, 40, 371, 22))
        self.currency_picker_2 = QComboBox(Converter)
        self.currency_picker_2.setObjectName(u"currency_picker_2")
        self.currency_picker_2.setEnabled(False)
        self.currency_picker_2.setGeometry(QRect(120, 130, 371, 22))
        self.currency_2_rate = QLabel(Converter)
        self.currency_2_rate.setObjectName(u"currency_2_rate")
        self.currency_2_rate.setGeometry(QRect(570, 130, 49, 21))
        self.groupBox = QGroupBox(Converter)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(70, 210, 721, 291))
        self.splitter = QSplitter(self.groupBox)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setGeometry(QRect(80, 0, 93, 271))
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setHandleWidth(20)
        self.Pound_name = QLabel(self.splitter)
        self.Pound_name.setObjectName(u"Pound_name")
        self.splitter.addWidget(self.Pound_name)
        self.Yuan_name = QLabel(self.splitter)
        self.Yuan_name.setObjectName(u"Yuan_name")
        self.splitter.addWidget(self.Yuan_name)
        self.Yen_name = QLabel(self.splitter)
        self.Yen_name.setObjectName(u"Yen_name")
        self.splitter.addWidget(self.Yen_name)
        self.Euro_name = QLabel(self.splitter)
        self.Euro_name.setObjectName(u"Euro_name")
        self.splitter.addWidget(self.Euro_name)
        self.USD_name = QLabel(self.splitter)
        self.USD_name.setObjectName(u"USD_name")
        self.splitter.addWidget(self.USD_name)
        self.splitter_2 = QSplitter(self.groupBox)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setGeometry(QRect(260, 10, 20, 271))
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter_2.setHandleWidth(20)
        self.USD_rate = QLabel(self.splitter_2)
        self.USD_rate.setObjectName(u"USD_rate")
        self.USD_rate.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.USD_rate)
        self.Euro_rate = QLabel(self.splitter_2)
        self.Euro_rate.setObjectName(u"Euro_rate")
        self.Euro_rate.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.Euro_rate)
        self.Yen_rate = QLabel(self.splitter_2)
        self.Yen_rate.setObjectName(u"Yen_rate")
        self.Yen_rate.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.Yen_rate)
        self.Yuan_rate = QLabel(self.splitter_2)
        self.Yuan_rate.setObjectName(u"Yuan_rate")
        self.Yuan_rate.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.Yuan_rate)
        self.Pound_rate = QLabel(self.splitter_2)
        self.Pound_rate.setObjectName(u"Pound_rate")
        self.Pound_rate.setAlignment(Qt.AlignCenter)
        self.splitter_2.addWidget(self.Pound_rate)
        self.more_btn = QPushButton(Converter)
        self.more_btn.setObjectName(u"more_btn")
        self.more_btn.setGeometry(QRect(660, 130, 161, 24))
        self.more_btn.setCheckable(True)

        self.retranslateUi(Converter)

        QMetaObject.connectSlotsByName(Converter)
    # setupUi

    def retranslateUi(self, Converter):
        Converter.setWindowTitle(QCoreApplication.translate("Converter", u"Form", None))
        self.currency_2_rate.setText(QCoreApplication.translate("Converter", u"?", None))
        self.groupBox.setTitle("")
        self.Pound_name.setText(QCoreApplication.translate("Converter", u"\u0424\u0443\u043d\u0442 \u0441\u0442\u0435\u0440\u043b\u0438\u043d\u0433\u043e\u0432", None))
        self.Yuan_name.setText(QCoreApplication.translate("Converter", u"\u041a\u0438\u0442\u0430\u0439\u0441\u043a\u0438\u0439 \u042e\u0430\u043d\u044c", None))
        self.Yen_name.setText(QCoreApplication.translate("Converter", u"\u042f\u043f\u043e\u043d\u0441\u043a\u0430\u044f \u0419\u0435\u043d\u0430", None))
        self.Euro_name.setText(QCoreApplication.translate("Converter", u"\u0415\u0432\u0440\u043e", None))
        self.USD_name.setText(QCoreApplication.translate("Converter", u"\u0414\u043e\u043b\u043b\u0430\u0440 \u0421\u0428\u0410", None))
        self.USD_rate.setText(QCoreApplication.translate("Converter", u"?", None))
        self.Euro_rate.setText(QCoreApplication.translate("Converter", u"?", None))
        self.Yen_rate.setText(QCoreApplication.translate("Converter", u"?", None))
        self.Yuan_rate.setText(QCoreApplication.translate("Converter", u"?", None))
        self.Pound_rate.setText(QCoreApplication.translate("Converter", u"?", None))
        self.more_btn.setText(QCoreApplication.translate("Converter", u"\u041f\u043e\u043f\u0443\u043b\u044f\u0440\u043d\u044b\u0435 \u043a\u043e\u0442\u0438\u0440\u043e\u0432\u043a\u0438", None))
    # retranslateUi

