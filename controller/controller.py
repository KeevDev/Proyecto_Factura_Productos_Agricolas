import sys
sys.path.append("C:/Users/angie/OneDrive/Escritorio/UNIVERSIDAD/PROGRA4/2/Proyecto_Factura_Productos_Agricolas/Farma_campo")
from datetime import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
from model.Cliente import  Cliente
from model.Factura import  Factura
from model.Producto_control import  ProductoControl
from model.Antibiotico import  Antibiotico
from ui.agregar_registro import Ui_agregar_cliente
from ui.Busqueda import Ui_busqueda
from ui.main import Ui_Main
from PyQt5 import QtWidgets
from ui.lista_clientes import Ui_list
from ui.clientes import Ui_customer


#CONTROLLER + CRUD


# def vender_producto(cliente, producto):
#     fecha_actual = datetime.now()
#     factura = Factura(fecha_actual, 0)  # El valor total se calculará sumando los productos vendidos
#     cliente.agregar_factura(factura)
#     factura.agregar_producto(producto)
#     factura.valor_total += producto.valor

# def imprimir_cliente(self,cedula):
#         if self.buscar_cedula(cedula) is True:
#             for i in self.clientes_facturados:
#                 if i.cliente.cedula == cedula:
#                     print(f"|   Nombre: {i.cliente.nombre}")
#                     print(f"|   Cedula: {i.cliente.cedula}")
#                     for i, prod in enumerate(self.productos):
#                         print(f"|   {i+1}. {prod.nombre}")
#                         print(f"|       Valor: {prod.valor}")
#                         print("--------------------------------------------------------")
#         else:
#             print("No se encontro el cliente")


# def lista_clientes(self):
#         for i in self.clientes_facturados:
#             print(f"|   Nombre: {i.cliente.nombre}")
#             print(f"|   Cedula: {i.cliente.cedula}")
#             for i, prod in enumerate(self.productos):
#                 print(f"|   {i+1}. {prod.nombre}")
#                 print(f"|       Valor: {prod.valor}")
#                 print("--------------------------------------------------------")

# # Funciones CRUD
'''

def crear_cliente(cedula, nombre):
    nuevo_cliente = Cliente(cedula, nombre)
    clientes.append(nuevo_cliente)
    return nuevo_cliente




def crear_factura(producto, cliente,total):
    nueva_factura = Factura(datetime.today(),total)
    nueva_factura.agregar_producto(producto)
    productos.append(producto) # este va en el main 
    cliente.agregar_factura(nueva_factura)
    # productos.limpiarlista


# def calcular_total(self):
#         total = sum([producto.valor for producto in self.productos])
#         return total
# 




def main():
    #while
    try:
        pass
    except(EOFError):
        print(EOFError)
    
    # eleccion = venta_eleccion()
    #if 1 = facturar 2 = en listar clientes 3 buscar un cliente -> es un menu para saber que camino coger
    #cedula = ventana_cedula()   // DEBE RETORNAR UNA CEDULA
    #if buscar_cedula(clientes,cedula):
        #devuelva el objeto(indice del objeto de la lista clientes) al que se le va agregar
        # abrir ventana de navegacion
    #else:
        #nombre = ventana_registrarse    // DEVUELVE UN NOMBRE PARA EL REGISTRO
        #if nombre is not null:  
        # cliente = crear_cliente(Cedula,"kev")
        # abrir ventana de navegacion cuando se haya registrado

    # ---Ventana actual (navegacion --> productos a elegir)----
    # productos = append(ventana_productos()) -> devuelve una lista de productos y asi guardamos una lista dentro de una lista de ordenes del cliente
    # for producto in productos
        # if producto in lista de productos 
        # Total a pagar += valor_producto
    #crear_factura(productos,cliente, total)
    # ventana_factura
    #if de agregar mas productos o imprimirla
    #Volver al inicio
 

'''





class Controller(object):
    def __init__(self) -> None:
        self.cedula = None
        self.encontrado = None
        self.ui = None
        self.cliente = Cliente("Kev",2)
        self.clientes = []
        self.clientes.append(self.cliente)
        self.ventanaActual = None
        
        #productos = []  
    def buscar_cedula(self):
        for cliente in self.clientes:
            if cliente.cedula == self.cedula:
                return True
                
    def store(self): #compras windows
        self.window_third = QtWidgets.QMainWindow()

    def add_person(self): #agregarwindow
        
        self.window_two = QtWidgets.QMainWindow()
        self.ui = Ui_agregar_cliente()
        self.ui.setupUi(self.window_two)
        self.window_two.show()
        self.window.hide()
        self.ui.boton_buscar.clicked.connect(self.agregar_cliente)
        
    def search_window(self): #busquedawindow
        self.window = QtWidgets.QMainWindow()
        self.window_main.hide()
        self.ui = Ui_busqueda()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.boton_buscar.clicked.connect(self.change_window) 
        #otra ventana tipo menu con mostrar cliente y facturarle al cliente
    def change_window(self):
        self.cedula = self.ui.click()
        if self.cedula != None:
            print(self.cedula)
            self.encontrado = self.buscar_cedula()
            self.person_found()
    def person_found(self):
        if self.encontrado == True:
            self.window.hide()
            self.encontrado = False
            self.store()
        else: 
            self.add_person()
    def list_customer(self):
        self.window_list = self.window_customers
        self.window_customers.hide()
        self.ui = Ui_list()
        self.ui.setupUi(self.window_list)
        self.window_list.show()
        self.ui.boton_clientes_3.clicked.connect(self.view_customers)

    def view_customers(self):
        self.window_customers = self.window_main
        self.ui = Ui_customer()
        self.window_main.hide()
        self.ui.setupUi(self.window_customers)
        self.window_customers.show()
        self.ui.boton_listar.clicked.connect(self.list_customer)
        self.ui.boton_buscar_clientes.clicked.connect(self.search_window)

    def menu_main(self,MainWindow):
        self.window_main = MainWindow
        self.ui = Ui_Main()
        self.ui.setupUi(self.window_main)
        self.window_main.show()
        self.ui.boton_facturar.clicked.connect(self.search_window)
        self.ui.boton_clientes.clicked.connect(self.view_customers)
        
            
    def agregar_cliente(self):
        self.nombre = str(self.ui.click())
        if self.nombre != '':
            nuevo_cliente = Cliente(self.nombre,self.cedula)
            self.clientes.append(nuevo_cliente)
            print(f"se agrego {nuevo_cliente.nombre}")
            self.store()
            self.window_two.hide()

    
   
            


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    control = Controller()
    control.menu_main(MainWindow)
    sys.exit(app.exec_())