# Examen Modulo 2

## En una aplicación de juego, un programador quiere implementar diferentes acciones dependiendo de la puntuación del jugador. Si la puntuación es superior a 100, se concede una vida extra. Si la puntuación está entre 50 y 100, se añaden puntos extra. En caso contrario, se mostrará el mensaje "¡Inténtalo de nuevo! ¿Qué Sentencia condicional sería la más adecuada para este escenario? Seleccione todas las que corresponda.

- [x] Una declaración anidada if dentro del bloque else para diferenciar aún más las acciones para puntuaciones inferiores al 50

Correcto Se necesita una sentencia if para comprobar la condición de que la puntuación sea superior a 100.

- [ ] Una sentencia if para comprobar si la puntuación es superior a 100
- [x] Una sentencia elif para comprobar si la puntuación está entre 50 y 100

Correcto Una sentencia elif es apropiada para comprobar el rango de puntuación intermedio entre 50 y 100.

- [x] Una sentencia else para tratar los casos en los que la puntuación es inferior al 50

Correcto Se puede utilizar una sentencia else para manejar el escenario en el que no se cumple ninguna de las condiciones anteriores (if y elif) (puntuación inferior a 50).


## Usted está desarrollando un juego en el que el jugador tiene que adivinar un número secreto entre 1 y 100. ¿Qué bucle sería el más adecuado para preguntar repetidamente al jugador hasta que adivine el número correcto? Seleccione la mejor respuesta.

- [ ] En este caso podrían utilizarse indistintamente los bucles for o while 
- [ ] Bucles anidados for, para recorrer todos los números posibles y compararlos con la suposición del jugador
- [ ] Un bucle for, ya que está diseñado para iterar sobre una secuencia conocida de números
- [x] Un bucle while, ya que continúa ejecutándose mientras la suposición del jugador sea incorrecta

Correcto Un bucle while es ideal aquí porque el número de adivinanzas es desconocido de antemano, y el bucle necesita continuar hasta que el jugador adivine correctamente.


## Está desarrollando un sitio web de comercio electrónico. Necesita mostrar diferentes contenidos a los usuarios en función de su estado de conexión. Por ejemplo, los usuarios registrados deberían ver su historial de pedidos y recomendaciones personalizadas, mientras que los usuarios invitados deberían ver avisos de registro y listados generales de productos. ¿Qué mecanismos de flujo de control serían esenciales para implementar esta experiencia del usuario personalizada? Seleccione todos los que correspondan.

- [x] Un bucle for para recorrer una lista de productos y mostrarlos a todos los usuarios

Correcto Se puede utilizar un bucle for para mostrar listados de productos, que son relevantes tanto para los usuarios registrados como para los invitados.

- [ ] Bucles anidados for para mostrar diferentes categorías de productos a distintos grupos de usuarios
- [ ] Un bucle while para comprobar continuamente los cambios en el estado de inicio de sesión del usuario
- [x] Sentencias condicionales (if, elif, else) para comprobar si un usuario está conectado y mostrar el contenido apropiado

Correcto Las Sentencias condicionales son cruciales para diferenciar entre usuarios registrados e invitados y presentarles el contenido relevante.

## Un colega te pide que revises su código Python. Quieres sugerir opciones para ver los valores de las variables en varios lugares del programa. ¿Qué métodos sugerirías? Selecciona todos los que correspondan.

- [x] Utilizar un depurador para recorrer el código línea por línea e inspeccionar los valores de las variables

Correcto Los depuradores permiten detener la ejecución y examinar el estado de las variables en cualquier punto, lo que ayuda a comprender el flujo de datos.

- [ ] Basarse en los comentarios del código para comprender el flujo de datos
- [ ] Examinar la pila de llamadas para ver la secuencia de llamadas a funciones
- [x] Añadir sentencias prints en lugares clave del código para verificar los valores de las variables

Correcto Los depuradores permiten detener la ejecución y examinar el estado de las variables en cualquier punto, lo que ayuda a comprender el flujo de datos.

## Mientras desarrolla un programa Python, se encuentra con un ZeroDivisionError. ¿Cuál es la forma más eficaz de evitar que este error bloquee tu programa y permitir que continúe su ejecución? Seleccione la mejor respuesta.

- [x] Utiliza un bloque try-except para atrapar el ZeroDivisionError y manejarlo con elegancia.
- [ ] Ignora el error y espera que no vuelva a ocurrir.
- [ ] Utiliza una sentencia condicional para comprobar si el divisor es cero antes de realizar la división.
- [ ] Reescriba el código para evitar cualquier posibilidad de división por cero, incluso si esto hace que el código sea menos eficiente.

Correcto: los bloques try-except permiten gestionar excepciones y evitar que el programa se bloquee.


## Un programador está desarrollando un juego en el que el inventario del jugador puede contener diversos objetos como armas, pociones y llaves. ¿Qué atributo de las listas en Python soportaría mejor el almacenamiento de estos diferentes tipos de objetos en el inventario? Selecciona la mejor respuesta.

- [ ] Orden
- [x] Versatilidad
- [ ] Indexación
- [ ] Mutabilidad

Correcto La versatilidad permite que la lista contenga una mezcla de tipos de datos, que representan los distintos tipos de objetos del inventario del jugador.

## Una aplicación de redes sociales necesita almacenar las publicaciones de los usuarios, que pueden incluir texto, imágenes y vídeos. ¿Qué características de las listas en Python las hacen adecuadas para gestionar esta diversidad de contenidos? Selecciona la mejor respuesta.

- [ ] ORDER BY
- [ ] Añadiendo
- [ ] Mutabilidad
- [x] Versatilidad

Correcto Las listas pueden alojar los distintos tipos de datos necesarios para almacenar diversos formatos de entrada (texto, imágenes, vídeos).

## Una aplicación de gestión de tareas utiliza listas para almacenar las tareas de los usuarios. ¿Qué características de las listas en Python contribuyen directamente a la capacidad de almacenar diferentes tipos de información sobre cada tarea, como el título de la tarea, la fecha de vencimiento y la prioridad, dentro de la misma lista? Seleccione todas las que correspondan.

- [ ] Orden

Correcto El orden asegura que las tareas se muestren en la secuencia en que fueron añadidas o priorizadas.

- [x] Mutabilidad

Correcto Las listas pueden alojar los distintos tipos de datos necesarios para almacenar diversos formatos de entrada (texto, imágenes, vídeos).

- [x] Versatilidad

Correcto La versatilidad permite almacenar distintos atributos de las tareas, como el título, la fecha de vencimiento y la prioridad.

- [ ] Indexación


## Un Analista de datos tiene una lista de cifras de ventas del último año, pero necesita analizar las tendencias específicamente del último trimestre. ¿Qué técnica extraería eficazmente este subconjunto de datos? Seleccione la mejor respuesta.

- [ ] pop()
- [x] Rebanar
- [ ] insert()
- [ ] Comprensión de la lista

Correcto La segmentación permite extraer una parte específica de la lista, como las cifras de ventas del último trimestre.

## ¿Qué técnicas de manipulación de listas son especialmente útiles para tareas de limpieza de datos, como la eliminación de incoherencias o valores no deseados de un conjunto de datos? Seleccione todas las que procedan.

- [ ] sort()
- [x] Comprensión de la lista

Correcto Las comprensiones de listas pueden filtrar elementos y aplicar transformaciones para crear una versión depurada de la lista.

- [ ] Rebanar

Correcto La función remove() puede utilizarse para eliminar valores específicos no deseados de la lista.

- [ ] remove()

