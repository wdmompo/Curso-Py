# Sintaxis básica de Python

## Ideas principales

- La **sintaxis** es el conjunto de reglas que determinan cómo se escriben las instrucciones en Python.
- Permite organizar palabras y símbolos para que la computadora entienda lo que debe hacer.
- Los elementos fundamentales de la sintaxis de Python incluyen:
  - **Indentación**
  - **Sentencias**
  - **Variables**
  - **Comentarios**
- Comprender estos elementos es esencial para escribir programas correctos y fáciles de leer.
- Un ejemplo clásico para empezar es el programa **Hello World**, que muestra un mensaje en pantalla.

---

## ¿Qué es la sintaxis?

En programación, la **sintaxis** se refiere a las reglas que indican cómo deben organizarse las instrucciones en un lenguaje.

Así como en un idioma existen reglas gramaticales para formar oraciones correctas, en Python la sintaxis define:

- cómo escribir código
- cómo estructurar instrucciones
- cómo comunicar ideas a la computadora.

Gracias a la sintaxis, las ideas del programador se convierten en **acciones que la máquina puede ejecutar**.

---

## Elementos fundamentales de la sintaxis en Python

Python utiliza cuatro elementos principales para estructurar el código:

- indentación
- sentencias
- variables
- comentarios

---

## Indentación

La **indentación** consiste en agregar espacios al inicio de una línea de código.

En muchos lenguajes se utilizan símbolos como `{}` para definir bloques de código, pero en Python se utiliza la **indentación**.

Esto permite:

- agrupar instrucciones relacionadas
- mostrar la estructura lógica del programa
- mejorar la legibilidad del código.

Cada nivel de indentación representa un **bloque de código anidado**.

Por ejemplo:

```python
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
```

Si la indentación está mal alineada, Python generará un error.

Además de ser necesaria para el funcionamiento del programa, la indentación también ayuda a que el código sea más fácil de entender y mantener.

## Sentencias

Las sentencias son las instrucciones que se le dan a la computadora.

Una sentencia suele ser una línea de código que realiza una acción específica.

Las sentencias pueden incluir:

- asignación de valores
- cálculos
- llamadas a funciones
- estructuras de control como bucles o condicionales.

Ejemplo de sentencia:

```python
resultado = 10 + 5
```

Cada sentencia representa un paso en la ejecución del programa.

Las sentencias forman la lógica del código, permitiendo que el programa:

- realice cálculos
- manipule datos
- tome decisiones
- interactúe con el usuario.

## Variables

Las variables son contenedores que almacenan datos.

Permiten asignar un nombre a un valor, lo que facilita su uso dentro del programa.

Ejemplo:

```python
edad = 25
nombre = "Ana"
```

Las variables permiten almacenar diferentes tipos de datos, como:

- números
- texto
- listas
- otros objetos.

También pueden actualizarse durante la ejecución del programa, lo que hace que el código sea más flexible.

Las variables se utilizan para:

- guardar datos introducidos por el usuario
- almacenar resultados de cálculos
- mantener información necesaria para el programa.

## Comentarios

Los comentarios son líneas de texto que se agregan al código para explicar lo que hace.

Python ignora los comentarios durante la ejecución, por lo que solo sirven para los programadores.

En Python, los comentarios comienzan con el símbolo #.

Ejemplo:

```python
# Este programa calcula la edad del usuario
edad = 25
```

Los comentarios se utilizan para:

- explicar la lógica del código
- dejar notas o recordatorios
- documentar decisiones de diseño.

Esto mejora la legibilidad y comprensión del código, especialmente en proyectos grandes o colaborativos.


## Pregunta

### ¿Cuál de los siguientes aspectos de la sintaxis de Python contribuye MÁS directamente a mejorar la legibilidad y mantenibilidad del código?

- [x] Indentación
- [ ] Declaraciones
- [ ] Variables
- [ ] Comentarios

> Correcto El uso único de la indentación en Python estructura visualmente el código, facilitando la comprensión del flujo y las relaciones entre las diferentes partes del programa.


## Ejemplo práctico: programa Hello World

El programa Hello World es tradicionalmente el primer programa que se escribe al aprender un lenguaje.

Su objetivo es mostrar un mensaje simple en pantalla.

- Paso 1: Crear un archivo
  - Crear un archivo nuevo con la extensión .py.
  - Por ejemplo:
    - hello.py
- Paso 2: Escribir el código
  - Dentro del archivo, escribir el siguiente código:
    ```python
    print("Hello, World!")
    ```
- Paso 3: Guardar y ejecutar    
  - Guardar el archivo y ejecutarlo.
    - Se puede hacer de dos formas:
      - Desde un IDE
        - Usando el botón Run o Ejecutar.
      - Desde la termina
        ```bash
        python hello.py
        ```
