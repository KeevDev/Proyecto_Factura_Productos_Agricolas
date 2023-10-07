class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    
    def agregar_cliente(self,cliente_nuevo):  
        self.info_cliente.append(cliente_nuevo)

