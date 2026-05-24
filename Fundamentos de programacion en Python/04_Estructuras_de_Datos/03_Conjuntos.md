# Sets en Python

## Introducción

Cuando trabajas con colecciones de elementos únicos en Python, una de las estructuras de datos más importantes son los conjuntos (`set`).

Los sets permiten:

- Organizar elementos únicos
- Eliminar duplicados automáticamente
- Realizar búsquedas rápidas
- Aplicar operaciones matemáticas entre colecciones

---

# ¿Qué es un Set?

Un set es una colección:

- Desordenada
- Mutable
- Sin elementos duplicados

Cada elemento del conjunto debe ser único.

---

# Crear un Set

```python
frutas = {"manzana", "banana", "pera"}
```

---

# Propiedad de Unicidad

La característica principal de los sets es que no permiten duplicados.

```python
numeros = {1, 2, 2, 3, 3, 3}

print(numeros)
```

Resultado:

```python
{1, 2, 3}
```

Los valores repetidos se eliminan automáticamente.

---

# ¿Por Qué Son Útiles los Sets?

Los sets son ideales cuando necesitas:

- Evitar duplicados
- Verificar pertenencia rápidamente
- Limpiar datos
- Comparar colecciones
- Realizar operaciones matemáticas

---

# Pruebas de Membresía

## Verificar si un elemento existe

```python
usuarios = {"Ana", "Carlos", "Lucía"}

print("Ana" in usuarios)
```

Resultado:

```python
True
```

---

# Eficiencia de los Sets

Los sets usan estructuras optimizadas como:

- Tablas hash

Esto permite búsquedas extremadamente rápidas, incluso con grandes cantidades de datos.

---

# Casos de Uso de Membresía

## Lista de suscriptores

```python
suscriptores = {"ana@email.com", "juan@email.com"}
```

Puedes verificar rápidamente si un usuario ya está registrado.

---

# Eliminación Automática de Duplicados

## Limpieza de datos

```python
datos = ["Ana", "Carlos", "Ana", "Lucía"]

datos_unicos = set(datos)

print(datos_unicos)
```

Resultado:

```python
{"Ana", "Carlos", "Lucía"}
```

---

# Casos Reales

## Conferencias

Evitar contar varias veces al mismo asistente.

## Inventarios

Evitar productos repetidos.

## Redes sociales

Eliminar hashtags duplicados para analizar tendencias.

---

# Agregar Elementos

```python
frutas = {"manzana", "banana"}

frutas.add("pera")
```

---

# Eliminar Elementos

```python
frutas.remove("banana")
```

---

# Operaciones Matemáticas con Sets

Los sets permiten realizar operaciones muy poderosas.

---

# Unión (`union`)

Combina todos los elementos únicos de dos conjuntos.

```python
a = {"manzana", "banana"}
b = {"pera", "banana"}

resultado = a | b

print(resultado)
```

Resultado:

```python
{"manzana", "banana", "pera"}
```

---

# Intersección (`intersection`)

Encuentra elementos comunes entre conjuntos.

```python
a = {"python", "sql", "excel"}
b = {"python", "java", "sql"}

resultado = a & b

print(resultado)
```

Resultado:

```python
{"python", "sql"}
```

---

# Diferencia (`difference`)

Obtiene elementos que existen en un conjunto pero no en otro.

```python
a = {"python", "sql", "excel"}
b = {"python"}

print(a - b)
```

Resultado:

```python
{"sql", "excel"}
```

---

# Diferencia Simétrica

Elementos que están en un conjunto o en otro, pero no en ambos.

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a ^ b)
```

Resultado:

```python
{1, 2, 4, 5}
```

---

# Aplicaciones Reales

## CRM (Gestión de Clientes)

Garantiza que cada correo electrónico se almacene una sola vez.

---

## Inventarios y Logística

Evita productos duplicados en registros de stock.

---

## Redes Sociales

Permite analizar hashtags únicos y tendencias populares.

---

## Marketing

Encontrar clientes que compraron productos de distintas categorías usando intersecciones.

---

# Comparación con Otras Estructuras

| Estructura | Ordenada | Duplicados | Acceso rápido | Uso principal |
|---|---|---|---|---|
| Lista (`list`) | Sí | Sí | Medio | Colecciones ordenadas |
| Diccionario (`dict`) | Sí | Claves únicas | Muy rápido | Relacionar datos |
| Set (`set`) | No | No | Muy rápido | Elementos únicos |

---

# Ventajas de los Sets

## Beneficios principales

- Eliminación automática de duplicados
- Búsquedas rápidas
- Operaciones matemáticas eficientes
- Limpieza de datos
- Comparación sencilla de colecciones

---

# Idea Principal

Los sets son herramientas poderosas para manejar datos únicos en Python.

Son especialmente útiles cuando necesitas:

- Garantizar unicidad
- Eliminar duplicados
- Comparar colecciones
- Realizar análisis rápidos de datos

Combinados con otras estructuras de datos, permiten construir soluciones eficientes y escalables.



## Estás intentando dar con un ejemplo en el que el uso de un conjunto Python sería la estructura de datos MÁS apropiada y eficiente. ¿Cuál de los siguientes escenarios lo ilustra mejor? Elige la mejor respuesta.


- [x] Recopilación de una lista única de direcciones de correo electrónico a partir de una base de datos para evitar el envío de correos electrónicos promocionales duplicados.
- [ ] Asignación de ID de productos a sus precios correspondientes en una tienda en línea.
- [ ] Mantener una secuencia de acciones del usuario en un videojuego, donde es necesario preservar el orden de las acciones.
- [ ] Almacenar una lista de nombres de alumnos en el orden en que se matricularon en una clase. 

Correcto. Los conjuntos son ideales para garantizar la unicidad, que es esencial para evitar la duplicación de correos electrónicos.