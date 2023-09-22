<p align="center">
  <a target="blank"><img src="7bd8ia2qa6k55khm7mgt0l4urc.png" alt="Javascript Logo @clipartmax.com" width="200" /></a>
</p>
<p align="center">
  <strong><span style="font-size: 30px;">(23004) Analista de Calidad</span></strong>
</p>
<p align="center">
  <strong><span style="font-size: 25px;">Jeferson Daniel Romero Acosta</span></strong>
</p>
<div align="center">
  <a href="https://www.linkedin.com/in/jefferdaniel0320/">
    <strong><span style="font-size: 20px;">linkedin/jefferdaniel0320</span></strong>
  </a>
</div>

# Instrucciones

Para acceder a la herramienta de pruebas, primero debe abrir PyCharm. Luego, proceda a instalar las siguientes bibliotecas en la terminal:
~~~
pip install selenium
~~~
Esto descargará e instalará la biblioteca Selenium en tu entorno de Python.

Verifica la instalación: Puedes verificar que Selenium se ha instalado correctamente ejecutando un comando simple en la terminal para importar Selenium y verificar que no hay errores:
~~~
python -c "import selenium"
~~~
Si no se visualiza ningún error, significa que Selenium se ha instalado correctamente.

A continuación, procederemos a ejecutar el archivo **main.py** Si deseamos modificar los datos de fecha y comentarios, debemos abrir el archivo **fechaComentarios.txt** y separarlos por **;**

Al ejecutar el archivo principal, observaremos cómo comienzan a ejecutarse las diferentes pruebas.

## Resumen del Programa

1. Define una lista de instalaciones de atención médica (selecFacilitys) y programas médicos (selectRadio_programs) para probar diferentes combinaciones.

2. Abre un archivo llamado fechaComentarios.txt, que contiene datos relacionados con fechas y comentarios que se utilizarán en las pruebas.

3. Inicia un bucle anidado que itera a través de las instalaciones de atención médica y los programas médicos.

4. Dentro de estos bucles, recorre cada línea del archivo fechaComentarios.txt y extrae datos como la fecha y el comentario.

5. Inicializa un navegador web (Google Chrome) utilizando Selenium y abre un sitio web específico (https://katalon-demo-cura.herokuapp.com/).

6. Lleva a cabo una serie de acciones en el sitio web, como hacer clic en botones, ingresar información en campos de texto y seleccionar opciones de menú desplegable.

7. Realiza una verificación al final de cada prueba para determinar si se mostró un mensaje de confirmación que dice "Appointment Confirmation".

8. Imprime un mensaje indicando si la prueba fue exitosa o falló.

9. Cierra el navegador después de cada prueba y continúa con la siguiente combinación de datos.

10. Maneja excepciones para tratar posibles errores durante la ejecución de las pruebas.

En resumen, este script automatiza pruebas en un sitio web de atención médica, probando diferentes combinaciones de instalaciones y programas médicos utilizando datos proporcionados en un archivo. Luego, informa si cada prueba fue exitosa o falló.