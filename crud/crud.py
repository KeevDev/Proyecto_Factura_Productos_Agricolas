from crud.cliente import Cliente
from crud.factura import Factura
from crud.productos_control import ControlPlagas, ControlFertilizantes
from crud.antibioticos import Antibiotico
from datetime import datetime


class crud:
    def __init__(self) -> None:
        pass
        
    def crear_usuario():
        nombre = str(input("Nombre: "))       
        cedula = str(input("Cc: "))
        cliente = Cliente(nombre,cedula)
        return cliente

    def crear_factura(cliente):
        nueva_factura = Factura(cliente, datetime.now())
        return nueva_factura
    
    
    
    

    