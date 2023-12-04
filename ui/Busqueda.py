
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_busqueda(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, register_camp):
        register_camp.setObjectName("register_camp")
        register_camp.resize(800, 600)
        register_camp.setStyleSheet("font-family: \'Open Sans\', sans-serif;")
        self.input_cedula = QtWidgets.QLineEdit(register_camp)
        self.input_cedula.setGeometry(QtCore.QRect(90, 300, 591, 41))
        self.input_cedula.setStyleSheet("border-radius: 10px; margin-left: 20px; font-size: 20px; padding: 5px")
        self.input_cedula.setText("")
        self.input_cedula.setObjectName("input_cedula")
        self.titulo = QtWidgets.QLabel(register_camp)
        self.titulo.setGeometry(QtCore.QRect(260, 50, 286, 52))
        font = QtGui.QFont()
        font.setFamily("Open Sans,sans-serif")
        font.setPointSize(-1)
        self.titulo.setFont(font)
        self.titulo.setStyleSheet("color: white; font-size: 42px")
        self.titulo.setObjectName("titulo")
        self.header = QtWidgets.QFrame(register_camp)
        self.header.setGeometry(QtCore.QRect(0, 0, 801, 121))
        self.header.setStyleSheet("background-color : red;")
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.body = QtWidgets.QFrame(register_camp)
        self.body.setGeometry(QtCore.QRect(0, 120, 801, 481))
        self.body.setStyleSheet("background-color: #333;")
        self.body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body.setObjectName("body")
        self.boton_buscar = QtWidgets.QPushButton(self.body, clicked = lambda: self.click())
        self.boton_buscar.setGeometry(QtCore.QRect(355, 280, 91, 31))
        self.boton_buscar.setStyleSheet("background-color: red; color: white; border-radius: 7px; font-size: 16px")
        self.boton_buscar.setObjectName("boton_buscar")
        self.text_cedula = QtWidgets.QLabel(self.body)
        self.text_cedula.setGeometry(QtCore.QRect(110, 130, 115, 39))
        font = QtGui.QFont()
        font.setFamily("Open Sans,sans-serif")
        font.setPointSize(-1)
        self.text_cedula.setFont(font)
        self.text_cedula.setStyleSheet("color: white; font-size: 32px")
        self.text_cedula.setObjectName("text_cedula")
        self.body.raise_()
        self.header.raise_()
        self.titulo.raise_()
        self.input_cedula.raise_()
        self.input_cedula.setPlaceholderText("Ingrese la cédula")
        self.input_cedula.textChanged.connect(lambda text: self.boton_buscar.setEnabled(bool(text))) 
        self.retranslateUi(register_camp)
        QtCore.QMetaObject.connectSlotsByName(register_camp)
        self.input_cedula.setValidator(QtGui.QRegExpValidator(QtCore.QRegExp("[0-9]+"), self.input_cedula))
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
        
        
            
        


    def retranslateUi(self, register_camp):
        _translate = QtCore.QCoreApplication.translate
        register_camp.setWindowTitle(_translate("register_camp", "Frame"))
        self.titulo.setText(_translate("register_camp", "FARMA CAMPO"))
        self.boton_buscar.setText(_translate("register_camp", "Buscar"))
        self.text_cedula.setText(_translate("register_camp", "CEDULA"))

    def click(self):
        if self.input_cedula.text() != '':
            return int(self.input_cedula.text())
        
    

