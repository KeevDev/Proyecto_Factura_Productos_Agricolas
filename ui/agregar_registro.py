
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_agregar_cliente(object):
    def setupUi(self, agregar_cliente):
        
        agregar_cliente.setObjectName("agregar_cliente")
        agregar_cliente.resize(799, 584)
        self.input_nombre = QtWidgets.QLineEdit(agregar_cliente)
        self.input_nombre.setGeometry(QtCore.QRect(90, 300, 591, 41))
        self.input_nombre.setStyleSheet("border-radius: 10px; margin-left: 20px; font-size: 20px; padding: 5px")
        self.input_nombre.setText("")
        self.input_nombre.setObjectName("input_nombre")
        self.titulo = QtWidgets.QLabel(agregar_cliente)
        self.titulo.setGeometry(QtCore.QRect(260, 50, 286, 52))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color: white; font-size: 42px")
        self.titulo.setObjectName("titulo")
        self.header = QtWidgets.QFrame(agregar_cliente)
        self.header.setGeometry(QtCore.QRect(0, 0, 801, 121))
        self.header.setStyleSheet("background-color : red;")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.body = QtWidgets.QFrame(agregar_cliente)
        self.body.setGeometry(QtCore.QRect(0, 120, 801, 481))
        self.body.setStyleSheet("background-color: #333;")
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.boton_buscar = QtWidgets.QPushButton(self.body)
        self.boton_buscar.setGeometry(QtCore.QRect(355, 280, 91, 31))
        self.boton_buscar.setStyleSheet("background-color: red; color: white; border-radius: 7px; font-size: 16px")
        self.boton_buscar.setObjectName("boton_buscar")
        self.text_nombre = QtWidgets.QLabel(self.body)
        self.text_nombre.setGeometry(QtCore.QRect(110, 130, 115, 39))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.text_nombre.setFont(font)
        self.text_nombre.setStyleSheet("color: white; font-size: 32px")
        self.text_nombre.setObjectName("text_nombre")
        self.titulo_2 = QtWidgets.QLabel(self.body)
        self.titulo_2.setGeometry(QtCore.QRect(20, 10, 341, 52))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.titulo_2.setFont(font)
        self.titulo_2.setStyleSheet("color: white; font-size: 42px")
        self.titulo_2.setObjectName("titulo_2")
        self.header.raise_()
        self.body.raise_()
        self.input_nombre.raise_()
        self.titulo.raise_()
        self.retranslateUi(agregar_cliente)
        QtCore.QMetaObject.connectSlotsByName(agregar_cliente)
        self.input_nombre.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[a-zA-Z]+"), self.input_nombre))
        normal_style = """
            QPushButton {
                background-color: red;
                color: white;
                border-radius: 7px;
                font-size: 16px;
            }
        """
        # Estilo de hover del botón
        hover_style = """
            QPushButton:hover {
                background-color: #FFCCCC;  /* Cambia a tu color de hover deseado */
                border: 2px solid #FFCCCC;  /* Agrega el borde y ajusta según sea necesario */
            }
        """
        self.boton_buscar.setStyleSheet(normal_style + hover_style)

    def retranslateUi(self, agregar_cliente):
        _translate = QtCore.QCoreApplication.translate
        agregar_cliente.setWindowTitle(_translate("agregar_cliente", "Frame"))
        self.titulo.setText(_translate("agregar_cliente", "FARMA CAMPO"))
        self.boton_buscar.setText(_translate("agregar_cliente", "Buscar"))
        self.text_nombre.setText(_translate("agregar_cliente", "Nombre"))
        self.titulo_2.setText(_translate("agregar_cliente", "Agregando Cliente"))

    def click(self):
        if self.input_nombre != '':
            return self.input_nombre.text()


    