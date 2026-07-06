from producto import Producto


class Bebidas(Producto):

    def __init__(self, nombre, precio, disponible, volumen):
        super().__init__(nombre, precio, disponible)
        self.volumen = volumen

    def mostrar_informacion(self):
        return (
            "=== BEBIDAs ===\n"
            f"{super().mostrar_informacion()}\n"
            f"Volumen: {self.volumen} ml"
        )
    