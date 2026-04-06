# Examen de funciones en Python


## Imagina que estás creando un programa para gestionar la colección de libros de una biblioteca. Decides crear una función llamada add_book. ¿Qué información sería esencial incluir como argumentos para que esta función funcione eficazmente? Seleccione todo lo que corresponda.

- [x] Año de publicación del libro

El año de publicación ayuda a distinguir las distintas ediciones y proporciona contexto.

- [ ] La fecha y hora actuales
- [x] El título del libro

El título es un dato fundamental para identificar un libro.

- [x] El autor del libro

Correcto El autor es crucial para catalogar y buscar el libro.

## Estás desarrollando un juego en el que los jugadores ganan puntos por completar diferentes tareas. Tienes una función llamada calculate_bonus_points que toma la puntuación actual del jugador como argumento y calcula puntos de bonificación adicionales basados en ciertas condiciones. WHERE debe almacenar la puntuación total acumulada del jugador para garantizar que se puede acceder y actualizar tanto dentro como fuera de la función calculate_bonus_points y otras funciones del juego? Seleccione la mejor respuesta.

- [x] Como variable global.
- [ ] Como variable local dentro de la función calculate_bonus_points.
- [ ] Como valor de retorno de la función calculate_bonus_points.
- [ ] Como argumento de la función calculate_bonus_points.

Correcto El almacenamiento de la puntuación total del jugador como una variable global permite que sea accesible y modificada por cualquier función en su juego, incluyendo calculate_bonus_points. Esto asegura que la puntuación se mantiene constante a lo largo de todo el juego.

## Estás trabajando en un programa Python que calcula el coste total de los artículos de un carrito de la compra. Tienes una función llamada calculate_total_cost que toma los precios de los artículos como una lista y aplica un descuento si es aplicable. También tienes una variable global llamada SALES_TAX_RATE que almacena la tasa actual del impuesto sobre las ventas. Dado que la variable SALES_TAX_RATE ya está declarada globalmente, ¿cómo debería accederse a ella en la función calculate_total_cost? Seleccione la mejor respuesta.

- [ ] Declare SALES_TAX_RATE dentro de la función calculate_total_cost y acceda a ella directamente.  
- [ ] Declare SALES_TAX_RATE como argumento de la función calculate_total_cost y acceda a él como parámetro.
- [x] Acceda a SALES_TAX_RATE directamente desde calculate_total_cost. 
- [ ] Declare SALES_TAX_RATE dentro de la función calculate_total_cost y acceda a ella utilizando la palabra clave global.

Correcto Declarar SALES_TAX_RATE fuera de cualquier función la convierte en una variable global, accesible en todo el programa, incluso dentro de la función calculate_total_cost.

## Estás diseñando un juego de acuario virtual y decides utilizar clases para representar las distintas especies de peces. Para gestionar estas diversas especies de manera eficiente y permitir acciones comunes como alimentar a todos los peces del acuario con un solo comando, sin dejar de tener en cuenta sus comportamientos de alimentación únicos, ¿qué par de conceptos de programación orientada a objetos sería MÁS ventajoso implementar? Seleccione la mejor respuesta.

- [ ] Encapsulación y aleatorización: Ocultación de los datos internos de los objetos peces y generación de atributos aleatorios para cada instancia de pez.

- [x] Herencia y polimorfismo: Crear una clase base Fish con atributos y comportamientos comunes y, a continuación, crear clases especializadas para cada especie (por ejemplo, Clownfish, Angelfish) que hereden de Fish e implementen su lógica de alimentación específica. Esto permite tratar a todos los peces de manera uniforme para las acciones generales, respetando al mismo tiempo sus necesidades individuales.

- [ ] Abstracción y reutilización: Simplificar la representación de los peces centrándose en las características esenciales y creando múltiples instancias de diferentes especies de peces a partir de sus respectivas clases.

- [ ] Datos y métodos: Definición de las propiedades (por ejemplo, nombre, tamaño, dieta) y acciones (por ejemplo, nadar, comer) de cada especie de pez dentro de sus respectivas clases.

Correcto La herencia le permite crear tipos de peces especializados con características compartidas, mientras que el polimorfismo le permite interactuar con ellos a través de una interfaz común (por ejemplo, alimentar a todos los peces independientemente de su tipo específico), acomodando sus comportamientos únicos.

## Está analizando un gran conjunto de datos y se da cuenta de que hay bloques de código idénticos que se repiten varias veces a lo largo del script. Estos bloques de código tienen diferentes propósitos. ¿Cuál es el MEJOR enfoque que aprovecha las funciones para agilizar el código y evitar la redundancia? Seleccione la mejor respuesta.

- [ ] Copiar y pegar los mismos segmentos de código para cada tarea de análisis de datos, garantizando la coherencia.
- [ ] Combina todos los bloques de código repetidos en una única función larga, evitando la creación de cualquier otra función.
- [ ] Ignore los bloques de código repetidos y continúe, abordándolos más adelante si es necesario.
- [x] Encapsule cada bloque de código repetido en su propia función independiente y llame a esas funciones según sea necesario.

Correcto Esto promueve la modularidad, la reutilización y la mantenibilidad.

## Estás trabajando en un proyecto de equipo en el que tienes que escribir una función para validar las contraseñas de los usuarios. Las contraseñas deben cumplir ciertos criterios, como tener una longitud mínima, contener letras mayúsculas y minúsculas, e incluir al menos un dígito. Debe devolver Verdadero o Falso. ¿Cuál de las siguientes definiciones de función cumple MEJOR con las convenciones de nomenclatura recomendadas y las mejores prácticas para escribir funciones Python? Seleccione la mejor respuesta.

- [ ] def ValidatePassword(password)
- [x] def is_valid_password(password)
- [ ] def check_password_validity(password)
- [ ] def is_valid_password(pwd)

Correcto
Correcto Este nombre de función es descriptivo, sigue snake_case, utiliza un prefijo booleano para indicar que devuelve un valor Verdadero/Falso y utiliza un nombre de parámetro completo y claro.