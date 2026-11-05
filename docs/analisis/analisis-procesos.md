Aquí está la información proporcionada por el usuario:

# ANÁLISIS DEL SISTEMA DE GESTIÓN COMERCIAL

## 1. Introducción

Este análisis busca identificar y describir los procesos que forman el Sistema de Gestión Comercial, que se desarrolló en el lenguaje Python.

El sistema sirve para administrar productos, registrar ventas, controlar inventario y generar informes. Para lograr esto, el sistema se divide en módulos que ayudan a organizar las tareas y guardar la información en archivos JSON.

Antes de explicar cada proceso, se definen sus objetivos, los datos que se usan, las operaciones que se realizan, los resultados esperados, las reglas que se siguen, las validaciones necesarias y los errores que pueden ocurrir. También se establece la lógica que se representará con diagramas de flujo.

## 2. Objetivo general del análisis

Analizar los principales procesos del Sistema de Gestión Comercial para entender cómo funciona, definir qué datos se necesitan, establecer las reglas de negocio y determinar las validaciones que permiten realizar las operaciones de forma correcta y confiable.

## 3. Análisis de los procesos funcionales

### 3.1. Proceso de registro de productos

**Nombre del proceso:** Registro de productos.

**Objetivo:** Permitir agregar nuevos productos al sistema para mantener el catálogo actualizado.

**Descripción del funcionamiento:**

El usuario elige la opción de registrar un producto en el módulo correspondiente. El sistema pide los datos necesarios como código, nombre, categoría, precio de venta, cantidad inicial y stock mínimo. Luego verifica que la información sea correcta y que el código no esté repetido. Si todo está bien, el producto se guarda en un archivo.

**Datos de entrada:**

- Código del producto.

- Nombre del producto.

- Categoría.

- Precio de venta.

- Cantidad inicial.

- Stock mínimo.

**Procesamiento realizado:**

1. Pedir los datos del producto.

2. Verificar que los campos obligatorios no estén vacíos.

3. Revisar que el código no esté usado.

4. Asegurar que el precio y las cantidades sean positivas.

5. Crear el registro del producto.

6. Guardar la información en el archivo JSON.

**Datos de salida:**

- Mensaje de que el producto se registró correctamente.

- Mensaje de error si hay problemas.

- Actualización del archivo de productos.

**Reglas de negocio:**

- Cada producto debe tener un código único.

- El nombre y la categoría son obligatorios.

- El precio no puede ser negativo.

- La cantidad y el stock mínimo no pueden ser negativos.

**Validaciones y posibles errores:**

- Código duplicado.

- Campos obligatorios vacíos.

- Precio negativo o datos incorrectos.

- Cantidad o stock mínimo negativo.

- Error al guardar el archivo.

**Diagrama de flujo correspondiente:** Registro de productos.

### 3.2. Proceso de consulta y modificación de productos

**Nombre del proceso:** Consulta y modificación de productos.

**Objetivo:** Facilitar la búsqueda de productos y permitir que se actualice su información cuando sea necesario.

**Descripción del funcionamiento:**

El usuario puede buscar un producto por su código. El sistema busca en el archivo de productos y muestra los datos si encuentra algo. Cuando elige modificar, el usuario puede cambiar el nombre, categoría, precio, cantidad o stock mínimo. Los cambios se guardan en el archivo JSON.

**Datos de entrada:**

- Código del producto que se quiere consultar o modificar.

- Nuevos datos como nombre, categoría, precio, cantidad o stock mínimo.

**Procesamiento realizado:**

1. Pedir el código del producto.

2. Buscar el código en los registros.

3. Verificar si el producto existe.

4. Mostrar la información encontrada.

5. Solicitar los nuevos datos que se quieren cambiar.

6. Validar la información ingresada.

7. Actualizar el registro y guardar los cambios.

**Datos de salida:**

- Información del producto consultado.

- Confirmación de los cambios.

- Mensaje indicando que el producto no existe, si aplica.

**Reglas de negocio:**

- Solo se pueden consultar o modificar productos ya registrados.

