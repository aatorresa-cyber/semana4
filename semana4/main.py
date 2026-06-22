from producto import Producto
from cliente import Cliente
from restaurante import Restaurante
restaurante = Restaurante("Sabor Amazónico")
p1 = Producto("Arroz con pollo", 5.50, "Plato fuerte")
p2 = Producto("Jugo de naranja", 2.00, "Bebida")
c1 = Cliente("María López", "1234567890", "0987654321")
c2 = Cliente("Juan Pérez", "0987654321", "0991234567")
restaurante.agregar_producto(p1)
restaurante.agregar_producto(p2)

restaurante.agregar_cliente(c1)
restaurante.agregar_cliente(c2)
print("=== RESTAURANTE ===")
print(restaurante.nombre)

restaurante.mostrar_productos()
restaurante.mostrar_clientes()
