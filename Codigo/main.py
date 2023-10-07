from cliente import Cliente
from factura import Factura
from productos_control import ControlPlagas, ControlFertilizantes
from antibioticos import Antibiotico
from datetime import datetime

def datos():
    nombre = str(input("Nombre: "))
    cedula = str(input("Cc: "))
    cliente = Cliente(nombre,cedula)
    return cliente
    #cliente1 = Cliente("Juan Perez", "123456789")
    #cliente2 = Cliente("Maria Lopez", "987654321")

def productos_comprar():
    print("Menú:")
    print("1. Control plagas")
    print("2. Control Fertilizantes")
    print("3. Antibiotico")
    print("4. Salir")
    n = int(input(""))
    return n if n>0 and n<4 else 0

def plagas():
    producto = ControlPlagas("ICAR123", "Plaguicida A", "15 días", 50, 30)
    return producto

def fertilizantes():
    producto = ControlFertilizantes("ICAR456", "Fertilizante B", "30 días", 40, "2023-09-15")
    return producto

def antibioticos():
    producto = Antibiotico("ICAR420","Antibiotico X", 500, "Bovinos", 25)
    return producto

def agregar(n,factura):
    if n == 1:
        factura.agregar_producto(plagas())
    elif n == 2:
        factura.agregar_producto(fertilizantes())
    elif n == 3 :
        factura.agregar_producto(antibioticos())
    else: 
        None

def lista_productos(factura):
    otro_producto = 's'
    while otro_producto == 's':
        n = productos_comprar()
        agregar(n,factura)
        otro_producto = input("Agregar otro?[s/n]")
def imprimirFactura(factura,total_factura):
    print("--------------------------------------------------------")
    print(f"|   Nombre: {factura.cliente.nombre}")
    print(f"|   Cedula: {factura.cliente.cedula}")
    print(f"|   Fecha: {factura.fecha}")
    for i, prod in enumerate(factura.productos):
        print(f"|   {i+1}. Producto: {prod.nombre}")
        print(f"|       ICA: {prod.ica_registro}")
        print(f"|       Valor: {prod.valor}")
    print(f"|   Total factura: ${total_factura}")
    print("--------------------------------------------------------")
def main():
    while True:
        salir = 's'
        cliente = datos()
        factura = Factura(cliente, datetime.now())
        lista_productos(factura)    
        total_factura = factura.calcular_total()
        imprimirFactura(factura,total_factura)
        salir = input("desea hacer otra factura? [s/n]: ")    
        if salir == 'n':
            break
main()