- Resultado
  - El programa mostrará en pantalla:
  ```textplain
  Hello, World!
  ```

Este simple programa representa el primer paso en el aprendizaje de Python.

## Conclusión

La sintaxis de Python es la base para escribir programas correctos.

Comprender elementos como:

- indentación
- sentencias
- variables
- comentarios

permite crear código claro, organizado y funcional.

Con práctica constante y experimentación, estos conceptos se convierten en herramientas esenciales para desarrollar programas más complejos.

La mejor forma de aprender es escribir código, probarlo y seguir practicando.


# Variables en Python

## Ideas principales

- Las **variables** son contenedores que almacenan datos dentro de un programa.
- Permiten asignar **nombres significativos a la información**, lo que facilita trabajar con ella.
- Sus principales ventajas son:
  - **legibilidad**
  - **reutilización**
  - **flexibilidad**
- En Python, una variable se crea **asignando un valor mediante el signo igual (`=`)**.
- Las variables también pueden **actualizarse o reasignarse** durante la ejecución del programa.

---

# ¿Qué es una variable?

Una **variable** es un contenedor de almacenamiento dentro del código que permite guardar datos para utilizarlos posteriormente.

Se pueden imaginar como **notas adhesivas digitales** que contienen información importante y que pueden consultarse o modificarse durante la ejecución del programa.

Por ejemplo, una variable puede almacenar:

- un nombre
- una temperatura
- una puntuación en un juego
- el precio de un producto.

---

# Beneficios de usar variables

## Legibilidad

Las variables hacen que el código sea **más fácil de entender**.

En lugar de usar valores difíciles de interpretar, se pueden utilizar nombres descriptivos.

Ejemplo:

```python id="x9r2tb"
ingresos_totales = 5000
```

Este nombre describe claramente lo que representa el valor.

Esto es mucho más comprensible que usar simplemente un número sin contexto.

Reutilización

Una vez que un valor se guarda en una variable, se puede usar varias veces en el programa.

Esto evita repetir el mismo valor constantemente.

Ejemplo:

tarifa_por_hora = 20
horas_trabajadas = 8
salario = tarifa_por_hora * horas_trabajadas

Si la tarifa cambia, solo es necesario modificar el valor en un lugar.

## Flexibilidad

Las variables permiten que el código se adapte a situaciones cambiantes.

Por ejemplo, si una aplicación muestra la temperatura actual:

```python 
temperatura = 22
```

Cuando la temperatura cambia, el valor de la variable puede actualizarse.

Esto permite que el programa muestre siempre la información más reciente.

---

# Cómo crear una variable en Python

Crear una variable es muy sencillo.

Solo hay que:

escribir el nombre de la variable

usar el signo `=`

asignar un valor.

### Ejemplo:

```
nombre_empleado = "Alice"
``` 
En este caso:

nombre_empleado es el nombre de la variable

"Alice" es el valor almacenado.

Asignación de variables

La asignación ocurre cuando se guarda un valor dentro de una variable.

Ejemplo:

```python
edad = 30
``` 

El valor 30 se almacena en la variable edad.

## Reasignación de variables

Las variables pueden cambiar de valor durante la ejecución del programa.

Esto se llama reasignación.

Ejemplo:

```python
puntuacion = 10
puntuacion = 20
```


La variable puntuacion primero tiene el valor 10, pero luego se actualiza a 20.

Esto es útil cuando los datos cambian, como:

- la puntuación de un jugador
- el saldo de una cuenta
- la temperatura actual.

## Importancia de los nombres de variables

Usar nombres claros y descriptivos es fundamental.

Esto facilita:

- comprender el código
- trabajar en equipo
- mantener proyectos grandes.

Ejemplo de buen nombre:

precio_total_compra = 120

Ejemplos de uso de variables en el mundo real

Comercio electrónico

Las variables pueden almacenar información como:

- nombre del cliente
- dirección de envío
- productos seleccionados
- costo total.

Esto permite generar automáticamente:

- confirmaciones de pedidos
- etiquetas de envío
- recomendaciones personalizadas.

Análisis de datos

Las variables ayudan a organizar información como:

- comportamiento de los clientes
- tendencias del mercado
- mediciones científicas.

Esto facilita:

- calcular métricas
- detectar patrones
- crear visualizaciones.

Automatización en empresas

Los scripts de Python pueden automatizar tareas repetitivas.

Las variables pueden almacenar datos como:

- fecha actual
- estado del sistema
- preferencias del usuario.

Esto permite crear programas más adaptables y reutilizables.

## Conclusión

Las variables son una herramienta esencial en Python.

Permiten:

- almacenar datos
- reutilizar información
- adaptar el código a diferentes situaciones.

Aprender a usar variables correctamente ayuda a escribir programas más claros, flexibles y fáciles de mantener.

Como en cualquier habilidad de programación, la práctica constante es la clave para dominar su uso.

