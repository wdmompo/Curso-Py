# Depuración en Python

El código Python es una secuencia de instrucciones diseñadas para ejecutarse sin problemas, pero a veces surgen errores. Aquí es donde comienza la depuración.

## ¿Qué es la Depuración?

La depuración es el proceso sistemático de identificar y corregir errores (bugs) en el código Python. Implica diseccionar el código, rastrear su ejecución paso a paso e identificar la causa raíz de un comportamiento inesperado. Esto puede incluir desde errores tipográficos hasta fallas lógicas.

### Importancia de la Depuración

La depuración es una parte crucial del desarrollo de software y no es un signo de fracaso, sino un compromiso con la creación de código fiable y de calidad. Cumple tres propósitos clave:

1. **Garantiza la Funcionalidad**: Limpia y corrige el código para asegurar que funcione como se espera.
2. **Mejora la Experiencia del Usuario**: Minimiza la frustración y confusión que pueden generar los errores.
3. **Ahorra Tiempo y Recursos**: Corregir errores durante el desarrollo es más eficiente que hacerlo después de la implementación.

## Proceso de Depuración en Seis Pasos

1. **Reproducir el Error**: Comprender la secuencia de acciones que desencadenan el problema. Esto permite observar el error de primera mano.

2. **Reunir Pruebas**: Recopilar información sobre el error, como mensajes de error y seguimientos de pila, para identificar posibles causas.

3. **Aislar la Causa**: Utilizar técnicas como:
   - **Revisión del Código**: Examinar el código cercano al error.
   - **Depuración de Impresión**: Insertar instrucciones de impresión para rastrear valores y flujo de ejecución.
   - **Depuradores**: Usar el depurador de tu IDE para revisar el código línea por línea.

4. **Hipotetizar y Probar**: Desarrollar causas hipotéticas del error y buscar maneras de probarlas. Esto puede incluir modificar el código o utilizar un depurador.

5. **Implementar una Solución**: Una vez identificada la causa, implementar una solución que puede variar desde corregir un error tipográfico hasta reestructurar el código.

6. **Probar la Solución**: Después de hacer la corrección, asegúrate de que el error se ha resuelto y que no se han introducido nuevos problemas.

## Técnicas Comunes de Depuración

- **Depuración de Rubber Duck**: Explicar el código línea por línea a un objeto inanimado, lo que ayuda a articular la lógica y detectar errores pasados por alto.
  
- **Comentando el Código**: Inhabilitar secciones del código para aislar áreas problemáticas.

- **Pruebas Unitarias**: Escribir pruebas automatizadas para detectar errores temprano y evitar regresiones.

## Conclusión

## La depuración es una habilidad esencial para los programadores de Python. Ayuda a abordar los errores con confianza, a crear código robusto y a ofrecer aplicaciones que superan las expectativas de los usuarios. Recuerda que la depuración no solo se trata de solucionar problemas, sino también de aprender y mejorar tus habilidades de programación.

- Has encontrado un error en tu programa Python que hace que se bloquee inesperadamente. ¿Cuál de los siguientes pasos deberías seguir primero para depurar el problema? Selecciona la mejor respuesta.
- Modifique inmediatamente el código en la zona donde cree que puede estar el error.
- Revise el mensaje de error y la información de rastreo proporcionada por Python para conocer la naturaleza y la ubicación del error.
- Consulte foros y comunidades en línea para ver si otros desarrolladores se han encontrado con un error similar.
- **Reproduzca el error, anotando los pasos o entradas específicos que lo desencadenan.**

Correcto
> Correcto Reproducir el error crea un entorno controlado para la investigación, lo que le permite observar su comportamiento y reunir pistas esenciales para su posterior depuración.

# La Depuración en Python Guia

Hoy exploraremos el apasionante mundo de la **depuración**, una habilidad esencial para todo programador. Tanto si eres un experto como si estás comenzando con Python, dominar las técnicas de depuración es clave para superar desafíos y liberar tu potencial.

## La Importancia de la Depuración

