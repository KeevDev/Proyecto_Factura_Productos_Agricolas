from datetime import datetime

class Factura:
    def __init__(self, cliente, fecha):
        self.cliente = cliente
        self.fecha = fecha
        self.productos = []
        self.clientes_facturados = []
        
    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        total = sum([producto.valor for producto in self.productos])
        return total
    def registros(self,factura):
        self.clientes_facturados.append(factura)
        
    def lista_clientes(self):
        for i in self.clientes_facturados:
            print(f"|   Nombre: {i.cliente.nombre}")
            print(f"|   Cedula: {i.cliente.cedula}")
            for i, prod in enumerate(self.productos):
                print(f"|   {i+1}. {prod.nombre}")
                print(f"|       Valor: {prod.valor}")
                print("--------------------------------------------------------")

    def buscar_cedula(self,cedula):
        for i in self.clientes_facturados:
            if i.cliente.cedula == cedula:
                return True
        
        return False # si llega aca es porque no lo encontro
               
    def imprimir_cliente(self,cedula):
        if self.buscar_cedula(cedula) is True:
            for i in self.clientes_facturados:
                if i.cliente.cedula == cedula:
                    print(f"|   Nombre: {i.cliente.nombre}")
                    print(f"|   Cedula: {i.cliente.cedula}")
                    for i, prod in enumerate(self.productos):
                        print(f"|   {i+1}. {prod.nombre}")
                        print(f"|       Valor: {prod.valor}")
                        print("--------------------------------------------------------")
        else:
            print("No se encontro el cliente")