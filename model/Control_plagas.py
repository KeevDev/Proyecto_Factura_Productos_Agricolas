from model.Producto_control import  ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, registro_ica, nombre, frecuencia_aplicacion, valor, periodo_carencia):
        super().__init__(registro_ica, nombre, frecuencia_aplicacion, valor)
        self.periodo_carencia = periodo_carencia