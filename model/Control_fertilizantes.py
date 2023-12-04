from model.Producto_control import  ProductoControl

class ControlFertilizantes(ProductoControl):
    def __init__(self, registro_ica, nombre, frecuencia_aplicacion, valor, ultima_aplicacion):
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, valor)
        self.ultima_aplicacion = ultima_aplicacion