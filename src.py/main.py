from productos import menu_productos
from ventas import menu_ventas
from inventario import menu_inventario
from reportes import menu_reportes

def mostrar_menu():
    print("\n====================================")
    print("     SISTEMA DE GESTION COMERCIAL")
    print("====================================")
    print("1. Gestion de productos")
    print("2. Registro de ventas")
    print("3. Control de inventarios")
    print("4. Reportes y estadisticas")
    print("5. Salir")
    print("====================================")


def menu_principal():

    while True:
        mostrar_menu()

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            menu_productos()

        elif opcion == "2":
            menu_ventas()

        elif opcion == "3":
            menu_inventario()
            
        elif opcion == "4":
            menu_reportes()

        elif opcion == "5":
            print("\nGracias por utilizar el sistema.")
            break

        else:
            print("\nError: opcion no valida.")
            print("Por favor, intente nuevamente.")


if __name__ == "__main__":
    menu_principal()
