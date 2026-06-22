class Cliente:
 def __init__(self, nombre, cedula, telefono):
        self.nombre = nombre
        self.cedula = cedula
        self.telefono = telefono

 def mostrar_info(self):
        return f"{self.nombre} - CI: {self.cedula} - Tel: {self.telefono}"

 def __str__(self):
        return self.mostrar_info()