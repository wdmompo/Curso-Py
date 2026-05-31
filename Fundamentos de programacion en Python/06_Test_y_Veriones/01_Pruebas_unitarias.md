# Resumen del Curso de Pruebas Unitarias

Este curso está diseñado para enseñarle a utilizar **pruebas unitarias** para:

- **Detectar errores tempranamente**
- **Mejorar la calidad del código**
- **Reducir el riesgo de cambios**

## Objetivos

Al finalizar, podrá:

- Explicar cómo las pruebas unitarias ayudan a identificar errores en las primeras etapas del desarrollo.
- Reconocer la importancia de las pruebas unitarias para mejorar la calidad del código.

## Analogía con Rascacielos

- **Construcción**: Así como los rascacielos son probados rigurosamente, las pruebas unitarias garantizan que cada componente del software funcione correctamente.
- Las pruebas unitarias actúan como **control de calidad** para el software.

## Pruebas Unitarias en Python

- Una prueba unitaria es un fragmento de código que evalúa una función o método específico.
- Proporciona entradas, ejecuta la función y verifica si la salida es la esperada.

## Importancia de las Pruebas Unitarias

- Detectan errores **antes de que se conviertan en problemas mayores**.
- Funcionan como un **sistema de alerta temprana** en el desarrollo de software.
- Ayudan a simplificar la reparación de errores, reduciendo costos.

## Ejemplo Práctico

- Imagine una función que calcula el costo total de un carrito de compras, considerando impuestos y descuentos. 
- Una prueba unitaria puede evaluar diferentes escenarios de artículos y códigos promocionales.


## Estás trabajando en un proyecto colaborativo de Python con una gran base de código. Varios desarrolladores están contribuyendo con nuevas características y modificando el código existente. En este escenario, ¿cuál de las siguientes opciones describe mejor la función principal de las pruebas unitarias? Seleccione la mejor respuesta.


- Garantizar que el aspecto visual de la aplicación sea estéticamente agradable y coherente
- **Actuar como red de seguridad, permitiendo a los desarrolladores refactorizar el código con confianza sin temor a romper la funcionalidad existente**
- Documentar los requisitos y especificaciones del proyecto para futuras referencias
- Generación automática de nuevas características y funcionalidades para la aplicación

Correcto
> Correcto Las pruebas unitarias verifican que los cambios en el código no introducen regresiones o efectos secundarios inesperados, lo que da a los desarrolladores la confianza necesaria para refactorizar y mejorar el código.

___

# Introducción a las Pruebas Unitarias

Presentaremos el concepto de **pruebas unitarias** y analizaremos su importancia. Al final, podrá:

- Explicar el concepto de pruebas unitarias y su propósito en el desarrollo de software.
- Comparar y contrastar pruebas unitarias con la prueba de piezas individuales de una máquina antes del ensamblaje.

## Analogía con la Construcción de Máquinas

Crear software es como construir una máquina compleja. Antes de montarlo, se prueba cada engranaje, palanca y circuito para asegurar que cada pieza funcione a la perfección. Las pruebas unitarias en Python funcionan de manera similar, evaluando las partes más pequeñas del código, como funciones y métodos, de forma individual.

## ¿Qué Son las Pruebas Unitarias?

Las pruebas unitarias implican:

- Diseccionar el código en sus componentes más granulares (funciones o métodos).
- Crear un código dedicado para examinar rigurosamente el comportamiento de cada componente en varios escenarios de entrada.

### Importancia de las Pruebas Unitarias

Sin pruebas unitarias, un cambio en el sistema de nómina podría introducir errores imprevistos que afecten a los empleados. Las pruebas unitarias actúan como un sistema de alerta temprana, permitiendo identificar y corregir problemas antes de que afecten al entorno de producción.

## Proceso de Pruebas Unitarias

1. **Aislar Componentes**: Identificar una función o método específico en el código.
2. **Elaborar Casos de Prueba**: Cubrir diferentes escenarios, como condiciones de funcionamiento típicas y entradas no válidas.
3. **Construir el Aparato de Prueba**: Usar un marco de pruebas de Python para invocar funciones y verificar resultados.

### Ejecución de Pruebas

- Ejecutar el conjunto de pruebas permite verificar el comportamiento de la función.
- Una ejecución limpia infunde confianza; una prueba fallida señala una posible falla de diseño.

## Proactividad y Control de Calidad

Las pruebas unitarias permiten explorar cómo su código maneja diversos escenarios y establecen una red de seguridad para mejorar el código sin temor a consecuencias imprevistas. 

## Conclusión

Las pruebas unitarias son fundamentales para asegurar la fiabilidad del código. Proporcionan confianza para realizar cambios y mejoran la estabilidad del sistema. Al adoptar las pruebas unitarias en su proceso de desarrollo, creará software sólido y confiable que resiste el paso del tiempo.


## Se te ha encargado optimizar una función compleja de Python que realiza cálculos computacionalmente intensivos. Quieres asegurarte de que tus optimizaciones no introducen inadvertidamente errores o regresiones. ¿Cuál de los siguientes enfoques sería el MÁS beneficioso en este escenario? Seleccione la mejor respuesta.

- Implemente sentencias de impresión dentro de la función para realizar un seguimiento de los valores intermedios y asegurarse de que se ajustan a sus expectativas.
- **Escribir pruebas unitarias completas para la función antes y después de la optimización, comparando los resultados para garantizar la precisión e identificar cualquier regresión.**
- Confiar únicamente en las pruebas manuales y la inspección visual del código para verificar su corrección tras la optimización.
- Confíe en los comentarios de los usuarios después de desplegar la función optimizada en producción para identificar posibles problemas.

Correcto
> Correcto Las pruebas unitarias proporcionan una red de seguridad para la refactorización. Permiten comparar la salida de las funciones originales y optimizadas para garantizar que producen los mismos resultados y detectar cualquier efecto secundario no deseado.