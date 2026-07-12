from producto import Producto
from cliente import Cliente
from restaurente import Restaurante 

restaurante = Restaurante()

while True:

    print("\n===== RESTAURANTE =====")
    print("1. Agregar producto")
    print("2. Agregar cliente")
    print("3. Listar productos")
    print("4. Listar clientes")
    print("5. Buscar producto")
    print("6. Buscar cliente")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: "))
        disponible = input("Disponible (s/n): ").lower() == "s"

        producto = Producto(nombre, categoria, precio, disponible)
        restaurante.agregar_producto(producto)

    elif opcion == "2":
        nombre = input("Nombre: ")
        correo = input("Correo: ")
        identificacion = input("Identificación: ")

        cliente = Cliente(nombre, correo, identificacion)
        restaurante.agregar_cliente(cliente)

    elif opcion == "3":
        restaurante.listar_productos()

    elif opcion == "4":
        restaurante.listar_clientes()

    elif opcion == "5":
        nombre = input("Nombre del producto: ")
        producto = restaurante.buscar_producto(nombre)

        if producto:
            print(producto)
        else:
            print("Producto no encontrado.")

    elif opcion == "6":
        identificacion = input("Identificación: ")
        cliente = restaurante.buscar_cliente(identificacion)

        if cliente:
            print(cliente)
        else:
            print("Cliente no encontrado.")

    elif opcion == "7":
        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")

