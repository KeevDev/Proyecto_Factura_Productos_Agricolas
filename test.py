import unittest
from datetime import datetime
from cliente import Cliente
from factura import Factura
from productos_control import ControlPlagas, ControlFertilizantes
from antibioticos import Antibiotico

class TestCliente(unittest.TestCase):
    def test_creacion_cliente(self):
        nombre = "Juan Perez"
        cedula = "123456789"
        cliente = Cliente(nombre, cedula)
        
        self.assertEqual(cliente.nombre, nombre)
        self.assertEqual(cliente.cedula, cedula)

class TestFactura(unittest.TestCase):
    def setUp(self):
         self.cliente = Cliente("Juan Perez", "123456789")

    def test_agregar_producto(self):
         factura = Factura(self.cliente, datetime.now())
    
         producto1 = ControlPlagas("ICAR123", "Plaguicida A", "15 días", 50, 10)
         producto2 = ControlFertilizantes("ICAR456", "Fertilizante B", "30 días", 40, "2023-09-15")
         producto3 = Antibiotico("ICAR456", "Antibiotico X", 500, "Bovinos", 25)

         factura.agregar_producto(producto1)
         factura.agregar_producto(producto2)
         factura.agregar_producto(producto3)

         self.assertEqual(len(factura.productos), 3)

    def test_calcular_total(self):
        factura = Factura(self.cliente, datetime.now())
        producto1 = ControlPlagas("ICAR123", "Plaguicida A", "15 días", 50, 10)
        producto2 = ControlFertilizantes("ICAR456", "Fertilizante B", "30 días", 40, "2023-09-15")
        producto3 = Antibiotico("ICAR456", "Antibiotico X", 500, "Bovinos", 25)

        factura.agregar_producto(producto1)
        factura.agregar_producto(producto2)
        factura.agregar_producto(producto3)

        total = factura.calcular_total()
        self.assertEqual(total, 115) 

if __name__ == "__main__":
    unittest.main()
