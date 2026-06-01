# Excepciones Comunes en Python: Una Guía de Campo

## Introducción
Las excepciones son señales de que algo inesperado ha ocurrido durante la ejecución del código. Su manejo adecuado es crucial para construir aplicaciones robustas en Python.

## Excepciones Comunes

### 1. NameError
- **Descripción**: Ocurre cuando Python no reconoce un nombre (variable, función, módulo).
- **Causas**:
  - Errores tipográficos.
  - Problemas de alcance (una variable definida en una función no es accesible fuera de ella).
  - Faltan importaciones.
- **Soluciones**:
  - Verifica cuidadosamente los nombres.
  - Asegúrate de importar correctamente los módulos.

### 2. TypeError
- **Descripción**: Aparece al intentar combinar tipos de datos incompatible.
- **Causas**:
  - Operaciones no coincidentes (ej. sumar una cadena y un entero).
  - Argumentos de función incorrectos (ej. pasar un número a `len()`).
  - Problemas en la herencia de clases.
- **Soluciones**:
  - Convierte los datos al tipo apropiado.
  - Usa `isinstance()` para verificar tipos en funciones.

### 3. IndexError
- **Descripción**: Ocurre al intentar acceder a un índice que no existe en una lista, tupla o cadena.
- **Causas**:
  - Acceso fuera de límites.
  - Secuencias vacías.
- **Soluciones**:
  - Comprueba la longitud de la secuencia antes de acceder a sus elementos.
  - Usa bloques `try-except` para manejar errores.

### 4. KeyError
- **Descripción**: Ocurre al intentar acceder a un valor en un diccionario usando una clave que no existe.
- **Causas**:
  - Clave inexistente.
  - Creación dinámica de claves que no coinciden.
- **Soluciones**:
  - Verifica si la clave está presente usando `if key in my_dict:`.
  - Utiliza el método `get()` para evitar errores.

## Proceso de Aprendizaje
- Las excepciones son oportunidades para aprender.
- Lee atentamente los mensajes de error para diagnosticar la causa raíz.
- Experimenta con diferentes soluciones y no dudes en buscar ayuda.

## Manejo de Excepciones en Producción
- Las excepciones no gestionadas pueden causar graves problemas.
- Registra errores y proporciona mensajes claros para mejorar la estabilidad de la aplicación.

## Ejemplo de Manejo de Excepciones
```python
import logging

my_dict = {"a": 1, "b": 2}
try:
    print(my_dict["c"])
except KeyError as e:
    logging.error(f"KeyError encountered: {e}")
    # Manejar el error o proporcionar un mecanismo de recuperación
```

Reto de Código: Manejar una KeyError
Tarea
Escribe una función get_city_population que tome un diccionario de poblaciones y el nombre de una ciudad, devolviendo la población o lanzando un KeyError si no se encuentra.
Ejemplo
city_populations = {"New York": 8336817, "Los Angeles": 3979576, "Chicago": 2679044}
city_name = "Tampa"  # Debe lanzar un KeyError indicando que "Tampa" no se encuentra.

Respuesta

```python 
def get_city_population(populations, city):
    try:
        return populations[city]
    except KeyError:
        raise KeyError(f'Ciudad "{city}" no encontrada en los datos de población.')
```