La depuración no es solo una habilidad técnica; es una mentalidad que te permite abordar problemas complejos con precisión y creatividad. Imagina tu código como una máquina compleja con partes interconectadas. Cuando algo falla, es un acertijo que espera ser resuelto.

### ¿Qué es la Depuración?

La depuración implica:
- Identificar, analizar y resolver problemas de manera sistemática.
- Asegurar que el código se ejecute sin problemas y eficientemente.
- Corregir errores menores, como comas mal colocadas o nombres de variables incorrectos, que pueden causar bloqueos o comportamientos inesperados.

## Proceso de Depuración en Pasos

1. **Reproducir el Error**: Comprender cómo se desencadena el problema para observarlo y recopilar pistas.

2. **Localizar el Error**: Eliminar partes del código o agregar sentencias de impresión para rastrear el flujo de ejecución.

3. **Entender los Mensajes de Error**: Analizar los mensajes de error del intérprete de Python para identificar el origen del problema.

4. **Usar un Depurador**: Esta herramienta permite revisar el código línea por línea, inspeccionar variables y establecer puntos de interrupción.

5. **Probar el Código**: Después de corregir un error, prueba el código con entradas y casos extremos para asegurarte de que no haya nuevos problemas.

6. **Llevar un Diario de Depuración**: Documentar errores y soluciones para evitar repeticiones en el futuro.

## Escenario Práctico de Depuración

Imagina que trabajas en un programa que calcula el promedio de una lista de números y te encuentras con un error de tipo persistente. 

- **Paso 1**: Ejecutas el programa y confirmas que el error no es aleatorio.
- **Paso 2**: Inserta sentencias de impresión para rastrear los valores.
- **Paso 3**: Descubres que un elemento de la lista es una cadena, no un número, lo que provoca la falta de coincidencia de tipos.
- **Paso 4**: Modificas el código para filtrar valores no numéricos antes de calcular el promedio.
- **Paso 5**: Creas pruebas unitarias para asegurar que tu solución maneje varios escenarios de entrada.

## Conclusión

La depuración es una habilidad indispensable para cualquier desarrollador de Python. No solo ayuda a corregir errores, sino que también brinda oportunidades para una comprensión más profunda del código. Cada error es una oportunidad de crecimiento y aprendizaje.

Acepta el desafío de depurar, aplica los principios discutidos y experimenta con diferentes enfoques. Con práctica y perseverancia, desarrollarás estrategias de depuración eficaces, lo que te permitirá solucionar problemas en el código más complejo con confianza.

La depuración no es solo solucionar problemas; es dominar tu oficio.

# Estrategias Habituales de Depuración Utilizadas por Desarrolladores Experimentados

La **depuración** es el arte de identificar y resolver sistemáticamente errores (o "bugs") en tu código. Es una habilidad esencial para cualquier desarrollador de Python, desde principiantes hasta profesionales experimentados. Dominar estrategias de depuración efectivas puede ahorrarte tiempo y frustración, y convertirte en un programador más eficiente y seguro.

## Técnicas de Depuración

### 1. Descifrar los Mensajes de Error

Los mensajes de error en Python son pistas valiosas para guiar tus esfuerzos de depuración. Presta atención a:

- **Tipo de error**: Clasifica el error en amplias categorías.
  - **Errores de sintaxis**: Como `SyntaxError: invalid syntax`.
  - **Errores de tiempo de ejecución**: Como `ZeroDivisionError` o `IndexError`.
  - **Errores lógicos**: El código se ejecuta, pero la salida es incorrecta.
  
- **Mensaje de error**: Proporciona una descripción específica del problema, como `NameError: name 'x' is not defined`.

- **Número de línea**: Indica la línea donde se detectó el problema.

### Ejemplo de Mensaje de Error

Para un error como `TypeError: 'str' object cannot be interpreted as an integer`, el desglose sería:

- **Tipo de error**: `TypeError`.
- **Mensaje**: Intentas usar una cadena donde se espera un número.
- **Depuración**: Revisa el código para encontrar operaciones matemáticas con cadenas.

### 2. Elegir la Herramienta Adecuada

