

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_list(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(800, 600)
        self.body = QtWidgets.QFrame(Frame)
        self.body.setGeometry(QtCore.QRect(0, 120, 801, 481))
        self.body.setStyleSheet("background-color: #333;")
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.subtitulo_3 = QtWidgets.QLabel(self.body)
        self.subtitulo_3.setGeometry(QtCore.QRect(230, 30, 381, 52))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.subtitulo_3.setFont(font)
        self.subtitulo_3.setStyleSheet("color: white; font-size: 42px")
        self.subtitulo_3.setObjectName("subtitulo_3")
        self.boton_clientes_3 = QtWidgets.QPushButton(self.body)
        self.boton_clientes_3.setGeometry(QtCore.QRect(310, 380, 191, 61))
        self.boton_clientes_3.setStyleSheet("background-color: red; color: white; border-radius: 7px; font-size: 16px")
        self.boton_clientes_3.setObjectName("boton_clientes_3")
        self.tableWidget = QtWidgets.QTableWidget(self.body)
        self.tableWidget.setGeometry(QtCore.QRect(300, 100, 211, 251))
        self.tableWidget.setStyleSheet("background-color: white; ")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
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
        self.subtitulo_3.setText(_translate("Frame", "LISTA DE CLIENTES"))
        self.boton_clientes_3.setText(_translate("Frame", "VOLVER"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Frame", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Frame", "Cedula"))
        self.titulo.setText(_translate("Frame", "FARMA CAMPO"))
class MiVentanaExtendida(QtWidgets.QMainWindow, Ui_list):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Agregar datos a la tabla
        datos = [
            ["Juan", "123456789"],
    ["María", "987654321"],
    ["Carlos", "567890123"],
    ["Laura", "456789012"],
    ["Alejandro", "321098765"],
    ["Isabel", "234567890"],
    ["Andrés", "890123456"],
    ["Ana", "678901234"],
    ["Luis", "789012345"],
    ["Gabriela", "234567890"],
    ["Diego", "123456789"],
    ["Valeria", "456789012"],
    ["Roberto", "789012345"],
    ["Sofía", "234567890"],
    ["Javier", "567890123"],
    ["Carmen", "890123456"],
    ["Miguel", "345678901"],
    ["Patricia", "678901234"],
    ["José", "456789012"],
    ["Rosa", "890123456"],
        ]

        self.llenar_tabla(datos)

    def llenar_tabla(self, datos):
        # Obtener el número de filas
        num_filas = len(datos)

        # Establecer el número de filas en la tabla
        self.tableWidget.setRowCount(num_filas)

    # Llenar la tabla con los datos
        for fila, datos_fila in enumerate(datos):
            for columna, dato in enumerate(datos_fila):
                item = QtWidgets.QTableWidgetItem(str(dato))
                self.tableWidget.setItem(fila, columna, item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventana_extendida = MiVentanaExtendida()
    ventana_extendida.show()
    sys.exit(app.exec_())


