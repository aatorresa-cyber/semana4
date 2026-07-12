class Producto:
    def __init__(self, nombre, categoria, precio, disponible=True):
        self.__nombre = nombre
        self.__categoria = categoria
        self.__precio = precio
        self.__disponible = disponible

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def categoria(self):
        return self.__categoria

    @categoria.setter
    def categoria(self, valor):
        self.__categoria = valor

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self, valor):
        if valor >= 0:
            self.__precio = valor

    @property
    def disponible(self):
        return self.__disponible

    @disponible.setter
    def disponible(self, valor):
        self.__disponible = valor

    def __str__(self):
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.nombre} | {self.categoria} | ${self.precio:.2f} | {estado}"