Los desarrolladores tienen a su disposición una variedad de herramientas de depuración para diferentes escenarios:

- **Sentencias de impresión**: Actúan como "migajas de pan" que dejas en el código. Usa `print()` para mostrar valores y flujos de ejecución.

- **Depuradores**: Herramientas como `pdb` e `ipdb` permiten detener la ejecución en puntos específicos y examinar el estado interno del programa.

- **Aislamiento**: Si el código es grande, comenta secciones para ver si el error persiste, reduciendo gradualmente el alcance hasta aislar el problema.

### 3. Cuestionar las Suposiciones

Revisa tus suposiciones sobre el funcionamiento del código y las bibliotecas externas. Verifica tu lógica y consulta la documentación.

### 4. Documentación y Comunidades en Línea

La documentación oficial de Python es un recurso invaluable. Los foros en línea como GitHub pueden ser útiles para buscar errores específicos o pedir ayuda.

## Ejemplo Práctico de Depuración

Imaginemos una función que no se comporta como se esperaba:

```python
def calculate_discount(price, percentage):
    if percentage < 0 or percentage > 100:
        return "Invalid discount percentage"  # Comportamiento incorrecto
    discount_amount = price * (percentage / 100)
    return price - discount_amount

print(calculate_discount(100, 150))  # Debería ser un error
```

## Problema Identificado

La función devuelve incorrectamente una cadena en lugar de lanzar una excepción. La solución es modificar el código para lanzar una ValueError.
Solución Mejorada

```python
def calculate_discount(price, percentage):
    if percentage < 0 or percentage > 100:
        raise ValueError("Discount percentage must be between 0 and 100")
    discount_amount = price * (percentage / 100)
    return price - discount_amount

try:
    print(calculate_discount(100, 150))
except ValueError as e:
    print(f"Error: {e}")
```


Ahora, la salida será:
Error: Discount percentage must be between 0 and 100


## Arsenal de Depuración Avanzado

A medida que adquieras más experiencia en Python, tu conjunto de herramientas de depuración se expandirá:

### Control de Versiones

Sistemas como Git permiten rastrear cambios y volver a versiones anteriores si aparece un error.

### Desarrollo Guiado por Pruebas (TDD)

Escribe pruebas antes de codificar. Esto garantiza que tu código funcione como se espera.
Estructuras de Registro

El módulo logging de Python permite clasificar mensajes por niveles de gravedad, facilitando 
el filtrado de información.

```python
import logging

logging.basicConfig(filename='myapp.log', level=logging.DEBUG)

def divide(x, y):
    try:
        result = x / y
        logging.info(f"Successfully divided {x} by {y} to get {result}")
        return result
    except ZeroDivisionError:
        logging.error("Division by zero attempted!")
        return None
```

## El Zen de la Depuración

Depurar es cultivar una mentalidad de resolución de problemas:

- **Ten paciencia**: La depuración lleva tiempo.
- **Sé sistemático**: No cambies cosas al azar.
- **Sé curioso**: Pregúntate por qué ocurre el error.
- **Aprende de los errores**: Documenta tus hallazgos para evitar repetirlos.

## Conclusión

Adoptar estas estrategias te permitirá ver la depuración como un reto gratificante. Con práctica y una actitud positiva, te convertirás en un desarrollador de Python más hábil y un solucionador de problemas más seguro.

### Bloque de Código Funcional: Depuración de un Cálculo Defectuoso

Escenario

Revisar la función calculate_discount(price, discount_percentage) para corregir errores de cálculo.
Tarea

Añade una entrada de ejemplo y ejecuta el código para identificar y corregir el error.

```python
def calculate_discount(price, discount_percentage):
    discount_amount = price * (discount_percentage / 100)
    discounted_price = price + discount_amount  # Error aquí
    return discounted_price

# Código para probar tu salida
price = 50
discount_percentage = 20
discounted_price = calculate_discount(price, discount_percentage)
```

Salida Esperada (después de corregir el error)
40.0

Asegúrate de que el precio final con descuento sea inferior al precio original.
```