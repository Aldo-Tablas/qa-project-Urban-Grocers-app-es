Bootcamp TripleTen-QA Proyecto Urban Grocers
Aldo Tablas Ramírez 

-Descripcón del proyecto
Este proyecto contiene pruebas automatizadas para verificar la validez del campo `name`
al crear kits de productos en la aplicación Urban Grocers.

-Tecnologías utilizadas
 1. Git Bash para clonar el repositorio 
 2. Pychard para realizar el proyecto
 3. Pytest para las pruebas dentro de Pychard
 4. Request para las solicitudes en Pychard

-Qué hice en el proyecto

1. Analicé los requerimientos funcionales del campo `name` para la creación de kits de productos.
2. Diseñé y desarrollé **casos de prueba automatizados** para validar:
   - Valores válidos e inválidos del campo `name`
   - Longitud mínima y máxima permitida
   - Tipos de datos incorrectos
3. Implementé pruebas automatizadas utilizando **Pytest** y **Requests**.
4. Ejecuté las pruebas desde la terminal y validé las respuestas de la API.
5. Documenté los resultados obtenidos durante la ejecución de las pruebas.

---

-Resultados obtenidos

1. Validación correcta del comportamiento del campo `name` frente a diferentes escenarios.
2. Detección de inconsistencias en la validación de datos enviados a la API.
3. Confirmación del correcto manejo de errores ante valores inválidos.
4. Mejora en la cobertura de pruebas para la funcionalidad de creación de kits.

-Instrucciones para configurar el entorno
Desde Git Bash crear una carpeta con mkdir llamada projects despues cambiar a esa carpeta
con el comando cd projects y clonar el repositorio con el comando 
git clone git@github.com:Aldo-Tablas/qa-project-Urban-Grocers-app-es.git

-Detalles sobre cómo instalar y usar las librerías necesarias
Desde la terminal de pychard poner el comando pip install pytest requests para instalar 
en el entorno del projecto pytest para hacer las pruebas y las librerias request para 
hacer las solicitudes.

-Indicaciones claras para ejecutar las pruebas desde la terminal
Desde la terminal de pychard poner el comando pytest create_kit_name_kit_test. py 
para realizar las pruebas.
