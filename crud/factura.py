from datetime import datetime

class Factura:
    def __init__(self, cliente, fecha):
        self.cliente = cliente
        self.fecha = fecha
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = sum([producto.valor for producto in self.productos])
        return total
