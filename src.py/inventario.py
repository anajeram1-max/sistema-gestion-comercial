
from datetime import datetime
from archivos import cargar_datos, guardar_datos

ARCHIVO_PRODUCTOS = "productos.json"
ARCHIVO_MOVIMIENTOS = "movimientos.json"


def obtener_productos():
    return cargar_datos(ARCHIVO_PRODUCTOS, [])


def obtener_movimientos():
    return cargar_datos(ARCHIVO_MOVIMIENTOS, [])


def guardar_movimiento(codigo, tipo, cantidad, descripcion):
    movimientos = obtener_movimientos()

    movimiento = {
        "fecha": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        "codigo": codigo,
        "tipo": tipo,
        "cantidad": cantidad,
        "descripcion": descripcion
    }

    movimientos.append(movimiento)
    guardar_datos(ARCHIVO_MOVIMIENTOS, movimientos)


def consultar_stock():
    productos = obtener_productos()
    codigo = input("Ingrese el codigo del producto: ").strip()

    for producto in productos:
        if producto["codigo"].lower() == codigo.lower():
            print("\n--- EXISTENCIAS DEL PRODUCTO ---")
            print("Codigo:", producto["codigo"])
            print("Nombre:", producto["nombre"])
            print("Cantidad disponible:", producto["cantidad"])
            return

    print("Producto no encontrado.")


def registrar_entrada():
    productos = obtener_productos()
    codigo = input("Ingrese el codigo del producto: ").strip()

    for producto in productos:
        if producto["codigo"].lower() == codigo.lower():
            if not producto.get("activo", True):
                print("El producto esta desactivado.")
                return

            try:
                cantidad = int(input("Ingrese la cantidad que ingresa: "))

                if cantidad <= 0:
                    print("La cantidad debe ser mayor que cero.")
                    return

            except ValueError:
                print("Ingrese una cantidad valida.")
                return

            producto["cantidad"] += cantidad
            guardar_datos(ARCHIVO_PRODUCTOS, productos)

            guardar_movimiento(
                codigo, "ENTRADA", cantidad, "Entrada de productos"
            )

            print("Entrada registrada correctamente.")
            print("Existencias actuales:", producto["cantidad"])
            return

    print("Producto no encontrado.")


def actualizar_existencias():
    productos = obtener_productos()
    codigo = input("Ingrese el codigo del producto: ").strip()

    for producto in productos:
        if producto["codigo"].lower() == codigo.lower():
            try:
                nueva_cantidad = int(
                    input("Ingrese la nueva cantidad de existencias: ")
                )

                if nueva_cantidad < 0:
                    print("La cantidad no puede ser negativa.")
                    return

            except ValueError:
                print("Ingrese una cantidad valida.")
                return

            cantidad_anterior = producto["cantidad"]
            diferencia = nueva_cantidad - cantidad_anterior

            producto["cantidad"] = nueva_cantidad
            guardar_datos(ARCHIVO_PRODUCTOS, productos)

            guardar_movimiento(
                codigo,
                "AJUSTE",
                diferencia,
                "Actualizacion de existencias"
            )

            print("Inventario actualizado correctamente.")
            print("Existencias actuales:", nueva_cantidad)
            return

    print("Producto no encontrado.")


def mostrar_bajo_stock():
    productos = obtener_productos()
    encontrados = False

    print("\n--- PRODUCTOS CON BAJO STOCK ---")

    for producto in productos:
        stock_minimo = producto.get(
            "stock_minimo", producto.get("stock_min", 0)
        )

        if (producto.get("activo", True)
                and producto["cantidad"] <= stock_minimo):
            print(
                f"Codigo: {producto['codigo']} | "
                f"Nombre: {producto['nombre']} | "
                f"Cantidad: {producto['cantidad']} | "
                f"Stock minimo: {stock_minimo}"
            )
            encontrados = True

    if not encontrados:
        print("No hay productos con bajo stock.")


def mostrar_movimientos():
    movimientos = obtener_movimientos()

    if not movimientos:
        print("\nNo hay movimientos registrados.")
        return

    print("\n--- HISTORIAL DE MOVIMIENTOS ---")

    for movimiento in movimientos:
        print("--------------------------------")
        print("Fecha:", movimiento["fecha"])
        print("Codigo:", movimiento["codigo"])
        print("Tipo:", movimiento["tipo"])
        print("Cantidad:", movimiento["cantidad"])
        print("Descripcion:", movimiento["descripcion"])


def menu_inventario():
    while True:
        print("\n================================")
        print("       CONTROL DE INVENTARIOS")
        print("================================")
        print("1. Consultar existencias")
        print("2. Registrar entrada de productos")
        print("3. Actualizar existencias")
        print("4. Mostrar productos con bajo stock")
        print("5. Historial de movimientos")
        print("6. Regresar al menu principal")
        print("================================")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            consultar_stock()
        elif opcion == "2":
            registrar_entrada()
        elif opcion == "3":
            actualizar_existencias()
        elif opcion == "4":
            mostrar_bajo_stock()
        elif opcion == "5":
            mostrar_movimientos()
        elif opcion == "6":
            break
        else:
            print("Opcion no valida. Intente nuevamente.")
