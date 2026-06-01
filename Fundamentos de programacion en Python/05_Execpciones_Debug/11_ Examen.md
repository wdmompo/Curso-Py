
## ¿Cuál de las siguientes técnicas te permite mostrar el valor de las variables en puntos específicos durante la ejecución de tu programa Python? Selecciona la mejor respuesta.

- Depurador interactivo
- Registro 
- Afirmaciones
- **Imprimir declaraciones**

## ¿Cuáles de las siguientes son características o capacidades típicamente asociadas con depuradores interactivos en Python? Seleccione todas las que correspondan.


- **La capacidad de inspeccionar los valores de las variables y la pila de llamadas en cualquier punto dado durante la ejecución.**

Buen trabajo
> Correcto Los depuradores interactivos proporcionan información sobre el estado actual del programa, incluidos los valores de las variables y la secuencia de llamadas a funciones que conducen al punto actual.

- **La posibilidad de establecer puntos de interrupción en el código para detener la ejecución en líneas específicas.**

Buen trabajo
> Correcto Los puntos de interrupción le permiten detener la ejecución del programa en determinados puntos, lo que le da la oportunidad de inspeccionar su estado.

- La posibilidad de corregir automáticamente errores en el código sin intervención manual.
- **La posibilidad de recorrer el código línea por línea, observando cómo cambian los valores de las variables.**

Buen trabajo
> Correcto Esta función permite una comprensión granular de cómo se ejecuta el código y cómo fluyen los datos a través de él.

## Estás trabajando en un gran proyecto Python y quieres seguir la secuencia de eventos mientras se ejecuta tu programa, incluyendo llamadas a funciones, asignaciones de variables y errores potenciales. También necesitas la capacidad de filtrar y analizar esta información más tarde, incluso después de que el programa haya terminado de ejecutarse. ¿Qué técnica de depuración se ajusta mejor a estos requisitos? Seleccione la mejor respuesta.

- Afirmaciones
- **Registro**
- Depurador interactivo
- Imprimir declaraciones

Buen trabajo
> Correcto El registro proporciona una forma estructurada de registrar eventos, errores y otra información durante la ejecución del programa, permitiendo su posterior análisis y filtrado.

## ¿Qué técnica básica de depuración consiste en desactivar temporalmente secciones del código para aislar las áreas problemáticas? Seleccione la mejor respuesta. 

- Imprimir declaraciones
- **Comentarios de código**
- Pruebas unitarias
- Depuración del patito de goma

Buen trabajo
> Correcto Comentar el código permite eliminar sistemáticamente partes del programa para localizar el origen de un error.

## Estás desarrollando un script en Python que procesa datos de ficheros externos. Quieres asegurarte de que si un archivo falta o está corrupto, tu programa no se bloquee, sino que informe al usuario del problema. ¿Cómo puede ayudarte a conseguirlo el Manejo de excepciones? Selecciona la mejor respuesta.

- Evitando que se produzcan errores relacionados con los archivos.
- **Permitiéndole capturar excepciones relacionadas con archivos y proporcionar mensajes de error informativos al usuario.**
- Corrigiendo automáticamente cualquier error en los archivos externos.
- Acelerando el tratamiento de los datos de los ficheros.

Buen trabajo
> ¡Correcto! El manejo de excepciones le permite anticipar y manejar con elegancia situaciones en las que los archivos pueden faltar o estar dañados, evitando fallos y mejorando la experiencia del usuario.

## Estás escribiendo una función de Python que espera una lista como argumento. Sin embargo, cuando llamas a la función con una cadena en su lugar, obtienes un error. ¿Qué excepción es la más probable responsable de este error? Selecciona la mejor respuesta.

- ValueError
- **TypeError**
- Error de índice
- ErrorNombre

Buen trabajo
> Correcto: TypeError aparece cuando se intenta realizar una operación en un objeto de tipo incompatible, como pasar una cadena a una función que espera una lista.

## Tienes un programa Python que procesa entradas de usuario. Quieres asegurarte de que el programa no se bloquea si el usuario introduce datos no válidos, como texto en un campo numérico. ¿Qué tipos de excepción sería apropiado atrapar en este escenario? Seleccione todas las que correspondan.


- **SyntaxError**

Correcto Si la entrada del usuario conduce a un código Python inválido, puede aparecer un SyntaxError.

- TypeError
- ZeroDivisionError
- **ValueError**

Buen trabajo
> ¡Correcto! ValueError se produce normalmente cuando se intenta convertir una cadena a un número pero la cadena contiene caracteres no válidos.

## Estás trabajando en un script Python que necesita conectarse a una base de datos. Anticipas que el servidor de la base de datos podría no estar disponible temporalmente. ¿Cómo puedes utilizar el Manejo de excepciones para que tu script sea más resistente en esta situación? Selecciona la mejor respuesta.

- **Utilice un bloque try-except para detectar errores de conexión e intentar reconectarse tras un breve retardo.**
- Ignora cualquier error potencial y deja que el script se bloquee si la base de datos no está disponible.
- Lanza una excepción personalizada cada vez que se produce un error de conexión.
- Envuelve el código de conexión a la base de datos en un bloque try-except, pero no proporciones ningún tratamiento de errores específico.

Buen trabajo
Correcto Este enfoque permite a su script manejar con gracia la indisponibilidad temporal de la base de datos reintentando la conexión, mejorando su resistencia.

## ¿Cuál es el resultado del siguiente fragmento de código? Seleccione la mejor respuesta.

````python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print("An error occurred: ", e)
finally:
    print("Execution completed")
```


- **No se puede dividir por cero**
- **Ejecución finalizada**

- Se ha producido un error: división por cero 
- Ejecución finalizada

- Se ha producido un error: división por cero
- Ejecución finalizada

Buen trabajo
> Correcto El ZeroDivisionError es capturado por el bloque except específico, y el bloque finally se ejecuta siempre.

## Estás trabajando en un programa Python, e inesperadamente se bloquea con un mensaje TypeError que indica que "el objeto int no es iterable". ¿Qué indica este mensaje de error? Selecciona la mejor respuesta. 

- Está intentando utilizar una variable que no ha sido definida
- **Estás intentando iterar sobre un entero como si fuera una lista u otro tipo iterable.**
- Está intentando realizar una operación con tipos de datos incompatibles
- Estás intentando dividir un entero por cero

Buen trabajo
> Correcto Este error significa que está intentando utilizar un número entero en un contexto que espera algo que se pueda recorrer en bucle, como una lista o una cadena.