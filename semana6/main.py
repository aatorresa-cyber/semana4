from platillos import Platillos
from bebidas import Bebidas
from restaurante import Restaurante

def menu():

    restaurante = Restaurante()

    while True:

        print("\n===== MENÚ =====")
        print("1. Agregar Platillo")
        print("2. Agregar Bebida")
        print("3. Mostrar Productos")
        print("4. Cambiar precio")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            nombre = input("Nombre del platillo: ")
            precio = float(input("Precio: "))
            disponible = input("¿Disponible? (s/n): ").lower() == "s"
            calorias = int(input("Calorías: "))

            platillos = Platillos(nombre, precio, disponible, calorias)

            restaurante.agregar_producto(platillos)

        elif opcion == "2":

            nombre = input("Nombre de la bebida: ")
            precio = float(input("Precio: "))
            disponible = input("¿Disponible? (s/n): ").lower() == "s"
            volumen = int(input("Volumen (ml): "))

            bebidas = Bebidas(nombre, precio, disponible, volumen)

            restaurante.agregar_producto(bebidas)

        elif opcion == "3":

            restaurante.mostrar_productos()

        elif opcion == "4":

            if len(restaurante.productos) == 0:
                print("No existen productos.")
                continue

            restaurante.mostrar_productos()

            indice = int(input("Seleccione el número del producto (1 al {}): ".format(len(restaurante.productos))))

            if indice >= 1 and indice <= len(restaurante.productos):

                nuevo_precio = float(input("Nuevo precio: "))

                restaurante.productos[indice - 1].cambiar_precio(nuevo_precio)

            else:
                print("Producto no válido.")

        elif opcion == "5":

            print("Gracias por utilizar el sistema.")
            break

        else:
            print("Opción incorrecta.")


menu()
