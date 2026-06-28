from restaurantes import Restaurantes
from menú import registrar_producto
from menú import registrar_cliente


restaurantes = Restaurantes("Restaurante Amazónico")

while True:

    print("\n====== MENÚ ======")
    print("1. Registrar producto")
    print("2. Registrar cliente")
    print("3. Mostrar productos")
    print("4. Mostrar clientes")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_producto(restaurante)

    elif opcion == "2":
        registrar_cliente(restaurante)

    elif opcion == "3":
        restaurante.mostrar_productos()

    elif opcion == "4":
        restaurante.mostrar_clientes()

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción incorrecta.")
        