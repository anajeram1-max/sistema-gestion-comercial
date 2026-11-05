# SISTEMA DE GESTIÓN COMERCIAL

## 1. Descripción del proyecto

El Sistema de Gestión Comercial es una aplicación desarrollada en el lenguaje de programación Python, cuyo propósito es facilitar la administración y el control de las operaciones de un negocio.

El sistema permite gestionar productos, registrar ventas, controlar el inventario y generar reportes para conocer el estado de las operaciones comerciales.

## 2. Objetivo general

Desarrollar un sistema informático que permita administrar de manera organizada y eficiente los productos, las ventas y el inventario de un negocio, utilizando herramientas de programación y almacenamiento de datos.

## 3. Funcionalidades principales

El sistema cuenta con las siguientes opciones:

- **Gestión de productos:** permite registrar, consultar, mostrar, modificar y desactivar productos.
- **Registro de ventas:** permite seleccionar productos, ingresar cantidades, calcular subtotales, aplicar el IVA del 12 % y obtener el total de la venta.
- **Gestión de inventario:** permite consultar existencias, registrar entradas de productos, actualizar cantidades y revisar movimientos.
- **Generación de reportes:** permite consultar información de productos, ventas, ingresos, productos más vendidos y valor del inventario.
- **Almacenamiento de datos:** utiliza archivos JSON para guardar la información y conservar los registros del sistema.

## 4. Tecnologías utilizadas

- Lenguaje de programación: Python.
- Editor de código: Visual Studio Code.
- Almacenamiento: archivos JSON.
- Control de versiones: Git.
- Repositorio remoto: GitHub.

## 5. Estructura del proyecto

```text
SISTEMA-GESTION-COMERCIAL/
│
├── src.py/
│   ├── main.py
│   ├── productos.py
│   ├── ventas.py
│   ├── inventario.py
│   ├── reportes.py
│   └── archivos.py
│
├── datos/
│   ├── productos.json
│   ├── ventas.json
│   └── movimientos.json
│
├── docs/
│   ├── analisis/
│   ├── diagramas/
│   ├── manual tecnico/
│   └── manual usuario/
│
├── evidencias/
│   └── EVIDENCIA.pdf
│
├── .gitignore
└── README.md
```

## 6. Requisitos para ejecutar el sistema

- Tener instalado Python.
- Tener instalado Visual Studio Code o utilizar una terminal de comandos.
- Descargar o clonar el repositorio del proyecto.

## 7. Instrucciones de ejecución

1. Abrir la carpeta del proyecto en Visual Studio Code.
2. Abrir la terminal.
3. Ubicarse en la carpeta principal del proyecto.
4. Ejecutar el siguiente comando:

```powershell
python .\src.py\main.py
```

5. Utilizar las opciones del menú principal para administrar los productos, las ventas, el inventario y los reportes.

## 8. Documentación

El proyecto incluye documentación complementaria:

- Análisis de los procesos del sistema.
- Diagramas de flujo de los principales procedimientos.
- Manual técnico.
- Manual de usuario.
- Evidencias de pruebas del funcionamiento.

## 9. Control de versiones

El desarrollo del proyecto se realizó utilizando Git para llevar un registro de los cambios y GitHub para almacenar y compartir el código fuente.

## 10. Conclusión

El Sistema de Gestión Comercial permite organizar y facilitar las actividades principales de un negocio mediante una aplicación desarrollada en Python. Su implementación contribuye al control de productos, ventas e inventario, además de proporcionar información útil para la toma de decisiones.


## Estado del proyecto

El Sistema de Gestión Comercial se encuentra desarrollado en Python.
Incluye gestión de productos, ventas, inventario y generación de reportes.
Los datos se almacenan mediante archivos JSON.