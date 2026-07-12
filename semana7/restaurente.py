class Restaurante:

    def __init__(self):
        self.productos = []
        self.clientes = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def listar_productos(self):
        if not self.productos:
            print("No existen productos.")
        else:
            for p in self.productos:
                print(p)

    def listar_clientes(self):
        if not self.clientes:
            print("No existen clientes.")
        else:
            for c in self.clientes:
                print(c)

    def buscar_producto(self, nombre):
        for p in self.productos:
            if p.nombre.lower() == nombre.lower():
                return p
        return None

    def buscar_cliente(self, identificacion):
        for c in self.clientes:
            if c.identificacion == identificacion:
                return c
        return None
    