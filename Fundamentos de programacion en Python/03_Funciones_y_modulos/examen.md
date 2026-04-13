# Examen Modulu 3

## Está trabajando en un programa que requiere una función para procesar los datos de los clientes. Esta función necesita tomar la información del cliente como entrada y devolver su estado de fidelidad y cualquier descuento aplicable. ¿Cuál de los siguientes enfoques es válido para diseñar esta función en Python? Seleccione todas las que correspondan.

- [x] Asigne la función a una variable denominada process_customer para facilitar su uso.

Correcto
Correcto Las funciones son objetos de primera clase en Python y pueden asignarse a variables.

- [ ] Incluya una sentencia print en la función para mostrar el estado de fidelización del cliente.

- [x] Devuelve tanto el estado de fidelización como el importe del descuento como valores separados.

Correcto
¡Correcto! Las funciones de Python pueden devolver múltiples valores.

- [x] Defina una función independiente dentro de la función principal para gestionar los cálculos de descuento.

Correcto
Correcto Las funciones pueden anidarse para crear código modular y organizado.

## Un desarrollador de software recibe el encargo de crear un programa para gestionar el inventario de una biblioteca. Decide utilizar clases para representar los distintos elementos de la biblioteca. ¿Cuál de los siguientes sería el uso más adecuado de una clase en este escenario? Seleccione la mejor respuesta.

- [x] Definir una clase "Libro" con atributos como título, autor e ISBN, y métodos como "tomar prestado" y "devolver"
- [ ] Definición de una clase para mostrar el logotipo de la biblioteca.
- [ ] Creación de una clase para almacenar los horarios de apertura de la biblioteca.
- [ ] Utilizar una clase para generar una lista aleatoria de títulos de libros.

Correcto
Correcto Esto refleja con exactitud cómo pueden utilizarse las clases para representar objetos del mundo real y sus acciones asociadas.

## Está desarrollando un programa para procesar grandes archivos de texto que contienen reseñas de clientes. Necesita realizar varias operaciones en cada reseña, como eliminar puntuación, convertir a minúsculas e identificar palabras clave. ¿Cuál de las siguientes opciones demuestra mejor las ventajas de utilizar funciones en este caso? Seleccione todas las que correspondan.

- [x] Depuración más sencilla al aislar los posibles problemas dentro de funciones específicas.

Correcto
Correcto Las funciones facilitan la localización y corrección de errores al aislar segmentos de código.

- [ ] Mayor velocidad de ejecución al evitar la sobrecarga de las llamadas a funciones.
- [x] Mejora de la legibilidad del código al dividir el procesamiento complejo en funciones más pequeñas y con nombre.

Correcto
Correcto Las funciones mejoran la legibilidad organizando el código en unidades lógicas.

- [x] Reducción de la duplicación de código encapsulando en funciones operaciones reutilizables como "eliminar puntuación".

Correcto
Correcto Esto se alinea con el principio DRY y promueve la mantenibilidad.

## Un programador está desarrollando un juego en el que los jugadores pueden ganar puntos por completar diferentes tareas. Quiere crear una función que calcule los puntos de bonificación basándose en la puntuación actual del jugador y en el nivel de dificultad de la tarea. ¿Cuál de las siguientes opciones representa mejor los argumentos y el valor de retorno de esta función? Selecciona la mejor respuesta.

- [ ] Argumentos: puntos de bonificación; Valor de retorno: puntuación del jugador, nivel de dificultad.
- [ ] Argumentos: nombre del jugador, nombre de la tarea; Valor de retorno: puntos totales.
- [x] Argumentos: puntuación del jugador, nivel de dificultad; Valor de retorno: puntos de bonificación.
- [ ] Argumentos: ninguno; Valor de retorno: un número aleatorio de puntos de bonificación.

Correcto
Correcto Esto identifica con precisión las entradas (puntuación, dificultad) y la salida (puntos de bonificación) de la función.

## Un equipo de desarrollo está trabajando en un proyecto con una gran base de código. Quieren asegurarse de que sus funciones son fácilmente comprensibles y mantenibles. ¿Cuál de las siguientes convenciones de nomenclatura sería la más adecuada para una función que comprueba si un usuario está autorizado a acceder a un recurso específico? Seleccione la mejor respuesta.

- [ ] checkUserAccess
- [x] is_authorized_to_access
- [ ] auth
- [ ] isUserAuthorizedToAccess

