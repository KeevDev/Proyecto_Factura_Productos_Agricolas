# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/clientes.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_customer(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(800, 600)
        self.body = QtWidgets.QFrame(Frame)
        self.body.setGeometry(QtCore.QRect(0, 120, 801, 481))
        self.body.setStyleSheet("background-color: #333;")
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.boton_listar = QtWidgets.QPushButton(self.body)
        self.boton_listar.setGeometry(QtCore.QRect(310, 160, 191, 61))
        self.boton_listar.setStyleSheet("background-color: red; color: white; border-radius: 7px; font-size: 16px")
        self.boton_listar.setObjectName("boton_listar")
        self.subtitulo_3 = QtWidgets.QLabel(self.body)
        self.subtitulo_3.setGeometry(QtCore.QRect(330, 70, 151, 52))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.subtitulo_3.setFont(font)
        self.subtitulo_3.setStyleSheet("color: white; font-size: 42px")
        self.subtitulo_3.setObjectName("subtitulo_3")
        self.boton_buscar_clientes = QtWidgets.QPushButton(self.body)
        self.boton_buscar_clientes.setGeometry(QtCore.QRect(310, 280, 191, 61))
        self.boton_buscar_clientes.setStyleSheet("background-color: red; color: white; border-radius: 7px; font-size: 16px")
        self.boton_buscar_clientes.setObjectName("boton_buscar_cliente")
        self.header_2 = QtWidgets.QFrame(Frame)
        self.header_2.setGeometry(QtCore.QRect(0, 0, 801, 121))
        self.header_2.setStyleSheet("background-color : red;")
        self.header_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_2.setObjectName("header_2")
        self.titulo = QtWidgets.QLabel(Frame)
        self.titulo.setGeometry(QtCore.QRect(260, 50, 286, 52))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color: white; font-size: 42px")
        self.titulo.setObjectName("titulo")
        self.header = QtWidgets.QFrame(Frame)
        self.header.setGeometry(QtCore.QRect(0, 0, 801, 121))
        self.header.setStyleSheet("background-color : red;")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.body.raise_()
        self.header_2.raise_()
        self.header.raise_()
        self.titulo.raise_()

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.boton_listar.setText(_translate("Frame", "LISTA CLIENTES"))
        self.subtitulo_3.setText(_translate("Frame", "Clientes"))
        self.boton_buscar_clientes.setText(_translate("Frame", "BUSCAR CLIENTE"))
        self.titulo.setText(_translate("Frame", "FARMA CAMPO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_customer()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())
