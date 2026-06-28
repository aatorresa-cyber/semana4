from productos import Productos
from clientes import Clientes

def registrar_producto(restaurante):

    id_producto = int(input("ID: "))
    nombre = input("Nombre: ")
    precio = float(input("Precio: "))
    disponible = input("Disponible (s/n): ").lower() == "s"

    producto = Producto(id_producto, nombre, precio, disponible)

    restaurante.agregar_producto(producto)

    print("Producto registrado correctamente.")


def registrar_cliente(restaurante):

    id_cliente = int(input("ID: "))
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")

    cliente = Cliente(id_cliente, nombre, telefono)

    restaurante.agregar_cliente(cliente)

    print("Cliente registrado correctamente.")
