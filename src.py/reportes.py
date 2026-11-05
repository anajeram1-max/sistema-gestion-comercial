
from archivos import cargar_datos
from datetime import datetime

ARCHIVO_PRODUCTOS = "productos.json"
ARCHIVO_VENTAS = "ventas.json"


def obtener_productos():
    return cargar_datos(ARCHIVO_PRODUCTOS, [])


def obtener_ventas():
    return cargar_datos(ARCHIVO_VENTAS, [])


def mostrar_productos():
    productos = obtener_productos()

    print("\n===== LISTA DE PRODUCTOS =====")

    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        if producto.get("activo", True):
            print("--------------------------------")
            print("Codigo:", producto["codigo"])
            print("Nombre:", producto["nombre"])
            print("Categoria:", producto["categoria"])
            print(f"Precio: Q{producto['precio']:.2f}")
            print("Cantidad:", producto["cantidad"])


def mostrar_bajo_stock():
    productos = obtener_productos()
    encontrados = False

    print("\n===== PRODUCTOS CON BAJO STOCK =====")

    for producto in productos:
        stock_minimo = producto.get(
            "stock_minimo", producto.get("stock_min", 0)
        )

        if (producto.get("activo", True)
                and producto["cantidad"] <= stock_minimo):
            print(
                f"{producto['nombre']} | "
                f"Existencias: {producto['cantidad']} | "
                f"Stock minimo: {stock_minimo}"
            )
            encontrados = True

    if not encontrados:
        print("No hay productos con bajo stock.")


def mostrar_historial_ventas():
    ventas = obtener_ventas()

    print("\n===== HISTORIAL DE VENTAS =====")

    if not ventas:
        print("No hay ventas registradas.")
        return

    for venta in ventas:
        print("--------------------------------")
        print("Numero de venta:", venta["numero"])
        print(f"Subtotal: Q{venta['subtotal']:.2f}")
        print(f"IVA: Q{venta['iva']:.2f}")
        print(f"Total: Q{venta['total']:.2f}")


def calcular_ingresos():
    ventas = obtener_ventas()

    if not ventas:
        print("\nNo hay ventas para calcular ingresos.")
        return

    total_ingresos = sum(venta["total"] for venta in ventas)

    print("\n===== INGRESOS TOTALES =====")
    print(f"Ingresos: Q{total_ingresos:.2f}")


def producto_mas_vendido():
    ventas = obtener_ventas()

    if not ventas:
        print("\nNo hay ventas registradas.")
        return

    cantidades = {}

    for venta in ventas:
        for detalle in venta["productos"]:
            nombre = detalle["nombre"]
            cantidad = detalle["cantidad"]

            cantidades[nombre] = cantidades.get(nombre, 0) + cantidad

    if not cantidades:
        print("No hay productos vendidos.")
        return

    nombre = max(cantidades, key=cantidades.get)

    print("\n===== PRODUCTO MAS VENDIDO =====")
    print("Producto:", nombre)
    print("Unidades vendidas:", cantidades[nombre])


def valor_total_inventario():
    productos = obtener_productos()

    if not productos:
        print("\nNo hay productos registrados.")
        return

    total = 0

    for producto in productos:
        if producto.get("activo", True):
            total += producto["precio"] * producto["cantidad"]

    print("\n===== VALOR DEL INVENTARIO =====")
    print(f"Valor total: Q{total:.2f}")



def calcular_promedio_periodo(tipo):
    ventas = obtener_ventas()
    totales_periodos = {}

    if not ventas:
        print("\nNo hay ventas registradas.")
        return

    for venta in ventas:
        fecha_venta = venta.get("fecha")

        if not fecha_venta:
            continue

        fecha = datetime.strptime(
            fecha_venta, "%Y-%m-%d %H:%M:%S"
        )

        if tipo == "diario":
            periodo = fecha.strftime("%d/%m/%Y")

        elif tipo == "semanal":
            periodo = fecha.strftime("%G-Semana %V")

        else:
            periodo = fecha.strftime("%m/%Y")

        totales_periodos[periodo] = (
            totales_periodos.get(periodo, 0) + venta["total"]
        )

    if not totales_periodos:
        print("\nNo hay ventas con fecha registrada.")
        print("Registre nuevas ventas para calcular los promedios.")
        return

    total = sum(totales_periodos.values())
    promedio = total / len(totales_periodos)

    print(f"\n===== PROMEDIO DE VENTAS {tipo.upper()} =====")

    for periodo, importe in sorted(totales_periodos.items()):
        print(f"{periodo}: Q{importe:.2f}")

    print("--------------------------------")
    print(f"Cantidad de periodos: {len(totales_periodos)}")
    print(f"Total vendido: Q{total:.2f}")
    print(f"Promedio {tipo}: Q{promedio:.2f}")


def promedio_diario():
    calcular_promedio_periodo("diario")


def promedio_semanal():
    calcular_promedio_periodo("semanal")


def promedio_mensual():
    calcular_promedio_periodo("mensual")

def menu_reportes():
    while True:
        print("\n================================")
        print("    REPORTES Y ESTADISTICAS")
        print("================================")
        print("1. Mostrar lista de productos")
        print("2. Mostrar productos con bajo stock")
        print("3. Mostrar historial de ventas")
        print("4. Calcular ingresos totales")
        print("5. Mostrar producto mas vendido")
        print("6. Calcular valor del inventario")
        print("7. Promedio de ventas diario")
        print("8. Promedio de ventas semanal")
        print("9. Promedio de ventas mensual")
        print("10. Regresar al menu principal")
        print("================================")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            mostrar_productos()
        elif opcion == "2":
            mostrar_bajo_stock()
        elif opcion == "3":
            mostrar_historial_ventas()
        elif opcion == "4":
            calcular_ingresos()
        elif opcion == "5":
            producto_mas_vendido()
        elif opcion == "6":
            valor_total_inventario()
        elif opcion == "7":
            promedio_diario()
        elif opcion == "8":
            promedio_semanal()
        elif opcion == "9":
            promedio_mensual()
        elif opcion == "10":
            break
        else:
            print("Opcion no valida. Intente nuevamente.")