# Importancia en el manejo de datos

Los datos reales suelen ser desordenados. Las listas permiten:

- Filtrar valores no deseados  
- Eliminar duplicados  
- Transformar datos a formatos útiles  
- Automatizar tareas repetitivas  

Ejemplo:
- Detectar direcciones incompletas en datos de clientes
- Limpiar errores como espacios extra o errores tipográficos

Las **listas** son estructuras de datos fundamentales en Python que permiten almacenar colecciones de elementos de forma flexible. A diferencia de otros lenguajes, pueden contener distintos tipos de datos al mismo tiempo, como números, cadenas, booleanos e incluso otras listas.

## Aplicaciones prácticas

- **Finanzas**: calcular promedios (ej: precios de acciones)
- **Ciencia**: filtrar resultados experimentales
- **Marketing**: personalizar correos a partir de listas de usuarios
- **Automatización**: renombrar archivos, extraer texto, agrupar datos


## Características principales de las listas

Las listas en Python tienen tres atributos clave:

### 1. Orden (Organized storage)
- 
- Permiten acceder fácilmente a elementos específicos.
- Son útiles cuando el orden importa (ej: procesos, eventos cronológicos, listas de tareas).

---

### 2. Mutabilidad (Mutable nature)
- Las listas son dinámicas.
- Se pueden modificar después de su creación:
  - Agregar elementos
  - Eliminar elementos
  - Cambiar valores existentes
- Son ideales para datos que cambian con el tiempo (ej: inventarios, registros de clientes).

---

### 3. Versatilidad (Versatility)
- Pueden almacenar diferentes tipos de datos:
  - Números (enteros y flotantes)
  - Cadenas de texto
  - Booleanos
  - Otras listas
- Permiten representar estructuras complejas del mundo real.

---

## Declaración de listas

Ejemplos comunes:

- **Lista vacía**

```python
new_list = []
```

- **Lista con elementos**

```python
grocery_list = ["milk", "hummus", "bread", "cheese", "apples"]
```

---

## Tipos de listas

- **Lista de números**

```python
primes = [2, 3, 5, 7, 11, 13]
```

- **Lista de cadenas**

```python
vowels = ["a", "e", "i", "o", "u"]
```

- **Lista de booleanos**

```python
coin_flips = [True, False, True, True, False]
```

- **Lista con valores mixtos**

```python
student_record = ["Aashvi", 24, "Computer Science", 3.8, True]
```

---

## Operaciones básicas

### Imprimir una lista

```python
print(grocery_list)
```

Salida:

```
['milk', 'hummus', 'bread', 'cheese', 'apples']
```

### Indexación

Los índices comienzan en 0

### Acceso a elementos:

```python
print(grocery_list[0])  # "milk"
```

### Longitud de una lista

```python
print(len(grocery_list))
```

Salida:

```
5
```

### Último elemento

```python
print(grocery_list[len(grocery_list) - 1])
```

Salida:

```
apples
```

#### Rebanado (Slicing)

el rebanado permite obtener una parte de la lista. crean una nueva lista con los elementos seleccionados.
es muy útil para extraer subconjuntos de datos de una lista. 

##### Permite obtener una parte de la lista:

```python
print(grocery_list[0:2])
```

Salida:

```
['milk', 'hummus']
```

##### Slice con índice negativo

Permite acceder a elementos desde el final de la lista:

```python
print(grocery_list[-1])  # "apples"
```
salida:

```bash
apples
``` 

##### Slice con paso 

Permite acceder a elementos saltando ciertos índices:

```python
print(grocery_list[0:5:2])  # ["milk", "bread", "apples"]
```

##### Inverter un slice

Permite acceder a elementos en orden inverso:

```python
print(grocery_list[::-1])  # ["apples", "cheese", "bread", "hummus", "milk"]
```

## Métodos comunes de listas

- `len(lista)`          # cantidad de elementos
- `list.append(x)`      # agregar elemento
- `list.insert(i, x)`   # insertar en posición
- `list.remove(x)`      # eliminar elemento
- `list.sort()`         # ordenar
- `list.reverse()`      # invertir
- `list.count(x)`       # contar ocurrencias
- `x in lista`          # verificar existencia
- `list.index(x)`       # obtener índice
- `list.pop(i)`         # eliminar y devolver elemento



### Comprensión de listas

Permite crear nuevas listas de forma concisa:

- Transforma datos
- Filtra elementos
- Realiza cálculos en una sola línea

Ejemplo de uso:
- Limpiar datos con errores (espacios, inconsistencias)
- Generar nuevas listas procesadas

Forma concisa de crear listas:

```python
[expression for item in iterable]
```

Ejemplo:

```python
exam_scores = [55, 70, 78, 52, 68]
curve_amount = 10

curved_grades = [score + curve_amount for score in exam_scores]
```
#### Comprensión de listas con condicional

Permite crear listas basadas en condiciones:

```python
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
```

#### Compresion de listas con if else

Permite crear listas basadas en condiciones:

```python
even_odd = ["par" if x % 2 == 0 else "impar" for x in range(1, 6)]
```

salida 

```bash
["par", "impar", "par", "impar", "par"]
```

## Errores comunes

- IndexError: índice fuera de rango
- ValueError: valor inexistente en la lista

## Listas bidimensionales

Listas dentro de listas:

```python	
grid = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

print(grid[1][2])  # 6
``` 
Salida:

```
6
```


## Idea clave

Las listas son una herramienta esencial en Python porque combinan:
- **Orden**
- **Flexibilidad**
- **Capacidad de modificación**

Esto las convierte en una solución poderosa para gestionar datos en múltiples contextos.

## Pregunta

### Estás trabajando en un proyecto Python para realizar un seguimiento de las ventas diarias de una tienda durante un mes. ¿Cuál de las siguientes características hace que una lista sea la estructura de datos MÁS adecuada para esta tarea? Selecciona la mejor respuesta.

- [ ] Las listas son mutables, lo que le permite añadir o eliminar fácilmente datos de ventas según sea necesario.
- [ ] Las listas pueden anidarse unas dentro de otras, lo que permite crear estructuras de datos complejas para almacenar información detallada sobre las ventas.
- [x] Las listas mantienen el orden en que se añaden los elementos, conservando la secuencia cronológica de los datos de venta.
- [ ] Las listas pueden almacenar elementos de distintos tipos de datos dentro de la misma lista.

Correcto
Correcto La naturaleza ordenada de las listas permite realizar un seguimiento preciso de las ventas diarias y analizar las tendencias a lo largo del tiempo.

## Está trabajando con una lista de datos de clientes que incluye nombres, direcciones de correo electrónico e historial de compras. Necesita identificar y extraer los clientes que han realizado compras superiores a un importe determinado. ¿Qué técnica de manipulación de listas sería la MÁS eficaz para conseguirlo? Seleccione la mejor respuesta.


- [ ] Utilice el método sort() para ordenar a los clientes por importe de compra y, a continuación, utilice el corte para extraer los que más gastan.
- [ ] Utilice el método append() para añadir clientes de alto gasto a una nueva lista.
- [ ] Recorrer manualmente la lista mediante un bucle for, comprobando el historial de compras de cada cliente y añadiéndolo a una nueva lista si cumple los criterios.
- [x] Utilice una comprensión de lista para crear una nueva lista que contenga sólo los clientes cuyo historial de compras supere el umbral.

Correcto Las comprensiones de listas están diseñadas para filtrar y transformar listas de forma concisa y eficiente, por lo que son ideales para esta tarea.