- El código del producto se usa como identificador.

- Los nuevos precios y cantidades no pueden ser negativos.

- Los campos que no se quieren cambiar se mantienen como están.

**Validaciones y posibles errores:**

- Código no encontrado.

- Datos numéricos incorrectos.

- Precio o cantidades negativas.

- Error al guardar los cambios.

**Diagrama de flujo correspondiente:** Consulta y modificación de productos.

### 3.3. Proceso de registro de ventas

**Nombre del proceso:** Registro de ventas.

**Objetivo:** Registrar las ventas realizadas, calcular los importes y actualizar las existencias de los productos vendidos.

**Descripción del funcionamiento:**

El usuario elige la opción de registrar una venta y escribe el código del producto y la cantidad que quiere vender. El sistema revisa que el producto exista, esté activo y tenga suficiente inventario. Luego calcula el subtotal, el IVA del 12% y el total. Finalmente, guarda la venta y reduce el inventario.

**Datos de entrada:**

- Código del producto.

- Cantidad a vender.

- Precio de venta del producto, tomado del registro.

**Procesamiento realizado:**

1. Empezar el registro de la venta.

2. Pedir el código del producto.

3. Buscar el producto en el catálogo.

4. Verificar que exista y esté activo.

5. Pedir la cantidad a vender.

6. Validar que sea mayor que cero.

7. Comprobar que haya suficiente inventario.

8. Calcular el subtotal.

9. Calcular el IVA del 12%.

10. Calcular el total.

11. Generar el número de venta y la fecha.

12. Guardar la venta en el archivo JSON.

13. Reducir las unidades vendidas del inventario.

**Datos de salida:**

- Número y fecha de la venta.

- Detalles de los productos vendidos.

- Subtotal.

- IVA del 12%.

- Total a pagar.

- Inventario actualizado.

- Registro de la venta.

**Reglas de negocio:**

- El producto debe existir y estar activo.

- La cantidad vendida debe ser mayor que cero.

- No se puede vender más de lo disponible.

- El precio usado debe ser el del producto registrado.

- El IVA aplicado es del 12%.

- Las ventas se guardan en el historial.

**Validaciones y posibles errores:**

- Código de producto no encontrado.

- Producto desactivado.

- Cantidad igual o menor que cero.

- Inventario insuficiente.

- Error al guardar la venta.

**Diagrama de flujo correspondiente:** Registro de ventas.

### 3.4. Proceso de actualización de inventario

**Nombre del proceso:** Actualización y control de inventario.

**Objetivo:** Mantener las cantidades de los productos actualizadas y controlar las entradas y ajustes.

**Descripción del funcionamiento:**

El usuario entra al módulo de inventario y elige la operación que quiere hacer. Puede consultar las existencias, registrar entradas o cambiar las cantidades manualmente. Cada cambio se guarda en un historial con fecha, código, tipo de movimiento, cantidad y descripción.

**Datos de entrada:**

- Código del producto.

- Cantidad de entrada o nueva existencia.

- Tipo de movimiento.

- Descripción del movimiento.

**Procesamiento realizado:**

1. Pedir el código del producto.

2. Buscar el producto registrado.

3. Verificar que exista.

4. Pedir la cantidad correspondiente.

5. Validar que la cantidad sea correcta.

6. Actualizar las existencias.

7. Registrar el movimiento.

8. Guardar los cambios en los archivos JSON.

**Datos de salida:**

- Existencias actualizadas.

- Mensaje de confirmación.

- Historial de movimientos.

- Advertencia sobre productos con bajo stock.

**Reglas de negocio:**

- El producto debe estar registrado.

- Las entradas deben ser cantidades positivas.

- Las existencias no pueden ser negativas.

- Los movimientos deben tener fecha.

- Se considera bajo stock cuando la cantidad disponible es menor o igual al stock mínimo.

**Validaciones y posibles errores:**

- Código de producto no encontrado.

- Cantidad incorrecta o negativa.

- Datos numéricos no válidos.

- Error al guardar los movimientos.

**Diagrama de flujo correspondiente:** Actualización de inventario.

