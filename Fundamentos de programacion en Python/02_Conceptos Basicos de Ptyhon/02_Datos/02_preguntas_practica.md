# Examen de oractica

## Estás trabajando en un proyecto de Python en el que necesitas almacenar y manipular una colección de puntuaciones de un juego. Has decidido utilizar una lista para almacenar estas puntuaciones. ¿Cuál de las siguientes afirmaciones describe correctamente las listas y sus operaciones en Python? Selecciona todas las que correspondan.

- [ ] El método append() añade un elemento al principio de la lista, mientras que el método remove() elimina el último elemento.
- [ ] Se produce un error en ValueError cuando se intenta acceder a un elemento utilizando un índice no válido, como un número negativo o un índice superior a la longitud de la lista.
- [x] Las listas son esenciales en Python para organizar datos, permitiendo realizar operaciones como ordenar, buscar e iterar a través de elementos.

Correcto Las listas proporcionan una estructura flexible para la organización y manipulación de datos, permitiendo diversas operaciones para un manejo eficiente de los datos.

- [x] Una lista es una colección ordenada y mutable de elementos, que permite almacenar diferentes tipos de datos dentro de la misma lista y modificar sus elementos después de la creación.

Correcto Las listas son ordenadas, lo que significa que los elementos mantienen su orden de inserción, y mutables, lo que permite modificaciones. También pueden contener tipos de datos mixtos.


## Estás desarrollando un programa para simular la cola de clientes de un restaurante popular. Necesitas almacenar los nombres de los clientes en el orden en que llegan. ¿Qué característica clave de las listas de Python las hace adecuadas para esta tarea? Selecciona la mejor respuesta.

- [ ] Versatilidad, ya que puede almacenar en la lista varios tipos de datos, como nombres y horas de llegada.
- [x] Orden, ya que garantiza que se pueda acceder y atender a los clientes en el orden en que fueron añadidos a la lista.
- [ ] Mutabilidad, ya que puede añadir y eliminar clientes de la cola a medida que llegan y se van.
- [ ] La posibilidad de añadir elementos, ya que permite añadir nuevos clientes a la cola.

Correcto Las listas conservan el orden de los elementos, lo que es crucial para gestionar una cola por orden de llegada.

## Una empresa de Redes sociales necesita almacenar varios tipos de datos para cada perfil de usuario, incluyendo su nombre de usuario (texto), edad (número), una lista de sus amigos (otra lista), y si están actualmente en línea (booleano). ¿Qué característica de las listas de Python las hace adecuadas para gestionar esta información tan diversa sobre los usuarios? Selecciona la mejor respuesta.

- [ ] Orden, ya que garantiza que los datos del usuario se almacenan en una secuencia predecible.
- [ ] Mutabilidad, ya que permite actualizar el perfil si el usuario cambia de edad o añade un amigo.
- [x] Versatilidad, ya que permite almacenar distintos tipos de datos dentro de una misma lista.
- [ ] Indexación, ya que permite acceder a información específica del perfil, como la edad del usuario.

Correcto Las listas pueden alojar varios tipos de datos, lo que resulta esencial para almacenar la diversa información de un perfil de usuario.

## Está trabajando con un conjunto de datos de opiniones de clientes, en el que cada entrada contiene una cadena de texto. Necesita limpiar estos datos eliminando los espacios sobrantes y convirtiendo todo el texto a minúsculas para que el análisis sea coherente. ¿Qué técnica de manipulación de listas sería la más adecuada? Seleccione la mejor respuesta.

- [x] Comprensión de listas: Crear una nueva lista con cadenas de texto depuradas, aplicando las transformaciones necesarias a cada elemento.
- [ ] sort() método: Ordene las entradas de comentarios alfabéticamente para identificar incoherencias en el uso de mayúsculas.
- [ ] index() método: Buscar la posición de las entradas con espacios de más o mayúsculas incoherentes para su posterior tratamiento.
- [ ] pop() método: Elimine las entradas con espacios de más o mayúsculas incoherentes.

Correcto Las comprensiones de listas permiten crear de forma eficiente una nueva lista aplicando a cada elemento de la lista original operaciones como la eliminación de los espacios sobrantes y la conversión a minúsculas.


## Un Analista de datos necesita procesar un gran conjunto de datos de reseñas de productos. Muchas de ellas contienen información irrelevante, como caracteres especiales y etiquetas HTML. ¿Qué concepto de Python sería más útil para automatizar la tarea de limpiar estas reseñas y extraer sólo la información textual esencial? Selecciona la mejor respuesta.

- [ ] Métodos de lista incorporados como append() y insert(): Añade reseñas depuradas a una nueva lista
- [ ] Indexación: Acceda a caracteres específicos dentro de cada reseña para identificar y eliminar información irrelevante
- [ ] Rebanar: Extraer partes de las reseñas que contengan comentarios relevantes
- [x] Comprensiones de lista combinadas con métodos de cadena: Iterar por las revisiones, eliminar los caracteres no deseados y crear una nueva lista con el texto depurado

Correcto Este enfoque combina la eficacia de las comprensiones de listas para iterar y filtrar con la potencia de los métodos de cadenas para manipular el texto dentro de cada revisión.
