# Examen Practica

## Estás escribiendo un programa en Python para determinar si un cliente tiene derecho a un descuento en función del importe de su## compra. ¿Cuál de las siguientes sentencias de decisión sería la más adecuada para esta tarea en Python? Seleccione la mejor respuesta.

- [ ] for bucle
- [x] if-else declaración
- [ ] print declaración
- [ ] while bucle

Correcto
Correcto Una sentencia if-else permite ejecutar diferentes bloques de código en Python en función de si el importe de la compra del cliente cumple los criterios de descuento.

## Estás construyendo un juego de adivinar números en Python. El jugador tiene que adivinar un número secreto, y el programa proporciona información si el número adivinado es demasiado alto o demasiado bajo. ¿Cómo podrían ayudarte los bucles y las sentencias condicionales de Python a implementar la lógica de este juego? Selecciona la mejor respuesta.


- [x] Un bucle while podría preguntar repetidamente al jugador por su suposición utilizando input(), y una sentencia if-elif-else podría comprobar si la suposición es correcta, demasiado alta o demasiado baja.
- [ ] Un bucle for podría mostrar las instrucciones del juego, y una sentencia if podría terminar el juego.
- [ ] Un bucle for podría realizar un seguimiento de la puntuación del jugador, y una sentencia if-else podría proporcionar pistas.
- [ ] Un bucle while podría generar un número aleatorio utilizando el módulo random, y una sentencia if podría asignar puntos al jugador.

Correcto
Correcto Esto describe correctamente cómo el bucle while de Python y las sentencias if-elif-else se pueden utilizar para crear el bucle de juego principal.

## Estás creando un programa para determinar si un estudiante puede optar a una beca en función de su nota media. ¿Qué Sentencia condicional utilizarías para comprobar si el GPA del estudiante está por encima de un determinado umbral? Seleccione la mejor respuesta.

- [ ] for
- [x] if
- [ ] else
- [ ] elif


Correcto
Correcto La sentencia if es la base de la lógica condicional, ya que permite comprobar una condición específica y ejecutar código si es cierta.

## Estás creando un sencillo juego de adivinanzas en el que el jugador tiene que adivinar un número secreto. Tienen un número ilimitado de intentos, pero sólo hay un juego. Después de adivinar la respuesta correcta, el programa termina. ¿Cuál de las siguientes tareas dentro de esa única ronda requeriría repetir una acción (usando un bucle)? Seleccione todas las que correspondan.


- [x] Pedir al jugador que adivine varias veces en una misma ronda.
- [ ] Generar la respuesta correcta al inicio del juego.
- [x] Comprobar si la suposición del jugador coincide con la respuesta correcta.

Correcto
Correcto ASi el usuario tiene múltiples intentos, cada intento debe ser comparado con la respuesta correcta.

- [ ] Mostrar un mensaje indicando al usuario que ha acertado y mostrando el número de aciertos.


## Un equipo de desarrollo de software está creando una aplicación de planificación financiera. Quieren incorporar funciones que ayuden a los usuarios a realizar un seguimiento de los gastos, establecer presupuestos y recibir alertas de gastos inusuales. ¿Cuál de los siguientes aspectos de esta aplicación dependería en gran medida del uso de sentencias condicionales y bucles en Python? Seleccione todo lo que corresponda.

- [x] Envío de una notificación si el usuario supera su presupuesto preestablecido para una categoría específica

Correcto
Correcto Se trataría de una sentencia condicional para comprobar si el gasto actual en una categoría es superior al importe presupuestado.

- [x] Categorizar los gastos en diferentes tipos (por ejemplo, "Comida", "Vivienda", "Ocio")

Correcto
Correcto Sentencia condicional podría utilizarse para comprobar la descripción de un gasto y asignarlo a la categoría apropiada.

- [x] Permite a los usuarios establecer distintos límites presupuestarios para cada mes.

Correcto
Correcto Se podrían utilizar bucles para iterar a través de los meses y aplicar los límites presupuestarios correspondientes, potencialmente con sentencias condicionales para manejar ajustes o casos especiales.

- [ ] Generar un informe visual que muestre los patrones de gasto del usuario a lo largo del tiempo

## Está depurando un programa Python que calcula el precio final de un artículo después de aplicar los descuentos y el impuesto sobre las ventas. El fragmento de código es el siguiente:

```python
original_price = 100
discount_percentage = 20
sales_tax_rate = 0.08

discount_amount = original_price * (discount_percentage / 100)
discounted_price = original_price - discount_amount
sales_tax = discounted_price * sales_tax_rate
final_price = discounted_price + sales_tax

print(final_price)
```

### ¿En qué orden Python ejecutará las líneas de código para determinar el final_price? Seleccione la mejor respuesta.


- [ ] Calculará primero el discounted_price, luego el discount_amount, seguido del sales_tax, y por último el final_price.
- [ ] Calculará el discount_amount, luego el sales_tax, luego el discounted_price, y finalmente el final_price.
- [ ] Primero calculará el final_price utilizando directamente el original_price, y después calculará los demás valores para su visualización.
- [x] Calculará el discount_amount, luego el discounted_price, seguido del sales_tax, y por último el final_price.

Correcto
Correcto Python ejecuta el código línea por línea, respetando el orden de las operaciones y las dependencias entre variables.

## Un desarrollador junior está trabajando en un programa Python. Este programa no se ejecuta y muestra un error sobre una variable que no está definida. Al mirar el programa, la variable está definida. ¿Cuál de los siguientes conceptos está más probablemente relacionado con este error? Seleccione la mejor respuesta.


- [x] Ámbito de la variable: Intentar acceder a una variable fuera de su ámbito definido.
- [ ] Sombreado de nombres: Utilizar el mismo nombre de variable para diferentes propósitos dentro del programa.
- [ ] Pasar por alto excepciones: El programa no está manejando correctamente una excepción.
- [ ] Error de administración de la memoria: Se está agotando la memoria.


Correcto
Correcto Si la variable está definida pero aparece un error que indica que no está definida, se trata de un error de ámbito común.