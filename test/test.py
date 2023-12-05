import unittest
import sys
sys.path.append('C:/Users/angie/OneDrive/Escritorio/UNIVERSIDAD/PROGRA4/2/Proyecto_Factura_Productos_Agricolas')
from datetime import datetime
from crud.cliente import Cliente
from crud.factura import Factura
from crud.productos_control import ControlPlagas, ControlFertilizantes
from crud.antibioticos import Antibiotico
from crud.crud import crud
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
    
class TestCrearUsuarioYFactura(unittest.TestCase):
    def test_crear_usuario(self):
        # Prueba de la función crear_usuario
        cliente = crud.crear_usuario()
        self.assertIsInstance(cliente, Cliente)

    def test_crear_factura(self):
        # Prueba de la función crear_factura
        cliente = Cliente("John Doe", "123456789")
        factura = crud.crear_factura(cliente)
        self.assertIsInstance(factura, Factura)
        self.assertEqual(factura.cliente, cliente)
        self.assertIsInstance(factura.fecha, datetime)



if __name__ == "__main__":
    unittest.main()
