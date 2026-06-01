

## Estás empezando un nuevo proyecto Python y quieres asegurarte de que tus pruebas están bien organizadas desde el principio. ¿Cuál de las siguientes prácticas te ayudará a lograr este objetivo? Selecciona todas las que correspondan.


- Incluya las dependencias relacionadas con las pruebas en su archivo de requisitos principal. 
- **Coloque sus archivos de prueba en un directorio separado dedicado a las pruebas.**

Buen trabajo
> Correcto Esto ayuda a mantener el proyecto organizado y facilita la localización de las pruebas. 

- Guarde los archivos de prueba en el mismo directorio que el código de implementación. 
- **Nombra tus archivos de prueba con el prefijo test_.**

Buen trabajo
> Correcto Esta convención de nomenclatura permite a los ejecutores de pruebas identificar y ejecutar fácilmente sus pruebas. 

## ¿Cuál es la forma recomendada de nombrar los archivos de prueba al organizar el directorio de pruebas? Seleccione la mejor respuesta.

- Los archivos de prueba deben llevar el nombre del desarrollador que escribió las pruebas. 
- Los archivos de prueba deben nombrarse con el sufijo *_test. 
- Los archivos de prueba pueden tener nombres arbitrarios siempre que estén en el mismo directorio. 
- **Los archivos de prueba deben nombrarse con un prefijo test_ seguido del nombre de la función o módulo que se está probando.**

Buen trabajo
> Correcto Nombrar los archivos de prueba con un prefijo test_ facilita su identificación y ejecución con los ejecutores de pruebas. 

## Estás escribiendo pruebas unitarias para una función de Python llamada calcular_suma que toma dos números como entrada y devuelve su suma. Quieres verificar que la llamada a calcular_suma(4, 6) produce correctamente la salida 10. ¿Cuál de las siguientes sentencias de Python lo conseguiría? Seleccione la mejor respuesta.


- assert calcula_suma(4, 6) != 10 
- assert calcular_suma(4, 6) es igual a 10 
- assert calcular_suma(4, 6) = 10 
- **assert calcular_suma(4, 6) == 10**

Buen trabajo
> Correcto Esta sentencia comprueba correctamente si la función calcular_suma devuelve 10 cuando se le dan las entradas 4 y 6. 

## Cuando se utilizan fixtures en un conjunto de pruebas, ¿cuál es la principal ventaja de utilizar el parámetro scope? Seleccione la mejor respuesta.

- Especifica los ajustes de configuración de la prueba para el fixture. 
- Determina el tipo de marco de pruebas que se utilizará. 
- Define el orden en que deben ejecutarse las pruebas. 
- **Controla el ciclo de vida del accesorio y puede hacer que las pruebas sean más eficaces.**

Buen trabajo
> Correcto El uso del parámetro de alcance ayuda a gestionar el ciclo de vida del fixture, lo que puede optimizar el rendimiento de la prueba. 

## En el contexto de la parametrización de pruebas en Python, ¿cuáles de las siguientes son razones válidas para utilizar la parametrización de pruebas? Seleccione todas las que correspondan.


- **Para ejecutar la misma prueba con varios conjuntos de entradas de datos.**

Buen trabajo
> Correcto La parametrización de pruebas permite ejecutar la misma lógica de prueba con diferentes conjuntos de datos. 

- Para garantizar que las pruebas se ejecutan en una secuencia específica. 
- **Para reducir la necesidad de complejos guiones de prueba.**

Buen trabajo
> Correcto Parametrizar las pruebas simplifica los scripts al eliminar la necesidad de múltiples casos de prueba similares. 

- Hacer que las pruebas dependan unas de otras. 