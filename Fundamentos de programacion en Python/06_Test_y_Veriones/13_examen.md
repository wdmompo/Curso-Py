
## ¿Cuál es el objetivo principal de las pruebas unitarias en el desarrollo de software? Seleccione la mejor respuesta.


- Para generar automáticamente la documentación de su código.
- Crear interfaces atractivas y fáciles de usar.
- **Para verificar la corrección y fiabilidad de los distintos componentes de su código.**
- Para acelerar el proceso de codificación.

Buen trabajo
> Correcto Las pruebas unitarias se centran en probar las partes más pequeñas de su código para asegurarse de que funcionan como se espera, de forma parecida a como se prueban los componentes individuales de un rascacielos antes de su construcción.

## Tienes una función que calcula el área de un círculo. ¿Cuál de los siguientes es un ejemplo de aserción que podrías utilizar en una prueba unitaria para esta función? Seleccione la mejor respuesta.


- assert calcular_área(-2) produce ValueError
- assert type(calcular_área(3)) == float
- **assert calcular_área(5) == 78.53981633974483**
- assert calcular_área(0) no es None

Buen trabajo
> Correcto Esta aserción comprueba si el área calculada para un círculo de radio 5 coincide con el valor esperado.

## Has hecho algunos cambios en tu código y quieres crear una instantánea de esos cambios en tu repositorio Git. ¿Qué comando utilizarías? Selecciona la mejor respuesta.

- git add
- git push
- **git commit**
- git init

Buen trabajo
> Correcto El comando git commit crea una instantánea de tu proyecto en un punto específico en el tiempo, capturando todos los cambios que has hecho desde el commit anterior.

## Ha realizado cambios en varios archivos de su proyecto y desea incluirlos en su próxima confirmación. ¿Qué comandos utilizarías para conseguirlo? Selecciona todos los que correspondan. 

- **git add <nombre de archivo>** 

Buen trabajo
> Correcto El comando git add <nombredearchivo> se utiliza para preparar archivos específicos, preparándolos para ser incluidos en la siguiente confirmación.

- git push
- git commit
- **git add .**

> Correcto El comando git add . escenifica todos los cambios en el directorio actual y sus subdirectorios, preparándolos para ser incluidos en su próxima confirmación.

## Has borrado accidentalmente un fragmento de código crucial de tu proyecto. ¿Cómo puede ayudarte Git a recuperarte de este error? Selecciona la mejor respuesta.

- **Git le permite volver a una versión anterior de su código donde el código eliminado todavía existe.**
- Git puede restaurar automáticamente el código eliminado.
- Git no puede ayudar en esta situación, tendrás que reescribir el código borrado desde cero.
- Git puede sugerir fragmentos de código alternativos para reemplazar el código eliminado.

Buen trabajo
> Correcto Las capacidades de control de versiones de Git te permiten "viajar atrás en el tiempo" a una confirmación anterior en la que el código eliminado todavía estaba presente

# En un proyecto colaborativo de desarrollo de software, ¿cuál de las siguientes situaciones pone de manifiesto la importancia del control de versiones? Seleccione todas las que procedan. 

**Es necesario seguir el historial de cambios realizados en el código base para comprender su evolución.**

Buen trabajo
> Correcto El Control de versión mantiene un historial detallado de todos los cambios, lo que facilita el seguimiento de la evolución del código base.

- Desea automatizar el despliegue de su código en un entorno de producción.
- **Varios desarrolladores trabajan simultáneamente en distintas funciones.**

Buen trabajo
> Correcto El control de versión ayuda a gestionar y fusionar los cambios de varios desarrolladores que trabajan en paralelo.

- **Necesita volver a una versión anterior del código debido a un error o una consecuencia no deseada.**

Buen trabajo
> Correcto Control de versión le permite volver fácilmente a estados anteriores de la base de código si es necesario.

## ¿Cuál de las siguientes funciones de pytest le ayuda a comprobar si su código produce los resultados esperados? Seleccione la mejor respuesta. 

- Organización de las pruebas
- **Afirmaciones**
- Parametrización
- Accesorios

Buen trabajo
> Correcto Las aserciones se utilizan para verificar que el código se comporta como se espera.

## Tienes una función greet(nombre) que devuelve un mensaje de saludo. Quieres escribir una prueba pytest para asegurarte de que funciona correctamente. ¿Cuál de los siguientes es el Caso de prueba más apropiado? Seleccione la mejor respuesta.

- **assert greet("Alice") == "¡Hola, Alice!"**
- assert greet() == "¡Hola, mundo!"
- greet("Charlie")
- assert greet("Bob") no es None

Buen trabajo
> Correcto Este Caso de prueba comprueba si la función devuelve el saludo esperado para una entrada específica.

## Usted tiene múltiples funciones de prueba que requieren una configuración específica, tales como el establecimiento de variables de entorno o la inicialización de una biblioteca con ciertos parámetros. ¿Cuál es la mejor manera de evitar repetir este código de configuración en cada función de prueba? Seleccione la mejor respuesta.

- **Crea un fixture que realice la configuración y utilízalo en tus funciones de prueba.** 
- Utilice los marcadores de pytest para agrupar las pruebas y aplicar el código de configuración a todo el grupo. 
- Defina una clase base con el código de configuración y haga que sus clases de prueba hereden de ella. 
- Copie y pegue el código de configuración en cada función de prueba. 

Buen trabajo
> Correcto Los Fixtures permiten definir código de configuración reutilizable, promoviendo la eficiencia y la mantenibilidad.

# Está trabajando en un proyecto con un gran conjunto de pruebas y algunas de ellas tardan mucho tiempo en ejecutarse. Desea poder ejecutar rápidamente un subconjunto de pruebas durante el desarrollo para obtener información más rápidamente. ¿Cómo puede lograrlo con pytest? Seleccione la mejor respuesta.

- Comente manualmente las pruebas lentas cada vez que desee ejecutar las más rápidas. 
- Ajuste el orden de ejecución de las pruebas para que se ejecuten primero las más rápidas. 
- Cree un conjunto de pruebas separado específicamente para las pruebas más rápidas. 
- **Utilice los marcadores de pytest para identificar las pruebas lentas y utilice el indicador -m para excluirlas al ejecutar las pruebas.** 

Buen trabajo
> Correcto Los marcadores le permiten categorizar las pruebas, y la bandera -m le da el control sobre qué categorías ejecutar o excluir.