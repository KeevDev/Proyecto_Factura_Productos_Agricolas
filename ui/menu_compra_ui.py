# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'menu_compra.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Main(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(800, 600)
        self.body = QFrame(Main)
        self.body.setObjectName(u"body")
        self.body.setGeometry(QRect(0, 120, 801, 481))
        self.body.setStyleSheet(u"background-color: #333;")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.boton_facturar = QPushButton(self.body)
        self.boton_facturar.setObjectName(u"boton_facturar")
        self.boton_facturar.setGeometry(QRect(310, 160, 191, 61))
        self.boton_facturar.setStyleSheet(u"background-color: red; color: white; border-radius: 7px; font-size: 16px")
        self.subtitulo = QLabel(self.body)
        self.subtitulo.setObjectName(u"subtitulo")
        self.subtitulo.setGeometry(QRect(350, 60, 101, 52))
        font = QFont()
        self.subtitulo.setFont(font)
        self.subtitulo.setStyleSheet(u"color: white; font-size: 42px")
        self.boton_clientes = QPushButton(self.body)
        self.boton_clientes.setObjectName(u"boton_clientes")
        self.boton_clientes.setGeometry(QRect(310, 280, 191, 61))
        self.boton_clientes.setStyleSheet(u"background-color: red; color: white; border-radius: 7px; font-size: 16px")
        self.header = QFrame(Main)
        self.header.setObjectName(u"header")
        self.header.setGeometry(QRect(0, 0, 801, 121))
        self.header.setStyleSheet(u"background-color : red;")
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.titulo = QLabel(Main)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(260, 50, 286, 52))
        self.titulo.setFont(font)
        self.titulo.setStyleSheet(u"color: white; font-size: 42px")
        self.header_2 = QFrame(Main)
        self.header_2.setObjectName(u"header_2")
        self.header_2.setGeometry(QRect(0, 0, 801, 121))
        self.header_2.setStyleSheet(u"background-color : red;")
        self.header_2.setFrameShape(QFrame.StyledPanel)
        self.header_2.setFrameShadow(QFrame.Raised)
        self.body.raise_()
        self.header.raise_()
        self.header_2.raise_()
        self.titulo.raise_()

        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Frame", None))
        self.boton_facturar.setText(QCoreApplication.translate("Main", u"FACTURAR", None))
        self.subtitulo.setText(QCoreApplication.translate("Main", u"Menu", None))
        self.boton_clientes.setText(QCoreApplication.translate("Main", u"CLIENTES", None))
        self.titulo.setText(QCoreApplication.translate("Main", u"FARMA CAMPO", None))
    # retranslateUi