### 3.5. Proceso de lectura de archivos

**Nombre del proceso:** Lectura y recuperación de información almacenada.

**Objetivo:** Obtener la información guardada en los archivos JSON para usarla en las operaciones del sistema.

**Descripción del funcionamiento:**

El sistema usa archivos JSON para guardar productos, ventas y movimientos de inventario. Cuando un módulo necesita datos, pide leer el archivo correspondiente. El sistema revisa si el archivo existe y, si está disponible, carga los datos para usarlos. Si no existe o hay problemas, se usa una estructura inicial para que el programa no falle.

Si existe, abrílo y lee su contenido.

Convierte la información JSON en estructuras de datos de Python.

Si no existe, devuelve la estructura inicial.

Controla errores de lectura o formato.

**Datos de salida:**

Información recuperada del archivo.

Estructura inicial cuando el archivo no existe.

Mensaje de error cuando ocurre un problema de lectura.

**Reglas de negocio:**

Los archivos deben manejarse en la carpeta de datos del proyecto.

La información debe mantener su estructura JSON.

La lectura no debe cambiar los registros almacenados.

El sistema debe controlar archivos que no existen o que tienen formato incorrecto.

**Validaciones y posibles errores:**

Archivo no existe.

Archivo JSON está dañado o tiene formato incorrecto.

Problemas de permisos.

Error al leer el archivo.

**Diagrama de flujo correspondiente:** Lectura de archivos.

### 3.6. Proceso de generación de reportes

**Nombre del proceso:** Generación de reportes y estadísticas.

**Objetivo:** Ofrecer información organizada sobre productos, inventario y ventas para facilitar el análisis y la toma de decisiones.

**Descripción del funcionamiento:**

El usuario entra al módulo de reportes y elige el informe que quiere ver. El sistema recibe los datos almacenados y realiza los cálculos necesarios para mostrar información sobre productos, existencias, ventas, ingresos, producto más vendido, valor del inventario y promedios de ventas diarios, semanales o mensuales.

**Datos de entrada:**

Información sobre productos.

Historial de ventas.

Fechas de las ventas.

Cantidades y precios registrados.

**Procesamiento realizado:**

Lee la información sobre productos y ventas.

Identifica el tipo de reporte que se pide.

Procesa los registros correspondientes.

Calcula los ingresos y los valores del inventario.

Identifica productos con poco stock.

Encuentra el producto más vendido.

Calcula los promedios de ventas según el período.

Muestra los resultados al usuario.

**Datos de salida:**

Lista de productos.

Reporte de productos con bajo stock.

Historial de ventas.

Ingresos totales.

Producto más vendido.

Valor total del inventario.

Promedios de ventas diarios, semanales y mensuales.

**Reglas de negocio:**

Los reportes deben usar la información que está guardada.

Los ingresos se calculan con base en los totales de las ventas.

El producto más vendido se elige según las unidades que se han vendido.

El valor del inventario se calcula multiplicando las existencias por el precio de venta de cada producto activo.

Los promedios se calculan usando los períodos que tienen ventas.

No se hacen cálculos estadísticos si no hay datos suficientes.

**Validaciones y posibles errores:**

No hay productos registrados.

No hay ventas registradas.

No hay ventas con fechas para calcular promedios.

Datos que faltan o que están mal.

Error al leer los archivos.

**Diagrama de flujo correspondiente:** Generación de reportes.

## 4. Conclusión del análisis

El análisis de los procesos ayudó a identificar las operaciones principales del Sistema de Gestión Comercial y a establecer las condiciones necesarias para que funcione correctamente.

Dividir el sistema en módulos hace más fácil la administración de productos, el registro de ventas, el control de inventario y la generación de reportes. Además, las validaciones y las reglas de negocio ayudan a evitar errores al ingresar y procesar la información.

Por último, el uso de archivos JSON permite guardar los datos para que puedan consultarse en diferentes ejecuciones del programa. Los diagramas de flujo apoyarán este análisis al mostrar gráficamente las decisiones, las validaciones y las secuencias de cada proceso.