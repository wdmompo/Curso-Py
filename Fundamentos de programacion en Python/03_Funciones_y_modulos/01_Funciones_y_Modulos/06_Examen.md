# Pregunta 

## Se te encarga desarrollar un programa para calcular el área de diferentes formas geométricas. Decides utilizar funciones para esta tarea. ¿Cómo beneficia específicamente a este programa el uso de funciones? Selecciona la mejor respuesta.

- [ ] Las funciones detectarán automáticamente el tipo de forma y calcularán el área en consecuencia, eliminando la necesidad de introducir datos por parte del usuario.
- [x] Las funciones le permitirán calcular el área de varias formas sin necesidad de reescribir las fórmulas varias veces, reduciendo la duplicación de código.
- [ ] Las funciones mostrarán el área calculada en un formato fácil de usar, como una representación gráfica de la forma con su área etiquetada.
- [ ] Las funciones harán que el programa se ejecute más rápido, ya que las llamadas a funciones son intrínsecamente más rápidas que ejecutar el código directamente dentro del programa.

¡Correcto! Las funciones encapsulan la lógica de cálculo del área para cada forma, permitiéndole reutilizarlas para diferentes formas sin reescribir el código.


## Estás diseñando un juego en el que los jugadores pueden elegir diferentes personajes con habilidades únicas. ¿Cómo utilizarías las clases para representar a estos personajes? Selecciona todas las que corresponda.

-  [ ] Utiliza la clase Character para crear directamente objetos de personaje individuales con nombres y habilidades específicos.
-  [x] Implementa el polimorfismo haciendo que diferentes clases de caracteres respondan de forma única a la misma llamada de método, como use_ability().   

Correcto Esto permite a los personajes especializados heredar rasgos básicos y añadir otros únicos.

-  [x] Cree una clase genérica Character con atributos comunes como health y name, y métodos como move y attack.

Correcto Esto permite a los personajes realizar acciones a su manera, lo que añade diversidad a la jugabilidad.

-  [x] Defina clases distintas para cada tipo de carácter (por ejemplo, Warrior, Mage, Archer) que hereden de la clase Character.

Correcto Esto establece una clase base para los rasgos de carácter compartidos.


## Un equipo de desarrolladores está creando una aplicación de planificación financiera. Necesitan crear una función que calcule el interés compuesto. ¿Cuál es la mejor manera de aplicar el principio DRY y el concepto de funciones para implementar esta función? Seleccione la mejor respuesta.


- [c] Cree una única función llamada calculate_compound_interest que tome los parámetros necesarios (principal, tipo de interés, periodo de tiempo, etc.) y devuelva el interés compuesto calculado.

- [ ] Escriba un bloque de código independiente para calcular el interés compuesto para cada tipo de inversión (por ejemplo, cuentas de ahorro, bonos, acciones) dentro del flujo principal del programa.

- [ ] Copie y pegue la fórmula de cálculo del interés compuesto donde sea necesario en el código de la aplicación.

- [ ] Calcule manualmente el interés compuesto cada vez que sea necesario dentro de la aplicación.

Correcto Este enfoque se adhiere al principio DRY encapsulando la lógica de cálculo del interés compuesto en una función reutilizable.

## Usted está desarrollando un programa que requiere la interacción del usuario para recopilar información y luego utiliza esa información para realizar cálculos. ¿Qué Función integrada sería esencial para recoger la información del usuario? Seleccione la mejor respuesta.

- [ ] input()
- [ ] type()
- [ ] len()
- [ ] print()
- [x] input()

Correcto: input() es la función integrada diseñada específicamente para pedir al usuario que introduzca datos y devolver su respuesta en forma de cadena

## Un Equipo de desarrollo está trabajando en un gran proyecto de Python para analizar datos meteorológicos. Han creado varias funciones para tareas como leer datos de diferentes fuentes, limpiar y procesar los datos, realizar análisis estadísticos y visualizar los resultados. ¿Cuál es la mejor forma de organizar estas funciones mediante módulos para mejorar la estructura y la capacidad de mantenimiento del código? Selecciona la mejor respuesta.

- [ ] Evite por completo el uso de módulos, ya que añaden una complejidad innecesaria al proyecto.

- [x] Agrupe funciones relacionadas en módulos independientes en función de su funcionalidad (por ejemplo, un data_reader module, un data_processing module, etc.).

- [ ] Coloca todas las funciones en un único archivo Python de gran tamaño.

- [ ] Distribuir aleatoriamente las funciones entre varios módulos sin una organización clara. 

Correcto Este enfoque fomenta la modularidad, lo que facilita la comprensión, el mantenimiento y la reutilización del código.
