from crud.crud import crud
from crud.cliente import Cliente
from crud.factura import Factura
from crud.productos_control import ControlPlagas, ControlFertilizantes
from crud.antibioticos import Antibiotico
import os

def productos_comprar():
    print("Menú de opciones:")
    print("1. Control plagas")
    print("2. Control Fertilizantes")
    print("3. Antibiotico")
    print("4. Salir")
    n = int(input(""))
    return n if n>0 and n<4 else 0

def producto(n):
    if n ==1 :
        producto = ControlPlagas("ICAR123", "Plaguicida A", "15 días", 50, 30)
    elif n == 2:
        producto = ControlFertilizantes("ICAR456", "Fertilizante B", "30 días", 40, "2023-09-15")
    elif n == 3:
        producto = Antibiotico("ICAR420","Antibiotico X", 500, "Bovinos", 25)
    return producto

def lista_productos(factura):
    otro_producto = 's'
    while otro_producto == 's':
        n = productos_comprar()
        p = producto(n)
        factura.agregar_producto(p)
        otro_producto = input("Agregar otro?[s/n]")

def menu_opciones() -> int:
    print("\n\t----Menú----")
    print("1. Agregar Cliente")
    print("2. Hacer Factura a Cliente")
    print("3. Lista de Clientes")
    print("4. Salir")
    print("----------------------------------------")
    opcion = int(input("Seleccione una opción: "))
    
    return opcion

def imprimirFactura(factura,total_factura):
    print("\n\t--------------SISTEMA DE FACTURACION TIENDA AGRICOLA-------------------------")
    print(f"|   Nombre: {factura.cliente.nombre}")
    print(f"|   Cedula: {factura.cliente.cedula}")
    print(f"|   Fecha: {factura.fecha}")
    for i, prod in enumerate(factura.productos):
        print(f"|   {i+1}. Producto: {prod.nombre}")
        print(f"|       ICA: {prod.ica_registro}")
        print(f"|       Valor: {prod.valor}")
    print(f"|   Total factura: ${total_factura}")
    print("--------------------------------------------------------")



factura = None
facturas = []
while True:
    salir = 's'
    eleccion = 0
    eleccion = menu_opciones()
    
    if eleccion == 1:
        os.system('cls')
        print("\t---- CREANDO NUEVO USUARIO ----")
        cliente = crud.crear_usuario()
        print("\t----------------------------")
    elif eleccion == 2:
        if cliente != None:
            factura = crud.crear_factura(cliente)
            lista_productos(factura) 
            total_factura = factura.calcular_total()
            imprimirFactura(factura,total_factura)
            registros = factura.registros(factura)
            salir = input("desea hacer otra factura? [s/n]: ")
            facturas.append(factura)
            if salir == 'n':
                continue
        else:
            print("\nNo hay clientes en las bases de datos")   
            input()             
    elif eleccion == 3:
        if factura != None:
            for registro in facturas:
                registro.lista_clientes()
        else:
            print("No hay clientes registrados")
            input()
    else:
        print("FIN DEL PROGRAMA")
        break
    
        
    
