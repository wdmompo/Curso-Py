# Resumen sobre Excepciones en Python

## Introducción
- Se compara la construcción de un rascacielos con la gestión de imprevistos en programación.
- Las excepciones en Python son alertas que indican problemas durante la ejecución del código.

## Definición de Excepciones
- Una excepción es como una luz de control del motor, avisando sobre problemas antes de que causen fallos.
- Interrumpen el flujo normal del programa y permiten resolver problemas antes de que el código se bloquee.

## Tipos de Excepciones
- Ejemplos comunes: división por cero, archivo no encontrado, entrada de usuario no válida.
- Al ocurrir una excepción, se lanza un objeto de excepción que contiene:
  - Tipo de excepción
  - Rastreo de la ejecución
  - Mensaje de error

## Manejo de Excepciones
- Las excepciones se gestionan con bloques `try` y `except`.
  - **Bloque `try`**: Contiene el código que puede generar una excepción.
  - **Bloque `except`**: Especifica cómo manejar la excepción si ocurre.

### Ejemplo de Uso
- Al intentar dividir por cero, el programa no falla; en su lugar, salta al bloque `except` y muestra un mensaje de error.

## Múltiples Bloques Except
- Se pueden gestionar diferentes tipos de excepciones usando varios bloques `except`.
- Cada bloque proporciona un mensaje de error específico.

## Recomendaciones
- Evitar el uso excesivo de excepciones; utilizarlas solo para condiciones inesperadas.
- Las excepciones no deben ser un método para controlar el flujo normal del programa.

## Conclusión
- El manejo adecuado de excepciones es crucial para mantener la estabilidad del programa. Se continuará con más sobre excepciones en la siguiente parte.

## Qué información contiene un objeto de excepción? Seleccione todo lo que corresponda.

- [ ] Frecuencia del error
- [x] Un rastreo
- [x] Tipo de excepción
- [x] El mensaje de error

> Correcto Los objetos de excepción contienen el tipo de excepción, un rastreo y el mensaje de error para ayudarle a localizar y resolver el problema. 

# Excepciones en Python

## Introducción
- Las excepciones son interrupciones en el flujo normal de ejecución del código en Python, pero ofrecen beneficios significativos que mejoran la robustez y la usabilidad de los programas.

## Beneficios de las Excepciones
1. **Manejo Estructurado de Errores**:
   - Permiten tratar errores y situaciones inesperadas, evitando bloqueos del programa.
   - Ejemplo: Un error de archivo no encontrado puede generar un mensaje que sugiera comprobar la ruta.

2. **Mejora de la Experiencia del Usuario**:
   - Mensajes de error pueden ser útiles e inteligentes, sugiriendo soluciones.
   - Ejemplo: Mensaje para corregir una dirección de correo electrónico no válida en un formulario.

3. **Ayuda en la Depuración**:
   - Proporcionan información de rastreo que indica la línea de código donde ocurrió el error.
   - Facilita la identificación y corrección de problemas, como en una calculadora financiera.

4. **Mantenibilidad del Código**:
   - Hacen que el código sea más robusto y menos propenso a errores, mejorando la mantenibilidad en proyectos grandes.

## Tipos Comunes de Excepciones
- **Error de División por Cero**: Ocurre al intentar dividir un número por cero.
- **Error de Archivo No Encontrado**: Sucede al acceder a un archivo inexistente o dañado.
- **Error de Tipo**: Se produce al realizar operaciones en tipos incompatibles (ej. sumar una cadena y un entero).
- **Error de Valor**: Ocurre al pasar un argumento inapropiado a una función (ej. convertir una cadena no numérica a entero).
- **Error de Índice**: Sucede al acceder a un índice fuera de los límites de una lista.

## Otras Excepciones Notables
- **Error de Importación**: Cuando un módulo o paquete no se encuentra.
- **Error Clave**: Cuando no se encuentra una clave en un diccionario.
- **Error de Atributo**: Fallas en referencias o asignaciones de atributos.
- **Error de Sintaxis**: Ocurre por errores en la sintaxis del código Python.

## Aplicaciones en el Mundo Real
- Validación de entradas de usuario en formularios.
- Gestión de errores en operaciones de red, como tiempos de espera.

## Conclusión
- Comprender y manejar excepciones permite crear aplicaciones confiables, que manejan la naturaleza impredecible de los datos y las interacciones de los usuarios.

### Estás desarrollando un script en Python que lee datos de archivos externos y realiza cálculos. Durante las pruebas, se encuentra con una situación en la que el script intenta acceder a un archivo que falta en el directorio especificado. ¿Cuál de los siguientes tipos de excepción incorporados es MÁS probable que se produzca en este caso? Seleccione la mejor respuesta.

- [ ] TypeError
- [c] FileNotFoundError
- [ ] ValueError
- [ ] ZeroDivisionError

