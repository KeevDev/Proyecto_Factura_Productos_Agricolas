# ventana1_ui.py
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QPushButton

class Ventana1UI(QDialog):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        button = QPushButton("Ir a Ventana 2")
        button.clicked.connect(self.abrir_ventana2)

        layout.addWidget(button)
        self.setLayout(layout)

    def abrir_ventana2(self):
        # Emitir una señal o llamar a una función en el controlador
        # para indicar que se debe abrir la segunda ventana.
        self.abrir_ventana2_signal.emit()


# ventana2_ui.py
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel

class Ventana2UI(QDialog):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("¡Estás en la Ventana 2!")

        layout.addWidget(label)
        self.setLayout(layout)


# controller.py
from PyQt5.QtWidgets import QApplication


class VentanaController:
    def __init__(self):
        self.ventana1 = Ventana1UI()
        self.ventana2 = Ventana2UI()

        # Conectar la señal desde la Ventana1UI a la función de abrir Ventana2UI
        self.ventana1.abrir_ventana2_signal.connect(self.mostrar_ventana2)

    def mostrar_ventana1(self):
        self.ventana1.show()

    def mostrar_ventana2(self):
        # Mostrar la segunda ventana cuando se emite la señal desde la Ventana1UI
        self.ventana1.close()
        self.ventana2.show()


if __name__ == "__main__":
    app = QApplication([])

    # Crear una instancia del controlador y mostrar la primera ventana
    controller = VentanaController()
    controller.mostrar_ventana1()

    app.exec_()
