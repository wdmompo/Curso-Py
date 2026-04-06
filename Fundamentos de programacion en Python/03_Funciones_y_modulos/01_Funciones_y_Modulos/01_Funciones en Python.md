# Funciones en Python

## 📌 ¿Qué es una función?
Las **funciones** son bloques de código reutilizables que realizan tareas específicas.  
Encapsulan un conjunto de instrucciones que puedes ejecutar múltiples veces sin tener que reescribir el código.

Se pueden considerar como pequeños programas dentro de un programa más grande.

---

## 🎯 ¿Por qué usar funciones?

Las funciones son fundamentales porque aportan:

- **Eficiencia**
- **Organización**
- **Reutilización**

Permiten crear código más:
- Robusto
- Mantenible
- Repetible

---

## 🔑 Beneficios principales

### 1. Organización del código
Las funciones dividen tareas complejas en partes más pequeñas y manejables.

- Facilitan la lectura y comprensión
- Ayudan a mantener el código
- Organizan el programa en secciones lógicas (como capítulos de un libro)

---

### 2. Reutilización
Una función puede ser utilizada múltiples veces.

- Evita repetir código
- Reduce errores
- Asegura consistencia

**Ejemplo:**
- Calcular impuestos en múltiples transacciones
- Procesar nóminas para varios empleados

---

### 3. Abstracción
Ocultan los detalles complejos detrás de una interfaz simple.

Permiten enfocarse en la lógica general sin preocuparse por la implementación interna.

**Ejemplo:**
Una función para enviar correos puede:
- Conectarse al servidor
- Formatear mensajes
- Adjuntar archivos

Todo esto ocurre internamente, mientras tú solo llamas a la función.

---

### 4. Colaboración
Las funciones permiten dividir el trabajo entre varios desarrolladores.

- Código modular
- Desarrollo en paralelo
- Integración más sencilla

---

## 🧩 Tipos de funciones en Python

### 1. Funciones integradas (built-in)
Funciones predefinidas en Python, como:

- `print()`
- `len()`
- `input()`

---

### 2. Funciones definidas por el usuario
Funciones creadas por el programador para tareas específicas.

---

### 3. Funciones lambda
Funciones anónimas de una sola línea.

- Se usan para operaciones simples
- Frecuentes como argumentos en otras funciones

**Ejemplo:**
Ordenar empleados por salario.

---

## 🏗️ Sintaxis básica de una función

```python
def nombre_funcion(parametros):
    """Docstring que explica la función"""
    
    # Código de la función
    
    return valor
```

### Desglose

- def → palabra clave para definir una función
- nombre_funcion → nombre descriptivo
- parametros → entradas de la función
- docstring → descripción de la función
- código → instrucciones a ejecutar
- return → valor que devuelve la función

## 🧠 Conclusión

Las funciones son una herramienta esencial en Python.
Permiten escribir código limpio, eficiente y reutilizable.

Practicar su uso es clave para mejorar como programador.

### En un gran proyecto de software con múltiples desarrolladores, ¿cuál de las siguientes opciones explica mejor cómo las funciones de Python contribuyen a una colaboración eficiente? Seleccione la mejor respuesta.

- [ ] Las funciones animan a los desarrolladores individuales a escribir su código con estilos únicos, fomentando la creatividad y la diversidad dentro del proyecto.
- [ ] Las funciones proporcionan un vocabulario compartido para debatir y comprender partes específicas del código, lo que facilita una comunicación clara entre los miembros del equipo.
- [x] Las funciones permiten el desarrollo paralelo de distintas part del proyecto, lo que permite a varios desarrolladores trabajar en unidades de código autónomas que posteriormente pueden integrarse sin problemas.

> Correcto Capta la esencia de cómo las funciones fomentan el trabajo en equipo al permitir a los desarrolladores trabajar de forma independiente en piezas modulares de código, lo que en última instancia acelera el desarrollo y reduce los conflictos.

- [ ] Las funciones permiten a los desarrolladores trabajar en partes aisladas del código base sin necesidad de comprender la estructura de todo el proyecto.