Correcto
Correcto Este nombre indica claramente el propósito de la función y sigue la convención recomendada snake_case.

## Un equipo de desarrollo de software está creando una aplicación de streaming de música. Deciden utilizar un enfoque funcional para estructurar su código. ¿Cuál de los siguientes beneficios es más probable que experimenten al adoptar esta estrategia? Seleccione la mejor respuesta.

- [ ] Menor reutilización del código y mayor redundancia
- [ ] Mayor complejidad del código y menor legibilidad
- [x] Mayor capacidad para gestionar errores y excepciones
- [ ] Menor flexibilidad y adaptabilidad a las necesidades cambiantes

Correcto
Correcto Las funciones pueden mejorar la gestión de errores aislando posibles problemas y facilitando su depuración.

## Está creando una función para enviar correos electrónicos. La dirección de correo electrónico del destinatario es obligatoria, pero el asunto y el cuerpo del correo electrónico tienen valores por defecto. ¿Cuál de las siguientes opciones demuestra el uso correcto de valores predeterminados y parámetros obligatorios en este caso? Seleccione la mejor respuesta.

- [x] def send_email(recipient, subject="Important Notice", body="This is a test email"):
- [ ] def send_email(subject, body, recipient="user@example.com"):
- [ ] def send_email(subject="Important Notice", body="This is a test email", recipient):
- [ ] def send_email(recipient, subject, body):

Correcto
Correcto Esto define correctamente el destinatario como un parámetro obligatorio y proporciona valores predeterminados para el asunto y el cuerpo.

## Un desarrollador está creando una aplicación web utilizando el framework Flask y necesita incorporar librerías adicionales para gestionar las interacciones con la base de datos y la autenticación de usuarios. Quiere garantizar un proceso de instalación eficiente y sin problemas para estas bibliotecas. ¿Qué herramienta sería la más adecuada? Seleccione la mejor respuesta.

- [ ] Escribir un script personalizado para automatizar la descarga e instalación de las librerías
- [ ] Utilización de Conda para crear un entorno e instalar las bibliotecas necesarias
- [ ] Descarga y configuración manual de cada biblioteca desde su fuente respectiva
- [x] Utilizando pip para instalar las librerías necesarias desde el Python Package Index (PyPI)

Correcto
¡Correcto! Pip es la herramienta recomendada para instalar bibliotecas Python y sus dependencias de forma eficiente.

## Un desarrollador está trabajando en un juego que requiere la generación de números aleatorios para varias mecánicas de juego, como la aparición de enemigos y la caída de objetos. Quiere asegurarse de que su código permanece organizado y eficiente. ¿Cuál es la forma más eficaz de conseguirlo utilizando módulos integrados? Selecciona la mejor respuesta.

- [ ] Importe sólo la función específica de generación de números aleatorios que necesite utilizando from random import randint.
- [c] Importe el módulo random completo y utilice sus funciones con el prefijo random..
- [ ] Define funciones personalizadas para la generación de números aleatorios dentro del script principal del juego. 
- [ ] Copia y pega el código de generación de números aleatorios necesario de una fuente en línea en el script del juego.

Correcto
Correcto Importar el módulo completo permite acceder a todas sus funciones y mantener el código organizado.

## Un programador está desarrollando un módulo para cálculos científicos. Quiere incluir funciones para realizar operaciones como la multiplicación de matrices, encontrar valores propios y resolver ecuaciones lineales. ¿Cuáles de los siguientes son componentes válidos para incluir en este módulo? Seleccione todos los que correspondan.

- [ ] Código ejecutable directamente dentro del módulo que realiza tareas no relacionadas, como enviar correos electrónicos o leer archivos.
- [x] Comentarios que explican el propósito y la lógica del código.

Correcto
Correcto Los comentarios mejoran la legibilidad y la comprensión del código.

- [x] Declaraciones de importación para las bibliotecas necesarias como NumPy o SciPy.

Correcto
Correcto Los módulos pueden importar otros módulos o bibliotecas para utilizar sus funcionalidades. 

- [x] Funciones con nombres y docstrings claros, como matrix_multiply(), find_eigenvalues(), y solve_linear_equations().

Correcto
Correcto Las funciones son componentes esenciales de los módulos y deben tener nombres descriptivos y docstrings.