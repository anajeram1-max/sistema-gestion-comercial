from archivos import cargar_datos, guardar_datos
from datetime import datetime

ARCHIVO_PRODUCTOS = "productos.json"
ARCHIVO_VENTAS = "ventas.json"


def obtener_productos():
    return cargar_datos(ARCHIVO_PRODUCTOS, [])


def obtener_ventas():
    return cargar_datos(ARCHIVO_VENTAS, [])


def registrar_venta():
    productos = obtener_productos()

    if not productos:
        print("\nNo hay productos registrados.")
        return

    print("\n===== PRODUCTOS DISPONIBLES =====")

    disponibles = [
        p for p in productos
        if p.get("activo", True) and p["cantidad"] > 0
    ]

    if not disponibles:
        print("No hay productos disponibles para vender.")
        return

    for producto in disponibles:
        print(
            f"Codigo: {producto['codigo']} | "
            f"Nombre: {producto['nombre']} | "
            f"Precio: Q{producto['precio']:.2f} | "
            f"Existencias: {producto['cantidad']}"
        )

    venta = []
    subtotal_general = 0

    while True:
        codigo = input("\nIngrese el codigo del producto (0 para terminar): ").strip()

        if codigo == "0":
            break

        producto_encontrado = None

        for producto in productos:
            if producto["codigo"].lower() == codigo.lower() and producto.get("activo", True):
                producto_encontrado = producto
                break

        if producto_encontrado is None:
            print("Producto no encontrado.")
            continue

        try:
            cantidad = int(input("Ingrese la cantidad que desea vender: "))

            if cantidad <= 0:
                print("La cantidad debe ser mayor que cero.")
                continue

            if cantidad > producto_encontrado["cantidad"]:
                print("No hay suficiente inventario.")
                continue

        except ValueError:
            print("Ingrese una cantidad valida.")
            continue

        precio = producto_encontrado["precio"]
        subtotal = precio * cantidad

        venta.append({
            "codigo": producto_encontrado["codigo"],
            "nombre": producto_encontrado["nombre"],
            "cantidad": cantidad,
            "precio": precio,
            "subtotal": subtotal
        })

        subtotal_general += subtotal
        producto_encontrado["cantidad"] -= cantidad

        print("Producto agregado a la venta.")

    if not venta:
        print("\nNo se registraron productos en la venta.")
        return

    iva = subtotal_general * 0.12
    total = subtotal_general + iva

    ventas = obtener_ventas()

    numero_venta = len(ventas) + 1

    nueva_venta = {
    "numero": numero_venta,
    "fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "productos": venta,
    "subtotal": subtotal_general,
    "iva": iva,
    "total": total
}

    ventas.append(nueva_venta)

    guardar_datos(ARCHIVO_PRODUCTOS, productos)
    guardar_datos(ARCHIVO_VENTAS, ventas)

    print("\n========== FACTURA ==========")
    print(f"Numero de venta: {numero_venta}")

    for detalle in venta:
        print(
            f"{detalle['nombre']} | "
            f"{detalle['cantidad']} unidades | "
            f"Q{detalle['subtotal']:.2f}"
        )

    print("-----------------------------")
    print(f"Subtotal: Q{subtotal_general:.2f}")
    print(f"IVA (12%): Q{iva:.2f}")
    print(f"TOTAL: Q{total:.2f}")
    print("=============================")


def mostrar_ventas():
    ventas = obtener_ventas()

    if not ventas:
        print("\nNo hay ventas registradas.")
        return

    print("\n========== HISTORIAL DE VENTAS ==========")

    for venta in ventas:
        print(f"\nVenta numero: {venta['numero']}")
        print(f"Subtotal: Q{venta['subtotal']:.2f}")
        print(f"IVA: Q{venta['iva']:.2f}")
        print(f"Total: Q{venta['total']:.2f}")


def menu_ventas():
    while True:
        print("\n================================")
        print("       REGISTRO DE VENTAS")
        print("================================")
        print("1. Registrar venta")
        print("2. Mostrar historial de ventas")
        print("3. Regresar al menu principal")
        print("================================")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_venta()
        elif opcion == "2":
            mostrar_ventas()
        elif opcion == "3":
            break
        else:
            print("Opcion no valida. Intente nuevamente.")