
import json
from pathlib import Path

# Crear carpeta para almacenar los datos
CARPETA_DATOS = Path(__file__).resolve().parent.parent / "datos"

CARPETA_DATOS.mkdir(exist_ok=True)


# FUNCION PARA CARGAR DATOS
def cargar_datos(nombre_archivo, valor_inicial):

    ruta = CARPETA_DATOS / nombre_archivo

    if not ruta.exists():
        return valor_inicial.copy()

    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)

    except (json.JSONDecodeError, OSError):
        print("Error al leer el archivo.")
        return valor_inicial.copy()


# FUNCION PARA GUARDAR DATOS
def guardar_datos(nombre_archivo, datos):

    ruta = CARPETA_DATOS / nombre_archivo

    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, indent=4, ensure_ascii=False)

        return True

    except OSError:
        print("Error al guardar la informacion.")
        return False
