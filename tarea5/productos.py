class Productos:
    def __init__(self, id_producto, nombre, precio, disponible):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.disponible = disponible

    def mostrar(self):
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"ID: {self.id_producto}")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Estado: {estado}")
        