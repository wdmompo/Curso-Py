# Diccionarios en Python

## Introducción

Uno de los aspectos más importantes de la programación en Python es organizar y acceder a la información de manera eficiente.

Los diccionarios (`dict`) son una de las estructuras de datos más útiles para administrar y recuperar datos rápidamente.

---

# ¿Qué es un diccionario?

Un diccionario funciona como una libreta de direcciones digital.

Cada entrada contiene:

- Una **clave** (`key`)
- Un **valor** (`value`)

La clave identifica de forma única la información almacenada.

---

# Estructura Clave-Valor

## Concepto

```python
clave -> valor
```

Ejemplo:

```python
telefono = {
    "Ana": "555-1234",
    "Carlos": "555-9876"
}
```

Aquí:

- `"Ana"` es la clave
- `"555-1234"` es el valor

---

# Características Principales de los Diccionarios

Los diccionarios destacan por:

1. Búsquedas eficientes
2. Mutabilidad
3. Representación de relaciones del mundo real

---

# 1. Búsquedas Eficientes

## Acceso rápido a los datos

Los diccionarios permiten recuperar información rápidamente usando una clave.

```python
print(telefono["Ana"])
```

Resultado:

```python
555-1234
```

---

## ¿Por qué son rápidos?

Python optimiza internamente los diccionarios para encontrar valores de manera eficiente, incluso en grandes cantidades de datos.

---

## Ejemplos reales

### Motores de búsqueda

- El usuario escribe una palabra clave
- El sistema recupera rápidamente resultados relacionados

### Aplicaciones de traducción

```python
traducciones = {
    "hello": "hola",
    "world": "mundo"
}
```

---

# 2. Mutabilidad

## Los diccionarios pueden modificarse

Puedes:

- Agregar datos
- Eliminar datos
- Actualizar datos

---

## Agregar elementos

```python
productos = {
    "Laptop": 1200
}

productos["Mouse"] = 25
```

---

## Modificar valores

```python
productos["Laptop"] = 1100
```

---

## Eliminar elementos

```python
del productos["Mouse"]
```

---

# Casos de Uso Reales

## Catálogo de productos

Los precios y disponibilidades cambian constantemente.

Los diccionarios permiten actualizar información fácilmente.

---

## Redes sociales

Un usuario puede cambiar:

- Su perfil
- Su estado
- Sus publicaciones

Los diccionarios ayudan a gestionar estos cambios dinámicamente.

---

# 3. Representación de Relaciones

Los diccionarios son ideales para modelar entidades del mundo real y sus atributos.

---

## Ejemplo: Cliente

```python
cliente = {
    "nombre": "María López",
    "email": "maria@email.com",
    "compras": 15,
    "activo": True
}
```

---

# Sistema de Gestión de Clientes

Cada cliente puede tener:

- Datos de contacto
- Historial de compras
- Interacciones de soporte
- Preferencias

Los diccionarios organizan toda esta información de manera estructurada.

---

# Comprendiendo las Claves y Valores

## Clave (`key`)

La clave actúa como identificador único.

Ejemplo:

```python
"id_empleado"
```

Es comparable a la etiqueta de un cajón.

---

## Valor (`value`)

El valor contiene la información asociada a la clave.

Ejemplo:

```python
"Juan Pérez"
```

Es comparable al contenido almacenado en el cajón.

---

# Ejemplo: Base de Datos de Empleados

```python
empleado = {
    "nombre": "Juan Pérez",
    "departamento": "Ventas",
    "edad": 32,
    "salario": 4500
}
```

---

# Acceso a Información

```python
print(empleado["departamento"])
```

Resultado:

```python
Ventas
```

---

# Diccionarios y Tiendas Online

## Catálogo de productos

Cada producto tiene una clave única:

- SKU
- Código de producto
- ID

---

## Ejemplo

```python
productos = {
    "SKU123": {
        "nombre": "Auriculares",
        "precio": 99,
        "stock": 15
    }
}
```

---

# Diccionarios Anidados

Los valores también pueden ser otros diccionarios.

```python
empresa = {
    "empleado1": {
        "nombre": "Ana",
        "puesto": "Diseñadora"
    },
    "empleado2": {
        "nombre": "Carlos",
        "puesto": "Programador"
    }
}
```

Esto se llama:

- Diccionario anidado

---

# Comprensiones de Diccionarios

Python permite crear diccionarios de forma compacta.

```python
cuadrados = {x: x**2 for x in range(5)}
```

Resultado:

```python
{
    0: 0,
    1: 1,
    2: 4,
    3: 9,
    4: 16
}
```

---

# Ventajas de los Diccionarios

## Beneficios principales

- Acceso rápido a datos
- Organización clara
- Flexibilidad
- Fácil actualización
- Representación eficiente de relaciones

---

# Idea Principal

Los diccionarios son fundamentales en Python porque permiten:

- Buscar información rápidamente
- Relacionar datos de forma estructurada
- Modelar entidades reales
- Actualizar información dinámicamente

Son herramientas esenciales para crear aplicaciones modernas y eficientes.


## Imagina que estás creando un programa para almacenar información de contacto. Necesitas encontrar rápidamente el número de teléfono de una persona utilizando su nombre. ¿Cuál de las siguientes opciones sería la forma MÁS eficaz de almacenar y recuperar esta información? Selecciona la mejor respuesta.


- [x] Un diccionario donde el nombre de la persona es la clave y su número de teléfono es el valor.
- [ ] Una lista en la que cada elemento contiene el nombre y el número de teléfono de la persona. Tendrías que repasar la lista para encontrar el nombre correcto.
- [ ] Un simple archivo de texto en el que cada línea contiene un nombre y un número de teléfono, y que se lee a través del archivo para encontrar el nombre.
- [ ] Listas separadas para nombres y números de teléfono, donde la posición en cada lista corresponde a la misma persona.

Correcto
Correcto Al igual que la "libreta de direcciones de alta tecnología" descrita en el vídeo, un diccionario permite acceder directamente al número de teléfono (el valor) utilizando el nombre de la persona (la clave única). Es la forma más eficaz de buscar información sin tener que buscar en una secuencia de elementos.