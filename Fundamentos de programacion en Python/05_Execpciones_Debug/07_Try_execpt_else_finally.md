# Resumen de la Estructura TRY-EXCEPT-ELSE-FINALLY

La estructura **TRY-EXCEPT-ELSE-FINALLY** es fundamental en la programación para manejar excepciones de manera proactiva, permitiendo anticipar y gestionar errores durante la ejecución del programa.

## Componentes de la Estructura

- **TRY**: Contiene el código que puede generar excepciones, como operaciones de archivos o validación de entradas de usuario.
- **EXCEPT**: Especifica la respuesta a excepciones particulares. Permite personalizar la gestión de errores.
- **ELSE**: (Opcional) Contiene código que se ejecuta solo si no ocurren excepciones.
- **FINALLY**: Código que siempre se ejecutará, independientemente de si se produjo una excepción. Usualmente se utiliza para operaciones de limpieza.

## Usos Comunes

1. **Manejo de Archivos**: Ideal para situaciones donde los archivos pueden no existir o tener permisos restringidos.
2. **Operaciones de Red**: Permite manejar errores de conexión y tiempos de espera mediante reintentos.
3. **Entrada del Usuario**: Ayuda a validar datos ingresados, proporcionando mensajes claros en caso de errores.

## Beneficios

- **Prevención de Bloqueos**: Evita que el programa se cierre inesperadamente ante errores.
- **Mejora la Experiencia del Usuario**: Ofrece mensajes de error informativos y sugerencias claras.
- **Mayor Legibilidad**: Separa el código de lógica de negocio de la gestión de errores, facilitando la comprensión.
- **Facilita la Depuración**: Proporciona información de rastreo útil para solucionar problemas.
- **Robustez**: Hace que el código sea menos propenso a errores inesperados, especialmente en proyectos grandes.

## Conclusión

La estructura TRY-EXCEPT-ELSE-FINALLY es esencial en Python. Practicar su uso permitirá a los programadores manejar excepciones de manera efectiva y estratégica.

## Estás escribiendo un script en Python para procesar datos de un Archivo CSV cargado por un usuario. Desea que el script gestione posibles errores, por ejemplo, si falta el archivo cargado o contiene datos no válidos. ¿Qué parte de la estructura try-except-else-finally sería la más adecuada para alertar al usuario si se produce una excepción durante el procesamiento del archivo?

- El bloque try 
- El bloque else 
- **El bloque except**
- El bloque finally 

Correcto
> Correcto El bloque except está diseñado específicamente para capturar y gestionar excepciones, por lo que es el lugar ideal para mostrar un mensaje de error al usuario.


# Manejo de Excepciones en Python

Hoy exploraremos el **manejo de excepciones**, fundamental para crear aplicaciones robustas que manejen situaciones inesperadas. Este proceso actúa como una red de seguridad, permitiendo que tu aplicación funcione sin problemas a pesar de los errores.

## Introducción al Bloque try-except

- **try**: Contiene el código que puede lanzar una excepción.
- **except**: Se ejecuta si ocurre una excepción, permitiendo manejarla elegantemente (registrar errores, ofrecer alternativas, etc.).

### Ejemplo de Uso

En un bloque `try`, puedes intentar realizar una operación arriesgada, como una división. Si ocurre un error de división por cero, el bloque `except` captura el error y proporciona un mensaje claro.

## Estrategias de Manejo de Errores

Es crucial capturar excepciones de manera específica para no enmascarar otros problemas. Esto asegura que tu programa no se detenga abruptamente, sino que informe al usuario sobre el problema, mejorando la experiencia.

### Cláusulas Opcionales

- **else**: Se ejecuta si no hay excepciones en el bloque `try`. Es útil para ejecutar código que solo debería correr bajo condiciones ideales.
- **finally**: Se ejecuta siempre, independientemente de si se produjo una excepción. Se usa comúnmente para operaciones de limpieza, como cerrar archivos.

## Ejemplo Práctico

1. **try**: Obtener entrada del usuario y realizar una división.
2. **except**: Manejar errores como `ValueError` o `ZeroDivisionError` con mensajes adecuados.
3. **finally**: Asegurar que los recursos se cierren o limpien.

## Lanzamiento de Excepciones

Puedes lanzar excepciones explícitamente usando `raise`, y crear excepciones personalizadas para manejar errores específicos de tu aplicación.

## Escenarios del Mundo Real

- **Archivos**: Manejo de archivos no encontrados o errores de permiso.
- **Conexiones de Red**: Manejar tiempos de espera y errores de conexión.
- **Entradas del Usuario**: Validar datos y proporcionar orientación si hay errores.
- **API Externas**: Manejo de límites de velocidad y errores de autenticación.
- **Bases de Datos**: Manejo de errores de conexión o problemas de integridad de datos.

