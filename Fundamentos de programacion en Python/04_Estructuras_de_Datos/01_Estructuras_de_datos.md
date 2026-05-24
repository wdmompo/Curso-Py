# Estructuras de Datos en Python

## Introducción

Las estructuras de datos en Python funcionan como contenedores para organizar información.  
Elegir la estructura adecuada ayuda a crear código más limpio, eficiente y fácil de mantener.

Las estructuras más comunes son:

- Listas (`list`)
- Diccionarios (`dict`)
- Conjuntos (`set`)

---

# Listas (`list`)

## ¿Qué son?

Las listas almacenan colecciones ordenadas de elementos.

Cada elemento tiene una posición llamada índice.

Ejemplo:

```python
frutas = ["manzana", "banana", "pera"]
```

Posiciones:

- `"manzana"` → índice `0`
- `"banana"` → índice `1`
- `"pera"` → índice `2`

---

## Características de las listas

Las listas son:

- Ordenadas
- Modificables
- Flexibles
- Permiten elementos duplicados

---

## Agregar elementos

```python
frutas.append("brócoli")
```

Resultado:

```python
["manzana", "banana", "pera", "brócoli"]
```

---

## Modificar elementos

```python
frutas[1] = "uva"
```

---

## Eliminar elementos

```python
frutas.remove("pera")
```

---

## Listas anidadas

Las listas pueden contener otras listas.

```python
compras = [
    ["manzana", "banana"],
    ["pan", "leche"]
]
```

Esto funciona como cestas organizadas dentro de otras cestas.

---

# Diccionarios (`dict`)

## ¿Qué son?

Los diccionarios almacenan información usando pares:

- clave → valor

Funcionan como tablas de consulta.

---

## Ejemplo

```python
precios = {
    "manzana": 1.50,
    "aguacate": 3.20,
    "banana": 2.00
}
```

---

## Acceder a valores

```python
print(precios["aguacate"])
```

Resultado:

```python
3.20
```

---

## Características de los diccionarios

Los diccionarios:

- Relacionan datos
- Permiten búsquedas rápidas
- Son ideales para información asociada

---

## Agregar elementos

```python
precios["pera"] = 2.80
```

---

## Modificar valores

```python
precios["banana"] = 2.50
```

---

## Eliminar elementos

```python
del precios["manzana"]
```

---

# Conjuntos (`set`)

## ¿Qué son?

Los conjuntos almacenan elementos únicos.

No permiten duplicados.

---

## Ejemplo

```python
ingredientes = {"sal", "pimienta", "ajo"}
```

---

## Características de los sets

Los conjuntos:

- No tienen orden fijo
- No permiten repetidos
- Son rápidos para búsquedas

---

## Evitar duplicados

```python
ingredientes.add("sal")
```

El conjunto seguirá teniendo un solo `"sal"`.

---

## Verificar existencia

```python
if "ajo" in ingredientes:
    print("Ya tienes ajo")
```

---

# Operaciones útiles con sets

## Unión

Combina conjuntos.

```python
a = {"manzana", "banana"}
b = {"pera", "banana"}

print(a | b)
```

Resultado:

```python
{"manzana", "banana", "pera"}
```

---

## Intersección

Encuentra elementos comunes.

```python
print(a & b)
```

Resultado:

```python
{"banana"}
```

---

# Comparación de Estructuras

| Estructura | Ordenada | Modificable | Duplicados | Uso principal |
|---|---|---|---|---|
| Lista (`list`) | Sí | Sí | Sí | Colecciones ordenadas |
| Diccionario (`dict`) | Sí | Sí | Claves únicas | Relacionar datos |
| Set (`set`) | No | Sí | No | Elementos únicos |

---

# Idea Principal

Las estructuras de datos ayudan a organizar información de forma eficiente.

La clave es elegir la herramienta adecuada:

- Usa listas para colecciones ordenadas
- Usa diccionarios para relacionar información
- Usa sets para elementos únicos y búsquedas rápidas

Python incluye muchas más estructuras especializadas, pero estas son la base para escribir código limpio y bien organizado.

