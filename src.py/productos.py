
from archivos import cargar_datos, guardar_datos

ARCHIVO_PRODUCTOS = "productos.json"


def obtener_productos():
    return cargar_datos(ARCHIVO_PRODUCTOS, [])


# 1. REGISTRAR PRODUCTOS
def registrar_producto():
    productos = obtener_productos()

    print("\n--- REGISTRAR PRODUCTO ---")

    codigo = input("Ingrese el codigo: ").strip()

    if not codigo:
        print("El codigo no puede estar vacio.")
        return

    for producto in productos:
        if producto["codigo"].lower() == codigo.lower():
            print("Error: el codigo ya existe.")
            return

    nombre = input("Ingrese el nombre: ").strip()

    if not nombre:
        print("El nombre no puede estar vacio.")
        return

    categoria = input("Ingrese la categoria: ").strip()

    if not categoria:
        print("La categoria no puede estar vacia.")
        return

    try:
        precio = float(input("Ingrese el precio de venta: "))
        cantidad = int(input("Ingrese la cantidad disponible: "))
        stock_minimo = int(input("Ingrese el stock minimo: "))

        if precio < 0 or cantidad < 0 or stock_minimo < 0:
            print("No se permiten valores negativos.")
            return

    except ValueError:
        print("Error: debe ingresar datos numericos validos.")
        return

    nuevo_producto = {
        "codigo": codigo,
        "nombre": nombre,
        "categoria": categoria,
        "precio": precio,
        "cantidad": cantidad,
        "stock_minimo": stock_minimo,
        "activo": True
    }

    productos.append(nuevo_producto)

    if guardar_datos(ARCHIVO_PRODUCTOS, productos):
        print("Producto registrado correctamente.")


# 2. CONSULTAR PRODUCTO
def consultar_producto():
    productos = obtener_productos()

    codigo = input("Ingrese el codigo del producto: ").strip()

    for producto in productos:
        if producto["codigo"].lower() == codigo.lower():
            print("\n--- INFORMACION DEL PRODUCTO ---")
            print("Codigo:", producto["codigo"])
            print("Nombre:", producto["nombre"])
            print("Categoria:", producto["categoria"])
            print("Precio: Q", producto["precio"])
            print("Cantidad:", producto["cantidad"])
            print("Stock minimo:", producto["stock_minimo"])
            print("Estado:", "Activo" if producto["activo"] else "Inactivo")
            return

    print("Producto no encontrado.")


# 3. MOSTRAR PRODUCTOS
def mostrar_productos():
    productos = obtener_productos()

    print("\n--- LISTADO DE PRODUCTOS ---")

    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        print("\nCodigo:", producto["codigo"])
        print("Nombre:", producto["nombre"])
        print("Categoria:", producto["categoria"])
        print("Precio: Q", producto["precio"])
        print("Cantidad:", producto["cantidad"])
        print("Stock minimo:", producto["stock_minimo"])
        print("Estado:", "Activo" if producto["activo"] else "Inactivo")
        print("-----------------------------")


# 4. MODIFICAR PRODUCTO
def modificar_producto():
    productos = obtener_productos()

    codigo = input("Ingrese el codigo del producto: ").strip()

    for producto in productos:
        if producto["codigo"].lower() == codigo.lower():

            print("Deje vacio el campo si no desea modificarlo.")

            nombre = input("Nuevo nombre: ").strip()
            categoria = input("Nueva categoria: ").strip()
            precio = input("Nuevo precio: ").strip()
            cantidad = input("Nueva cantidad: ").strip()
            stock = input("Nuevo stock minimo: ").strip()

            try:
                if nombre:
                    producto["nombre"] = nombre

                if categoria:
                    producto["categoria"] = categoria

                if precio:
                    nuevo_precio = float(precio)
                    if nuevo_precio < 0:
                        print("Precio negativo no permitido.")
                        return
                    producto["precio"] = nuevo_precio

                if cantidad:
                    nueva_cantidad = int(cantidad)
                    if nueva_cantidad < 0:
                        print("Cantidad negativa no permitida.")
                        return
                    producto["cantidad"] = nueva_cantidad

                if stock:
                    nuevo_stock = int(stock)
                    if nuevo_stock < 0:
                        print("Stock negativo no permitido.")
                        return
                    producto["stock_minimo"] = nuevo_stock

            except ValueError:
                print("Error: ingrese valores numericos validos.")
                return

            if guardar_datos(ARCHIVO_PRODUCTOS, productos):
                print("Producto modificado correctamente.")
            return

    print("Producto no encontrado.")


# 5. DESACTIVAR PRODUCTO
def desactivar_producto():
    productos = obtener_productos()

    codigo = input("Ingrese el codigo del producto: ").strip()

    for producto in productos:
        if producto["codigo"].lower() == codigo.lower():

            if not producto["activo"]:
                print("El producto ya esta desactivado.")
                return

            producto["activo"] = False

            if guardar_datos(ARCHIVO_PRODUCTOS, productos):
                print("Producto desactivado correctamente.")
            return

    print("Producto no encontrado.")


# MENU DE PRODUCTOS
def menu_productos():

    while True:
        print("\n================================")
        print("       GESTION DE PRODUCTOS")
        print("================================")
        print("1. Registrar producto")
        print("2. Consultar producto")
        print("3. Mostrar productos")
        print("4. Modificar producto")
        print("5. Desactivar producto")
        print("6. Regresar al menu principal")
        print("================================")

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            registrar_producto()

        elif opcion == "2":
            consultar_producto()

        elif opcion == "3":
            mostrar_productos()

        elif opcion == "4":
            modificar_producto()

        elif opcion == "5":
            desactivar_producto()

        elif opcion == "6":
            break

        else:
            print("Opcion no valida. Intente nuevamente.")