## Conclusión

El manejo de excepciones no solo resuelve errores, sino que construye aplicaciones resilientes que mejoran la experiencia del usuario. Haz del manejo de excepciones una parte integral de tu codificación en Python para desarrollar aplicaciones robustas y confiables.

___

# Manejo de Excepciones: Buenas Prácticas

El manejo de excepciones es fundamental para construir aplicaciones Python robustas y fáciles de usar. Consiste en anticipar y manejar errores inesperados, manteniendo la aplicación funcionando sin interrupciones.

## Importancia del Manejo de Excepciones

### Prevención de Caídas Abruptas
Las excepciones no manejadas pueden causar terminaciones inesperadas de programas, lo que resulta frustrante para los usuarios y puede llevar a la pérdida de datos.

#### Ejemplo:
En un sitio de comercio electrónico, un error en el procesamiento de pagos podría bloquear la aplicación, dejando pedidos incompletos y afectando la confianza del usuario.

### Recuperación Gradual y Experiencia del Usuario
El manejo adecuado de excepciones permite que las aplicaciones se recuperen de errores presentando mensajes informativos o sugiriendo acciones alternativas.

#### Ejemplo:
Una API externa que experimenta problemas puede mostrar un mensaje amigable en lugar de un error genérico.

### Depuración Optimizada
Las excepciones proporcionan información valiosa a través de rastreos detallados, facilitando la identificación de problemas en el código.

#### Ejemplo:
Un script de análisis de datos puede utilizar el rastreo de excepciones para identificar un acceso fuera de límites en una lista.

### Profesionalidad y Fiabilidad
El manejo de excepciones refleja un compromiso con la calidad del software, aumentando la confianza del usuario.

#### Ejemplo:
Una aplicación financiera que se bloquea por entradas no válidas puede dañar la reputación del software.

## Estructura try-except-finally

El manejo de excepciones en Python se basa en tres palabras clave:

- **try**: Contiene el código que podría generar un error.
  
```python
file_name = "sample.txt"
try:
    with open(file_name, 'r') as file:
        contents = file.read()
        print(contents)

    # except: Especifica la acción a tomar si ocurre una excepción específica.
except FileNotFoundError:
    print("Error: File not found -", file_name)
# finally: Código que se ejecuta siempre, útil para liberar recursos.
```

Selección de Excepciones
Es importante elegir la excepción correcta para manejar errores específicos:

- ZeroDivisionError: División por cero.
- TypeError: Operaciones con tipos incompatibles.
- FileNotFoundError: Archivo no encontrado.
- IndexError: Índice fuera de rango.
- KeyError: Clave no existente en un diccionario.

Ejemplo de Manejo de Excepciones

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")
except TypeError:
    print("Error: Invalid data types")
```

Registro de Errores
Registrar excepciones es crucial para la depuración:

```
import logging

try:
    # Código propenso a errores
except Exception as e:
    logging.error(f"An error occurred: {e}")
```


## Creación de Excepciones Personalizadas

A veces, necesitarás definir excepciones específicas para tu aplicación:

```python
class InvalidCredentialsError(Exception):
    pass

if not valid_credentials(username, password):
    raise InvalidCredentialsError("Incorrect username or password")
```

Evitar Clausulas Except Demasiado Amplias
Capturar todas las excepciones con una cláusula except: es desaconsejado, ya que oculta la naturaleza del error.
Ejemplo de Captura Amplia

```python
try:
    result = some_function()
except:
    print("An error occurred")  # Oculta el problema real
```


## Tipado de Patos

Python permite un enfoque flexible, pero puede llevar a errores inesperados. Usa comprobaciones de tipo cuando sea necesario.

Ejemplo de Comprobación de Tipos

```python
def calculate_area(shape):
    try:
        return shape.calculate_area()
    except AttributeError:
        raise TypeError("Object does not have a calculate_area method")
```

## Filosofías de Manejo de Errores

### LBYL (Look Before You Leap)
Verifica errores potenciales antes de ejecutar el código.

### EAFP (Easier to Ask Forgiveness than Permission)
Intenta ejecutar el código y captura excepciones si ocurren. Este enfoque es más común en Python.

### Reto de Código: Lectura Segura de Archivos

Tarea

Escribe una función read_file_contents que tome file_path como argumento. Utiliza un bloque try-except para abrir y leer un archivo, manejando FileNotFoundError.
Consejos

Nombra tu variable de archivo file.

Usa with open() para cerrar automáticamente el archivo.

Ejemplo de Entrada
read_file_contents("/Users/Example/Documents/my_file.txt")

Salida Esperada
Error: Archivo no encontrado - /Users/Example/Documents/my_file.txt