
## ¿Cuál de las siguientes es una práctica importante a la hora de escribir manejadores de excepciones efectivos en Python? Seleccione la mejor respuesta.

- Utilice una única cláusula except para gestionar todas las excepciones.
- Plantear excepciones en bloques finally.
- **Especifique claramente el tipo de excepción que está gestionando.**
- Evite registrar excepciones para mantener el código limpio.

Buen trabajo
> Correcto Especificar el tipo de excepción ayuda a capturar sólo las excepciones que desea manejar.

## Cuáles son las prácticas que contribuyen a escribir manejadores de excepciones eficaces en Python. Selecciona todas las que correspondan.

- Utilización de cláusulas de excepción desnudas.
- **Generación de excepciones personalizadas.**

Buen trabajo
> Correcto Las excepciones personalizadas pueden proporcionar más contexto sobre el error.

- **Registro de los detalles de la excepción.**

Buen trabajo
> Correcto El registro ayuda a diagnosticar y depurar problemas.

- **Atrapar sólo excepciones específicas.**

Buen trabajo
> Correcto La captura de excepciones específicas evita la gestión de excepciones no deseadas.

## Eres mentor de un desarrollador junior de Python. Están trabajando en un script que necesita procesar datos de varios archivos. Algunos de estos archivos pueden faltar o estar corruptos. ¿Qué consejo le darías para asegurar que su script se ejecute sin problemas incluso si se encuentra con estos problemas? Selecciona la mejor respuesta.


- Envuelva siempre las operaciones con archivos, como la apertura y la lectura, dentro de un bloque try-except. De esta forma, si falta un archivo o no se puede leer, el script no se bloqueará.

- Asegúrate de incluir muchas sentencias print a lo largo del código. Esto te ayudará a seguir el progreso de tu script y a detectar cualquier error.

- Comprueba dos veces todos tus cálculos matemáticos. Los errores aritméticos pueden dar lugar a resultados inesperados.

- **Organice su código en funciones bien definidas. Así será más fácil de leer y mantener.**

Buen trabajo
> ¡Correcto! Manejo de excepciones es esencial cuando se trata de operaciones con archivos, ya que pueden surgir problemas inesperados.

## ¿Cuál de los siguientes bloques de una estructura try-except-else-finally se ejecuta independientemente de si se ha producido una excepción o no? Seleccione la mejor respuesta.

- **Finally**
- Except
- try
- else

Buen trabajo

> Correcto El bloque finally siempre se ejecuta, independientemente de si se ha lanzado o manejado una excepción.

## ¿Cuál de los siguientes ejemplos requiere manejo de excepciones? Seleccione todo lo que corresponda.

- **Conexión a una base de datos que puede estar desconectada.**

Buen trabajo
> Correcto Manejo de excepciones es crucial aquí para gestionar los posibles fallos de conexión.

- **Acceder a un diccionario con una clave que puede no existir.**

Buen trabajo
> Correcto Manejar las excepciones en este caso evita que los errores clave rompan el código.

- **Acceso a un elemento de una lista por índice.**

Buen trabajo
> Correcto Manejo de excepciones ayuda a gestionar posibles errores de índice.

- Concatenar dos cadenas.