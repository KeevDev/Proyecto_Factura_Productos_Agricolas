class Factura:
    def __init__(self, fecha, valor_total):
        self.fecha = fecha
        self.valor_total = valor_total
        self.productos_vendidos = []
        

    def agregar_producto(self, producto):
        self.productos_vendidos.append(producto)
    
    