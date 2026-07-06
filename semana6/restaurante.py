class Restaurante:

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f"{producto.nombre} agregado correctamente.")

    def mostrar_productos(self):
        print("\n===== PRODUCTOS DEL RESTAURANTE =====\n")

        if len(self.productos) == 0:
            print("No existen productos registrados.")
            return

        for producto in self.productos:
            print(producto.mostrar_informacion())
            print("-" * 40)
            