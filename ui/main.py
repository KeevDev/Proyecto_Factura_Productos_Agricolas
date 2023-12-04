
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(800, 600)
        self.body = QtWidgets.QFrame(Main)
        self.body.setGeometry(QtCore.QRect(0, 120, 801, 481))
        self.body.setStyleSheet("background-color: #333;")
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.boton_facturar = QtWidgets.QPushButton(self.body)
        self.boton_facturar.setGeometry(QtCore.QRect(310, 160, 191, 61))
        self.boton_facturar.setStyleSheet("background-color: red; color: white; border-radius: 7px; font-size: 16px")
        self.boton_facturar.setObjectName("boton_facturar")
        self.subtitulo = QtWidgets.QLabel(self.body)
        self.subtitulo.setGeometry(QtCore.QRect(350, 60, 101, 52))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.subtitulo.setFont(font)
        self.subtitulo.setStyleSheet("color: white; font-size: 42px")
        self.subtitulo.setObjectName("subtitulo")
        self.boton_clientes = QtWidgets.QPushButton(self.body)
        self.boton_clientes.setGeometry(QtCore.QRect(310, 280, 191, 61))
        self.boton_clientes.setStyleSheet("background-color: red; color: white; border-radius: 7px; font-size: 16px")
        self.boton_clientes.setObjectName("boton_clientes")
        self.header = QtWidgets.QFrame(Main)
        self.header.setGeometry(QtCore.QRect(0, 0, 801, 121))
        self.header.setStyleSheet("background-color : red;")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.titulo = QtWidgets.QLabel(Main)
        self.titulo.setGeometry(QtCore.QRect(260, 50, 286, 52))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color: white; font-size: 42px")
        self.titulo.setObjectName("titulo")
        self.header_2 = QtWidgets.QFrame(Main)
        self.header_2.setGeometry(QtCore.QRect(0, 0, 801, 121))
        self.header_2.setStyleSheet("background-color : red;")
        self.header_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_2.setObjectName("header_2")
        self.body.raise_()
        self.header.raise_()
        self.header_2.raise_()
        self.titulo.raise_()

        self.retranslateUi(Main)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "Frame"))
        self.boton_facturar.setText(_translate("Main", "FACTURAR"))
        self.subtitulo.setText(_translate("Main", "Menu"))
        self.boton_clientes.setText(_translate("Main", "CLIENTES"))
        self.titulo.setText(_translate("Main", "FARMA CAMPO"))
