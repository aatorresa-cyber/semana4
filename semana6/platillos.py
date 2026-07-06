from producto import Producto


class Platillos(Producto):

    def __init__(self, nombre, precio, disponible, calorias):
        super().__init__(nombre, precio, disponible)
        self.calorias = calorias

    def mostrar_informacion(self):
        return (
            "=== PLATILLOS ===\n"
            f"{super().mostrar_informacion()}\n"
            f"Calorías: {self.calorias} kcal"
        )
    