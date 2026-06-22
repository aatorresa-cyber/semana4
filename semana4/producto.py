class Producto:
 def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

 def mostrar_info(self):
        return f"{self.nombre} - ${self.precio} ({self.categoria})"
 def __str__(self):
        return self.mostrar_info()
